"""Regression tests for delimiter-looking values through both validation paths."""

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
def isolate_reference_validator():
    build_supporting_text_validator.cache_clear()
    yield
    build_supporting_text_validator.cache_clear()


@pytest.fixture(params=[
    {"content_type": "abstract_only"},
    {"content_type": "full_text_xml"},
    {"content_type": "full_text_html"},
    {"full_text_available": False},
    {"full_text_available": True},
], ids=["legacy-abstract", "legacy-xml", "legacy-html", "modern-abstract", "modern-fulltext"])
def cache(tmp_path, request):
    # With trust_cached_entries, all metadata shapes preserve the reviewed body;
    # these cases check cache preservation, not metadata precedence.
    text = (
        "---\npmid: '1'\ntitle: '"
        + TITLE
        + "'\njournal: Fixture\nyear: '2026'\n"
        + yaml.safe_dump(request.param)
        + "---\n\n## Abstract\n\n"
        + QUOTE
        + "\n\n---\nTrailing body text.\n"
    )
    p = tmp_path / "PMID_1.md"
    p.write_text(text)
    return tmp_path


@pytest.mark.parametrize("newline", ["\n", "\r\n"])
def test_in_process_title_quote_and_cache_preservation(cache, newline, monkeypatch):
    p = cache / "PMID_1.md"
    p.write_bytes(p.read_text().replace("\n", newline).encode())
    before = p.read_bytes()
    build_supporting_text_validator.cache_clear()
    validator, _ = build_supporting_text_validator(cache)
    def forbid_network(*args, **kwargs):
        pytest.fail("Validation must use the reviewed cache without network access")

    # Cover both source fetching and full-text retries through their network boundary.
    monkeypatch.setattr("socket.socket.connect", forbid_network)
    assert validator.config.trust_cached_entries is True
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


@pytest.mark.parametrize("metadata", ["", "plain scalar", "- item", "true"])
def test_non_mapping_cache_fails_without_fetch_or_overwrite(tmp_path, metadata, monkeypatch):
    cache_file = tmp_path / "PMID_1.md"
    cache_file.write_text(f"---\n{metadata}\n---\n{QUOTE}")
    before = cache_file.read_bytes()
    validator, _ = build_supporting_text_validator(tmp_path)

    def forbid_network(*args, **kwargs):
        pytest.fail("Malformed cached metadata must not trigger a network request")

    monkeypatch.setattr("socket.socket.connect", forbid_network)
    monkeypatch.setattr("socket.getaddrinfo", forbid_network)
    # Upstream may raise or return a clean failure; neither may fetch or rewrite.
    try:
        result = validator.validate_title("PMID:1", TITLE)
    except Exception:
        # pytest.fail raises BaseException, so a network attempt cannot be swallowed.
        pass
    else:
        assert not result.is_valid
    assert cache_file.read_bytes() == before


@pytest.mark.parametrize("bad", [None, "title", "quote", "empty", "editorial"])
def test_normal_reference_wrapper_preserves_strict_validation(cache, tmp_path, bad, no_network_subprocess_env):
    title = "An unrelated title" if bad == "title" else TITLE
    quote = {
        "quote": "This invented sentence has no matching content zzqq.",
        "empty": "",
        "editorial": "[An editorial assertion, with no quoted passage]",
    }.get(bad, QUOTE)
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
    env, network_attempt = no_network_subprocess_env
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
        "--config",
        str(PROJECT_ROOT / "conf/reference_validator_config.yaml"),
    ]
    r = subprocess.run(cmd, text=True, capture_output=True, env=env, timeout=60)
    assert not network_attempt.exists(), r.stdout + r.stderr
    assert (r.returncode == 0) == (bad is None), r.stdout + r.stderr
    if bad == "title":
        assert "Title mismatch" in r.stdout
    if bad in ("quote", "empty", "editorial"):
        assert "[ERROR]" in r.stdout
    assert (cache / "PMID_1.md").read_bytes() == before


