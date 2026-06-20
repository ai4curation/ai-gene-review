#!/usr/bin/env python3
"""Convert BioReason HF protein_catalogue GO sections to PredictionReview YAML.

The HuggingFace catalogue contains BioReason-Pro SFT generations. The structured
GO sections at the end of each generation are converted to
``{GENE}-sft-predictions.yaml`` files and assessed heuristically against local
GOA/AIGR files.

Usage:
    python scripts/hf_to_sft_predictions.py --protein-id P0A9K9 --gene SlyD --species ECOLI
    python scripts/hf_to_sft_predictions.py --batch scripts/batch_proteins.tsv

The batch TSV should have columns: protein_id, gene_symbol, species_code.
"""

import argparse
import re
from pathlib import Path
from typing import Any

import duckdb
import yaml


DB_PATH = Path("data/bioreason-hf/protein_catalogue.ddb")
HF_PARQUET_URLS = [
    "https://huggingface.co/datasets/wanglab/protein_catalogue/resolve/main/data/train-00000-of-00003.parquet",
    "https://huggingface.co/datasets/wanglab/protein_catalogue/resolve/main/data/train-00001-of-00003.parquet",
    "https://huggingface.co/datasets/wanglab/protein_catalogue/resolve/main/data/train-00002-of-00003.parquet",
]
SOURCE_REFERENCE_ID = "doi:10.64898/2026.03.19.712954"


def load_hf_entry(protein_id: str) -> dict[str, str]:
    """Return one HF catalogue row by UniProt accession."""
    if DB_PATH.exists():
        con = duckdb.connect(str(DB_PATH), read_only=True)
        row = con.execute(
            "SELECT protein_id, generation, model, protein, organism "
            "FROM protein_catalogue WHERE protein_id = ?",
            [protein_id],
        ).fetchone()
        con.close()
    else:
        con = duckdb.connect()
        try:
            con.execute("LOAD httpfs;")
        except duckdb.Error:
            con.execute("INSTALL httpfs; LOAD httpfs;")
        row = con.execute(
            "SELECT protein_id, generation, model, protein, organism "
            "FROM read_parquet(?) WHERE protein_id = ?",
            [HF_PARQUET_URLS, protein_id],
        ).fetchone()
        con.close()

    if row is None:
        raise ValueError(f"Protein {protein_id} not found in HF catalogue")

    return {
        "protein_id": row[0],
        "generation": row[1] or "",
        "model": row[2] or "",
        "protein": row[3] or "",
        "organism": row[4] or "",
    }


def extract_go_terms(generation: str) -> list[tuple[str, str, str]]:
    """Extract (GO id, label, term type) from structured GO sections."""
    terms: list[tuple[str, str, str]] = []
    seen: set[tuple[str, str]] = set()
    aspect_map = [
        ("Molecular Function", "GO_MF"),
        ("Biological Process", "GO_BP"),
        ("Cellular Component", "GO_CC"),
    ]

    for aspect, term_type in aspect_map:
        pattern = (
            rf"- {re.escape(aspect)}:\s*\n"
            r"((?:\s+-\s+GO:\d{7}.*(?:\n|$))*)"
        )
        match = re.search(pattern, generation)
        if not match:
            continue
        for line in match.group(1).splitlines():
            term_match = re.match(r"\s+-\s+(GO:\d{7})\s+(.+?)\s*$", line)
            if not term_match:
                continue
            go_id, label = term_match.groups()
            key = (go_id, term_type)
            if key in seen:
                continue
            seen.add(key)
            terms.append((go_id, label.strip(), term_type))

    return terms


def load_goa_terms(goa_file: Path) -> set[str]:
    terms = set()
    if not goa_file.exists():
        return terms
    with goa_file.open() as handle:
        for line in handle:
            parts = line.rstrip("\n").split("\t")
            if len(parts) > 4 and re.match(r"GO:\d{7}", parts[4]):
                terms.add(parts[4])
    return terms


def load_aigr_review(review_file: Path) -> tuple[dict[str, str], set[str]]:
    actions: dict[str, str] = {}
    core_terms: set[str] = set()
    if not review_file.exists():
        return actions, core_terms

    with review_file.open() as handle:
        doc = yaml.safe_load(handle) or {}

    for ann in doc.get("existing_annotations", []):
        go_id = ann.get("term", {}).get("id", "")
        action = ann.get("review", {}).get("action", "")
        if not go_id.startswith("GO:") or not action:
            continue
        if go_id not in actions or action in {"REMOVE", "MARK_AS_OVER_ANNOTATED"}:
            actions[go_id] = action

    for core_function in doc.get("core_functions", []):
        mf = core_function.get("molecular_function", {})
        if mf.get("id", "").startswith("GO:"):
            core_terms.add(mf["id"])
        for slot in ("directly_involved_in", "occurs_in", "locations"):
            for term in core_function.get(slot, []) or []:
                if term.get("id", "").startswith("GO:"):
                    core_terms.add(term["id"])

    return actions, core_terms


