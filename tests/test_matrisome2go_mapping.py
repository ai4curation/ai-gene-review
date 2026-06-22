"""Tests for the curated matrisome-family->GO SSSOM mapping and the missing-annotation report.

- Unit tests check the SSSOM structure, the gap-row convention, and that the generated nested
  term-tuple file (``matrisome2go.terms.yaml``) is in sync with the SSSOM source of truth.
- Unit tests exercise the report's pure logic (family->GO loading, species-aware masterlist lookup,
  subsumption classifier) on small fixtures.
- The integration test runs ``linkml-term-validator`` to confirm every GO CURIE resolves with a
  matching, non-obsolete label.
"""

import importlib.util
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
SSSOM = REPO / "projects/MATRISOME/matrisome2go.sssom.yaml"
TERMS = REPO / "projects/MATRISOME/matrisome2go.terms.yaml"
SCHEMA = REPO / "src/ai_gene_review/schema/matrisome_go_mapping.yaml"
CONVERTER = REPO / "projects/MATRISOME/sssom_to_terms.py"
REPORT = REPO / "projects/MATRISOME/missing_annotation_report.py"
DATA = REPO / "projects/MATRISOME/data"
OAK_CONFIG = REPO / "conf/oak_config.yaml"

CORE_FAMILIES = {"Collagens", "ECM Glycoproteins", "Proteoglycans"}
ASSOCIATED_FAMILIES = {"ECM-affiliated Proteins", "ECM Regulators", "Secreted Factors"}

# The masterlist CSVs are not committed (project is parked; see projects/MATRISOME/README.md).
# Tests that need them are skipped unless the data has been regenerated locally.
needs_masterlist = pytest.mark.skipif(
    not (DATA / "matrisome_human.csv").exists(),
    reason="matrisome masterlist CSVs not present (regenerate per projects/MATRISOME/data/README.md)",
)


def _load(path: Path) -> dict:
    return yaml.safe_load(path.read_text())


