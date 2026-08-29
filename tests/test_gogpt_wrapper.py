"""Regression tests for the repository GO-GPT just wrappers."""

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_JUSTFILE = REPO_ROOT / "project.justfile"


def test_gogpt_wrappers_expose_repository_package_to_bioreason_python() -> None:
    """Every external BioReason Python call must be able to import ai_gene_review."""
    command_lines = [
        line.strip()
        for line in PROJECT_JUSTFILE.read_text().splitlines()
        if "scripts/gogpt_predict.py" in line and not line.lstrip().startswith("#")
    ]

    assert len(command_lines) == 5
    assert all(line.startswith("PYTHONPATH=src ") for line in command_lines)
