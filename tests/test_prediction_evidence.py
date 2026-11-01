"""Prediction sidecar evidence checks use actual source files, without network."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.prediction_evidence import local_quote_matches, validate_prediction_evidence


def write_case(root: Path) -> Path:
    """Write an isolated sidecar and its local evidence source."""
    (root / "genes").mkdir()
    (root / "genes/source.txt").write_text("DOMAIN  40..259\nBinding domain.\n")
    path = root / "review.yaml"
    path.write_text(yaml.safe_dump({
        "source_documents": ["genes/source.txt"],
        "references": [{"id": "file:source.txt", "title": "Source"}],
        "predictions": [{"review": {
            "assessment": "UNC", "confidence_score": 1,
            "supported_by": [{"reference_id": "file:source.txt",
                              "supporting_text": "DOMAIN 40..259 ... Binding domain."}],
        }}],
    }))
    return path


def test_local_quotes_allow_layout_whitespace_and_ellipsis(tmp_path: Path) -> None:
    path = write_case(tmp_path)
    report = validate_prediction_evidence(path, tmp_path)
    assert report.is_valid
    assert report.metadata["verified_quotes"] == 1


@pytest.mark.parametrize("fault", ["quote", "reference", "source", "score"])
def test_invalid_prediction_evidence_fails(tmp_path: Path, fault: str) -> None:
    path = write_case(tmp_path)
    data = yaml.safe_load(path.read_text())
    review = data["predictions"][0]["review"]
    if fault == "quote":
        review["supported_by"][0]["supporting_text"] = "DOMAIN 41..260"
    elif fault == "reference":
        data["references"] = []
    elif fault == "source":
        (tmp_path / "genes/source.txt").unlink()
    else:
        review["confidence_score"] = 2
    path.write_text(yaml.safe_dump(data))
    assert not validate_prediction_evidence(path, tmp_path).is_valid


def test_goa_file_as_support_fails(tmp_path: Path) -> None:
    path = write_case(tmp_path)
    (tmp_path / "genes/X-goa.tsv").write_text("enables\tGO:0003674\tmolecular_function\n")
    data = yaml.safe_load(path.read_text())
    data["references"].append({"id": "file:X-goa.tsv", "title": "GOA"})
    data["predictions"][0]["review"]["supported_by"].append(
        {"reference_id": "file:X-goa.tsv", "supporting_text": "molecular_function"})
    path.write_text(yaml.safe_dump(data))
    report = validate_prediction_evidence(path, tmp_path)
    assert not report.is_valid
    assert [i.check_type for i in report.issues] == ["supporting_text_goa_file"]


def test_goa_file_listed_only_in_references_passes(tmp_path: Path) -> None:
    path = write_case(tmp_path)
    (tmp_path / "genes/X-goa.tsv").write_text("enables\tGO:0003674\tmolecular_function\n")
    data = yaml.safe_load(path.read_text())
    data["references"].append({"id": "file:X-goa.tsv", "title": "GOA"})
    path.write_text(yaml.safe_dump(data))
    assert validate_prediction_evidence(path, tmp_path).is_valid


def test_missing_quote_is_reported_without_changing_schema_optionality(tmp_path: Path) -> None:
    path = write_case(tmp_path)
    data = yaml.safe_load(path.read_text())
    del data["predictions"][0]["review"]["supported_by"][0]["supporting_text"]
    path.write_text(yaml.safe_dump(data))
    report = validate_prediction_evidence(path, tmp_path)
    assert report.is_valid
    assert report.warning_count == 1
    assert report.metadata["verified_quotes"] == 0


def test_strict_excerpt_validation_rejects_missing_quotes(tmp_path: Path) -> None:
    path = write_case(tmp_path)
    data = yaml.safe_load(path.read_text())
    del data["predictions"][0]["review"]["supported_by"][0]["supporting_text"]
    path.write_text(yaml.safe_dump(data))
    report = validate_prediction_evidence(path, tmp_path, require_excerpts=True)
    assert not report.is_valid
    assert report.error_count == 1


def test_excerpt_segments_must_follow_source_order_without_reusing_text() -> None:
    source = "First finding.\nIntervening detail.\nSecond finding."
    assert local_quote_matches("First finding. ... Second finding.", source)
    assert not local_quote_matches("Second finding. ... First finding.", source)
    assert not local_quote_matches("First finding. ... First finding.", source)


@pytest.mark.parametrize("fault", [None, "title", "quote", "cache"])
def test_publication_titles_quotes_and_missing_cache(tmp_path: Path, fault: str | None) -> None:
    path = write_case(tmp_path)
    publications = tmp_path / "publications"
    publications.mkdir()
    cache = publications / "PMID_1.md"
    cache.write_text("---\npmid: '1'\ntitle: Source title.\nfull_text_available: true\n---\n"
                     "# Source title.\n\n## Abstract\nMeasured receptor binding.\n")
    data = yaml.safe_load(path.read_text())
    data["references"] = [{"id": "PMID:1", "title": "Source title."}]
    support = {"reference_id": "PMID:1", "supporting_text": "Measured receptor binding."}
    data["predictions"][0]["review"]["supported_by"] = [support]
    if fault == "title":
        data["references"][0]["title"] = "Unrelated experiment."
    elif fault == "quote":
        support["supporting_text"] = "Measured kinase activity."
    elif fault == "cache":
        cache.unlink()
    path.write_text(yaml.safe_dump(data))
    report = validate_prediction_evidence(path, tmp_path)
    assert report.is_valid == (fault is None)


@pytest.mark.parametrize(
    ("source", "valid"),
    [
        ("huggingface.co/datasets/wanglab/protein_catalogue", True),
        ("https://example.org/data.tsv", True),
        ("genes/missing.txt", False),
        ("missing.md", False),
        ("SPAC8E11.10-hypotheses/x/openscientist.md", False),
        ("SPCC16C4.02c-notes/x.md", False),
    ],
)
def test_source_documents_external_ids_pass_missing_files_fail(
    tmp_path: Path, source: str, valid: bool
) -> None:
    path = write_case(tmp_path)
    data = yaml.safe_load(path.read_text())
    data["source_documents"].append(source)
    path.write_text(yaml.safe_dump(data))
    assert validate_prediction_evidence(path, tmp_path).is_valid is valid


@pytest.mark.parametrize("prefix", ["DOI", "doi"])
@pytest.mark.parametrize("title_ok", [True, False])
def test_doi_reference_is_resolved_whatever_the_prefix_case(
    tmp_path: Path, prefix: str, title_ok: bool
) -> None:
    path = write_case(tmp_path)
    publications = tmp_path / "publications"
    publications.mkdir()
    (publications / "DOI_10.1_x.md").write_text(
        "---\nreference_id: DOI:10.1/x\ntitle: Source title.\ndoi: 10.1/x\n"
        "content_type: abstract_only\n---\n\n# Source title.\n\n## Content\n\nAbstract.\n"
    )
    data = yaml.safe_load(path.read_text())
    data["references"].append(
        {"id": f"{prefix}:10.1/x", "title": "Source title." if title_ok else "Unrelated experiment."}
    )
    path.write_text(yaml.safe_dump(data))
    report = validate_prediction_evidence(path, tmp_path)
    assert report.is_valid is title_ok
    assert not any("Unsupported source" in issue.message for issue in report.issues)
    assert report.metadata["verified_titles"] == (1 if title_ok else 0)
