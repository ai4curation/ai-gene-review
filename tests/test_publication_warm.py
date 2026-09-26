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
    is_usable_full_text,
    mark_attempted,
    parse_publication_file,
    warm_publication,
    warm_publications,
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


def test_parse_publication_file_ignores_dashes_inside_values(tmp_path: Path) -> None:
    # A "---" embedded mid-line (e.g. in a title) must not end the frontmatter.
    path = tmp_path / "PMID_2.md"
    path.write_text(
        "---\npmid: '2'\ntitle: alpha---beta studies\nfull_text_available: false\n---\n"
        "\n# alpha---beta studies\n\n## Abstract\n\nText.\n"
    )
    frontmatter, body = parse_publication_file(path)
    assert frontmatter["title"] == "alpha---beta studies"
    assert body.startswith("\n\n# alpha---beta studies")


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


def test_mark_attempted_keeps_body_byte_identical(tmp_path: Path) -> None:
    # PubMed abstracts are hard-wrapped with trailing spaces; a frontmatter-only
    # change must not rewrite them (supporting_text is matched verbatim).
    path = tmp_path / "PMID_510.md"
    body = "\n\n# T\n\n## Abstract\n\nRegulation of body length \nand tail rays. \n"
    path.write_text("---\npmid: '510'\nfull_text_available: false\n---" + body)
    frontmatter, parsed_body = parse_publication_file(path)
    mark_attempted(path, frontmatter, parsed_body)

    content = path.read_text()
    assert "Regulation of body length \nand tail rays. \n" in content
    assert read_frontmatter(path)["full_text_attempted"] is True


def test_find_warm_candidates_retry_attempted(tmp_path: Path) -> None:
    write_pub(tmp_path, "520", full_text_attempted=True)
    assert find_warm_candidates(tmp_path) == []
    retried = find_warm_candidates(tmp_path, include_attempted=True)
    assert [c.pmid for c in retried] == ["520"]


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
        license_name="cc-by",
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


ABSTRACT = (
    "The CLAVATA1 and CLAVATA3 genes are required to maintain the balance "
    "between cell proliferation and organ formation at the shoot and flower "
    "meristems. CLV1 encodes a receptor-like protein kinase present in two "
    "protein complexes in vivo, one of approximately 185 kD and one of 450 kD."
)
BODY_WITH_ABSTRACT = f"\n\n# T\n\n## Abstract\n\n{ABSTRACT}\n"


def test_is_usable_full_text_rejects_paywall_preview() -> None:
    preview = (
        "Nature volume 22, pages 291-294. 912 Accesses. "
        + ABSTRACT
        + " This is a preview of subscription content, access via your institution. "
        "Subscribe to this journal. " + "Padding sentence about nothing. " * 50
    )
    assert is_usable_full_text(preview, BODY_WITH_ABSTRACT) is False


def test_is_usable_full_text_rejects_pmc_pdf_stub() -> None:
    stub = (
        ABSTRACT
        + " The Full Text of this article is available as aPDF(683.6 KB). "
        "Articles are provided here courtesy of Oxford University Press. "
        + "Reference list entry. " * 60
    )
    assert is_usable_full_text(stub, BODY_WITH_ABSTRACT) is False


def test_is_usable_full_text_rejects_abstract_echo() -> None:
    echo = ABSTRACT + " Keywords: meristem, kinase."
    assert is_usable_full_text(echo, BODY_WITH_ABSTRACT) is False


def test_is_usable_full_text_accepts_genuine_body_text() -> None:
    genuine = ABSTRACT + " INTRODUCTION. " + "Novel experimental detail sentence. " * 40
    assert is_usable_full_text(genuine, BODY_WITH_ABSTRACT) is True


def test_is_usable_full_text_rejects_echo_of_short_headered_abstract() -> None:
    # A short abstract whose cached copy starts with a PubMed citation header:
    # the midpoint probe can land in the header, so the tail probe must catch
    # the echo.
    short_abstract = "CLV1 encodes a receptor-like protein kinase in meristems."
    body = (
        "\n\n# T\n\n## Abstract\n\n1. Plant Cell. 1999 Mar;11(3):393-406. "
        "doi: 10.1105/tpc.11.3.393.\n\n" + short_abstract + "\n"
    )
    echo = short_abstract + " Keywords: meristem."
    assert is_usable_full_text(echo, body) is False


