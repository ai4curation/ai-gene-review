"""External prediction sidecars stay distinct from the main annotation review."""

from pathlib import Path

import pytest
import yaml
from bs4 import BeautifulSoup

from ai_gene_review.render import render_gene_review


def write_review(gene_dir: Path) -> Path:
    """Create a review whose accession filename differs from its gene symbol."""
    path = gene_dir / "A0A8C9H4D2-ai-review.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "id": "A0A8C9H4D2",
                "gene_symbol": "OLFML2A",
                "existing_annotations": [
                    {
                        "term": {"id": "GO:0005615", "label": "extracellular space"},
                        "evidence_type": "IEA",
                        "review": {"action": "ACCEPT"},
                    }
                ],
            }
        )
    )
    return path


def write_predictions(path: Path, method: str = "ProtNLM2") -> None:
    """Write a real sidecar with source metadata and an assessed prediction."""
    path.write_text(
        yaml.safe_dump(
            {
                "id": "A0A8C9H4D2",
                "gene_symbol": "OLFML2A",
                "description": "External review summary <script>bad()</script>",
                "predictions": [
                    {
                        "source_method": method,
                        "source_version": "UniProt 2024_06 pilot",
                        "predicted_term": {
                            "id": "GO:0031012",
                            "label": "extracellular matrix",
                        },
                        "predicted_term_type": "GO_CC",
                        "review": {
                            "assessment": "COR",
                            "confidence_score": 2,
                            "summary": "Evidence supports this prediction.",
                            "supported_by": [
                                {"reference_id": "PMID:15836428"},
                                {
                                    "reference_id": "PMID:15836428",
                                    "supporting_text": "An exact source excerpt.",
                                },
                            ],
                        },
                    }
                ],
            }
        )
    )


@pytest.mark.parametrize(
    "filename",
    [
        "A0A8C9H4D2-protnlm-predictions-review.yaml",
        "A0A8C9H4D2-predictions-review.yaml",
        "OLFML2A-predictions-review.yaml",
        "OLFML2A-det-predictions-review.yaml",
    ],
)
def test_inline_predictions_are_separate_and_attributed(
    tmp_path: Path, filename: str
) -> None:
    review = write_review(tmp_path)
    write_predictions(tmp_path / filename)
    soup = BeautifulSoup(render_gene_review(review).read_text(), "html.parser")
    section = soup.select_one("#external-predictions")
    assert section is not None
    text = section.get_text(" ", strip=True)
    assert "External Prediction Reviews" in text
    assert "GOA annotation set used for this review" in text
    assert "do not constitute official GO annotations" in text
    assert "ProtNLM2" in text
    assert "UniProt 2024_06 pilot" in text
    assert "COR — Correct novel prediction" in text
    assert "Review score: 2/2" in text
    assert "Evidence supports this prediction." in text
    assert section.select_one('a[href="https://pubmed.ncbi.nlm.nih.gov/15836428"]')
    assert [item.get_text() for item in section.select(".finding-text")] == [
        '"An exact source excerpt."'
    ]
    assert section.select_one(f'a[href="{filename}"]')
    assert section.select_one('a[href="https://www.ebi.ac.uk/QuickGO/term/GO:0031012"]')
    assert section.find("script") is None
    assert len(soup.select(".annotations-table tbody tr")) == 1
    annotations = soup.select_one(".annotations-table")
    assert annotations is not None
    assert "GO:0031012" not in annotations.get_text()


def test_multiple_sidecars_and_custom_output_links(tmp_path: Path) -> None:
    gene_dir = tmp_path / "gene"
    gene_dir.mkdir()
    review = write_review(gene_dir)
    write_predictions(gene_dir / "A0A8C9H4D2-protnlm-predictions-review.yaml")
    write_predictions(gene_dir / "OLFML2A-predictions-review.yaml", "DeepECTF")
    # Unreviewed model outputs must not be mistaken for PredictionReview files.
    (gene_dir / "A0A8C9H4D2-sft-predictions.yaml").write_text("invalid: [")
    output = tmp_path / "preview.html"
    soup = BeautifulSoup(
        render_gene_review(review, output_path=output).read_text(), "html.parser"
    )
    assert len(soup.select("#external-predictions .prediction-card")) == 2
    assert len(soup.select("#external-predictions .prediction-review")) == 2
    for filename in [
        "A0A8C9H4D2-protnlm-predictions-review.yaml",
        "OLFML2A-predictions-review.yaml",
    ]:
        assert soup.select_one(f'#external-predictions a[href="gene/{filename}"]')


def test_external_local_evidence_links_resolve_from_output(tmp_path: Path) -> None:
    gene_dir = tmp_path / "genes" / "9PRIM" / "A0A8C9H4D2"
    gene_dir.mkdir(parents=True)
    review = write_review(gene_dir)
    sidecar = gene_dir / "A0A8C9H4D2-protnlm-predictions-review.yaml"
    write_predictions(sidecar)
    source = gene_dir / "A0A8C9H4D2-uniprot.txt"
    source.write_text("Domain evidence")
    data = yaml.safe_load(sidecar.read_text())
    data["predictions"][0]["review"]["supported_by"] = [
        {"reference_id": "file:9PRIM/A0A8C9H4D2/A0A8C9H4D2-uniprot.txt"}
    ]
    sidecar.write_text(yaml.safe_dump(data))
    output = tmp_path / "preview.html"
    soup = BeautifulSoup(
        render_gene_review(review, output_path=output).read_text(), "html.parser"
    )
    link = soup.select_one("#external-predictions .finding-item a")
    assert link is not None
    href = link["href"]
    assert isinstance(href, str)
    assert (output.parent / href).resolve() == source.resolve()


@pytest.mark.parametrize("empty_sidecar", [False, True])
def test_no_external_section_without_predictions(
    tmp_path: Path, empty_sidecar: bool
) -> None:
    review = write_review(tmp_path)
    if empty_sidecar:
        (tmp_path / "A0A8C9H4D2-predictions-review.yaml").write_text(
            "predictions: []\n"
        )
    soup = BeautifulSoup(render_gene_review(review).read_text(), "html.parser")
    assert soup.select_one("#external-predictions") is None
    assert soup.select_one('a[href="#external-predictions"]') is None


def test_prediction_identity_mismatch_fails(tmp_path: Path) -> None:
    review = write_review(tmp_path)
    sidecar = tmp_path / "A0A8C9H4D2-predictions-review.yaml"
    write_predictions(sidecar)
    data = yaml.safe_load(sidecar.read_text())
    data["id"] = "OTHER_PROTEIN"
    sidecar.write_text(yaml.safe_dump(data))
    with pytest.raises(ValueError, match="Prediction review ID mismatch"):
        render_gene_review(review)
