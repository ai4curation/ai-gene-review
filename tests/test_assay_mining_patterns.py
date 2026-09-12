"""Regression tests for ASSAY_TO_FUNCTION paper-mining patterns."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
MINE_PAPERS_PATH = REPO_ROOT / "projects/ASSAY_TO_FUNCTION/mine_papers.py"
CATALOG_PATH = REPO_ROOT / "projects/ASSAY_TO_FUNCTION/readout_catalog.yaml"


def load_mine_papers() -> ModuleType:
    spec = importlib.util.spec_from_file_location("assay_mine_papers", MINE_PAPERS_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def paper_catalog() -> dict[str, dict[str, Any]]:
    """Load the production catalog, including its required paper screens."""
    return load_mine_papers().load_catalog(CATALOG_PATH)


def test_production_catalog_has_all_required_paper_screens(
    paper_catalog: dict[str, dict[str, Any]],
) -> None:
    assert all(
        not spec.get("patterns") or spec.get("_screen")
        for spec in paper_catalog.values()
    )


@pytest.mark.parametrize(
    "sample",
    [
        "Morris Water Maze",
        "MWM",
        "open-field test",
        "open field arena",
        "openfield assay",
        "rota-rod",
        "rotarod",
        "forced swim",
        "tail suspension",
        "elevated plus-maze",
        "fear conditioning",
        "novel object recognition",
        "Barnes maze",
        "Y-maze",
        "Ymaze",
        "light/dark box",
        "startle response",
        "acoustic startle reflex",
        "beam-walk",
        "grip strength",
    ],
)
def test_behavioral_assay_patterns_survive_paper_screen(
    paper_catalog: dict[str, dict[str, Any]], sample: str
) -> None:
    behavioral = paper_catalog["BEHAVIORAL_ASSAY"]
    compiled = behavioral["_compiled"]
    screen = behavioral["_screen"]

    assert compiled.search(sample)
    assert any(token in sample.lower() for token in screen)
