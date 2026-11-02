"""Tests for the GO-CAM structural linter (ai_gene_review.gocam_lint).

Graph-rule tests run on real cached models under gocams/. Ontology tests need
the oaklib GO SQLite build and are marked integration.
"""

from pathlib import Path

import pytest

from ai_gene_review.gocam_lint import (
    COMPARTMENT_ANCHORS,
    _ANCHOR_PARENTS,
    OakOracle,
    ModelView,
    classify_crossing,
    faces_from_ancestors,
    lint_model,
    load_model,
    near_duplicate_models,
)

GOCAMS = Path(__file__).resolve().parents[1] / "gocams"


def _model(model_id: str):
    return load_model(GOCAMS / model_id / f"{model_id}-src.yaml")


def _rules(findings, rule_id):
    return [f for f in findings if f.rule == rule_id]


@pytest.mark.parametrize(
    "up,down,expected",
    [
        ({"C"}, {"E"}, "ERROR"),  # cytosol -> extracellular in one step
        ({"E"}, {"C"}, "ERROR"),
        ({"M"}, {"E"}, "ERROR"),
        ({"C"}, {"P"}, "ERROR"),  # bacterial cytoplasm -> periplasm
        ({"C"}, {"M"}, "WARNING"),  # import into the matrix omitted
        ({"C"}, {"L"}, "WARNING"),  # translocation into the ER omitted
        ({"L"}, {"E"}, "INFO"),  # topologically continuous
        ({"C"}, {"C", "E", "P"}, None),  # plasma membrane bridges
        ({"E"}, {"C", "E", "P"}, None),
        ({"C"}, {"C"}, None),
    ],
)
def test_classify_crossing(up, down, expected):
    assert classify_crossing(frozenset(up), frozenset(down)) == expected


@pytest.mark.parametrize(
    "term,ancestors,expected",
    [
        # most specific anchor wins over its organelle and cytoplasm
        ("GO:0005759", ["GO:0005739", "GO:0005737", "GO:0005622"], {"M"}),
        # leaflet: intersection of cytoplasmic side and ER membrane
        ("GO:0098554", ["GO:0098562", "GO:0005789", "GO:0005783", "GO:0005737"], {"C"}),
        # extrinsic to cytoplasmic side of the plasma membrane
        ("GO:0031234", ["GO:0098562", "GO:0005886"], {"C"}),
        # extrinsic component of plasma membrane, side unspecified
        ("GO:0019897", ["GO:0005886"], {"C", "E", "P"}),
        ("GO:0005576", [], {"E"}),
        # host-cell terms are skipped
        ("GO:0030430", ["GO:0033643", "GO:0018995", "GO:0005737"], None),
        # no anchor: generic membrane
        ("GO:0016020", [], None),
    ],
)
def test_faces_from_ancestors(term, ancestors, expected):
    faces = faces_from_ancestors(term, ancestors)
    assert (faces if faces is None else set(faces)) == expected


def test_same_gene_chain_nlrp3():
    """The NLRP3 inflammasome model chains five NLRP3 activities."""
    findings = _rules(lint_model(_model("635b1e3e00001811")), "same_gene_chain")
    sizes = sorted(len(f.activity_ids) for f in findings if "NLRP3" in f.message)
    assert sizes == [5]


def test_opposite_sign_fanout_isr():
    """EIF2AK3 activates one EIF2S1 node and inhibits another."""
    findings = _rules(lint_model(_model("66b5638000001589")), "opposite_sign_fanout")
    assert len(findings) == 1
    assert "EIF2AK3" in findings[0].message and "EIF2S1" in findings[0].message


def test_parallel_components_nbn():
    """The NBN repair-choice model is two parallel chains with a duplicated TERF2."""
    findings = lint_model(_model("65a1f4f800002884"))
    comps = _rules(findings, "disconnected_components")
    assert [f.severity for f in comps] == ["WARNING"]
    dups = _rules(findings, "duplicate_activity")
    assert any(f.severity == "WARNING" and "TERF2" in f.message for f in dups)


def test_clean_rules_on_il1_model():
    """The IL-1 model has no structural graph anomalies of these kinds."""
    findings = lint_model(_model("59cc772c00000000"))
    for rid in ("same_gene_chain", "duplicate_activity", "orphan_activity",
                "disconnected_components", "contradictory_edges", "self_loop"):
        assert _rules(findings, rid) == [], rid
    # the IRAK1 -> TAK1 edge has no evidence
    assert len(_rules(findings, "missing_evidence")) == 1


def test_near_duplicate_models_ospc():
    """The IFN-beta and IFN-gamma calmodulin models are near-clones."""
    views = [ModelView.from_model(_model(m)) for m in
             ("62b4ffe300004525", "62b4ffe300004489", "59cc772c00000000")]
    pairs = {(f.model_id, f.message.split()[-3]) for f in near_duplicate_models(views)}
    assert ("62b4ffe300004489", "62b4ffe300004525") in pairs
    assert not any("59cc772c00000000" in p for pair in pairs for p in pair)


@pytest.fixture(scope="module")
def go_oracle():
    return OakOracle()


@pytest.mark.integration
def test_compartment_crossing_casp1(go_oracle):
    """CASP1 (cytosol) directly activating IL1B (extracellular) is impossible."""
    findings = _rules(lint_model(_model("59cc772c00000000"), go_oracle), "compartment_crossing")
    assert [f.severity for f in findings] == ["ERROR"]
    assert "CASP1" in findings[0].message and "IL1B" in findings[0].message


@pytest.mark.integration
def test_generic_kinase_il1(go_oracle):
    findings = _rules(lint_model(_model("59cc772c00000000"), go_oracle), "generic_mf")
    assert len(findings) == 3


@pytest.mark.integration
@pytest.mark.parametrize("anchor", sorted(COMPARTMENT_ANCHORS))
def test_anchor_labels_match_go(go_oracle, anchor):
    assert go_oracle.label(anchor) == COMPARTMENT_ANCHORS[anchor][0]


@pytest.mark.integration
@pytest.mark.parametrize("anchor", sorted(COMPARTMENT_ANCHORS))
def test_anchor_parents_match_go(go_oracle, anchor):
    """The static anchor order equals the anchors GO places above each anchor."""
    above = (go_oracle.ancestors(anchor) - {anchor}) & set(COMPARTMENT_ANCHORS)
    assert above == set(_ANCHOR_PARENTS.get(anchor, frozenset()))


@pytest.mark.parametrize(
    "term,ancestors,expected",
    [
        # plasma membrane region under an intracellular cytoskeletal part
        ("GO:0031528", ["GO:0005886", "GO:0005622"], {"C", "E", "P"}),
        # specific granule: vesicle, not generic cytoplasm
        ("GO:0042581", ["GO:0031410", "GO:0005737", "GO:0005622"], {"C", "L"}),
    ],
)
def test_weak_anchors_yield(term, ancestors, expected):
    assert set(faces_from_ancestors(term, ancestors)) == expected


def test_lumen_to_extracellular_is_info():
    """Golgi processing followed by secretion is topologically continuous."""
    assert classify_crossing(frozenset({"C", "L"}), frozenset({"E"})) == "INFO"
