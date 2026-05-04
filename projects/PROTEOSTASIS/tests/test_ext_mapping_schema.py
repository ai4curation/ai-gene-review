"""Tests for the external mapping sidecar schema."""

from pathlib import Path

import yaml


REPO_ROOT = next(
    path for path in Path(__file__).resolve().parents if (path / "project.justfile").exists()
)
SCHEMA_PATH = REPO_ROOT / "src/ai_gene_review/schema/ext_mapping.yaml"
MAPPING_DIR = REPO_ROOT / "projects/PROTEOSTASIS/mappings"


def test_ext_mapping_schema_has_go_term_binding() -> None:
    """The schema should bind GO target IDs to the GO dynamic enum."""
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))

    assert "ExternalMappingSet" in schema["classes"]
    binding = schema["slots"]["target_term"]["bindings"][0]

    assert binding["binds_value_of"] == "id"
    assert binding["range"] == "GOTermEnum"
    assert schema["slots"]["unmapped_subjects"]["range"] == "UnmappedSubject"
    assert schema["slots"]["unmapped_status"]["range"] == "UnmappedStatusEnum"
    assert schema["slots"]["unmapped_status"]["required"] is True
    assert schema["enums"]["GOTermEnum"]["reachable_from"]["source_nodes"] == [
        "GO:0003674",
        "GO:0008150",
        "GO:0005575",
    ]
    assert schema["classes"]["GOTerm"]["slot_usage"]["label"]["required"] is True
    assert schema["slots"]["representative_genes"]["multivalued"] is True
    assert "too_broad_to_propagate" in schema["enums"]["MappingScopeEnum"]["permissible_values"]


