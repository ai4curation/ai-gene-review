#!/usr/bin/env python
"""Audit module steps where two or more activators converge.

The Boolean translation of a module gives every step the default rule "active
when any activator is active and no inhibitor is". Where several activating
connections converge on one step, that OR is sometimes right (alternative
routes) and sometimes wrong (an assembly or transport step that needs every
input). This script lists every such step across ``modules/`` and classifies
it from the module's own structure:

* ``DECLARED`` - the step already carries ``activation_logic``.
* ``ALTERNATIVE_VARIANTS`` - every activator sits in a different variant of a
  shared ``variant_set``, i.e. the module itself declares them alternatives,
  so OR is right by construction.
* ``UNDECIDED`` - structure does not settle it; a curator has to read the
  module and decide.

Usage::

    uv run python projects/EXECUTABLE_MODELS/audit_activator_convergence.py

writes ``projects/EXECUTABLE_MODELS/activator_convergence_audit.yaml`` and
``projects/EXECUTABLE_MODELS/activator_convergence_audit.md``. Nothing is
hand-edited in either file.
"""

from __future__ import annotations

import copy
from collections import Counter
from pathlib import Path
from typing import Any, Optional

import yaml

from ai_gene_review.module_boolean import _descendant_map, module_to_boolean
from ai_gene_review.module_dynamics import _labels
from ai_gene_review.module_notation import iter_connections, iter_nodes
from ai_gene_review.render_modules import as_list, iter_module_files, load_module_yaml

ROOT = Path(__file__).resolve().parents[2]
OUT_YAML = Path(__file__).with_name("activator_convergence_audit.yaml")
OUT_MD = Path(__file__).with_name("activator_convergence_audit.md")


def variant_of(doc: dict[str, Any]) -> dict[str, tuple[str, str]]:
    """Map every element id to the (variant_set id, variant id) it sits under."""
    module = doc["module"]
    parent = _descendant_map(module)
    variant_root: dict[str, tuple[str, str]] = {}
    for node in iter_nodes(module):
        for vs in as_list(node.get("variant_sets")):
            if not isinstance(vs, dict):
                continue
            for variant in as_list(vs.get("variants")):
                if isinstance(variant, dict) and variant.get("id"):
                    variant_root[str(variant["id"])] = (
                        str(vs.get("id")),
                        str(variant["id"]),
                    )

    def lookup(element: str) -> Optional[tuple[str, str]]:
        current: Optional[str] = element
        while current is not None:
            if current in variant_root:
                return variant_root[current]
            current = parent.get(current)
        return None

    return {eid: v for eid in parent for v in [lookup(eid)] if v is not None}


def classify(
    step: str,
    activators: list[str],
    declared: set[str],
    variants: dict[str, tuple[str, str]],
) -> str:
    if step in declared:
        return "DECLARED"
    placed = [variants.get(a) for a in activators]
    if (
        all(placed)
        and len({p[0] for p in placed if p}) == 1
        and len({p[1] for p in placed if p}) == len(activators)
    ):
        return "ALTERNATIVE_VARIANTS"
    return "UNDECIDED"


def connection_notes(doc: dict[str, Any], step: str) -> dict[str, str]:
    """Description of each connection declared into ``step`` (raw, before flattening)."""
    return {
        str(
            c.get("source")
        ): f"{c.get('connection_type')}: {' '.join(str(c.get('description') or '').split())}"
        for c in iter_connections(doc["module"])
        if str(c.get("target")) == step
    }


def without_declared_logic(doc: dict[str, Any]) -> dict[str, Any]:
    """A copy of the module with every ``activation_logic`` removed."""
    stripped = copy.deepcopy(doc)
    for node in iter_nodes(stripped["module"]):
        for element in [
            node,
            *[a for a in as_list(node.get("annotons")) if isinstance(a, dict)],
        ]:
            element.pop("activation_logic", None)
            element.pop("omitted_regulators", None)
    return stripped


def audit() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in iter_module_files(ROOT / "modules"):
        doc = load_module_yaml(path)
        if not isinstance(doc.get("module"), dict):
            continue
        model = module_to_boolean(doc)
        default_model = module_to_boolean(without_declared_logic(doc))
        labels = _labels(doc)
        declared = {
            str(n.get("id"))
            for n in iter_nodes(doc["module"])
            if n.get("activation_logic")
        } | {
            str(a.get("id"))
            for n in iter_nodes(doc["module"])
            for a in as_list(n.get("annotons"))
            if isinstance(a, dict) and a.get("activation_logic")
        }
        variants = variant_of(doc)
        for step in model.variables:
            activators = sorted(
                e.source
                for e in default_model.edges
                if e.target == step and e.sign == "+"
            )
            if len(activators) < 2:
                continue
            notes = connection_notes(doc, step)
            rows.append(
                {
                    "module": path.stem,
                    "step": step,
                    "step_label": labels.get(step, step),
                    "classification": classify(step, activators, declared, variants),
                    "default_rule": default_model.rules[step],
                    "rule": model.rules[step],
                    "activators": [
                        {
                            "id": a,
                            "label": labels.get(a, a),
                            "connection": notes.get(a, "via a container"),
                        }
                        for a in activators
                    ],
                }
            )
    return rows


def main() -> None:
    rows = audit()
    counts = Counter(r["classification"] for r in rows)
    OUT_YAML.write_text(
        "# Generated by audit_activator_convergence.py; do not edit by hand.\n"
        + yaml.safe_dump(
            {"summary": dict(sorted(counts.items())), "steps": rows},
            sort_keys=False,
            width=100,
        )
    )
    lines = [
        "---",
        'title: "Executable models - activator convergence audit"',
        "maturity: IN_PROGRESS",
        "tags: [PIPELINE]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# Activator convergence audit",
        "",
        "Generated by [`audit_activator_convergence.py`](audit_activator_convergence.py); do not edit "
        "by hand. Part of [EXECUTABLE_MODELS](../EXECUTABLE_MODELS.md). Full detail, including each "
        "connection's description, is in [`activator_convergence_audit.yaml`](activator_convergence_audit.yaml).",
        "",
        "Every step with two or more activating regulators, which the Boolean translation would "
        "OR together by default. `ALTERNATIVE_VARIANTS` steps are settled by the module's own "
        "structure (the activators are alternative variants); `DECLARED` steps carry "
        "`activation_logic`; `UNDECIDED` steps need a curator to read the module.",
        "",
        f"{len(rows)} steps in {len({r['module'] for r in rows})} modules: "
        + ", ".join(f"{k} {v}" for k, v in sorted(counts.items()))
        + ".",
        "",
        "| module | step | classification | default rule | declared rule |",
        "|---|---|---|---|---|",
    ]
    for r in sorted(
        rows, key=lambda r: (r["classification"] != "UNDECIDED", r["module"], r["step"])
    ):
        declared = f"`{r['rule']}`" if r["rule"] != r["default_rule"] else ""
        lines.append(
            f"| `{r['module']}` | {r['step_label']} | {r['classification']} "
            f"| `{r['default_rule']}` | {declared} |"
        )
    OUT_MD.write_text("\n".join(lines) + "\n")
    print(
        f"{len(rows)} steps; "
        + ", ".join(f"{k} {v}" for k, v in sorted(counts.items()))
    )


if __name__ == "__main__":
    main()