@pytest.fixture
def configurable_provider():
    """Register a provider whose located result is set per-test."""
    from linkml_reference_validator.etl.fulltext.base import (
        FullTextProvider,
        FullTextProviderRegistry,
    )

    class ConfigurableProvider(FullTextProvider):
        location = None
        error: Exception | None = None

        @classmethod
        def name(cls) -> str:
            return "warm-test-configurable"

        def locate(self, ids, config):
            if self.error is not None:
                raise self.error
            return self.location

    provider = ConfigurableProvider()
    FullTextProviderRegistry.register_instance("warm-test-configurable", provider)
    yield provider
    FullTextProviderRegistry._by_name.pop("warm-test-configurable", None)


def make_fetcher(tmp_path: Path):
    from linkml_reference_validator.models import ReferenceValidationConfig
    from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher

    return ReferenceFetcher(ReferenceValidationConfig(cache_dir=tmp_path / "lrv"))


def test_warm_publication_rejects_short_text(tmp_path: Path, configurable_provider) -> None:
    from linkml_reference_validator.models import FullTextLocation

    configurable_provider.location = FullTextLocation(
        text="Too short to be full text.", format_hint="text", provider="x"
    )
    path = write_pub(tmp_path, "801")
    outcome = warm_publication(
        path, make_fetcher(tmp_path), providers=["warm-test-configurable"]
    )
    assert outcome == "attempted"
    assert read_frontmatter(path)["full_text_available"] is False


def test_warm_publication_ignores_non_open_location(
    tmp_path: Path, configurable_provider
) -> None:
    from linkml_reference_validator.models import FullTextLocation

    configurable_provider.location = FullTextLocation(
        text="Private library text. " * 100,
        format_hint="text",
        provider="zotero",
        access_type="user_library",
    )
    path = write_pub(tmp_path, "802")
    outcome = warm_publication(
        path, make_fetcher(tmp_path), providers=["warm-test-configurable"]
    )
    assert outcome == "attempted"
    assert read_frontmatter(path)["full_text_available"] is False
    assert "Private library text" not in path.read_text()


def test_warm_publication_ignores_bronze_without_license(
    tmp_path: Path, configurable_provider
) -> None:
    from linkml_reference_validator.models import FullTextLocation

    configurable_provider.location = FullTextLocation(
        text="Publisher free-to-read text with no license. " * 50,
        format_hint="text",
        provider="unpaywall",
        oa_status="bronze",
    )
    path = write_pub(tmp_path, "803")
    outcome = warm_publication(
        path, make_fetcher(tmp_path), providers=["warm-test-configurable"]
    )
    assert outcome == "attempted"
    assert read_frontmatter(path)["full_text_available"] is False


def test_warm_publication_rejects_stub_text_as_clean_miss(
    tmp_path: Path, configurable_provider
) -> None:
    from linkml_reference_validator.models import FullTextLocation

    configurable_provider.location = FullTextLocation(
        text="This is a preview of subscription content, access via your institution. "
        * 30,
        format_hint="html",
        provider="openalex",
        oa_status="green",
    )
    path = write_pub(tmp_path, "804")
    outcome = warm_publication(
        path, make_fetcher(tmp_path), providers=["warm-test-configurable"]
    )
    assert outcome == "attempted"
    assert read_frontmatter(path)["full_text_available"] is False


def test_warm_publication_transient_error_leaves_record_retryable(
    tmp_path: Path, configurable_provider
) -> None:
    configurable_provider.error = RuntimeError("socket timeout")
    path = write_pub(tmp_path, "805")
    before = path.read_text()
    outcome = warm_publication(
        path, make_fetcher(tmp_path), providers=["warm-test-configurable"]
    )
    assert outcome == "transient_error"
    assert path.read_text() == before
    assert [c.pmid for c in find_warm_candidates(tmp_path)] == ["805"]


def test_warm_publications_survives_record_level_failure(
    tmp_path: Path, monkeypatch
) -> None:
    # A single record whose processing raises must not abort the sweep.
    write_pub(tmp_path, "901")
    write_pub(tmp_path, "902")

    import ai_gene_review.etl.publication_warm as warm_module

    real_warm = warm_module.warm_publication

    def exploding_warm(path, fetcher, providers=None):
        if "901" in path.name:
            raise RuntimeError("boom")
        return real_warm(path, fetcher, providers)

    monkeypatch.setattr(warm_module, "warm_publication", exploding_warm)
    stats = warm_publications(
        publications_dir=tmp_path,
        delay=0,
        providers=["nonexistent-provider"],
        fetcher=make_fetcher(tmp_path),
    )
    assert stats["processed"] == 2
    assert stats["transient_error"] == 1
    assert stats["attempted"] == 1


