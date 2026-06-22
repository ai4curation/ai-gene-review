#!/usr/bin/env python3
"""Run focused deep research for AIGR gene-level curation hypotheses."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

import yaml


DEFAULT_GENES_ROOT = Path("genes")
DEFAULT_TEMPLATE = Path("templates/gene_hypothesis_deep_research.md")
DEFAULT_FUNCTION_SUPPORT_TEMPLATE = Path("templates/function_support_deep_research.md")
LOCAL_EVIDENCE_MAX_CHARS_PER_FILE = 12000
LOCAL_EVIDENCE_MAX_CHARS_TOTAL = 24000
FOCUS_TYPES = {
    "existing_go_annotation_decision",
    "function_assignment",
    "proposed_go_term",
    "computational_prediction",
    "core_function",
    "function_support",
    "free_text",
}
FOCUS_TYPE_CHOICES = sorted(
    FOCUS_TYPES | {focus_type.replace("_", "-") for focus_type in FOCUS_TYPES}
)
PROVIDER_ALIASES = {
    "edison": "falcon",
}


class LiteralString(str):
    """Marker class for readable multiline YAML block scalars."""


class HypothesisDumper(yaml.SafeDumper):
    """Safe dumper that keeps multiline strings readable."""


def _represent_literal_string(
    dumper: yaml.SafeDumper, data: LiteralString
) -> yaml.nodes.ScalarNode:
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


HypothesisDumper.add_representer(LiteralString, _represent_literal_string)


@dataclass(frozen=True)
class GeneHypothesisRecord:
    organism: str
    gene: str
    gene_symbol: str
    taxon_id: str
    taxon_label: str
    focus_type: str
    slug: str
    hypothesis_text: str
    term_context: str
    reference_context: str
    source_file: Path | None
    source_selector: str
    source_context: Mapping[str, Any]


@dataclass(frozen=True)
class ExistingHypothesisOutput:
    provider: str
    path: Path
    citations_path: Path
    citations_exists: bool


@dataclass(frozen=True)
class RunResult:
    record: GeneHypothesisRecord
    provider: str
    status: str
    returncode: int | str
    duration_seconds: float
    output_file: Path
    citations_file: Path
    command: list[str]
    detail: str


def normalize_provider(provider: str) -> str:
    value = provider.strip().lower()
    return PROVIDER_ALIASES.get(value, value)


def normalize_focus_type(value: str) -> str:
    normalized = value.strip().lower().replace("-", "_")
    if normalized not in FOCUS_TYPES:
        choices = ", ".join(sorted(focus.replace("_", "-") for focus in FOCUS_TYPES))
        raise ValueError(f"Unknown focus type {value!r}; expected one of: {choices}")
    return normalized


def slugify(text: str, fallback: str = "hypothesis") -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "-", text.strip())
    cleaned = re.sub(r"-+", "-", cleaned).strip("-").lower()
    if not cleaned:
        return fallback
    return cleaned[:96].rstrip("-") or fallback


def load_yaml(path: Path) -> Mapping[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, Mapping):
        raise ValueError(f"Expected mapping at top level of {path}")
    return data


def as_mapping(value: Any) -> Mapping[str, Any]:
    """Return value as a mapping when possible, otherwise an empty mapping."""
    return value if isinstance(value, Mapping) else {}


def literalize_multiline(value: Any) -> Any:
    if isinstance(value, str) and "\n" in value:
        return LiteralString(value)
    if isinstance(value, list):
        return [literalize_multiline(item) for item in value]
    if isinstance(value, Mapping):
        return {key: literalize_multiline(val) for key, val in value.items()}
    return value


def dump_context_yaml(value: Mapping[str, Any]) -> str:
    if not value:
        return "{}"
    return yaml.dump(
        literalize_multiline(dict(value)),
        Dumper=HypothesisDumper,
        sort_keys=False,
        allow_unicode=True,
        width=100,
    ).rstrip()


def gene_dir_for(genes_root: Path, organism: str, gene: str) -> Path:
    gene_dir = genes_root / organism / gene
    if not gene_dir.exists():
        raise FileNotFoundError(
            f"Gene directory not found: {gene_dir}. Run `just fetch-gene {organism} {gene}` first."
        )
    return gene_dir


def review_file_for(gene_dir: Path, gene: str) -> Path:
    return gene_dir / f"{gene}-ai-review.yaml"


def predictions_file_for(gene_dir: Path, gene: str) -> Path:
    return gene_dir / f"{gene}-predictions-review.yaml"


def gene_metadata(data: Mapping[str, Any], fallback_gene: str) -> tuple[str, str, str]:
    taxon = as_mapping(data.get("taxon"))
    return (
        str(data.get("gene_symbol") or fallback_gene),
        str(taxon.get("id") or ""),
        str(taxon.get("label") or ""),
    )


def term_label(term: Mapping[str, Any] | None) -> str:
    if not isinstance(term, Mapping):
        return ""
    term_id = str(term.get("id") or "")
    label = str(term.get("label") or "")
    if term_id and label:
        return f"{label} ({term_id})"
    return label or term_id


def term_slug(term: Mapping[str, Any] | None, fallback: str = "term") -> str:
    if not isinstance(term, Mapping):
        return fallback
    return slugify(str(term.get("id") or term.get("label") or fallback), fallback)


def collect_reference_ids(value: Any) -> list[str]:
    refs: list[str] = []

    def add(ref: Any) -> None:
        if isinstance(ref, str) and ref and ref not in refs:
            refs.append(ref)

    if not isinstance(value, Mapping):
        return refs
    add(value.get("original_reference_id"))
    add(value.get("source_reference_id"))
    for ref in value.get("additional_reference_ids") or []:
        add(ref)
    for support in value.get("supported_by") or []:
        if isinstance(support, Mapping):
            add(support.get("reference_id"))
    review = value.get("review")
    if isinstance(review, Mapping):
        for support in review.get("supported_by") or []:
            if isinstance(support, Mapping):
                add(support.get("reference_id"))
    return refs


def format_reference_context(reference_ids: Sequence[str]) -> str:
    if not reference_ids:
        return "No specific reference context supplied."
    return "\n".join(f"- {ref}" for ref in reference_ids)


def is_bioinformatics_path(path: Path) -> bool:
    """Return whether a local path is a bioinformatics analysis artifact."""
    return any(
        part == "bioinformatics" or part.endswith("-bioinformatics")
        for part in path.parts
    )


def resolve_local_bioinformatics_reference(
    reference_id: str, genes_root: Path
) -> Path | None:
    """Resolve file: references that point to local bioinformatics evidence."""
    if not reference_id.startswith("file:"):
        return None
    raw_path = reference_id.removeprefix("file:").strip()
    if not raw_path:
        return None

    reference_path = Path(raw_path)
    candidates: list[Path]
    if reference_path.is_absolute():
        candidates = [reference_path]
    else:
        candidates = [genes_root / reference_path, reference_path]

    for candidate in candidates:
        if (
            candidate.exists()
            and candidate.is_file()
            and is_bioinformatics_path(candidate)
        ):
            return candidate
    return None


def read_bounded_text(path: Path, max_chars: int) -> tuple[str, bool]:
    """Read a text file with a character cap; return text and truncation flag."""
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) <= max_chars:
        return text.rstrip(), False
    return text[:max_chars].rstrip(), True


def format_local_bioinformatics_context(
    reference_ids: Sequence[str],
    *,
    genes_root: Path,
    max_chars_per_file: int = LOCAL_EVIDENCE_MAX_CHARS_PER_FILE,
    max_chars_total: int = LOCAL_EVIDENCE_MAX_CHARS_TOTAL,
) -> str:
    """Expand cited local bioinformatics reports for post-run comparison."""
    included: list[str] = []
    used_chars = 0
    seen_paths: set[Path] = set()

    for reference_id in reference_ids:
        path = resolve_local_bioinformatics_reference(reference_id, genes_root)
        if path is None:
            continue
        resolved = path.resolve()
        if resolved in seen_paths:
            continue
        seen_paths.add(resolved)

        remaining = max_chars_total - used_chars
        if remaining <= 0:
            break
        limit = min(max_chars_per_file, remaining)
        text, truncated = read_bounded_text(path, limit)
        used_chars += len(text)
        truncation_note = (
            f"Included first {len(text)} characters; file was truncated for prompt size."
            if truncated
            else "Included full local report."
        )
        included.append(
            "\n".join(
                [
                    f"### {reference_id}",
                    f"- Local path: `{path}`",
                    f"- Inclusion: {truncation_note}",
                    "",
                    "```markdown",
                    text,
                    "```",
                ]
            )
        )

    if not included:
        return (
            "No cited local bioinformatics `RESULTS.md` or analysis artifact was "
            "available for post-run comparison."
        )
    return "\n\n".join(included)


def is_local_bioinformatics_reference(reference_id: str, genes_root: Path) -> bool:
    """Return whether a reference id points to a local bioinformatics artifact."""
    if not reference_id.startswith("file:"):
        return False
    raw_path = reference_id.removeprefix("file:").strip()
    if raw_path and is_bioinformatics_path(Path(raw_path)):
        return True
    return resolve_local_bioinformatics_reference(reference_id, genes_root) is not None


def visible_reference_ids(
    reference_ids: Sequence[str], *, genes_root: Path
) -> list[str]:
    """Remove local bioinformatics references from provider-visible context."""
    return [
        reference_id
        for reference_id in reference_ids
        if not is_local_bioinformatics_reference(reference_id, genes_root)
    ]


def redact_local_bioinformatics_context(value: Any, *, genes_root: Path) -> Any:
    """Remove local bioinformatics references from YAML sent to providers."""
    if isinstance(value, str):
        return None if is_local_bioinformatics_reference(value, genes_root) else value
    if isinstance(value, list):
        redacted_list = []
        for item in value:
            if (
                isinstance(item, Mapping)
                and is_local_bioinformatics_reference(
                    str(item.get("reference_id") or ""), genes_root
                )
            ):
                continue
            redacted = redact_local_bioinformatics_context(item, genes_root=genes_root)
            if redacted is not None:
                redacted_list.append(redacted)
        return redacted_list
    if isinstance(value, Mapping):
        return {
            key: redacted
            for key, item in value.items()
            if (
                redacted := redact_local_bioinformatics_context(
                    item, genes_root=genes_root
                )
            )
            is not None
        }
    return value


def format_annotation_context(annotation: Mapping[str, Any]) -> str:
    review = as_mapping(annotation.get("review"))
    term = as_mapping(annotation.get("term"))
    lines = [
        f"- Term: {term_label(term) or 'not specified'}",
        f"- Evidence type: {annotation.get('evidence_type') or 'not specified'}",
        f"- Original reference: {annotation.get('original_reference_id') or 'not specified'}",
        f"- Current review action: {review.get('action') or 'not specified'}",
    ]
    if review.get("summary"):
        lines.append(f"- Review summary: {review['summary']}")
    if review.get("reason"):
        lines.append(f"- Review reason: {review['reason']}")
    return "\n".join(lines)


def format_prediction_context(prediction: Mapping[str, Any]) -> str:
    review = as_mapping(prediction.get("review"))
    term = prediction.get("predicted_term")
    term_map = as_mapping(term)
    lines = [
        f"- Predicted term: {term_label(term_map) or 'not specified'}",
        f"- Predicted term type: {prediction.get('predicted_term_type') or 'not specified'}",
        f"- Source method: {prediction.get('source_method') or 'not specified'}",
        f"- Source version: {prediction.get('source_version') or 'not specified'}",
        f"- Source reference: {prediction.get('source_reference_id') or 'not specified'}",
        f"- Current assessment: {review.get('assessment') or 'not specified'}",
    ]
    if review.get("error_type"):
        lines.append(f"- Error type: {review['error_type']}")
    if review.get("summary"):
        lines.append(f"- Review summary: {review['summary']}")
    return "\n".join(lines)


def format_core_function_context(core_function: Mapping[str, Any]) -> str:
    mf = core_function.get("molecular_function")
    mf_map = as_mapping(mf)
    lines = [f"- Molecular function: {term_label(mf_map) or 'not specified'}"]
    if core_function.get("description"):
        lines.append(f"- Description: {core_function['description']}")
    for field, label in (
        ("directly_involved_in", "Directly involved in"),
        ("locations", "Locations"),
        ("occurs_in", "Occurs in"),
    ):
        values = core_function.get(field) or []
        if values:
            terms = [term_label(item) for item in values if isinstance(item, Mapping)]
            if terms:
                lines.append(f"- {label}: {', '.join(terms)}")
    return "\n".join(lines)


def annotation_hypothesis(
    gene_symbol: str, annotation: Mapping[str, Any], focus_type: str
) -> str:
    review = as_mapping(annotation.get("review"))
    term = as_mapping(annotation.get("term"))
    action = str(review.get("action") or "UNDECIDED")
    reason = str(review.get("reason") or review.get("summary") or "").strip()
    if focus_type == "proposed_go_term":
        lead = f"{gene_symbol} should be considered for GO annotation to {term_label(term)}."
    else:
        lead = (
            f"The existing {gene_symbol} GO annotation to {term_label(term)} "
            f"should receive review action {action}."
        )
    if reason:
        return f"{lead} Current rationale: {reason}"
    return lead


def prediction_hypothesis(gene_symbol: str, prediction: Mapping[str, Any]) -> str:
    review = as_mapping(prediction.get("review"))
    term = prediction.get("predicted_term")
    term_map = as_mapping(term)
    assessment = str(review.get("assessment") or "UNC")
    summary = str(review.get("summary") or "").strip()
    lead = (
        f"The computational prediction that {gene_symbol} has {term_label(term_map)} "
        f"should be evaluated as {assessment}."
    )
    if summary:
        return f"{lead} Current rationale: {summary}"
    return lead


def core_function_hypothesis(gene_symbol: str, core_function: Mapping[str, Any]) -> str:
    mf = core_function.get("molecular_function")
    mf_map = as_mapping(mf)
    description = str(core_function.get("description") or "").strip()
    lead = f"{term_label(mf_map) or 'The described activity'} is a core function of {gene_symbol}."
    if description:
        return f"{lead} Current rationale: {description}"
    return lead


def function_assignment_hypothesis(
    gene_symbol: str, annotation: Mapping[str, Any]
) -> str:
    term = as_mapping(annotation.get("term"))
    negated = bool(annotation.get("negated"))
    relation = "does not have" if negated else "has"
    return f"{gene_symbol} {relation} {term_label(term)}."


def proposed_term_hypothesis(
    gene_symbol: str, item: Mapping[str, Any], source_term: Mapping[str, Any] | None = None
) -> str:
    term = item.get("term") if isinstance(item.get("term"), Mapping) else item
    lead = f"{gene_symbol} should be considered for GO term {term_label(term)}."
    if source_term:
        lead += f" This term is being considered in relation to {term_label(source_term)}."
    text = str(item.get("description") or item.get("reason") or item.get("summary") or "").strip()
    if text:
        return f"{lead} Current rationale: {text}"
    return lead


def make_record(
    *,
    organism: str,
    gene: str,
    gene_symbol: str,
    taxon_id: str,
    taxon_label: str,
    focus_type: str,
    slug: str,
    hypothesis_text: str,
    term_context: str = "",
    reference_ids: Sequence[str] = (),
    source_file: Path | None = None,
    source_selector: str = "",
    source_context: Mapping[str, Any] | None = None,
) -> GeneHypothesisRecord:
    return GeneHypothesisRecord(
        organism=organism,
        gene=gene,
        gene_symbol=gene_symbol,
        taxon_id=taxon_id,
        taxon_label=taxon_label,
        focus_type=normalize_focus_type(focus_type),
        slug=slugify(slug),
        hypothesis_text=hypothesis_text.strip(),
        term_context=term_context.strip() or "No specific term context supplied.",
        reference_context=format_reference_context(reference_ids),
        source_file=source_file,
        source_selector=source_selector,
        source_context=source_context or {},
    )


def uniquify_records(records: Sequence[GeneHypothesisRecord]) -> list[GeneHypothesisRecord]:
    seen: dict[str, int] = {}
    unique: list[GeneHypothesisRecord] = []
    for record in records:
        count = seen.get(record.slug, 0) + 1
        seen[record.slug] = count
        if count == 1:
            unique.append(record)
            continue
        unique.append(
            GeneHypothesisRecord(
                organism=record.organism,
                gene=record.gene,
                gene_symbol=record.gene_symbol,
                taxon_id=record.taxon_id,
                taxon_label=record.taxon_label,
                focus_type=record.focus_type,
                slug=f"{record.slug}-{count}",
                hypothesis_text=record.hypothesis_text,
                term_context=record.term_context,
                reference_context=record.reference_context,
                source_file=record.source_file,
                source_selector=record.source_selector,
                source_context=record.source_context,
            )
        )
    return unique


def records_from_review(
    *,
    organism: str,
    gene: str,
    review_path: Path,
) -> list[GeneHypothesisRecord]:
    if not review_path.exists():
        return []
    data = load_yaml(review_path)
    gene_symbol, taxon_id, taxon_label = gene_metadata(data, gene)
    records: list[GeneHypothesisRecord] = []

    for index, annotation in enumerate(data.get("existing_annotations") or [], start=1):
        if not isinstance(annotation, Mapping):
            continue
        review = as_mapping(annotation.get("review"))
        action = str(review.get("action") or "").upper()
        term = as_mapping(annotation.get("term"))
        focus_type = (
            "proposed_go_term" if action == "NEW" else "existing_go_annotation_decision"
        )
        prefix = "new" if action == "NEW" else "existing"
        records.append(
            make_record(
                organism=organism,
                gene=gene,
                gene_symbol=gene_symbol,
                taxon_id=taxon_id,
                taxon_label=taxon_label,
                focus_type=focus_type,
                slug=f"{prefix}-{term_slug(term)}-{action.lower() or index}",
                hypothesis_text=annotation_hypothesis(gene_symbol, annotation, focus_type),
                term_context=format_annotation_context(annotation),
                reference_ids=collect_reference_ids(annotation),
                source_file=review_path,
                source_selector=f"existing_annotations[{index}]",
                source_context=annotation,
            )
        )

        if action == "MODIFY":
            for repl_index, replacement in enumerate(
                annotation.get("proposed_replacement_terms") or [], start=1
            ):
                if not isinstance(replacement, Mapping):
                    continue
                records.append(
                    make_record(
                        organism=organism,
                        gene=gene,
                        gene_symbol=gene_symbol,
                        taxon_id=taxon_id,
                        taxon_label=taxon_label,
                        focus_type="proposed_go_term",
                        slug=f"replacement-{term_slug(replacement)}",
                        hypothesis_text=proposed_term_hypothesis(
                            gene_symbol, replacement, term
                        ),
                        term_context=(
                            f"- Proposed replacement: {term_label(replacement)}\n"
                            f"- Original term: {term_label(term)}"
                        ),
                        reference_ids=collect_reference_ids(annotation),
                        source_file=review_path,
                        source_selector=(
                            f"existing_annotations[{index}]."
                            f"proposed_replacement_terms[{repl_index}]"
                        ),
                        source_context={
                            "original_annotation": annotation,
                            "proposed_replacement_term": replacement,
                        },
                    )
                )

    for index, proposed in enumerate(data.get("proposed_new_terms") or [], start=1):
        if not isinstance(proposed, Mapping):
            continue
        term = as_mapping(proposed.get("term")) or as_mapping(proposed)
        records.append(
            make_record(
                organism=organism,
                gene=gene,
                gene_symbol=gene_symbol,
                taxon_id=taxon_id,
                taxon_label=taxon_label,
                focus_type="proposed_go_term",
                slug=f"proposed-{term_slug(term)}",
                hypothesis_text=proposed_term_hypothesis(gene_symbol, proposed),
                term_context=f"- Proposed term: {term_label(term)}",
                source_file=review_path,
                source_selector=f"proposed_new_terms[{index}]",
                source_context=proposed,
            )
        )

    for index, core_function in enumerate(data.get("core_functions") or [], start=1):
        if not isinstance(core_function, Mapping):
            continue
        mf = core_function.get("molecular_function")
        mf_map = as_mapping(mf)
        records.append(
            make_record(
                organism=organism,
                gene=gene,
                gene_symbol=gene_symbol,
                taxon_id=taxon_id,
                taxon_label=taxon_label,
                focus_type="core_function",
                slug=f"core-function-{index}-{term_slug(mf_map, 'activity')}",
                hypothesis_text=core_function_hypothesis(gene_symbol, core_function),
                term_context=format_core_function_context(core_function),
                reference_ids=collect_reference_ids(core_function),
                source_file=review_path,
                source_selector=f"core_functions[{index}]",
                source_context=core_function,
            )
        )

    return uniquify_records(records)


def records_from_predictions(
    *,
    organism: str,
    gene: str,
    predictions_path: Path,
    review_fallback_path: Path | None = None,
) -> list[GeneHypothesisRecord]:
    if not predictions_path.exists():
        return []
    data = load_yaml(predictions_path)
    gene_symbol, taxon_id, taxon_label = gene_metadata(data, gene)
    if review_fallback_path and review_fallback_path.exists():
        review_data = load_yaml(review_fallback_path)
        review_gene_symbol, review_taxon_id, review_taxon_label = gene_metadata(
            review_data, gene
        )
        if not data.get("gene_symbol"):
            gene_symbol = review_gene_symbol
        taxon_id = taxon_id or review_taxon_id
        taxon_label = taxon_label or review_taxon_label

    records: list[GeneHypothesisRecord] = []
    for index, prediction in enumerate(data.get("predictions") or [], start=1):
        if not isinstance(prediction, Mapping):
            continue
        term = prediction.get("predicted_term")
        term_map = as_mapping(term)
        source = slugify(str(prediction.get("source_method") or "prediction"))
        records.append(
            make_record(
                organism=organism,
                gene=gene,
                gene_symbol=gene_symbol,
                taxon_id=taxon_id,
                taxon_label=taxon_label,
                focus_type="computational_prediction",
                slug=f"prediction-{source}-{term_slug(term_map)}",
                hypothesis_text=prediction_hypothesis(gene_symbol, prediction),
                term_context=format_prediction_context(prediction),
                reference_ids=collect_reference_ids(prediction),
                source_file=predictions_path,
                source_selector=f"predictions[{index}]",
                source_context=prediction,
            )
        )
    return uniquify_records(records)


def annotation_independent_literature_refs(annotation: Mapping[str, Any]) -> list[str]:
    """Return PMID/DOI refs that *independently* support an annotation.

    "Independent" means a literature citation other than the annotation's own
    ``original_reference_id`` (for an IBA that is the PANTHER ``GO_REF``). These
    are the refs counted as independent support in
    ``scripts/analyze_iba_support.py``.
    """
    original = str(annotation.get("original_reference_id") or "").strip()
    refs: list[str] = []

    def consider(ref: Any) -> None:
        value = str(ref or "").strip()
        if not (value.startswith("PMID:") or value.startswith("DOI:")):
            return
        if value == original or value in refs:
            return
        refs.append(value)

    for support in annotation.get("supported_by") or []:
        if isinstance(support, Mapping):
            consider(support.get("reference_id"))
    review = as_mapping(annotation.get("review"))
    for support in review.get("supported_by") or []:
        if isinstance(support, Mapping):
            consider(support.get("reference_id"))
    for ref in review.get("additional_reference_ids") or []:
        consider(ref)
    return refs


def function_support_hypothesis(gene_symbol: str, term: Mapping[str, Any]) -> str:
    """Neutral gene-function hypothesis derived from a GO term.

    Kept concise and biology-forward: retrieval providers (e.g. asta) use the
    rendered prompt as a literal, length-limited search query, so filler and
    ontology meta-vocabulary degrade recall. The support-finding *objective*
    (find independent evidence, expect false positives, quote verbatim snippets)
    lives in the template, not here.
    """
    label = term_label(term)
    if label:
        return f"{gene_symbol} has {label}."
    return f"A specific molecular function or biological role should be assigned to {gene_symbol}."


def _neutral_annotation_context(annotation: Mapping[str, Any]) -> tuple[dict[str, Any], str]:
    """Build a blinded (no prior review decision) context for an annotation.

    Mirrors :func:`function_assignment_record` so a support search is not biased
    by the existing curation action.
    """
    term = as_mapping(annotation.get("term"))
    neutral_context: dict[str, Any] = {
        "term": annotation.get("term"),
        "evidence_type": annotation.get("evidence_type"),
        "original_reference_id": annotation.get("original_reference_id"),
    }
    lines = [
        f"- Term: {term_label(term) or 'not specified'}",
        f"- Existing evidence type: {annotation.get('evidence_type') or 'not specified'}",
        f"- Original reference: {annotation.get('original_reference_id') or 'not specified'}",
    ]
    if annotation.get("negated") is not None:
        neutral_context["negated"] = annotation.get("negated")
        if annotation.get("negated"):
            lines.append("- Existing annotation is negated: true")
    if annotation.get("isoform") is not None:
        neutral_context["isoform"] = annotation.get("isoform")
        lines.append(f"- Isoform: {annotation['isoform']}")
    return neutral_context, "\n".join(lines)


def function_support_record_from_annotation(
    *,
    organism: str,
    gene: str,
    gene_symbol: str,
    taxon_id: str,
    taxon_label: str,
    annotation: Mapping[str, Any],
    source_selector: str,
    source_file: Path | None,
) -> GeneHypothesisRecord:
    """Build a neutral function-support record from an existing annotation."""
    term = as_mapping(annotation.get("term"))
    neutral_context, term_context = _neutral_annotation_context(annotation)
    return make_record(
        organism=organism,
        gene=gene,
        gene_symbol=gene_symbol,
        taxon_id=taxon_id,
        taxon_label=taxon_label,
        focus_type="function_support",
        slug=f"function-support-{term_slug(term)}",
        hypothesis_text=function_support_hypothesis(gene_symbol, term),
        term_context=term_context,
        reference_ids=collect_reference_ids(annotation),
        source_file=source_file,
        source_selector=source_selector,
        source_context=neutral_context,
    )


def iba_support_records(
    genes_root: Path,
    organism: str,
    gene: str,
    *,
    only_unsupported: bool = True,
) -> list[GeneHypothesisRecord]:
    """Thin IBA wrapper: feed each IBA annotation into the function-support flow.

    Produces one neutral ``function_support`` record per IBA annotation. With
    ``only_unsupported`` (the default), IBAs that already carry independent
    PMID/DOI support are skipped, focusing the run on annotations still needing
    confirmation.
    """
    gene_dir = gene_dir_for(genes_root, organism, gene)
    review_path = review_file_for(gene_dir, gene)
    if not review_path.exists():
        return []
    data = load_yaml(review_path)
    gene_symbol, taxon_id, taxon_label = gene_metadata(data, gene)
    records: list[GeneHypothesisRecord] = []
    for index, annotation in enumerate(data.get("existing_annotations") or [], start=1):
        if not isinstance(annotation, Mapping):
            continue
        if str(annotation.get("evidence_type") or "").upper() != "IBA":
            continue
        if only_unsupported and annotation_independent_literature_refs(annotation):
            continue
        records.append(
            function_support_record_from_annotation(
                organism=organism,
                gene=gene,
                gene_symbol=gene_symbol,
                taxon_id=taxon_id,
                taxon_label=taxon_label,
                annotation=annotation,
                source_selector=f"existing_annotations[{index}]",
                source_file=review_path,
            )
        )
    return uniquify_records(records)


def function_support_record_from_args(args: argparse.Namespace) -> GeneHypothesisRecord:
    """Build a single function-support record from CLI args.

    Accepts exactly one of: a free-text ``--hypothesis``, an
    ``--annotation-term-id`` (neutralised from the gene review), or a standalone
    ``--term-id`` (with optional ``--term-label``).
    """
    selectors = [
        bool(args.hypothesis),
        args.annotation_term_id is not None,
        args.term_id is not None,
    ]
    if sum(selectors) != 1:
        raise ValueError(
            "Specify exactly one of --hypothesis, --annotation-term-id, or --term-id."
        )

    gene_dir = gene_dir_for(args.genes_root, args.organism, args.gene)
    review_path = review_file_for(gene_dir, args.gene)
    predictions_path = predictions_file_for(gene_dir, args.gene)
    metadata: Mapping[str, Any] = {}
    if review_path.exists():
        metadata = load_yaml(review_path)
    elif predictions_path.exists():
        metadata = load_yaml(predictions_path)
    gene_symbol, taxon_id, taxon_label = gene_metadata(metadata, args.gene)
    source_file = review_path if review_path.exists() else None

    if args.annotation_term_id is not None:
        record = select_record(
            candidate_records(args.genes_root, args.organism, args.gene),
            annotation_term_id=args.annotation_term_id,
        )
        return function_support_record_from_annotation(
            organism=record.organism,
            gene=record.gene,
            gene_symbol=record.gene_symbol,
            taxon_id=record.taxon_id,
            taxon_label=record.taxon_label,
            annotation=record.source_context,
            source_selector=record.source_selector,
            source_file=record.source_file,
        )

    if args.hypothesis:
        term_context_lines: list[str] = []
        if args.term_id or args.term_label:
            term_context_lines.append(
                f"- Term: {args.term_label or 'not specified'} ({args.term_id or 'no id'})"
            )
        term_context_lines.extend(f"- {item}" for item in args.context)
        return make_record(
            organism=args.organism,
            gene=args.gene,
            gene_symbol=gene_symbol,
            taxon_id=taxon_id,
            taxon_label=taxon_label,
            focus_type="function_support",
            slug=args.slug or f"function-support-{args.hypothesis}",
            hypothesis_text=args.hypothesis,
            term_context="\n".join(term_context_lines),
            reference_ids=args.reference_id,
            source_file=source_file,
            source_selector="free-text",
            source_context={
                "hypothesis": args.hypothesis,
                "term_id": args.term_id,
                "term_label": args.term_label,
                "context": args.context,
                "reference_id": args.reference_id,
            },
        )

    term = {"id": args.term_id, "label": args.term_label or ""}
    return make_record(
        organism=args.organism,
        gene=args.gene,
        gene_symbol=gene_symbol,
        taxon_id=taxon_id,
        taxon_label=taxon_label,
        focus_type="function_support",
        slug=args.slug or f"function-support-{term_slug(term)}",
        hypothesis_text=function_support_hypothesis(gene_symbol, term),
        term_context=f"- Term: {term_label(term)}",
        reference_ids=args.reference_id,
        source_file=source_file,
        source_selector=f"term:{args.term_id}",
        source_context={"term": term},
    )


def candidate_records(genes_root: Path, organism: str, gene: str) -> list[GeneHypothesisRecord]:
    gene_dir = gene_dir_for(genes_root, organism, gene)
    review_path = review_file_for(gene_dir, gene)
    predictions_path = predictions_file_for(gene_dir, gene)
    return uniquify_records(
        [
            *records_from_review(
                organism=organism,
                gene=gene,
                review_path=review_path,
            ),
            *records_from_predictions(
                organism=organism,
                gene=gene,
                predictions_path=predictions_path,
                review_fallback_path=review_path,
            ),
        ]
    )


def core_function_records(
    records: Sequence[GeneHypothesisRecord],
) -> list[GeneHypothesisRecord]:
    return [record for record in records if record.focus_type == "core_function"]


def reference_ids_from_context(reference_context: str) -> list[str]:
    refs: list[str] = []
    for line in reference_context.splitlines():
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        ref = stripped[2:].strip()
        if ref and ref not in refs:
            refs.append(ref)
    return refs


def combined_core_function_record(
    records: Sequence[GeneHypothesisRecord],
    *,
    slug: str = "combined-core-functions",
) -> GeneHypothesisRecord:
    core_records = core_function_records(records)
    if not core_records:
        raise ValueError("No core_functions records found for this gene.")

    first = core_records[0]
    hypothesis_lines = [
        (
            f"The current core-function model for {first.gene_symbol} should be evaluated "
            "as a coherent curation model. Determine which activities/processes are primary "
            "core functions, which are downstream or non-core, and whether the model should "
            "be split, merged, or refined."
        ),
        "",
        "Current core-function hypotheses:",
    ]
    term_context_lines = ["Current core-function records:"]
    reference_ids: list[str] = []
    source_contexts: list[Mapping[str, Any]] = []
    source_selectors: list[str] = []
    for index, record in enumerate(core_records, start=1):
        hypothesis_lines.append(f"{index}. {record.hypothesis_text}")
        term_context_lines.append(f"\n## Core function {index}: {record.source_selector}")
        term_context_lines.append(record.term_context)
        source_contexts.append(record.source_context)
        source_selectors.append(record.source_selector)
        for ref in reference_ids_from_context(record.reference_context):
            if ref not in reference_ids:
                reference_ids.append(ref)

    return make_record(
        organism=first.organism,
        gene=first.gene,
        gene_symbol=first.gene_symbol,
        taxon_id=first.taxon_id,
        taxon_label=first.taxon_label,
        focus_type="core_function",
        slug=slug,
        hypothesis_text="\n".join(hypothesis_lines),
        term_context="\n".join(term_context_lines),
        reference_ids=reference_ids,
        source_file=first.source_file,
        source_selector=",".join(source_selectors),
        source_context={"core_functions": source_contexts},
    )


def function_assignment_record(record: GeneHypothesisRecord) -> GeneHypothesisRecord:
    """Convert an existing annotation decision into a neutral term hypothesis."""
    if not record.source_selector.startswith("existing_annotations["):
        raise ValueError(
            "--as-function-hypothesis requires an existing annotation selector."
        )
    annotation = record.source_context
    term = as_mapping(annotation.get("term"))
    neutral_context: dict[str, Any] = {
        "term": annotation.get("term"),
        "evidence_type": annotation.get("evidence_type"),
        "original_reference_id": annotation.get("original_reference_id"),
    }
    if annotation.get("negated") is not None:
        neutral_context["negated"] = annotation.get("negated")
    if annotation.get("isoform") is not None:
        neutral_context["isoform"] = annotation.get("isoform")

    term_context_lines = [
        f"- Term: {term_label(term) or 'not specified'}",
        f"- Evidence type: {annotation.get('evidence_type') or 'not specified'}",
        f"- Original reference: {annotation.get('original_reference_id') or 'not specified'}",
    ]
    if annotation.get("negated"):
        term_context_lines.append("- Existing annotation is negated: true")
    if annotation.get("isoform"):
        term_context_lines.append(f"- Isoform: {annotation['isoform']}")

    return make_record(
        organism=record.organism,
        gene=record.gene,
        gene_symbol=record.gene_symbol,
        taxon_id=record.taxon_id,
        taxon_label=record.taxon_label,
        focus_type="function_assignment",
        slug=f"function-hypothesis-{term_slug(term)}",
        hypothesis_text=function_assignment_hypothesis(record.gene_symbol, annotation),
        term_context="\n".join(term_context_lines),
        reference_ids=collect_reference_ids(annotation),
        source_file=record.source_file,
        source_selector=f"{record.source_selector}.function_hypothesis",
        source_context=neutral_context,
    )


def output_dir_for(
    record: GeneHypothesisRecord, genes_root: Path, organism: str, gene: str
) -> Path:
    return genes_root / organism / gene / f"{gene}-hypotheses" / record.slug


def output_file_for(
    record: GeneHypothesisRecord,
    genes_root: Path,
    organism: str,
    gene: str,
    provider: str,
) -> Path:
    normalized = normalize_provider(provider)
    return output_dir_for(record, genes_root, organism, gene) / f"{normalized}.md"


def existing_outputs(
    record: GeneHypothesisRecord, genes_root: Path, organism: str, gene: str
) -> list[ExistingHypothesisOutput]:
    directory = output_dir_for(record, genes_root, organism, gene)
    if not directory.exists():
        return []
    outputs: list[ExistingHypothesisOutput] = []
    for path in sorted(directory.glob("*.md")):
        if path.name.endswith(".citations.md"):
            continue
        citations_path = Path(f"{path}.citations.md")
        outputs.append(
            ExistingHypothesisOutput(
                provider=path.stem,
                path=path,
                citations_path=citations_path,
                citations_exists=citations_path.exists()
                and citations_path.stat().st_size > 0,
            )
        )
    return outputs


def build_provider_args(provider: str) -> list[str]:
    normalized = normalize_provider(provider)
    if normalized == "cborg":
        return ["--use-cborg"]
    if normalized == "cyberian-codex":
        return ["--provider", "cyberian", "--param", "agent_type=codex"]
    if normalized == "perplexity-lite":
        return [
            "--provider",
            "perplexity",
            "--param",
            "reasoning_effort=low",
            "--param",
            "model=sonar-pro",
        ]
    return ["--provider", normalized]


def template_vars(record: GeneHypothesisRecord, *, genes_root: Path) -> dict[str, str]:
    reference_ids = reference_ids_from_context(record.reference_context)
    provider_reference_ids = visible_reference_ids(reference_ids, genes_root=genes_root)
    provider_source_context = redact_local_bioinformatics_context(
        record.source_context,
        genes_root=genes_root,
    )
    return {
        "organism": record.organism,
        "gene": record.gene,
        "gene_symbol": record.gene_symbol,
        "taxon_id": record.taxon_id,
        "taxon_label": record.taxon_label,
        "focus_type": record.focus_type,
        "hypothesis_slug": record.slug,
        "hypothesis_text": record.hypothesis_text,
        "term_context": record.term_context,
        "reference_context": format_reference_context(provider_reference_ids),
        "source_file": str(record.source_file or ""),
        "source_selector": record.source_selector,
        "source_context_yaml": dump_context_yaml(provider_source_context),
    }


def build_command(
    record: GeneHypothesisRecord,
    *,
    provider: str,
    genes_root: Path,
    template: Path,
    extra_args: Sequence[str],
) -> list[str]:
    normalized = normalize_provider(provider)
    output_file = output_file_for(
        record, genes_root, record.organism, record.gene, normalized
    )
    command = [
        "uv",
        "run",
        "deep-research-client",
        "research",
        "--template",
        str(template),
    ]
    for key, value in template_vars(record, genes_root=genes_root).items():
        command.extend(["--var", f"{key}={value}"])
    command.extend(build_provider_args(normalized))
    command.extend(
        [
            "--output",
            str(output_file),
            "--separate-citations",
            f"{output_file}.citations.md",
        ]
    )
    command.extend(extra_args)
    return command


def shell_join(parts: Sequence[str]) -> str:
    return " ".join(subprocess.list2cmdline([part]) for part in parts)


def tail_detail(result: subprocess.CompletedProcess[str]) -> str:
    text = (result.stderr or result.stdout or "").strip()
    if not text:
        return ""
    return text.splitlines()[-1][:500]


def run_record(
    record: GeneHypothesisRecord,
    *,
    provider: str,
    genes_root: Path,
    template: Path,
    extra_args: Sequence[str],
    timeout_seconds: int,
    dry_run: bool,
    overwrite: bool,
) -> RunResult:
    normalized = normalize_provider(provider)
    output_file = output_file_for(
        record, genes_root, record.organism, record.gene, normalized
    )
    citations_file = Path(f"{output_file}.citations.md")
    command = build_command(
        record,
        provider=normalized,
        genes_root=genes_root,
        template=template,
        extra_args=extra_args,
    )

    if dry_run:
        return RunResult(
            record=record,
            provider=normalized,
            status="DRY_RUN",
            returncode=0,
            duration_seconds=0.0,
            output_file=output_file,
            citations_file=citations_file,
            command=command,
            detail="",
        )

    if output_file.exists() and not overwrite:
        return RunResult(
            record=record,
            provider=normalized,
            status="SKIPPED_EXISTS",
            returncode=0,
            duration_seconds=0.0,
            output_file=output_file,
            citations_file=citations_file,
            command=command,
            detail="use --overwrite to replace existing output",
        )

    output_file.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    try:
        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
        duration = time.monotonic() - started
        output_ok = output_file.exists() and output_file.stat().st_size > 0
        if result.returncode == 0 and output_ok:
            status = "OK"
        elif result.returncode == 0:
            status = "MISSING_OUTPUT"
        else:
            status = f"ERROR_{result.returncode}"
        return RunResult(
            record=record,
            provider=normalized,
            status=status,
            returncode=result.returncode,
            duration_seconds=duration,
            output_file=output_file,
            citations_file=citations_file,
            command=command,
            detail=tail_detail(result),
        )
    except subprocess.TimeoutExpired:
        duration = time.monotonic() - started
        return RunResult(
            record=record,
            provider=normalized,
            status="TIMEOUT",
            returncode="timeout",
            duration_seconds=duration,
            output_file=output_file,
            citations_file=citations_file,
            command=command,
            detail=f"timeout after {timeout_seconds}s",
        )


def list_records(
    records: Sequence[GeneHypothesisRecord],
    *,
    genes_root: Path,
    provider: str | None,
    missing_provider: str | None,
) -> None:
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(
        [
            "organism",
            "gene",
            "focus_type",
            "slug",
            "source_selector",
            "providers",
            "provider_count",
            "has_target_provider",
            "output_dir",
            "hypothesis_text",
        ]
    )
    target_provider = normalize_provider(provider or missing_provider or "")
    displayed = 0
    for record in records:
        outputs = existing_outputs(record, genes_root, record.organism, record.gene)
        providers = sorted(output.provider for output in outputs)
        has_target = bool(target_provider and target_provider in providers)
        if missing_provider and has_target:
            continue
        displayed += 1
        writer.writerow(
            [
                record.organism,
                record.gene,
                record.focus_type,
                record.slug,
                record.source_selector,
                ",".join(providers),
                len(providers),
                "yes" if has_target else "no" if target_provider else "",
                output_dir_for(record, genes_root, record.organism, record.gene),
                record.hypothesis_text,
            ]
        )
    print("# summary")
    print(f"# hypotheses_total\t{len(records)}")
    print(f"# rows_displayed\t{displayed}")
    if target_provider:
        print(f"# target_provider\t{target_provider}")


def select_record(
    records: Sequence[GeneHypothesisRecord],
    *,
    slug: str | None = None,
    annotation_index: int | None = None,
    annotation_term_id: str | None = None,
    prediction_index: int | None = None,
    prediction_term_id: str | None = None,
    core_function_index: int | None = None,
    proposed_term_index: int | None = None,
) -> GeneHypothesisRecord:
    selectors = [
        value is not None
        for value in (
            slug,
            annotation_index,
            annotation_term_id,
            prediction_index,
            prediction_term_id,
            core_function_index,
            proposed_term_index,
        )
    ]
    if sum(selectors) != 1:
        raise ValueError("Specify exactly one record selector or use --hypothesis.")

    if slug is not None:
        matches = [record for record in records if record.slug == slug]
    elif annotation_index is not None:
        selector = f"existing_annotations[{annotation_index}]"
        matches = [record for record in records if record.source_selector == selector]
    elif annotation_term_id is not None:
        wanted = annotation_term_id.casefold()
        matches = [
            record
            for record in records
            if record.source_selector.startswith("existing_annotations[")
            and isinstance(record.source_context.get("term"), Mapping)
            and str(record.source_context["term"].get("id") or "").casefold() == wanted
        ]
    elif prediction_index is not None:
        selector = f"predictions[{prediction_index}]"
        matches = [record for record in records if record.source_selector == selector]
    elif prediction_term_id is not None:
        wanted = prediction_term_id.casefold()
        matches = [
            record
            for record in records
            if record.source_selector.startswith("predictions[")
            and isinstance(record.source_context.get("predicted_term"), Mapping)
            and str(record.source_context["predicted_term"].get("id") or "").casefold()
            == wanted
        ]
    elif core_function_index is not None:
        selector = f"core_functions[{core_function_index}]"
        matches = [record for record in records if record.source_selector == selector]
    else:
        selector = f"proposed_new_terms[{proposed_term_index}]"
        matches = [record for record in records if record.source_selector == selector]

    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise ValueError("No hypothesis record matched the selector.")
    options = ", ".join(f"{record.source_selector}:{record.slug}" for record in matches)
    raise ValueError(f"Multiple hypothesis records matched; select by --slug. Matches: {options}")


def direct_record_from_args(args: argparse.Namespace) -> GeneHypothesisRecord:
    if not args.hypothesis:
        raise ValueError("--hypothesis is required when no source selector is provided.")
    if not args.focus_type:
        raise ValueError("--focus-type is required when using --hypothesis.")
    gene_dir = gene_dir_for(args.genes_root, args.organism, args.gene)
    review_path = review_file_for(gene_dir, args.gene)
    predictions_path = predictions_file_for(gene_dir, args.gene)
    metadata: Mapping[str, Any] = {}
    if review_path.exists():
        metadata = load_yaml(review_path)
    elif predictions_path.exists():
        metadata = load_yaml(predictions_path)
    gene_symbol, taxon_id, taxon_label = gene_metadata(metadata, args.gene)

    term_context_lines = []
    if args.term_id or args.term_label:
        term_context_lines.append(
            f"- Term: {args.term_label or 'not specified'} ({args.term_id or 'no id'})"
        )
    term_context_lines.extend(f"- {item}" for item in args.context)
    slug = args.slug or f"{normalize_focus_type(args.focus_type)}-{args.hypothesis}"
    return make_record(
        organism=args.organism,
        gene=args.gene,
        gene_symbol=gene_symbol,
        taxon_id=taxon_id,
        taxon_label=taxon_label,
        focus_type=args.focus_type,
        slug=slug,
        hypothesis_text=args.hypothesis,
        term_context="\n".join(term_context_lines),
        reference_ids=args.reference_id,
        source_context={
            "hypothesis": args.hypothesis,
            "focus_type": normalize_focus_type(args.focus_type),
            "term_id": args.term_id,
            "term_label": args.term_label,
            "context": args.context,
            "reference_id": args.reference_id,
        },
    )


def selected_or_direct_record(args: argparse.Namespace) -> GeneHypothesisRecord:
    selector_values = [
        args.record_slug,
        args.annotation_index,
        args.annotation_term_id,
        args.prediction_index,
        args.prediction_term_id,
        args.core_function_index,
        args.proposed_term_index,
    ]
    if any(value is not None for value in selector_values):
        records = candidate_records(args.genes_root, args.organism, args.gene)
        record = select_record(
            records,
            slug=args.record_slug,
            annotation_index=args.annotation_index,
            annotation_term_id=args.annotation_term_id,
            prediction_index=args.prediction_index,
            prediction_term_id=args.prediction_term_id,
            core_function_index=args.core_function_index,
            proposed_term_index=args.proposed_term_index,
        )
        if args.as_function_hypothesis:
            return function_assignment_record(record)
        return record
    if args.as_function_hypothesis:
        raise ValueError(
            "--as-function-hypothesis requires an existing annotation selector."
        )
    return direct_record_from_args(args)


def print_run_result(result: RunResult) -> None:
    print(
        f"{result.record.organism}/{result.record.gene}/{result.record.slug} "
        f"provider={result.provider} status={result.status}"
    )
    print(f"output={result.output_file}")
    print(f"citations={result.citations_file}")
    print(f"command={shell_join(result.command)}")
    if result.detail:
        print(f"detail={result.detail}")


def run_batch(
    records: Sequence[GeneHypothesisRecord],
    *,
    provider: str,
    genes_root: Path,
    template: Path,
    extra_args: Sequence[str],
    timeout_seconds: int,
    dry_run: bool,
    overwrite: bool,
    stop_on_error: bool,
) -> list[RunResult]:
    results: list[RunResult] = []
    for record in records:
        result = run_record(
            record,
            provider=provider,
            genes_root=genes_root,
            template=template,
            extra_args=extra_args,
            timeout_seconds=timeout_seconds,
            dry_run=dry_run,
            overwrite=overwrite,
        )
        print_run_result(result)
        results.append(result)
        if stop_on_error and result.status.startswith(("ERROR_", "TIMEOUT", "MISSING_")):
            break
    return results


def print_batch_summary(results: Sequence[RunResult]) -> None:
    counts: dict[str, int] = {}
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1
    print("# batch_summary")
    print(f"# records\t{len(results)}")
    for status in sorted(counts):
        print(f"# {status}\t{counts[status]}")


def has_failed_result(results: Sequence[RunResult]) -> bool:
    return any(
        result.status.startswith(("ERROR_", "TIMEOUT", "MISSING_"))
        for result in results
    )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    if argv is None:
        argv = sys.argv[1:]

    research_args: list[str] = []
    if "--" in argv:
        separator_index = list(argv).index("--")
        research_args = list(argv[separator_index + 1 :])
        argv = [*argv[:separator_index]]

    parser = argparse.ArgumentParser(
        description="Run focused deep research for AIGR gene curation hypotheses."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_gene_args(subparser: argparse.ArgumentParser) -> None:
        subparser.add_argument("organism", help="Organism directory under genes/")
        subparser.add_argument("gene", help="Gene directory name")
        subparser.add_argument(
            "--genes-root",
            type=Path,
            default=DEFAULT_GENES_ROOT,
            help="Root directory containing organism/gene folders",
        )

    list_parser = subparsers.add_parser(
        "list", help="List source-derived hypothesis research candidates."
    )
    add_gene_args(list_parser)
    list_parser.add_argument("--provider")
    list_parser.add_argument("--missing-provider")

    run_parser = subparsers.add_parser(
        "run", help="Run deep research for one focused gene hypothesis."
    )
    add_gene_args(run_parser)
    run_parser.add_argument("provider", help="Deep research provider")
    run_parser.add_argument(
        "--focus-type",
        choices=FOCUS_TYPE_CHOICES,
        help="Explicit focus type for a free-text hypothesis",
    )
    run_parser.add_argument("--hypothesis", help="Free-text hypothesis to research")
    run_parser.add_argument(
        "--slug",
        help="Output slug for a free-text hypothesis",
    )
    run_parser.add_argument("--term-id", help="Optional GO/EC/ontology term id")
    run_parser.add_argument("--term-label", help="Optional term label")
    run_parser.add_argument(
        "--reference-id",
        action="append",
        default=[],
        help="Optional reference context; repeat for multiple references",
    )
    run_parser.add_argument(
        "--context",
        action="append",
        default=[],
        help="Optional extra context line; repeat for multiple lines",
    )
    run_parser.add_argument(
        "--record-slug",
        help="Select a listed source-derived record by slug",
    )
    run_parser.add_argument(
        "--annotation-index",
        type=int,
        help="Select existing_annotations[N] from the gene review, using 1-based indexing",
    )
    run_parser.add_argument(
        "--annotation-term-id",
        help="Select an existing annotation by term id; use --record-slug if ambiguous",
    )
    run_parser.add_argument(
        "--prediction-index",
        type=int,
        help="Select predictions[N] from the predictions review, using 1-based indexing",
    )
    run_parser.add_argument(
        "--prediction-term-id",
        help="Select a computational prediction by predicted term id",
    )
    run_parser.add_argument(
        "--core-function-index",
        type=int,
        help="Select core_functions[N] from the gene review, using 1-based indexing",
    )
    run_parser.add_argument(
        "--proposed-term-index",
        type=int,
        help="Select proposed_new_terms[N] from the gene review, using 1-based indexing",
    )
    run_parser.add_argument(
        "--as-function-hypothesis",
        action="store_true",
        help=(
            "Convert a selected existing annotation into a neutral 'gene has term' "
            "hypothesis, withholding the prior review decision."
        ),
    )
    run_parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    run_parser.add_argument("--dry-run", action="store_true")
    run_parser.add_argument("--overwrite", action="store_true")
    run_parser.add_argument("--timeout-seconds", type=int, default=5400)

    def add_run_options(subparser: argparse.ArgumentParser) -> None:
        subparser.add_argument("provider", help="Deep research provider")
        subparser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
        subparser.add_argument("--dry-run", action="store_true")
        subparser.add_argument("--overwrite", action="store_true")
        subparser.add_argument("--timeout-seconds", type=int, default=5400)

    all_core_parser = subparsers.add_parser(
        "run-all-core",
        help="Run deep research for each core_functions[*] record in one gene review.",
    )
    add_gene_args(all_core_parser)
    add_run_options(all_core_parser)
    all_core_parser.add_argument(
        "--stop-on-error",
        action="store_true",
        help="Stop after the first failed core-function run.",
    )

    combined_core_parser = subparsers.add_parser(
        "run-combined-core",
        help="Run one synthesis query over all core_functions[*] records in one gene review.",
    )
    add_gene_args(combined_core_parser)
    add_run_options(combined_core_parser)
    combined_core_parser.add_argument(
        "--slug",
        default="combined-core-functions",
        help="Output slug for the combined core-function query.",
    )

    function_support_parser = subparsers.add_parser(
        "run-function-support",
        help=(
            "Find independent literature support for a gene-function hypothesis "
            "(free text, an existing annotation, or a GO term)."
        ),
    )
    add_gene_args(function_support_parser)
    function_support_parser.add_argument("provider", help="Deep research provider")
    function_support_parser.add_argument(
        "--hypothesis",
        help="Free-text gene-function hypothesis to find support for.",
    )
    function_support_parser.add_argument(
        "--annotation-term-id",
        help="Derive a neutral hypothesis from an existing annotation by GO term id.",
    )
    function_support_parser.add_argument(
        "--term-id",
        help="Derive a neutral 'GENE has TERM' hypothesis from a GO term id.",
    )
    function_support_parser.add_argument("--term-label", help="Label for --term-id.")
    function_support_parser.add_argument(
        "--context",
        action="append",
        default=[],
        help="Extra context line for the hypothesis (repeatable).",
    )
    function_support_parser.add_argument(
        "--reference-id",
        action="append",
        default=[],
        help="Seed reference id to include as context (repeatable).",
    )
    function_support_parser.add_argument("--slug", help="Override the output slug.")
    function_support_parser.add_argument(
        "--template", type=Path, default=DEFAULT_FUNCTION_SUPPORT_TEMPLATE
    )
    function_support_parser.add_argument("--dry-run", action="store_true")
    function_support_parser.add_argument("--overwrite", action="store_true")
    function_support_parser.add_argument("--timeout-seconds", type=int, default=5400)

    list_iba_parser = subparsers.add_parser(
        "list-iba",
        help="List IBA annotations that are candidates for support-finding research.",
    )
    add_gene_args(list_iba_parser)
    list_iba_parser.add_argument("--provider")
    list_iba_parser.add_argument("--missing-provider")
    list_iba_parser.add_argument(
        "--include-supported",
        action="store_true",
        help="Also list IBAs that already have independent PMID/DOI support.",
    )

    iba_parser = subparsers.add_parser(
        "run-iba-support",
        help=(
            "Thin IBA wrapper around run-function-support: research each IBA "
            "annotation as a gene-function hypothesis."
        ),
    )
    add_gene_args(iba_parser)
    iba_parser.add_argument("provider", help="Deep research provider")
    iba_parser.add_argument("--template", type=Path, default=DEFAULT_FUNCTION_SUPPORT_TEMPLATE)
    iba_parser.add_argument("--dry-run", action="store_true")
    iba_parser.add_argument("--overwrite", action="store_true")
    iba_parser.add_argument("--timeout-seconds", type=int, default=5400)
    iba_parser.add_argument(
        "--include-supported",
        action="store_true",
        help="Also research IBAs that already have independent PMID/DOI support.",
    )
    iba_parser.add_argument(
        "--annotation-term-id",
        help="Restrict to a single IBA annotation by GO term id (e.g. GO:0005737).",
    )
    iba_parser.add_argument(
        "--stop-on-error",
        action="store_true",
        help="Stop after the first failed IBA-support run.",
    )

    args = parser.parse_args(argv)
    args.research_args = research_args
    return args


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = parse_args(argv)
        if args.command == "list":
            records = candidate_records(args.genes_root, args.organism, args.gene)
            list_records(
                records,
                genes_root=args.genes_root,
                provider=args.provider,
                missing_provider=args.missing_provider,
            )
            return 0

        if args.command == "run":
            record = selected_or_direct_record(args)
            result = run_record(
                record,
                provider=args.provider,
                genes_root=args.genes_root,
                template=args.template,
                extra_args=args.research_args,
                timeout_seconds=args.timeout_seconds,
                dry_run=args.dry_run,
                overwrite=args.overwrite,
            )
            print_run_result(result)
            return 1 if result.status.startswith(("ERROR_", "TIMEOUT", "MISSING_")) else 0

        if args.command == "run-all-core":
            records = core_function_records(
                candidate_records(args.genes_root, args.organism, args.gene)
            )
            if not records:
                raise ValueError("No core_functions records found for this gene.")
            results = run_batch(
                records,
                provider=args.provider,
                genes_root=args.genes_root,
                template=args.template,
                extra_args=args.research_args,
                timeout_seconds=args.timeout_seconds,
                dry_run=args.dry_run,
                overwrite=args.overwrite,
                stop_on_error=args.stop_on_error,
            )
            print_batch_summary(results)
            return 1 if has_failed_result(results) else 0

        if args.command == "run-combined-core":
            record = combined_core_function_record(
                candidate_records(args.genes_root, args.organism, args.gene),
                slug=args.slug,
            )
            result = run_record(
                record,
                provider=args.provider,
                genes_root=args.genes_root,
                template=args.template,
                extra_args=args.research_args,
                timeout_seconds=args.timeout_seconds,
                dry_run=args.dry_run,
                overwrite=args.overwrite,
            )
            print_run_result(result)
            return 1 if result.status.startswith(("ERROR_", "TIMEOUT", "MISSING_")) else 0

        if args.command == "run-function-support":
            record = function_support_record_from_args(args)
            result = run_record(
                record,
                provider=args.provider,
                genes_root=args.genes_root,
                template=args.template,
                extra_args=args.research_args,
                timeout_seconds=args.timeout_seconds,
                dry_run=args.dry_run,
                overwrite=args.overwrite,
            )
            print_run_result(result)
            return 1 if result.status.startswith(("ERROR_", "TIMEOUT", "MISSING_")) else 0

        if args.command == "list-iba":
            records = iba_support_records(
                args.genes_root,
                args.organism,
                args.gene,
                only_unsupported=not args.include_supported,
            )
            list_records(
                records,
                genes_root=args.genes_root,
                provider=args.provider,
                missing_provider=args.missing_provider,
            )
            return 0

        if args.command == "run-iba-support":
            records = iba_support_records(
                args.genes_root,
                args.organism,
                args.gene,
                only_unsupported=not args.include_supported,
            )
            if args.annotation_term_id:
                wanted = args.annotation_term_id.casefold()
                records = [
                    record
                    for record in records
                    if isinstance(record.source_context.get("term"), Mapping)
                    and str(record.source_context["term"].get("id") or "").casefold()
                    == wanted
                ]
            if not records:
                raise ValueError(
                    "No matching IBA annotations found "
                    "(use --include-supported to include already-supported IBAs)."
                )
            results = run_batch(
                records,
                provider=args.provider,
                genes_root=args.genes_root,
                template=args.template,
                extra_args=args.research_args,
                timeout_seconds=args.timeout_seconds,
                dry_run=args.dry_run,
                overwrite=args.overwrite,
                stop_on_error=args.stop_on_error,
            )
            print_batch_summary(results)
            return 1 if has_failed_result(results) else 0
    except (FileNotFoundError, ValueError) as err:
        print(f"error: {err}", file=sys.stderr)
        return 2

    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
