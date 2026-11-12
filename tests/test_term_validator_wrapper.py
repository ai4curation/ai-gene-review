"""The term-validator wrapper retries an ontology-service outage and nothing else."""

from __future__ import annotations

import os
import stat
import subprocess
from pathlib import Path

import pytest

WRAPPER = Path(__file__).parent.parent / "scripts" / "run_term_validator.sh"

# A stand-in for `uv`: it answers the wrapper's `--help` probe, then fails with the
# given exit code and message until the counter file reaches FAIL_TIMES.
FAKE_UV = """#!/usr/bin/env bash
if [[ "$*" == *"--help"* ]]; then echo "usage"; exit 0; fi
count=$(cat "$COUNTER" 2>/dev/null || echo 0)
count=$((count + 1))
echo "$count" > "$COUNTER"
if [[ $count -le $FAIL_TIMES ]]; then echo "$FAIL_MESSAGE" >&2; exit "$FAIL_CODE"; fi
echo "ok"
"""


def run_wrapper(tmp_path: Path, fail_times: int, fail_code: int, message: str) -> tuple[int, int, str]:
    """Run the wrapper against the stand-in; return (exit code, calls made, output)."""
    fake = tmp_path / "uv"
    fake.write_text(FAKE_UV)
    fake.chmod(fake.stat().st_mode | stat.S_IEXEC)
    counter = tmp_path / "count"
    env = {
        **os.environ,
        "PATH": f"{tmp_path}{os.pathsep}{os.environ['PATH']}",
        "COUNTER": str(counter),
        "FAIL_TIMES": str(fail_times),
        "FAIL_CODE": str(fail_code),
        "FAIL_MESSAGE": message,
        "TERM_VALIDATOR_RETRY_DELAY": "0",
    }
    done = subprocess.run([str(WRAPPER), "validate-data", "x.yaml"], env=env, capture_output=True, text=True)
    return done.returncode, int(counter.read_text()), done.stdout + done.stderr


OUTAGE = "Unable to validate at this time: ontology service unavailable."


@pytest.mark.parametrize(
    "fail_times,fail_code,message,expected_exit,expected_calls",
    [
        pytest.param(0, 0, "", 0, 1, id="success is not retried"),
        pytest.param(2, 2, OUTAGE, 0, 3, id="an outage is retried until the service answers"),
        pytest.param(5, 2, OUTAGE, 2, 3, id="a lasting outage still fails"),
        pytest.param(5, 1, "ERROR: term not found", 1, 1, id="a data error is not retried"),
        pytest.param(5, 2, "usage error", 2, 1, id="exit 2 without the outage message is not retried"),
    ],
)
def test_wrapper_retries_only_outages(
    tmp_path: Path, fail_times: int, fail_code: int, message: str, expected_exit: int, expected_calls: int
) -> None:
    exit_code, calls, _ = run_wrapper(tmp_path, fail_times, fail_code, message)
    assert (exit_code, calls) == (expected_exit, expected_calls)
