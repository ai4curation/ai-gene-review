"""Tests for provider deep research frontmatter validation."""

from __future__ import annotations

import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_deep_research.py"
SPEC = importlib.util.spec_from_file_location("validate_deep_research", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
validate_deep_research = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_deep_research)


def test_validate_deep_research_accepts_valid_provider_file(tmp_path):
    for provider in (
        "openai",
        "perplexity-lite",
        "cyberian",
        "openscientist",
        "asta",
    ):
        path = tmp_path / f"GENE-deep-research-{provider}.md"
        path.write_text(
            "---\n"
            f"provider: {provider}\n"
            "start_time: '2026-03-21T00:00:00'\n"
            "end_time: '2026-03-21T00:05:00'\n"
            "---\n\n"
            "# Report\n",
            encoding="utf-8",
        )

    assert validate_deep_research.validate_files([tmp_path]) == 0


def test_validate_deep_research_rejects_missing_frontmatter(tmp_path):
    path = tmp_path / "GENE-deep-research-perplexity.md"
    path.write_text("# Not real deep research output\n", encoding="utf-8")

    assert validate_deep_research.validate_files([tmp_path]) == 1


def test_validate_deep_research_rejects_missing_required_field(tmp_path):
    path = tmp_path / "GENE-deep-research-falcon.md"
    path.write_text(
        "---\n"
        "provider: falcon\n"
        "start_time: '2026-03-21T00:00:00'\n"
        "---\n\n"
        "# Report\n",
        encoding="utf-8",
    )

    assert validate_deep_research.validate_files([tmp_path]) == 1


def test_validate_deep_research_ignores_manual_files(tmp_path):
    for filename in (
        "GENE-deep-research-manual.md",
        "GENE-deep-research-bioreason-sft.md",
        "GENE-deep-research-openai-citations.md",
        "GENE-deep-research-openai.md.citations.md",
    ):
        path = tmp_path / filename
        path.write_text("# Sidecar notes\n", encoding="utf-8")

    assert validate_deep_research.validate_files([tmp_path]) == 0
