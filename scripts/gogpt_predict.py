#!/usr/bin/env python3
"""Run GO-GPT or refresh GO-GPT reviews derived from BioReason exports.

Inference usage:
    python scripts/gogpt_predict.py <organism> <gene> [--compare]

Refresh the committed BioReason web-export cohort without rerunning the model:
    python scripts/gogpt_predict.py --refresh-web-exports
    python scripts/gogpt_predict.py --check-web-exports

The refresh mode treats the raw ``*-bioreason-rl-predictions.md`` files as
immutable model provenance. It reparses their GO-GPT terms, removes generic and
non-leaf terms with GO IS_A relationships, normalizes labels with GO, and joins
exact term IDs to the current AIGR annotation decisions.
"""

import argparse
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable

import yaml

from ai_gene_review.bioreason_ontology import FROZEN_GO_ADAPTER, get_go_adapter


BIOREASON_REF = "doi:10.64898/2026.03.19.712954"
BIOREASON_TITLE = (
    "BioReason-Pro: Advancing Protein Function Prediction with Multimodal "
    "Biological Reasoning (Fallahpour et al. 2026)"
)
MANUAL_ASSESSMENT_MARKER = "Requires manual assessment"
ONTOLOGY_LABEL_AUDIT_MARKER = "[ONTOLOGY_LABEL_AUDIT]"

ROOT_TERMS = {
    "GO:0003674",  # molecular_function
    "GO:0008150",  # biological_process
    "GO:0005575",  # cellular_component
}

# Root and upper-level terms that do not constitute useful leaf predictions.
# GO:0005622 is retained in old exports after its obsoletion severed the IS_A
# path that previously made it an ancestor; it remains too generic to review.
GENERIC_TERMS = ROOT_TERMS | {
    "GO:0005488",
    "GO:0009987",
    "GO:0008152",
    "GO:0044237",
    "GO:0071704",
    "GO:0044238",
    "GO:0006807",
    "GO:0044260",
    "GO:0043170",
    "GO:0097159",
    "GO:1901363",
    "GO:0005622",
}

ASPECT_MAP = {
    "MF": "GO_MF",
    "BP": "GO_BP",
    "CC": "GO_CC",
}

ASPECT_FULL = {
    "MF": "molecular_function",
    "BP": "biological_process",
    "CC": "cellular_component",
}

BIOREASON_ASPECTS = {
    "Molecular Function": "MF",
    "Biological Process": "BP",
    "Cellular Component": "CC",
}

POSITIVE_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE"}
NEGATIVE_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
NEGATED_ACTION_PREFIX = "NOT:"
CONFIDENCE_BY_ASSESSMENT = {
    "COR": 2,
    "CNN": 2,
    "LSP": 2,
    "UNC": 1,
    "PLI": 0,
    "NPI": 0,
    "REP": 0,
}

GO_ID_RE = re.compile(r"GO:\d{7}")
GO_LABEL_PAIR_RE = re.compile(r"(?:^|,\s*)(.+?)\s*\(`(GO:\d{7})`\)")
GENERATED_SUMMARY_PREFIXES = (
    "Deterministic exact-match comparison:",
    "No deterministic exact-action match",
)


def get_organism_name(organism_code: str, organism_mapper: Any) -> str:
    """Map an AIGR organism code to a GO-GPT organism name."""
    code_map = {
        "human": "Homo sapiens",
        "mouse": "Mus musculus",
        "rat": "Rattus norvegicus",
        "yeast": "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)",
        "worm": "Caenorhabditis elegans",
        "DROME": "Drosophila melanogaster",
        "ARATH": "Arabidopsis thaliana",
        "PSEPK": (
            "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / "
            "NCIMB 11950 / KT2440)"
        ),
        "ECOLI": "Escherichia coli (strain K12)",
        "PSEAE": (
            "Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP "
            "104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1)"
        ),
        "BACSU": "Bacillus subtilis (strain 168)",
    }
    if organism_code in code_map:
        return code_map[organism_code]
    for name in organism_mapper.organism_to_idx:
        if organism_code.lower() in name.lower():
            return name
    return organism_code


