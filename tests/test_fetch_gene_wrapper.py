"""Argument-boundary tests for the public gene-fetch wrapper."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path


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

with open(os.environ["FETCH_GENE_ARGV_LOG"], "w") as handle:
    json.dump(sys.argv[1:], handle)
"""
    )
    fake_uv.chmod(0o755)
    return fake_bin, tmp_path / "argv log.json"


def _run_fetch_gene(
    tmp_path: Path, fake_bin: Path, log_path: Path, *args: str
) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
    env["FETCH_GENE_ARGV_LOG"] = str(log_path)
    return subprocess.run(
        [
            "just",
            "--justfile",
            str(REPO_ROOT / "justfile"),
            "--working-directory",
            str(tmp_path),
            "fetch-gene",
            *args,
        ],
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=30,
    )


def test_fetch_gene_wrapper_preserves_exact_argument_boundaries(tmp_path: Path) -> None:
    fake_bin, log_path = _write_fake_uv(tmp_path)
    organism = "TESTORG"
    gene = "Gene Symbol"

    result = _run_fetch_gene(tmp_path, fake_bin, log_path, organism, gene)
    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == [
        "run",
        "--no-dev",
        "ai-gene-review",
        "fetch-gene",
        organism,
        gene,
        "--output-dir",
        ".",
    ]

    tail = [
        "--alias",
        "Alias (draft), v1? $GENE_ALIAS",
        "--uniprot-id",
        "P12345",
        "--no-seed",
        "--force",
    ]
    result = _run_fetch_gene(tmp_path, fake_bin, log_path, organism, gene, *tail)
    assert result.returncode == 0, result.stderr
    assert json.loads(log_path.read_text()) == [
        "run",
        "--no-dev",
        "ai-gene-review",
        "fetch-gene",
        organism,
        gene,
        "--output-dir",
        ".",
        *tail,
    ]


def test_fetch_gene_wrapper_recognizes_force_as_an_exact_flag(tmp_path: Path) -> None:
    fake_bin, log_path = _write_fake_uv(tmp_path)
    organism = "TESTORG"
    gene = "EUG1"
    gene_dir = tmp_path / "genes" / organism / gene
    gene_dir.mkdir(parents=True)
    (gene_dir / f"{gene}-uniprot.txt").write_text("existing\n")

    result = _run_fetch_gene(
        tmp_path,
        fake_bin,
        log_path,
        organism,
        gene,
        "--uniprot-id",
        "not--force",
    )
    assert result.returncode == 0, result.stderr
    assert "already exists" in result.stdout

    result = _run_fetch_gene(
        tmp_path, fake_bin, log_path, organism, gene, "-f"
    )
    assert result.returncode == 0, result.stderr
    assert "already exists" not in result.stdout
    assert json.loads(log_path.read_text())[-1] == "-f"


def test_fetch_gene_wrapper_checks_the_aliased_output_path(tmp_path: Path) -> None:
    fake_bin, log_path = _write_fake_uv(tmp_path)
    organism = "TESTORG"
    gene = "SourceGene"
    alias = "Alias (draft), v1? $GENE_ALIAS"
    alias_dir = tmp_path / "genes" / organism / alias
    alias_dir.mkdir(parents=True)
    (alias_dir / f"{alias}-goa.tsv").write_text("existing\n")
    source_dir = tmp_path / "genes" / organism / gene
    source_dir.mkdir(parents=True)
    (source_dir / f"{gene}-uniprot.txt").write_text("existing\n")

    tail = ["--alias", alias, "--uniprot-id", "P12345"]
    result = _run_fetch_gene(tmp_path, fake_bin, log_path, organism, gene, *tail)
    assert result.returncode == 0, result.stderr
    assert f"Gene data for {organism}/{alias} already exists" in result.stdout
    assert json.loads(log_path.read_text())[-len(tail) :] == tail

    result = _run_fetch_gene(
        tmp_path, fake_bin, log_path, organism, gene, "-a", alias, "-f"
    )
    assert result.returncode == 0, result.stderr
    assert "already exists" not in result.stdout

    result = _run_fetch_gene(
        tmp_path, fake_bin, log_path, organism, gene, f"--alias={alias}"
    )
    assert result.returncode == 0, result.stderr
    assert f"Gene data for {organism}/{alias} already exists" in result.stdout

    result = _run_fetch_gene(
        tmp_path, fake_bin, log_path, organism, gene, f"-a{alias}"
    )
    assert result.returncode == 0, result.stderr
    assert f"Gene data for {organism}/{alias} already exists" in result.stdout

    result = _run_fetch_gene(
        tmp_path, fake_bin, log_path, organism, gene, "-fa", alias
    )
    assert result.returncode == 0, result.stderr
    assert "already exists" not in result.stdout

    result = _run_fetch_gene(
        tmp_path, fake_bin, log_path, organism, gene, f"-fa{alias}"
    )
    assert result.returncode == 0, result.stderr
    assert "already exists" not in result.stdout

    result = _run_fetch_gene(
        tmp_path, fake_bin, log_path, organism, gene, "--alias="
    )
    assert result.returncode == 0, result.stderr
    assert f"Gene data for {organism}/{gene} already exists" in result.stdout
