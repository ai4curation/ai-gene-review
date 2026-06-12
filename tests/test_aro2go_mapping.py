"""Tests for the curated ARO->GO SSSOM mapping and its term-validator wiring.

- Unit tests check the SSSOM structure and that the generated nested term-tuple file
  (``aro2go.terms.yaml``) is in sync with the SSSOM source of truth.
- The integration test runs ``linkml-term-validator`` to confirm every ARO and GO
  CURIE resolves and its label matches the ontology.
"""

import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
SSSOM = REPO / "projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml"
TERMS = REPO / "projects/ANTIMICROBIAL_RESISTANCE/aro2go.terms.yaml"
SCHEMA = REPO / "src/ai_gene_review/schema/aro_go_mapping.yaml"
CONVERTER = REPO / "projects/ANTIMICROBIAL_RESISTANCE/sssom_to_terms.py"
OAK_CONFIG = REPO / "conf/oak_config.yaml"


def _load(path: Path) -> dict:
    return yaml.safe_load(path.read_text())


def test_sssom_structure():
    """Every mapping is a CURIE+label tuple; gap rows use the SSSOM NoTermFound convention."""
    doc = _load(SSSOM)
    mappings = doc["mappings"]
    assert mappings, "no mappings found"
    for m in mappings:
        assert m["subject_id"].startswith("ARO:"), m
        assert m["subject_label"], m
        assert m["mapping_justification"], m
        if m["object_id"] == "sssom:NoTermFound":
            # gap row: records an ARO family with no suitable GO term
            assert m.get("object_source") == "obo:go.owl", m
            assert m.get("comment"), m
        else:
            assert m["object_id"].startswith("GO:"), m
            assert m["object_label"], m
            assert m["predicate_id"].split(":")[0] in {"RO", "skos"}, m
            assert m["predicate_label"], m
    # subjects are unique (one mapping row per ARO term)
    subjects = [m["subject_id"] for m in mappings]
    assert len(subjects) == len(set(subjects)), "duplicate subject_id"


def test_gap_rows_present():
    """Gap rows (NoTermFound) are recorded in the mapping file, not just in prose."""
    doc = _load(SSSOM)
    gaps = [m for m in doc["mappings"] if m["object_id"] == "sssom:NoTermFound"]
    assert gaps, "expected at least one NoTermFound gap row"


def test_terms_file_in_sync():
    """aro2go.terms.yaml must equal a fresh conversion of the SSSOM source."""
    result = subprocess.run(
        ["uv", "run", "python", str(CONVERTER), str(SSSOM), "-o", "/tmp/_aro2go_check.terms.yaml"],
        capture_output=True, text=True, cwd=REPO,
    )
    assert result.returncode == 0, result.stderr
    regenerated = Path("/tmp/_aro2go_check.terms.yaml").read_text()
    committed = TERMS.read_text()
    assert regenerated == committed, (
        "aro2go.terms.yaml is out of sync with aro2go.sssom.yaml; "
        "regenerate with: uv run python projects/ANTIMICROBIAL_RESISTANCE/sssom_to_terms.py "
        "projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml -o projects/ANTIMICROBIAL_RESISTANCE/aro2go.terms.yaml"
    )


@pytest.mark.integration
def test_term_validator_passes():
    """linkml-term-validator confirms all ARO+GO ids resolve with matching labels."""
    result = subprocess.run(
        [
            "uv", "run", "linkml-term-validator", "validate-data",
            str(TERMS),
            "-s", str(SCHEMA),
            "-t", "AROGOMappingSet",
            "--labels",
            "-c", str(OAK_CONFIG),
        ],
        capture_output=True, text=True, cwd=REPO,
    )
    output = result.stdout + result.stderr
    assert "Validation passed" in output, output
