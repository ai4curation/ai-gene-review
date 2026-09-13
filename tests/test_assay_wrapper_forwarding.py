"""Argument-boundary tests for the remaining ASSAY_TO_FUNCTION wrappers."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("recipe", "fixed_argv"),
    [
        (
            "assay-flag",
            ["run", "python", "projects/ASSAY_TO_FUNCTION/flag_candidates.py"],
        ),
        (
            "assay-consolidate",
            [
                "run",
                "--with",
                "matplotlib",
                "python",
                "projects/ASSAY_TO_FUNCTION/consolidate.py",
            ],
        ),
        (
            "assay-stage-hypotheses",
            ["run", "python", "projects/ASSAY_TO_FUNCTION/stage_hypotheses.py"],
        ),
    ],
)
def test_assay_wrappers_preserve_exact_argument_boundaries(
    tmp_path: Path,
    recipe: str,
    fixed_argv: list[str],
) -> None:
    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys

with open(os.environ["ASSAY_WRAPPER_ARGV_LOG"], "w") as handle:
    json.dump(sys.argv[1:], handle)
"""
    )
    fake_uv.chmod(0o755)

    log_path = tmp_path / "argv log.json"
    env = os.environ.copy()
    env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
    env["ASSAY_WRAPPER_ARGV_LOG"] = str(log_path)
    tail = [
        "--input",
        str(tmp_path / "input set (draft), v1?.tsv"),
        "--label",
        "multiword value; exact?",
        "--",
        "A -- B",
    ]

    for forwarded, expected in ((tail, fixed_argv + tail), ([], fixed_argv)):
        result = subprocess.run(
            ["just", recipe, *forwarded],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
            env=env,
            timeout=30,
        )
        assert result.returncode == 0, result.stderr
        assert json.loads(log_path.read_text()) == expected