def extract_sequence(uniprot_file: Path) -> str:
    """Extract a protein sequence from a UniProt flat file."""
    in_sequence = False
    sequence = []
    for line in uniprot_file.read_text().splitlines():
        if line.startswith("SQ"):
            in_sequence = True
            continue
        if in_sequence:
            if line.startswith("//"):
                break
            sequence.append(line.strip().replace(" ", ""))
    return "".join(sequence)


def extract_accession(uniprot_file: Path) -> str:
    """Extract the primary UniProt accession from a flat file."""
    for line in uniprot_file.read_text().splitlines():
        if line.startswith("AC"):
            return line.split()[1].rstrip(";")
    return ""


def load_review_decisions(review_file: Path) -> dict[str, set[str]]:
    """Load exact GO ID to AIGR action mappings from existing annotations."""
    review = yaml.safe_load(review_file.read_text()) or {}
    decisions: dict[str, set[str]] = defaultdict(set)
    for annotation in review.get("existing_annotations", []) or []:
        go_id = (annotation.get("term") or {}).get("id", "")
        action = (annotation.get("review") or {}).get("action")
        if GO_ID_RE.fullmatch(go_id) and action:
            decision = (
                f"{NEGATED_ACTION_PREFIX}{action}"
                if annotation.get("negated")
                else action
            )
            decisions[go_id].add(decision)
    return dict(decisions)


def load_review_terms(review_file: Path) -> dict[str, set[str]]:
    """Load GO terms by aspect for callers that only need term membership."""
    review = yaml.safe_load(review_file.read_text()) or {}
    terms: dict[str, set[str]] = {"MF": set(), "BP": set(), "CC": set()}
    full_to_short = {value: key for key, value in ASPECT_FULL.items()}

    for annotation in review.get("existing_annotations", []) or []:
        go_id = (annotation.get("term") or {}).get("id", "")
        aspect = full_to_short.get(annotation.get("aspect", ""))
        if aspect and GO_ID_RE.fullmatch(go_id):
            terms[aspect].add(go_id)
    return terms


def load_go_cache(repo_root: Path) -> dict[str, str]:
    """Load committed sparse GO label caches."""
    labels: dict[str, str] = {}
    cache_specs = [
        (repo_root / "cache" / "ontologies" / "go.tsv", "\t", "term_id"),
        (repo_root / "cache" / "go" / "terms.csv", ",", "curie"),
    ]
    for cache_file, delimiter, id_column in cache_specs:
        if not cache_file.exists():
            continue
        with cache_file.open(newline="") as stream:
            for row in csv.DictReader(stream, delimiter=delimiter):
                go_id = row.get(id_column, "")
                label = row.get("label", "")
                if GO_ID_RE.fullmatch(go_id) and label:
                    labels[go_id] = label
    return labels


def load_go_adapter(adapter_string: str = FROZEN_GO_ADAPTER) -> Any:
    """Load the GO ontology used for leaf pruning and canonical labels."""
    return get_go_adapter(adapter_string)


def canonical_go_label(
    go_id: str,
    go_labels: dict[str, str],
    go_adapter: Any | None = None,
) -> str:
    """Return a validated canonical label, never a GO ID placeholder."""
    label = go_adapter.label(go_id) if go_adapter is not None else None
    label = label or go_labels.get(go_id)
    if not label:
        raise ValueError(f"No GO label available for {go_id}")
    if GO_ID_RE.fullmatch(label.strip()):
        raise ValueError(f"Malformed GO label for {go_id}: {label!r}")
    return label


def parse_bioreason_go_terms(markdown: str) -> list[dict[str, str]]:
    """Parse ordered GO ID/raw-label pairs from a BioReason web export."""
    terms: list[dict[str, str]] = []
    for line in markdown.splitlines():
        for heading, aspect in BIOREASON_ASPECTS.items():
            prefix = f"**{heading}:**"
            if not line.startswith(prefix):
                continue
            payload = line[len(prefix) :].strip()
            for match in GO_LABEL_PAIR_RE.finditer(payload):
                terms.append(
                    {
                        "id": match.group(2),
                        "raw_label": match.group(1).strip(),
                        "aspect": aspect,
                        "type": ASPECT_MAP[aspect],
                    }
                )
            break
    return terms


