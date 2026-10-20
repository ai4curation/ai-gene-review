"""Run the DISMECH_METABOLIC_ALIGNMENT page generator's guard harness.

The harness prints its own case and refusal counts, so this file deliberately states
none: a count written here would be a claim to keep in step with the harness, which is
the thing the harness exists to avoid.

It is here so the harness actually runs. It was reachable only by typing the command,
and being named `check_*` pytest did not collect it either, so a regression in any
refusal would have broken nothing.
"""
import os
import subprocess
import sys

HARNESS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "projects", "DISMECH_METABOLIC_ALIGNMENT", "check_page_guards.py")


def test_page_generator_guards_behave_as_declared():
    r = subprocess.run([sys.executable, HARNESS], capture_output=True, text=True)
    assert r.returncode == 0, (r.stdout + r.stderr)[-4000:]
    assert "every guard behaved as declared" in r.stdout
