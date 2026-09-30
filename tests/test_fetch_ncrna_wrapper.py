"""Argument-boundary tests for the public ncRNA-fetch wrappers."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]


def _write_fake_uv(tmp_path: Path) -> tuple[Path, Path]:
    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys

with open(os.environ["FETCH_NCRNA_ARGV_LOG"], "w") as handle:
    json.dump(sys.argv[1:], handle)
"""
    )
    fake_uv.chmod(0o755)
    return fake_bin, tmp_path / "argv log.json"


def _run_wrapper(
    tmp_path: Path, fake_bin: Path, log_path: Path, recipe: str, *args: str
) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
    env["FETCH_NCRNA_ARGV_LOG"] = str(log_path)
    return subprocess.run(
        [
            "just",
            "--justfile",
            str(REPO_ROOT / "justfile"),
            "--working-directory",
            str(tmp_path),
            recipe,
            *args,
        ],
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=30,
    )


@pytest.mark.parametrize("recipe", ["fetch-ncrna", "fetch-rna-gene"])
def test_fetch_ncrna_wrappers_preserve_exact_argument_boundaries(
    tmp_path: Path, recipe: str
) -> None:
    fake_bin, log_path = _write_fake_uv(tmp_path)
    organism = "TEST ORG"
    gene = "ncRNA (draft), v1? $GENE"
    fixed = [
        "run",
        "ai-gene-review",
        "fetch-ncrna",
        organism,
        gene,
        "--output-dir",
        ".",
    ]

    result = _run_wrapper(tmp_path, fake_bin, log_path, recipe, organism, gene)
    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == fixed

    tail = [
        "--alias",
        "Alias (draft), v1? $NCRNA_ALIAS",
        "--rnacentral-id",
        "URS000012345_9606",
        "--no-seed",
        "--force",
    ]
    result = _run_wrapper(
        tmp_path, fake_bin, log_path, recipe, organism, gene, *tail
    )
    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == [*fixed, *tail]
