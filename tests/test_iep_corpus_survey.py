"""Regression checks for complete IEP disposition reporting."""

import importlib.util
from collections import Counter
from pathlib import Path

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "projects/IEP/iep_corpus_survey.py"
SPEC = importlib.util.spec_from_file_location("iep_corpus_survey", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
survey = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(survey)


@pytest.mark.parametrize("extra_action", ["NEW", "FUTURE_ACTION"])
def test_disposition_columns_account_for_every_counted_row(extra_action):
    """An action omitted from the usual column list must never hide rows."""
    counts = Counter({"ACCEPT": 4, "REMOVE": 2, "UNREVIEWED": 1, extra_action: 3})
    lines = survey.render_disposition_table({"IEP": counts})
    headings = [cell.strip() for cell in lines[0].strip("|").split("|")]
    cells = [cell.strip() for cell in lines[2].strip("|").split("|")]
    row = dict(zip(headings, cells))

    assert row[extra_action] == "3"
    assert row["Reviewed"] == "10"
    assert sum(int(count) for count in cells[2:-1]) == 10
    assert row["% negative"] == "**20.0%**"


def test_committed_disposition_report_reconciles():
    """The published snapshot must account for all rows, across every code."""
    report = SCRIPT.with_name("iep-corpus-survey.md").read_text()
    table = report.split("### Disposition by evidence code\n", 1)[1]
    table = table.strip().split("\n\n", 1)[0]
    rows = table.splitlines()[2:]
    assert rows
    for line in rows:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        total = int(cells[1].replace(",", ""))
        assert sum(int(count) for count in cells[2:-1]) == total, cells[0]
