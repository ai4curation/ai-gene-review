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

from ai_gene_review.module_boolean import module_to_boolean, omitted_regulators

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


def test_cases_are_exactly_the_declared_set() -> None:
    """Every declared case is present and nothing else is: the set cannot silently shrink."""
    script = build_script()
    assert set(CASE_NAMES) == set(script.SYNTHETIC) | set(script.FROZEN)


def test_biodivine_aeon_is_installed() -> None:
    """The aeon cross-checks below skip without biodivine-aeon; this one does not.

    biodivine-aeon is a declared dev dependency so that the cross-checks run in CI.
    If it ever stops installing, this fails instead of the cross-checks quietly
    turning into skips.
    """
    assert importlib.util.find_spec("biodivine_aeon") is not None


@pytest.mark.parametrize("name", build_script().FROZEN)
def test_frozen_copies_translate_like_the_live_module(name: str) -> None:
    """slim() keeps every key translation reads.

    Both sides re-read the live module, so ordinary curation does not break this;
    it fails when module_boolean starts reading a key that slim() drops.
    """
    live = yaml.safe_load((ROOT / "modules" / f"{name}.yaml").read_text())
    frozen = build_script().freeze(name)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        a, b = module_to_boolean(live), module_to_boolean(frozen)
    assert (a.variables, a.rules, a.edges) == (b.variables, b.rules, b.edges)
    assert omitted_regulators(live) == omitted_regulators(frozen)


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
    for scenario in expected["scenarios"]:
        removed = {(s, t) for s, t in scenario["removed_connections"]}
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            variant = (
                module_to_boolean(doc, removed_connections=removed)
                if removed
                else model
            )
        assert list(variant.variables) == scenario["variables"], scenario["id"]
        assert {v: variant.rules.get(v) for v in variant.variables} == scenario[
            "rules"
        ], scenario["id"]
        assert sorted([e.source, e.target, e.sign] for e in variant.edges) == [
            e[:3] for e in scenario["edges"]
        ], scenario["id"]


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
