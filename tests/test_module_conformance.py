"""Tests for bundle-scoped conformance checking in module_qc.

A node may declare `conforms_to: [{template: <module>[#node], status: ...}]`.
The checker resolves the template motif and verifies the conforming bundle
contains the template's ordered tiers (by molecular-function term) and the same
activating connection topology, honoring the declared `status`.
"""

from pathlib import Path

import yaml

from ai_gene_review.module_qc import (
    conformance_violations,
    node_tier_terms,
    resolve_template_node,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULES_DIR = PROJECT_ROOT / "modules"


def load_module(name: str) -> dict:
    return yaml.safe_load((MODULES_DIR / name).read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- #
# template resolution + tier extraction
# --------------------------------------------------------------------------- #


def test_resolve_template_root_node():
    node = resolve_template_node("mapk_relay", MODULES_DIR)
    assert node is not None
    assert node["id"] == "mapk_relay"


def test_resolve_template_named_node():
    node = resolve_template_node("mapk_relay#map2k", MODULES_DIR)
    assert node is not None
    assert node["id"] == "map2k"


def test_resolve_template_missing_returns_none():
    assert resolve_template_node("does_not_exist", MODULES_DIR) is None
    assert resolve_template_node("mapk_relay#nope", MODULES_DIR) is None


def test_node_tier_terms_reads_relay_motif():
    relay = resolve_template_node("mapk_relay", MODULES_DIR)
    tiers = node_tier_terms(relay)
    assert [t["function_id"] for t in tiers] == [
        "GO:0004709",
        "GO:0004708",
        "GO:0004707",
    ]


# --------------------------------------------------------------------------- #
# real module: erk_cascade conforms EXACTly
# --------------------------------------------------------------------------- #


def test_erk_cascade_conforms_without_violations():
    data = load_module("erk_cascade.yaml")
    violations = conformance_violations(data, modules_dir=MODULES_DIR)
    assert violations == [], violations


# --------------------------------------------------------------------------- #
# synthetic positive/negative cases
# --------------------------------------------------------------------------- #


def _relay_bundle(tier_terms, status="EXACT", deviations=None, edges=("01", "12")):
    """Build a minimal conforming bundle node with the given tier function ids."""
    ids = ["t0", "t1", "t2"][: len(tier_terms)]
    parts = [
        {
            "order": i + 1,
            "node": {
                "id": ids[i],
                "label": ids[i],
                "annotons": [{"function": {"term": {"id": term, "label": term}}}],
            },
        }
        for i, term in enumerate(tier_terms)
    ]
    connections = [
        {
            "source": ids[int(e[0])],
            "target": ids[int(e[1])],
            "connection_type": "CAUSES",
        }
        for e in edges
        if int(e[0]) < len(ids) and int(e[1]) < len(ids)
    ]
    conf = {"template": "mapk_relay", "status": status}
    if deviations is not None:
        conf["deviations"] = deviations
    bundle = {
        "id": "bundle",
        "label": "bundle",
        "conforms_to": [conf],
        "parts": parts,
        "connections": connections,
    }
    return {"module": {"id": "m", "label": "m", "parts": [{"node": bundle}]}}


def test_exact_match_passes():
    data = _relay_bundle(["GO:0004709", "GO:0004708", "GO:0004707"])
    assert conformance_violations(data, modules_dir=MODULES_DIR) == []


def test_wrong_tier_term_is_error():
    data = _relay_bundle(["GO:0004709", "GO:0004708", "GO:9999999"])
    violations = conformance_violations(data, modules_dir=MODULES_DIR)
    assert any(v["severity"] == "error" for v in violations)
    assert any("tier" in v["message"].lower() for v in violations)


def test_missing_tier_count_is_error():
    data = _relay_bundle(["GO:0004709", "GO:0004708"])
    violations = conformance_violations(data, modules_dir=MODULES_DIR)
    assert any(v["severity"] == "error" for v in violations)
    assert any("tier count" in v["message"].lower() for v in violations)


def test_wrong_topology_is_error():
    # Connect t0->t2 and t1->t2 instead of the relay chain t0->t1->t2.
    data = _relay_bundle(["GO:0004709", "GO:0004708", "GO:0004707"], edges=("02", "12"))
    violations = conformance_violations(data, modules_dir=MODULES_DIR)
    assert any("topology" in v["message"].lower() for v in violations)


def test_with_deviations_downgrades_to_info():
    data = _relay_bundle(
        ["GO:0004709", "GO:0004708", "GO:9999999"],
        status="WITH_DEVIATIONS",
        deviations=["terminal tier substituted for a non-canonical kinase"],
    )
    violations = conformance_violations(data, modules_dir=MODULES_DIR)
    # The tier mismatch is recorded but downgraded to info, not error.
    assert violations
    assert all(v["severity"] != "error" for v in violations)
    assert any(v["severity"] == "info" for v in violations)


def test_with_deviations_but_none_listed_warns():
    data = _relay_bundle(
        ["GO:0004709", "GO:0004708", "GO:0004707"],
        status="WITH_DEVIATIONS",
        deviations=[],
    )
    violations = conformance_violations(data, modules_dir=MODULES_DIR)
    assert any(
        v["severity"] == "warning" and "deviation" in v["message"].lower()
        for v in violations
    )


def test_missing_template_is_error():
    data = _relay_bundle(["GO:0004709", "GO:0004708", "GO:0004707"])
    data["module"]["parts"][0]["node"]["conforms_to"][0]["template"] = "no_such_motif"
    violations = conformance_violations(data, modules_dir=MODULES_DIR)
    assert any(
        v["severity"] == "error" and "template" in v["message"].lower()
        for v in violations
    )


def test_subclass_predicate_allows_descendant_term():
    # A child term that is a subclass of the template tier term should pass when
    # an ontology subclass predicate is supplied.
    data = _relay_bundle(["GO:0004709", "GO:0004708", "GO:0102456"])

    def subclass_of(child, parent):
        return (child, parent) == ("GO:0102456", "GO:0004707")

    violations = conformance_violations(
        data, modules_dir=MODULES_DIR, subclass_of=subclass_of
    )
    assert violations == []
