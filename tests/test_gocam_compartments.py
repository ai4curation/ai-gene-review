"""Tests for GO-CAM compartment QC (ai_gene_review.gocam_compartments).

Ontology lookups use a real slice of go-basic (tests/input/go_cc_mini.obo)
through oaklib's simpleobo adapter. The two model tests run on cached
production GO-CAMs named in projects/GOCAM_COMPARTMENTS.md.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.gocam_compartments import (
    CompartmentModel,
    EdgeStatus,
    ResolutionStatus,
    check_model,
    oak_ancestor_fn,
    summarize,
)

ROOT = Path(__file__).parent.parent
MINI_GO = Path(__file__).parent / "input" / "go_cc_mini.obo"


@pytest.fixture(scope="module")
def cm() -> CompartmentModel:
    return CompartmentModel.load()


@pytest.fixture(scope="module")
def anc():
    return oak_ancestor_fn(f"simpleobo:{MINI_GO}")


@pytest.mark.parametrize(
    "term,status,compartments",
    [
        ("GO:0005829", ResolutionStatus.RESOLVED, ["CYTOSOL"]),
        ("GO:0005886", ResolutionStatus.RESOLVED, ["PLASMA_MEMBRANE"]),
        # extrinsic component of plasma membrane part_of plasma membrane
        ("GO:0019897", ResolutionStatus.RESOLVED, ["PLASMA_MEMBRANE"]),
        ("GO:0005654", ResolutionStatus.RESOLVED, ["NUCLEAR_LUMEN"]),
        ("GO:0000228", ResolutionStatus.RESOLVED, ["NUCLEAR_LUMEN"]),
        ("GO:0005759", ResolutionStatus.RESOLVED, ["MITOCHONDRIAL_MATRIX"]),
        # lysosomal lumen is_a vacuolar lumen: the more specific anchor wins
        ("GO:0043202", ResolutionStatus.RESOLVED, ["LYSOSOME_LUMEN"]),
        ("GO:0005737", ResolutionStatus.COARSE, None),
        ("GO:0005739", ResolutionStatus.COARSE, None),
        ("GO:0009986", ResolutionStatus.COARSE, None),
        # chromatin -> chromosome, which GO does not put in the nucleus
        ("GO:0000785", ResolutionStatus.UNRESOLVED, []),
        (None, ResolutionStatus.MISSING, []),
    ],
)
def test_resolve(cm, anc, term, status, compartments):
    r = cm.resolve(term, anc)
    assert r.status == status
    if compartments is not None:
        assert sorted(r.compartments) == compartments


def test_chromatin_hint(cm, anc):
    r = cm.resolve("GO:0000785", anc)
    assert r.hint is not None
    assert r.hint["usual"] == "NUCLEAR_LUMEN"
    assert r.hint["better_term"]["id"] == "GO:0000228"


def test_cell_type_as_location_gets_hint(cm):
    r = cm.resolve("CL:0000235", lambda t: {t})
    assert r.status == ResolutionStatus.UNRESOLVED
    assert "cell type" in r.hint["note"]


def test_coarse_mitochondrion_members(cm, anc):
    r = cm.resolve("GO:0005739", anc)
    assert "MITOCHONDRIAL_MATRIX" in r.compartments
    assert "CYTOSOL" not in r.compartments


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ({"CYTOSOL"}, {"CYTOSOL"}, (EdgeStatus.SAME, 0)),
        ({"EXTRACELLULAR"}, {"PLASMA_MEMBRANE"}, (EdgeStatus.ADJACENT, 1)),
        ({"CYTOSOL"}, {"EXTRACELLULAR"}, (EdgeStatus.NONADJACENT, 2)),
        ({"PLASMA_MEMBRANE"}, {"NUCLEAR_LUMEN"}, (EdgeStatus.NONADJACENT, 3)),
        ({"CYTOSOL"}, {"MITOCHONDRIAL_MATRIX"}, (EdgeStatus.NONADJACENT, 4)),
        ({"ER_LUMEN"}, {"GOLGI_LUMEN"}, (EdgeStatus.NONADJACENT, 4)),
        # two cytosol-facing membranes: contact site or vesicle docking
        ({"ER_MEMBRANE"}, {"GOLGI_MEMBRANE"}, (EdgeStatus.BRIDGED, 2)),
        ({"MITOCHONDRIAL_OUTER_MEMBRANE"}, {"ER_MEMBRANE"}, (EdgeStatus.BRIDGED, 2)),
        # outer and inner mitochondrial membranes border the IMS
        (
            {"MITOCHONDRIAL_OUTER_MEMBRANE"},
            {"MITOCHONDRIAL_INNER_MEMBRANE"},
            (EdgeStatus.BRIDGED, 2),
        ),
        # a membrane and a space are never bridged
        ({"MITOCHONDRIAL_INNER_MEMBRANE"}, {"CYTOSOL"}, (EdgeStatus.NONADJACENT, 3)),
        ({"GOLGI_MEMBRANE"}, {"EXTRACELLULAR"}, (EdgeStatus.NONADJACENT, 3)),
        # coarse nucleus may be the lumen, so a receptor -> nucleus edge is not bridged
        (
            {"PLASMA_MEMBRANE"},
            {"NUCLEAR_ENVELOPE", "NUCLEAR_LUMEN"},
            (EdgeStatus.NONADJACENT, 2),
        ),
        (set(), {"CYTOSOL"}, (EdgeStatus.INDETERMINATE, None)),
    ],
)
def test_edge_status(cm, a, b, expected):
    from ai_gene_review.gocam_compartments import Resolution

    ra = Resolution("x", ResolutionStatus.RESOLVED, frozenset(a))
    rb = Resolution("y", ResolutionStatus.RESOLVED, frozenset(b))
    assert cm.edge_status(ra, rb) == expected


def test_every_compartment_has_a_kind(cm):
    for key, c in cm.compartments.items():
        assert c.get("kind") in ("membrane", "space"), key


def test_adjacency_is_symmetric_and_connected(cm):
    for a, nbrs in cm.adjacency.items():
        for b in nbrs:
            assert a in cm.adjacency[b]
    for c in cm.compartments:
        assert cm.distance({"CYTOSOL"}, {c}) is not None, c


def _load(model_id: str) -> dict:
    p = ROOT / "gocams" / model_id / f"{model_id}-src.yaml"
    return yaml.safe_load(p.read_text())


def test_il1b_model_casp1_skips_plasma_membrane(cm, anc):
    """CASP1 (cytosol) directly regulates IL1B (extracellular region)."""
    r = check_model(_load("59cc772c00000000"), cm, anc)
    assert not r.unresolved
    bad = [(e.upstream_label, e.downstream_label, e.distance) for e in r.nonadjacent]
    assert bad == [("CASP1 Hsap", "IL1B Hsap", 2)]
    assert r.nonadjacent[0].direct is True


def test_bmp9_model_chromatin_unresolved(cm, anc):
    """SMAD1 occurs in chromatin, which reaches no compartment."""
    r = check_model(_load("600ced8500002343"), cm, anc)
    assert [loc.gene_label for loc in r.unresolved] == ["SMAD1 Hsap"]
    # so the ACVRL1 -> SMAD1 edge cannot be placed
    smad_edges = [e for e in r.edges if e.downstream_label == "SMAD1 Hsap"]
    assert [e.status for e in smad_edges] == [EdgeStatus.INDETERMINATE]
    s = summarize([r])
    assert s["unresolved_terms"][0]["term"] == "GO:0000785"