def test_warming_opts_out_of_trusting_existing_cache(monkeypatch):
    module = runpy.run_path(str(PROJECT_ROOT / "scripts/warm_reference_cache.py"))
    monkeypatch.setattr(module["glob"], "glob", lambda pattern: ["fixture.yaml"])
    calls = []
    def capture(*args, **kwargs):
        command = args[0]
        config = yaml.safe_load(Path(command[command.index("--config") + 1]).read_text())
        assert config["trust_cached_entries"] is False
        assert config["cache_dir"] == "publications"
        calls.append((args, kwargs))

    monkeypatch.setattr(module["subprocess"], "run", capture)
    assert module["main"]() == 0
    assert calls[0][0][0][:7] == [
        "uv", "run", "python", "-m", "ai_gene_review.validation.reference_cli",
        "validate", "data",
    ]
    assert "--no-full-text" not in calls[0][0][0]


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
def test_direct_utilities_trust_reviewed_cache(monkeypatch, tmp_path, script):
    import linkml_reference_validator.validation.supporting_text_validator as upstream

    calls = []
    def constructor(config):
        assert config.trust_cached_entries is True
        expected = yaml.safe_load((PROJECT_ROOT / "conf/reference_validator_config.yaml").read_text())
        assert config.skip_prefixes == expected["skip_prefixes"]
        assert config.literal_bracket_patterns == expected["literal_bracket_patterns"]
        assert config.reference_base_dir == PROJECT_ROOT / expected["reference_base_dir"]
        calls.append(config)
        return SimpleNamespace(config=config)

    monkeypatch.setattr(upstream, "SupportingTextValidator", constructor)
    monkeypatch.chdir(tmp_path)  # No real gene files or publication caches are visited.
    monkeypatch.setattr(sys, "argv", [script, "--dry-run"])
    module = runpy.run_path(str(PROJECT_ROOT / "scripts" / script))
    if script == "mark_full_text_unavailable.py":
        module["main"]()
    assert len(calls) == 1


def test_subprocess_network_guard_is_active_through_wrapper(tmp_path, no_network_subprocess_env):
    cache_dir = tmp_path / "empty_cache"
    cache_dir.mkdir()
    review = tmp_path / "uncached.yaml"
    review.write_text(yaml.safe_dump({
        "id": "P00918",
        "gene_symbol": "CA2",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "references": [{"id": "PMID:1", "title": TITLE}],
    }))
    env, attempted = no_network_subprocess_env
    env.update(UV_NO_SYNC="1", UV_OFFLINE="1", PYTHONDONTWRITEBYTECODE="1")
    result = subprocess.run(
        [
            str(PROJECT_ROOT / "scripts/run_reference_validator.sh"),
            "validate", "data", str(review),
            "--schema", str(PROJECT_ROOT / "src/ai_gene_review/schema/gene_review.yaml"),
            "--target-class", "GeneReview", "--cache-dir", str(cache_dir),
            "--config", str(PROJECT_ROOT / "conf/reference_validator_config.yaml"),
        ],
        env=env, capture_output=True, text=True, timeout=60,
    )
    # Unknown/unfetchable references can be advisory; the recorded attempt is
    # the assertion even if the CLI catches the guard's exception and exits 0.
    assert attempted.exists(), result.stdout + result.stderr
    event, target = attempted.read_text().split(" ", 1)
    assert event in {"socket.connect", "socket.getaddrinfo"}
    assert target.startswith("(") and target != "()", attempted.read_text()
    assert not (cache_dir / "PMID_1.md").exists()


def test_bare_cli_default_config_trusts_reviewed_cache(monkeypatch):
    """A validator run without --config uses .linkml-reference-validator.yaml."""
    from linkml_reference_validator.cli.shared import load_validation_config

    monkeypatch.chdir(PROJECT_ROOT)
    config = load_validation_config(None, load_custom_sources=False)
    assert config.trust_cached_entries is True
