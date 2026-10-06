#!/usr/bin/env python
"""Render the executable models that modules declare under ``executable_models``.

Every module-derived Boolean model gets an interactive page
(``pages/models/<model id>.html``) that runs the network in the browser: pick a
curated scenario, lock any step on or off, and watch the cascade update and
settle (or not). Every model of any type (Boolean, kinetic, constraint-based,
agent-based; derived or external) is listed on ``pages/models/index.html``.

The pages are rendered alongside the module pages by
:func:`ai_gene_review.render_modules.render_all_modules`, so they are rebuilt
with the site and never edited by hand.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from ai_gene_review.module_boolean import module_to_boolean
from ai_gene_review.module_dynamics import (
    MAX_EXHAUSTIVE_VARIABLES,
    boolean_model_payload,
    run_scenario,
)
from ai_gene_review.render_modules import (
    _environment,
    as_list,
    clean_rendered_html,
    evidence_url,
    relative_href,
    slugify,
)

REPO_BLOB = "https://github.com/ai4curation/ai-gene-review/blob/main/"

MODEL_TYPE_LABELS = {
    "BOOLEAN": "Boolean",
    "KINETIC": "Kinetic",
    "CONSTRAINT_BASED": "Constraint-based",
    "AGENT_BASED": "Agent-based",
    "OTHER": "Other",
}


def models_dir_for(module_output_dir: Path) -> Path:
    """Model pages live in a ``models`` directory beside the module pages.

    >>> models_dir_for(Path("pages/modules")).as_posix()
    'pages/models'
    """
    return module_output_dir.parent / "models"


def model_page_path(models_dir: Path, model_id: str) -> Path:
    """Output path of a model's interactive page.

    >>> model_page_path(Path("pages/models"), "erk_cascade_boolean").as_posix()
    'pages/models/erk_cascade_boolean.html'
    """
    return models_dir / f"{slugify(model_id)}.html"


def is_interactive(model: dict[str, Any], doc: dict[str, Any]) -> bool:
    """Whether a model gets an in-browser page: derived, Boolean, small enough."""
    if (
        model.get("model_type") != "BOOLEAN"
        or model.get("derivation") != "DERIVED_FROM_MODULE"
    ):
        return False
    return len(module_to_boolean(doc).variables) <= MAX_EXHAUSTIVE_VARIABLES


def model_summaries(
    doc: dict[str, Any],
    yaml_path: Path,
    module_page: Path,
    models_dir: Path,
    from_file: Path,
) -> list[dict[str, Any]]:
    """Compact descriptions of a module's executable models.

    Links are made relative to ``from_file`` (the page that shows them). For an
    interactive model, every scenario is run so the summary carries its verdict.
    """
    out: list[dict[str, Any]] = []
    for model in as_list(doc.get("executable_models")):
        if not isinstance(model, dict) or not model.get("id"):
            continue
        interactive = is_interactive(model, doc)
        scenarios = []
        for scenario in as_list(model.get("scenarios")):
            if not isinstance(scenario, dict):
                continue
            entry = {
                "id": scenario.get("id"),
                "label": scenario.get("label") or scenario.get("id"),
            }
            if interactive:
                result = run_scenario(doc, str(model["id"]), scenario)
                entry["passed"] = result.passed
                entry["kinds"] = [a.kind for a in result.attractors]
            scenarios.append(entry)
        out.append(
            {
                "id": model["id"],
                "title": model.get("title") or model["id"],
                "model_type": model.get("model_type"),
                "type_label": MODEL_TYPE_LABELS.get(
                    str(model.get("model_type")), model.get("model_type")
                ),
                "derivation": model.get("derivation"),
                "description": model.get("description"),
                "files": [
                    {"path": f, "url": REPO_BLOB + str(f)}
                    for f in as_list(model.get("files"))
                ],
                "evidence": [
                    {"source_id": e.get("source_id"), "url": evidence_url(e)}
                    for e in as_list(model.get("evidence"))
                    if isinstance(e, dict)
                ],
                "scenarios": scenarios,
                "scenarios_passed": sum(1 for s in scenarios if s.get("passed")),
                "interactive": interactive,
                "page_href": (
                    relative_href(
                        from_file, model_page_path(models_dir, str(model["id"]))
                    )
                    if interactive
                    else None
                ),
                "module_id": doc.get("id"),
                "module_title": doc.get("title") or yaml_path.stem,
                "module_href": relative_href(from_file, module_page),
                "source_path": yaml_path.as_posix(),
            }
        )
    return out


def _template(name: str) -> Any:
    path = Path(__file__).parent / "templates" / name
    return _environment(path).get_template(path.name)


def render_model_pages(
    doc: dict[str, Any],
    yaml_path: Path,
    module_page: Path,
    models_dir: Path,
) -> list[Path]:
    """Write the interactive page of every derived Boolean model of one module."""
    written: list[Path] = []
    for model in as_list(doc.get("executable_models")):
        if not isinstance(model, dict) or not is_interactive(model, doc):
            continue
        page = model_page_path(models_dir, str(model["id"]))
        payload = boolean_model_payload(doc, model)
        html = _template("executable_model.html.j2").render(
            payload=payload,
            payload_json=json.dumps(payload, sort_keys=True).replace("</", "<\\/"),
            model=model,
            module_title=doc.get("title") or yaml_path.stem,
            module_href=relative_href(page, module_page),
            index_href=relative_href(page, models_dir / "index.html"),
            modules_index_href=relative_href(page, module_page.parent / "index.html"),
            source_path=yaml_path.as_posix(),
            source_url=REPO_BLOB + yaml_path.as_posix(),
        )
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(clean_rendered_html(html), encoding="utf-8")
        written.append(page)
    return written


def render_models_index(
    summaries: list[dict[str, Any]],
    models_dir: Path,
    modules_index: Optional[Path] = None,
) -> Path:
    """Write the cross-module index of executable models."""
    index = models_dir / "index.html"
    html = _template("executable_model_index.html.j2").render(
        models=summaries,
        type_counts={
            label: sum(1 for m in summaries if m["type_label"] == label)
            for label in sorted({m["type_label"] for m in summaries})
        },
        modules_index_href=(
            relative_href(index, modules_index) if modules_index is not None else None
        ),
    )
    models_dir.mkdir(parents=True, exist_ok=True)
    index.write_text(clean_rendered_html(html), encoding="utf-8")
    return index


def clean_model_html(models_dir: Path) -> None:
    """Remove previously generated model pages."""
    if models_dir.exists():
        for page in models_dir.glob("*.html"):
            page.unlink()
