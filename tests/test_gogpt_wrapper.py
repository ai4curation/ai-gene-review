"""Regression tests for the repository GO-GPT just wrappers."""

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_JUSTFILE = REPO_ROOT / "project.justfile"


def test_gogpt_wrappers_expose_repository_package_to_bioreason_python() -> None:
    """Every external BioReason Python call must be able to import ai_gene_review."""
    command_lines = [
        line.strip()
        for line in PROJECT_JUSTFILE.read_text().splitlines()
        if "BioReason-Pro" in line
        and "scripts/gogpt_predict.py" in line
        and not line.lstrip().startswith("#")
    ]

    assert command_lines, "expected at least one external BioReason GO-GPT invocation"
    missing = [
        line
        for line in command_lines
        if not line.startswith("PYTHONPATH=src${PYTHONPATH:+:$PYTHONPATH} ")
    ]
    assert not missing, f"BioReason invocations without repository PYTHONPATH: {missing}"
