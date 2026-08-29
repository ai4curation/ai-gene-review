"""Tests for the publication-cache full-text warm sweep.

The warm sweep (``ai_gene_review.etl.publication_warm``) is modeled on the
monarch-initiative/dismech ``warm-reference-cache`` workflow: records that lack
full text are attempted once through the linkml-reference-validator full-text
provider chain, and the durable ``full_text_attempted: true`` frontmatter flag
guarantees each record is only ever attempted once, so bounded ``--limit`` runs
drain the backlog incrementally.

These tests exercise candidate selection and the frontmatter/body rewriting on
temporary files; no network access is required. The provider-chain test uses a
real ``FullTextProvider`` registered through linkml-reference-validator's public
``FullTextProviderRegistry.register_instance`` hook (the same extension point
custom YAML-defined providers use), not a mock of our own code.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.etl.publication_warm import (
    apply_full_text,
    find_warm_candidates,
    identifiers_from_frontmatter,
    mark_attempted,
    parse_publication_file,
    warm_publication,
)


def write_pub(
    directory: Path,
    pmid: str,
    *,
    full_text_available: bool = False,
    full_text_attempted: bool | None = None,
    pmcid: str | None = None,
    doi: str | None = None,
    body_extra: str = "",
) -> Path:
    """Write a minimal publication cache file in the repo's format."""
    frontmatter: dict = {
        "pmid": pmid,
        "title": f"Title for {pmid}",
        "authors": ["Doe J"],
        "journal": "J Test",
        "year": "2020",
        "full_text_available": full_text_available,
    }
    if full_text_attempted is not None:
        frontmatter["full_text_attempted"] = full_text_attempted
    if pmcid:
        frontmatter["pmcid"] = pmcid
    if doi:
        frontmatter["doi"] = doi
    body = f"\n# Title for {pmid}\n\n## Abstract\n\nAn abstract.\n{body_extra}"
    text = "---\n" + yaml.dump(frontmatter, sort_keys=False) + "---\n" + body
    path = directory / f"PMID_{pmid}.md"
    path.write_text(text)
    return path


def read_frontmatter(path: Path) -> dict:
    parts = path.read_text().split("---", 2)
    return yaml.safe_load(parts[1])


def test_parse_publication_file_roundtrip(tmp_path: Path) -> None:
    path = write_pub(tmp_path, "1", doi="10.1/x")
    frontmatter, body = parse_publication_file(path)
    assert frontmatter["pmid"] == "1"
    assert frontmatter["doi"] == "10.1/x"
    assert "## Abstract" in body


def test_find_warm_candidates_selects_unattempted_without_full_text(
    tmp_path: Path,
) -> None:
    has_full_text = write_pub(
        tmp_path, "100", full_text_available=True, body_extra="\n## Full Text\n\nBody\n"
    )
    needs_warm = write_pub(tmp_path, "200", doi="10.1/y")
    already_attempted = write_pub(tmp_path, "300", full_text_attempted=True)

    candidates = find_warm_candidates(tmp_path)
    paths = [c.path for c in candidates]
    assert needs_warm in paths
    assert has_full_text not in paths
    assert already_attempted not in paths


def test_find_warm_candidates_flags_missing_full_text_section(tmp_path: Path) -> None:
    # full_text_available: true but no "## Full Text" section -> still a candidate
    inconsistent = write_pub(tmp_path, "400", full_text_available=True)
    candidates = find_warm_candidates(tmp_path)
    assert [c.path for c in candidates] == [inconsistent]


def test_identifiers_from_frontmatter_strips_pmc_prefix() -> None:
    ids = identifiers_from_frontmatter(
        {"pmid": "123", "pmcid": "PMC456", "doi": "10.1/z"}
    )
    assert ids.pmid == "123"
    assert ids.pmcid == "456"
    assert ids.doi == "10.1/z"


def test_mark_attempted_preserves_body(tmp_path: Path) -> None:
    path = write_pub(tmp_path, "500")
    frontmatter, body = parse_publication_file(path)
    mark_attempted(path, frontmatter, body)

    updated = read_frontmatter(path)
    assert updated["full_text_attempted"] is True
    assert updated["full_text_available"] is False
    assert "## Abstract" in path.read_text()
    # A durably attempted record is no longer a candidate.
    assert find_warm_candidates(tmp_path) == []


def test_apply_full_text_appends_section_and_tags(tmp_path: Path) -> None:
    path = write_pub(tmp_path, "600", doi="10.1/q")
    frontmatter, body = parse_publication_file(path)
    apply_full_text(
        path,
        frontmatter,
        body,
        text="The full text body.",
        extraction_method="pdf",
        provider="unpaywall",
        oa_status="gold",
        license="cc-by",
        full_text_url="https://example.org/x.pdf",
    )

    updated = read_frontmatter(path)
    assert updated["full_text_available"] is True
    assert updated["full_text_attempted"] is True
    assert updated["full_text_provider"] == "unpaywall"
    assert updated["full_text_extraction_method"] == "pdf"
    assert updated["oa_status"] == "gold"
    assert updated["license"] == "cc-by"
    assert updated["full_text_url"] == "https://example.org/x.pdf"

    content = path.read_text()
    assert "## Full Text\n\nThe full text body." in content
    assert "## Abstract" in content
    assert find_warm_candidates(tmp_path) == []


def test_apply_full_text_replaces_existing_section(tmp_path: Path) -> None:
    path = write_pub(
        tmp_path, "700", body_extra="\n## Full Text\n\nStale partial text.\n"
    )
    frontmatter, body = parse_publication_file(path)
    apply_full_text(
        path,
        frontmatter,
        body,
        text="Fresh complete text.",
        extraction_method="xml",
        provider="pmc",
    )
    content = path.read_text()
    assert "Fresh complete text." in content
    assert "Stale partial text." not in content
    assert content.count("## Full Text") == 1


@pytest.fixture
def stub_provider():
    """Register a full-text provider via LRV's public registry hook."""
    from linkml_reference_validator.etl.fulltext.base import (
        FullTextProvider,
        FullTextProviderRegistry,
    )
    from linkml_reference_validator.models import FullTextLocation

    class StubProvider(FullTextProvider):
        @classmethod
        def name(cls) -> str:
            return "warm-test-stub"

        def locate(self, ids, config):
            if ids.pmid == "800":
                return FullTextLocation(
                    text="Stub full text. " * 100,
                    format_hint="text",
                    oa_status="gold",
                    provider="warm-test-stub",
                )
            return None

    FullTextProviderRegistry.register_instance("warm-test-stub", StubProvider())
    yield "warm-test-stub"
    FullTextProviderRegistry._by_name.pop("warm-test-stub", None)


def test_warm_publication_full_text_via_provider_chain(
    tmp_path: Path, stub_provider: str
) -> None:
    from linkml_reference_validator.models import ReferenceValidationConfig
    from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher

    fetcher = ReferenceFetcher(ReferenceValidationConfig(cache_dir=tmp_path / "lrv"))
    hit = write_pub(tmp_path, "800")
    miss = write_pub(tmp_path, "900")

    assert warm_publication(hit, fetcher, providers=[stub_provider]) == "full_text"
    assert warm_publication(miss, fetcher, providers=[stub_provider]) == "attempted"

    hit_frontmatter = read_frontmatter(hit)
    assert hit_frontmatter["full_text_available"] is True
    assert hit_frontmatter["full_text_provider"] == "warm-test-stub"
    assert "Stub full text." in hit.read_text()

    miss_frontmatter = read_frontmatter(miss)
    assert miss_frontmatter["full_text_available"] is False
    assert miss_frontmatter["full_text_attempted"] is True
