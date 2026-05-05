"""Tests for the external mapping sidecar schema."""

from pathlib import Path

import yaml


REPO_ROOT = next(
    path for path in Path(__file__).resolve().parents if (path / "project.justfile").exists()
)
SCHEMA_PATH = REPO_ROOT / "src/ai_gene_review/schema/ext_mapping.yaml"
MAPPING_DIR = REPO_ROOT / "projects/PROTEOSTASIS/mappings"


def _mapping_sets() -> dict[str, dict]:
    return {
        path.name: yaml.safe_load(path.read_text(encoding="utf-8"))
        for path in sorted(MAPPING_DIR.glob("*.yaml"))
    }


def _curations(mapping_sets: dict[str, dict]) -> list[dict]:
    rows = []
    for file_name, mapping_set in mapping_sets.items():
        for curation in mapping_set["subject_curations"]:
            row = dict(curation)
            row["mapping_file"] = file_name
            rows.append(row)
    return rows


def _find_curation(mapping_sets: dict[str, dict], subject_code: str) -> dict:
    matches = [
        curation
        for curation in _curations(mapping_sets)
        if curation["subject_code"] == subject_code
    ]
    assert len(matches) == 1
    return matches[0]


def test_ext_mapping_schema_has_go_term_binding() -> None:
    """The schema should bind GO target IDs to the GO dynamic enum."""
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))

    assert "ExternalMappingSet" in schema["classes"]
    binding = schema["slots"]["target_term"]["bindings"][0]

    assert binding["binds_value_of"] == "id"
    assert binding["range"] == "GOTermEnum"
    assert schema["slots"]["subject_curations"]["range"] == "SubjectCuration"
    assert schema["slots"]["curation_status"]["range"] == "CurationStatusEnum"
    assert schema["slots"]["curation_status"]["required"] is True
    assert schema["enums"]["GOTermEnum"]["reachable_from"]["source_nodes"] == [
        "GO:0003674",
        "GO:0008150",
        "GO:0005575",
    ]
    assert schema["classes"]["GOTerm"]["slot_usage"]["label"]["required"] is True
    assert schema["slots"]["representative_genes"]["multivalued"] is True
    assert "too_broad_to_propagate" in schema["enums"]["MappingScopeEnum"]["permissible_values"]
    assert set(schema["enums"]["CurationStatusEnum"]["permissible_values"]) == {
        "pending_review",
        "mapped",
        "context_only",
        "no_mapping",
        "deferred",
    }


def test_ext_mapping_sets_use_unified_subject_curations() -> None:
    """Every PN node should be represented as one explicit curation record."""
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    mapping_sets = _mapping_sets()
    curations = _curations(mapping_sets)

    subject_levels = set(schema["enums"]["SourceHierarchyLevelEnum"]["permissible_values"])
    statuses = set(schema["enums"]["CurationStatusEnum"]["permissible_values"])
    scopes = set(schema["enums"]["MappingScopeEnum"]["permissible_values"])

    assert set(mapping_sets) == {
        "autophagy_lysosome_pathway.yaml",
        "chaperone_systems.yaml",
        "extracellular_proteostasis.yaml",
        "er_proteostasis.yaml",
        "mitochondrial_proteostasis.yaml",
        "nuclear_proteostasis.yaml",
        "pn_regulation.yaml",
        "translation.yaml",
        "ubiquitin_proteasome_system.yaml",
    }
    assert sum("mappings" in mapping_set for mapping_set in mapping_sets.values()) == 0
    assert sum("unmapped_subjects" in mapping_set for mapping_set in mapping_sets.values()) == 0
    assert len(curations) == 2029
    assert len({(row["subject_level"], row["subject_code"]) for row in curations}) == 2029

    for row in curations:
        assert row["subject_level"] in subject_levels
        assert row["curation_status"] in statuses
        if row["curation_status"] in {"mapped", "context_only"}:
            assert row["target_term"]["id"].startswith("GO:")
            assert row["target_term"]["label"]
            assert row["mapping_scope"] in scopes
        else:
            assert "target_term" not in row
            assert "mapping_scope" not in row

    status_counts = {
        status: sum(row["curation_status"] == status for row in curations)
        for status in statuses
    }
    assert status_counts == {
        "pending_review": 1227,
        "mapped": 401,
        "context_only": 64,
        "no_mapping": 337,
        "deferred": 0,
    }


def test_representative_curations_survived_migration() -> None:
    """Key curated records should retain status, target, and rationale fields."""
    mapping_sets = _mapping_sets()

    alp_class = _find_curation(
        mapping_sets,
        "Autophagy-Lysosome Pathway|Autophagophore initiation and elongation",
    )
    assert alp_class["curation_status"] == "context_only"
    assert alp_class["target_term"]["id"] == "GO:0016236"
    assert alp_class["mapping_scope"] == "too_broad_to_propagate"

    hsp90 = _find_curation(
        mapping_sets,
        "Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90",
    )
    assert hsp90["curation_status"] == "mapped"
    assert hsp90["target_term"]["id"] == "GO:0140662"

    translation_branch = _find_curation(mapping_sets, "Translation")
    assert translation_branch["curation_status"] == "context_only"
    assert translation_branch["mapping_scope"] == "too_broad_to_propagate"

    eif4f = _find_curation(
        mapping_sets,
        "Translation|Cytosolic translation|Translation initiation|eIF4F complex",
    )
    assert eif4f["curation_status"] == "mapped"
    assert eif4f["target_term"]["id"] == "GO:0016281"

    mitochondrial_chaperone = _find_curation(
        mapping_sets,
        "Mitochondrial proteostasis|Chaperone",
    )
    assert mitochondrial_chaperone["curation_status"] == "no_mapping"
