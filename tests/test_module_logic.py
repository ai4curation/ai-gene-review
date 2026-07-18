"""Tests for the module satisfiability engine (ai_gene_review.module_logic).

The engine compiles a module document into a boolean circuit (parts/annotons ->
AND, variant_sets -> OR) and reasons over it: route enumeration, per-context
satisfiability against an externally supplied predicate, and gate identification.

These tests exercise the logic on a hand-built toy module and on the real human
gluconeogenesis module, including an expression-grounded predicate that should
recover the textbook gluconeogenic tissue restriction.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from ai_gene_review.module_logic import (
    Atom,
    compile_module,
    compile_module_file,
    enumerate_routes,
    active_routes,
    is_satisfied,
    core_atoms,
    iter_atoms,
    step_id,
    unsatisfied_steps,
    abduce,
)

GLUCONEO_HUMAN = Path("modules/gluconeogenesis_human.yaml")


def _annoton(aid: str, symbol: str, acc: str) -> dict:
    return {"id": aid, "participant": {"gene": {
        "preferred_term": symbol, "term": {"id": f"UniProtKB:{acc}"}}}}


def _toy_module() -> dict:
    """Entry step (required) -> two-way isozyme choice -> two-component AND step."""
    return {"module": {"id": "toy", "parts": [
        {"order": 1, "node": {"id": "entry", "annotons": [_annoton("a", "A", "P1")]}},
        {"order": 2, "node": {"id": "iso", "variant_sets": [
            {"id": "vs", "selection": "ONE_OR_MORE", "variants": [
                {"id": "b", "annotons": [_annoton("b", "B", "P2")]},
                {"id": "c", "annotons": [_annoton("c", "C", "P3")]},
            ]}]}},
        {"order": 3, "node": {"id": "complex", "annotons": [
            _annoton("d", "D", "P4"), _annoton("e", "E", "P5")]}},
    ]}}


# --------------------------------------------------------------------------- #
# Toy-module structure                                                         #
# --------------------------------------------------------------------------- #


def test_toy_atoms_extracted():
    circuit = compile_module(_toy_module())
    symbols = sorted(a.gene_symbol for a in iter_atoms(circuit))
    assert symbols == ["A", "B", "C", "D", "E"]
    # accessions are parsed off the UniProtKB CURIE
    by_sym = {a.gene_symbol: a.uniprot for a in iter_atoms(circuit)}
    assert by_sym["A"] == "P1" and by_sym["D"] == "P4"


def test_toy_routes_expand_variant_set():
    circuit = compile_module(_toy_module())
    routes = [sorted(a.gene_symbol for a in r) for r in enumerate_routes(circuit)]
    # one OR with two branches -> two routes; AND atoms appear in both
    assert sorted(routes) == [["A", "B", "D", "E"], ["A", "C", "D", "E"]]


def test_toy_core_atoms_are_the_and_backbone():
    circuit = compile_module(_toy_module())
    assert sorted(a.gene_symbol for a in core_atoms(circuit)) == ["A", "D", "E"]


@pytest.mark.parametrize(
    "present,expected",
    [
        ({"A", "B", "D", "E"}, True),       # one isozyme branch is enough
        ({"A", "C", "D", "E"}, True),       # the other branch
        ({"A", "B", "C", "D", "E"}, True),  # both branches present
        ({"B", "C", "D", "E"}, False),      # missing required entry atom A
        ({"A", "D", "E"}, False),           # no isozyme branch satisfied
        ({"A", "B", "C", "D"}, False),      # missing one AND-component of the complex
    ],
)
def test_toy_satisfiability(present, expected):
    circuit = compile_module(_toy_module())
    assert is_satisfied(circuit, lambda atom: atom.gene_symbol in present) is expected


def test_optional_part_never_gates():
    doc = {"module": {"id": "m", "parts": [
        {"order": 1, "node": {"id": "req", "annotons": [_annoton("a", "A", "P1")]}},
        {"order": 2, "optional": True,
         "node": {"id": "opt", "annotons": [_annoton("z", "Z", "P9")]}},
    ]}}
    circuit = compile_module(doc)
    # satisfiable with only the required atom; Z is optional
    assert is_satisfied(circuit, lambda atom: atom.gene_symbol == "A") is True
    assert [a.gene_symbol for a in core_atoms(circuit)] == ["A"]


# --------------------------------------------------------------------------- #
# Real human gluconeogenesis module                                           #
# --------------------------------------------------------------------------- #


@pytest.mark.skipif(not GLUCONEO_HUMAN.exists(), reason="module file absent")
def test_gluconeogenesis_routes_and_gate():
    circuit = compile_module_file(GLUCONEO_HUMAN)
    routes = enumerate_routes(circuit)
    assert len(routes) == 4  # PCK1/PCK2 x FBP1/FBP2
    # every route runs entry -> a PEPCK -> an FBPase -> terminal G6PC1 + SLC37A4
    for r in routes:
        syms = {a.gene_symbol for a in r}
        assert {"PC", "G6PC1", "SLC37A4"} <= syms
        assert syms & {"PCK1", "PCK2"} and syms & {"FBP1", "FBP2"}
    assert sorted(a.gene_symbol for a in core_atoms(circuit)) == ["G6PC1", "PC", "SLC37A4"]


@pytest.mark.skipif(not GLUCONEO_HUMAN.exists(), reason="module file absent")
@pytest.mark.parametrize(
    "expressed,expected_sat,active",
    [
        # liver-like: gluconeogenic catalytic subunit + transporter present
        ({"PC", "PCK1", "PCK2", "FBP1", "G6PC1", "SLC37A4"}, True, 2),
        # muscle-like: G6PC1 absent (only the ubiquitous paralog would be on) -> gated
        ({"PC", "FBP2", "SLC37A4"}, False, 0),
        # terminal catalytic present but transporter missing -> still gated
        ({"PC", "PCK1", "FBP1", "G6PC1"}, False, 0),
    ],
)
def test_gluconeogenesis_expression_grounded(expressed, expected_sat, active):
    circuit = compile_module_file(GLUCONEO_HUMAN)

    def holds(atom):
        return atom.gene_symbol in expressed

    assert is_satisfied(circuit, holds) is expected_sat
    assert len(active_routes(circuit, holds)) == active


GLUCONEO_SUBSTRATES = Path("modules/gluconeogenesis_human_substrates.yaml")


@pytest.mark.skipif(not GLUCONEO_SUBSTRATES.exists(), reason="module file absent")
def test_substrate_module_glycerol_bypasses_carboxylation():
    """Glycerol entry omits PC/PEPCK, so the universal gate is only the terminal step."""
    circuit = compile_module_file(GLUCONEO_SUBSTRATES)
    routes = enumerate_routes(circuit)
    assert len(routes) == 18  # (lactate|alanine x LDH/ALT isozymes) x PEPCK x FBPase + glycerol x FBPase
    # PC is required by every pyruvate-derived route but NOT by glycerol routes,
    # so it must drop out of the AND-core; only the terminal system is universal.
    assert sorted(a.gene_symbol for a in core_atoms(circuit)) == ["G6PC1", "SLC37A4"]
    glycerol_routes = [r for r in routes if "GK" in {a.gene_symbol for a in r}]
    assert glycerol_routes
    for r in glycerol_routes:
        syms = {a.gene_symbol for a in r}
        assert "PC" not in syms and "PCK1" not in syms and "PCK2" not in syms
        assert {"GK", "GPD1", "G6PC1", "SLC37A4"} <= syms


@pytest.mark.skipif(not GLUCONEO_SUBSTRATES.exists(), reason="module file absent")
@pytest.mark.parametrize(
    "expressed,sat",
    [
        ({"GK", "GPD1", "FBP1", "G6PC1", "SLC37A4"}, True),   # glycerol-only, no PC needed
        ({"LDHA", "PC", "PCK1", "FBP1", "G6PC1", "SLC37A4"}, True),  # lactate via pyruvate
        ({"GPT", "FBP1", "G6PC1", "SLC37A4"}, False),         # alanine but missing PC/PEPCK
        ({"GK", "GPD1", "FBP1", "SLC37A4"}, False),           # missing terminal catalytic gate
    ],
)
def test_substrate_module_satisfiability(expressed, sat):
    circuit = compile_module_file(GLUCONEO_SUBSTRATES)

    def holds(atom):
        return atom.gene_symbol in expressed

    assert is_satisfied(circuit, holds) is sat


# --------------------------------------------------------------------------- #
# Microbial GapMind-style genome reconstruction                               #
# --------------------------------------------------------------------------- #

METHIONINE = Path("modules/methionine_biosynthesis.yaml")


@pytest.mark.skipif(not METHIONINE.exists(), reason="module file absent")
def test_methionine_template_structure():
    circuit = compile_module_file(METHIONINE)
    assert [step_id(c) for c in circuit.children] == [
        "acylation", "sulfur_incorporation", "methylation"]
    assert len(enumerate_routes(circuit)) == 12
    # every step is an OR, so no enzyme is universally required
    assert core_atoms(circuit) == []
    assert sorted({a.gene_symbol for a in iter_atoms(circuit)}) == [
        "metA", "metB", "metC", "metE", "metH", "metX", "metY", "metZ"]


@pytest.mark.skipif(not METHIONINE.exists(), reason="module file absent")
@pytest.mark.parametrize(
    "present,found,gaps",
    [
        # E. coli-like: succinyl + trans-sulfuration + both synthases -> found, no gaps
        ({"metA", "metB", "metC", "metE", "metH"}, True, []),
        # H. influenzae-like: acetyl acylation route still completes
        ({"metX", "metB", "metC", "metE"}, True, []),
        # C. glutamicum-like: trans-sulfuration incomplete (no metC) but metY rescues it
        ({"metX", "metB", "metY", "metE", "metH"}, True, []),
        # Buchnera-like reduced genome: only metE -> gap at acylation + sulfur step
        ({"metE"}, False, ["acylation", "sulfur_incorporation"]),
        # missing only the methylation step
        ({"metA", "metB", "metC"}, False, ["methylation"]),
    ],
)
def test_methionine_genome_reconstruction(present, found, gaps):
    """Genome-presence predicate drives route selection and gap detection."""
    circuit = compile_module_file(METHIONINE)

    def holds(atom):
        return atom.gene_symbol in present

    assert is_satisfied(circuit, holds) is found
    assert [step_id(s) for s in unsatisfied_steps(circuit, holds)] == gaps


@pytest.mark.skipif(not METHIONINE.exists(), reason="module file absent")
@pytest.mark.parametrize(
    "present,active,classification,gaps",
    [
        # complete pathway, organism known prototroph -> explained
        ({"metA", "metB", "metC", "metE"}, True, "CONSISTENT_ACTIVE", []),
        # autotroph (makes methionine) but no acylation/sulfur candidates -> abduction lead
        ({"metH"}, True, "ABDUCTION_TARGET", ["acylation", "sulfur_incorporation"]),
        # nothing encoded, known auxotroph -> engine correctly predicts the auxotrophy
        (set(), False, "CONSISTENT_INACTIVE", ["acylation", "sulfur_incorporation", "methylation"]),
        # complete pathway but asserted inactive -> overprediction
        ({"metA", "metB", "metC", "metE"}, False, "OVERPREDICTION", []),
    ],
)
def test_abduction_classification(present, active, classification, gaps):
    circuit = compile_module_file(METHIONINE)

    def holds(atom):
        return atom.gene_symbol in present

    ab = abduce(circuit, holds, asserted_active=active)
    assert ab.classification == classification
    assert ab.gap_steps == gaps
    # only abduction targets carry gap-filling hypotheses
    assert bool(ab.hypotheses) == (classification in {"ABDUCTION_TARGET", "OVERPREDICTION"})
    if classification == "ABDUCTION_TARGET":
        # the candidate canonical enzymes that were all absent are reported per gap
        assert ab.gap_candidates["acylation"] == ["metA", "metX"]
        assert ab.gap_candidates["sulfur_incorporation"] == ["metB", "metC", "metY", "metZ"]


KETOLYSIS = Path("modules/ketone_body_oxidation.yaml")


@pytest.mark.skipif(not KETOLYSIS.exists(), reason="module file absent")
def test_ketolysis_structure():
    circuit = compile_module_file(KETOLYSIS)
    assert [step_id(c) for c in circuit.children] == ["bdh1_step", "oxct1_step", "acat1_step"]
    assert len(enumerate_routes(circuit)) == 1  # linear, all required
    assert sorted(a.gene_symbol for a in core_atoms(circuit)) == ["ACAT1", "BDH1", "OXCT1"]


@pytest.mark.skipif(not KETOLYSIS.exists(), reason="module file absent")
@pytest.mark.parametrize(
    "present,active,classification,gaps",
    [
        # ketolytic tissue (heart/brain/...): all enzymes, asserted active
        ({"BDH1", "OXCT1", "ACAT1"}, True, "CONSISTENT_ACTIVE", []),
        # liver: SCOT/OXCT1 absent, and liver genuinely does not oxidise ketones
        ({"BDH1", "ACAT1"}, False, "CONSISTENT_INACTIVE", ["oxct1_step"]),
        # if a tissue truly oxidised ketones yet lacked OXCT1, that is a lead
        ({"BDH1", "ACAT1"}, True, "ABDUCTION_TARGET", ["oxct1_step"]),
    ],
)
def test_ketolysis_abduction(present, active, classification, gaps):
    circuit = compile_module_file(KETOLYSIS)

    def holds(atom):
        return atom.gene_symbol in present

    ab = abduce(circuit, holds, asserted_active=active)
    assert ab.classification == classification
    assert ab.gap_steps == gaps
    if classification == "CONSISTENT_INACTIVE":
        # the liver gap pinpoints the SCOT step
        assert ab.gap_candidates["oxct1_step"] == ["OXCT1"]


def test_atom_is_hashable():
    # frozen dataclass -> usable in sets (a regression we want to keep)
    atoms = set(iter_atoms(compile_module(_toy_module())))
    assert len(atoms) == 5
    assert all(isinstance(a, Atom) for a in atoms)
