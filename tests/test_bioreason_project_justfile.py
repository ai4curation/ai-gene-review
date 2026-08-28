"""Regression tests for the BioReason project-local justfile."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_JUSTFILE = REPO_ROOT / "projects/BIOREASON_COMPARISON/justfile"
PATH_FUNCTION_INTERPOLATION = re.compile(
    r"\{\{\s*(?:justfile_directory|just_executable|invocation_directory)\(\)\s*\}\}"
)


def test_all_path_function_interpolations_are_quoted() -> None:
    """Every path-producing interpolation should begin inside a shell quote."""
    text = PROJECT_JUSTFILE.read_text()
    unquoted_occurrences = [
        match.group(0)
        for match in PATH_FUNCTION_INTERPOLATION.finditer(text)
        if match.start() == 0 or text[match.start() - 1] not in {'"', "'"}
    ]
    assert unquoted_occurrences == []


def test_gogpt_overlap_supports_repository_paths_with_spaces(tmp_path: Path) -> None:
    """Project recipes should quote the directory supplied by just."""
    copied_root = tmp_path / "repository with spaces"
    copied_project = copied_root / "projects/BIOREASON_COMPARISON"
    copied_project.mkdir(parents=True)
    copied_justfile = copied_project / "justfile"
    shutil.copyfile(PROJECT_JUSTFILE, copied_justfile)

    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    log_path = tmp_path / "uv-call.json"
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys

with open(os.environ["BIOREASON_PROJECT_JUSTFILE_LOG"], "w") as handle:
    json.dump({"argv": sys.argv[1:], "cwd": os.getcwd()}, handle)
"""
    )
    fake_uv.chmod(0o755)

    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
    env["BIOREASON_PROJECT_JUSTFILE_LOG"] = str(log_path)
    result = subprocess.run(
        ["just", "--justfile", str(copied_justfile), "gogpt-overlap"],
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == {
        "argv": ["run", "python", "scripts/gogpt_compare_levels.py"],
        "cwd": str(copied_root),
    }
