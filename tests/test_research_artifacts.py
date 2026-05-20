"""Tests for Edison artifact ingestion helpers."""

from __future__ import annotations

import base64
import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script_module(name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


fetch_artifacts = load_script_module(
    "fetch_edison_artifacts_script",
    "scripts/fetch_edison_artifacts.py",
)
index_artifacts = load_script_module(
    "index_research_artifacts_script",
    "scripts/index_research_artifacts.py",
)


def test_update_research_text_adds_artifact_metadata_and_section():
    record = fetch_artifacts.ArtifactRecord(
        filename="plot.png",
        content_base64=base64.b64encode(b"plot-bytes").decode("ascii"),
        media_type="image/png",
        description="Summary plot",
        path="GENE-deep-research-falcon_artifacts/plot.png",
    )
    text = """---
provider: falcon
---

## Output

# Report

Body.

## Citations
"""

    updated = fetch_artifacts.update_research_text(text, "trajectory-1", [record])
    metadata, body = fetch_artifacts.split_frontmatter(updated)

    assert metadata["trajectory_id"] == "trajectory-1"
    assert metadata["artifact_count"] == 1
    assert (
        metadata["artifacts"][0]["path"]
        == "GENE-deep-research-falcon_artifacts/plot.png"
    )
    assert "## Artifacts" in body
    assert "![Summary plot](GENE-deep-research-falcon_artifacts/plot.png)" in body
    assert body.index("## Artifacts") < body.index("## Citations")


def test_write_artifacts_refuses_different_existing_content(tmp_path):
    report_file = tmp_path / "GENE-deep-research-falcon.md"
    report_file.write_text("# Report\n", encoding="utf-8")
    artifact_dir = fetch_artifacts.artifact_directory_for_report(report_file)
    artifact_dir.mkdir()
    (artifact_dir / "plot.png").write_bytes(b"old")
    record = fetch_artifacts.ArtifactRecord(
        filename="plot.png",
        content_base64=base64.b64encode(b"new").decode("ascii"),
    )

    try:
        fetch_artifacts.write_artifacts([record], report_file)
    except FileExistsError as e:
        assert "Refusing to overwrite" in str(e)
    else:
        raise AssertionError("Expected FileExistsError")


def test_build_index_collects_gene_context_and_detects_collisions(tmp_path):
    root = tmp_path / "genes"
    gene_dir = root / "human" / "GENE"
    gene_dir.mkdir(parents=True)
    for provider, trajectory in [("falcon", "tid-1"), ("openai", "tid-2")]:
        (gene_dir / f"GENE-deep-research-{provider}.md").write_text(
            f"""---
provider: {provider}
model: test-model
trajectory_id: {trajectory}
artifact_count: 1
artifacts:
  - filename: plot.png
    path: shared/plot.png
    media_type: image/png
---

# Report
""",
            encoding="utf-8",
        )
    (gene_dir / "GENE-deep-research-falcon-citations.md").write_text(
        "# Citations\n",
        encoding="utf-8",
    )

    index = index_artifacts.build_index(root)

    assert index["report_count"] == 2
    assert index["reports_with_artifacts_count"] == 2
    assert index["artifact_total"] == 2
    assert index["collision_count"] == 1
    assert index["collisions"][0]["path"] == "human/GENE/shared/plot.png"
    assert index["reports"][0]["organism"] == "human"
    assert index["reports"][0]["gene"] == "GENE"
    assert index["index_by_trajectory_id"]["tid-1"]["artifact_paths"] == [
        "human/GENE/shared/plot.png"
    ]


def test_build_index_handles_repeated_trajectory_ids(tmp_path):
    root = tmp_path / "genes"
    gene_dir = root / "human" / "GENE"
    gene_dir.mkdir(parents=True)
    for provider in ["falcon", "openai", "cyberian"]:
        (gene_dir / f"GENE-deep-research-{provider}.md").write_text(
            f"""---
provider: {provider}
trajectory_id: same-tid
---

# Report
""",
            encoding="utf-8",
        )

    index = index_artifacts.build_index(root)

    trajectory_entry = index["index_by_trajectory_id"]["same-tid"]
    assert trajectory_entry["_collision"] is True
    assert trajectory_entry["reports"] == [
        "human/GENE/GENE-deep-research-cyberian.md",
        "human/GENE/GENE-deep-research-falcon.md",
        "human/GENE/GENE-deep-research-openai.md",
    ]
