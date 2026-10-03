"""Regression tests for delimiter-looking values through both validation paths."""

import os
from pathlib import Path
import subprocess

import pytest
import yaml

from ai_gene_review.validation import reference_cache_compat as compat
from ai_gene_review.validation.supporting_text import build_supporting_text_validator
from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TITLE = "Carbonic anhydrase His----Tyr: structural comparison"
QUOTE = "Controlled fixture passage."


@pytest.fixture
def cache(tmp_path):
    text = (
        "---\npmid: '1'\ntitle: '"
        + TITLE
        + "'\njournal: Fixture\nyear: '2026'\n---\n\n## Abstract\n\n"
        + QUOTE
        + "\n\n---\nTrailing body text.\n"
    )
    p = tmp_path / "PMID_1.md"
    p.write_text(text)
    return tmp_path


@pytest.mark.parametrize("newline", ["\n", "\r\n"])
def test_in_process_title_quote_and_cache_preservation(cache, newline):
    p = cache / "PMID_1.md"
    p.write_bytes(p.read_text().replace("\n", newline).encode())
    before = p.read_bytes()
    build_supporting_text_validator.cache_clear()
    validator, _ = build_supporting_text_validator(cache)
    assert validator.validate_title("PMID:1", TITLE).is_valid
    assert validator.validate(QUOTE, "PMID:1").is_valid
    assert not validator.validate_title("PMID:1", "An unrelated title").is_valid
    assert not validator.validate(
        "This invented sentence has no matching content zzqq.", "PMID:1"
    ).is_valid
    loaded = validator.fetcher.fetch("PMID:1")
    assert loaded.journal == "Fixture" and loaded.year == "2026"
    assert "Trailing body text." in loaded.content
    assert p.read_bytes() == before


def test_malformed_frontmatter_is_still_rejected(cache):
    p = cache / "PMID_1.md"
    p.write_text("---\ntitle: 'unfinished\n---\nBody\n")
    build_supporting_text_validator.cache_clear()
    validator, _ = build_supporting_text_validator(cache)
    with pytest.raises(Exception, match="quoted scalar|expected"):
        validator.validate_title("PMID:1", TITLE)


def test_install_is_idempotent_and_limited_to_affected_version(monkeypatch):
    monkeypatch.setattr(compat, "version", lambda name: "0.2.1")
    assert compat.install_reference_cache_compatibility()
    method = ReferenceFetcher._load_markdown_format
    assert compat.install_reference_cache_compatibility()
    assert ReferenceFetcher._load_markdown_format is method
    monkeypatch.setattr(compat, "version", lambda name: "0.2.2")

    def sentinel(*args):
        return None

    monkeypatch.setattr(ReferenceFetcher, "_load_markdown_format", sentinel)
    assert not compat.install_reference_cache_compatibility()
    assert ReferenceFetcher._load_markdown_format is sentinel


@pytest.mark.parametrize("bad", [None, "title", "quote"])
def test_normal_reference_wrapper_preserves_strict_validation(cache, tmp_path, bad):
    title = "An unrelated title" if bad == "title" else TITLE
    quote = (
        "This invented sentence has no matching content zzqq."
        if bad == "quote"
        else QUOTE
    )
    data = {
        "id": "P00918",
        "gene_symbol": "CA2",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "references": [{"id": "PMID:1", "title": title}],
        "existing_annotations": [
            {
                "term": {"id": "GO:0004089", "label": "carbonate dehydratase activity"},
                "evidence_type": "IDA",
                "original_reference_id": "PMID:1",
                "review": {
                    "summary": "Fixture assertion",
                    "action": "ACCEPT",
                    "supported_by": [
                        {"reference_id": "PMID:1", "supporting_text": quote}
                    ],
                },
            }
        ],
    }
    f = tmp_path / "review.yaml"
    f.write_text(yaml.safe_dump(data))
    before = (cache / "PMID_1.md").read_bytes()
    env = os.environ.copy()
    env.update(UV_NO_SYNC="1", UV_OFFLINE="1", PYTHONDONTWRITEBYTECODE="1")
    cmd = [
        str(PROJECT_ROOT / "scripts/run_reference_validator.sh"),
        "validate",
        "data",
        str(f),
        "--schema",
        str(PROJECT_ROOT / "src/ai_gene_review/schema/gene_review.yaml"),
        "--target-class",
        "GeneReview",
        "--cache-dir",
        str(cache),
        "--no-full-text",
    ]
    r = subprocess.run(cmd, text=True, capture_output=True, env=env, timeout=60)
    assert (r.returncode == 0) == (bad is None), r.stdout + r.stderr
    if bad == "title":
        assert "Title mismatch" in r.stdout
    if bad == "quote":
        assert "[ERROR]" in r.stdout
    assert (cache / "PMID_1.md").read_bytes() == before
