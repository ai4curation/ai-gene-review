"""scripts/term_validate.sh maps an ontology-service outage to a sentinel exit.

The whole point of the wrapper is that a transient outage (linkml-term-validator
exit 2 + "ontology service unavailable") becomes a skip (97) or a strict block
(96), while a genuine status passes through. If linkml-term-validator ever
stopped using exit 2 for the outage, the wrapper would silently become a no-op
on the next blip, so the contract is asserted here against the installed
package rather than only in the script's comments.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "scripts" / "term_validate.sh"


def test_ltv_service_unavailable_exit_code_is_2():
    """The wrapper keys the outage on exit code 2; lock that against drift."""
    from linkml_term_validator.cli import EXIT_SERVICE_UNAVAILABLE

    assert EXIT_SERVICE_UNAVAILABLE == 2


def _run_helper(tmp_path, *, simulate, strict=False, extra_env=None):
    """Run the helper with a stub `uv` that fakes linkml-term-validator."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    # The helper invokes `uv run linkml-term-validator ...`; the stub decides the
    # faked outcome from SIMULATE without touching the network.
    stub = f"""#!{sys.executable}
import os, sys
sim = os.environ["SIMULATE"]
if sim == "outage":
    sys.stderr.write("\\n\U0001f310 Unable to validate at this time: "
                     "ontology service unavailable.\\n"
                     "   could not reach ontology service to resolve "
                     "NCBITaxon:9606: Read timed out.\\n")
    sys.exit(2)
if sim == "usage":
    sys.stderr.write("Error: no such option: --bogus\\n")
    sys.exit(2)
if sim == "issues":
    sys.stdout.write("\u274c ERROR: GO:9999999 not found\\n")
    sys.exit(1)
sys.stdout.write("\u2705 Validation passed\\n")
sys.exit(0)
"""
    uv = bin_dir / "uv"
    uv.write_text(stub)
    uv.chmod(0o755)
    env = {
        **os.environ,
        "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
        "SIMULATE": simulate,
        "TERM_VALIDATE_RETRIES": "0",  # no 8s sleeps in the test
    }
    if strict:
        env["TERM_VALIDATION_STRICT"] = "1"
    else:
        env.pop("TERM_VALIDATION_STRICT", None)
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        ["bash", str(HELPER), "validate-data", "x.yaml"],
        capture_output=True, text=True, env=env, timeout=30,
    )


@pytest.mark.parametrize(
    "simulate,strict,expected",
    [
        ("outage", False, 97),   # outage, non-strict -> skip sentinel
        ("outage", True, 96),    # outage, strict -> block sentinel
        ("usage", False, 2),     # exit 2 without the banner -> passthrough, not swallowed
        ("issues", False, 1),    # genuine validation issues -> passthrough
        ("ok", False, 0),        # clean pass -> passthrough
    ],
)
def test_helper_exit_mapping(tmp_path, simulate, strict, expected):
    if shutil.which("bash") is None:
        pytest.skip("bash is not available")
    result = _run_helper(tmp_path, simulate=simulate, strict=strict)
    assert result.returncode == expected, result.stdout + result.stderr
