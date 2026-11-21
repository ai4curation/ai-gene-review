"""Subset projection must retain multiple paths without counting a row twice."""

from pathlib import Path
import json

import pytest

from ai_gene_review.tools.build_browser_hierarchies import (
    build_go_hierarchy,
    build_taxonomy_hierarchy,
    append_hierarchies,
    fetch_taxonomy,
    read_go_obo,
)


@pytest.fixture
def ontology(tmp_path: Path):
    """A small synthetic graph using familiar IDs, including unsafe relations."""
    path = tmp_path / "go.obo"
    path.write_text("""format-version: 1.2
data-version: test-release

[Term]
id: GO:0008150
name: biological_process

[Term]
id: GO:0009987
name: cellular process
subset: goslim_generic
is_a: GO:0008150

[Term]
id: GO:0008152
name: metabolic process
subset: goslim_generic
is_a: GO:0008150

[Term]
id: GO:0044237
name: cellular metabolic process
subset: goslim_generic
is_a: GO:0009987
is_a: GO:0008152

[Term]
id: GO:0006629
name: lipid metabolic process
alt_id: GO:TEST_ALT
relationship: part_of GO:0044237

[Term]
id: GO:0019222
name: regulation of metabolic process
is_a: GO:0008150
relationship: regulates GO:0008152
relationship: has_part GO:0006629

[Term]
id: GO:TEST_OBSOLETE
name: obsolete example
is_obsolete: true
is_a: GO:0008152
""")
    return read_go_obo(path)


def test_slim_projection_preserves_diamond_and_deduplicates(ontology):
    terms, version = ontology
    facet = build_go_hierarchy(terms, {"GO:0006629", "GO:TEST_ALT"})
    assert version == "test-release"
    assert set(facet["nodes"]["GO:0044237"]["parents"]) == {"GO:0009987", "GO:0008152"}
    assert facet["memberships"]["GO:0006629"] == facet["memberships"]["GO:TEST_ALT"]
    assert len(facet["memberships"]["GO:0006629"]) == 4
    assert "GO:0006629" not in facet["nodes"]  # hidden detail still matches


def test_unsafe_edges_and_unresolved_ids(ontology):
    terms, _ = ontology
    facet = build_go_hierarchy(terms, {"GO:0019222", "GO:TEST_OBSOLETE", "GO:UNKNOWN"})
    assert facet["memberships"]["GO:0019222"] == ["GO:0008150"]
    assert facet["memberships"]["GO:UNKNOWN"] == ["unmapped"]
    assert facet["memberships"]["GO:TEST_OBSOLETE"] == ["unmapped"]


def test_taxonomy_uses_lineage_and_retains_species_leaves():
    records = [
        {
            "taxonId": 9606,
            "scientificName": "Homo sapiens",
            "lineage": [
                {"taxonId": 2759, "scientificName": "Eukaryota"},
                {"taxonId": 33154, "scientificName": "Opisthokonta"},
                {"taxonId": 33208, "scientificName": "Metazoa"},
                {"taxonId": 9605, "scientificName": "Homo"},
            ],
        }
    ]
    facet = build_taxonomy_hierarchy(records)
    assert facet["nodes"]["NCBITaxon:9606"]["parents"] == ["NCBITaxon:33208"]
    assert facet["nodes"]["NCBITaxon:33208"]["parents"] == ["NCBITaxon:33154"]
    assert len(facet["memberships"]["NCBITaxon:9606"]) == 4


def test_cycle_fails_instead_of_emitting_partial_mapping(ontology):
    terms, _ = ontology
    terms["GO:0008150"]["parents"] = ["GO:0044237"]
    with pytest.raises(ValueError, match="Cycle"):
        build_go_hierarchy(terms, {"GO:0006629"})


@pytest.mark.parametrize("bad_id", ["NCBITaxon:DESVH", "9606", "taxon:9606"])
def test_cached_taxonomy_and_unmapped_data_remain_browsable(tmp_path, bad_id):
    """Malformed existing IDs do not acquire invented biological ancestry."""
    (tmp_path / "9606.json").write_text(
        json.dumps(
            {
                "taxonId": 9606,
                "scientificName": "Homo sapiens",
                "lineage": [{"taxonId": 33208, "scientificName": "Metazoa"}],
            }
        )
    )
    with pytest.warns(UserWarning, match="Unmapped taxonomy"):
        records = fetch_taxonomy(
            {"NCBITaxon:9606": "human", bad_id: "Unresolved organism"},
            tmp_path,
        )
    facet = build_taxonomy_hierarchy(records)
    assert facet["memberships"][bad_id] == [
        "unmapped-taxonomy",
        bad_id,
    ]
    assert facet["nodes"][bad_id]["label"] == "Unresolved organism"
    assert facet["nodes"]["NCBITaxon:9606"]["parents"] == ["NCBITaxon:33208"]
    assert facet["nodes"]["NCBITaxon:9606"]["label"] == "Homo sapiens"
    assert facet["memberships"]["NCBITaxon:9606"] == [
        "NCBITaxon:33208",
        "NCBITaxon:9606",
    ]


def test_schema_metadata_is_idempotent_and_does_not_rewrite_base(tmp_path):
    path = tmp_path / "schema.js"
    original = 'window.searchSchema = {"facets": []};\n'
    path.write_text(original)
    append_hierarchies(path, [], {"version": "old"})
    append_hierarchies(path, [], {"version": "new"})
    assert path.read_text().startswith(original)
    assert path.read_text().count("window.searchSchema.hierarchies") == 1
    assert '"old"' not in path.read_text()