def test_apply_full_text_normalizes_pmc_url(tmp_path: Path) -> None:
    path = write_pub(tmp_path, "950")
    frontmatter, body = parse_publication_file(path)
    apply_full_text(
        path,
        frontmatter,
        body,
        text="Body text.",
        extraction_method="html",
        provider="openalex",
        full_text_url="https://www.ncbi.nlm.nih.gov/pmc/articles/144183",
    )
    assert (
        read_frontmatter(path)["full_text_url"]
        == "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC144183"
    )


# --- a repository landing page is not full text -------------------------------------------
#
# openalex resolved PMID:12534463 (the P. putida KT2440 genome paper) to a university
# repository landing page. The "full text" it yielded was that page's header, the abstract
# as prose, and a RIS citation export repeating the abstract as N2 and AB. It cleared every
# guard: no paywall marker, longer than the abstract, and the citation metadata supplied
# enough added characters to pass MIN_FULL_TEXT_CHARS.
#
# The cost was not a bad cache entry. `full_text_available` flipped to true, which made
# twelve accurate `full_text_unavailable` flags across ten reviews look false, and they were
# deleted on that basis before a reviewer noticed the body was a citation dump.

_LANDING_PAGE_ABSTRACT = (
    "Pseudomonas putida is a metabolically versatile saprophytic soil bacterium that has "
    "been certified as a biosafety host for the cloning of foreign genes. Sequence analysis "
    "of the 6.18 Mb genome of strain KT2440 reveals diverse transport and metabolic systems."
)

_LANDING_PAGE_BODY = f"""Research output:Contribution to journal›Article›Academic›peer-review

{_LANDING_PAGE_ABSTRACT}

}}

Research output:Contribution to journal›Article›Academic›peer-review

TY  - JOUR

T1  - Complete genome sequence and comparative analysis of the metabolically versatile Pseudomonas putida KT2440

AU  - Nelson, K.E.

AU  - Weinel, C.

JO  - Environmental Microbiology

VL  - 4

SP  - 799

EP  - 808

N2  - {_LANDING_PAGE_ABSTRACT}

AB  - {_LANDING_PAGE_ABSTRACT}

ER  -
"""

_CACHED_RECORD = f"""---
pmid: '12534463'
title: Complete genome sequence and comparative analysis of Pseudomonas putida KT2440.
full_text_available: false
---

# Complete genome sequence and comparative analysis of Pseudomonas putida KT2440.

## Abstract

{_LANDING_PAGE_ABSTRACT}
"""


def test_a_repository_landing_page_with_a_ris_dump_is_rejected():
    """The shape that got through: header + abstract + citation export, no body."""
    assert is_usable_full_text(_LANDING_PAGE_BODY, _CACHED_RECORD) is False


def test_a_bare_ris_export_is_rejected():
    """`TY  - JOUR` alone is enough to disqualify: RIS is metadata, never body text."""
    assert is_usable_full_text("TY  - JOUR\n\nAU  - Someone\n\nER  -\n", _CACHED_RECORD) is False


def test_genuine_body_text_is_still_accepted():
    """The guard must stay narrow -- these markers cannot reject a real paper."""
    real = (
        "Chemotaxis in KT2440 is mediated by a large complement of methyl-accepting "
        "proteins. We identified 27 such loci, and disruption of cheZ abolished the "
        "dephosphorylation of CheY-P in vitro. The shikimate pathway is encoded at "
        "PP_5078, whose product we assign as 3-dehydroquinate synthase on the basis of "
        "reciprocal best hits and conserved active-site residues."
    ) * 4
    assert is_usable_full_text(real, _CACHED_RECORD) is True


def test_the_abstract_wrapper_matches_the_body_based_guard():
    """``cache_publication`` holds an abstract, not a cache-file body -- same verdict either way."""
    from ai_gene_review.etl.publication_warm import is_usable_full_text_for_abstract

    assert is_usable_full_text_for_abstract(_LANDING_PAGE_BODY, _LANDING_PAGE_ABSTRACT) is False
    real = (
        "Chemotaxis in KT2440 is mediated by methyl-accepting proteins; disruption of cheZ "
        "abolished dephosphorylation of CheY-P in vitro, and PP_5078 encodes the "
        "3-dehydroquinate synthase of the shikimate pathway."
    ) * 4
    assert is_usable_full_text_for_abstract(real, _LANDING_PAGE_ABSTRACT) is True


def test_accept_full_text_rejects_a_citation_dump():
    """The writer that caused the incident, now guarded and reachable by a test.

    ``fetch_pubmed_data`` set ``full_text_available`` straight from
    ``FullTextResult.is_complete``, which reports what the provider *claimed*. The warm
    sweep had a content guard; this path had none -- and it is the path
    ``cache_publication(force=True)`` uses and the validator's error message recommends.

    Two earlier attempts at this test were worthless: one patched ``fetch_pubmed_data``
    itself, bypassing the guard entirely, and one patched a function name I had invented,
    so the stub was inert. Both passed with the guard deleted. Extracting the decision as
    ``accept_full_text`` is what makes it testable without faking Entrez.
    """
    from ai_gene_review.etl.publication import accept_full_text

    assert accept_full_text(_LANDING_PAGE_BODY, True, _LANDING_PAGE_ABSTRACT) is False


