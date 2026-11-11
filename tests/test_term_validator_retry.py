"""The shell entry point recovers transport failures without accepting bad data."""

import json
import os
from pathlib import Path
import subprocess
import sys

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/run_term_validator.sh"
OUTAGE = "Terms could not be checked; this is not a data error."


def run_wrapper(tmp_path, reports):
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
        "assert '--strict' in sys.argv\n"
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
    result = subprocess.run(
        ["bash", str(SCRIPT), "validate-data", "review.yaml"],
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
    assert "retrying complete term validation" in result.stderr


def test_exhausted_outage_remains_failure(tmp_path):
    result, count = run_wrapper(tmp_path, [(2, OUTAGE)])
    assert result.returncode == 2
    assert count == 3
    assert OUTAGE in result.stdout


@pytest.mark.parametrize("first", [[], [(2, OUTAGE)]])
@pytest.mark.parametrize(
    "invalid", [(1, "ERROR: wrong GO branch"), (0, "WARN: label mismatch")]
)
def test_invalid_data_fails_even_after_service_recovers(tmp_path, first, invalid):
    result, count = run_wrapper(tmp_path, first + [invalid])
    assert result.returncode != 0
    assert count == len(first) + 1
    assert invalid[1] in result.stdout
