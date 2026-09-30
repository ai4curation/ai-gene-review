"""End-to-end tests for the generic deep-research provider interface."""

from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_wrapper():
    scripts_dir = ROOT / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    path = scripts_dir / "deep_research_wrapper.py"
    spec = importlib.util.spec_from_file_location("deep_research_wrapper", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    ("provider_args", "expected_provider"),
    [
        (["--provider", "perplexity"], "perplexity"),
        (["openai"], "openai"),
    ],
)
def test_main_accepts_option_and_legacy_positional_provider(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    provider_args: list[str],
    expected_provider: str,
) -> None:
    wrapper = load_wrapper()
    captured: dict[str, object] = {}

    def fake_run_deep_research(**kwargs):
        captured.update(kwargs)
        return 0

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(wrapper, "run_deep_research", fake_run_deep_research)
    monkeypatch.setattr(
        sys,
        "argv",
        ["deep_research_wrapper.py", "human", "TP53", *provider_args],
    )

    assert wrapper.main() == 0
    assert captured["provider"] == expected_provider


def test_select_provider_rejects_conflicting_values() -> None:
    wrapper = load_wrapper()

    with pytest.raises(ValueError, match="Conflicting providers"):
        wrapper.select_provider("falcon", "perplexity")


def test_supported_providers_cover_public_gene_recipes() -> None:
    wrapper = load_wrapper()
    recipe_text = (ROOT / "project.justfile").read_text()
    recipe_providers = dict(
        re.findall(
            r"^deep-research-([a-z-]+)[^\n]*:\n"
            r"\s+uv run python scripts/deep_research_wrapper\.py "
            r"\{\{organism\}\} \{\{gene_id\}\} ([a-z-]+)",
            recipe_text,
            flags=re.MULTILINE,
        )
    )

    assert recipe_providers
    assert set(recipe_providers.values()) <= set(wrapper.PROVIDERS)
    assert all(recipe == provider for recipe, provider in recipe_providers.items())


def test_select_provider_rejects_unknown_value() -> None:
    wrapper = load_wrapper()

    with pytest.raises(ValueError, match="Unsupported provider 'perplexty'"):
        wrapper.select_provider(None, "perplexty")


def test_build_command_maps_codex_to_cyberian_agent_type(tmp_path: Path) -> None:
    wrapper = load_wrapper()

    cmd = wrapper._build_cmd(
        organism="human",
        gene_id="TP53",
        provider="codex",
        gene_symbol="TP53",
        output_path=tmp_path / "TP53-deep-research-codex.md",
    )

    assert cmd[cmd.index("--provider") + 1] == "cyberian"
    assert "agent_type=codex" in cmd


def test_fallback_after_hyphenated_provider_uses_canonical_output_path(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    wrapper = load_wrapper()
    gene_dir = tmp_path / "TP53"
    calls: list[list[str]] = []

    def fake_run(cmd, **kwargs):
        calls.append(cmd)
        return subprocess.CompletedProcess(cmd, returncode=1 if len(calls) == 1 else 0)

    monkeypatch.setattr(wrapper.subprocess, "run", fake_run)

    result = wrapper.run_deep_research(
        organism="human",
        gene_id="TP53",
        provider="perplexity-lite",
        gene_symbol="TP53",
        output_path=gene_dir / "TP53-deep-research-perplexity-lite.md",
        use_template=False,
        fallback_providers=["falcon"],
    )

    assert result == 0
    assert len(calls) == 2
    assert calls[0][calls[0].index("--output") + 1] == str(
        gene_dir / "TP53-deep-research-perplexity-lite.md"
    )
    assert calls[1][calls[1].index("--output") + 1] == str(
        gene_dir / "TP53-deep-research-falcon.md"
    )


@pytest.mark.parametrize(
    "provider_args",
    [
        ["--provider", "perplexty"],
        ["perplexty"],
        ["--provider", "openai", "--fallback", "perplexty"],
    ],
)
def test_main_rejects_unknown_primary_and_fallback_providers(
    monkeypatch: pytest.MonkeyPatch,
    provider_args: list[str],
) -> None:
    wrapper = load_wrapper()
    monkeypatch.setattr(
        sys,
        "argv",
        ["deep_research_wrapper.py", "human", "TP53", *provider_args],
    )

    with pytest.raises(SystemExit) as error:
        wrapper.main()

    assert error.value.code == 2


def test_generic_just_recipe_forwards_arguments(tmp_path: Path) -> None:
    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys

with open(os.environ["DEEP_RESEARCH_ARGV_LOG"], "w") as handle:
    json.dump(sys.argv[1:], handle)
"""
    )
    fake_uv.chmod(0o755)
    log_path = tmp_path / "argv.json"
    env = os.environ.copy()
    env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
    env["DEEP_RESEARCH_ARGV_LOG"] = str(log_path)

    result = subprocess.run(
        [
            "just",
            "deep-research",
            "human",
            "TP53",
            "--provider",
            "perplexity",
            "--alias",
            "TP53",
            "--timeout",
            "42",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=120,
    )

    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == [
        "run",
        "python",
        "scripts/deep_research_wrapper.py",
        "human",
        "TP53",
        "--provider",
        "perplexity",
        "--alias",
        "TP53",
        "--timeout",
        "42",
    ]
