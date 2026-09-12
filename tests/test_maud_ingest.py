"""Tests for Maud TOML ingest and regulation diffing.

The methionine_cycle module was transcribed from the Maud source, so a correct
ingest + diff must report FULL AGREEMENT — and must detect a deliberately
perturbed edge. The source is treated as evidence (mediated by a reviewed mapping),
never silently merged.
"""

from __future__ import annotations

from pathlib import Path

import yaml
import pytest

from ai_gene_review.maud_ingest import (
    candidate_connections,
    load_mapping,
    maud_edges_from_files,
    maud_regulatory_edges,
    parse_maud_toml,
)
from ai_gene_review.regulation_compare import (
    RegEdge,
    diff_edges,
    module_regulatory_edges,
)


TOML = Path("models/methionine/methionine_cycle.regulation.toml")
MAPPING = Path("models/methionine/maud_methionine_mapping.yaml")
MODULE = Path("modules/methionine_cycle.yaml")

pytestmark = pytest.mark.skipif(
    not (TOML.exists() and MAPPING.exists() and MODULE.exists()),
    reason="methionine source/module fixtures not present",
)


def test_parse_counts_all_regulatory_entries():
    model = parse_maud_toml(TOML)
    assert len(model["allostery"]) == 7
    assert len(model["competitive_inhibition"]) == 3


def test_edges_use_mapped_symbols_and_mechanisms():
    edges = maud_edges_from_files(TOML, MAPPING)
    assert len(edges) == 10
    # MAT-I competitively inhibited by SAM; MAT-III allosterically activated by SAM.
    assert RegEdge("amet", "mat1", "-", "competitive") in edges
    assert RegEdge("amet", "mat3", "+", "allosteric") in edges
    # methionine activates MAT-III (met-L -> met via the mapping)
    assert RegEdge("met", "mat3", "+", "allosteric") in edges


def test_unmapped_ids_fall_back_to_lowercase():
    model = parse_maud_toml(TOML)
    edges = maud_regulatory_edges(model)  # no mapping
    # GNMT1 stays 'gnmt1' without a mapping, surfacing the misalignment rather than guessing.
    assert any(e.enzyme == "gnmt1" for e in edges)


def test_curated_module_fully_agrees_with_source():
    curated = module_regulatory_edges(yaml.safe_load(MODULE.read_text()))
    source = maud_edges_from_files(TOML, MAPPING)
    diff = diff_edges(curated, source)
    assert diff.is_clean, (
        f"unexpected differences: only_left={diff.only_in_left} "
        f"only_right={diff.only_in_right} sign={diff.sign_conflicts} mech={diff.mechanism_conflicts}"
    )
    assert len(diff.agreements) == 10


def test_diff_detects_sign_flip():
    curated = module_regulatory_edges(yaml.safe_load(MODULE.read_text()))
    source = maud_edges_from_files(TOML, MAPPING)
    # Flip MAT-I inhibition to activation in the source.
    perturbed = {
        RegEdge("amet", "mat1", "+", "competitive")
        if e == RegEdge("amet", "mat1", "-", "competitive")
        else e
        for e in source
    }
    diff = diff_edges(curated, perturbed)
    assert not diff.is_clean
    assert len(diff.sign_conflicts) == 1
    left, right = diff.sign_conflicts[0]
    assert left.key == ("amet", "mat1") and left.sign == "-" and right.sign == "+"


def test_diff_detects_missing_and_extra():
    curated = module_regulatory_edges(yaml.safe_load(MODULE.read_text()))
    source = maud_edges_from_files(TOML, MAPPING)
    dropped = {e for e in source if e != RegEdge("amet", "cbs", "+", "allosteric")}
    extra = dropped | {RegEdge("sah", "fake", "-", "competitive")}
    diff = diff_edges(curated, extra)
    assert any(e.key == ("amet", "cbs") for e in diff.only_in_left)
    assert any(e.key == ("sah", "fake") for e in diff.only_in_right)


def test_candidate_connections_ground_to_sbo_with_evidence():
    edges = {RegEdge("amet", "mat1", "-", "competitive")}
    conns = candidate_connections(edges, source_id="GitHub:biosustain/Methionine_model")
    assert len(conns) == 1
    conn = conns[0]
    assert conn["connection_type"] == "NEGATIVELY_REGULATES"
    assert conn["predicate"]["term"]["id"] == "SBO:0000206"
    assert conn["source"] == "amet_pool" and conn["target"] == "mat1_activity"
    assert conn["evidence"][0]["source_id"] == "GitHub:biosustain/Methionine_model"


def test_mapping_loads_enzyme_and_metabolite_tables():
    mapping = load_mapping(MAPPING)
    assert mapping["enzymes"]["MAT3"] == "mat3"
    assert mapping["metabolites"]["met-L"] == "met"
