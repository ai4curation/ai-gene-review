"""The GO-GPT three-level overlap is exposed in the prediction browser as a dated snapshot."""

import json
from pathlib import Path

import pytest

from ai_gene_review.export.gogpt_overlap_export import (
    LEVELS_REPORT,
    collect_gogpt_overlap,
    overlap_rows_for_record,
)
from ai_gene_review.source_tree import BENCHMARK_POLICY
from ai_gene_review.tools.build_prediction_browser import build_prediction_browser
from tests.test_build_prediction_browser import read_browser_payload

REPO_ROOT = Path(__file__).resolve().parents[1]

RECORD = {
    "organism": "ECOLI",
    "gene": "g",
    "preds": 3,
    "goa_terms": 4,
    "goa_overlap": 2,
    "post_review_terms": 3,
    "post_review_overlap": 1,
    "core_terms": 1,
    "core_overlap": 1,
    "predicted_terms": ["GO:0000001", "GO:0000002", "GO:0000003"],
    "goa_overlap_terms": ["GO:0000001", "GO:0000002"],
    "post_review_overlap_terms": ["GO:0000001"],
    "core_overlap_terms": ["GO:0000001"],
}


def write_snapshot_inputs(root: Path, records: list[dict]) -> None:
    """Write the minimal policy and report that date and populate the overlap rows."""
    (root / BENCHMARK_POLICY).parent.mkdir(parents=True)
    (root / BENCHMARK_POLICY).write_text(
        "review_snapshot_commit: " + "a" * 40 + '\nreview_snapshot_date: "2026-01-02"\n'
    )
    (root / LEVELS_REPORT).parent.mkdir(parents=True)
    (root / LEVELS_REPORT).write_text(json.dumps(records))


@pytest.mark.parametrize(
    ("field", "expected"),
    [("in_goa", 2), ("in_post_review", 1), ("in_core", 1)],
)
def test_level_flags_reproduce_per_gene_overlap_counts(field: str, expected: int) -> None:
    rows = overlap_rows_for_record(RECORD)
    assert len(rows) == RECORD["preds"]
    assert sum(row[field] for row in rows) == expected


def test_prediction_count_mismatch_is_rejected() -> None:
    with pytest.raises(ValueError, match="predicted terms but preds"):
        overlap_rows_for_record(dict(RECORD, preds=4))


def test_rows_carry_snapshot_date_and_review_link(tmp_path: Path) -> None:
    write_snapshot_inputs(tmp_path, [RECORD])

    rows, metadata = collect_gogpt_overlap(tmp_path, lambda org, gene: f"{org}/{gene}.html")

    assert {row["snapshot_date"] for row in rows} == {"2026-01-02"}
    assert {row["review_link"] for row in rows} == {"ECOLI/g.html"}
    assert metadata["overlap_snapshot_date"] == "2026-01-02"
    assert metadata["overlap_gene_count"] == 1
    assert metadata["overlap_row_count"] == 3


def test_checkout_without_report_contributes_no_rows(tmp_path: Path) -> None:
    assert collect_gogpt_overlap(tmp_path, lambda org, gene: "") == ([], {})


def test_committed_report_rows_reproduce_pinned_snapshot_totals() -> None:
    """Facet counts in the browser equal the aggregate overlap pinned for the manuscript."""
    rows, metadata = collect_gogpt_overlap(REPO_ROOT, lambda org, gene: "")

    assert metadata["overlap_gene_count"] == 296
    assert len(rows) == 8806
    assert sum(row["in_goa"] for row in rows) == 1020
    assert sum(row["in_post_review"] for row in rows) == 849
    assert sum(row["in_core"] for row in rows) == 355


def test_browser_build_ships_overlap_dataset(tmp_path: Path) -> None:
    write_snapshot_inputs(tmp_path, [RECORD])
    review = tmp_path / "genes/ECOLI/g/g-ai-review.html"
    review.parent.mkdir(parents=True)
    review.write_text("<html></html>")
    output = tmp_path / "app/predictions"

    result = build_prediction_browser(tmp_path, output)

    data = read_browser_payload(output / "data.js")
    assert result["overlap"] == 3
    assert [row["term_id"] for row in data["overlap"]] == RECORD["predicted_terms"]
    assert data["overlap"][0]["review_link"] == "../../genes/ECOLI/g/g-ai-review.html"
    assert data["metadata"]["overlap_snapshot_date"] == "2026-01-02"
    sources = json.loads((output / "source-files.json").read_text())
    assert "genes/ECOLI/g/g-ai-review.html" in sources
