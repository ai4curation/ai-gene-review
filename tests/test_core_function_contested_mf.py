"""A core function with an MF_DARK knowledge gap gets an INFO note, not a warning to add a NEW row."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation import validate_gene_review
from ai_gene_review.validation.validation_report import ValidationSeverity

CHECK = "core_function_molecular_function_not_in_annotations"


def _review(with_gap: bool) -> dict:
    core = {
        "description": "Proposed isomerase (activity disputed).",
        "molecular_function": {"id": "GO:0051750", "label": "delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity"},
        "supported_by": [{"reference_id": "PMID:1", "supporting_text": "x"}],
    }
    if with_gap:
        core["knowledge_gaps"] = [{
            "gap_statement": "Whether the protein has the activity at all.",
            "gap_kind": ["BIOLOGY"],
            "dark_aspect": "MF_DARK",
        }]
    return {
        "id": "Q12345",
        "gene_symbol": "TEST",
        "taxon": {"id": "NCBITaxon:559292", "label": "Saccharomyces cerevisiae"},
        "description": "Test gene",
        "references": [{"id": "PMID:1", "title": "Test paper"}],
        "existing_annotations": [{
            "term": {"id": "GO:0051750", "label": "delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity"},
            "evidence_type": "EXP",
            "original_reference_id": "PMID:1",
            "review": {"action": "UNDECIDED"},
        }],
        "core_functions": [core],
    }


@pytest.mark.parametrize(
    "with_gap,severity", [(False, ValidationSeverity.WARNING), (True, ValidationSeverity.INFO)]
)
def test_contested_core_mf(tmp_path: Path, with_gap: bool, severity: ValidationSeverity):
    f = tmp_path / "TEST-ai-review.yaml"
    f.write_text(yaml.dump(_review(with_gap)))
    report = validate_gene_review(f, check_best_practices=True)
    assert [i.severity for i in report.issues if i.check_type == CHECK] == [severity]
