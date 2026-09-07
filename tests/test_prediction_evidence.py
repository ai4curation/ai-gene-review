"""Prediction sidecar evidence checks use actual source files, without network."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.prediction_evidence import validate_prediction_evidence


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


def test_missing_quote_is_reported_without_changing_schema_optionality(tmp_path: Path) -> None:
    path = write_case(tmp_path)
    data = yaml.safe_load(path.read_text())
    del data["predictions"][0]["review"]["supported_by"][0]["supporting_text"]
    path.write_text(yaml.safe_dump(data))
    report = validate_prediction_evidence(path, tmp_path)
    assert report.is_valid
    assert report.warning_count == 1
    assert report.metadata["verified_quotes"] == 0


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
