"""Tests for module deep-research wrapper helpers."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "module_deep_research_wrapper.py"
SPEC = importlib.util.spec_from_file_location("module_deep_research_wrapper", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
module_deep_research = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module_deep_research
SPEC.loader.exec_module(module_deep_research)


MODULE_YAML = """id: MODULE:peroxisome_lifecycle
title: Peroxisome lifecycle
description: Peroxisome maintenance and import.
module:
  id: peroxisome_lifecycle
  label: Peroxisome lifecycle
  module_type: ORGANELLE_LIFECYCLE
  concepts:
    - preferred_term: peroxisome organization
      term:
        id: GO:0007031
        label: peroxisome organization
  annotons:
    - id: cargo_recognition
      label: Cargo recognition
      participant:
        selector_type: FAMILY
        family:
          preferred_term: Pex5 family
          term:
            id: PANTHER:PTHR10130
            label: peroxisomal biogenesis factor 5
      function:
        preferred_term: peroxisomal matrix protein signal-1 binding
  connections:
    - source: cargo_recognition
      target: importomer_docking
      connection_type: PROVIDES_INPUT_FOR
"""


def test_resolve_module_path_accepts_stem_and_module_id(tmp_path):
    modules_dir = tmp_path / "modules"
    modules_dir.mkdir()
    path = modules_dir / "peroxisome-lifecycle.yaml"
    path.write_text(MODULE_YAML, encoding="utf-8")

    assert module_deep_research.resolve_module_path(
        "peroxisome-lifecycle", modules_dir
    ) == path
    assert module_deep_research.resolve_module_path(
        "peroxisome_lifecycle", modules_dir
    ) == path
    assert module_deep_research.resolve_module_path(
        "MODULE:peroxisome_lifecycle", modules_dir
    ) == path


def test_build_command_maps_perplexity_lite_but_keeps_output_slug(tmp_path):
    modules_dir = tmp_path / "modules"
    modules_dir.mkdir()
    path = modules_dir / "peroxisome-lifecycle.yaml"
    path.write_text(MODULE_YAML, encoding="utf-8")
    data = module_deep_research.load_module_yaml(path)
    output_path = module_deep_research.output_path_for_research(path, "perplexity-lite")

    cmd = module_deep_research.build_deep_research_command(
        module_path=path,
        data=data,
        provider="perplexity-lite",
        output_path=output_path,
        template_path=Path("templates/module_research.md.j2"),
        extra_args=["--param", "model=sonar-pro"],
    )

    assert output_path == modules_dir / "peroxisome-lifecycle-deep-research-perplexity-lite.md"
    assert cmd[cmd.index("--provider") + 1] == "perplexity"
    assert "--param" in cmd
    assert any(arg.startswith("module_outline=") for arg in cmd)
    assert any("Pex5 family" in arg for arg in cmd)


def test_build_command_maps_codex_to_cyberian_agent_type(tmp_path):
    modules_dir = tmp_path / "modules"
    modules_dir.mkdir()
    path = modules_dir / "peroxisome-lifecycle.yaml"
    path.write_text(MODULE_YAML, encoding="utf-8")
    data = module_deep_research.load_module_yaml(path)
    output_path = module_deep_research.output_path_for_research(path, "codex")

    cmd = module_deep_research.build_deep_research_command(
        module_path=path,
        data=data,
        provider="codex",
        output_path=output_path,
        template_path=Path("templates/module_research.md.j2"),
    )

    assert output_path == modules_dir / "peroxisome-lifecycle-deep-research-codex.md"
    assert cmd[cmd.index("--provider") + 1] == "cyberian"
    assert "--param" in cmd
    assert "agent_type=codex" in cmd


def test_module_template_renders_through_deep_research_processor():
    from deep_research_client.processing import ResearchProcessor

    processor = ResearchProcessor()
    query, metadata = processor.process_template_file(
        Path("templates/module_research.md.j2"),
        [
            "module_title=Peroxisome lifecycle",
            "module_summary=Peroxisome assembly and function.",
            "module_outline=- Matrix protein import",
            "module_connections=- Matrix import feeds into metabolism",
        ],
    )

    assert metadata["template_format"] == "jinja"
    assert "Peroxisome lifecycle" in query
    assert "Peroxisome assembly and function." in query
    assert "{module_title}" not in query
    assert "{{ module_title }}" not in query


def test_output_placeholder_detection(tmp_path):
    report = tmp_path / "report.md"
    report.write_text("Question: {module_title}\n", encoding="utf-8")

    assert module_deep_research.output_contains_unresolved_placeholders(report)

    report.write_text("Question: Peroxisome lifecycle\n", encoding="utf-8")
    assert not module_deep_research.output_contains_unresolved_placeholders(report)
