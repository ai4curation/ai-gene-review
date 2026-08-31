"""End-to-end tests for the generic deep-research provider interface."""

from __future__ import annotations

import importlib.util
import json
import os
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

    assert set(wrapper.PROVIDERS) == {
        "openai",
        "perplexity",
        "perplexity-lite",
        "falcon",
        "cyberian",
        "codex",
        "asta",
        "openscientist",
    }


def test_select_provider_rejects_unknown_value() -> None:
    wrapper = load_wrapper()

    with pytest.raises(ValueError, match="Unsupported provider 'perplexty'"):
        wrapper.select_provider(None, "perplexty")


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
