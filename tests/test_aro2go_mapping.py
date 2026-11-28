"""Tests for the curated ARO->GO SSSOM mapping and its term-validator wiring.

- Unit tests check the SSSOM structure and that the generated nested term-tuple file
  (``aro2go.terms.yaml``) is in sync with the SSSOM source of truth.
- The integration test runs ``linkml-term-validator`` to confirm every ARO and GO
  CURIE resolves and its label matches the ontology.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
SSSOM = REPO / "projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml"
TERMS = REPO / "projects/ANTIMICROBIAL_RESISTANCE/aro2go.terms.yaml"
SCHEMA = REPO / "src/ai_gene_review/schema/aro_go_mapping.yaml"
CONVERTER = REPO / "projects/ANTIMICROBIAL_RESISTANCE/sssom_to_terms.py"
AR_DIR = REPO / "projects/ANTIMICROBIAL_RESISTANCE"
TRIAGE = AR_DIR / "aro_family_triage.yaml"


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
    # (subject, object) pairs are unique; a bifunctional family may carry two GO rows
    pairs = [(m["subject_id"], m["object_id"]) for m in mappings]
    assert len(pairs) == len(set(pairs)), "duplicate (subject_id, object_id)"
    for m in mappings:
        if m["object_id"] != "sssom:NoTermFound":
            assert 0 < m["confidence"] <= 1, m


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


def test_subsumption_classifier():
    """The gain report suppresses a candidate when a more specific child term is already present."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "annotation_gain_report", REPO / "projects/ANTIMICROBIAL_RESISTANCE/annotation_gain_report.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # GO:0034069 (aminoglycoside N-acetyltransferase) has child GO:0047663 (6'-N-acetyltransferase)
    desc = {"GO:0034069": {"GO:0047663"}}
    assert mod.classify_candidate("GO:0034069", {"GO:0047663", "GO:0046677"}, desc) == "redundant"
    assert mod.classify_candidate("GO:0034069", {"GO:0046677"}, desc) == "new"
    assert mod.classify_candidate("GO:0034069", {"GO:0034069"}, desc) == "already"
    # without a descendant index, only exact-match suppression applies
    assert mod.classify_candidate("GO:0034069", {"GO:0047663"}, None) == "new"


@pytest.mark.integration
def test_term_validator_passes():
    """linkml-term-validator confirms all ARO+GO ids resolve with matching labels.

    Needs the pinned CARD release in .cache/aro (``just fetch-aro``).
    """
    result = subprocess.run(
        [
            "uv", "run", "linkml-term-validator", "validate-data",
            str(TERMS),
            "-s", str(SCHEMA),
            "-t", "AROGOMappingSet",
            "--labels",
            "--no-cache",
            "-c", str(AR_DIR / "oak_config.yaml"),
        ],
        capture_output=True, text=True, cwd=REPO,
    )
    output = result.stdout + result.stderr
    assert "Validation passed" in output, output


# ---------------------------------------------------------------------------
# Propagation, release checks and triage (offline, on a miniature ARO)
# ---------------------------------------------------------------------------

