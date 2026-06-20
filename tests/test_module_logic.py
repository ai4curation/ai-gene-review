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


def test_atom_is_hashable():
    # frozen dataclass -> usable in sets (a regression we want to keep)
    atoms = set(iter_atoms(compile_module(_toy_module())))
    assert len(atoms) == 5
    assert all(isinstance(a, Atom) for a in atoms)
