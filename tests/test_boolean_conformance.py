"""Boolean-model conformance fixtures: the contract every translator and engine must meet.

The fixtures under ``models/boolean/conformance/`` are shared with other
implementations (the AmiGO 3 Dynamics tab ports the translator and has its own
JavaScript engine). These tests keep them honest on this side: they must match
what ``module_boolean`` and ``module_dynamics`` produce now, every curated
scenario in them must hold, and the attractors must agree with biodivine-aeon's
symbolic algorithm.
"""

from __future__ import annotations

import importlib.util
import json
import warnings
from pathlib import Path

import pytest
import yaml

from ai_gene_review.module_boolean import module_to_boolean

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "models" / "boolean" / "conformance" / "cases"
CASE_NAMES = sorted(p.name for p in CASES.iterdir() if (p / "expected.json").exists())


def load(name: str) -> tuple[dict, dict]:
    doc = yaml.safe_load((CASES / name / "module.yaml").read_text())
    return doc, json.loads((CASES / name / "expected.json").read_text())


def build_script():
    spec = importlib.util.spec_from_file_location(
        "build_boolean_conformance", ROOT / "scripts" / "build_boolean_conformance.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_cases_cover_the_translation_rules_and_dynamics() -> None:
    """Guard against the fixture set silently shrinking."""
    expected = {
        "relay_with_phosphatase",
        "negative_feedback_oscillator",
        "toggle_switch",
        "container_flattening",
        "unwired_container_expansion",
        "declared_logic",
        "erk_cascade",
        "jak_stat_signaling",
        "p38_cascade",
    }
    assert expected <= set(CASE_NAMES)


def test_fixtures_are_current() -> None:
    """expected.json is what this repository's translator and engine produce now.

    A failure means the translation or the dynamics changed. If the change is
    intended, rebuild with ``uv run python scripts/build_boolean_conformance.py``
    and review the diff: every other implementation must then follow.
    """
    assert build_script().main(["--check"]) == 0


@pytest.mark.parametrize("name", CASE_NAMES)
def test_curated_scenarios_hold(name: str) -> None:
    _, expected = load(name)
    failing = [s["id"] for s in expected["scenarios"] if not s["expectations_hold"]]
    assert not failing


@pytest.mark.parametrize("name", CASE_NAMES)
def test_translation_matches(name: str) -> None:
    doc, expected = load(name)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        model = module_to_boolean(doc)
    assert list(model.variables) == expected["variables"]
    assert {v: model.rules.get(v) for v in model.variables} == expected["rules"]
    assert sorted([e.source, e.target, e.sign] for e in model.edges) == [
        e[:3] for e in expected["edges"]
    ]


def aeon_summary(aeon, model, fixed: dict[str, bool]) -> list[dict]:
    bn = aeon.BooleanNetwork.from_bnet(model.with_inputs(fixed).to_bnet())
    graph = aeon.AsynchronousGraph(bn)
    out = []
    for attractor in aeon.Attractors.attractors(graph):
        constant = attractor.vertices().enclosing_named_subspace()
        out.append(
            {
                "size": int(attractor.cardinality()),
                "always_on": sorted(v for v, value in constant.items() if value),
                "always_off": sorted(v for v, value in constant.items() if not value),
                "oscillating": sorted(v for v in model.variables if v not in constant),
            }
        )
    return sorted(out, key=lambda a: (a["size"], a["always_on"], a["always_off"]))


def ours(attractors: list[dict]) -> list[dict]:
    return sorted(
        (
            {k: sorted(a[k]) if isinstance(a[k], list) else a[k] for k in a}
            for a in attractors
        ),
        key=lambda a: (a["size"], a["always_on"], a["always_off"]),
    )


@pytest.mark.parametrize("name", CASE_NAMES)
def test_attractors_agree_with_biodivine_aeon(name: str) -> None:
    """Every fixture attractor, free and per scenario, matches aeon's symbolic search."""
    aeon = pytest.importorskip("biodivine_aeon")
    doc, expected = load(name)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        base = module_to_boolean(doc)
        assert aeon_summary(aeon, base, {}) == ours(expected["free_attractors"])
        for scenario in expected["scenarios"]:
            removed = {tuple(pair) for pair in scenario["removed_connections"]}
            model = (
                module_to_boolean(doc, removed_connections=removed) if removed else base
            )
            assert list(model.variables) == scenario["variables"], scenario["id"]
            assert aeon_summary(aeon, model, scenario["settings"]) == ours(
                scenario["attractors"]
            ), scenario["id"]