def test_accept_full_text_keeps_genuine_body_text():
    """Narrow: a real paper body is still accepted."""
    from ai_gene_review.etl.publication import accept_full_text

    real = (
        "Chemotaxis in KT2440 is mediated by methyl-accepting proteins; disruption of cheZ "
        "abolished dephosphorylation of CheY-P in vitro, and PP_5078 encodes the "
        "3-dehydroquinate synthase of the shikimate pathway."
    ) * 4
    assert accept_full_text(real, True, _LANDING_PAGE_ABSTRACT) is True


def test_accept_full_text_requires_the_provider_claim_too():
    """A provider that did not claim completeness is still not full text."""
    from ai_gene_review.etl.publication import accept_full_text

    real = "Genuine body prose about chemotaxis and the shikimate pathway. " * 20
    assert accept_full_text(real, False, _LANDING_PAGE_ABSTRACT) is False
    assert accept_full_text(None, True, _LANDING_PAGE_ABSTRACT) is False


def test_fetch_pubmed_data_actually_calls_the_guard():
    """The wiring, which the value tests above cannot see.

    Deleting the call site and setting ``full_text_available = is_complete`` again leaves
    every ``accept_full_text`` test passing -- the exact shape that let a dropped call site
    through earlier in this PR. ``fetch_pubmed_data`` needs Entrez to run, so the wiring is
    asserted against its source instead.
    """
    import inspect
    from ai_gene_review.etl import publication as pub

    src = inspect.getsource(pub.fetch_pubmed_data)
    assert "accept_full_text(" in src, "fetch_pubmed_data no longer routes through the guard"
    assert "full_text_available = full_text_result.is_complete" not in src, (
        "the unguarded assignment is back"
    )


def test_a_rejected_body_is_not_written_into_the_cache_file():
    """Judging the flag is not enough -- the rejected text must not reach `## Full Text`.

    `fetch_pubmed_data` assigned `publication.full_text` unconditionally and guarded only
    the flag, while `to_markdown` emits the section on truthiness. So a rejected fetch
    recorded `full_text_available: false` *and* wrote the landing page into the body that
    `supporting_text` quotes are matched against -- a quote lifted from it would verify
    verbatim. The warm path never had this gap: `apply_full_text` runs only on accept.
    """
    import inspect
    from ai_gene_review.etl import publication as pub

    src = inspect.getsource(pub.fetch_pubmed_data)
    assert "if accepted:" in src, "full_text must be written only when the guard passes"
    body = src.split("full_text_result = fetch_pmc_fulltext", 1)[1]
    guard_at = body.index("if accepted:")
    assign_at = body.index("publication.full_text = full_text_result.content")
    assert guard_at < assign_at, "the assignment must sit inside the accept branch"


def test_the_doi_converter_respects_an_explicit_false(tmp_path):
    """The third writer. It derived the flag from content_type and ignored the explicit key.

    Four cached records were marked `full_text_available: false` by hand because their
    bodies are openalex landing pages plus RIS exports; two are `content_type:
    full_text_html`, so one `just convert-doi-publications` would have written `true`
    straight back over that judgement -- and lifted the RIS dump into the new record's
    `abstract`.
    """
    from ai_gene_review.etl.publication import convert_doi_publication

    src = tmp_path / "DOI_10.1234_x.md"
    src.write_text(
        "---\ndoi: 10.1234/x\npmid: '999999'\ntitle: t\n"
        "content_type: full_text_html\nfull_text_available: false\n---\n\n"
        "## Content\n\nTY  - JOUR\n\nER  -\n"
    )
    # pmid passed explicitly so the converter does not need to resolve the DOI over the
    # network. (An earlier version of this assertion was `is not False or True`, which is
    # a tautology -- it would have passed however the converter behaved.)
    assert convert_doi_publication(src, tmp_path, pmid="999999") is True

    out = tmp_path / "PMID_999999.md"
    assert out.exists(), "converter did not write the PMID record"
    assert "full_text_available: false" in out.read_text(), (
        "an explicit false must win over content_type"
    )


