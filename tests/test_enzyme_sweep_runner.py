"""Doctests of the Enzyme Specificity analysis scripts, which live under projects/ and
so are outside the doctest collection that runs on src/."""

import doctest
import importlib.util
from pathlib import Path

import pytest

PROJECT = Path(__file__).parents[1] / "projects/ENZYME_SPECIFICITY"
SCRIPTS = [
    PROJECT / "cutoff-check/sweep/run_sweep.py",
    PROJECT / "ncbifam-metadata/check_release_table.py",
    PROJECT / "ncbifam-metadata/render_feedback.py",
]


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda p: p.name)
def test_script_doctests(script: Path):
    """Each script's documented helpers behave as their examples say."""
    spec = importlib.util.spec_from_file_location(script.stem, script)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = doctest.testmod(module)
    assert result.attempted > 0
    assert result.failed == 0
