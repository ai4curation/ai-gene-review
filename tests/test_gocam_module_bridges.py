"""Tests for explaining GO-CAM edges with module paths (gocam_module_bridges).

The last tests use the curated modules and cached GO-CAM models in the repo:
the receptor/JAK -> nuclear transcription factor edges discussed in
projects/GOCAM_COMPARTMENTS.md.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.gocam_compartments import (
    CompartmentModel,
    EdgeStatus,
    ProteinLocationIndex,
    check_model,
    oak_ancestor_fn,
)
from ai_gene_review.gocam_module_bridges import ModuleBridgeIndex, ModuleGraph

ROOT = Path(__file__).parent.parent
MINI_GO = Path(__file__).parent / "input" / "go_cc_mini.obo"


def _module(connections, transport=("transport",)):
    """A module with nodes a, side, transport, z; activities pinned to a and z."""
    nodes = []
    for nid in ["a", "side", "transport", "z"]:
        node = {"id": nid, "label": nid}
        if nid in transport:
            node["module_type"] = "TRANSPORT_STEP"
        if nid == "a":
            node["gocam_associations"] = [
                {"model": "gomodel:M", "activity": "gomodel:M/up"}
            ]
        if nid == "z":
            node["annotons"] = [
                {
                    "id": "z_tf",
                    "gocam_associations": [
                        {"model": "gomodel:M", "activity": "gomodel:M/down"}
                    ],
                }
            ]
        nodes.append({"order": len(nodes) + 1, "node": node})
    conns = [
        {"source": s, "target": t, "connection_type": ct} for s, t, ct in connections
    ]
    return {"module": {"id": "m", "label": "m", "parts": nodes, "connections": conns}}


def test_side_branch_does_not_hide_the_transport_path():
    """The shortest path a -> side -> z has no transport; a -> transport -> z does."""
    doc = _module(
        [
            ("a", "side", "PRECEDES"),
            ("side", "z", "POSITIVELY_REGULATES"),
            ("a", "transport", "PRECEDES"),
            ("transport", "z", "PROVIDES_INPUT_FOR"),
        ]
    )
    e = ModuleBridgeIndex([ModuleGraph.from_dict("m", doc)]).explain(
        "gomodel:M/up", "gomodel:M/down"
    )
    assert e is not None
    assert e.path == ("a", "transport", "z")
    assert e.downstream_element == "z_tf"


def test_no_transport_step_no_explanation():
    doc = _module([("a", "side", "PRECEDES"), ("side", "z", "CAUSES")], transport=())
    index = ModuleBridgeIndex([ModuleGraph.from_dict("m", doc)])
    assert index.explain("gomodel:M/up", "gomodel:M/down") is None


def test_negative_regulation_does_not_carry_the_signal():
    doc = _module(
        [("a", "transport", "PRECEDES"), ("transport", "z", "NEGATIVELY_REGULATES")]
    )
    index = ModuleBridgeIndex([ModuleGraph.from_dict("m", doc)])
    assert index.explain("gomodel:M/up", "gomodel:M/down") is None


@pytest.fixture(scope="module")
def index() -> ModuleBridgeIndex:
    return ModuleBridgeIndex.from_dir(ROOT / "modules")


@pytest.mark.parametrize(
    "module,up,down",
    [
        # IL-6 trans-signaling: JAK1 (plasma membrane) -> STAT3 (nucleus)
        (
            "jak_stat_signaling",
            "gomodel:5f46c3b700002685/5f46c3b700002801",
            "gomodel:5f46c3b700002685/5f46c3b700002806",
        ),
        # BMP4 signaling: BMPR1A (plasma membrane) -> SMAD1 (nucleus)
        (
            "bmp_signaling",
            "gomodel:66e382fb00001232/66e382fb00001247",
            "gomodel:66e382fb00001232/66e382fb00001262",
        ),
    ],
)
def test_curated_modules_explain_receptor_to_nucleus_edges(index, module, up, down):
    e = index.explain(up, down)
    assert e is not None
    assert e.module == module
    assert "karyopherin_nuclear_protein_import" in e.via_modules


def test_bmp4_model_edges_are_explained(index):
    cm = CompartmentModel.load()
    anc = oak_ancestor_fn(f"simpleobo:{MINI_GO}")
    model = yaml.safe_load(
        (ROOT / "gocams/66e382fb00001232/66e382fb00001232-src.yaml").read_text()
    )
    r = check_model(model, cm, anc, explainer=index.explain)
    receptor_to_smad = [e for e in r.edges if e.upstream_label == "BMPR1A Hsap"]
    assert receptor_to_smad
    assert {e.status for e in receptor_to_smad} == {EdgeStatus.EXPLAINED}


def test_stat3_known_locations_include_cytosol():
    """STAT3's gene folder places it in the cytosol, next to plasma-membrane JAKs."""
    cm = CompartmentModel.load()
    anc = oak_ancestor_fn(f"simpleobo:{MINI_GO}")
    locations = ProteinLocationIndex(ROOT / "genes", cm, anc)
    assert "CYTOSOL" in locations("UniProtKB:P40763")
    assert locations("UniProtKB:NOT_A_PROTEIN") == frozenset()
