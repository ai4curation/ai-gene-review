"""Tests for PMC failure candidate logging."""

import tempfile
from pathlib import Path

import pytest

from ai_gene_review.etl.publication_refresh import log_pmc_failure, load_pmc_candidates


def test_log_pmc_failure_creates_entry():
    """Should append a TSV line to the candidates file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        candidates_file = Path(tmpdir) / "pmc_override_candidates.tsv"
        candidates_file.write_text("# PMC Override Candidates\n# PMID\tPMCID\tfailure_reason\tdate_logged\n")

        log_pmc_failure("12345", "PMC999999", "html_too_short", candidates_file)

        content = candidates_file.read_text()
        assert "12345\tPMC999999\thtml_too_short\t" in content


def test_log_pmc_failure_does_not_duplicate():
    """Should not log the same PMID twice."""
    with tempfile.TemporaryDirectory() as tmpdir:
        candidates_file = Path(tmpdir) / "pmc_override_candidates.tsv"
        candidates_file.write_text("# header\n")

        log_pmc_failure("12345", "PMC999999", "failed", candidates_file)
        log_pmc_failure("12345", "PMC999999", "failed_again", candidates_file)

        content = candidates_file.read_text()
        assert content.count("12345\t") == 1


def test_load_pmc_candidates():
    """Should load candidates from the TSV file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        candidates_file = Path(tmpdir) / "pmc_override_candidates.tsv"
        candidates_file.write_text(
            "# header\n"
            "12345\tPMC999999\thtml_too_short\t2026-04-24\n"
            "67890\tPMC888888\tfetch_error\t2026-04-24\n"
        )

        candidates = load_pmc_candidates(candidates_file)

        assert len(candidates) == 2
        assert candidates["12345"]["pmcid"] == "PMC999999"
        assert candidates["67890"]["reason"] == "fetch_error"