def test_the_doi_converter_still_derives_the_flag_when_unstated(tmp_path):
    """Without an explicit key it falls back to content_type, via the shared constant."""
    from ai_gene_review.etl.publication import convert_doi_publication

    src = tmp_path / "DOI_10.1234_y.md"
    src.write_text(
        "---\ndoi: 10.1234/y\npmid: '999998'\ntitle: t\n"
        "content_type: full_text_html\n---\n\n## Content\n\nReal body prose here.\n"
    )
    assert convert_doi_publication(src, tmp_path, pmid="999998") is True
    assert "full_text_available: true" in (tmp_path / "PMID_999998.md").read_text()


def test_the_doi_converter_does_not_lift_a_citation_dump_into_the_abstract(tmp_path):
    """The second harm, named in a commit message and then not fixed.

    `to_markdown` emits the lifted `## Content` as `## Abstract` with no availability test,
    and for an abstract-only record the validator tells authors to "quote a verbatim
    substring of the cached abstract" -- so a citation export lifted here becomes quotable
    and a quote from its `N2  -` line verifies. Conversion also drops `content_type`,
    `full_text_provider`, `full_text_url` and `oa_status`, so the marker is the last signal
    left that the body is junk.
    """
    from ai_gene_review.etl.publication import convert_doi_publication

    src = tmp_path / "DOI_10.1234_z.md"
    src.write_text(
        "---\ndoi: 10.1234/z\npmid: '999997'\ntitle: t\n"
        "content_type: full_text_html\nfull_text_available: false\n---\n\n"
        f"## Content\n\n{_LANDING_PAGE_BODY}\n"
    )
    assert convert_doi_publication(src, tmp_path, pmid="999997") is True
    out = (tmp_path / "PMID_999997.md").read_text()
    assert "TY  - JOUR" not in out, "a citation export must not become the abstract"
    assert "Research output:Contribution to journal" not in out
    # The strip is partial, not all-or-nothing: this fixture's landing page carries the
    # paper's real abstract alongside the junk, and keeping the paper's own words is
    # strictly better than discarding the section. What must not survive is the export.
    assert "metabolically versatile saprophytic soil bacterium" in out


def test_the_doi_converter_still_lifts_a_real_abstract(tmp_path):
    """Narrow: genuine `## Content` prose is still carried across."""
    from ai_gene_review.etl.publication import convert_doi_publication

    src = tmp_path / "DOI_10.1234_w.md"
    src.write_text(
        "---\ndoi: 10.1234/w\npmid: '999996'\ntitle: t\ncontent_type: abstract_only\n---\n\n"
        "## Content\n\nWe show that CheZ accelerates dephosphorylation of CheY-P.\n"
    )
    assert convert_doi_publication(src, tmp_path, pmid="999996") is True
    assert "accelerates dephosphorylation" in (tmp_path / "PMID_999996.md").read_text()


def test_a_null_content_type_fails_closed(tmp_path):
    """`str(None).lower()` is "none", which is not in the negative list -- so it failed open."""
    from ai_gene_review.etl.publication import convert_doi_publication

    src = tmp_path / "DOI_10.1234_v.md"
    src.write_text(
        "---\ndoi: 10.1234/v\npmid: '999995'\ntitle: t\ncontent_type:\n---\n\n"
        "## Content\n\nSome prose.\n"
    )
    assert convert_doi_publication(src, tmp_path, pmid="999995") is True
    assert "full_text_available: false" in (tmp_path / "PMID_999995.md").read_text()


def test_the_converter_puts_full_text_under_full_text_not_abstract(tmp_path):
    """A converted record must not claim full text and then hide it under `## Abstract`.

    `## Content` is "the text we have"; `content_type` says which kind. Routing it always
    to `abstract` produced a record that `cached_full_text_available` called complete and
    `publication_warm` (`bool(flag) and FULL_TEXT_HEADER in body`) called a candidate for
    re-fetching -- two consumers disagreeing about one record. Found by self-audit.
    """
    from ai_gene_review.etl.publication import convert_doi_publication
    from ai_gene_review.etl.publication_warm import FULL_TEXT_HEADER

    src = tmp_path / "DOI_10.1234_a.md"
    src.write_text(
        "---\ndoi: 10.1234/a\npmid: '999994'\ntitle: t\ncontent_type: full_text_pdf\n---\n\n"
        "## Content\n\nThe complete article text, several paragraphs of it.\n"
    )
    assert convert_doi_publication(src, tmp_path, pmid="999994") is True
    out = (tmp_path / "PMID_999994.md").read_text()

    assert "full_text_available: true" in out
    assert FULL_TEXT_HEADER in out, "a record claiming full text must carry the section"
    assert "The complete article text" in out.split(FULL_TEXT_HEADER, 1)[1]
    # and the two consumers now agree
    body = out.split("---", 2)[-1]
    assert bool("full_text_available: true" in out) and (FULL_TEXT_HEADER in body)


