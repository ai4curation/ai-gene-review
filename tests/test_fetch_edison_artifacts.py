"""Tests for Edison artifact frontmatter helpers."""

import base64
from pathlib import Path

import yaml

from scripts import fetch_edison_artifacts as artifacts


def test_normalize_artifacts_deduplicates_filenames() -> None:
    encoded = base64.b64encode(b"hello").decode()

    records = artifacts.normalize_artifacts(
        [
            {"filename": "../evidence table.png", "content_base64": encoded},
            {"filename": "evidence table.png", "content_base64": encoded},
        ]
    )

    assert [record.filename for record in records] == [
        "evidence_table.png",
        "evidence_table_2.png",
    ]


def test_update_research_text_adds_frontmatter_and_artifacts_before_citations() -> None:
    record = artifacts.ArtifactRecord(
        filename="evidence.png",
        content_base64=base64.b64encode(b"image").decode(),
        media_type="image/png",
        description="Evidence matrix",
        path="REPORT_artifacts/evidence.png",
    )

    updated = artifacts.update_research_text(
        "---\nprovider: falcon\n---\n# Report\n\n## Citations\nold citations\n",
        "trajectory-1",
        [record],
    )
    metadata_text = updated.split("---", 2)[1]
    metadata = yaml.safe_load(metadata_text)

    assert metadata["trajectory_id"] == "trajectory-1"
    assert metadata["artifact_count"] == 1
    assert metadata["artifacts"][0]["path"] == "REPORT_artifacts/evidence.png"
    assert "## Artifacts" in updated
    assert updated.index("## Artifacts") < updated.index("## Citations")


def test_write_artifacts_refuses_conflicting_overwrite(tmp_path: Path) -> None:
    report = tmp_path / "REPORT.md"
    report.write_text("# Report\n", encoding="utf-8")
    artifact_dir = tmp_path / "REPORT_artifacts"
    artifact_dir.mkdir()
    destination = artifact_dir / "evidence.txt"
    destination.write_text("existing", encoding="utf-8")
    record = artifacts.ArtifactRecord(
        filename="evidence.txt",
        content_base64=base64.b64encode(b"different").decode(),
    )

    try:
        artifacts.write_artifacts([record], report)
    except FileExistsError as exc:
        assert "Refusing to overwrite" in str(exc)
    else:
        raise AssertionError("expected conflicting artifact overwrite to fail")
