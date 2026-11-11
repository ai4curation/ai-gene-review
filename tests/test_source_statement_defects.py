"""Tests for the statement-defect asserted_value check."""

from pathlib import Path

import pytest

from ai_gene_review.validation.source_statement_defects import (
    STATEMENT_DEFECT_CHECK,
    validate_statement_defects,
)
from ai_gene_review.validation.validation_report import ValidationReport

SOURCE = """---
provider: wormbase
---

# WormBase gene description for g (worm)

ATG-2 has noobvious phenotype in mass RNAi assays.
"""


def _data(defect_type: str, value: str) -> dict:
    return {"references": [{"id": "file:worm/g/g-deep-research-wormbase.md", "reference_review": {
        "source_defects": [{"defect_type": defect_type, "asserted_value": value}]}}]}


@pytest.mark.parametrize(
    "defect_type,value,warns",
    [
        ("OUTDATED_STATEMENT", "ATG-2 has noobvious phenotype in mass RNAi assays", False),
        ("WRONG_STATEMENT", "ATG-2   has noobvious\nphenotype", False),
        ("OUTDATED_STATEMENT", "WB:WBGene00019748", True),
        ("WRONG_STATEMENT", "ATG-2 has no obvious phenotype", True),
        ("MISSING_STATEMENT", "WB:WBGene00019748", False),
    ],
)
def test_statement_value_must_be_in_source(tmp_path: Path, defect_type: str, value: str, warns: bool):
    gene = tmp_path / "genes" / "worm" / "g"
    gene.mkdir(parents=True)
    (gene / "g-deep-research-wormbase.md").write_text(SOURCE)
    report = ValidationReport(file_path=Path("g-ai-review.yaml"), is_valid=True)
    validate_statement_defects(_data(defect_type, value), report, project_root=tmp_path)
    assert any(i.check_type == STATEMENT_DEFECT_CHECK for i in report.issues) is warns
