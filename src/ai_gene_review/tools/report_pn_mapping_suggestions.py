"""Generate candidate GO mappings for uncovered Proteostasis Network codes."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable

from rapidfuzz import fuzz

from ai_gene_review.tools.report_pn_mapping_coverage import (
    LEVELS,
    PNCodeRecord,
    load_subject_specs,
    load_workbook_codes,
    summarize_coverage,
)

DEFAULT_GO_CACHE = Path("cache/ontologies/go.tsv")
DEFAULT_MAPPING_DIR = Path("projects/PROTEOSTASIS/mappings")
DEFAULT_OUTPUT_DIR = Path("projects/PROTEOSTASIS/reports/pn_mapping_suggestions")
GENERIC_TOKENS = {
    "activity",
    "assembly",
    "autophagy",
    "binding",
    "branch",
    "class",
    "complex",
    "component",
    "control",
    "degradation",
    "factor",
    "folding",
    "function",
    "group",
    "localization",
    "machinery",
    "membrane",
    "modulator",
    "pathway",
    "process",
    "protein",
    "proteostasis",
    "quality",
    "regulation",
    "response",
    "role",
    "signaling",
    "subtype",
    "system",
    "term",
    "transport",
    "type",
}
STOPWORDS = {
    "a",
    "an",
    "and",
    "associated",
    "component",
    "components",
    "direct",
    "for",
    "in",
    "no",
    "of",
    "or",
    "specific",
    "the",
    "to",
    "unknown",
    "with",
}
TEXT_REPLACEMENTS = {
    "cct/tric": "cct tric",
    "class 3": "class iii",
    "co-chaperone": "cochaperone",
    "endoplasmic-reticulum": "endoplasmic reticulum",
    "erad": "endoplasmic reticulum associated degradation",
    "hsp70-hsp90": "hsp70 hsp90",
    "pi3k": "phosphatidylinositol 3 kinase",
    "qc": "quality control",
}
PHRASE_ALIASES = {
    "cma": ("chaperone-mediated autophagy",),
    "erphagy": ("reticulophagy",),
    "lysophagy": ("autophagy cargo adaptor activity",),
    "midbody autophagy": ("autophagy cargo adaptor activity",),
    "synaptophagy": ("autophagy cargo adaptor activity",),
    "ferritinophagy": ("autophagy cargo adaptor activity",),
    "ribosome associated qc": ("protein quality control for misfolded or incompletely synthesized proteins",),
    "nuclear pore complex": ("nuclear pore",),
    "nuclear transport receptor": ("nucleocytoplasmic transport",),
    "nuclear transport ran system": ("nucleocytoplasmic transport",),
    "get pathway component": ("post-translational protein targeting to endoplasmic reticulum membrane",),
    "signal recognition particle component": ("srp-dependent cotranslational protein targeting to membrane",),
    "srp receptor subunit": ("srp-dependent cotranslational protein targeting to membrane",),
    "class 3 pi3k complex 1 component": ("phosphatidylinositol 3-kinase complex, class iii, type i",),
    "class 3 pi3k complex 2 component": ("phosphatidylinositol 3-kinase complex, class iii, type ii",),
    "gator1 complex component": ("gator1 complex",),
    "gator2 complex component": ("gator2 complex",),
    "hops complex component": ("hops complex",),
    "tomm complex": ("mitochondrial outer membrane translocase complex",),
    "timm22 complex": ("tim22 mitochondrial import inner membrane insertion complex",),
    "eif2 complex": ("eukaryotic translation initiation factor 2 complex",),
    "eif2b complex": ("eukaryotic translation initiation factor 2b complex",),
    "eif3 complex": ("eukaryotic translation initiation factor 3 complex",),
}
ROLE_HINTS = {
    "accessory",
    "activity",
    "adaptor",
    "binding",
    "cofactor",
    "cochaperone",
    "component",
    "components",
    "effector",
    "factor",
    "inhibitor",
    "localization",
    "modulator",
    "receptor",
    "regulator",
    "subunit",
}


@dataclass(frozen=True)
class GOTerm:
    """A non-obsolete GO term loaded from the local ontology cache."""

    curie: str
    label: str
    normalized_label: str
    tokens: frozenset[str]


@dataclass(frozen=True)
class CandidateMatch:
    """A ranked candidate GO term for a PN code."""

    term: GOTerm
    score: float
    basis: str
    overlap_tokens: tuple[str, ...]
    suggested_scope: str


def normalize_text(text: str) -> str:
    """Normalize free text for lexical matching."""
    normalized = text.lower().strip()
    for source, target in TEXT_REPLACEMENTS.items():
        normalized = normalized.replace(source, target)
    normalized = normalized.replace("/", " ")
    normalized = normalized.replace("-", " ")
    normalized = re.sub(r"[^a-z0-9\s]+", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def tokenize_text(text: str) -> set[str]:
    """Tokenize normalized text into informative lexical units."""
    normalized = normalize_text(text)
    tokens: set[str] = set()
    for token in normalized.split():
        if token in STOPWORDS:
            continue
        if len(token) < 3 and token not in {"er"}:
            continue
        tokens.add(token)
    return tokens


def _segments_for_record(record: PNCodeRecord) -> list[str]:
    """Return the non-empty path segments represented by this record."""
    values = [
        record.branch,
        record.class_name,
        record.group,
        record.type_name,
        record.subtype,
    ]
    return values[: LEVELS.index(record.level) + 1]


def _phrase_aliases_for_record(record: PNCodeRecord) -> set[str]:
    """Return normalized alias phrases that should be treated as exact alternates."""
    aliases: set[str] = set()
    for segment in _segments_for_record(record):
        normalized = normalize_text(segment)
        for alias in PHRASE_ALIASES.get(normalized, ()):
            aliases.add(normalize_text(alias))
    aliases.add(normalize_text(record.code))
    return aliases


def _query_strings_for_record(record: PNCodeRecord) -> tuple[str, str, str]:
    """Return normalized lexical query strings for the record."""
    segments = _segments_for_record(record)
    last = normalize_text(segments[-1]) if segments else ""
    suffix2 = normalize_text(" ".join(segments[-2:])) if len(segments) >= 2 else last
    full = normalize_text(" ".join(segments))
    return last, suffix2, full


def _query_tokens_for_record(record: PNCodeRecord) -> set[str]:
    """Return weighted lexical tokens for candidate retrieval."""
    tokens: set[str] = set()
    for segment in _segments_for_record(record):
        tokens.update(tokenize_text(segment))
    return tokens


def load_go_terms(cache_path: Path) -> list[GOTerm]:
    """Load non-obsolete GO terms from the local cache."""
    terms: list[GOTerm] = []
    with cache_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("is_obsolete", "").lower() == "true":
                continue
            label = row["label"].strip()
            normalized = normalize_text(label)
            terms.append(
                GOTerm(
                    curie=row["term_id"].strip(),
                    label=label,
                    normalized_label=normalized,
                    tokens=frozenset(tokenize_text(label)),
                )
            )
    return terms


def build_go_indexes(
    terms: Iterable[GOTerm],
) -> tuple[list[GOTerm], dict[str, set[int]], dict[str, set[int]]]:
    """Build simple lexical indexes over GO terms."""
    term_list = list(terms)
    token_index: dict[str, set[int]] = {}
    label_index: dict[str, set[int]] = {}

    for idx, term in enumerate(term_list):
        label_index.setdefault(term.normalized_label, set()).add(idx)
        for token in term.tokens:
            token_index.setdefault(token, set()).add(idx)

    return term_list, token_index, label_index


def _candidate_indices_for_record(
    record: PNCodeRecord,
    token_index: dict[str, set[int]],
    label_index: dict[str, set[int]],
) -> set[int]:
    """Return candidate GO-term indices worth scoring for this record."""
    query_tokens = _query_tokens_for_record(record)
    alias_phrases = _phrase_aliases_for_record(record)
    last, suffix2, full = _query_strings_for_record(record)

    indices: set[int] = set()
    for phrase in {last, suffix2, full, *alias_phrases}:
        if phrase:
            indices.update(label_index.get(phrase, set()))

    specific_tokens = [token for token in query_tokens if token not in GENERIC_TOKENS]
    token_pool = specific_tokens or list(query_tokens)
    for token in token_pool:
        indices.update(token_index.get(token, set()))

    return indices


def _suggested_scope(record: PNCodeRecord, matched_text: str, exact_like: bool) -> str:
    """Heuristically suggest a mapping scope for a candidate."""
    normalized = normalize_text(matched_text)
    if exact_like and record.level in {"class", "group"} and not any(
        hint in normalized for hint in ROLE_HINTS
    ):
        return "exact"
    return "ok_for_propagation_to_go"


def rank_candidates_for_record(
    record: PNCodeRecord,
    terms: list[GOTerm],
    token_index: dict[str, set[int]],
    label_index: dict[str, set[int]],
    top_n: int = 5,
) -> list[CandidateMatch]:
    """Rank candidate GO terms for one uncovered PN code."""
    indices = _candidate_indices_for_record(record, token_index, label_index)
    if not indices:
        return []

    last, suffix2, full = _query_strings_for_record(record)
    alias_phrases = _phrase_aliases_for_record(record)
    query_tokens = _query_tokens_for_record(record)
    specific_tokens = {token for token in query_tokens if token not in GENERIC_TOKENS}

    candidates: list[CandidateMatch] = []
    for idx in indices:
        term = terms[idx]

        exact_last = term.normalized_label == last and last != ""
        exact_suffix = term.normalized_label in {suffix2, full} and term.normalized_label != ""
        alias_exact = term.normalized_label in alias_phrases and term.normalized_label != ""
        exact_like = exact_last or exact_suffix or alias_exact

        overlap_all = sorted(query_tokens & set(term.tokens))
        overlap_specific = specific_tokens & set(term.tokens)
        similarity = max(
            fuzz.token_set_ratio(last, term.normalized_label) if last else 0,
            fuzz.token_set_ratio(suffix2, term.normalized_label) if suffix2 else 0,
            fuzz.token_set_ratio(full, term.normalized_label) if full else 0,
        )

        bonus = 0.0
        basis = "weak_lexical"
        if exact_last:
            bonus = 120.0
            basis = "exact_terminal_label"
        elif alias_exact:
            bonus = 115.0
            basis = "exact_alias_label"
        elif exact_suffix:
            bonus = 110.0
            basis = "exact_path_suffix"
        elif len(overlap_specific) >= 2 and similarity >= 80:
            basis = "strong_lexical"
        elif len(overlap_specific) >= 1 and similarity >= 70:
            basis = "moderate_lexical"

        score = (
            bonus
            + (8.0 * len(overlap_specific))
            + (3.0 * len(overlap_all))
            + (0.35 * similarity)
        )

        if not exact_like and len(overlap_specific) == 0 and similarity < 75:
            continue

        candidates.append(
            CandidateMatch(
                term=term,
                score=round(score, 2),
                basis=basis,
                overlap_tokens=tuple(overlap_all),
                suggested_scope=_suggested_scope(record, term.label, exact_like),
            )
        )

    candidates.sort(
        key=lambda candidate: (
            candidate.score,
            len(candidate.overlap_tokens),
            candidate.term.label,
        ),
        reverse=True,
    )
    return candidates[:top_n]


def write_suggestion_reports(
    uncovered_records: list[PNCodeRecord],
    suggestions: dict[str, list[CandidateMatch]],
    output_dir: Path,
) -> None:
    """Write summary and long-form suggestion TSVs."""
    output_dir.mkdir(parents=True, exist_ok=True)

    summary_path = output_dir / "pn_mapping_candidate_summary.tsv"
    with summary_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "level",
                "code",
                "best_go_id",
                "best_go_label",
                "best_score",
                "best_basis",
                "suggested_scope",
                "top_candidates",
            ],
            delimiter="\t",
        )
        writer.writeheader()
        for record in uncovered_records:
            ranked = suggestions.get(record.code, [])
            top = ranked[0] if ranked else None
            writer.writerow(
                {
                    "level": record.level,
                    "code": record.code,
                    "best_go_id": top.term.curie if top else "",
                    "best_go_label": top.term.label if top else "",
                    "best_score": top.score if top else "",
                    "best_basis": top.basis if top else "",
                    "suggested_scope": top.suggested_scope if top else "",
                    "top_candidates": " | ".join(
                        f"{candidate.term.curie} {candidate.term.label} ({candidate.score})"
                        for candidate in ranked
                    ),
                }
            )

    details_path = output_dir / "pn_mapping_candidate_details.tsv"
    with details_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "level",
                "code",
                "rank",
                "go_id",
                "go_label",
                "score",
                "basis",
                "suggested_scope",
                "overlap_tokens",
            ],
            delimiter="\t",
        )
        writer.writeheader()
        for record in uncovered_records:
            for rank, candidate in enumerate(suggestions.get(record.code, []), start=1):
                writer.writerow(
                    {
                        "level": record.level,
                        "code": record.code,
                        "rank": rank,
                        "go_id": candidate.term.curie,
                        "go_label": candidate.term.label,
                        "score": candidate.score,
                        "basis": candidate.basis,
                        "suggested_scope": candidate.suggested_scope,
                        "overlap_tokens": ",".join(candidate.overlap_tokens),
                    }
                )


def build_argument_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Generate ranked GO candidates for uncovered PN codes."
    )
    parser.add_argument("--workbook", required=True, type=Path, help="Path to the PN workbook")
    parser.add_argument(
        "--mapping-dir",
        type=Path,
        default=DEFAULT_MAPPING_DIR,
        help=f"Directory containing PN mapping-set YAML files (default: {DEFAULT_MAPPING_DIR})",
    )
    parser.add_argument(
        "--go-cache",
        type=Path,
        default=DEFAULT_GO_CACHE,
        help=f"Path to local GO ontology cache TSV (default: {DEFAULT_GO_CACHE})",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory for suggestion reports (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=5,
        help="Number of ranked candidates to emit per uncovered code (default: 5)",
    )
    return parser


def main() -> None:
    """Generate suggestion reports for uncovered PN codes."""
    parser = build_argument_parser()
    args = parser.parse_args()

    code_records = load_workbook_codes(args.workbook)
    mapping_specs = load_subject_specs(args.mapping_dir, slot_name="mappings")
    unmapped_specs = load_subject_specs(args.mapping_dir, slot_name="unmapped_subjects")
    coverage_rows = summarize_coverage(code_records, mapping_specs, unmapped_specs)

    code_by_key = {(record.level, record.code): record for record in code_records}
    uncovered_records = [
        code_by_key[(row["level"], row["code"])]
        for row in coverage_rows
        if row["status"] == "uncovered"
    ]

    terms = load_go_terms(args.go_cache)
    term_list, token_index, label_index = build_go_indexes(terms)
    suggestions = {
        record.code: rank_candidates_for_record(
            record,
            term_list,
            token_index,
            label_index,
            top_n=args.top_n,
        )
        for record in uncovered_records
    }
    write_suggestion_reports(uncovered_records, suggestions, args.output_dir)

    with_candidates = sum(bool(suggestions[record.code]) for record in uncovered_records)
    print(f"Wrote suggestion reports to {args.output_dir}")
    print(
        "Suggestion summary: "
        f"uncovered_codes={len(uncovered_records)} "
        f"with_candidates={with_candidates} "
        f"without_candidates={len(uncovered_records) - with_candidates}"
    )


if __name__ == "__main__":
    main()
