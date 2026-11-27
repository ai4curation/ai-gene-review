"""Tests for the ProtNLM2 re-review manifest refresher."""

import importlib.util
from pathlib import Path
from types import ModuleType

import pytest
import yaml
from typer.testing import CliRunner

SCRIPT = Path(__file__).resolve().parents[1] / "projects/PROTNLM_EVALUATION/rereview/refresh_manifest.py"


@pytest.fixture(scope="module")
def module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("refresh_manifest", SCRIPT)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def write_review(repo: Path, species: str, folder: str, body: str) -> None:
    d = repo / "genes" / species / folder
    d.mkdir(parents=True)
    (d / f"{folder}-ai-review.yaml").write_text(body)


@pytest.mark.parametrize(
    "body,expected",
    [
        ("id: P1\ndescription: A kinase.\n", "complete"),
        ("id: P1\ndescription: 'TODO: Add description for X'\n", "stub_or_pending"),
        ("id: P1\ndescription: A kinase.\nexisting_annotations:\n- review:\n    action: PENDING\n", "stub_or_pending"),
    ],
)
def test_cli_refreshes_status(module: ModuleType, tmp_path: Path, body: str, expected: str) -> None:
    write_review(tmp_path, "human", "GENE1", body)
    manifest = tmp_path / "manifest.yaml"
    manifest.write_text(
        yaml.safe_dump(
            {
                "description": "test",
                "genes": [
                    {"accession": "P1", "species": "human", "review": None, "review_status": "missing"},
                    {"accession": "Q9", "species": "human", "review": "stale/path.yaml", "review_status": "complete"},
                ],
            },
            sort_keys=False,
        )
    )
    result = CliRunner().invoke(module.app, ["--manifest-path", str(manifest), "--repo", str(tmp_path)])
    assert result.exit_code == 0, result.output
    data = yaml.safe_load(manifest.read_text())
    assert "generated_at" in data
    first, second = data["genes"]
    assert first["review"] == "genes/human/GENE1/GENE1-ai-review.yaml"
    assert first["review_status"] == expected
    assert second["review"] is None and second["review_status"] == "missing"


def test_committed_manifest_matches_repository(module: ModuleType) -> None:
    """Every row marked complete points at a review file that is complete now."""
    data = yaml.safe_load((SCRIPT.parent / "manifest.yaml").read_text())
    repo = SCRIPT.parents[3]
    for gene in data["genes"]:
        if gene["review_status"] == "complete":
            path = repo / gene["review"]
            assert path.exists(), gene["review"]
            assert module.review_status(path.read_text()) == "complete", gene["review"]
