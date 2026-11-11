"""The shell entry point recovers transport failures without accepting bad data."""

import json
import os
from pathlib import Path
import subprocess
import sys

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/run_term_validator.sh"
OUTAGE = "Terms could not be checked; this is not a data error."


def run_wrapper(tmp_path, reports, strict=True):
    """Substitute a deterministic validator, exercising the real shell wrapper."""
    (tmp_path / "reports.json").write_text(json.dumps(reports))
    executable = tmp_path / "uv"
    executable.write_text(
        f"#!{sys.executable}\n"
        "import json, pathlib, sys\n"
        "root = pathlib.Path(__file__).parent\n"
        "if '--help' in sys.argv:\n"
        "    print('--strict')\n"
        "    sys.exit(0)\n"
        f"assert ('--strict' in sys.argv) == {strict!r}\n"
        "count = root / 'count'\n"
        "n = int(count.read_text()) if count.exists() else 0\n"
        "count.write_text(str(n + 1))\n"
        "reports = json.loads((root / 'reports.json').read_text())\n"
        "code, report = reports[min(n, len(reports) - 1)]\n"
        "print(report)\n"
        "sys.exit(code)\n"
    )
    executable.chmod(0o755)
    sleep = tmp_path / "sleep"
    sleep.write_text("#!/bin/sh\nexit 0\n")
    sleep.chmod(0o755)
    command = (
        ["bash", str(SCRIPT), "validate-data", "review.yaml"]
        if strict else
        ["bash", str(SCRIPT.with_name("retry_ontology_validation.sh")),
         "uv", "run", "linkml-term-validator", "validate-data", "review.yaml"]
    )
    result = subprocess.run(
        command,
        env={**os.environ, "PATH": f"{tmp_path}{os.pathsep}{os.environ['PATH']}"},
        capture_output=True,
        text=True,
        timeout=10,
    )
    return result, int((tmp_path / "count").read_text())


def test_recovers_outage_without_leaking_error_report(tmp_path):
    result, count = run_wrapper(tmp_path, [(2, OUTAGE), (0, "Validation passed")])
    assert result.returncode == 0
    assert count == 2
    assert OUTAGE not in result.stdout + result.stderr
    assert "retrying complete term validation" in result.stdout + result.stderr


def test_exhausted_outage_remains_failure(tmp_path):
    result, count = run_wrapper(tmp_path, [(2, OUTAGE)])
    assert result.returncode == 2
    assert count == 3
    assert OUTAGE in result.stdout
    assert "Unable to validate" in result.stderr + result.stdout


@pytest.mark.parametrize("strict", [True, False])
def test_zero_status_cannot_hide_skipped_validation(tmp_path, strict):
    result, count = run_wrapper(tmp_path, [(0, OUTAGE)], strict=strict)
    assert result.returncode != 0
    assert count == 3
    assert OUTAGE in result.stdout
    assert "Unable to validate" in result.stderr + result.stdout


def test_corpus_retry_does_not_enable_strict_warning_gate(tmp_path):
    result, count = run_wrapper(
        tmp_path, [(2, OUTAGE), (0, "WARN: GO label mismatch")], strict=False
    )
    assert result.returncode == 0
    assert count == 2
    assert "WARN: GO label mismatch" in result.stdout


def test_corpus_retry_preserves_failure_exit(tmp_path):
    result, count = run_wrapper(
        tmp_path, [(2, OUTAGE), (1, "ERROR: wrong GO branch")], strict=False
    )
    assert result.returncode == 1
    assert count == 2


def test_all_recipe_term_validation_uses_shared_helper():
    text = (SCRIPT.parents[1] / "project.justfile").read_text()
    direct = [line for line in text.splitlines()
              if "uv run linkml-term-validator validate-data" in line]
    assert len(direct) >= 3
    assert all("bash scripts/retry_ontology_validation.sh" in line for line in direct)


@pytest.mark.parametrize("first", [[], [(2, OUTAGE)]])
@pytest.mark.parametrize(
    "invalid", [(1, "ERROR: wrong GO branch"), (0, "WARN: label mismatch")]
)
def test_invalid_data_fails_even_after_service_recovers(tmp_path, first, invalid):
    result, count = run_wrapper(tmp_path, first + [invalid])
    assert result.returncode != 0
    assert count == len(first) + 1
    assert invalid[1] in result.stdout
