"""Tests for the nicotine biosynthesis project launcher."""

import csv
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "projects"
    / "NICOTINE_BIOSYNTHESIS"
    / "launch_review_jobs.py"
)


def load_launcher_module():
    """Load the nicotine project launcher from its project-sidecar path."""
    spec = spec_from_file_location("nicotine_project_launcher", MODULE_PATH)
    module = module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


launcher = load_launcher_module()


def write_jobs_csv(tmp_path: Path, rows: list[dict[str, str]]) -> Path:
    """Create a minimal review_jobs.csv fixture in a temporary workspace."""
    jobs_file = tmp_path / "projects" / "NICOTINE_BIOSYNTHESIS" / "review_jobs.csv"
    jobs_file.parent.mkdir(parents=True, exist_ok=True)

    with jobs_file.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "job_id",
                "canonical_symbol",
                "fetch_id",
                "alias",
                "species",
                "status",
                "notes",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    return jobs_file


def make_existing_review(tmp_path: Path, alias: str, species: str = "NICAT") -> None:
    """Create a seeded review file matching a queued alias."""
    review_file = tmp_path / "genes" / species / alias / f"{alias}-ai-review.yaml"
    review_file.parent.mkdir(parents=True, exist_ok=True)
    review_file.write_text("status: INITIALIZED\n", encoding="utf-8")


def test_collect_matching_jobs_skips_existing_by_default(tmp_path):
    """Already-launched aliases are not selected unless explicitly requested."""
    jobs = [
        {
            "job_id": "existing_job",
            "canonical_symbol": "NaPMT1.1",
            "fetch_id": "Q93XQ5",
            "alias": "NaPMT1.1",
            "species": "NICAT",
            "status": "launch_ready",
            "notes": "Existing seeded review",
        },
        {
            "job_id": "new_job",
            "canonical_symbol": "NaAO2",
            "fetch_id": "A0A1J6KBX2",
            "alias": "NaAO2_candidate_AO_0",
            "species": "NICAT",
            "status": "launch_ready",
            "notes": "New candidate",
        },
        {
            "job_id": "pending_job",
            "canonical_symbol": "NaMPO1",
            "fetch_id": "",
            "alias": "NaMPO1",
            "species": "NICAT",
            "status": "launch_ready",
            "notes": "Pending accession",
        },
    ]
    make_existing_review(tmp_path, alias="NaPMT1.1")

    selected, existing, unresolved = launcher.collect_matching_jobs(
        jobs=jobs,
        status="launch_ready",
        workspace_root=tmp_path,
    )

    assert [job["job_id"] for job in selected] == ["new_job"]
    assert [job["job_id"] for job in existing] == ["existing_job"]
    assert [job["job_id"] for job in unresolved] == ["pending_job"]


def test_collect_matching_jobs_can_include_existing(tmp_path):
    """Existing aliases stay in queue order when reruns are enabled."""
    jobs = [
        {
            "job_id": "existing_job",
            "canonical_symbol": "NaPMT1.1",
            "fetch_id": "Q93XQ5",
            "alias": "NaPMT1.1",
            "species": "NICAT",
            "status": "launch_ready",
            "notes": "Existing seeded review",
        },
        {
            "job_id": "new_job",
            "canonical_symbol": "NaAO2",
            "fetch_id": "A0A1J6KBX2",
            "alias": "NaAO2_candidate_AO_0",
            "species": "NICAT",
            "status": "launch_ready",
            "notes": "New candidate",
        },
    ]
    make_existing_review(tmp_path, alias="NaPMT1.1")

    selected, existing, unresolved = launcher.collect_matching_jobs(
        jobs=jobs,
        status="launch_ready",
        workspace_root=tmp_path,
        include_existing=True,
    )

    assert [job["job_id"] for job in selected] == ["existing_job", "new_job"]
    assert [job["job_id"] for job in existing] == ["existing_job"]
    assert unresolved == []


def test_run_command_uses_workspace_root(tmp_path):
    """Commands execute relative to the provided workspace root."""
    with patch.object(launcher.subprocess, "run") as mock_run:
        launcher.run_command(["just", "fetch-gene", "NICAT", "Q93XQ5"], False, tmp_path)

    mock_run.assert_called_once_with(
        ["just", "fetch-gene", "NICAT", "Q93XQ5"],
        check=True,
        cwd=tmp_path,
    )


def test_main_reports_existing_aliases_by_default(tmp_path, capsys):
    """The CLI reports when all launch-ready jobs have already been seeded."""
    write_jobs_csv(
        tmp_path,
        rows=[
            {
                "job_id": "existing_job",
                "canonical_symbol": "NaPMT1.1",
                "fetch_id": "Q93XQ5",
                "alias": "NaPMT1.1",
                "species": "NICAT",
                "status": "launch_ready",
                "notes": "Existing seeded review",
            },
            {
                "job_id": "pending_job",
                "canonical_symbol": "NaMPO1",
                "fetch_id": "",
                "alias": "NaMPO1",
                "species": "NICAT",
                "status": "launch_ready",
                "notes": "Pending accession",
            },
        ],
    )
    make_existing_review(tmp_path, alias="NaPMT1.1")

    argv = [
        "launch_review_jobs.py",
        "--workspace-root",
        str(tmp_path),
        "--jobs-file",
        "projects/NICOTINE_BIOSYNTHESIS/review_jobs.csv",
        "--dry-run",
    ]
    with patch.object(sys, "argv", argv):
        launcher.main()

    out = capsys.readouterr().out
    assert "already launched aliases: 1" in out
    assert "selected for execution: 0" in out
    assert "No jobs selected for execution." in out
    assert "Use --include-existing" in out
    assert "- pending_job: NaMPO1 (Pending accession)" in out


def test_main_include_existing_emits_commands(tmp_path, capsys):
    """The CLI can explicitly rerun already-seeded aliases in dry-run mode."""
    write_jobs_csv(
        tmp_path,
        rows=[
            {
                "job_id": "existing_job",
                "canonical_symbol": "NaPMT1.1",
                "fetch_id": "Q93XQ5",
                "alias": "NaPMT1.1",
                "species": "NICAT",
                "status": "launch_ready",
                "notes": "Existing seeded review",
            }
        ],
    )
    make_existing_review(tmp_path, alias="NaPMT1.1")

    argv = [
        "launch_review_jobs.py",
        "--workspace-root",
        str(tmp_path),
        "--jobs-file",
        "projects/NICOTINE_BIOSYNTHESIS/review_jobs.csv",
        "--include-existing",
        "--with-deep-research",
        "--dry-run",
    ]
    with patch.object(sys, "argv", argv):
        launcher.main()

    out = capsys.readouterr().out
    assert "[1/1] existing_job -> NaPMT1.1" in out
    assert "$ just fetch-gene NICAT Q93XQ5 --alias NaPMT1.1" in out
    assert "$ just deep-research-codex NICAT Q93XQ5 --alias NaPMT1.1" in out