def filter_to_leaf_terms(
    terms: list[dict[str, str]],
    ancestor_lookup: Callable[[str], set[str]],
) -> list[dict[str, str]]:
    """Remove generic terms and terms that are IS_A ancestors of predictions."""
    retained: list[dict[str, str]] = []
    for aspect in ASPECT_MAP:
        aspect_terms = [term for term in terms if term["aspect"] == aspect]
        term_ids = {term["id"] for term in aspect_terms}
        redundant = set()
        for go_id in term_ids:
            redundant.update((ancestor_lookup(go_id) - {go_id}) & term_ids)

        seen = set()
        for term in aspect_terms:
            go_id = term["id"]
            if go_id in GENERIC_TERMS or go_id in redundant or go_id in seen:
                continue
            retained.append(term)
            seen.add(go_id)
    return retained


def validate_leaf_terms(
    terms: list[dict[str, str]],
    ancestor_lookup: Callable[[str], set[str]],
) -> None:
    """Fail if derived leaves contain duplicates, generic terms, or ancestors."""
    errors = []
    for aspect in ASPECT_MAP:
        term_ids = [term["id"] for term in terms if term["aspect"] == aspect]
        if len(term_ids) != len(set(term_ids)):
            errors.append(f"{aspect} contains duplicate term IDs")
        generic = set(term_ids) & GENERIC_TERMS
        if generic:
            errors.append(f"{aspect} retains generic terms: {sorted(generic)}")
        term_set = set(term_ids)
        for go_id in term_ids:
            retained_ancestors = (ancestor_lookup(go_id) - {go_id}) & term_set
            if retained_ancestors:
                errors.append(
                    f"{aspect} retains ancestors of {go_id}: "
                    f"{sorted(retained_ancestors)}"
                )
    if errors:
        raise ValueError("Invalid GO-GPT leaf set: " + "; ".join(errors))


def is_malformed_raw_label(label: str) -> bool:
    """Detect model labels made only from one or more GO identifiers."""
    tokens = label.split()
    return not tokens or all(GO_ID_RE.fullmatch(token) for token in tokens)


def deterministic_assessment(
    go_id: str,
    review_decisions: dict[str, set[str]] | None,
) -> tuple[str, str]:
    """Classify only exact, unambiguous current AIGR action matches."""
    actions = set((review_decisions or {}).get(go_id, set()))
    action_text = ", ".join(sorted(actions))

    # A retained annotation is sufficient evidence that the exact prediction is
    # correct-not-novel, even if another evidence line has a different action.
    positive = sorted(actions & POSITIVE_ACTIONS)
    if positive:
        return (
            "CNN",
            "Deterministic exact-match comparison: current AIGR action(s) "
            f"{', '.join(positive)} retain this GO term, so it is correct but "
            "not novel.",
        )

    accepted_negations = sorted(
        action.removeprefix(NEGATED_ACTION_PREFIX)
        for action in actions
        if action.startswith(NEGATED_ACTION_PREFIX)
        and action.removeprefix(NEGATED_ACTION_PREFIX) in POSITIVE_ACTIONS
    )
    if accepted_negations:
        return (
            "NPI",
            "Deterministic exact-match comparison: current AIGR retains a NOT "
            f"annotation with action(s) {', '.join(accepted_negations)}, which "
            "directly contradicts this positive GO-GPT prediction; classified as "
            "nonparalog incorrect.",
        )

    # Only a pure negative decision set is auto-classified. Mixed REMOVE/PENDING,
    # MODIFY, and UNDECIDED cases remain unresolved. REP is never inferred from a
    # generic REMOVE because frequency bias requires separate evidence.
    if actions and actions <= NEGATIVE_ACTIONS:
        return (
            "NPI",
            "Deterministic exact-match comparison: current AIGR action(s) "
            f"{action_text} reject or flag this exact GO term as over-annotated; "
            "classified as nonparalog incorrect.",
        )

    return (
        "UNC",
        "No deterministic exact-action match resolves this prediction in the "
        f"current AIGR review. {MANUAL_ASSESSMENT_MARKER}.",
    )


def normalize_review_confidence(review: dict[str, Any]) -> dict[str, Any]:
    """Normalize confidence to the declared PredictionAssessment mapping."""
    normalized = dict(review)
    assessment = normalized.get("assessment", "UNC")
    if assessment not in CONFIDENCE_BY_ASSESSMENT:
        raise ValueError(f"Unknown prediction assessment: {assessment}")
    normalized["confidence_score"] = CONFIDENCE_BY_ASSESSMENT[assessment]
    return normalized


