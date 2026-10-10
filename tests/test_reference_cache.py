"""Regression tests for reading the committed publications cache.

Covers delimiter-looking values (fixed upstream in linkml-reference-validator
0.3.0) through both validation paths, and that validation trusts the cache as
written rather than re-fetching entries that lack an extractor_version stamp.
"""

import os
from pathlib import Path
import subprocess
import runpy
import sys
from types import SimpleNamespace

import pytest
import yaml

pytest.importorskip("linkml_reference_validator")

from ai_gene_review.validation.supporting_text import build_supporting_text_validator

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TITLE = "Carbonic anhydrase His----Tyr: structural comparison"
QUOTE = "Controlled fixture passage."


@pytest.fixture(autouse=True)
def clear_validator_cache():
    build_supporting_text_validator.cache_clear()
    yield
    build_supporting_text_validator.cache_clear()


@pytest.fixture
def cache(tmp_path):
    # No extractor_version stamp, like nearly every committed cache entry: an
    # untrusted 0.3.0 fetcher would treat it as stale and re-fetch PMID:1.
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


@pytest.mark.parametrize(
    "config_path",
    ["conf/reference_validator_config.yaml", ".linkml-reference-validator.yaml"],
)
def test_repo_configs_trust_committed_cache(config_path):
    config = yaml.safe_load((PROJECT_ROOT / config_path).read_text())
    assert config["trust_cached_entries"] is True


def test_in_process_title_quote_and_cache_preservation(cache):
    p = cache / "PMID_1.md"
    before = p.read_bytes()
    validator, _ = build_supporting_text_validator(cache)
    assert validator.config.trust_cached_entries
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
    validator, _ = build_supporting_text_validator(cache)
    with pytest.raises(Exception, match="quoted scalar|expected"):
        validator.validate_title("PMID:1", TITLE)


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
        "--config",
        str(PROJECT_ROOT / "conf/reference_validator_config.yaml"),
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


def test_warming_uses_upstream_cli_without_running_it(monkeypatch):
    module = runpy.run_path(str(PROJECT_ROOT / "scripts/warm_reference_cache.py"))
    monkeypatch.setattr(module["glob"], "glob", lambda pattern: ["fixture.yaml"])
    calls = []
    monkeypatch.setattr(module["subprocess"], "run", lambda *a, **kw: calls.append((a, kw)))
    assert module["main"]() == 0
    cmd = calls[0][0][0]
    assert cmd[:5] == ["uv", "run", "linkml-reference-validator", "validate", "data"]
    assert cmd[cmd.index("--config") + 1] == "conf/reference_validator_config.yaml"
    assert "--no-full-text" not in cmd


@pytest.mark.parametrize("newline", ["\n", "\r\n"])
def test_full_text_metadata_survives_title_delimiters(tmp_path, newline):
    module = runpy.run_path(str(PROJECT_ROOT / "scripts/mark_full_text_unavailable.py"))
    p = tmp_path / "PMID_1.md"
    p.write_bytes((
        f"---\ntitle: '{TITLE}'\ncontent_type: full_text_xml\n"
        "full_text_available: true\n---\nBody\n---\nTail\n"
    ).replace("\n", newline).encode())
    before = p.read_bytes()
    assert module["load_pub_metadata"](p)["title"] == TITLE
    assert module["pub_has_full_text"](p)
    assert p.read_bytes() == before


@pytest.mark.parametrize("metadata", ["", "plain scalar", "- item", "title: 'unfinished"])
def test_full_text_utility_rejects_invalid_metadata(tmp_path, metadata):
    module = runpy.run_path(str(PROJECT_ROOT / "scripts/mark_full_text_unavailable.py"))
    p = tmp_path / "PMID_1.md"
    p.write_text(f"---\n{metadata}\n---\nBody")
    assert module["load_pub_metadata"](p) is None


@pytest.mark.parametrize("script", ["mark_full_text_unavailable.py", "extract_supporting_text_fixes.py"])
def test_direct_utilities_trust_committed_cache(monkeypatch, tmp_path, script):
    import linkml_reference_validator.validation.supporting_text_validator as upstream

    calls = []

    def constructor(config):
        calls.append(config)
        return SimpleNamespace()

    monkeypatch.setattr(upstream, "SupportingTextValidator", constructor)
    monkeypatch.chdir(tmp_path)  # No real gene files or publication caches are visited.
    monkeypatch.setattr(sys, "argv", [script, "--dry-run"])
    module = runpy.run_path(str(PROJECT_ROOT / "scripts" / script))
    if script == "mark_full_text_unavailable.py":
        module["main"]()
    assert len(calls) == 1
    assert calls[0].trust_cached_entries
