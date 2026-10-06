"""Tests for executable-model pages rendered alongside the module pages."""

from __future__ import annotations

import json
import re
from pathlib import Path

from ai_gene_review.render_models import model_summaries, render_models_index
from ai_gene_review.render_modules import render_all_modules, render_module

MODULE_YAML = """id: MODULE:loop
title: Feedback loop
module:
  id: loop
  label: Feedback loop
  parts:
    - node: {id: stimulus, label: Stimulus}
    - node: {id: kinase, label: Kinase}
    - node: {id: phosphatase, label: Phosphatase}
  connections:
    - {source: stimulus, target: kinase, connection_type: CAUSES}
    - {source: kinase, target: phosphatase, connection_type: CAUSES}
    - {source: phosphatase, target: kinase, connection_type: NEGATIVELY_REGULATES}
executable_models:
  - id: loop_boolean
    title: Loop as a Boolean network
    model_type: BOOLEAN
    derivation: DERIVED_FROM_MODULE
    scenarios:
      - id: stimulated
        label: Stimulus on
        settings: [{element: stimulus, active: true}]
        expected_attractor_kind: CYCLIC
      - id: cut
        label: Loop cut
        settings: [{element: stimulus, active: true}, {element: phosphatase, active: false}]
        removed_connections: [{source: kinase, target: phosphatase}]
        expected_attractor_kind: FIXED_POINT
        expected_active: [kinase]
  - id: loop_kinetic
    title: A kinetic model
    model_type: KINETIC
    derivation: EXTERNAL
    files: [models/loop/model.xml]
"""


def _write(tmp_path: Path) -> tuple[Path, Path]:
    modules = tmp_path / "modules"
    modules.mkdir()
    yaml_path = modules / "loop.yaml"
    yaml_path.write_text(MODULE_YAML)
    return modules, tmp_path / "pages" / "modules"


def _payload(html: str) -> dict:
    match = re.search(
        r'<script type="application/json" id="model-data">(.*?)</script>', html, re.S
    )
    assert match
    return json.loads(match.group(1))


def test_render_module_writes_an_interactive_model_page(tmp_path: Path) -> None:
    modules, out = _write(tmp_path)
    page, _ = render_module(modules / "loop.yaml", output_dir=out, modules_dir=modules)
    model_page = tmp_path / "pages" / "models" / "loop_boolean.html"
    assert model_page.exists()
    assert not (tmp_path / "pages" / "models" / "loop_kinetic.html").exists()

    payload = _payload(model_page.read_text())
    assert [v["id"] for v in payload["variables"]] == [
        "stimulus",
        "kinase",
        "phosphatase",
    ]
    by_id = {s["id"]: s for s in payload["scenarios"]}
    assert by_id["stimulated"]["attractors"][0]["kind"] == "CYCLIC"
    assert by_id["cut"]["failures"] == []
    assert by_id["cut"]["rule_overrides"] == {"phosphatase": None}

    module_html = page.read_text()
    assert "Executable models" in module_html
    assert 'href="../models/loop_boolean.html"' in module_html
    assert "Run in browser" in module_html


def test_render_all_writes_models_index_and_module_filter(tmp_path: Path) -> None:
    modules, out = _write(tmp_path)
    render_all_modules(
        modules_dir=modules, output_dir=out, genes_dir=tmp_path / "genes"
    )
    index = (tmp_path / "pages" / "models" / "index.html").read_text()
    assert "Loop as a Boolean network" in index and "A kinetic model" in index
    assert 'data-type="Kinetic"' in index
    assert "all expectations hold" in index
    modules_index = (out / "index.html").read_text()
    assert 'data-model-types="BOOLEAN KINETIC"' in modules_index
    assert "data-model-filter" in modules_index


def test_model_summaries_report_failing_scenarios(tmp_path: Path) -> None:
    import yaml

    doc = yaml.safe_load(MODULE_YAML)
    doc["executable_models"][0]["scenarios"][0]["expected_attractor_kind"] = (
        "FIXED_POINT"
    )
    rows = model_summaries(
        doc,
        Path("modules/loop.yaml"),
        Path("pages/modules/loop.html"),
        Path("pages/models"),
        from_file=Path("pages/models/index.html"),
    )
    boolean = rows[0]
    assert boolean["interactive"] and boolean["scenarios_passed"] == 1
    assert boolean["page_href"] == "loop_boolean.html"
    assert boolean["module_href"] == "../modules/loop.html"
    out = render_models_index(rows, tmp_path / "models")
    assert "1 failing" in out.read_text()
