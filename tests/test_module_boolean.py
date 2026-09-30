"""Tests for the module -> Boolean network translator (ai_gene_review.module_boolean).

The translator flattens a module's hierarchical ``connections`` graph into a
Boolean network (every endpoint a variable; CaSQ-style default rules), parses
external ``.bnet`` models with sign inference, ingests SIGNOR pathway exports,
and diffs signed wiring through a reviewed id-mapping.

These tests exercise a hand-built toy module (with a nested container whose
entry/exit tiers must be resolved, and a pure-inhibitor tier that must become an
input), the real ERK cascade module, the cached BBM-070 MAPK model, and the
SIGNOR EGFR snapshot.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from ai_gene_review.module_boolean import (
    SignedEdge,
    diff_signed_edges,
    find_paths,
    format_signed_diff,
    iter_mapping_pairs,
    load_mapping,
    module_file_to_boolean,
    module_to_boolean,
    parse_bnet,
    parse_bnet_file,
    path_sign,
    project_edges,
    signor_signed_edges,
)

ROOT = Path(__file__).resolve().parents[1]
ERK = ROOT / "modules/erk_cascade.yaml"
JAK_STAT = ROOT / "modules/jak_stat_signaling.yaml"
BBM070 = ROOT / "models/boolean/bbm-070-mapk-cancer-cell-fate/model.bnet"
BBM070_MAPPING = (
    ROOT / "models/boolean/bbm-070-mapk-cancer-cell-fate/mapping_to_modules.yaml"
)
SIGNOR_EGF = ROOT / "models/boolean/signor/SIGNOR-EGF.tsv"
SIGNOR_MAPPING = ROOT / "models/boolean/signor/SIGNOR-EGF.mapping_to_modules.yaml"


def _toy_module() -> dict:
    """An entry step, a nested switch (GEF -> GTPase -| GAP), a relay, an inhibitor."""
    return {
        "id": "MODULE:toy",
        "module": {
            "id": "toy",
            "parts": [
                {"order": 1, "node": {"id": "receptor"}},
                {
                    "order": 2,
                    "node": {
                        "id": "switch",
                        "parts": [
                            {"node": {"id": "gef"}},
                            {"node": {"id": "gtpase"}},
                            {"node": {"id": "gap"}},
                        ],
                        "connections": [
                            {
                                "source": "gef",
                                "target": "gtpase",
                                "connection_type": "CAUSES",
                            },
                            {
                                "source": "gap",
                                "target": "gtpase",
                                "connection_type": "NEGATIVELY_REGULATES",
                            },
                        ],
                    },
                },
                {
                    "order": 3,
                    "node": {
                        "id": "relay",
                        "parts": [{"node": {"id": "k1"}}, {"node": {"id": "k2"}}],
                        "connections": [
                            {
                                "source": "k1",
                                "target": "k2",
                                "connection_type": "CAUSES",
                            }
                        ],
                    },
                },
                {"order": 4, "node": {"id": "phosphatase"}},
            ],
            "connections": [
                {
                    "source": "receptor",
                    "target": "switch",
                    "connection_type": "PROVIDES_INPUT_FOR",
                },
                {"source": "switch", "target": "relay", "connection_type": "CAUSES"},
                {
                    "source": "phosphatase",
                    "target": "k2",
                    "connection_type": "NEGATIVELY_REGULATES",
                },
                {"source": "relay", "target": "toy", "connection_type": "PART_OF"},
            ],
        },
    }


def test_toy_flattening_resolves_entries_and_exits():
    bn = module_to_boolean(_toy_module())
    # receptor -> switch lands on the GEF (entry), not the GAP (pure inhibitor)
    assert SignedEdge("receptor", "gef", "+") in bn.edges
    assert SignedEdge("receptor", "gap", "+") not in bn.edges
    # switch -> relay originates from the GTPase (exit) and lands on k1 (entry)
    assert SignedEdge("gtpase", "k1", "+") in bn.edges
    # PART_OF is structural and ignored
    assert not any(e.target == "toy" for e in bn.edges)
    assert bn.inputs == ["receptor", "gap", "phosphatase"]
    assert bn.rules["gtpase"] == "gef & !gap"
    assert bn.rules["k2"] == "k1 & !phosphatase"


def test_toy_bnet_round_trip_preserves_edges():
    bn = module_to_boolean(_toy_module())
    parsed = parse_bnet(bn.to_bnet())
    assert parsed.edges == bn.edges
    assert parsed.inputs == bn.inputs


@pytest.mark.parametrize(
    "input_mode,expect_input_line", [("identity", True), ("free", False)]
)
def test_bnet_input_modes(input_mode, expect_input_line):
    text = module_to_boolean(_toy_module()).to_bnet(input_mode=input_mode)
    assert ("receptor, receptor" in text) is expect_input_line


def test_logic_override_and_scenario():
    bn = module_to_boolean(_toy_module())
    overridden = bn.with_logic({"k2": "k1 & gtpase & !phosphatase"})
    assert SignedEdge("gtpase", "k2", "+") in overridden.edges
    assert SignedEdge("k1", "k2", "+") in overridden.edges
    fixed = overridden.with_inputs({"receptor": True, "gap": False})
    assert fixed.rules["receptor"] == "1"
    assert fixed.rules["gap"] == "0"
    with pytest.raises(KeyError):
        bn.with_inputs({"nope": True})


def test_erk_cascade_translation():
    bn = module_file_to_boolean(ERK)
    # the GAP tier is the only regulator left as a free input besides the stimulus:
    # the DUSP step is now induced by ERK output (feedback loop closed)
    assert bn.inputs == ["adaptor_recruitment", "rasgap_step"]
    assert bn.rules["ras_active"] == "ras_gef_step & !rasgap_step"
    assert bn.rules["erk_mapk"] == "mek_map2k & !mapk_negative_regulation"
    assert bn.rules["mapk_negative_regulation"] == "erk_output"
    # the relay is a linear chain RAF -> MEK -> ERK, and ERK still exits the relay
    # bundle onto the output step although it feeds back onto RAF
    assert SignedEdge("raf_map3k", "mek_map2k", "+") in bn.edges
    assert SignedEdge("mek_map2k", "erk_mapk", "+") in bn.edges
    assert SignedEdge("erk_mapk", "erk_output", "+") in bn.edges
    assert "erk_relay" not in bn.variables
    # the two calibration feedbacks
    assert SignedEdge("erk_mapk", "raf_map3k", "-") in bn.edges
    assert SignedEdge("erk_output", "ras_gef_step", "-") in bn.edges
    assert bn.rules["raf_map3k"] == "ras_active & !erk_mapk"


def test_feedback_edge_does_not_hide_relay_exit():
    """A last-tier -| first-tier feedback inside a bundle must not turn the bundle itself into a variable."""
    doc = _toy_module()
    doc["module"]["connections"].append(
        {"source": "k2", "target": "k1", "connection_type": "NEGATIVELY_REGULATES"}
    )
    bn = module_to_boolean(doc)
    assert "relay" not in bn.variables
    assert bn.rules["k1"] == "gtpase & !k2"


def test_parse_bbm070_signs():
    bn = parse_bnet_file(BBM070)
    assert len(bn.variables) == 53
    assert set(bn.inputs) == {
        "v_DNA_damage",
        "v_EGFR_stimulus",
        "v_FGFR3_stimulus",
        "v_TGFBR_stimulus",
    }
    assert SignedEdge("v_MEK1_2", "v_ERK", "+") in bn.edges
    assert SignedEdge("v_ERK", "v_RAF", "-") in bn.edges  # ERK -| RAF negative feedback
    assert SignedEdge("v_RSK", "v_SOS", "-") in bn.edges
    assert SignedEdge("v_PPP2CA", "v_MEK1_2", "-") in bn.edges
    # the published model has 104 regulations
    assert len(bn.edges) == 104


def test_bbm070_calibration_of_erk_cascade():
    mapping = load_mapping(BBM070_MAPPING)
    module_map = dict(iter_mapping_pairs(mapping["modules"]["erk_cascade"]))
    external_map = dict(iter_mapping_pairs(mapping["external"]))
    curated = project_edges(module_file_to_boolean(ERK).edges, module_map)
    external = project_edges(parse_bnet_file(BBM070).edges, external_map)
    erk_symbols = set(module_map.values())
    ext_edges = {
        e for e in external.edges if e.source in erk_symbols and e.target in erk_symbols
    }
    diff = diff_signed_edges(curated.edges, ext_edges)
    # the kinase relay and Ras switch agree edge-for-edge
    for edge in ["GRB2 -> SOS", "SOS -> RAS", "RAS -> RAF", "RAF -> MEK", "MEK -> ERK"]:
        assert edge in {str(e) for e in diff.agree}
    assert not diff.sign_conflict
    # the two feedbacks the calibration surfaced are now in the curated module
    agree = {str(e) for e in diff.agree}
    assert "ERK -| RAF" in agree
    assert "ERK_OUTPUT -| SOS" in agree
    assert not diff.right_only
    # the ERK-induced DUSP loop is module-only (BBM-070 routes DUSP1 via CREB)
    assert "ERK_OUTPUT -> DUSP" in {str(e) for e in diff.left_only}
    # the module's DUSP -| ERK edge has no counterpart (BBM DUSP1 targets p38/JNK)
    assert "DUSP -| ERK" in {str(e) for e in diff.left_only}
    report = format_signed_diff(diff, "erk_cascade", "BBM-070")
    assert "agree=" in report


def test_signor_egf_ingest_and_projection():
    edges = signor_signed_edges(SIGNOR_EGF)
    assert SignedEdge("SOS1", "HRAS", "+") in edges
    assert SignedEdge("ERK1/2", "SOS1", "-") in edges
    mapping = load_mapping(SIGNOR_MAPPING)
    external_map = dict(iter_mapping_pairs(mapping["external"]))
    proj = project_edges(edges, external_map)
    assert SignedEdge("SOS", "RAS", "+") in proj.edges
    assert SignedEdge("ERK", "SOS", "-") in proj.edges
    # a partially mapped edge names an external regulator of a mapped element
    assert any(e.target == "RAS" and e.source == "SRC" for e in proj.partial)


def test_path_sign_recognises_tier_compression():
    bn = module_file_to_boolean(ERK)
    # BBM has RAS -> MEK? no; but MAP3K1_3 -> MEK exists. The relay is a path in the module:
    assert (
        path_sign(bn.edges, "ras_active", "erk_mapk", {"raf_map3k", "mek_map2k"}) == "+"
    )
    assert path_sign(bn.edges, "ras_active", "erk_mapk", {"raf_map3k"}) is None
    assert (
        path_sign(
            bn.edges,
            "rasgap_step",
            "erk_mapk",
            {"ras_active", "raf_map3k", "mek_map2k"},
        )
        == "-"
    )


def test_as_inputs_drops_rule_and_incoming_edges():
    bn = module_file_to_boolean(ERK)
    assert "mapk_negative_regulation" in bn.rules
    free = bn.as_inputs("mapk_negative_regulation")
    assert "mapk_negative_regulation" in free.inputs
    assert not any(e.target == "mapk_negative_regulation" for e in free.edges)
    # the counterfactual file written by the demo must be readable back with DUSP as an input
    assert "mapk_negative_regulation, mapk_negative_regulation" in free.to_bnet()


def test_container_with_referenced_child_expands_to_children():
    """jak_stat: the negative-regulation bundle has no internal edges but its SOCS child is
    an endpoint, so the bundle must resolve to its children rather than become a second
    variable alongside socs_feedback."""
    bn = module_file_to_boolean(JAK_STAT)
    assert "jak_stat_negative_regulation" not in bn.variables
    assert bn.rules["socs_feedback"] == "stat_transcription"
    assert SignedEdge("socs_feedback", "jak_activation", "-") in bn.edges
    assert bn.rules["jak_activation"].count("socs_feedback") == 1
    # the phosphatase and PIAS children are external inputs
    assert {"ptp_dephosphorylation", "pias_restraint"} <= set(bn.inputs)


@pytest.mark.parametrize(
    "text,rule,inputs",
    [
        ("targets, factors\nx, 1\ny, x & !z\nz, z", "1", ["z"]),
        ("targets, factors\nx, 0\ny, x | z", "0", ["z"]),
        ("targets, factors\nx, true\ny, x", "true", []),
    ],
)
def test_parse_bnet_constant_rules(text, rule, inputs):
    bn = parse_bnet(text)
    assert bn.rules["x"] == rule
    assert bn.inputs == inputs
    assert not any(e.target == "x" for e in bn.edges)


def test_parse_bnet_rejects_c_style_operators():
    with pytest.raises(ValueError, match="not bnet syntax"):
        parse_bnet("targets, factors\nx, a && b")


def test_signor_filters_and_skipping():
    pooled = signor_signed_edges(SIGNOR_EGF)
    human_direct = signor_signed_edges(SIGNOR_EGF, direct_only=True, taxa={"9606"})
    assert human_direct < pooled
    # the SOS1 phosphosite rows are macaque (tax 9534): dropped by a human-only filter
    assert SignedEdge("ERK1/2", "SOS1", "-") in pooled
    assert SignedEdge("ERK1/2", "SOS1", "-") not in human_direct
    # 'unknown' effects are skipped: the EGFR -> GRB2 'unknown' row must not add a '?' edge
    assert not any(e.sign not in {"+", "-"} for e in pooled)


def test_find_paths_is_exhaustive_and_deterministic():
    es = {
        SignedEdge("a", "b", "+"),
        SignedEdge("b", "d", "+"),
        SignedEdge("a", "c", "-"),
        SignedEdge("c", "d", "+"),
    }
    assert find_paths(es, "a", "d", {"b", "c"}) == [("+", ["b"]), ("-", ["c"])]
    assert path_sign(es, "a", "d", {"b", "c"}) == "?"
    assert path_sign(es, "a", "d", {"b"}) == "+"


def test_module_to_bnet_cli(tmp_path):
    from typer.testing import CliRunner

    from ai_gene_review.cli import app

    runner = CliRunner()
    result = runner.invoke(app, ["module-to-bnet", str(ERK), "-o", str(tmp_path)])
    assert result.exit_code == 0, result.output
    written = (tmp_path / "erk_cascade.bnet").read_text()
    assert written.startswith("targets, factors")
    assert parse_bnet(written).edges == module_file_to_boolean(ERK).edges
    stdout = runner.invoke(app, ["module-to-bnet", str(ERK)])
    assert (
        stdout.exit_code == 0
        and "inputs: adaptor_recruitment, rasgap_step" in stdout.output
    )


def test_with_logic_declares_non_essential_regulators():
    """A regulator that cancels out still has to be declared, or to_bnet references an unknown symbol."""
    bn = parse_bnet("targets, factors\na, a\nx, a")
    over = bn.with_logic({"x": "a | (b & !b)"})
    assert "b" in over.variables
    assert not any(e.source == "b" for e in over.edges)
    text = over.to_bnet()
    assert "b, b" in text
    assert parse_bnet(text).variables == over.variables


def test_descendants_rejects_cyclic_tree():
    """A cycle introduced into the parts tree raises instead of recursing forever."""
    from ai_gene_review.module_boolean import _Flattener

    doc = {"id": "a", "parts": [{"node": {"id": "b", "parts": []}}]}
    flat = _Flattener(doc)
    flat.index["b"]["parts"].append({"node": flat.index["a"]})  # a -> b -> a
    with pytest.raises(ValueError, match="cyclic"):
        flat._descendants("a")
