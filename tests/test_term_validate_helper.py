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
RUN_TERM_VALIDATOR = ROOT / "scripts" / "run_term_validator.sh"


def test_ltv_service_unavailable_exit_code_is_2():
    """The wrapper keys the outage on exit code 2; lock that against drift."""
    from linkml_term_validator.cli import EXIT_SERVICE_UNAVAILABLE

    assert EXIT_SERVICE_UNAVAILABLE == 2


def _run_helper(tmp_path, *, simulate, strict=False, extra_env=None, script=None):
    """Run the helper (or another wrapper) with a stub `uv` faking LTV."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir(exist_ok=True)  # may be called more than once per tmp_path
    # The helper invokes `uv run linkml-term-validator ...`; the stub decides the
    # faked outcome from SIMULATE without touching the network.
    stub = f"""#!{sys.executable}
import os, sys
# `linkml-term-validator validate-data --help` (run_term_validator.sh probes for
# --strict) must not touch the network, so it succeeds regardless of SIMULATE.
if "--help" in sys.argv:
    sys.stdout.write("usage: linkml-term-validator validate-data [OPTIONS]\\n")
    sys.exit(0)
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
    # GITHUB_STEP_SUMMARY is set on every Actions step and inherited here; the
    # stubbed-outage cases would otherwise append "term validation skipped" lines
    # to the real `test` job's run summary on every (green) PR. Scrub it so the
    # tests never write to the actual summary.
    env.pop("GITHUB_STEP_SUMMARY", None)
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        ["bash", str(script or HELPER), "validate-data", "x.yaml",
         "-s", "schema.yaml", "-t", "GeneReview", "--labels", "-c", "oak.yaml"],
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


def test_run_term_validator_outage_is_visible_and_nonblocking(tmp_path):
    """On an outage the wrapper must exit 0 AND emit a WARN line on stdout.

    `ai-gene-review validate --terms` runs run_term_validator.sh under
    subprocess.run(capture_output=True), so a stderr-only ::warning:: is
    swallowed and the skip would be a silent green. The stdout WARN line is what
    cli.py's _warning_lines matches, turning the skip into a visible, advisory
    (non-blocking) validation warning.
    """
    if shutil.which("bash") is None:
        pytest.skip("bash is not available")
    result = _run_helper(tmp_path, simulate="outage", strict=False,
                         script=RUN_TERM_VALIDATOR)
    assert result.returncode == 0, result.stdout + result.stderr
    # cli.py:_warning_lines matches a line with "WARN" or "⚠" on stdout.
    assert any(("WARN" in line) or ("⚠" in line)
               for line in result.stdout.splitlines()), result.stdout
    # Must not look like the blocking NCBITaxon label-mismatch warning.
    assert "Label mismatch for" not in result.stdout, result.stdout


def test_run_term_validator_strict_outage_blocks(tmp_path):
    """Under TERM_VALIDATION_STRICT (weekly pass) an outage must block."""
    if shutil.which("bash") is None:
        pytest.skip("bash is not available")
    result = _run_helper(tmp_path, simulate="outage", strict=True,
                         script=RUN_TERM_VALIDATOR)
    assert result.returncode != 0, result.stdout + result.stderr


def test_step_summary_written_only_on_outage(tmp_path):
    """The outage line lands on $GITHUB_STEP_SUMMARY; a clean run writes nothing."""
    if shutil.which("bash") is None:
        pytest.skip("bash is not available")
    outage_summary = tmp_path / "outage.md"
    outage_summary.write_text("")
    r = _run_helper(tmp_path, simulate="outage", strict=False,
                    extra_env={"GITHUB_STEP_SUMMARY": str(outage_summary)})
    assert r.returncode == 97, r.stdout + r.stderr
    assert "Ontology service unavailable" in outage_summary.read_text()

    clean_summary = tmp_path / "clean.md"
    clean_summary.write_text("")
    r = _run_helper(tmp_path, simulate="ok", strict=False,
                    extra_env={"GITHUB_STEP_SUMMARY": str(clean_summary)})
    assert r.returncode == 0, r.stdout + r.stderr
    assert clean_summary.read_text() == ""