def test_ext_mapping_sets_use_schema_values() -> None:
    """The curated mapping sets should use declared scope and level values."""
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    mapping_sets = {
        path.name: yaml.safe_load(path.read_text(encoding="utf-8"))
        for path in sorted(MAPPING_DIR.glob("*.yaml"))
    }

    subject_levels = set(schema["enums"]["SourceHierarchyLevelEnum"]["permissible_values"])
    scopes = set(schema["enums"]["MappingScopeEnum"]["permissible_values"])
    unmapped_statuses = set(schema["enums"]["UnmappedStatusEnum"]["permissible_values"])

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
    assert sum(len(mapping_set["mappings"]) for mapping_set in mapping_sets.values()) >= 100
    assert (
        sum(len(mapping_set.get("unmapped_subjects", [])) for mapping_set in mapping_sets.values())
        >= 1700
    )
    assert all(
        unmapped["unmapped_status"] in unmapped_statuses
        for mapping_set in mapping_sets.values()
        for unmapped in mapping_set.get("unmapped_subjects", [])
    )
    assert any(
        unmapped["unmapped_status"] == "pending_review"
        for mapping_set in mapping_sets.values()
        for unmapped in mapping_set.get("unmapped_subjects", [])
    )
    assert any(
        unmapped["unmapped_status"] == "no_mapping_appropriate"
        for mapping_set in mapping_sets.values()
        for unmapped in mapping_set.get("unmapped_subjects", [])
    )

    example_set = mapping_sets["autophagy_lysosome_pathway.yaml"]
    example = example_set["mappings"][0]

    assert example_set["id"] == "pn_mapping_set:autophagy_lysosome_pathway"
    assert len(example_set["mappings"]) >= 40
    assert "subject_code" in example
    assert "id" not in example
    assert "label" not in example
    assert example["subject_level"] in subject_levels
    assert example["mapping_scope"] in scopes
    assert example["subject_code"] == "Autophagy-Lysosome Pathway|Chaperone-mediated autophagy"
    assert example["target_term"]["id"] == "GO:0061684"
    assert example["target_term"]["label"] == "chaperone-mediated autophagy"

    hsp90_mapping = next(
        mapping
        for mapping in mapping_sets["chaperone_systems.yaml"]["mappings"]
        if mapping["subject_code"] == "HSP90"
    )
    assert hsp90_mapping["conditions"] == [
        {"condition_level": "class", "condition_code": "Chaperone"},
        {"condition_level": "group", "condition_code": "HSP90 system"},
    ]
    ferritinophagy_mapping = next(
        mapping
        for mapping in example_set["mappings"]
        if mapping["subject_code"].endswith("|Ferritinophagy")
    )
    assert ferritinophagy_mapping["target_term"]["id"] == "GO:0160247"
    assert ferritinophagy_mapping["target_term"]["label"] == "autophagy cargo adaptor activity"
    alp_class_mapping = next(
        mapping
        for mapping in example_set["mappings"]
        if mapping["subject_code"] == "Autophagy-Lysosome Pathway|Autophagophore initiation and elongation"
    )
    assert alp_class_mapping["target_term"]["id"] == "GO:0016236"
    assert alp_class_mapping["target_term"]["label"] == "macroautophagy"

    nuclear_mapping = next(
        mapping
        for mapping in mapping_sets["nuclear_proteostasis.yaml"]["mappings"]
        if mapping["subject_code"] == "Nuclear proteostasis|Protein transport|Nuclear pore complex"
    )
    assert nuclear_mapping["target_term"]["id"] == "GO:0005643"
    assert nuclear_mapping["target_term"]["label"] == "nuclear pore"
    importin_alpha_mapping = next(
        mapping
        for mapping in mapping_sets["nuclear_proteostasis.yaml"]["mappings"]
        if mapping["subject_code"]
        == "Nuclear proteostasis|Protein transport|Nuclear transport receptor|Importin, alpha type"
    )
    assert importin_alpha_mapping["target_term"]["id"] == "GO:0006913"
    assert importin_alpha_mapping["target_term"]["label"] == "nucleocytoplasmic transport"
    histone_chaperone_mapping = next(
        mapping
        for mapping in mapping_sets["nuclear_proteostasis.yaml"]["mappings"]
        if mapping["subject_code"] == "Nuclear proteostasis|Chaperone|Histone chaperone"
    )
    assert histone_chaperone_mapping["target_term"]["id"] == "GO:0140713"
    assert histone_chaperone_mapping["target_term"]["label"] == "histone chaperone activity"
    nuclear_receptor_group = next(
        mapping
        for mapping in mapping_sets["nuclear_proteostasis.yaml"]["mappings"]
        if mapping["subject_code"] == "Nuclear proteostasis|Protein transport|Nuclear transport receptor"
    )
    assert nuclear_receptor_group["representative_genes"] == [
        "KPNB1",
        "KPNA2",
        "XPO1",
        "HIKESHI",
    ]
    extracellular_mapping = next(
        mapping
        for mapping in mapping_sets["extracellular_proteostasis.yaml"]["mappings"]
        if mapping["subject_code"] == "Extracellular proteostasis|Protease|Plasma membrane"
    )
    assert extracellular_mapping["target_term"]["id"] == "GO:0005886"
    assert extracellular_mapping["target_term"]["label"] == "plasma membrane"

    eif3_mapping = next(
        mapping
        for mapping in mapping_sets["translation.yaml"]["mappings"]
        if mapping["subject_code"]
        == "Translation|Cytosolic translation|Translation initiation|eIF3 complex"
    )
    assert eif3_mapping["target_term"]["id"] == "GO:0005852"
    assert (
        eif3_mapping["target_term"]["label"]
        == "eukaryotic translation initiation factor 3 complex"
    )
    translation_branch_mapping = next(
        mapping
        for mapping in mapping_sets["translation.yaml"]["mappings"]
        if mapping["subject_code"] == "Translation"
    )
    assert translation_branch_mapping["mapping_scope"] == "too_broad_to_propagate"
    cytosolic_translation_mapping = next(
        mapping
        for mapping in mapping_sets["translation.yaml"]["mappings"]
        if mapping["subject_code"] == "Translation|Cytosolic translation"
    )
    assert cytosolic_translation_mapping["mapping_scope"] == "too_broad_to_propagate"
    ribosome_biogenesis_mapping = next(
        mapping
        for mapping in mapping_sets["translation.yaml"]["mappings"]
        if mapping["subject_code"] == "Translation|Cytosolic translation|Ribosome biogenesis factor"
    )
    assert ribosome_biogenesis_mapping["target_term"]["id"] == "GO:0042254"
    assert ribosome_biogenesis_mapping["target_term"]["label"] == "ribosome biogenesis"
    explicit_unmapped = mapping_sets["translation.yaml"]["unmapped_subjects"][0]
    assert (
        explicit_unmapped["subject_code"]
        == "Translation|Cytosolic translation|Translation initiation|eIF4F complex"
    )
    assert explicit_unmapped["subject_level"] == "type"
    assert explicit_unmapped["unmapped_status"] == "deferred"
    explicit_unmapped_2 = mapping_sets["translation.yaml"]["unmapped_subjects"][1]
    assert (
        explicit_unmapped_2["subject_code"]
        == "Translation|Mitochondrial translation|Ribosome"
    )
    assert explicit_unmapped_2["subject_level"] == "group"
    assert explicit_unmapped_2["unmapped_status"] == "deferred"

    ups_mapping = next(
        mapping
        for mapping in mapping_sets["ubiquitin_proteasome_system.yaml"]["mappings"]
        if mapping["subject_code"]
        == (
            "Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|"
            "idiosyncratic RING complex|Anaphase Promoting Complex"
        )
    )
    assert ups_mapping["target_term"]["id"] == "GO:0005680"
    assert ups_mapping["target_term"]["label"] == "anaphase-promoting complex"
    ups_translation_mapping = next(
        mapping
        for mapping in mapping_sets["ubiquitin_proteasome_system.yaml"]["mappings"]
        if mapping["subject_code"]
        == "Ubiquitin Proteasome System|Ubiquitin and UBL binding|translation"
    )
    assert ups_translation_mapping["mapping_scope"] == "too_broad_to_propagate"
    pi3k_group_mapping = next(
        mapping
        for mapping in mapping_sets["autophagy_lysosome_pathway.yaml"]["mappings"]
        if mapping["subject_code"]
        == "Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct"
    )
    assert pi3k_group_mapping["target_term"]["id"] == "GO:0035032"
    assert (
        pi3k_group_mapping["target_term"]["label"]
        == "phosphatidylinositol 3-kinase complex, class III"
    )
    oxidative_stress_mapping = next(
        mapping
        for mapping in mapping_sets["pn_regulation.yaml"]["mappings"]
        if mapping["subject_code"] == "PN regulation|Transcription factor|Oxidative stress response"
    )
    assert oxidative_stress_mapping["target_term"]["id"] == "GO:1900407"
    assert (
        oxidative_stress_mapping["target_term"]["label"]
        == "regulation of cellular response to oxidative stress"
    )
    sumo_e2_mapping = next(
        mapping
        for mapping in mapping_sets["ubiquitin_proteasome_system.yaml"]["mappings"]
        if mapping["subject_code"] == "Ubiquitin Proteasome System|E2 conjugating enzymes|SUMOylation"
    )
    assert sumo_e2_mapping["target_term"]["id"] == "GO:0019789"
    assert sumo_e2_mapping["target_term"]["label"] == "SUMO transferase activity"
    jdomain_mapping = next(
        mapping
        for mapping in mapping_sets["chaperone_systems.yaml"]["mappings"]
        if mapping["subject_code"] == "J-domain containing HSP70 cochaperone"
    )
    assert jdomain_mapping["target_term"]["id"] == "GO:0030544"
    assert jdomain_mapping["target_term"]["label"] == "Hsp70 protein binding"
    mitochondrial_unmapped = next(
        unmapped
        for unmapped in mapping_sets["mitochondrial_proteostasis.yaml"]["unmapped_subjects"]
        if unmapped["subject_code"] == "Mitochondrial proteostasis|Chaperone"
    )
    assert mitochondrial_unmapped["subject_level"] == "class"
    assert mitochondrial_unmapped["unmapped_status"] == "no_mapping_appropriate"