def assess_prediction(
    go_id: str,
    goa_terms: set[str],
    actions: dict[str, str],
    core_terms: set[str],
) -> dict[str, Any]:
    action = actions.get(go_id, "")

    if go_id in goa_terms:
        if action in {"REMOVE", "MARK_AS_OVER_ANNOTATED"}:
            return {
                "assessment": "NPI",
                "confidence_score": 0,
                "summary": (
                    f"Term is present in GOA, but the curated AIGR review recommends "
                    f"{action}. The SFT model is reproducing an existing annotation "
                    "that the review rejects or flags as over-annotated."
                ),
            }
        if action == "MODIFY":
            return {
                "assessment": "LSP",
                "confidence_score": 2,
                "summary": (
                    "Term is present in GOA, but the curated AIGR review recommends "
                    "MODIFY to a more appropriate term. The prediction is correct at "
                    "a broad level but less precise than the reviewed annotation."
                ),
            }
        return {
            "assessment": "CNN",
            "confidence_score": 2,
            "summary": "Term is present in GOA. Correct but not novel.",
        }

    if go_id in core_terms:
        return {
            "assessment": "COR",
            "confidence_score": 2,
            "summary": (
                "Term is not present in GOA but is included in AIGR core functions. "
                "The prediction is treated as correct relative to the curated review."
            ),
        }

    if action in {"ACCEPT", "KEEP_AS_NON_CORE"}:
        return {
            "assessment": "COR",
            "confidence_score": 2,
            "summary": (
                f"Term is not present in GOA but the AIGR review action is {action}. "
                "The prediction is treated as correct relative to the curated review."
            ),
        }

    if action in {"REMOVE", "MARK_AS_OVER_ANNOTATED"}:
        return {
            "assessment": "NPI",
            "confidence_score": 0,
            "summary": (
                f"The AIGR review action is {action}. The prediction is likely "
                "incorrect or over-annotated relative to the curated review."
            ),
        }

    return {
        "assessment": "UNC",
        "confidence_score": 1,
        "summary": "Not in GOA and not addressed in the AIGR review. Cannot determine.",
    }


def build_prediction_review(protein_id: str, gene: str, species: str) -> dict[str, Any]:
    entry = load_hf_entry(protein_id)
    terms = extract_go_terms(entry["generation"])
    gene_dir = Path("genes") / species / gene
    goa_terms = load_goa_terms(gene_dir / f"{gene}-goa.tsv")
    actions, core_terms = load_aigr_review(gene_dir / f"{gene}-ai-review.yaml")

    predictions = []
    for go_id, label, term_type in terms:
        predictions.append(
            {
                "source_method": "BioReason-Pro-SFT",
                "source_version": "wanglab/protein_catalogue",
                "source_reference_id": SOURCE_REFERENCE_ID,
                "predicted_term": {"id": go_id, "label": label},
                "predicted_term_type": term_type,
                "review": assess_prediction(go_id, goa_terms, actions, core_terms),
            }
        )

    return {
        "id": protein_id,
        "gene_symbol": gene,
        "taxon": {"id": f"uniprot:{species}", "label": species},
        "status": "COMPLETE",
        "description": (
            f"BioReason-Pro SFT predictions for {gene} ({species}). "
            f"{len(predictions)} GO terms extracted from HF protein_catalogue."
        ),
        "references": [
            {
                "id": SOURCE_REFERENCE_ID,
                "title": "BioReason-Pro (Fallahpour et al. 2026)",
            }
        ],
        "source_documents": ["huggingface.co/datasets/wanglab/protein_catalogue"],
        "predictions": predictions,
    }


def write_prediction_review(
    protein_id: str,
    gene: str,
    species: str,
    output_dir: Path,
    overwrite: bool,
) -> Path:
    outdir = output_dir / species / gene
    outpath = outdir / f"{gene}-sft-predictions.yaml"
    if outpath.exists() and not overwrite:
        print(f"  SKIP {outpath} (already exists)")
        return outpath

    doc = build_prediction_review(protein_id, gene, species)
    outdir.mkdir(parents=True, exist_ok=True)
    with outpath.open("w") as handle:
        yaml.safe_dump(doc, handle, sort_keys=False, allow_unicode=False, width=88)
    print(f"  WROTE {outpath}")
    return outpath


def iter_batch(batch_file: Path) -> list[tuple[str, str, str]]:
    rows = []
    with batch_file.open() as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 3:
                raise ValueError(f"Expected protein_id, gene_symbol, species_code: {line}")
            rows.append((parts[0], parts[1], parts[2]))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protein-id", help="UniProt accession")
    parser.add_argument("--gene", help="Gene symbol")
    parser.add_argument("--species", help="Species code, e.g. ECOLI")
    parser.add_argument("--batch", type=Path, help="TSV with protein_id, gene_symbol, species_code")
    parser.add_argument("--output-dir", type=Path, default=Path("genes"))
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    if args.batch:
        rows = iter_batch(args.batch)
    elif args.protein_id and args.gene and args.species:
        rows = [(args.protein_id, args.gene, args.species)]
    else:
        parser.error("Provide either --batch or --protein-id/--gene/--species")

    for protein_id, gene, species in rows:
        write_prediction_review(
            protein_id=protein_id,
            gene=gene,
            species=species,
            output_dir=args.output_dir,
            overwrite=args.overwrite,
        )


if __name__ == "__main__":
    main()
