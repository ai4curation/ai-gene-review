#!/usr/bin/env python
"""Build or check the Boolean-model conformance fixtures in models/boolean/conformance/.

Each case is a directory holding a module document (``module.yaml``) and the
behaviour every implementation of the translator and engine must reproduce
(``expected.json``): variable order, update rules, signed edges, omitted
regulators, the rules under each scenario's removed connections, and the
asynchronous attractors with all inputs free and under each scenario.

Cases are of two kinds:

* ``synthetic``: small hand-written modules, one per translation rule or dynamic
  behaviour (flattening, GAP tiers, declared logic, oscillation, bistability).
* ``frozen``: slimmed snapshots of real modules with curated scenarios or
  declared logic. ``--refresh-inputs`` re-copies them from ``modules/``; until
  then, curation edits to the live module do not change the fixture.

Usage::

    uv run python scripts/build_boolean_conformance.py            # rewrite expected.json
    uv run python scripts/build_boolean_conformance.py --check    # fail on any difference
    uv run python scripts/build_boolean_conformance.py --refresh-inputs
"""

from __future__ import annotations

import argparse
import json
import sys
import warnings
from pathlib import Path
from typing import Any

import yaml

from ai_gene_review.module_boolean import module_to_boolean, omitted_regulators
from ai_gene_review.module_dynamics import attractors, boolean_models, run_scenario

ROOT = Path(__file__).resolve().parents[1]
CONFORMANCE = ROOT / "models" / "boolean" / "conformance"
FORMAT_VERSION = 1

# Real modules frozen as fixtures: every module with curated Boolean scenarios, plus
# declared-logic modules that exercise omitted_regulators.
FROZEN = [
    "erk_cascade",
    "jak_stat_signaling",
    "p38_cascade",
    "c_elegans_dbl1_body_size_signaling",
    "bacterial_type_iv_secretion_apparatus",
]

# Keys translation reads; everything else (evidence, descriptions, grounding) is
# dropped from frozen copies.
NODE_KEYS = (
    "id",
    "label",
    "module_type",
    "parts",
    "variant_sets",
    "annotons",
    "connections",
    "activation_logic",
    "omitted_regulators",
)


def slim(value: Any, key: str = "") -> Any:
    """Keep only what translation and scenarios read."""
    if isinstance(value, list):
        return [slim(v, key) for v in value]
    if not isinstance(value, dict):
        return value
    if key == "connections":
        return {
            k: value[k] for k in ("source", "target", "connection_type") if k in value
        }
    if key in ("activation_logic", "all_of", "any_of", "none_of"):
        return value
    if key == "parts":
        out = {k: v for k, v in value.items() if k in ("node", "optional")}
        return {k: slim(v, k) for k, v in out.items()}
    if key == "variant_sets":
        return {
            "id": value.get("id"),
            "variants": slim(value.get("variants") or [], "variants"),
        }
    if key == "annotons":
        # Translation only asks whether an element is an annoton (has a participant).
        return {"id": value.get("id"), "label": value.get("label"), "participant": {}}
    return {k: slim(v, k) for k, v in value.items() if k in NODE_KEYS}


def freeze(name: str) -> dict:
    doc = yaml.safe_load((ROOT / "modules" / f"{name}.yaml").read_text())
    out = {
        "id": doc["id"],
        "title": doc.get("title"),
        "module": slim(doc["module"], "node"),
    }
    models = [
        {k: m[k] for k in ("id", "model_type", "derivation", "scenarios") if k in m}
        for m in boolean_models(doc)
    ]
    if models:
        out["executable_models"] = models
    return out


def summarise(found) -> list[dict]:
    return [
        {
            "size": len(a.states),
            "always_on": a.always_on,
            "always_off": a.always_off,
            "oscillating": a.oscillating,
        }
        for a in found
    ]


def expected(doc: dict, source: str) -> dict:
    model = module_to_boolean(doc)
    omitted = omitted_regulators(doc)
    edges = sorted(
        [e.source, e.target, e.sign, e.source in omitted.get(e.target, [])]
        for e in model.edges
    )
    scenarios = []
    for entry in boolean_models(doc):
        for scenario in entry.get("scenarios") or []:
            removed = {
                (str(r["source"]), str(r["target"]))
                for r in scenario.get("removed_connections") or []
            }
            variant = (
                module_to_boolean(doc, removed_connections=removed)
                if removed
                else model
            )
            settings = {
                str(s["element"]): bool(s["active"])
                for s in scenario.get("settings") or []
            }
            result = run_scenario(doc, str(entry.get("id")), scenario)
            scenarios.append(
                {
                    "id": scenario["id"],
                    "settings": settings,
                    "removed_connections": sorted([s, t] for s, t in removed),
                    "rules": {v: variant.rules.get(v) for v in model.variables},
                    "attractors": summarise(attractors(variant, settings)),
                    "expectations_hold": result.passed,
                }
            )
    return {
        "format_version": FORMAT_VERSION,
        "source": source,
        "variables": list(model.variables),
        "inputs": model.inputs,
        "rules": {v: model.rules.get(v) for v in model.variables},
        "edges": edges,
        "free_attractors": summarise(attractors(model)),
        "scenarios": scenarios,
    }


def dump(data: Any) -> str:
    return json.dumps(data, indent=1, sort_keys=False) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check", action="store_true", help="fail if any expected.json would change"
    )
    parser.add_argument(
        "--refresh-inputs", action="store_true", help="re-copy frozen module snapshots"
    )
    args = parser.parse_args(argv)
    warnings.simplefilter("ignore", UserWarning)
    cases = CONFORMANCE / "cases"
    if args.refresh_inputs:
        for name in FROZEN:
            path = cases / name / "module.yaml"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                f"# Frozen from modules/{name}.yaml by scripts/build_boolean_conformance.py;\n"
                "# translation-relevant keys only. Refresh with --refresh-inputs.\n"
                + yaml.safe_dump(freeze(name), sort_keys=False, allow_unicode=True)
            )
    stale = []
    for case in sorted(p for p in cases.iterdir() if (p / "module.yaml").exists()):
        doc = yaml.safe_load((case / "module.yaml").read_text())
        source = "frozen" if case.name in FROZEN else "synthetic"
        text = dump(expected(doc, source))
        target = case / "expected.json"
        if args.check:
            if not target.exists() or target.read_text() != text:
                stale.append(case.name)
        else:
            target.write_text(text)
    if stale:
        print(
            "Stale conformance fixtures (rebuild and review the diff):",
            ", ".join(stale),
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
