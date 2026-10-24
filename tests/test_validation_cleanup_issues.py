"""Tests for turning validation-all warnings into low-effort cleanup issues."""

import json

import pytest
from typer.testing import CliRunner

from ai_gene_review.cli import app
from ai_gene_review.validation import cleanup_issues
from ai_gene_review.validation.validation_report import ValidationReport

PREFIX = "/home/runner/work/ai-gene-review/ai-gene-review/"


def _row(file_path, check_type, severity="warning", path="references[0]"):
    return {
        "file_path": PREFIX + file_path,
        "severity": severity,
        "validation_category": "BestPractices",
        "check_type": check_type,
        "path": path,
        "message": f"{check_type} message",
        "suggestion": "",
        "details": "",
        "timestamp": "2026-10-19T06:30:00",
    }


@pytest.fixture
def validation_tsv(tmp_path):
    rows = [
        _row("genes/human/ABCA1/ABCA1-ai-review.yaml", "folded_scalar_hyphen"),
        _row("genes/human/ABCA1/ABCA1-ai-review.yaml", "uniprot_quote_restating_field"),
        # judgement / sanctioned-legacy checks are never filed
        _row("genes/human/ABCA1/ABCA1-ai-review.yaml", "protein_binding_policy"),
        _row("genes/human/AARD/AARD-ai-review.yaml", "inconsistent_review_actions"),
        _row("genes/human/AARD/AARD-ai-review.yaml", "no_deep_research_results"),
        # errors are blocked in CI already, not low-effort cleanup
        _row("genes/human/AASDH/AASDH-ai-review.yaml", "folded_scalar_hyphen", "error"),
        _row("genes/yeast/VMA1/VMA1-ai-review.yaml", "local_source_supporting_text"),
    ]
    p = tmp_path / "validation-all.tsv"
    with p.open("w") as f:
        f.write("\t".join(ValidationReport.tsv_header()) + "\n")
        for r in rows:
            f.write("\t".join(r[h] for h in ValidationReport.tsv_header()) + "\n")
    return p


def test_collect_keeps_only_low_effort_warnings(validation_tsv):
    issues = cleanup_issues.collect_issues(validation_tsv)
    assert [i.review_file for i in issues] == [
        "genes/human/ABCA1/ABCA1-ai-review.yaml",
        "genes/yeast/VMA1/VMA1-ai-review.yaml",
    ]
    assert [w.check_type for w in issues[0].warnings] == [
        "folded_scalar_hyphen",
        "uniprot_quote_restating_field",
    ]


def test_body_names_the_file_and_validate_command(validation_tsv):
    issue = cleanup_issues.collect_issues(validation_tsv)[1]
    assert "`genes/yeast/VMA1/VMA1-ai-review.yaml`" in issue.body
    assert "just validate yeast VMA1" in issue.body
    assert "local_source_supporting_text" in issue.body


@pytest.mark.parametrize(
    "open_titles,max_new,max_open,expected",
    [
        (set(), 5, 15, ["genes/yeast/VMA1", "genes/human/ABCA1"]),
        ({"[validation-cleanup] genes/yeast/VMA1"}, 5, 15, ["genes/human/ABCA1"]),
        (set(), 1, 15, ["genes/yeast/VMA1"]),
        ({"a", "b"}, 5, 3, ["genes/yeast/VMA1"]),
        ({"a", "b", "c"}, 5, 3, []),
    ],
)
def test_select_dedups_and_caps(validation_tsv, open_titles, max_new, max_open, expected):
    issues = cleanup_issues.collect_issues(validation_tsv)
    selected = cleanup_issues.select_issues(issues, open_titles, max_new, max_open, 10)
    assert [i.gene_dir for i in selected] == expected


def test_select_skips_files_with_too_many_warnings(validation_tsv):
    issues = cleanup_issues.collect_issues(validation_tsv)
    selected = cleanup_issues.select_issues(issues, set(), 5, 15, 1)
    assert [i.gene_dir for i in selected] == ["genes/yeast/VMA1"]


def test_cli_writes_json_lines(validation_tsv, tmp_path):
    open_titles = tmp_path / "open.txt"
    open_titles.write_text("[validation-cleanup] genes/yeast/VMA1\n")
    out = tmp_path / "issues.jsonl"
    result = CliRunner().invoke(
        app,
        [
            "validation-cleanup-issues",
            str(validation_tsv),
            "-o",
            str(out),
            "--open-titles",
            str(open_titles),
        ],
    )
    assert result.exit_code == 0, result.output
    records = [json.loads(line) for line in out.read_text().splitlines()]
    assert [r["title"] for r in records] == ["[validation-cleanup] genes/human/ABCA1"]
    assert "folded_scalar_hyphen" in records[0]["body"]
