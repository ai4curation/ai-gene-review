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

from ai_gene_review.bioreason_ontology import FROZEN_GO_ADAPTER, get_go_adapter


DB_PATH = Path("data/bioreason-hf/protein_catalogue.ddb")
HF_PARQUET_URLS = [
    "https://huggingface.co/datasets/wanglab/protein_catalogue/resolve/main/data/train-00000-of-00003.parquet",
    "https://huggingface.co/datasets/wanglab/protein_catalogue/resolve/main/data/train-00001-of-00003.parquet",
    "https://huggingface.co/datasets/wanglab/protein_catalogue/resolve/main/data/train-00002-of-00003.parquet",
]
SOURCE_REFERENCE_ID = "doi:10.64898/2026.03.19.712954"
DEFAULT_ONTOLOGY_ADAPTER = FROZEN_GO_ADAPTER
POSITIVE_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE"}
NEGATIVE_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
ONTOLOGY_NOTE_MARKER = "[ONTOLOGY_LABEL_AUDIT]"


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
    terms: set[str] = set()
    if not goa_file.exists():
        return terms
    with goa_file.open() as handle:
        for line in handle:
            parts = line.rstrip("\n").split("\t")
            if len(parts) > 4 and re.fullmatch(r"GO:\d{7}", parts[4]):
                terms.add(parts[4])
    return terms


def load_aigr_review(review_file: Path) -> tuple[dict[str, set[str]], set[str]]:
    """Load all exact AIGR actions and authored core-function GO terms."""
    actions: dict[str, set[str]] = {}
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
        actions.setdefault(go_id, set()).add(action)

    def add_term_values(value: Any) -> None:
        values = value if isinstance(value, list) else [value]
        for term in values:
            if isinstance(term, dict) and term.get("id", "").startswith("GO:"):
                core_terms.add(term["id"])

    for core_function in doc.get("core_functions", []):
        for slot in (
            "molecular_function",
            "contributes_to_molecular_function",
            "directly_involved_in",
            "occurs_in",
            "locations",
            "in_complex",
        ):
            add_term_values(core_function.get(slot))

    return actions, core_terms


def assess_prediction(
    go_id: str,
    goa_terms: set[str],
    actions: dict[str, set[str]],
    core_terms: set[str],
) -> dict[str, Any]:
    exact_actions = actions.get(go_id, set())

    if exact_actions and exact_actions <= NEGATIVE_ACTIONS:
        return {
            "assessment": "NPI",
            "confidence_score": 0,
            "summary": (
                "The exact AIGR actions are "
                f"{', '.join(sorted(exact_actions))}. The SFT model is reproducing "
                "an annotation that the current review rejects or flags as "
                "over-annotated."
            ),
        }

    if exact_actions & POSITIVE_ACTIONS:
        return {
            "assessment": "CNN",
            "confidence_score": 2,
            "summary": (
                "The exact term is already present in AIGR with a positive action "
                f"({', '.join(sorted(exact_actions & POSITIVE_ACTIONS))}). Correct "
                "but not novel."
            ),
        }

    if go_id in goa_terms and exact_actions == {"MODIFY"}:
        return {
            "assessment": "LSP",
            "confidence_score": 2,
            "summary": (
                "The term is in GOA, but AIGR recommends MODIFY to a more appropriate "
                "term. It is retained as a less-precise prediction."
            ),
        }

    if go_id in goa_terms and not exact_actions:
        return {
            "assessment": "CNN",
            "confidence_score": 2,
            "summary": "The exact term is present in current GOA. Correct but not novel.",
        }

    if not exact_actions and go_id in core_terms:
        return {
            "assessment": "COR",
            "confidence_score": 2,
            "summary": (
                "The term is absent from current GOA but present in AIGR core "
                "functions. It is treated as correct relative to the local review."
            ),
        }

    return {
        "assessment": "UNC",
        "confidence_score": 1,
        "summary": (
            "The term is not resolved by an unambiguous exact current-GOA/AIGR match. "
            "Manual assessment is required."
        ),
    }


def ontology_label_note(
    go_id: str,
    raw_label: str,
    ontology_adapter: Any,
) -> str | None:
    """Return an explicit raw-pair warning without normalizing model output."""
    canonical = ontology_adapter.label(go_id)
    if canonical is None:
        return (
            f"{ONTOLOGY_NOTE_MARKER} {go_id} does not resolve in the configured "
            f"current GO ontology. The raw model label '{raw_label}' is retained for "
            "provenance and the unresolved identifier is explicitly flagged."
        )

    def normalize(value: str) -> str:
        return " ".join(value.split()).casefold()

    if normalize(raw_label) == normalize(canonical):
        return None
    aliases = {
        normalize(alias) for alias in ontology_adapter.entity_aliases(go_id) if alias
    }
    if normalize(raw_label) in aliases:
        return None
    return (
        f"{ONTOLOGY_NOTE_MARKER} Raw model pair mismatch: {go_id} resolves to "
        f"'{canonical}', not '{raw_label}'. The raw ID and label are retained for "
        "provenance; the assessment applies to the GO ID and explicitly flags the "
        "label error."
    )


def build_prediction_review(
    protein_id: str,
    gene: str,
    species: str,
    ontology_adapter: Any | None = None,
) -> dict[str, Any]:
    entry = load_hf_entry(protein_id)
    terms = extract_go_terms(entry["generation"])
    gene_dir = Path("genes") / species / gene
    goa_terms = load_goa_terms(gene_dir / f"{gene}-goa.tsv")
    actions, core_terms = load_aigr_review(gene_dir / f"{gene}-ai-review.yaml")

    predictions = []
    for go_id, label, term_type in terms:
        review = assess_prediction(go_id, goa_terms, actions, core_terms)
        if ontology_adapter is not None:
            note = ontology_label_note(go_id, label, ontology_adapter)
            if note:
                review["summary"] = f"{review['summary']} {note}"
        predictions.append(
            {
                "source_method": "BioReason-Pro-SFT",
                "source_version": "wanglab/protein_catalogue",
                "source_reference_id": SOURCE_REFERENCE_ID,
                "predicted_term": {"id": go_id, "label": label},
                "predicted_term_type": term_type,
                "review": review,
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
    ontology_adapter: Any | None = None,
) -> Path:
    outdir = output_dir / species / gene
    outpath = outdir / f"{gene}-sft-predictions.yaml"
    if outpath.exists() and not overwrite:
        print(f"  SKIP {outpath} (already exists)")
        return outpath

    doc = build_prediction_review(protein_id, gene, species, ontology_adapter)
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
    parser.add_argument("--ontology-adapter", default=DEFAULT_ONTOLOGY_ADAPTER)
    parser.add_argument(
        "--skip-ontology",
        action="store_true",
        help="Skip GO ID/label validation",
    )
    args = parser.parse_args()

    if args.batch:
        rows = iter_batch(args.batch)
    elif args.protein_id and args.gene and args.species:
        rows = [(args.protein_id, args.gene, args.species)]
    else:
        parser.error("Provide either --batch or --protein-id/--gene/--species")

    if args.skip_ontology:
        ontology_adapter = None
    else:
        ontology_adapter = get_go_adapter(args.ontology_adapter)

    for protein_id, gene, species in rows:
        write_prediction_review(
            protein_id=protein_id,
            gene=gene,
            species=species,
            output_dir=args.output_dir,
            overwrite=args.overwrite,
            ontology_adapter=ontology_adapter,
        )


if __name__ == "__main__":
    main()
