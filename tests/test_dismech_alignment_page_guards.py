"""Run the DISMECH_METABOLIC_ALIGNMENT page generator's guard harness.

The harness exists so that its counts are a command rather than a claim in a history
record, and it prints them itself - so this file deliberately states none. An earlier
version of this docstring hardcoded "eighteen of twenty-one cases must refuse", in the
round that added the 22nd case, which made the one file whose purpose is "this count is
not a claim" state the claim, wrongly.

It is here because nothing ran the harness: it was reachable only by typing the command,
and being named `check_*` pytest did not collect it either, so a regression in any refusal
would have broken nothing.
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
