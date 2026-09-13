"""Public-wrapper regressions for rule-review validation."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]


def run_rules_validate(
    review_path: Path,
    *args: str,
    extra_env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    env.update(extra_env or {})
    return subprocess.run(
        [
            "just",
            "--justfile",
            str(REPO_ROOT / "justfile"),
            "--working-directory",
            str(REPO_ROOT),
            "rules-validate",
            *args,
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


def install_warning_validator(tmp_path: Path) -> tuple[Path, dict[str, str]]:
    fake_bin = tmp_path / "fake-bin"
    fake_bin.mkdir()
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import os
import sys

if sys.argv[1:3] != ["run", "ai-gene-review"]:
    raise SystemExit(f"unexpected uv arguments: {sys.argv[1:]}")
os.execv(
    os.environ["RULE_VALIDATE_PYTHON"],
    [
        os.environ["RULE_VALIDATE_PYTHON"],
        "-c",
        "from ai_gene_review.cli import app; app()",
        *sys.argv[3:],
    ],
)
"""
    )
    fake_uv.chmod(0o755)
    fake_validator = fake_bin / "linkml-validate"
    fake_validator.write_text(
        """#!/usr/bin/env python3
print("[WARNING] synthetic schema warning")
"""
    )
    fake_validator.chmod(0o755)
    return fake_bin, {
        "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
        "RULE_VALIDATE_PYTHON": sys.executable,
    }


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


def test_rules_validate_verbose_displays_schema_warnings(tmp_path: Path) -> None:
    review_path = tmp_path / "warning-review.yaml"
    write_rule_review(review_path, include_rule_type=True)
    _, env = install_warning_validator(tmp_path)

    result = run_rules_validate(review_path, "--verbose", extra_env=env)
    output = result.stdout + result.stderr

    assert result.returncode == 0, output
    assert f"✓ {review_path}" in result.stdout
    assert "synthetic schema warning" in output
    assert "⚠" in output
    assert "✓ All 1 review(s) valid" in result.stdout
