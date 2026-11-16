"""Tests for the offline ontology-cache coverage report (ai4curation/ai-gene-review#5731).

These run the real linkml-term-validator with ``--offline``, so they need no
network: ``NCBITaxon:9606`` is in the committed cache, and ``NCBITaxon:9999999999``
is not a real taxon, so it can never be cached.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.tools.ontology_cache_coverage import (
    expand_inputs,
    main,
    measure_coverage,
)

CACHED = ("NCBITaxon:9606", "Homo sapiens")
UNCACHED = ("NCBITaxon:9999999999", "Not a real taxon")


def write_prediction_review(path: Path, taxon: tuple[str, str]) -> Path:
    """Write a minimal PredictionReview whose only term is its taxon."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(
            {
                "id": "P00001",
                "gene_symbol": "TEST1",
                "taxon": {"id": taxon[0], "label": taxon[1]},
            }
        ),
        encoding="utf-8",
    )
    return path


def test_cached_terms_are_covered(tmp_path: Path) -> None:
    review = write_prediction_review(
        tmp_path / "covered-predictions-review.yaml", CACHED
    )

    report = measure_coverage(expand_inputs([review]), warm=False)

    assert report.files_checked == 1
    assert report.covered
    assert report.other_findings == []


def test_uncached_term_is_reported_against_its_file(tmp_path: Path) -> None:
    covered = write_prediction_review(tmp_path / "a-predictions-review.yaml", CACHED)
    missing = write_prediction_review(tmp_path / "b-predictions-review.yaml", UNCACHED)

    report = measure_coverage(expand_inputs([tmp_path]), warm=False).to_dict()

    assert report["files_checked"] == 2
    assert report["covered"] is False
    labels = report["missing_labels"]
    assert [entry["curie"] for entry in labels] == [UNCACHED[0]]
    assert labels[0]["files"] == [missing.resolve().as_posix()]
    assert covered.resolve().as_posix() not in labels[0]["files"]
    assert {entry["enum"] for entry in report["missing_enum_memberships"]} == {
        "NCBITaxonEnum"
    }


def test_wrong_label_is_a_finding_not_a_cache_miss(tmp_path: Path) -> None:
    review = write_prediction_review(
        tmp_path / "wrong-label-predictions-review.yaml",
        (CACHED[0], "Mus musculus"),
    )

    report = measure_coverage(expand_inputs([review]), warm=False)

    assert report.covered
    [(path, severity, message)] = report.other_findings
    assert path == review.resolve().as_posix()
    assert severity == "WARN"
    assert "Label mismatch" in message


@pytest.mark.parametrize(
    ("taxon", "expected_exit"),
    [(CACHED, 0), (UNCACHED, 1)],
)
def test_check_exit_code(
    tmp_path: Path, taxon: tuple[str, str], expected_exit: int
) -> None:
    review = write_prediction_review(tmp_path / "x-predictions-review.yaml", taxon)
    report_path = tmp_path / "report.yaml"

    assert main([str(review), "--check", "-o", str(report_path)]) == expected_exit
    assert yaml.safe_load(report_path.read_text())["files_checked"] == 1


def test_unrecognised_files_are_skipped(tmp_path: Path) -> None:
    (tmp_path / "notes.yaml").write_text("a: 1\n", encoding="utf-8")

    assert expand_inputs([tmp_path]) == {}
    assert main([str(tmp_path), "--check"]) == 0
