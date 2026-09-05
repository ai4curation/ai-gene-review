"""CAFA-style protein-centric precision/recall metrics.

This module reimplements the PAN-GO Human Functionome supplementary evaluation
workflow for prepared annotation files. It intentionally follows the bundled
PAN-GO Perl scripts' semantics: post-cutoff experimental annotations are used as
the proxy test set, pre-cutoff experimental annotations are excluded, and
precision/recall are macro-averaged over proteins.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass
import gzip
from pathlib import Path
import re
from typing import TextIO

DEFAULT_EXCLUDED_TERMS = frozenset(
    {
        "GO:0005515",  # protein binding
        "GO:0005488",  # binding
        "GO:0003674",  # molecular function
        "GO:0008150",  # biological process
        "GO:0005575",  # cellular component
    }
)

DEFAULT_ASPECTS = ("all", "mf", "bp", "cc")
ASPECT_ALIASES = {
    "all": "all",
    "mf": "mf",
    "f": "mf",
    "molecular_function": "mf",
    "molecular function": "mf",
    "bp": "bp",
    "p": "bp",
    "biological_process": "bp",
    "biological process": "bp",
    "cc": "cc",
    "c": "cc",
    "cellular_component": "cc",
    "cellular component": "cc",
}

GO_ID_PATTERN = re.compile(r"GO:\d{7}")
UNIPROT_IN_LONG_ID_PATTERN = re.compile(r"(?:^|\|)UniProtKB=([^|]+)")

GeneTermMap = dict[str, set[str]]
AspectGeneTermMap = dict[str, GeneTermMap]
ThresholdPredictionMap = dict[int, AspectGeneTermMap]


@dataclass(frozen=True)
class CafaMetricRow:
    """Protein-centric metric row for one threshold and ontology aspect."""

    threshold_rank: int
    threshold_fraction: float
    aspect: str
    precision_total: float
    precision_count: int
    precision: float | None
    recall_total: float
    recall_count: int
    recall: float | None
    f_score: float | None


def evaluate_cafa_predictions(
    prediction_file: str | Path,
    training_annotations_file: str | Path,
    new_annotations_file: str | Path,
    curated_genes_file: str | Path,
    go_parents_file: str | Path | None = None,
    *,
    thresholds: Sequence[int] = tuple(range(1, 11)),
    aspects: Sequence[str] = DEFAULT_ASPECTS,
    excluded_terms: Iterable[str] = DEFAULT_EXCLUDED_TERMS,
) -> list[CafaMetricRow]:
    """Evaluate predictions with the PAN-GO CAFA-style metric.

    Args:
        prediction_file: Prediction TSV. Gzip-compressed files are supported.
            Expected columns are gene ID, GO ID, label, aspect, score, rank.
        training_annotations_file: Pre-cutoff experimental annotations. Expected
            columns are UniProt ID, GO ID, aspect, evidence, direct/parent type.
        new_annotations_file: Post-cutoff experimental annotations in the same
            five-column format as ``training_annotations_file``.
        curated_genes_file: PAN-GO-style curatable gene list, one long gene ID
            per line, e.g. ``HUMAN|HGNC=10741|UniProtKB=O75326``.
        go_parents_file: Optional all-parent lookup. Expected columns include a
            child term containing a GO ID and a parent term containing a GO ID.
            All listed parents are used, matching the PAN-GO Perl script.
        thresholds: Integer rank thresholds. Rank 1 predictions are included at
            every threshold; rank N predictions are included for thresholds >= N.
        aspects: Ontology aspects to report. Defaults to all, MF, BP, and CC.
        excluded_terms: GO IDs to remove from training, test, parent closure,
            and prediction files.

    Returns:
        Metric rows ordered by threshold, then aspect.
    """

    excluded = set(excluded_terms)
    threshold_values = tuple(sorted(set(thresholds)))
    if not threshold_values:
        msg = "At least one threshold is required"
        raise ValueError(msg)

    genes, uniprot_to_gene = load_curated_genes(curated_genes_file)
    go_parents = load_go_parent_map(go_parents_file) if go_parents_file else {}
    existing = load_training_annotations(
        training_annotations_file,
        genes,
        uniprot_to_gene,
        go_parents,
        excluded,
    )
    new_annotations = load_new_annotations(
        new_annotations_file,
        genes,
        uniprot_to_gene,
        existing,
        excluded,
    )
    predictions, predicted_gene_ids = load_predictions(
        prediction_file,
        genes,
        uniprot_to_gene,
        new_annotations,
        threshold_values,
        excluded,
    )
    filtered_new_annotations = {
        aspect: {
            gene: terms
            for gene, terms in gene_terms.items()
            if gene in predicted_gene_ids.get(aspect, set())
        }
        for aspect, gene_terms in new_annotations.items()
    }

    return calculate_protein_centric_rows(
        predictions,
        filtered_new_annotations,
        threshold_values,
        aspects,
    )


def load_curated_genes(path: str | Path) -> tuple[set[str], dict[str, str]]:
    """Load curatable genes and UniProt-to-long-ID mappings."""

    genes: set[str] = set()
    uniprot_to_gene: dict[str, str] = {}
    with open_text(path) as handle:
        for line_number, raw_line in enumerate(handle, 1):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            genes.add(line)
            match = UNIPROT_IN_LONG_ID_PATTERN.search(line)
            if not match:
                msg = f"{path}:{line_number}: could not find UniProtKB= in {line!r}"
                raise ValueError(msg)
            uniprot_to_gene[match.group(1)] = line
    return genes, uniprot_to_gene


def load_go_parent_map(path: str | Path) -> dict[str, set[str]]:
    """Load a child GO ID to parent GO IDs lookup."""

    parent_map: dict[str, set[str]] = {}
    with open_text(path) as handle:
        for line_number, raw_line in enumerate(handle, 1):
            line = raw_line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            fields = line.split("\t")
            if len(fields) < 2:
                msg = f"{path}:{line_number}: expected at least 2 tab-separated fields"
                raise ValueError(msg)
            child_match = GO_ID_PATTERN.search(fields[0])
            parent_match = GO_ID_PATTERN.search(fields[1])
            if not child_match or not parent_match:
                continue
            parent_map.setdefault(child_match.group(0), set()).add(parent_match.group(0))
    return parent_map


def load_training_annotations(
    path: str | Path,
    genes: set[str],
    uniprot_to_gene: dict[str, str],
    go_parents: dict[str, set[str]],
    excluded_terms: set[str],
) -> GeneTermMap:
    """Load pre-cutoff annotations and add parent closure for exclusion."""

    existing: GeneTermMap = {}
    with open_text(path) as handle:
        for line_number, raw_line in enumerate(handle, 1):
            fields = parse_tsv_fields(path, line_number, raw_line, min_fields=2)
            if fields is None:
                continue
            gene = canonical_gene_id(fields[0], genes, uniprot_to_gene)
            if gene is None:
                continue
            go_id = fields[1]
            if go_id in excluded_terms:
                continue
            terms = existing.setdefault(gene, set())
            terms.add(go_id)
            for parent in go_parents.get(go_id, set()):
                if parent not in excluded_terms:
                    terms.add(parent)
    return existing


def load_new_annotations(
    path: str | Path,
    genes: set[str],
    uniprot_to_gene: dict[str, str],
    existing: GeneTermMap,
    excluded_terms: set[str],
) -> AspectGeneTermMap:
    """Load post-cutoff annotations, excluding anything already in training."""

    new_annotations: AspectGeneTermMap = {}
    with open_text(path) as handle:
        for line_number, raw_line in enumerate(handle, 1):
            fields = parse_tsv_fields(path, line_number, raw_line, min_fields=3)
            if fields is None:
                continue
            gene = canonical_gene_id(fields[0], genes, uniprot_to_gene)
            if gene is None:
                continue
            go_id = fields[1]
            if go_id in excluded_terms or go_id in existing.get(gene, set()):
                continue
            aspect = normalize_aspect(fields[2], path, line_number)
            add_term(new_annotations, aspect, gene, go_id)
            add_term(new_annotations, "all", gene, go_id)
    return new_annotations


def load_predictions(
    path: str | Path,
    genes: set[str],
    uniprot_to_gene: dict[str, str],
    new_annotations: AspectGeneTermMap,
    thresholds: Sequence[int],
    excluded_terms: set[str],
) -> tuple[ThresholdPredictionMap, dict[str, set[str]]]:
    """Load prediction rows and expand each rank into threshold pools."""

    predictions: ThresholdPredictionMap = {}
    predicted_gene_ids: dict[str, set[str]] = {}
    threshold_values = tuple(sorted(thresholds))
    min_threshold = threshold_values[0]
    max_threshold = threshold_values[-1]

    with open_text(path) as handle:
        for line_number, raw_line in enumerate(handle, 1):
            fields = parse_tsv_fields(path, line_number, raw_line, min_fields=6)
            if fields is None:
                continue
            gene = canonical_gene_id(fields[0], genes, uniprot_to_gene)
            if gene is None:
                continue
            go_id = fields[1]
            if go_id in excluded_terms:
                continue
            aspect = normalize_aspect(fields[3], path, line_number)
            if gene not in new_annotations.get(aspect, {}):
                continue
            try:
                rank = int(fields[5])
            except ValueError as e:
                if line_number == 1:
                    continue
                msg = f"{path}:{line_number}: prediction rank must be an integer"
                raise ValueError(msg) from e
            if rank < min_threshold or rank > max_threshold:
                msg = (
                    f"{path}:{line_number}: prediction rank {rank} is outside "
                    f"the configured threshold range {min_threshold}-{max_threshold}"
                )
                raise ValueError(msg)

            predicted_gene_ids.setdefault(aspect, set()).add(gene)
            for threshold in threshold_values:
                if threshold >= rank:
                    add_term(predictions.setdefault(threshold, {}), aspect, gene, go_id)

    return predictions, predicted_gene_ids


def calculate_protein_centric_rows(
    predictions: ThresholdPredictionMap,
    new_annotations: AspectGeneTermMap,
    thresholds: Sequence[int],
    aspects: Sequence[str] = DEFAULT_ASPECTS,
) -> list[CafaMetricRow]:
    """Calculate macro-averaged protein-centric precision, recall, and F score."""

    max_threshold = max(thresholds)
    rows: list[CafaMetricRow] = []
    for threshold in sorted(thresholds):
        threshold_predictions = predictions.get(threshold, {})
        for aspect in aspects:
            normalized_aspect = normalize_aspect(aspect)
            aspect_predictions = threshold_predictions.get(normalized_aspect, {})
            aspect_truth = new_annotations.get(normalized_aspect, {})

            precision_total = 0.0
            precision_count = 0
            for gene, predicted_terms in aspect_predictions.items():
                if not predicted_terms:
                    continue
                true_terms = aspect_truth.get(gene, set())
                common_count = len(predicted_terms & true_terms)
                precision_total += common_count / len(predicted_terms)
                precision_count += 1

            recall_total = 0.0
            recall_count = 0
            for gene, true_terms in aspect_truth.items():
                if not true_terms:
                    continue
                predicted_terms = aspect_predictions.get(gene, set())
                common_count = len(predicted_terms & true_terms)
                recall_total += common_count / len(true_terms)
                recall_count += 1

            precision = (
                precision_total / precision_count if precision_count else None
            )
            recall = recall_total / recall_count if recall_count else None
            f_score = harmonic_mean(precision, recall)
            rows.append(
                CafaMetricRow(
                    threshold_rank=threshold,
                    threshold_fraction=threshold / max_threshold,
                    aspect=normalized_aspect,
                    precision_total=precision_total,
                    precision_count=precision_count,
                    precision=precision,
                    recall_total=recall_total,
                    recall_count=recall_count,
                    recall=recall,
                    f_score=f_score,
                )
            )
    return rows


def format_cafa_rows_tsv(
    rows: Sequence[CafaMetricRow],
    *,
    include_header: bool = True,
) -> str:
    """Format metric rows as TSV."""

    lines: list[str] = []
    if include_header:
        lines.append(
            "\t".join(
                [
                    "threshold_rank",
                    "threshold_fraction",
                    "aspect",
                    "precision_total",
                    "precision_count",
                    "precision",
                    "recall_total",
                    "recall_count",
                    "recall",
                    "f_score",
                ]
            )
        )
    for row in rows:
        lines.append(
            "\t".join(
                [
                    str(row.threshold_rank),
                    format_float(row.threshold_fraction),
                    row.aspect,
                    format_float(row.precision_total),
                    str(row.precision_count),
                    format_float(row.precision),
                    format_float(row.recall_total),
                    str(row.recall_count),
                    format_float(row.recall),
                    format_float(row.f_score),
                ]
            )
        )
    return "\n".join(lines) + "\n"


def add_term(mapping: AspectGeneTermMap, aspect: str, gene: str, go_id: str) -> None:
    """Add a GO term to nested aspect/gene/set mapping."""

    mapping.setdefault(aspect, {}).setdefault(gene, set()).add(go_id)


def canonical_gene_id(
    raw_id: str,
    genes: set[str],
    uniprot_to_gene: dict[str, str],
) -> str | None:
    """Return the long gene ID for a long PAN-GO ID or UniProt accession."""

    if raw_id in genes:
        return raw_id
    return uniprot_to_gene.get(raw_id)


def normalize_aspect(
    aspect: str,
    path: str | Path | None = None,
    line_number: int | None = None,
) -> str:
    """Normalize GO aspect labels to all/mf/bp/cc."""

    normalized = ASPECT_ALIASES.get(aspect.strip().lower())
    if normalized:
        return normalized
    location = ""
    if path is not None and line_number is not None:
        location = f"{path}:{line_number}: "
    msg = f"{location}unknown GO aspect {aspect!r}"
    raise ValueError(msg)


def parse_tsv_fields(
    path: str | Path,
    line_number: int,
    raw_line: str,
    *,
    min_fields: int,
) -> list[str] | None:
    """Parse a non-empty TSV row, returning None for comments and blanks."""

    line = raw_line.rstrip("\n")
    if not line or line.startswith("#"):
        return None
    fields = line.split("\t")
    if len(fields) < min_fields:
        msg = f"{path}:{line_number}: expected at least {min_fields} tab-separated fields"
        raise ValueError(msg)
    return fields


def harmonic_mean(precision: float | None, recall: float | None) -> float | None:
    """Return F score for precision and recall, or None when undefined."""

    if precision is None or recall is None:
        return None
    denominator = precision + recall
    if denominator == 0:
        return None
    return 2 * precision * recall / denominator


def format_float(value: float | None) -> str:
    """Format metric values in a compact, deterministic way."""

    if value is None:
        return "na"
    return f"{value:.12g}"


def open_text(path: str | Path) -> TextIO:
    """Open a plain-text or gzip-compressed file for reading."""

    path = Path(path)
    if path.suffix == ".gz":
        return gzip.open(path, "rt")
    return path.open()
