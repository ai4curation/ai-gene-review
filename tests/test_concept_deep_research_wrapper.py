"""Tests for concept deep-research provider handling."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_wrapper():
    path = ROOT / "scripts" / "concept_deep_research_wrapper.py"
    spec = importlib.util.spec_from_file_location("concept_deep_research_wrapper", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_codex_maps_to_cyberian_agent_type(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    wrapper = load_wrapper()
    captured: list[str] = []

    def fake_run(cmd):
        captured.extend(cmd)
        return subprocess.CompletedProcess(cmd, returncode=0)

    monkeypatch.setattr(wrapper.subprocess, "run", fake_run)

    result = wrapper.run_deep_research(
        concept="spliceosome",
        concept_slug="spliceosome",
        provider="codex",
        output_path=tmp_path / "spliceosome-deep-research-codex.md",
        template_path=Path("templates/concept_research.md.j2"),
    )

    assert result == 0
    assert captured[captured.index("--provider") + 1] == "cyberian"
    assert "agent_type=codex" in captured


def test_main_preserves_codex_in_output_filename(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    wrapper = load_wrapper()
    captured: dict[str, object] = {}

    def fake_run_deep_research(**kwargs):
        captured.update(kwargs)
        return 0

    monkeypatch.setattr(wrapper, "run_deep_research", fake_run_deep_research)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "concept_deep_research_wrapper.py",
            "RNA splicing",
            "codex",
            "--output-dir",
            str(tmp_path),
        ],
    )

    assert wrapper.main() == 0
    assert captured["provider"] == "codex"
    assert captured["output_path"] == (
        tmp_path / "rna_splicing" / "rna_splicing-deep-research-codex.md"
    )


def test_public_codex_recipe_passes_canonical_provider() -> None:
    recipe_text = (ROOT / "project.justfile").read_text()

    assert (
        'term-deep-research-codex concept *args="":\n'
        '    uv run python scripts/concept_deep_research_wrapper.py "{{concept}}" codex {{args}}'
        in recipe_text
    )
