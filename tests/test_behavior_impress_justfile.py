"""Regression tests for the IMPReSS project-local justfile."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

from tests.justfile_quoting import find_unquoted_recipe_path_interpolations


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_JUSTFILE = REPO_ROOT / "projects/BEHAVIOR/impress/justfile"


def _copy_project_justfile(tmp_path: Path) -> tuple[Path, Path]:
    copied_root = tmp_path / "repository with spaces"
    copied_project = copied_root / "projects/BEHAVIOR/impress"
    copied_project.mkdir(parents=True)
    copied_justfile = copied_project / "justfile"
    shutil.copyfile(PROJECT_JUSTFILE, copied_justfile)
    return copied_root, copied_justfile


def _write_fake_uv(tmp_path: Path) -> tuple[Path, Path]:
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
    return fake_bin, log_path


def _run_with_fake_uv(
    tmp_path: Path, copied_justfile: Path, *recipe_args: str
) -> tuple[subprocess.CompletedProcess[str], Path]:
    fake_bin, log_path = _write_fake_uv(tmp_path)
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
    env["IMPRESS_JUSTFILE_LOG"] = str(log_path)
    result = subprocess.run(
        ["just", "--justfile", str(copied_justfile), *recipe_args],
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=30,
    )
    return result, log_path


def test_all_impress_recipe_paths_are_quoted() -> None:
    """Every root or justfile interpolation used as a shell path should be quoted."""
    assert find_unquoted_recipe_path_interpolations(
        PROJECT_JUSTFILE.read_text(),
        {"root", "justfile()", "just_executable()", "justfile_directory()"},
    ) == []


def test_check_supports_repository_paths_with_spaces(tmp_path: Path) -> None:
    """Root-changing recipes should preserve a space-containing repository path."""
    copied_root, copied_justfile = _copy_project_justfile(tmp_path)
    result, log_path = _run_with_fake_uv(tmp_path, copied_justfile, "check")

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


def test_ingest_preserves_pipeline_override_with_spaces(tmp_path: Path) -> None:
    """A user-supplied pipeline value should remain one command argument."""
    copied_root, copied_justfile = _copy_project_justfile(tmp_path)
    result, log_path = _run_with_fake_uv(
        tmp_path, copied_justfile, "pipelines=IMPC_001 custom", "ingest"
    )

    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == {
        "argv": [
            "run",
            "python",
            "projects/BEHAVIOR/impress/ingest_impress.py",
            "--pipelines",
            "IMPC_001 custom",
            "--out-dir",
            "projects/BEHAVIOR/impress",
        ],
        "cwd": str(copied_root),
    }


def test_default_listing_supports_justfile_paths_with_spaces(tmp_path: Path) -> None:
    """The nested listing should preserve spaced executable and justfile paths."""
    _, copied_justfile = _copy_project_justfile(tmp_path)
    real_just = shutil.which("just")
    assert real_just is not None
    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    copied_just = fake_bin / "just"
    shutil.copy2(real_just, copied_just)
    result = subprocess.run(
        [str(copied_just), "--justfile", str(copied_justfile)],
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    assert "ingest" in result.stdout
    assert "validate-online" in result.stdout
