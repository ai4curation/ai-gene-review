"""The TreeGrafter rejection re-review's batch records must stay self-consistent.

`projects/TREEGRAFTER/rereview-2026-09-24/check_outcomes.py` encodes the audit's
three invariants (recorded action vs the live review, and both `outcome` fields
against the definitions in that folder's README). Without this test the rule held
only as long as someone remembered to run the script by hand, which is how the
field drifted into two incompatible readings in the first place.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

CHECKER = (
    Path(__file__).resolve().parents[1]
    / "projects"
    / "TREEGRAFTER"
    / "rereview-2026-09-24"
    / "check_outcomes.py"
)


def _load():
    spec = importlib.util.spec_from_file_location("tg_check_outcomes", CHECKER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.mark.skipif(not CHECKER.exists(), reason="audit folder not present")
def test_rereview_outcomes_consistent(capsys):
    """Zero violations: actions match the live reviews and both outcome fields hold."""
    module = _load()
    rc = module.main()
    out = capsys.readouterr().out
    assert rc == 0, f"check_outcomes.py reported violations:\n{out}"
    # Guard against the checker silently finding nothing to check.
    assert "checked 0 gene entries" not in out, out
    # The audit merged PSEPK/aroQ into PSEPK/aroQ-III, so one recorded
    # gene_file no longer exists. That entry must be reported and checked
    # against the surviving twin, not skipped: a quiet skip is how a row's
    # action gets "verified" against nothing while the gate still prints it
    # among the rows checked. Asserting the report rather than a count, so a
    # future audit's own merge does not have to touch this test.
    assert "merged entry:" in out, out
