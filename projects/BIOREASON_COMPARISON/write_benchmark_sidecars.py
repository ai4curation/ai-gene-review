"""Write benchmark cohort sidecars for the BioReason-Pro comparison project."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any

import yaml


PROJECT_DIR = Path(__file__).resolve().parent
REPO_ROOT = PROJECT_DIR.parents[1]
GENES_DIR = REPO_ROOT / "genes"
REPORTS_DIR = REPO_ROOT / "reports"

CORR_RE = re.compile(r"Correctness\*\*:\s*([0-5])\s*/\s*5", re.IGNORECASE)
COMPL_RE = re.compile(r"Completeness\*\*:\s*([0-5])\s*/\s*5", re.IGNORECASE)


def read_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def gene_review_id(organism: str, gene: str) -> str:
    review_path = GENES_DIR / organism / gene / f"{gene}-ai-review.yaml"
    if not review_path.exists():
        return ""
    return str(read_yaml(review_path).get("id") or "")


def read_rl_gene_list() -> dict[tuple[str, str], dict[str, str]]:
    rows: dict[tuple[str, str], dict[str, str]] = {}
    with (PROJECT_DIR / "genes.csv").open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            key = (row["species"], row["symbol"])
            rows[key] = row
    return rows


def parse_scores(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    correctness = CORR_RE.search(text)
    completeness = COMPL_RE.search(text)
    return (
        correctness.group(1) if correctness else "",
        completeness.group(1) if completeness else "",
    )


def sft_prediction_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(GENES_DIR.glob("*/*/*-sft-predictions.yaml")):
        organism, gene = path.parts[-3], path.parts[-2]
        doc = read_yaml(path)
        predictions = doc.get("predictions", []) or []
        source_versions = sorted(
            {
                str(pred.get("source_version"))
                for pred in predictions
                if pred.get("source_version")
            }
        )
        source_version = ";".join(source_versions)
        rows.append(
            {
                "organism": organism,
                "gene": gene,
                "uniprot_id": doc.get("id") or gene_review_id(organism, gene),
                "source_version": source_version,
                "source_file": rel(path),
                "n_predictions": len(predictions),
            }
        )
    return rows


def sft_narrative_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(GENES_DIR.glob("*/*/*bioreason-sft-review.md")):
        organism, gene = path.parts[-3], path.parts[-2]
        correctness, completeness = parse_scores(path)
        pred_path = GENES_DIR / organism / gene / f"{gene}-sft-predictions.yaml"
        uniprot_id = ""
        if pred_path.exists():
            uniprot_id = str(read_yaml(pred_path).get("id") or "")
        rows.append(
            {
                "organism": organism,
                "gene": gene,
                "uniprot_id": uniprot_id or gene_review_id(organism, gene),
                "source_version": "wanglab/protein_catalogue",
                "source_file": rel(path),
                "correctness": correctness,
                "completeness": completeness,
            }
        )
    return rows


def gogpt_overlap_rows() -> list[dict[str, Any]]:
    path = REPORTS_DIR / "gogpt-comparison-levels.json"
    records = json.loads(path.read_text(encoding="utf-8"))
    rows: list[dict[str, Any]] = []
    for record in records:
        organism = record["organism"]
        gene = record["gene"]
        rows.append(
            {
                "organism": organism,
                "gene": gene,
                "uniprot_id": gene_review_id(organism, gene),
                "source_version": "GO-GPT direct run",
                "source_file": rel(path),
                "n_predictions": record["preds"],
                "goa_overlap": record["goa_overlap"],
                "post_review_overlap": record["post_review_overlap"],
                "core_overlap": record["core_overlap"],
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def main() -> None:
    rl_genes = read_rl_gene_list()
    sft_predictions = sft_prediction_rows()
    sft_narratives = sft_narrative_rows()
    gogpt_overlap = gogpt_overlap_rows()
    rl_keys = set(rl_genes)
    hf_keys = {
        (row["organism"], row["gene"])
        for row in sft_predictions
        if row["source_version"] == "wanglab/protein_catalogue"
    }
    web_keys = {
        (row["organism"], row["gene"])
        for row in sft_predictions
        if row["source_version"] != "wanglab/protein_catalogue"
    }

    benchmark_rows: list[dict[str, Any]] = []

    for (organism, gene), row in sorted(rl_genes.items()):
        review_path = GENES_DIR / organism / gene / f"{gene}-bioreason-rl-review.md"
        correctness, completeness = parse_scores(review_path)
        benchmark_rows.append(
            {
                "benchmark": "argo139_rl_narrative",
                "organism": organism,
                "gene": gene,
                "uniprot_id": row.get("uniprot_id", ""),
                "source_version": "app.bioreason.net/RL",
                "source_file": rel(review_path),
                "reason_included": row.get("reason_included", ""),
                "correctness": correctness,
                "completeness": completeness,
            }
        )

    for row in sft_narratives:
        benchmark_rows.append({"benchmark": "supplement_sft_narrative_hf", **row})

    for row in sft_predictions:
        key = (row["organism"], row["gene"])
        if key in rl_keys:
            benchmark_rows.append({"benchmark": "argo139_sft_terms", **row})
            argo_source = (
                "argo139_sft_terms_hf_catalogue"
                if row["source_version"] == "wanglab/protein_catalogue"
                else "argo139_sft_terms_web_export"
            )
            benchmark_rows.append({"benchmark": argo_source, **row})
        benchmark_rows.append({"benchmark": "supplement_sft_terms_union_184", **row})
        supplement_source = (
            "supplement_sft_terms_hf_catalogue_140"
            if row["source_version"] == "wanglab/protein_catalogue"
            else "supplement_sft_terms_web_export_44"
        )
        benchmark_rows.append({"benchmark": supplement_source, **row})

    for row in gogpt_overlap:
        benchmark_rows.append({"benchmark": "supplement_gogpt_overlap_300", **row})

    fields = [
        "benchmark",
        "organism",
        "gene",
        "uniprot_id",
        "source_version",
        "source_file",
        "reason_included",
        "n_predictions",
        "correctness",
        "completeness",
        "goa_overlap",
        "post_review_overlap",
        "core_overlap",
    ]
    write_csv(PROJECT_DIR / "benchmark-genes.csv", benchmark_rows, fields)

    argo_predictions = [row for row in sft_predictions if (row["organism"], row["gene"]) in rl_keys]
    argo_hf = [
        row
        for row in argo_predictions
        if row["source_version"] == "wanglab/protein_catalogue"
    ]
    argo_web = [
        row
        for row in argo_predictions
        if row["source_version"] != "wanglab/protein_catalogue"
    ]
    cohort_rows = [
        {
            "benchmark": "argo139_rl_narrative",
            "n_genes": len(rl_genes),
            "n_predictions": "",
            "source": "BioReason-Pro RL web export plus AIGR comparison review",
            "description": "ARGO139 primary narrative-quality benchmark; member list is genes.csv.",
        },
        {
            "benchmark": "argo139_sft_terms",
            "n_genes": len({(row["organism"], row["gene"]) for row in argo_predictions}),
            "n_predictions": sum(row["n_predictions"] for row in argo_predictions),
            "source": "HuggingFace wanglab/protein_catalogue plus BioReason-Pro SFT web export",
            "description": f"ARGO139 SFT term-prediction review: {len(argo_hf)} HF-catalogue genes and {len(argo_web)} web-export genes.",
        },
        {
            "benchmark": "argo139_sft_terms_hf_catalogue",
            "n_genes": len(argo_hf),
            "n_predictions": sum(row["n_predictions"] for row in argo_hf),
            "source": "HuggingFace wanglab/protein_catalogue SFT term predictions",
            "description": "ARGO139 genes available in the cleaner HF catalogue source.",
        },
        {
            "benchmark": "argo139_sft_terms_web_export",
            "n_genes": len(argo_web),
            "n_predictions": sum(row["n_predictions"] for row in argo_web),
            "source": "BioReason-Pro SFT web export",
            "description": "ARGO139 genes absent from the HF catalogue; web export includes full ancestor hierarchy.",
        },
        {
            "benchmark": "supplement_sft_narrative_hf",
            "n_genes": len(sft_narratives),
            "n_predictions": "",
            "source": "HuggingFace wanglab/protein_catalogue SFT outputs",
            "description": "Supplementary SFT narrative cross-check; 44/45 files have parseable 1-5 scores.",
        },
        {
            "benchmark": "supplement_sft_terms_hf_catalogue_140",
            "n_genes": sum(
                1
                for row in sft_predictions
                if row["source_version"] == "wanglab/protein_catalogue"
            ),
            "n_predictions": sum(
                row["n_predictions"]
                for row in sft_predictions
                if row["source_version"] == "wanglab/protein_catalogue"
            ),
            "source": "HuggingFace wanglab/protein_catalogue SFT term predictions",
            "description": f"Supplemental cleaner leaf-term source view; includes {len(hf_keys & rl_keys)} ARGO139 genes plus {len(hf_keys - rl_keys)} additional HF-only genes.",
        },
        {
            "benchmark": "supplement_sft_terms_web_export_44",
            "n_genes": sum(
                1
                for row in sft_predictions
                if row["source_version"] != "wanglab/protein_catalogue"
            ),
            "n_predictions": sum(
                row["n_predictions"]
                for row in sft_predictions
                if row["source_version"] != "wanglab/protein_catalogue"
            ),
            "source": "BioReason-Pro SFT web export",
            "description": f"SFT web-export predictions for {len(web_keys & rl_keys)} ARGO139 genes absent from the HF catalogue; includes full ancestor hierarchy.",
        },
        {
            "benchmark": "supplement_sft_terms_union_184",
            "n_genes": len({(row["organism"], row["gene"]) for row in sft_predictions}),
            "n_predictions": sum(row["n_predictions"] for row in sft_predictions),
            "source": "HuggingFace wanglab/protein_catalogue plus BioReason-Pro SFT web export",
            "description": f"Combined SFT term-prediction review: {len(rl_keys)} genes in ARGO139 plus {len(hf_keys - rl_keys)} HF-only genes; source partitions are listed separately.",
        },
        {
            "benchmark": "supplement_gogpt_overlap_300",
            "n_genes": len(gogpt_overlap),
            "n_predictions": sum(row["n_predictions"] for row in gogpt_overlap),
            "source": "reports/gogpt-comparison-levels.json",
            "description": "Separate GO-GPT overlap review against raw GOA, post-review GOA, and AIGR core functions.",
        },
    ]
    write_csv(
        PROJECT_DIR / "benchmark-cohorts.csv",
        cohort_rows,
        ["benchmark", "n_genes", "n_predictions", "source", "description"],
    )

    print(f"wrote {PROJECT_DIR / 'benchmark-cohorts.csv'}")
    print(f"wrote {PROJECT_DIR / 'benchmark-genes.csv'}")


if __name__ == "__main__":
    main()
