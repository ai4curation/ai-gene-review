"""Expose the GO-GPT three-level overlap as browsable per-term rows.

The source is the committed ``reports/gogpt-comparison-levels.json``, which
``scripts/gogpt_compare_levels.py`` derives from the repository at the declared
``review_snapshot_commit``. Rows are therefore a dated snapshot, consistent with
the BioReason manuscript, and do not change as reviews are curated. Each row is
one specific (non-generic) GO-GPT predicted term for one gene, with one boolean
per reference layer, so facet counts reproduce the aggregate overlap numbers.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Callable

from ai_gene_review.source_tree import BENCHMARK_POLICY, declared_review_snapshot

LEVELS_REPORT = Path("reports/gogpt-comparison-levels.json")
OVERLAP_COHORT = "supplement_gogpt_overlap_300"
LEVELS = (
    ("in_goa", "goa_overlap_terms"),
    ("in_post_review", "post_review_overlap_terms"),
    ("in_core", "core_overlap_terms"),
)
LEVEL_LABELS = {
    "in_goa": "Raw GOA",
    "in_post_review": "Post-review AIGR",
    "in_core": "AIGR core functions",
}
NO_LEVEL_LABEL = "No reference layer"


def overlap_rows_for_record(record: dict[str, Any]) -> list[dict[str, Any]]:
    """Expand one per-gene report record into one row per predicted term.

    >>> record = {"organism": "ECOLI", "gene": "g", "preds": 2,
    ...     "goa_terms": 3, "post_review_terms": 2, "core_terms": 1,
    ...     "predicted_terms": ["GO:1", "GO:2"],
    ...     "goa_overlap_terms": ["GO:1"], "post_review_overlap_terms": ["GO:1"],
    ...     "core_overlap_terms": []}
    >>> rows = overlap_rows_for_record(record)
    >>> [(r["term_id"], r["in_goa"], r["in_post_review"], r["in_core"]) for r in rows]
    [('GO:1', True, True, False), ('GO:2', False, False, False)]
    >>> rows[0]["matched_levels"], rows[1]["matched_levels"]
    (['Raw GOA', 'Post-review AIGR'], ['No reference layer'])

    A report whose overlap lists name a term outside the predicted set is
    inconsistent and is rejected rather than silently dropped:

    >>> overlap_rows_for_record(dict(record, core_overlap_terms=["GO:9"]))
    Traceback (most recent call last):
    ...
    ValueError: ECOLI/g: overlap terms not among predicted terms: ['GO:9']
    """
    organism, gene = record["organism"], record["gene"]
    predicted = record["predicted_terms"]
    if len(predicted) != record["preds"]:
        raise ValueError(
            f"{organism}/{gene}: {len(predicted)} predicted terms but preds={record['preds']}"
        )
    overlaps = {field: set(record[key]) for field, key in LEVELS}
    stray = sorted(set().union(*overlaps.values()) - set(predicted))
    if stray:
        raise ValueError(
            f"{organism}/{gene}: overlap terms not among predicted terms: {stray}"
        )
    rows = []
    for term_id in predicted:
        flags = {field: term_id in overlaps[field] for field, _ in LEVELS}
        rows.append(
            {
                "overlap_id": "go-"
                + hashlib.sha256(f"{organism}\0{gene}\0{term_id}".encode()).hexdigest()[:20],
                "gene_symbol": gene,
                "species": organism,
                "term_id": term_id,
                **flags,
                "matched_levels": [LEVEL_LABELS[f] for f, hit in flags.items() if hit]
                or [NO_LEVEL_LABEL],
                "gene_predictions": record["preds"],
                "gene_goa_terms": record["goa_terms"],
                "gene_post_review_terms": record["post_review_terms"],
                "gene_core_terms": record["core_terms"],
            }
        )
    return rows


def collect_gogpt_overlap(
    root: Path, review_link: Callable[[str, str], str]
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Return per-term overlap rows and snapshot metadata, or nothing if unreported.

    ``review_link(organism, gene)`` returns a browser-relative gene review link
    or an empty string. A checkout without the report (or without the benchmark
    policy that dates it) contributes no rows.

    Fields that are the same on every row (method, project, cohort, snapshot,
    source file) are stored once in ``metadata["overlap_row_defaults"]`` rather
    than repeated on each of the ~9,000 rows; the browser merges them back in.
    The GO-GPT batch behind this report carries no model version, so
    ``source_version`` is left empty rather than given a descriptive label.
    """
    report = root / LEVELS_REPORT
    if not report.is_file() or not (root / BENCHMARK_POLICY).is_file():
        return [], {}
    snapshot = declared_review_snapshot(root)
    records = json.loads(report.read_text(encoding="utf-8"))
    row_defaults = {
        "source_method": "GO-GPT",
        "source_version": "",
        "projects": ["BIOREASON_COMPARISON"],
        "cohorts": [OVERLAP_COHORT],
        "snapshot_date": snapshot.date,
        "snapshot_commit": snapshot.commit,
        "source_file": LEVELS_REPORT.as_posix(),
    }
    rows = []
    for record in records:
        link = review_link(record["organism"], record["gene"])
        for row in overlap_rows_for_record(record):
            rows.append({**row, "review_link": link})
    metadata = {
        "overlap_row_defaults": row_defaults,
        "overlap_snapshot_date": snapshot.date,
        "overlap_snapshot_commit": snapshot.commit,
        "overlap_gene_count": len(records),
        "overlap_row_count": len(rows),
        "overlap_source": LEVELS_REPORT.as_posix(),
    }
    return rows, metadata