def test_the_converter_keeps_an_abstract_only_record_as_an_abstract(tmp_path):
    """The other branch: abstract_only content stays in `## Abstract`, no full-text claim."""
    from ai_gene_review.etl.publication import convert_doi_publication
    from ai_gene_review.etl.publication_warm import FULL_TEXT_HEADER

    src = tmp_path / "DOI_10.1234_b.md"
    src.write_text(
        "---\ndoi: 10.1234/b\npmid: '999993'\ntitle: t\ncontent_type: abstract_only\n---\n\n"
        "## Content\n\nA short abstract about CheZ.\n"
    )
    assert convert_doi_publication(src, tmp_path, pmid="999993") is True
    out = (tmp_path / "PMID_999993.md").read_text()
    assert "full_text_available: false" in out
    assert FULL_TEXT_HEADER not in out
    assert "A short abstract about CheZ." in out


def test_writing_a_record_invalidates_the_memoised_reads(tmp_path):
    """The hazard closed end to end, not just "the helper exists".

    The validation-side predicates are lru_cached filesystem reads with no invalidation,
    so repairing a record and re-validating in the same process returned the pre-repair
    answer. That is exactly the sequence this PR ran over six stub records; it escaped only
    because the steps happened to be separate processes. Every writer of a publications/
    record now invalidates.
    """
    from ai_gene_review.etl.publication_warm import _rewrite
    from ai_gene_review.validation.supporting_text import (
        cached_full_text_available,
        clear_publication_caches,
    )

    clear_publication_caches()
    pubs = tmp_path
    rec = pubs / "PMID_5.md"
    rec.write_text("---\npmid: '5'\ntitle: t\nfull_text_available: false\n---\n\n## Abstract\n\na\n")

    assert cached_full_text_available("PMID:5", pubs) is False  # warms the cache

    _rewrite(rec, {"pmid": "5", "title": "t", "full_text_available": True},
             "\n\n## Abstract\n\na\n\n## Full Text\n\nreal body\n")

    assert cached_full_text_available("PMID:5", pubs) is True, (
        "a repaired record must be visible to the very next read in the same process"
    )


def test_every_publications_writer_invalidates():
    """Wiring, which the behavioural test above cannot see for the other three sites."""
    import inspect
    from ai_gene_review.etl import publication as pub
    from ai_gene_review.etl import publication_warm as warm

    # _rewrite is publication_warm's single write point; mark_attempted and
    # apply_full_text both go through it.
    for fn in (
        pub.fetch_pubmed_data,  # an independent write site, reached through none of the others
        pub.cache_publication,
        pub.convert_doi_publication,
        warm._rewrite,
    ):
        assert "clear_publication_caches()" in inspect.getsource(fn), (
            f"{fn.__name__} writes a publications/ record without invalidating"
        )


def test_the_converter_reject_path_does_not_claim_full_text(tmp_path):
    """The defect fixed on the accept path was still live on the reject path.

    `full_text_available` is decided from `content_type` before the lift is inspected and
    was never revised, so a rejected `## Content` left the flag `true`, `full_text` unset
    and the abstract as "No abstract available." -- bit-for-bit the record the previous
    commit set out to eliminate, except with no text at all. `cached_record_has_no_body`
    cannot see it either: that body is neither empty nor the literal stub signature.
    """
    from ai_gene_review.etl.publication import convert_doi_publication

    src = tmp_path / "DOI_10.1234_c.md"
    src.write_text(
        "---\ndoi: 10.1234/c\npmid: '999992'\ntitle: t\ncontent_type: full_text_html\n---\n\n"
        "## Content\n\nTY  - JOUR\n\nAU  - Someone\n\nER  -\n"
    )
    assert convert_doi_publication(src, tmp_path, pmid="999992") is True
    out = (tmp_path / "PMID_999992.md").read_text()
    assert "full_text_available: false" in out, (
        "nothing survived the strip, so the record has no full text"
    )
    assert "## Full Text" not in out


def test_the_strip_keeps_the_papers_own_abstract(tmp_path):
    """All-or-nothing rejection discarded genuine prose sitting beside the junk."""
    from ai_gene_review.etl.publication import _strip_stub_lines, _carries_stub_marker

    mixed = (
        "SUMMARY\nNucleotide-derived second messengers are present in all domains of life.\n\n"
        "Research output:Contribution to journal\u203aArticle\n\n}\n\n"
        "TY  - JOUR\n\nAU  - Someone\n\nER  -\n"
    )
    kept = _strip_stub_lines(mixed)
    assert "Nucleotide-derived second messengers" in kept
    assert not _carries_stub_marker(kept)
    assert "TY  - JOUR" not in kept and "}" not in kept


