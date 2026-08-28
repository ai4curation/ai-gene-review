"""Regression tests for the IMPReSS project-local justfile."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_JUSTFILE = REPO_ROOT / "projects/BEHAVIOR/impress/justfile"


def _copy_project_justfile(tmp_path: Path) -> tuple[Path, Path]:
    copied_root = tmp_path / "repository with spaces"
    copied_project = copied_root / "projects/BEHAVIOR/impress"
    copied_project.mkdir(parents=True)
    copied_justfile = copied_project / "justfile"
    shutil.copyfile(PROJECT_JUSTFILE, copied_justfile)
    return copied_root, copied_justfile


def test_all_impress_recipe_paths_are_quoted() -> None:
    """Every root or justfile interpolation used as a shell path should be quoted."""
    unquoted_occurrences = [
        token
        for line in PROJECT_JUSTFILE.read_text().splitlines()
        for token in ("{{root}}", "{{justfile()}}", "{{just_executable()}}")
        if token in line and f'"{token}' not in line and f"'{token}" not in line
    ]
    assert unquoted_occurrences == []


def test_check_supports_repository_paths_with_spaces(tmp_path: Path) -> None:
    """Root-changing recipes should preserve a space-containing repository path."""
    copied_root, copied_justfile = _copy_project_justfile(tmp_path)
    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    log_path = tmp_path / "uv-call.json"
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys

with open(os.environ["IMPRESS_JUSTFILE_LOG"], "w") as handle:
    json.dump({"argv": sys.argv[1:], "cwd": os.getcwd()}, handle)
"""
    )
    fake_uv.chmod(0o755)

    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
    env["IMPRESS_JUSTFILE_LOG"] = str(log_path)
    result = subprocess.run(
        ["just", "--justfile", str(copied_justfile), "check"],
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == {
        "argv": [
            "run",
            "python",
            "projects/BEHAVIOR/impress/check_behaviour_assays.py",
            "--out-dir",
            "projects/BEHAVIOR/impress",
        ],
        "cwd": str(copied_root),
    }


def test_default_listing_supports_justfile_paths_with_spaces(tmp_path: Path) -> None:
    """The nested recipe listing should preserve the copied justfile path."""
    _, copied_justfile = _copy_project_justfile(tmp_path)
    result = subprocess.run(
        ["just", "--justfile", str(copied_justfile)],
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    assert "check" in result.stdout
