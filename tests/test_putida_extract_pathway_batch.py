"""Tests for provider-aware P. putida pathway batch status."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "projects"
    / "P_PUTIDA"
    / "extract_pathway_batch.py"
)
SPEC = importlib.util.spec_from_file_location("extract_pathway_batch", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
extract_pathway_batch = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = extract_pathway_batch
SPEC.loader.exec_module(extract_pathway_batch)


def test_provider_label_preserves_known_branding():
    assert extract_pathway_batch.provider_label("openscientist") == "OpenScientist"
    assert extract_pathway_batch.provider_label("perplexity-lite") == "Perplexity Lite"


def test_review_status_uses_requested_research_provider(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    gene_dir = Path("genes/PSEPK/argF")
    gene_dir.mkdir(parents=True)
    (gene_dir / "argF-ai-review.yaml").write_text(
        """id: Q88NX4
gene_symbol: argF
existing_annotations:
  - review:
      action: ACCEPT
""",
        encoding="utf-8",
    )
    report = gene_dir / "argF-deep-research-openscientist.md"
    report.write_text("report\n", encoding="utf-8")
    extract_pathway_batch._PSEPK_REVIEW_INDEX = None

    status = extract_pathway_batch.review_status(
        {
            "suggested_review_name": "argF",
            "uniprot_accession": "Q88NX4",
        },
        "openscientist",
    )

    assert status["review_status"] == "PRESENT"
    assert status["curation_status"] == "CURATED"
    assert status["openscientist_research_status"] == "PRESENT"
    assert status["openscientist_research_file"] == report.as_posix()
    assert "asta_research_status" not in status