def test_a_forced_refetch_refreshes_metadata_and_keeps_a_vouched_body(tmp_path):
    """The skip was keyed on presence, not quality, so 888 records could never refresh.

    Those records are `full_text_available: false` while carrying a `## Full Text`
    section; a forced re-fetch wrote nothing at all for them -- not the body and not the
    metadata -- while returning True. Gate on the record's own verdict instead.
    """
    from ai_gene_review.etl.publication import _existing_accepted_full_text

    good = tmp_path / "PMID_1.md"
    good.write_text(
        "---\npmid: '1'\nfull_text_available: true\nfull_text_extraction_method: xml\n"
        "full_text_provider: pmc\noa_status: gold\nlicense: CC-BY\n---\n\n"
        "## Abstract\n\na\n\n## Full Text\n\nA genuine body.\n"
    )
    text, method, provenance = _existing_accepted_full_text(good)
    assert text == "A genuine body." and method == "xml"
    # the body's provenance travels with it -- `license` governs redistribution of the
    # very text being preserved, and the previous skip-the-write kept it by accident.
    assert provenance == {
        "full_text_provider": "pmc",
        "oa_status": "gold",
        "license": "CC-BY",
    }

    # the 888 shape: a section present, but the record does not vouch for it
    rejected = tmp_path / "PMID_2.md"
    rejected.write_text(
        "---\npmid: '2'\nfull_text_available: false\n---\n\n"
        "## Abstract\n\na\n\n## Full Text\n\nAbstract\n\na\n"
    )
    assert _existing_accepted_full_text(rejected) == (None, None, {})


def test_a_stripped_section_is_abstract_grade_not_full_text(tmp_path):
    """The strip's survivor must not be promoted to `full_text`.

    Revising the derived flag only `if not content` made the revision unreachable whenever
    prose survived -- which is the strip's entire purpose. A section that needed stripping
    was a landing page, so its residue is at best abstract-grade; on the live records the
    residue IS the abstract. `is_usable_full_text` has three rejection criteria and this
    converter can apply only the marker list; "contained in the cached abstract" and "adds
    less than MIN_FULL_TEXT_CHARS" are exactly what a stripped landing page fails.
    """
    from ai_gene_review.etl.publication import convert_doi_publication

    src = tmp_path / "DOI_10.1234_d.md"
    src.write_text(
        "---\ndoi: 10.1234/d\npmid: '999991'\ntitle: t\ncontent_type: full_text_html\n---\n\n"
        "## Content\n\nSUMMARY\nReal abstract prose about second messengers.\n\n"
        "Research output:Contribution to journal\n\nTY  - JOUR\n\nER  -\n"
    )
    assert convert_doi_publication(src, tmp_path, pmid="999991") is True
    out = (tmp_path / "PMID_999991.md").read_text()

    assert "full_text_available: false" in out, "a stripped landing page is not full text"
    assert "## Full Text" not in out
    assert "Real abstract prose about second messengers." in out, "the prose is kept"
    assert "TY  - JOUR" not in out


def test_cache_publication_keeps_a_good_body_when_the_refetch_is_rejected(tmp_path, monkeypatch):
    """Pin the carry-forward end to end: body kept, metadata refreshed, provenance carried.

    What this test does **not** cover, stated plainly because an earlier version of this
    docstring claimed otherwise: it cannot see the `use_cache` collision that made the
    carry-forward dead in production. It monkeypatches `fetch_pubmed_data`, so no inner
    write happens whichever kwargs the call site passes -- restore
    `fetch_pubmed_data(pmid)` and all four assertions below still pass. Only
    `test_cache_publication_does_not_let_the_fetch_write_the_record` fails on that
    mutation, and the two tests are only jointly sufficient.

    What it does cover, which the earlier helper-level test did not: delete the
    carry-forward block and `"A genuine cached body." in out` fails.
    """
    from types import SimpleNamespace
    import ai_gene_review.etl.publication as pub

    existing = tmp_path / "PMID_3.md"
    existing.write_text(
        "---\npmid: '3'\ntitle: old\nfull_text_available: true\n"
        "full_text_extraction_method: xml\nlicense: CC-BY\n---\n\n"
        "## Abstract\n\nold abstract\n\n## Full Text\n\nA genuine cached body.\n"
    )

    rejected = pub.Publication(
        pmid="3", title="refreshed title", authors=["A"], journal="j", year="2020",
        abstract="refreshed abstract", full_text=None, full_text_available=False,
    )
    monkeypatch.setattr(pub, "fetch_pubmed_data", lambda pmid, **kw: rejected, raising=False)

    assert pub.cache_publication("3", output_dir=tmp_path, force=True) is True
    out = existing.read_text()

    assert "A genuine cached body." in out, "the good body must survive a rejected re-fetch"
    assert "refreshed title" in out, "and the metadata must still be refreshed"
    assert "license: CC-BY" in out, "with the body's provenance"
    assert "full_text_available: true" in out


