"""The ``forbid_working_tree_genes`` guard must catch every way of listing ``genes/``."""

import os
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    "consult",
    [
        lambda: list(REPO_ROOT.glob("genes/human/*")),
        lambda: list((REPO_ROOT / "genes" / "human").rglob("*.yaml")),
        lambda: list(os.scandir(REPO_ROOT / "genes")),
        lambda: os.listdir(REPO_ROOT / "genes"),
        lambda: (REPO_ROOT / "genes" / "human").is_file(),
    ],
    ids=["root-glob", "rglob", "scandir", "listdir", "is_file"],
)
def test_guard_rejects_working_tree_gene_listing(
    consult, forbid_working_tree_genes: None
) -> None:
    with pytest.raises(AssertionError, match="working-tree gene file consulted"):
        consult()


def test_guard_allows_paths_outside_genes(forbid_working_tree_genes: None) -> None:
    assert (REPO_ROOT / "pyproject.toml").is_file()
    assert "pyproject.toml" in os.listdir(REPO_ROOT)
