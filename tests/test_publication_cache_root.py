"""Publication availability must not depend on the review's directory."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.status_manager import compute_status_from_file
from ai_gene_review.validation import validate_gene_review
from ai_gene_review.validation import validator


def _write_cache(directory: Path, available: bool) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "PMID_987654321.md").write_text(
        "---\npmid: '987654321'\ntitle: Test DNA binding\n"
        f"full_text_available: {str(available).lower()}\n---\n"
    )


def _write_review(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump({
        "id": "Q12345",
        "gene_symbol": "TEST",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "A protein with experimentally measured DNA binding.",
        "references": [{"id": "PMID:987654321", "title": "Test DNA binding"}],
        "core_functions": [{
            "description": "Binds DNA.",
            "molecular_function": {"id": "GO:0003677", "label": "DNA binding"},
        }],
        "existing_annotations": [{
            "term": {"id": "GO:0003677", "label": "DNA binding"},
            "evidence_type": "IDA",
            "original_reference_id": "PMID:987654321",
            "review": {"action": "ACCEPT", "summary": "Observed DNA binding."},
        }],
    }))
    path.with_name("TEST-goa.tsv").write_text(
        "GENE PRODUCT DB\tGENE PRODUCT ID\tSYMBOL\tQUALIFIER\tGO TERM\tGO NAME\t"
        "GO ASPECT\tECO ID\tGO EVIDENCE CODE\tREFERENCE\tWITH/FROM\tTAXON ID\n"
        "UniProtKB\tQ12345\tTEST\tenables\tGO:0003677\tDNA binding\t"
        "molecular_function\tECO:0000314\tIDA\tPMID:987654321\t\t9606\n"
    )


def _missing_support(report):
    return [issue for issue in report.issues if "lacks supported_by" in issue.message]


def test_nested_cache_cannot_change_canonical_vs_staged_status(tmp_path, monkeypatch):
    """A conflicting nested cache must not hide the real full-text record."""
    root = tmp_path / "repo"
    _write_cache(root / "publications", True)
    _write_cache(root / "genes/human/publications", False)
    monkeypatch.setattr(validator, "get_project_root", lambda: root)
    canonical = root / "genes/human/TEST/TEST-ai-review.yaml"
    staged = root / "tmp/proposal/TEST-ai-review.yaml"
    reports = []
    for path in (canonical, staged):
        _write_review(path)
        status, report = compute_status_from_file(path)
        assert report.is_valid
        assert len(_missing_support(report)) == 1
        assert status == "DRAFT"
        reports.append(report)
    assert reports[0].issues == reports[1].issues


@pytest.mark.parametrize("available", [True, False])
@pytest.mark.parametrize("check_goa", [True, False])
def test_explicit_fixture_cache_overrides_repository_cache(
    tmp_path, monkeypatch, available, check_goa
):
    """Explicit fixture roots work in both GOA and data-only validation paths."""
    root = tmp_path / "repo"
    _write_cache(root / "publications", not available)
    fixture_cache = tmp_path / "fixture-cache"
    _write_cache(fixture_cache, available)
    monkeypatch.setattr(validator, "get_project_root", lambda: root)
    path = root / "genes/human/TEST/TEST-ai-review.yaml"
    _write_review(path)
    report = validate_gene_review(
        path, check_goa=check_goa, check_supporting_text=False,
        publications_dir=fixture_cache,
    )
    assert len(_missing_support(report)) == int(available)


@pytest.mark.parametrize("check_goa", [True, False])
def test_default_cache_does_not_follow_working_directory(tmp_path, monkeypatch, check_goa):
    """Disabling GOA or changing cwd must not select unrelated source bytes."""
    root = tmp_path / "repo"
    _write_cache(root / "publications", True)
    elsewhere = tmp_path / "elsewhere"
    _write_cache(elsewhere / "publications", False)
    monkeypatch.setattr(validator, "get_project_root", lambda: root)
    monkeypatch.chdir(elsewhere)
    path = root / "genes/human/TEST/TEST-ai-review.yaml"
    _write_review(path)
    report = validate_gene_review(path, check_goa=check_goa, check_supporting_text=False)
    assert len(_missing_support(report)) == 1


@pytest.mark.parametrize("check_goa", [True, False])
@pytest.mark.parametrize("metadata,available", [
    ("content_type: full_text_xml", True),
    ("content_type: full_text_html", True),
    ("content_type: full_text_pdf", True),
    ("content_type: url", True),
    ("content_type: abstract_only", False),
    ("content_type: unavailable", False),
    ("full_text_available: false\ncontent_type: full_text_xml", False),
    ("full_text_available: true\ncontent_type: abstract_only", True),
    ("content_type: null", False),
    ("- not a mapping", False),
    ("", False),
])
def test_missing_support_uses_shared_cache_availability(
    tmp_path, metadata, available, check_goa
):
    """The warning must follow the same availability metadata as quote checks."""
    cache = tmp_path / "cache"
    cache.mkdir()
    (cache / "PMID_987654321.md").write_text(f"---\n{metadata}\n---\n")
    path = tmp_path / "TEST/TEST-ai-review.yaml"
    _write_review(path)
    report = validate_gene_review(
        path, check_goa=check_goa, check_supporting_text=False,
        publications_dir=cache,
    )
    assert len(_missing_support(report)) == int(available)


def test_unterminated_cache_metadata_does_not_claim_full_text(tmp_path):
    """A missing front-matter delimiter supplies no availability assertion."""
    cache = tmp_path / "cache"
    cache.mkdir()
    (cache / "PMID_987654321.md").write_text("---\ncontent_type: full_text_xml\n")
    path = tmp_path / "TEST/TEST-ai-review.yaml"
    _write_review(path)
    report = validate_gene_review(
        path, check_goa=False, check_supporting_text=False,
        publications_dir=cache,
    )
    assert not _missing_support(report)
