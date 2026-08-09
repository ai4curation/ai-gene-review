"""End-to-end tests for rule-review wrapper argument forwarding."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]


def write_enriched_rule(cache_dir: Path, rule_id: str) -> Path:
    rule_dir = cache_dir / rule_id
    rule_dir.mkdir(parents=True)
    (rule_dir / f"{rule_id}.enriched.json").write_text(
        json.dumps(
            {
                "rule_set": {"condition_sets": [], "annotations": []},
                "reviewed_protein_count": 0,
                "unreviewed_protein_count": 0,
            }
        )
    )
    return rule_dir


def run_just(
    *args: str,
    extra_env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(extra_env or {})
    return subprocess.run(
        ["just", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=120,
    )


def test_init_rule_review_wrapper_uses_custom_cache_dir(tmp_path: Path) -> None:
    rule_id = "ARBA00026249"
    cache_dir = tmp_path / "rule cache (draft), v1?"
    rule_dir = write_enriched_rule(cache_dir, rule_id)

    result = run_just(
        "init-rule-review",
        rule_id,
        "--cache-dir",
        str(cache_dir),
    )

    assert result.returncode == 0, result.stderr
    review_path = rule_dir / f"{rule_id}-review.yaml"
    review = yaml.safe_load(review_path.read_text())
    assert review["id"] == rule_id
    assert review["rule_type"] == "ARBA"
    assert f"just analyze-rule {rule_id}" in result.stdout
    assert f"just sync-rule-review-single {rule_id}" in result.stdout
    assert f"just render-rule {rule_id}" in result.stdout


def test_init_unirule_omits_unsupported_analysis_next_steps(tmp_path: Path) -> None:
    rule_id = "UR000000070"
    cache_dir = tmp_path / "unirule cache"
    rule_dir = write_enriched_rule(cache_dir, rule_id)

    result = run_just(
        "init-rule-review",
        rule_id,
        "--cache-dir",
        str(cache_dir),
    )

    assert result.returncode == 0, result.stderr
    review = yaml.safe_load((rule_dir / f"{rule_id}-review.yaml").read_text())
    assert review["rule_type"] == "UniRule"
    assert "rules-deep-research-perplexity" in result.stdout
    assert "currently support ARBA IDs only" in result.stdout
    assert "analyze-rule" not in result.stdout
    assert "sync-rule-review-single" not in result.stdout
    assert "render-rule" not in result.stdout


def test_init_rule_review_wrapper_forwards_no_empty_tail(tmp_path: Path) -> None:
    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys

with open(os.environ["RULE_WRAPPER_ARGV_LOG"], "w") as handle:
    json.dump(sys.argv[1:], handle)
"""
    )
    fake_uv.chmod(0o755)

    log_path = tmp_path / "argv log.json"
    env = {
        "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
        "RULE_WRAPPER_ARGV_LOG": str(log_path),
    }
    result = run_just(
        "init-rule-review",
        "ARBA00026249",
        extra_env=env,
    )

    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == [
        "run",
        "ai-gene-review",
        "init-rule-review",
        "ARBA00026249",
    ]
