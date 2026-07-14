"""Regression tests for the canonicalized three-level GO-GPT comparison."""

from __future__ import annotations

import json
from pathlib import Path

from scripts.gogpt_compare_levels import (
    build_comparison,
    get_core_terms_from_document,
)
from scripts.gogpt_batch import load_review_terms


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_core_term_extraction_covers_every_go_valued_slot() -> None:
    review = {
        "core_functions": [
            {
                "molecular_function": {"id": "GO:0000001"},
                "contributes_to_molecular_function": {"id": "GO:0000002"},
                "directly_involved_in": [{"id": "GO:0000003"}],
                "in_complex": {"id": "GO:0000004"},
                "locations": [{"id": "GO:0000005"}],
            }
        ]
    }

    assert get_core_terms_from_document(review) == {
        "GO:0000001",
        "GO:0000002",
        "GO:0000003",
        "GO:0000004",
        "GO:0000005",
    }


def test_committed_three_level_report_matches_current_reviews() -> None:
    details, stats = build_comparison(REPO_ROOT)
    committed = json.loads(
        (REPO_ROOT / "reports/gogpt-comparison-levels.json").read_text()
    )

    assert committed == details
    assert len(details) == 299
    assert stats == {
        "goa": {"overlap": 1040, "total": 2960, "pred": 8871},
        "post_review": {"overlap": 847, "total": 2705, "pred": 8871},
        "core": {"overlap": 341, "total": 1196, "pred": 8871},
    }


def test_batch_reference_loader_uses_goa_aspects_and_core_slots(tmp_path: Path) -> None:
    goa = tmp_path / "gene-goa.tsv"
    goa.write_text(
        "GO TERM\tGO ASPECT\n"
        "GO:0000001\tmolecular_function\n"
        "GO:0000002\tbiological_process\n"
        "GO:0000003\tcellular_component\n"
    )
    review = tmp_path / "gene-ai-review.yaml"
    review.write_text(
        """
existing_annotations:
  - term: {id: GO:0000001}
    review: {action: ACCEPT}
  - term: {id: GO:0000002}
    review: {action: REMOVE}
  - term: {id: GO:0000003}
    review:
      action: MODIFY
      proposed_replacement_terms: [{id: GO:0000004}]
core_functions:
  - molecular_function: {id: GO:0000005}
    contributes_to_molecular_function: {id: GO:0000006}
    directly_involved_in: [{id: GO:0000007}]
    in_complex: {id: GO:0000008}
    locations: [{id: GO:0000009}]
"""
    )

    assert load_review_terms(review, goa) == {
        "MF": {"GO:0000001", "GO:0000005", "GO:0000006"},
        "BP": {"GO:0000007"},
        "CC": {"GO:0000004", "GO:0000008", "GO:0000009"},
    }
