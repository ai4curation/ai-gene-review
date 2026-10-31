"""Tests for the two-layer gap model in ``module_logic``.

A process step requires a molecular function; that function is carried out by
one of several families, domains or complexes. These tests cover how the engine
keeps the two apart:

* ``variant_kind`` on a variant set (declared, or inferred as REALIZER when every
  variant carries the same single function);
* ``gap_report``, which locates each gap at its innermost failing element,
  including inside referenced modules, and labels it by layer;
* ``abduce``, whose gap candidates list only absent atoms and whose hypotheses
  follow the layers of the gaps;
* family and domain selectors carried on compiled atoms.

See projects/ORGANELLE_LIFECYCLES/two-layer-model.md.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from ai_gene_review.module_logic import (
    GENERAL_HYPOTHESES,
    REALIZER_HYPOTHESES,
    ROUTE_HYPOTHESES,
    Or,
    abduce,
    compile_module,
    compile_module_file,
    gap_report,
    iter_atoms,
)


def _annoton(aid: str, symbol: str, mf: str | None = None) -> dict:
    annoton: dict = {"id": aid, "participant": {"gene": {"preferred_term": symbol}}}
    if mf:
        annoton["function"] = {"term": {"id": mf}}
    return annoton


def _choice(kind: str | None, *variants: tuple[str, str, str]) -> dict:
    """A one-step module whose step is a variant set over (id, symbol, MF) variants."""
    vs: dict = {"id": "choice", "variants": [
        {"id": vid, "annotons": [_annoton(vid, symbol, mf)]} for vid, symbol, mf in variants
    ]}
    if kind:
        vs["variant_kind"] = kind
    return {"module": {"id": "m", "parts": [{"node": {"id": "step", "variant_sets": [vs]}}]}}


def _only_or(circuit) -> Or:
    step, = circuit.children
    choice, = step.children
    assert isinstance(choice, Or)
    return choice


@pytest.mark.parametrize(
    ("kind", "mfs", "expected", "inferred"),
    [
        (None, ("GO:1", "GO:1"), "REALIZER", True),     # same activity, two carriers
        (None, ("GO:1", "GO:2"), None, False),          # different activities: not inferable
        ("ROUTE", ("GO:1", "GO:1"), "ROUTE", False),    # a declaration wins
        ("REALIZER", ("GO:1", "GO:2"), "REALIZER", False),
    ],
)
def test_variant_kind_is_declared_or_inferred(kind, mfs, expected, inferred):
    doc = _choice(kind, ("x", "X", mfs[0]), ("y", "Y", mfs[1]))
    choice = _only_or(compile_module(doc))
    assert (choice.kind, choice.kind_inferred) == (expected, inferred)


@pytest.mark.parametrize(
    ("kind", "mfs", "layer"),
    [
        (None, ("GO:1", "GO:1"), "REALIZER"),
        (None, ("GO:1", "GO:2"), "UNCLASSIFIED"),
        ("ROUTE", ("GO:1", "GO:2"), "ROUTE"),
    ],
)
def test_failed_choice_is_labelled_by_layer(kind, mfs, layer):
    doc = _choice(kind, ("x", "X", mfs[0]), ("y", "Y", mfs[1]))
    gap, = gap_report(compile_module(doc), lambda atom: False)
    assert gap.path == ("step", "choice")
    assert gap.layer == layer
    assert gap.candidates == ["X", "Y"]


def test_single_carrier_step_is_a_realizer_gap():
    doc = {"module": {"id": "m", "parts": [
        {"node": {"id": "s", "annotons": [_annoton("a", "A", "GO:1")]}}]}}
    gap, = gap_report(compile_module(doc), lambda atom: False)
    assert (gap.path, gap.layer, gap.step) == (("s", "a"), "REALIZER", "a")


def test_gap_candidates_list_only_absent_atoms():
    doc = {"module": {"id": "m", "parts": [
        {"node": {"id": "s", "annotons": [_annoton("a", "A"), _annoton("b", "B")]}}]}}
    result = abduce(compile_module(doc), lambda atom: atom.gene_symbol == "A", asserted_active=True)
    assert result.gap_steps == ["s"]
    assert result.gap_candidates == {"s": ["B"]}
    assert [g.path for g in result.gaps] == [("s", "b")]


@pytest.mark.parametrize(
    ("kind", "mfs", "excluded"),
    [
        ("ROUTE", ("GO:1", "GO:2"), REALIZER_HYPOTHESES),
        (None, ("GO:1", "GO:1"), ROUTE_HYPOTHESES),
    ],
)
def test_hypotheses_follow_the_gap_layer(kind, mfs, excluded):
    doc = _choice(kind, ("x", "X", mfs[0]), ("y", "Y", mfs[1]))
    result = abduce(compile_module(doc), lambda atom: False, asserted_active=True)
    assert result.classification == "ABDUCTION_TARGET"
    assert not set(excluded) & set(result.hypotheses)
    assert set(GENERAL_HYPOTHESES) <= set(result.hypotheses)


def test_unclassified_gap_keeps_both_layer_hypotheses():
    doc = _choice(None, ("x", "X", "GO:1"), ("y", "Y", "GO:2"))
    result = abduce(compile_module(doc), lambda atom: False, asserted_active=True)
    assert set(REALIZER_HYPOTHESES + ROUTE_HYPOTHESES) <= set(result.hypotheses)


def test_gap_report_descends_into_referenced_modules(tmp_path: Path):
    (tmp_path / "imp.yaml").write_text(yaml.safe_dump({"id": "MODULE:imp", "module": {
        "id": "imp", "parts": [
            {"node": {"id": "pore", "annotons": [_annoton("tom", "TOM40")]}},
            {"node": {"id": "channel", "annotons": [_annoton("tim", "TIM23")]}},
        ]}}))
    umbrella = {"module": {"id": "life", "parts": [
        {"node": {"id": "protein_import", "module_ref": "imp"}}]}}
    circuit = compile_module(umbrella, modules_dir=tmp_path)
    gap, = gap_report(circuit, lambda atom: atom.gene_symbol == "TOM40")
    assert gap.path == ("protein_import", "imp", "channel", "imp#tim")
    assert gap.candidates == ["TIM23"]


def test_atom_carries_family_and_domain_selectors():
    doc = {"module": {"id": "m", "annotons": [{"id": "a", "participant": {
        "family": {"term": {"id": "PANTHER:PTHR1"},
                   "family_terms": [{"id": "PANTHER:PTHR2"}, {"id": "PANTHER:PTHR1"}]},
        "domain": {"term": {"id": "InterPro:IPR1"}},
        "required_domain": {"term": {"id": "Pfam:PF1"}},
    }}]}}
    atom, = iter_atoms(compile_module(doc))
    assert atom.family_ids == ("PANTHER:PTHR1", "PANTHER:PTHR2")
    assert atom.domain_ids == ("InterPro:IPR1", "Pfam:PF1")


UMBRELLA = Path("modules/mitochondrion_lifecycle.yaml")
KETOLYSIS = Path("modules/ketone_body_oxidation.yaml")


@pytest.mark.skipif(not UMBRELLA.exists(), reason="module file absent")
def test_mitochondrion_import_gap_is_located_inside_the_import_module():
    """With TIM23 and TIM22 absent, the gaps name those two steps, not the whole stage."""
    missing = {"mitochondrial_protein_import#tim23_channel",
               "mitochondrial_protein_import#tim22_insertase"}
    result = abduce(compile_module_file(UMBRELLA), lambda atom: atom.node_id not in missing,
                    asserted_active=True)
    assert result.gap_steps == ["protein_import"]
    assert result.gap_candidates == {"protein_import": ["TIMM22", "TIMM23"]}
    assert sorted(g.step for g in result.gaps) == sorted(missing)
    assert all(g.layer == "REALIZER" for g in result.gaps)
    assert all(g.path[:2] == ("protein_import", "mitochondrial_protein_import") for g in result.gaps)


@pytest.mark.skipif(not UMBRELLA.exists(), reason="module file absent")
def test_import_module_atoms_carry_panther_families():
    atoms = {a.node_id: a for a in iter_atoms(compile_module_file(Path("modules/mitochondrial_protein_import.yaml")))}
    assert atoms["tim23_channel"].family_ids == ("PANTHER:PTHR15371",)


@pytest.mark.skipif(not KETOLYSIS.exists(), reason="module file absent")
def test_ketolysis_activation_is_a_route_gap():
    """SCOT and AACS are different activities, so losing both is a route gap."""
    result = abduce(compile_module_file(KETOLYSIS),
                    lambda atom: any(s in {"BDH1", "ACAT1"} for s in atom.gene_symbols),
                    asserted_active=True)
    activation = [g for g in result.gaps if g.path[0] == "acetoacetate_activation"]
    assert [(g.step, g.layer, g.layer_inferred) for g in activation] == [
        ("acetoacetate_activation_route", "ROUTE", False)]
