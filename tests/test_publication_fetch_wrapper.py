"""Argument-boundary tests for the publication-fetch wrappers."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("recipe", "required_args", "fixed_argv"),
    [
        (
            "fetch-pmid",
            ["PMID:11485577"],
            ["run", "ai-gene-review", "fetch-pmid", "PMID:11485577"],
        ),
        (
            "fetch-gene-pmids",
            ["yeast", "EUG1"],
            ["run", "ai-gene-review", "fetch-gene-pmids", "yeast", "EUG1"],
        ),
        (
            "fetch-pmids-from-file",
            ["PMID input (draft), v1?.txt"],
            [
                "run",
                "ai-gene-review",
                "fetch-pmids-from-file",
                "PMID input (draft), v1?.txt",
            ],
        ),
    ],
)
def test_publication_fetch_wrappers_preserve_exact_argument_boundaries(
    tmp_path: Path,
    recipe: str,
    required_args: list[str],
    fixed_argv: list[str],
) -> None:
    # The external command is replaced so this public-Just boundary test stays
    # network-free while still exercising Just's real positional forwarding.
    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys

with open(os.environ["PUBLICATION_FETCH_ARGV_LOG"], "w") as handle:
    json.dump(sys.argv[1:], handle)
"""
    )
    fake_uv.chmod(0o755)

    log_path = tmp_path / "argv log.json"
    output_dir = tmp_path / "publication cache (forced), v1?"
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
    env["PUBLICATION_FETCH_ARGV_LOG"] = str(log_path)

    cases = [
        ([], [], "publications"),
        ([], ["--force", "--delay", "0.0"], "publications"),
        ([str(output_dir)], [], str(output_dir)),
        ([str(output_dir)], ["--force", "--delay", "0.0"], str(output_dir)),
    ]
    for output_args, tail, expected_output_dir in cases:
        result = subprocess.run(
            ["just", recipe, *required_args, *output_args, *tail],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
            env=env,
            timeout=30,
        )
        assert result.returncode == 0, result.stderr
        assert json.loads(log_path.read_text()) == [
            *fixed_argv,
            "--output-dir",
            expected_output_dir,
            *tail,
        ]


def test_fetch_pmid_wrapper_preserves_multiple_pmids(tmp_path: Path) -> None:
    fake_bin = tmp_path / "fake bin"
    fake_bin.mkdir()
    fake_uv = fake_bin / "uv"
    fake_uv.write_text(
        """#!/usr/bin/env python3
import json
import os
import sys

with open(os.environ["PUBLICATION_FETCH_ARGV_LOG"], "w") as handle:
    json.dump(sys.argv[1:], handle)
"""
    )
    fake_uv.chmod(0o755)

    log_path = tmp_path / "argv log.json"
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
    env["PUBLICATION_FETCH_ARGV_LOG"] = str(log_path)

    result = subprocess.run(
        [
            "just",
            "fetch-pmid",
            "PMID:11485577",
            "1406650",
            "--force",
            "--delay",
            "0.0",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=30,
    )
    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == [
        "run",
        "ai-gene-review",
        "fetch-pmid",
        "PMID:11485577",
        "1406650",
        "--output-dir",
        "publications",
        "--force",
        "--delay",
        "0.0",
    ]
