"""Tests for the compact human-readable module notation projection.

The notation is a *read-only* projection of a module YAML document: a legend
block mapping short symbols to grounded entities, a reactions block, and a
regulation block. It is generated from the canonical YAML (no parse-back).
"""

from __future__ import annotations

from pathlib import Path

import yaml
import pytest

from ai_gene_review.module_notation import render_module_notation


MET_CYCLE = Path("modules/methionine_cycle.yaml")


def _small_module() -> dict:
    """A minimal module exercising legend, a reaction, and both regulation types."""
    return {
        "id": "MODULE:toy",
        "title": "Toy",
        "module": {
            "id": "toy",
            "label": "Toy",
            "module_type": "METABOLIC_PATHWAY",
            "concepts": [
                {
                    "preferred_term": "toy pathway",
                    "term": {"id": "GO:0000001", "label": "toy"},
                }
            ],
            "parts": [
                {
                    "order": 1,
                    "node": {
                        "id": "rxn_step",
                        "label": "step",
                        "module_type": "REACTION",
                        "annotons": [
                            {
                                "id": "enz_activity",
                                "function": {
                                    "preferred_term": "widgetase activity",
                                    "term": {
                                        "id": "GO:0004478",
                                        "label": "widgetase activity",
                                    },
                                    "substrates": [
                                        {"preferred_term": "A"},
                                        {"preferred_term": "ATP"},
                                    ],
                                    "products": [{"preferred_term": "B"}],
                                },
                            }
                        ],
                    },
                },
                {
                    "order": 2,
                    "node": {
                        "id": "effectors",
                        "label": "effectors",
                        "module_type": "MODULE",
                        "parts": [
                            {
                                "node": {
                                    "id": "x_pool",
                                    "label": "X pool",
                                    "concepts": [
                                        {
                                            "preferred_term": "X",
                                            "term": {
                                                "id": "CHEBI:15414",
                                                "label": "X-mol",
                                            },
                                        }
                                    ],
                                }
                            }
                        ],
                    },
                },
            ],
            "connections": [
                {
                    "source": "x_pool",
                    "target": "enz_activity",
                    "connection_type": "NEGATIVELY_REGULATES",
                    "predicate": {
                        "preferred_term": "competitive inhibition",
                        "term": {"id": "SBO:0000206", "label": "competitive inhibitor"},
                    },
                },
                {
                    "source": "x_pool",
                    "target": "enz_activity",
                    "connection_type": "POSITIVELY_REGULATES",
                    "predicate": {
                        "preferred_term": "allosteric activation",
                        "term": {"id": "SBO:0000636", "label": "allosteric activator"},
                    },
                },
            ],
        },
    }


def test_legend_lists_enzyme_with_go():
    out = render_module_notation(_small_module())
    assert "enz" in out
    assert "GO:0004478" in out


def test_legend_lists_metabolite_with_chebi():
    out = render_module_notation(_small_module())
    # the _pool suffix is stripped to a short symbol
    assert "x " in out or "x\t" in out or "x:=" in out.replace(" ", "")
    assert "CHEBI:15414" in out


def test_reaction_line_uses_arrow_and_symbols():
    out = render_module_notation(_small_module())
    # enzyme symbol from the annoton id (suffix stripped), reaction arrow, substrates/products
    assert "enz:" in out
    assert "->" in out
    assert "ATP" in out


def test_regulation_competitive_uses_inhibition_arrow_and_mechanism():
    out = render_module_notation(_small_module())
    assert "x -| enz" in out
    assert "[competitive]" in out
    assert "SBO:0000206" in out


def test_regulation_allosteric_uses_activation_arrow():
    out = render_module_notation(_small_module())
    assert "x -o enz" in out
    assert "[allosteric]" in out


def test_no_yaml_braces_leak_into_output():
    out = render_module_notation(_small_module())
    # The projection should be plain notation, not echoed python/yaml structures.
    assert "{'" not in out
    assert "preferred_term:" not in out


@pytest.mark.skipif(
    not MET_CYCLE.exists(), reason="methionine_cycle module not present"
)
def test_methionine_isozyme_opposite_regulation_is_visible():
    """The showcase: MAT-I competitively inhibited vs MAT-III allosterically activated by SAM."""
    data = yaml.safe_load(MET_CYCLE.read_text())
    out = render_module_notation(data)
    assert "amet -| mat1   [competitive]" in out.replace("  ", " ").replace(
        "  ", " "
    ) or ("amet -| mat1" in out and "[competitive]" in out)
    assert "amet -o mat3" in out and "[allosteric]" in out
    # grounding present
    assert "GO:0004478" in out
    assert "CHEBI:15414" in out
    assert "SBO:0000206" in out


@pytest.mark.skipif(
    not MET_CYCLE.exists(), reason="methionine_cycle module not present"
)
def test_methionine_all_ten_regulatory_edges_rendered():
    data = yaml.safe_load(MET_CYCLE.read_text())
    out = render_module_notation(data)
    reg_lines = [
        ln for ln in out.splitlines() if (" -| " in ln or " -o " in ln) and "[" in ln
    ]
    assert len(reg_lines) == 10
