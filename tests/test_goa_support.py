"""Tests for rejecting GOA files as supporting evidence."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation import ValidationSeverity
from ai_gene_review.validation.goa_support import (
    GOA_SUPPORT_CHECK,
    goa_support_paths,
    main,
    validate_goa_support,
)
from ai_gene_review.validation.validation_report import ValidationReport

OWN_GOA = "file:PSEPK/coaD/coaD-goa.tsv"
UNIPROT = "file:PSEPK/coaD/coaD-uniprot.txt"


def _review_file(root: Path) -> Path:
    path = root / "genes" / "PSEPK" / "coaD" / "coaD-ai-review.yaml"
    path.parent.mkdir(parents=True)
    path.write_text("id: Q88CQ7\n")
    return path


def _review(supported_by, action="ACCEPT"):
    return {
        "id": "Q88CQ7",
        "gene_symbol": "coaD",
        "existing_annotations": [
            {
                "term": {"id": "GO:0005737", "label": "cytoplasm"},
                "evidence_type": "IEA",
                "original_reference_id": "GO_REF:0000120",
                "review": {"action": action, "supported_by": supported_by},
            }
        ],
    }


@pytest.mark.parametrize("action", ["ACCEPT", "KEEP_AS_NON_CORE", "REMOVE", "MARK_AS_OVER_ANNOTATED", "UNDECIDED"])
@pytest.mark.parametrize(
    "reference_id",
    [OWN_GOA, "file:genes/PSEPK/coaD/coaD-goa.tsv"],
)
def test_own_goa_is_flagged_for_every_action(tmp_path, action, reference_id):
    data = _review(
        [
            {"reference_id": reference_id, "supporting_text": "GO:0005737\tcytoplasm"},
            {"reference_id": UNIPROT, "supporting_text": "SUBCELLULAR LOCATION: Cytoplasm"},
        ],
        action,
    )
    assert goa_support_paths(data, _review_file(tmp_path), tmp_path) == [
        ("existing_annotations[0].review.supported_by[0]", True)
    ]


@pytest.mark.parametrize(
    "reference_id",
    [UNIPROT, "PMID:27041211", "GO_REF:0000120", "file:PSEPK/coaD/coaD-notes.md"],
)
def test_other_sources_are_not_flagged(tmp_path, reference_id):
    data = _review([{"reference_id": reference_id, "supporting_text": "x"}])
    assert goa_support_paths(data, _review_file(tmp_path), tmp_path) == []


@pytest.mark.parametrize(
    "reference_id",
    ["file:PSEPK/coaE/coaE-goa.tsv", "file:genes/human/AMN/AMN-goa.tsv"],
)
def test_another_genes_goa_is_flagged(tmp_path, reference_id):
    data = _review([{"reference_id": reference_id, "supporting_text": "x"}])
    assert goa_support_paths(data, _review_file(tmp_path), tmp_path) == [
        ("existing_annotations[0].review.supported_by[0]", False)
    ]


def test_core_functions_are_checked_but_reference_listings_are_not(tmp_path):
    data = {
        "core_functions": [{"supported_by": [{"reference_id": OWN_GOA, "supporting_text": "x"}]}],
        "references": [
            {"id": OWN_GOA, "title": "GOA", "findings": [{"supporting_text": "x"}]},
            {"id": OWN_GOA, "title": "GOA", "findings": []},
        ],
    }
    assert goa_support_paths(data, _review_file(tmp_path), tmp_path) == [
        ("core_functions[0].supported_by[0]", True),
    ]


def test_reported_as_errors(tmp_path):
    data = _review(
        [
            {"reference_id": OWN_GOA, "supporting_text": "GO:0005737\tcytoplasm"},
            {"reference_id": "file:PSEPK/coaE/coaE-goa.tsv", "supporting_text": "x"},
        ]
    )
    report = ValidationReport(file_path=tmp_path, is_valid=True)
    validate_goa_support(data, report, _review_file(tmp_path), tmp_path)
    issues = [i for i in report.issues if i.check_type == GOA_SUPPORT_CHECK]
    assert [i.severity for i in issues] == [ValidationSeverity.ERROR.value] * 2
    assert "own GOA file" in issues[0].message
    assert "another gene's GOA file" in issues[1].message


@pytest.mark.parametrize(
    ("reference_id", "exit_code"), [(OWN_GOA, 1), (UNIPROT, 0)]
)
def test_cli_exit_code(tmp_path, capsys, reference_id, exit_code):
    path = tmp_path / "x-sft-predictions.yaml"
    path.write_text(yaml.safe_dump({"predictions": [{"review": {
        "assessment": "NPI",
        "supported_by": [{"reference_id": reference_id, "supporting_text": "x"}],
    }}]}))
    assert main([str(path)]) == exit_code
    out = capsys.readouterr().out
    assert ("supported_by[0]" in out) == bool(exit_code)
    assert ("use UNDECIDED" in out) == bool(exit_code)