def test_cache_publication_does_not_let_the_fetch_write_the_record(tmp_path):
    """Wiring: the inner write must stay off, or the guard above is unreachable again.

    This is the **only** test that catches the collision. `fetch_pubmed_data` defaults to
    `use_cache=True, cache_dir=Path("publications")` -- the same file `cache_publication`
    is about to write -- so calling it without the kwarg overwrote the record before the
    carry-forward guard could read it, making two commits' worth of fixes inert on the
    path `validator.py` recommends.

    Asserted against the source because exercising it needs Entrez, and because the
    behavioural test above stubs `fetch_pubmed_data` and therefore cannot observe which
    kwargs it receives. If this assertion is ever deleted as brittle, the collision
    becomes silently reintroducible -- nothing else would notice.
    """
    import inspect
    import ai_gene_review.etl.publication as pub

    src = inspect.getsource(pub.cache_publication)
    assert "fetch_pubmed_data(pmid, use_cache=False)" in src, (
        "the inner write would overwrite the record before the carry-forward reads it"
    )


def test_the_carry_forward_keeps_the_whole_body(tmp_path):
    """No truncation at the next `## ` -- every such line inside the section is content.

    Both writers append `## Full Text` LAST (`to_markdown` emits Abstract then Full Text
    and stops; `apply_full_text` rstrips and appends), so a `## ` inside it is never a
    sibling heading. Cutting there dropped 61% of `PMID_26063905` at the extractor's own
    `## Results (full text retrieved from PMC HTML, ...)` label and 62% of
    `PMID_37865089` at a `## Splitting 50 PDBs...` shell comment in a code listing -- in
    the function whose entire purpose is preserving that body.
    """
    from ai_gene_review.etl.publication import _existing_accepted_full_text

    rec = tmp_path / "PMID_9.md"
    rec.write_text(
        "---\npmid: '9'\nfull_text_available: true\n---\n\n"
        "## Abstract\n\nabs\n\n"
        "## Full Text\n\nIntroduction prose.\n\n"
        "## Results (full text retrieved from PMC HTML, PMC1)\n\nThe results section.\n"
    )
    text, _, _ = _existing_accepted_full_text(rec)
    assert "Introduction prose." in text
    assert "The results section." in text, "the tail after an inner ## must survive"
    assert "## Results (full text retrieved" in text


def test_the_section_finder_ignores_a_deeper_heading(tmp_path):
    """`body.find("## Full Text")` also matches inside `### Full Text Notes`.

    It lands on the `## Full Text` at offset one, and `apply_full_text` truncates there --
    destroying everything between that point and the real section. Same
    substring-for-structure shape as the truncation removed from
    `_existing_accepted_full_text`; this is the sibling function, which writes the section
    that one reads. Pre-existing and unreachable from the data today, fixed because it is
    the same bug one function over in a file this change already touches.
    """
    from ai_gene_review.etl.publication_warm import _full_text_section_start

    body = "## Abstract\n\nabs\n\n### Full Text Notes\n\nx\n\n## Full Text\n\nreal body\n"
    i = _full_text_section_start(body)
    assert body[i:].startswith("## Full Text\n\nreal body"), "must find the real section"
    assert "### Full Text Notes" in body[:i], "the deeper heading stays in the kept prefix"

    assert _full_text_section_start("## Full Text\n\nb\n") == 0
    assert _full_text_section_start("## Abstract\n\na\n") == -1


def test_apply_full_text_replaces_only_the_real_section(tmp_path):
    """End to end: a deeper heading before the section must survive the rewrite."""
    from ai_gene_review.etl.publication_warm import apply_full_text

    rec = tmp_path / "PMID_11.md"
    rec.write_text(
        "---\npmid: '11'\nfull_text_available: false\n---\n\n"
        "## Abstract\n\nabs\n\n### Full Text Notes\n\nkeep me\n\n"
        "## Full Text\n\nold body\n"
    )
    frontmatter = {"pmid": "11", "full_text_available": False}
    body = rec.read_text().split("---", 2)[2]
    apply_full_text(
        rec,
        frontmatter,
        body,
        text="brand new body text",
        extraction_method="xml",
        provider="pmc",
    )
    out = rec.read_text()
    assert "keep me" in out, "content before the section must not be truncated away"
    assert "brand new body text" in out
    assert "old body" not in out
