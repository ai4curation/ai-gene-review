"""Public-wrapper regressions for rule-review validation."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]


def run_rules_validate(review_path: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    return subprocess.run(
        [
            "just",
            "--justfile",
            str(REPO_ROOT / "justfile"),
            "--working-directory",
            str(REPO_ROOT),
            "rules-validate",
            str(review_path),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=120,
    )


def write_rule_review(path: Path, *, include_rule_type: bool) -> None:
    review = {
        "id": "ARBA00000001",
        "rule": {
            "rule_id": "ARBA00000001",
            "condition_sets": [],
            "entries": [],
        },
        "action": "UNDECIDED",
    }
    if include_rule_type:
        review["rule_type"] = "ARBA"
    path.write_text(yaml.safe_dump(review, sort_keys=False))


def test_rules_validate_accepts_schema_valid_review(tmp_path: Path) -> None:
    review_path = tmp_path / "valid-review.yaml"
    write_rule_review(review_path, include_rule_type=True)

    result = run_rules_validate(review_path)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "✓ All 1 review(s) valid" in result.stdout


def test_rules_validate_rejects_schema_invalid_review(tmp_path: Path) -> None:
    review_path = tmp_path / "invalid-review.yaml"
    write_rule_review(review_path, include_rule_type=False)

    result = run_rules_validate(review_path)
    output = result.stdout + result.stderr

    assert result.returncode != 0
    assert "Schema validation failed" in output
    assert "rule_type" in output
    assert "required property" in output
    assert "✗ 1 invalid, 0 valid" in output
