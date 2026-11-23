"""Doctests of the cutoff-check sweep runner, which lives under projects/ and so
is outside the doctest collection that runs on src/."""

import doctest
import importlib.util
from pathlib import Path

RUNNER = (
    Path(__file__).parents[1]
    / "projects/ENZYME_SPECIFICITY/cutoff-check/sweep/run_sweep.py"
)


def test_runner_doctests():
    """gene_token and the other documented helpers behave as their examples say."""
    spec = importlib.util.spec_from_file_location("run_sweep", RUNNER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = doctest.testmod(module)
    assert result.attempted > 0
    assert result.failed == 0
