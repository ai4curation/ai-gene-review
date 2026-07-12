"""Write benchmark cohort sidecars for the BioReason-Pro comparison project."""
from __future__ import annotations

import csv
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml


PROJECT_DIR = Path(__file__).resolve().parent
REPO_ROOT = PROJECT_DIR.parents[1]
GENES_DIR = REPO_ROOT / "genes"
REPORTS_DIR = REPO_ROOT / "reports"
POLICY_PATH = PROJECT_DIR / "benchmark-policy.yaml"

CORR_RE = re.compile(r"Correctness\*\*:\s*([1-5])\s*/\s*5", re.IGNORECASE)
COMPL_RE = re.compile(r"Completeness\*\*:\s*([1-5])\s*/\s*5", re.IGNORECASE)
BIOREASON_SEQUENCE_RE = re.compile(
    r"\*\*Sequence:\*\*\s*```\s*([A-Z\s]+?)\s*```", re.MULTILINE
)
UNIPROT_SEQUENCE_RE = re.compile(
    r"^SQ\s+SEQUENCE\s+\d+ AA;.*?\n(.*?)\n//", re.MULTILINE | re.DOTALL
)
UNIPROT_ACCESSION_RE = re.compile(r"^AC\s+([^;]+);", re.MULTILINE)
EXPORT_DATE_RE = re.compile(r"^\*Exported on (.+?)\*$", re.MULTILINE)
REVIEW_STATUS_RE = re.compile(r"^status:\s*([A-Z_]+)\s*$", re.MULTILINE)


@lru_cache(maxsize=None)
def read_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


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