def is_manual_review(review: dict[str, Any] | None) -> bool:
    """Return whether a prediction has a non-generated assessment rationale."""
    if not review:
        return False
    summary = review.get("summary", "")
    if not summary or MANUAL_ASSESSMENT_MARKER in summary:
        return False
    return not summary.startswith(GENERATED_SUMMARY_PREFIXES)


def build_prediction_entry(
    term: dict[str, str],
    review_decisions: dict[str, set[str]] | None,
    go_labels: dict[str, str],
    go_adapter: Any | None,
    source_version: str,
    existing_prediction: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build one normalized prediction while preserving manual adjudication."""
    existing_prediction = existing_prediction or {}
    canonical_label = canonical_go_label(term["id"], go_labels, go_adapter)
    existing_review = existing_prediction.get("review")
    if isinstance(existing_review, dict) and is_manual_review(existing_review):
        review = normalize_review_confidence(existing_review)
    else:
        assessment, summary = deterministic_assessment(term["id"], review_decisions)
        review = {
            "assessment": assessment,
            "confidence_score": CONFIDENCE_BY_ASSESSMENT[assessment],
            "summary": summary,
        }

    raw_label = term.get("raw_label", "")
    if raw_label != canonical_label:
        problem = (
            "was malformed; the current GO label is"
            if is_malformed_raw_label(raw_label)
            else "did not match the current GO label"
        )
        raw_note = (
            f" {ONTOLOGY_LABEL_AUDIT_MARKER} Raw BioReason label {raw_label!r} "
            f"{problem} {canonical_label!r}; the "
            "structured label was normalized from GO and the raw source was retained."
        )
        if raw_note.strip() not in review.get("summary", ""):
            review["summary"] = review.get("summary", "").rstrip() + raw_note

    return {
        "source_method": existing_prediction.get("source_method", "GO-GPT"),
        "source_version": existing_prediction.get("source_version", source_version),
        "source_reference_id": existing_prediction.get(
            "source_reference_id", BIOREASON_REF
        ),
        "predicted_term": {
            "id": term["id"],
            "label": canonical_label,
        },
        "predicted_term_type": term["type"],
        "review": review,
    }


def prediction_review_status(predictions: list[dict[str, Any]]) -> str:
    """Keep a document DRAFT while generated manual-review placeholders remain."""
    unresolved = any(
        MANUAL_ASSESSMENT_MARKER in prediction.get("review", {}).get("summary", "")
        for prediction in predictions
    )
    return "DRAFT" if unresolved else "COMPLETE"


def assessment_counts(predictions: list[dict[str, Any]]) -> Counter[str]:
    """Count prediction assessments."""
    return Counter(
        prediction.get("review", {}).get("assessment", "UNC")
        for prediction in predictions
    )


def build_prediction_review_yaml(
    gene: str,
    organism: str,
    accession: str,
    predictions: dict[str, list[str]],
    review_decisions: dict[str, set[str]] | None,
    go_labels: dict[str, str],
    seq_length: int,
    go_adapter: Any | None = None,
) -> dict[str, Any]:
    """Build a PredictionReview document from a local GO-GPT inference."""
    del seq_length  # Retained in the API for compatibility with existing callers.
    predicted_annotations = []
    for aspect in ("MF", "BP", "CC"):
        for go_id in predictions.get(aspect, []):
            if go_id in GENERIC_TERMS:
                continue
            predicted_annotations.append(
                build_prediction_entry(
                    {
                        "id": go_id,
                        "raw_label": go_labels.get(go_id, ""),
                        "aspect": aspect,
                        "type": ASPECT_MAP[aspect],
                    },
                    review_decisions,
                    go_labels,
                    go_adapter,
                    "wanglab/gogpt",
                )
            )

    counts = assessment_counts(predicted_annotations)
    description = (
        f"GO-GPT predictions for {gene} ({organism}). "
        f"{len(predicted_annotations)} non-generic terms retained. Deterministic "
        f"exact comparison against current AIGR: CNN:{counts['CNN']} "
        f"NPI:{counts['NPI']} UNC:{counts['UNC']}."
    )
    return {
        "id": accession,
        "gene_symbol": gene,
        "taxon": {"id": f"uniprot:{organism}", "label": organism},
        "status": prediction_review_status(predicted_annotations),
        "description": description,
        "references": [{"id": BIOREASON_REF, "title": BIOREASON_TITLE}],
        "predictions": predicted_annotations,
    }


def build_web_export_review(
    existing_document: dict[str, Any],
    raw_export: Path,
    review_file: Path,
    go_labels: dict[str, str],
    go_adapter: Any,
) -> dict[str, Any]:
    """Regenerate one leaf review from immutable raw BioReason provenance."""
    parsed_terms = parse_bioreason_go_terms(raw_export.read_text())
    if not parsed_terms:
        raise ValueError(f"No GO terms parsed from {raw_export}")

    ancestor_cache: dict[str, set[str]] = {}

    def ancestors(go_id: str) -> set[str]:
        if go_id not in ancestor_cache:
            from oaklib.datamodels.vocabulary import IS_A

            ancestor_cache[go_id] = set(
                go_adapter.ancestors(go_id, predicates=[IS_A])
            )
        return ancestor_cache[go_id]

    leaf_terms = filter_to_leaf_terms(parsed_terms, ancestors)
    validate_leaf_terms(leaf_terms, ancestors)
    review_decisions = load_review_decisions(review_file)

    existing_by_key = {
        (
            (prediction.get("predicted_term") or {}).get("id"),
            prediction.get("predicted_term_type"),
        ): prediction
        for prediction in existing_document.get("predictions", []) or []
    }
    default_source_version = "bioreason.net/2026-03/rl"
    existing_predictions = existing_document.get("predictions", []) or []
    if existing_predictions:
        default_source_version = existing_predictions[0].get(
            "source_version", default_source_version
        )

    predictions = [
        build_prediction_entry(
            term,
            review_decisions,
            go_labels,
            go_adapter,
            default_source_version,
            existing_by_key.get((term["id"], term["type"])),
        )
        for term in leaf_terms
    ]

    counts = assessment_counts(predictions)
    raw_specific_count = sum(
        1 for term in parsed_terms if term["id"] not in ROOT_TERMS
    )
    raw_label_mismatches = []
    raw_malformed_pairs = []
    for term in parsed_terms:
        canonical_label = canonical_go_label(term["id"], go_labels, go_adapter)
        if term["raw_label"] != canonical_label:
            raw_label_mismatches.append(term)
        if is_malformed_raw_label(term["raw_label"]):
            raw_malformed_pairs.append(term)

    aspect_counts = Counter(term["aspect"] for term in leaf_terms)
    gene = existing_document.get("gene_symbol", raw_export.parent.name)
    organism = raw_export.parent.parent.name
    unresolved_note = (
        "Remaining UNC entries require manual assessment."
        if counts["UNC"]
        else "All retained terms were resolved by deterministic exact matching."
    )
    label_audit_note = ""
    if raw_label_mismatches:
        label_audit_note = (
            f" {ONTOLOGY_LABEL_AUDIT_MARKER} The raw export contained "
            f"{len(raw_label_mismatches)} ID/label pairs that differ from current "
            "GO labels; structured leaf labels were normalized and the raw source "
            "was retained."
        )
    if raw_malformed_pairs:
        malformed_details = ", ".join(
            f"{term['id']} <- {term['raw_label']!r}" for term in raw_malformed_pairs
        )
        label_audit_note += (
            f" {len(raw_malformed_pairs)} raw labels consisted only of GO IDs: "
            f"{malformed_details}."
        )
    description = (
        f"BioReason-Pro RL web export for {gene} ({organism}). GO-GPT produced "
        f"{raw_specific_count} non-root terms; {len(leaf_terms)} non-generic IS_A "
        f"leaf terms retained (MF:{aspect_counts['MF']} BP:{aspect_counts['BP']} "
        f"CC:{aspect_counts['CC']}). Deterministic exact comparison against "
        f"current AIGR: CNN:{counts['CNN']} NPI:{counts['NPI']} "
        f"UNC:{counts['UNC']}. {unresolved_note}{label_audit_note}"
    )

    source_documents = existing_document.get("source_documents") or [raw_export.name]
    if raw_export.name not in source_documents:
        source_documents = [*source_documents, raw_export.name]

    result = {
        "id": existing_document.get("id"),
        "gene_symbol": gene,
        "taxon": existing_document.get(
            "taxon", {"id": f"uniprot:{organism}", "label": organism}
        ),
        "status": prediction_review_status(predictions),
        "description": description,
        "references": existing_document.get("references")
        or [{"id": BIOREASON_REF, "title": BIOREASON_TITLE}],
        "source_documents": source_documents,
        "predictions": predictions,
    }
    if existing_document.get("locus_tag"):
        result["locus_tag"] = existing_document["locus_tag"]
    return result


def summarize_documents(documents: list[dict[str, Any]]) -> dict[str, Any]:
    """Return reproducible status and assessment counts for a document cohort."""
    statuses: Counter[str] = Counter()
    assessments: Counter[str] = Counter()
    predictions = 0
    manual_placeholders = 0
    for document in documents:
        statuses[document.get("status", "UNKNOWN")] += 1
        for prediction in document.get("predictions", []) or []:
            predictions += 1
            review = prediction.get("review", {})
            assessments[review.get("assessment", "UNKNOWN")] += 1
            if MANUAL_ASSESSMENT_MARKER in review.get("summary", ""):
                manual_placeholders += 1
    return {
        "documents": len(documents),
        "predictions": predictions,
        "statuses": dict(sorted(statuses.items())),
        "assessments": dict(sorted(assessments.items())),
        "manual_placeholders": manual_placeholders,
    }


def refresh_web_exports(
    repo_root: Path,
    go_adapter: Any,
    write: bool,
    check: bool,
) -> int:
    """Regenerate every committed GO-GPT leaf review from its raw source."""
    paths = sorted(repo_root.glob("genes/*/*/*-gogpt-leaf-predictions.yaml"))
    go_labels = load_go_cache(repo_root)
    before_documents = []
    after_documents = []
    stale_paths = []

    for path in paths:
        existing = yaml.safe_load(path.read_text()) or {}
        before_documents.append(existing)
        source_documents = existing.get("source_documents") or []
        raw_name = next(
            (
                name
                for name in source_documents
                if name.endswith("-bioreason-rl-predictions.md")
            ),
            f"{path.parent.name}-bioreason-rl-predictions.md",
        )
        raw_export = path.parent / raw_name
        review_file = path.parent / f"{path.parent.name}-ai-review.yaml"
        if not raw_export.exists():
            raise FileNotFoundError(f"Missing raw provenance: {raw_export}")
        if not review_file.exists():
            raise FileNotFoundError(f"Missing AIGR review: {review_file}")

        regenerated = build_web_export_review(
            existing, raw_export, review_file, go_labels, go_adapter
        )
        after_documents.append(regenerated)
        if regenerated != existing:
            stale_paths.append(path)
        if write:
            with path.open("w") as stream:
                yaml.safe_dump(
                    regenerated,
                    stream,
                    sort_keys=False,
                    allow_unicode=True,
                    width=120,
                )

    print("Before:", json.dumps(summarize_documents(before_documents), sort_keys=True))
    print("After: ", json.dumps(summarize_documents(after_documents), sort_keys=True))
    print(f"Files changed: {len(stale_paths)} of {len(paths)}")
    if check and stale_paths:
        print("GO-GPT leaf reviews are stale. Run --refresh-web-exports.")
        return 1
    return 0


def load_predictor(model_dir: Path) -> Any:
    """Load the local GO-GPT predictor."""
    import torch  # type: ignore[import-not-found]
    from transformers import AutoTokenizer  # type: ignore[import-not-found]

    sys.path.insert(0, str(Path.home() / "repos/BioReason-Pro/gogpt/src"))
    from gogpt.inference import (  # type: ignore[import-not-found]
        GOGPTPredictor,
        GOTokenizerJSON,
        OrganismMapperJSON,
    )

    predictor = object.__new__(GOGPTPredictor)
    predictor.device = torch.device(
        "mps" if torch.backends.mps.is_available() else "cpu"
    )
    predictor.verbose = False
    predictor.config_path = str(model_dir / "config.yaml")
    predictor._embed_model_path = "facebook/esm2_t36_3B_UR50D"

    with (model_dir / "tokenizer_info.json").open() as stream:
        predictor.tokenizer_info = json.load(stream)
    predictor.go_tokenizer = GOTokenizerJSON.from_json(
        model_dir / "go_tokenizer.json"
    )
    predictor.organism_mapper = OrganismMapperJSON.from_json(
        model_dir / "organism_mapper.json"
    )
    predictor.protein_tokenizer = AutoTokenizer.from_pretrained(
        "facebook/esm2_t36_3B_UR50D"
    )
    predictor._load_model(str(model_dir / "model.ckpt"))
    return predictor


def run_inference(args: argparse.Namespace) -> int:
    """Run GO-GPT for one gene and write a PredictionReview document."""
    if not args.organism or not args.gene:
        raise SystemExit("organism and gene are required for GO-GPT inference")

    repo_root = Path(args.output_dir)
    gene_dir = repo_root / "genes" / args.organism / args.gene
    uniprot_file = gene_dir / f"{args.gene}-uniprot.txt"
    if not uniprot_file.exists():
        raise SystemExit(f"No UniProt file: {uniprot_file}")

    sequence = extract_sequence(uniprot_file)
    if not sequence:
        raise SystemExit(f"Could not extract sequence from {uniprot_file}")
    accession = extract_accession(uniprot_file)
    if len(sequence) > 2000:
        print(f"Truncating sequence from {len(sequence)} to 2000 aa (ESM limit)")
        sequence = sequence[:2000]

    predictor = load_predictor(Path(args.model_dir))
    organism_name = get_organism_name(args.organism, predictor.organism_mapper)
    print(f"GO-GPT prediction for {args.gene} ({args.organism})")
    print(f"Organism: {organism_name}")
    print(f"Sequence: {len(sequence)} aa")
    print(f"Device: {predictor.device}")

    result = predictor.predict(sequence=sequence, organism=organism_name)
    review_decisions = None
    if args.compare:
        review_file = gene_dir / f"{args.gene}-ai-review.yaml"
        if review_file.exists():
            review_decisions = load_review_decisions(review_file)
        else:
            print(f"No AIGR review found: {review_file}")

    go_adapter = load_go_adapter(args.go_adapter)
    document = build_prediction_review_yaml(
        gene=args.gene,
        organism=args.organism,
        accession=accession,
        predictions=result,
        review_decisions=review_decisions,
        go_labels=load_go_cache(repo_root),
        seq_length=len(sequence),
        go_adapter=go_adapter,
    )

    if args.format in ("yaml", "both"):
        yaml_file = gene_dir / f"{args.gene}-gogpt-predictions.yaml"
        with yaml_file.open("w") as stream:
            yaml.safe_dump(
                document,
                stream,
                sort_keys=False,
                allow_unicode=True,
                width=120,
            )
        print(f"Saved YAML: {yaml_file}")
    if args.format in ("json", "both"):
        json_file = gene_dir / f"{args.gene}-gogpt-predictions.json"
        json_file.write_text(json.dumps(document, indent=2))
        print(f"Saved JSON: {json_file}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run GO-GPT or refresh BioReason GO-GPT leaf reviews"
    )
    parser.add_argument("organism", nargs="?", help="Organism code")
    parser.add_argument("gene", nargs="?", help="Gene symbol")
    parser.add_argument(
        "--compare", action="store_true", help="Compare exact IDs with AIGR actions"
    )
    parser.add_argument("--output-dir", default=".", help="Repository root")
    parser.add_argument(
        "--model-dir",
        default=os.path.expanduser("~/repos/BioReason-Pro/models/gogpt"),
        help="Path to the local GO-GPT model",
    )
    parser.add_argument(
        "--go-adapter",
        default=FROZEN_GO_ADAPTER,
        help="OAK adapter used for GO labels and IS_A leaf pruning",
    )
    parser.add_argument(
        "--format", choices=["yaml", "json", "both"], default="yaml"
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--refresh-web-exports",
        action="store_true",
        help="Regenerate all committed GO-GPT leaf reviews from raw web exports",
    )
    mode.add_argument(
        "--check-web-exports",
        action="store_true",
        help="Exit nonzero if committed leaf reviews differ from regeneration",
    )
    args = parser.parse_args()

    if args.refresh_web_exports or args.check_web_exports:
        adapter = load_go_adapter(args.go_adapter)
        return refresh_web_exports(
            Path(args.output_dir),
            adapter,
            write=args.refresh_web_exports,
            check=args.check_web_exports,
        )
    return run_inference(args)


if __name__ == "__main__":
    raise SystemExit(main())
