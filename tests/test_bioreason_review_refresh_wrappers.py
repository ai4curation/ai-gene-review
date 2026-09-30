"""Argument-boundary tests for public BioReason review refresh wrappers."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("recipe", "expected_argv"),
    [
        (
            "check-bioreason-sft-reviews",
            ["run", "python", "scripts/auto_review_sft_predictions.py"],
        ),
        (
            "refresh-bioreason-sft-reviews",
            ["run", "python", "scripts/auto_review_sft_predictions.py", "--apply"],
        ),
        (
            "check-gogpt-web-exports",
            [
                "run",
                "python",
                "scripts/gogpt_predict.py",
                "--check-web-exports",
            ],
        ),
        (
            "refresh-gogpt-web-exports",
            [
                "run",
                "python",
                "scripts/gogpt_predict.py",
                "--refresh-web-exports",
            ],
        ),
    ],
)
def test_review_refresh_wrapper_arguments(
    tmp_path: Path, recipe: str, expected_argv: list[str]
) -> None:
    """Each recipe should preserve the audited CLI's argument boundary."""
    script_argument = next(
        argument for argument in expected_argv if argument.startswith("scripts/")
    )
    assert (REPO_ROOT / script_argument).is_file()

    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    log_path = tmp_path / "argv.json"
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys

with open(os.environ["BIOREASON_REFRESH_ARGV_LOG"], "w") as handle:
    json.dump(sys.argv[1:], handle)
"""
    )
    fake_uv.chmod(0o755)

    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
    env["BIOREASON_REFRESH_ARGV_LOG"] = str(log_path)
    result = subprocess.run(
        [
            "just",
            "--justfile",
            str(REPO_ROOT / "justfile"),
            "--working-directory",
            str(tmp_path),
            recipe,
        ],
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == expected_argv


@pytest.mark.parametrize(
    ("script", "flag"),
    [
        ("scripts/auto_review_sft_predictions.py", "--apply"),
        ("scripts/gogpt_predict.py", "--check-web-exports"),
        ("scripts/gogpt_predict.py", "--refresh-web-exports"),
    ],
)
def test_review_refresh_cli_supports_wrapped_flag(script: str, flag: str) -> None:
    """The target parser should advertise every option exposed by a recipe."""
    target = REPO_ROOT / script
    assert target.is_file()
    result = subprocess.run(
        [sys.executable, str(target), "--help"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    assert flag in result.stdout