def _load_module(name: str):
    """Load a project script as a module (projects/ is not an importable package)."""
    spec = importlib.util.spec_from_file_location(name, AR_DIR / f"{name}.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module  # dataclasses resolve their module through sys.modules
    spec.loader.exec_module(module)
    return module


aro_release = _load_module("aro_release")
AroOntology = aro_release.AroOntology
applicable_subjects = aro_release.applicable_subjects
check = aro_release.check
family_status = aro_release.family_status

MINI = AroOntology.from_obo_text(aro_release.MINI_OBO)


@pytest.mark.parametrize(
    "gene,subject,relation",
    [
        ("ARO:4", "ARO:4", "exact"),
        ("ARO:4", "ARO:2", "narrower"),
        # mechanism reached by is_a* o participates_in o is_a*
        ("ARO:4", "ARO:11", "participates_in"),
        ("ARO:4", "ARO:10", "participates_in"),
        ("ARO:2", "ARO:10", "participates_in"),
    ],
)
def test_applicable_subjects(gene, subject, relation):
    assert applicable_subjects(MINI, gene)[subject] == relation


def test_mechanism_not_reached_without_participates_in():
    """A gene in a family with no participates_in edge reaches no mechanism."""
    onto = AroOntology.from_obo_text(aro_release.MINI_OBO.replace("relationship: participates_in ARO:11\n", ""))
    assert "ARO:10" not in applicable_subjects(onto, "ARO:4")


def test_mechanism_rows_are_related_match():
    """Mechanism -> GO:0046677 rows cross axes, so they are relatedMatch, never enables."""
    doc = _load(SSSOM)
    mechanism_rows = [m for m in doc["mappings"] if m["object_id"] == "GO:0046677"]
    assert mechanism_rows
    for m in mechanism_rows:
        assert m["predicate_id"] == "skos:relatedMatch", m


PIN = {"card_version": "4.0.2", "aro_date": "2026-08-11", "aro_obo_sha256": "abc"}
META = {"card_version": "4.0.2", "aro_date": "2026-08-11", "aro_obo_sha256": "abc"}
SOURCE = "CARD 4.0.2 (ARO 2026-08-11)"


def _sssom(*rows):
    return {"subject_source_version": SOURCE, "mappings": list(rows)}


def _row(subject, label, obj="GO:0008800"):
    return {"subject_id": subject, "subject_label": label, "object_id": obj}


def test_check_clean():
    result = check(MINI, META, PIN, _sssom(_row("ARO:2", "beta-lactamase")), {"families": []}, {"ARO:3": "class A"})
    assert result.ok, result


def test_check_detects_label_drift():
    result = check(MINI, META, PIN, _sssom(_row("ARO:2", "beta lactamase")), {"families": []}, {})
    assert result.label_drift == [("aro2go.sssom.yaml", "ARO:2", "beta lactamase", "beta-lactamase")]


def test_check_detects_missing_term():
    result = check(MINI, META, PIN, _sssom(_row("ARO:99", "gone")), {"families": []}, {})
    assert result.missing == [("aro2go.sssom.yaml", "ARO:99", "gone")]


def test_check_detects_version_mismatch():
    newer = {"card_version": "4.0.3", "aro_date": "2026-12-01", "aro_obo_sha256": "def"}
    result = check(MINI, newer, PIN, _sssom(), {"families": []}, {})
    assert result.version_mismatch


def test_check_detects_changed_obo_for_same_version():
    result = check(MINI, {**META, "aro_obo_sha256": "other"}, PIN, _sssom(), {"families": []}, {})
    assert result.version_mismatch and "sha256" in result.version_mismatch[0]


def test_check_detects_untriaged_and_stale_triage():
    families = {"ARO:2": "beta-lactamase", "ARO:10": "antibiotic inactivation"}
    triage = {"families": [{"id": "ARO:2", "label": "beta-lactamase", "reason": "DEFERRED"}]}
    result = check(MINI, META, PIN, _sssom(_row("ARO:2", "beta-lactamase")), triage, families)
    assert result.untriaged_families == [("ARO:10", "antibiotic inactivation")]
    assert result.stale_triage == [("ARO:2", "beta-lactamase")]


def test_not_in_release_triage_is_not_a_missing_term():
    triage = {"families": [{"id": "ARO:99", "label": "gone family", "reason": "NOT_IN_ONTOLOGY_RELEASE"}]}
    result = check(MINI, META, PIN, _sssom(), triage, {"ARO:99": "gone family"})
    assert result.ok, result


def test_family_status_gap_via_ancestor():
    sssom = {"mappings": [{"subject_id": "ARO:2", "object_id": "sssom:NoTermFound"}]}
    assert family_status(MINI, {"ARO:3": "class A"}, sssom) == {"ARO:3": ("GO_GAP", "ARO:2")}


def test_triage_file_validates():
    result = subprocess.run(
        ["uv", "run", "linkml-validate", "-s", str(SCHEMA), "-C", "AROFamilyTriage", str(TRIAGE)],
        capture_output=True, text=True, cwd=REPO,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_triage_and_mapping_disjoint():
    """A family is either mapped/gapped in the SSSOM file or triaged, never both."""
    subjects = {m["subject_id"] for m in _load(SSSOM)["mappings"]}
    triaged = {f["id"] for f in _load(TRIAGE)["families"]}
    assert not subjects & triaged


def test_release_pin_matches_sssom():
    pin = _load(AR_DIR / "aro_release.yaml")
    assert _load(SSSOM)["subject_source_version"] == f"CARD {pin['card_version']} (ARO {pin['aro_date']})"


def test_cli_check_without_release_explains(tmp_path):
    from typer.testing import CliRunner

    result = CliRunner().invoke(aro_release.app, ["check", "--cache", str(tmp_path)])
    assert result.exit_code != 0
    assert "fetch-aro" in result.output


@pytest.mark.integration
def test_check_against_pinned_release():
    """The mapping is consistent with the pinned CARD release (needs ``just fetch-aro``)."""
    result = subprocess.run(
        ["uv", "run", "python", str(AR_DIR / "aro_release.py"), "check"], capture_output=True, text=True, cwd=REPO
    )
    assert result.returncode == 0, result.stdout + result.stderr