def extract_bioreason_sequence(path: Path) -> str:
    match = BIOREASON_SEQUENCE_RE.search(path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError(f"No BioReason sequence block found in {path}")
    return "".join(match.group(1).split())


def extract_export_date(path: Path) -> str:
    match = EXPORT_DATE_RE.search(path.read_text(encoding="utf-8"))
    return match.group(1) if match else ""


def extract_markdown_section(path: Path, heading: str) -> str | None:
    pattern = re.compile(
        rf"^### {re.escape(heading)}\s*$\n(.*?)(?=^### |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(path.read_text(encoding="utf-8"))
    if not match:
        return None
    return match.group(1).strip() + "\n"


def extract_uniprot_record(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    accession = UNIPROT_ACCESSION_RE.search(text)
    sequence = UNIPROT_SEQUENCE_RE.search(text)
    if not accession or not sequence:
        raise ValueError(f"Incomplete UniProt flat file: {path}")
    return accession.group(1), "".join(re.findall(r"[A-Z]+", sequence.group(1)))


def extract_review_status(path: Path) -> str:
    match = REVIEW_STATUS_RE.search(path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError(f"No review status found in {path}")
    return match.group(1)


def latest_goa_date(path: Path) -> str:
    with path.open(newline="", encoding="utf-8") as handle:
        dates = [row.get("DATE", "") for row in csv.DictReader(handle, delimiter="\t")]
    return max((date for date in dates if date), default="")


def goa_ids(path: Path) -> set[str]:
    """Return exact GO IDs from a committed QuickGO TSV."""
    with path.open(newline="", encoding="utf-8") as handle:
        return {
            identifier
            for row in csv.DictReader(handle, delimiter="\t")
            if (identifier := str(row.get("GO TERM") or "")).startswith("GO:")
        }


def rl_quality_rows(
    rl_genes: dict[tuple[str, str], dict[str, str]], policy: dict[str, Any]
) -> list[dict[str, Any]]:
    cohort_policy = policy["cohorts"]["argo139_rl_narrative"]
    exclusions = {
        (item["species"], item["symbol"]): item
        for item in cohort_policy.get("performance_exclusions", [])
    }
    sequence_limit = int(cohort_policy["input_quality"]["model_sequence_limit"])
    rows: list[dict[str, Any]] = []

    for (organism, gene), source_row in sorted(rl_genes.items()):
        gene_dir = GENES_DIR / organism / gene
        prediction_path = gene_dir / f"{gene}-bioreason-rl-predictions.md"
        review_path = gene_dir / f"{gene}-bioreason-rl-review.md"
        reference_path = gene_dir / f"{gene}-ai-review.yaml"
        uniprot_path = gene_dir / f"{gene}-uniprot.txt"
        goa_path = gene_dir / f"{gene}-goa.tsv"
        input_sequence = extract_bioreason_sequence(prediction_path)
        interpro_input = extract_markdown_section(prediction_path, "InterPro Domains")
        gogpt_input = extract_markdown_section(prediction_path, "GO Terms")
        cached_accession, reference_sequence = extract_uniprot_record(uniprot_path)
        exclusion = exclusions.get((organism, gene))

        if exclusion:
            input_quality = exclusion["reason"]
        elif input_sequence == reference_sequence:
            input_quality = "FULL_LENGTH_MATCH"
        elif (
            len(input_sequence) == sequence_limit
            and len(reference_sequence) > sequence_limit
            and reference_sequence.startswith(input_sequence)
        ):
            input_quality = "TRUNCATED_AT_MODEL_LIMIT"
        else:
            input_quality = "SEQUENCE_MISMATCH"

        rows.append(
            {
                "organism": organism,
                "gene": gene,
                "expected_uniprot_id": source_row.get("uniprot_id", ""),
                "cached_uniprot_id": cached_accession,
                "reference_status": extract_review_status(reference_path),
                "performance_included": "false" if exclusion else "true",
                "exclusion_reason": exclusion["reason"] if exclusion else "",
                "input_quality": input_quality,
                "input_sequence_length": len(input_sequence),
                "reference_sequence_length": len(reference_sequence),
                "model_version": cohort_policy["model_version"],
                "export_timestamp": extract_export_date(prediction_path),
                "goa_latest_annotation_date": latest_goa_date(goa_path),
                "prediction_sha256": sha256(prediction_path),
                "interpro_input_present": str(interpro_input is not None).lower(),
                "interpro_input_count": len(
                    set(re.findall(r"IPR\d{6}", interpro_input or ""))
                ),
                "interpro_input_sha256": (
                    sha256_text(interpro_input) if interpro_input is not None else ""
                ),
                "gogpt_input_present": str(gogpt_input is not None).lower(),
                "gogpt_input_term_count": len(
                    re.findall(r"GO:\d{7}", gogpt_input or "")
                ),
                "gogpt_input_sha256": (
                    sha256_text(gogpt_input) if gogpt_input is not None else ""
                ),
                "review_sha256": sha256(review_path),
                "reference_sha256": sha256(reference_path),
                "uniprot_sha256": sha256(uniprot_path),
                "goa_sha256": sha256(goa_path),
            }
        )
    return rows


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
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def average_ranks(values: list[int]) -> list[float]:
    order = sorted(range(len(values)), key=values.__getitem__)
    ranks = [0.0] * len(values)
    start = 0
    while start < len(order):
        end = start + 1
        while end < len(order) and values[order[end]] == values[order[start]]:
            end += 1
        rank = (start + 1 + end) / 2
        for index in order[start:end]:
            ranks[index] = rank
        start = end
    return ranks


def pearson(values_x: list[float], values_y: list[float]) -> float:
    mean_x = sum(values_x) / len(values_x)
    mean_y = sum(values_y) / len(values_y)
    numerator = sum(
        (value_x - mean_x) * (value_y - mean_y)
        for value_x, value_y in zip(values_x, values_y)
    )
    denominator = math.sqrt(
        sum((value - mean_x) ** 2 for value in values_x)
        * sum((value - mean_y) ** 2 for value in values_y)
    )
    return numerator / denominator


def score_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    correctness = [int(row["correctness"]) for row in rows]
    completeness = [int(row["completeness"]) for row in rows]
    return {
        "n": len(rows),
        "mean_correctness": round(sum(correctness) / len(correctness), 6),
        "mean_completeness": round(sum(completeness) / len(completeness), 6),
        "correctness_distribution": dict(sorted(Counter(correctness).items())),
        "completeness_distribution": dict(sorted(Counter(completeness).items())),
    }


def assessment_summary(
    pattern: str,
    *,
    keys: set[tuple[str, str]] | None = None,
    source_version: str | None = None,
    exclude_source_version: str | None = None,
) -> dict[str, Any]:
    assessments: Counter[str] = Counter()
    statuses: Counter[str] = Counter()
    genes: set[tuple[str, str]] = set()
    for path in sorted(GENES_DIR.glob(pattern)):
        organism, gene = path.parts[-3], path.parts[-2]
        if keys is not None and (organism, gene) not in keys:
            continue
        document = read_yaml(path)
        included = False
        for prediction in document.get("predictions", []) or []:
            if source_version and prediction.get("source_version") != source_version:
                continue
            if (
                exclude_source_version
                and prediction.get("source_version") == exclude_source_version
            ):
                continue
            assessment = (prediction.get("review") or {}).get("assessment")
            if assessment:
                assessments[str(assessment)] += 1
                included = True
        if included:
            genes.add((organism, gene))
            statuses[str(document.get("status") or "")] += 1
    return {
        "n_genes": len(genes),
        "n_predictions": sum(assessments.values()),
        "assessment_distribution": dict(sorted(assessments.items())),
        "document_status_distribution": dict(sorted(statuses.items())),
    }


def gogpt_overlap_summary() -> dict[str, Any]:
    """Summarize the reproducible 300-gene GO-GPT reference-layer comparison."""
    records = json.loads(
        (REPORTS_DIR / "gogpt-comparison-levels.json").read_text(encoding="utf-8")
    )
    levels = {
        "goa": ("goa_terms", "goa_overlap"),
        "post_review": ("post_review_terms", "post_review_overlap"),
        "core": ("core_terms", "core_overlap"),
    }
    predicted = sum(int(record["preds"]) for record in records)
    summary: dict[str, Any] = {
        "n_genes": len(records),
        "n_predictions": predicted,
    }
    for level, (reference_field, overlap_field) in levels.items():
        reference = sum(int(record[reference_field]) for record in records)
        overlap = sum(int(record[overlap_field]) for record in records)
        summary[level] = {
            "n_reference_terms": reference,
            "n_overlap": overlap,
            "prediction_overlap_rate": round(overlap / predicted, 6),
        }
    return summary


def argo95_exact_goa_summary(
    keys: set[tuple[str, str]],
) -> dict[str, int]:
    """Count exact frozen-GOA membership for final ARGO95 CNN/COR calls."""
    cnn_exact = 0
    cnn_other_basis = 0
    cor_in_goa = 0
    for path in sorted(GENES_DIR.glob("*/*/*-sft-predictions.yaml")):
        organism, gene = path.parts[-3], path.parts[-2]
        if (organism, gene) not in keys:
            continue
        exact_ids = goa_ids(path.parent / f"{gene}-goa.tsv")
        for prediction in read_yaml(path).get("predictions", []) or []:
            if prediction.get("source_version") != "wanglab/protein_catalogue":
                continue
            identifier = str((prediction.get("predicted_term") or {}).get("id") or "")
            assessment = str((prediction.get("review") or {}).get("assessment") or "")
            if assessment == "CNN":
                if identifier in exact_ids:
                    cnn_exact += 1
                else:
                    cnn_other_basis += 1
            elif assessment == "COR" and identifier in exact_ids:
                cor_in_goa += 1
    return {
        "cnn_exact_frozen_goa": cnn_exact,
        "cnn_other_established_basis": cnn_other_basis,
        "cor_exact_frozen_goa": cor_in_goa,
    }


def ontology_pair_audit_summary() -> dict[str, int]:
    path = PROJECT_DIR / "argo95-ontology-pair-adjudication.tsv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    return {
        "n_reviewed": len(rows),
        "n_changed": sum(row["change_required"] == "true" for row in rows),
    }


def build_metrics(
    rl_genes: dict[tuple[str, str], dict[str, str]],
    quality_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    quality_by_key = {
        (row["organism"], row["gene"]): row for row in quality_rows
    }
    performance_rows: list[dict[str, Any]] = []
    per_organism: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for organism, gene in sorted(rl_genes):
        review_path = GENES_DIR / organism / gene / f"{gene}-bioreason-rl-review.md"
        correctness, completeness = parse_scores(review_path)
        if not correctness or not completeness:
            raise ValueError(f"Out-of-range or missing narrative score: {review_path}")
        row = {
            "organism": organism,
            "gene": gene,
            "correctness": correctness,
            "completeness": completeness,
        }
        if quality_by_key[(organism, gene)]["performance_included"] == "true":
            performance_rows.append(row)
            per_organism[organism].append(row)

    correctness = [int(row["correctness"]) for row in performance_rows]
    completeness = [int(row["completeness"]) for row in performance_rows]
    rl_summary = score_summary(performance_rows)
    rl_summary.update(
        {
            "n_collected": len(rl_genes),
            "n_excluded": len(rl_genes) - len(performance_rows),
            "pearson_correctness_completeness": round(
                pearson(correctness, completeness), 6
            ),
            "spearman_correctness_completeness": round(
                pearson(average_ranks(correctness), average_ranks(completeness)), 6
            ),
            "input_quality_distribution": dict(
                sorted(Counter(row["input_quality"] for row in quality_rows).items())
            ),
            "reference_status_distribution": dict(
                sorted(Counter(row["reference_status"] for row in quality_rows).items())
            ),
            "per_organism": {
                organism: score_summary(rows)
                for organism, rows in sorted(per_organism.items())
            },
        }
    )

    sft_narrative_rows: list[dict[str, Any]] = []
    for path in sorted(GENES_DIR.glob("*/*/*bioreason-sft-review.md")):
        correctness, completeness = parse_scores(path)
        if not correctness or not completeness:
            raise ValueError(f"Out-of-range or missing narrative score: {path}")
        sft_narrative_rows.append(
            {"correctness": correctness, "completeness": completeness}
        )

    argo95_summary = assessment_summary(
        "*/*/*-sft-predictions.yaml",
        keys=set(rl_genes),
        source_version="wanglab/protein_catalogue",
    )
    argo95_summary.update(argo95_exact_goa_summary(set(rl_genes)))
    argo95_summary["ontology_pair_adjudication"] = ontology_pair_audit_summary()

    return {
        "policy_release": read_yaml(POLICY_PATH)["benchmark_release"],
        "rl_narrative": rl_summary,
        "sft_narrative_supplement": score_summary(sft_narrative_rows),
        "argo95_sft_terms": argo95_summary,
        "argo139_gogpt_terms": assessment_summary(
            "*/*/*-gogpt-leaf-predictions.yaml", keys=set(rl_genes)
        ),
        "supplement_sft_terms_argo139_mixed_sources": assessment_summary(
            "*/*/*-sft-predictions.yaml", keys=set(rl_genes)
        ),
        "supplement_sft_terms_hf_catalogue_all": assessment_summary(
            "*/*/*-sft-predictions.yaml",
            source_version="wanglab/protein_catalogue",
        ),
        "supplement_sft_terms_web_export": assessment_summary(
            "*/*/*-sft-predictions.yaml",
            exclude_source_version="wanglab/protein_catalogue",
        ),
        "supplement_sft_terms_union_all": assessment_summary(
            "*/*/*-sft-predictions.yaml"
        ),
        "supplement_gogpt_overlap_300": gogpt_overlap_summary(),
    }


def main(output_dir: Path = PROJECT_DIR) -> None:
    policy = read_yaml(POLICY_PATH)
    rl_genes = read_rl_gene_list()
    quality_rows = rl_quality_rows(rl_genes, policy)
    quality_by_key = {
        (row["organism"], row["gene"]): row for row in quality_rows
    }
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
        quality = quality_by_key[(organism, gene)]
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
                "performance_included": quality["performance_included"],
                "exclusion_reason": quality["exclusion_reason"],
                "input_quality": quality["input_quality"],
                "input_sequence_length": quality["input_sequence_length"],
                "reference_sequence_length": quality["reference_sequence_length"],
                "reference_status": quality["reference_status"],
            }
        )

    for row in sft_narratives:
        benchmark_rows.append({"benchmark": "supplement_sft_narrative_hf", **row})

    for row in sft_predictions:
        key = (row["organism"], row["gene"])
        if key in rl_keys:
            if row["source_version"] == "wanglab/protein_catalogue":
                benchmark_rows.append({"benchmark": "argo95_sft_terms", **row})
            benchmark_rows.append({"benchmark": "supplement_sft_terms_argo139_mixed_sources", **row})
        benchmark_rows.append({"benchmark": "supplement_sft_terms_union_all", **row})
        supplement_source = (
            "supplement_sft_terms_hf_catalogue_all"
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
        "performance_included",
        "exclusion_reason",
        "input_quality",
        "input_sequence_length",
        "reference_sequence_length",
        "reference_status",
    ]
    write_csv(output_dir / "benchmark-genes.csv", benchmark_rows, fields)

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
            "n_performance_genes": sum(
                row["performance_included"] == "true" for row in quality_rows
            ),
            "n_flagged_inputs": sum(
                row["input_quality"] != "FULL_LENGTH_MATCH" for row in quality_rows
            ),
            "n_predictions": "",
            "source": "BioReason-Pro RL web export plus AIGR comparison review",
            "description": "ARGO139 collected narrative cohort; performance summaries exclude documented wrong-input cases and stratify truncated inputs.",
        },
        {
            "benchmark": "argo95_sft_terms",
            "n_genes": len(argo_hf),
            "n_predictions": sum(row["n_predictions"] for row in argo_hf),
            "source": "HuggingFace wanglab/protein_catalogue SFT term predictions",
            "description": "ARGO95 primary SFT term-prediction benchmark: ARGO139 genes available in the cleaner HF catalogue source.",
        },
        {
            "benchmark": "supplement_sft_terms_argo139_mixed_sources",
            "n_genes": len({(row["organism"], row["gene"]) for row in argo_predictions}),
            "n_predictions": sum(row["n_predictions"] for row in argo_predictions),
            "source": "HuggingFace wanglab/protein_catalogue plus BioReason-Pro SFT web export",
            "description": f"Supplemental mixed-source ARGO139 SFT diagnostic: {len(argo_hf)} HF-catalogue genes and {len(argo_web)} web-export genes; not a primary benchmark.",
        },
        {
            "benchmark": "supplement_sft_narrative_hf",
            "n_genes": len(sft_narratives),
            "n_predictions": "",
            "source": "HuggingFace wanglab/protein_catalogue SFT outputs",
            "description": "Supplementary SFT narrative cross-check; all 45 files have parseable 1-5 scores.",
        },
        {
            "benchmark": "supplement_sft_terms_hf_catalogue_all",
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
            "description": f"Supplemental all-HF source view; includes {len(hf_keys & rl_keys)} ARGO139 genes plus {len(hf_keys - rl_keys)} additional HF-only genes.",
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
            "benchmark": "supplement_sft_terms_union_all",
            "n_genes": len({(row["organism"], row["gene"]) for row in sft_predictions}),
            "n_predictions": sum(row["n_predictions"] for row in sft_predictions),
            "source": "HuggingFace wanglab/protein_catalogue plus BioReason-Pro SFT web export",
            "description": f"All available SFT term-prediction reviews: {len(rl_keys)} genes in ARGO139 plus {len(hf_keys - rl_keys)} HF-only genes; source partitions are listed separately.",
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
        output_dir / "benchmark-cohorts.csv",
        cohort_rows,
        [
            "benchmark",
            "n_genes",
            "n_performance_genes",
            "n_flagged_inputs",
            "n_predictions",
            "source",
            "description",
        ],
    )

    write_csv(
        output_dir / "benchmark-quality.csv",
        quality_rows,
        [
            "organism",
            "gene",
            "expected_uniprot_id",
            "cached_uniprot_id",
            "reference_status",
            "performance_included",
            "exclusion_reason",
            "input_quality",
            "input_sequence_length",
            "reference_sequence_length",
            "model_version",
            "export_timestamp",
            "goa_latest_annotation_date",
            "prediction_sha256",
            "interpro_input_present",
            "interpro_input_count",
            "interpro_input_sha256",
            "gogpt_input_present",
            "gogpt_input_term_count",
            "gogpt_input_sha256",
            "review_sha256",
            "reference_sha256",
            "uniprot_sha256",
            "goa_sha256",
        ],
    )

    metrics = build_metrics(rl_genes, quality_rows)
    (output_dir / "benchmark-metrics.json").write_text(
        json.dumps(metrics, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    print(f"wrote {output_dir / 'benchmark-cohorts.csv'}")
    print(f"wrote {output_dir / 'benchmark-genes.csv'}")
    print(f"wrote {output_dir / 'benchmark-quality.csv'}")
    print(f"wrote {output_dir / 'benchmark-metrics.json'}")


if __name__ == "__main__":
    main()
