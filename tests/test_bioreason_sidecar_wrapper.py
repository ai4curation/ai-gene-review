"""Argument-boundary test for the public BioReason sidecar wrapper."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_refresh_bioreason_sidecars_uses_project_generator(tmp_path: Path) -> None:
    """The public recipe should invoke the deterministic generator through uv."""
    generator = REPO_ROOT / "projects/BIOREASON_COMPARISON/write_benchmark_sidecars.py"
    assert generator.exists()

    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    log_path = tmp_path / "argv.json"
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys

with open(os.environ["BIOREASON_SIDECAR_ARGV_LOG"], "w") as handle:
    json.dump(sys.argv[1:], handle)
"""
    )
    fake_uv.chmod(0o755)

    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
    env["BIOREASON_SIDECAR_ARGV_LOG"] = str(log_path)
    result = subprocess.run(
        [
            "just",
            "--justfile",
            str(REPO_ROOT / "justfile"),
            "--working-directory",
            str(tmp_path),
            "refresh-bioreason-benchmark-sidecars",
        ],
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == [
        "run",
        "python",
        "projects/BIOREASON_COMPARISON/write_benchmark_sidecars.py",
    ]