def _report_module():
    spec = importlib.util.spec_from_file_location("missing_annotation_report", REPORT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_sssom_structure():
    """Every mapping is a CURIE+label tuple; gap rows use the SSSOM NoTermFound convention."""
    doc = _load(SSSOM)
    mappings = doc["mappings"]
    assert mappings, "no mappings found"
    for m in mappings:
        assert m["subject_id"].startswith("matrisome:"), m
        assert m["subject_label"], m
        assert m["mapping_justification"], m
        if m["object_id"] == "sssom:NoTermFound":
            assert m.get("object_source") == "obo:go.owl", m
            assert m.get("comment"), m
        else:
            assert m["object_id"].startswith("GO:"), m
            assert m["object_label"], m
            assert m["predicate_id"].split(":")[0] in {"RO", "skos"}, m
            assert m["predicate_label"], m
    subjects = [m["subject_id"] for m in mappings]
    assert len(subjects) == len(set(subjects)), "duplicate subject_id"


def test_core_mapped_associated_gapped():
    """Core families map to GO; associated families are deliberately NoTermFound gap rows."""
    doc = _load(SSSOM)
    mapped = {
        m["subject_label"] for m in doc["mappings"] if m["object_id"].startswith("GO:")
    }
    gapped = {
        m["subject_label"]
        for m in doc["mappings"]
        if m["object_id"] == "sssom:NoTermFound"
    }
    assert mapped == CORE_FAMILIES
    assert gapped == ASSOCIATED_FAMILIES


def test_no_obsolete_go0062023_object():
    """Guard against mapping TO the obsoleted collagen-containing ECM term (replaced by GO:0031012).

    The id may appear in an explanatory comment, but must never be a mapping object_id.
    """
    doc = _load(SSSOM)
    object_ids = {m["object_id"] for m in doc["mappings"]}
    assert "GO:0062023" not in object_ids, (
        "GO:0062023 was obsoleted (replaced_by GO:0031012); use GO:0031012 for ECM localization"
    )


def test_terms_file_in_sync(tmp_path):
    """matrisome2go.terms.yaml must equal a fresh conversion of the SSSOM source."""
    out = tmp_path / "check.terms.yaml"
    result = subprocess.run(
        ["uv", "run", "python", str(CONVERTER), str(SSSOM), "-o", str(out)],
        capture_output=True,
        text=True,
        cwd=REPO,
    )
    assert result.returncode == 0, result.stderr
    assert out.read_text() == TERMS.read_text(), (
        "matrisome2go.terms.yaml is out of sync; regenerate with "
        "uv run python projects/MATRISOME/sssom_to_terms.py "
        "projects/MATRISOME/matrisome2go.sssom.yaml -o projects/MATRISOME/matrisome2go.terms.yaml"
    )


def test_load_family_go_mappings():
    """Only the three core families (mapped to GO) are returned; gap rows are excluded."""
    mod = _report_module()
    fam = mod.load_family_go_mappings(SSSOM)
    assert set(fam) == CORE_FAMILIES
    assert fam["ECM Glycoproteins"] == ("GO:0031012", "extracellular matrix")


@needs_masterlist
def test_load_matrisome_is_species_partitioned():
    """The masterlist loader keeps a per-species lookup; human SPOCK1 resolves to a core proteoglycan."""
    mod = _report_module()
    by_species = mod.load_matrisome(DATA)
    assert "human" in by_species and "mouse" in by_species
    assert by_species["human"]["SPOCK1"] == ("Core matrisome", "Proteoglycans")
    # SERPINH1 (HSP47) is associated, not core -- it must NOT be flagged for ECM localization
    assert by_species["human"]["SERPINH1"][0] == "Matrisome-associated"


def test_subsumption_classifier():
    """A candidate is suppressed when a more specific (is_a descendant) term is already present."""
    mod = _report_module()
    desc = {"GO:0031012": {"GO:0005604"}}  # basement membrane is_a extracellular matrix
    assert mod.classify_candidate("GO:0031012", {"GO:0005604"}, desc) == "redundant"
    assert mod.classify_candidate("GO:0031012", {"GO:0005634"}, desc) == "new"
    assert mod.classify_candidate("GO:0031012", {"GO:0031012"}, desc) == "already"
    assert mod.classify_candidate("GO:0031012", {"GO:0005604"}, None) == "new"


@needs_masterlist
def test_compute_finds_core_gap_and_skips_associated_and_nonmetazoan(tmp_path):
    """End-to-end on a tiny fixture: core gap -> candidate; associated and bacterial genes -> skipped."""
    mod = _report_module()
    genes = tmp_path / "genes"
    header = (
        "GENE PRODUCT DB\tGENE PRODUCT ID\tSYMBOL\tQUALIFIER\tGO TERM\tGO NAME\tGO ASPECT\t"
        "ECO ID\tGO EVIDENCE CODE\tREFERENCE\tWITH/FROM\tTAXON ID\tTAXON NAME\tASSIGNED BY\t"
        "GENE NAME\tDATE\n"
    )

    def write(species, gene, symbol, acc, go_ids):
        d = genes / species / gene
        d.mkdir(parents=True)
        rows = header
        if not go_ids:
            go_ids = [""]
        for go in go_ids:
            rows += f"UniProtKB\t{acc}\t{symbol}\t\t{go}\t\tcellular_component\t\tIDA\t\t\t9606\t\t\t\t\n"
        (d / f"{gene}-goa.tsv").write_text(rows)

    # human core proteoglycan with NO ECM term -> candidate
    write("human", "DCN", "DCN", "P07585", [])
    # human core glycoprotein that already has GO:0031012 -> suppressed (already)
    write("human", "FN1", "FN1", "P02751", ["GO:0031012"])
    # human associated regulator (SERPINH1) -> never proposed
    write("human", "SERPINH1", "SERPINH1", "P50454", [])
    # bacterial gene whose symbol collides with a human matrisome alias -> skipped (non-metazoan)
    write("PSEPK", "cca", "cca", "Q88QU2", [])

    by_species = mod.load_matrisome(DATA)
    fam = mod.load_family_go_mappings(SSSOM)
    rows, stats = mod.compute(
        genes, by_species, fam, go_descendants={"GO:0031012": set()}
    )

    flagged = {(r["species"], r["gene"]) for r in rows}
    assert ("human", "DCN") in flagged
    assert ("human", "FN1") not in flagged
    assert ("human", "SERPINH1") not in flagged
    assert ("PSEPK", "cca") not in flagged
    assert stats["candidates"] == len(rows) >= 1


@pytest.mark.integration
def test_term_validator_passes():
    """linkml-term-validator confirms all GO ids resolve with matching, non-obsolete labels."""
    result = subprocess.run(
        [
            "uv",
            "run",
            "linkml-term-validator",
            "validate-data",
            str(TERMS),
            "-s",
            str(SCHEMA),
            "-t",
            "MatrisomeGOMappingSet",
            "--labels",
            "-c",
            str(OAK_CONFIG),
        ],
        capture_output=True,
        text=True,
        cwd=REPO,
    )
    output = result.stdout + result.stderr
    assert "Validation passed" in output, output
