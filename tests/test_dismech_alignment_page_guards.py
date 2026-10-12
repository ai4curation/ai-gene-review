"""Run the DISMECH_METABOLIC_ALIGNMENT page generator's guard harness.

The harness exists so that "eighteen of twenty-one cases must refuse" is a command rather
than a claim in a history record. That only holds if something runs it: it was reachable
only by typing the command, and it is named `check_*`, so pytest did not collect it either
and a regression in any of the eighteen refusals would have broken nothing.
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
