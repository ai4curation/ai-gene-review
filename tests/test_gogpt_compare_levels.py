"""Regression tests for the canonicalized three-level GO-GPT comparison."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.gogpt_compare_levels import (
    build_comparison,
    get_core_terms_from_document,
    get_post_review_terms,
)
from scripts.gogpt_batch import (
    GoAspectResolutionError,
    LocalGoAspectResolver,
    load_go_adapter_spec,
    load_review_terms,
    preflight_review_terms,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


ASPECT_PREDICATES = ("oio:hasOBONamespace", "IAO:0100001")
MetadataStatement = tuple[str, str, object, object | None, dict[str, object]]


def metadata_statement(subject: str, predicate: str, value: object) -> MetadataStatement:
    return subject, predicate, value, None, {}


class FakeMetadataAdapter:
    def __init__(
        self,
        statements: list[MetadataStatement],
        error: Exception | None = None,
    ):
        self.statements = statements
        self.error = error
        self.calls: list[tuple[tuple[str, ...], tuple[str, ...], bool]] = []

    def entities_metadata_statements(
        self,
        curies: list[str],
        predicates: list[str] | None = None,
        include_nested_metadata: bool = False,
    ):
        curie_tuple = tuple(curies)
        predicate_tuple = tuple(predicates or [])
        self.calls.append((curie_tuple, predicate_tuple, include_nested_metadata))
        if self.error is not None:
            raise self.error
        for statement in self.statements:
            if statement[0] not in curie_tuple:
                continue
            if predicates is not None and statement[1] not in predicates:
                continue
            yield statement


def test_core_term_extraction_covers_every_go_valued_slot() -> None:
    review = {
        "core_functions": [
            {
                "molecular_function": {"id": "GO:0000001"},
                "contributes_to_molecular_function": {"id": "GO:0000002"},
                "directly_involved_in": [{"id": "GO:0000003"}],
                "in_complex": {"id": "GO:0000004"},
                "locations": [{"id": "GO:0000005"}],
            }
        ]
    }

    assert get_core_terms_from_document(review) == {
        "GO:0000001",
        "GO:0000002",
        "GO:0000003",
        "GO:0000004",
        "GO:0000005",
    }


def test_post_review_terms_include_new_go_terms_and_respect_exclusions(
    tmp_path: Path,
) -> None:
    review = tmp_path / "gene-ai-review.yaml"
    review.write_text(
        """
existing_annotations:
  - term: {id: GO:0000001}
    review: {action: NEW}
  - term: {id: GO:0000002}
    negated: true
    review: {action: NEW}
  - term: {id: TEMP:new-term}
    review: {action: NEW}
  - term: {id: GO:0000003}
    review: {action: REMOVE}
core_functions:
  - molecular_function: {id: GO:0000001}
    directly_involved_in: [{id: GO:0000004}]
"""
    )

    assert get_post_review_terms(review) == {"GO:0000001", "GO:0000004"}


def test_committed_three_level_report_matches_current_reviews() -> None:
    details, stats = build_comparison(REPO_ROOT)
    committed = json.loads(
        (REPO_ROOT / "reports/gogpt-comparison-levels.json").read_text()
    )

    assert committed == details
    assert len(details) == 299
    assert stats == {
        "goa": {"overlap": 1040, "total": 2960, "pred": 8871},
        # Upstream reviews moved these levels. The HdeB re-review retains
        # GO:0051082 as an explicit interim post-review/core term (+1 to both
        # post_review and core). Separately, surA now retains GO:0005515
        # post-review (+1 post_review only), while the HdeA comprehensive review
        # adds one post-review term and two GO-valued core slots without changing
        # either overlap count. The Spy comprehensive review adds two post-review
        # terms and two GO-valued core slots without changing either overlap count.
        # The CpxP comprehensive review adds one post-review term and two GO-valued
        # core slots, also without changing either overlap count. DnaJ removes two
        # net post-review terms and three predicted overlaps after
        # resolving miscited CAFA rows. Its core count and overlap stay unchanged:
        # evidence-backed GO:0001671 replaces overclaimed GO:0043335 in the core set.
        # surA, Spy, CpxP, DnaJ, DnaK, GroEL, RidA, and SecB advanced to COMPLETE,
        # moving the reference-status distribution 67->75 COMPLETE in the benchmark sidecars.
        # DnaK changes review classifications without changing the three overlap totals.
        # GroEL removes two net post-review terms and one predicted overlap after
        # narrowing broad cytoplasm to the directly supported cytosol term; its core
        # count and overlap stay unchanged.
        # RidA removes one net post-review term and one predicted overlap by narrowing
        # broad annotations and replacing obsolete terms with the specific isoleucine
        # process or the holdase NTR; its GO-valued core set and overlap stay unchanged.
        # SecB removes two net post-review terms and two predicted overlaps by narrowing
        # broad transport/localization annotations; its core set and overlap stay unchanged.
        # Skp removes one post-review/core term and one predicted overlap by replacing
        # generic folding with outer membrane assembly and treating homotrimerization
        # as non-core.
        # GOA is unaffected,
        # distinguishing upstream review edits from a comparison regression.
        "post_review": {"overlap": 852, "total": 2764, "pred": 8871},
        "core": {"overlap": 349, "total": 1230, "pred": 8871},
    }


def test_batch_reference_loader_uses_goa_aspects_and_core_slots(tmp_path: Path) -> None:
    goa = tmp_path / "gene-goa.tsv"
    goa.write_text(
        "GO TERM\tGO ASPECT\n"
        "GO:0000001\tmolecular_function\n"
        "GO:0000002\tbiological_process\n"
        "GO:0000003\tcellular_component\n"
    )
    review = tmp_path / "gene-ai-review.yaml"
    review.write_text(
        """
existing_annotations:
  - term: {id: GO:0000001}
    review: {action: ACCEPT}
  - term: {id: GO:0000002}
    review: {action: REMOVE}
  - term: {id: GO:0000003}
    review:
      action: MODIFY
      proposed_replacement_terms: [{id: GO:0000004}]
  - term: {id: GO:0000010}
    review: {action: NEW}
  - term: {id: GO:0000011}
    review: {action: NEW}
  - term: {id: GO:0000012}
    review: {action: NEW}
  - term: {id: GO:0000013}
    negated: true
    review: {action: NEW}
  - term: {id: TEMP:new-term}
    review: {action: NEW}
core_functions:
  - molecular_function: {id: GO:0000005}
    contributes_to_molecular_function: {id: GO:0000006}
    directly_involved_in: [{id: GO:0000007}]
    in_complex: {id: GO:0000008}
    locations: [{id: GO:0000009}]
"""
    )

    aspects = {
        "GO:0000010": "MF",
        "GO:0000011": "BP",
        "GO:0000012": "CC",
    }
    calls: list[str] = []

    def resolve(go_id: str) -> str | None:
        calls.append(go_id)
        return aspects.get(go_id)

    assert load_review_terms(review, goa, aspect_resolver=resolve) == {
        "MF": {"GO:0000001", "GO:0000005", "GO:0000006", "GO:0000010"},
        "BP": {"GO:0000007", "GO:0000011"},
        "CC": {"GO:0000004", "GO:0000008", "GO:0000009", "GO:0000012"},
    }
    assert calls == ["GO:0000010", "GO:0000011", "GO:0000012"]


def test_local_go_aspect_resolver_uses_namespace_and_obsolete_replacement() -> None:
    adapter = FakeMetadataAdapter(
        [
            metadata_statement(
                "GO:0000010", "oio:hasOBONamespace", "molecular_function"
            ),
            metadata_statement("GO:0000011", "IAO:0100001", "GO:0000012"),
            metadata_statement(
                "GO:0000012", "oio:hasOBONamespace", "legacy_namespace"
            ),
            metadata_statement("GO:0000012", "IAO:0100001", "GO:0000013"),
            metadata_statement(
                "GO:0000013", "oio:hasOBONamespace", "cellular_component"
            ),
        ]
    )
    resolver = LocalGoAspectResolver(adapter)

    assert resolver.resolve("GO:0000010") == "MF"
    assert resolver.resolve("GO:0000011") == "CC"
    assert resolver.resolve("GO:0000011") == "CC"
    assert adapter.calls == [
        (("GO:0000010",), ASPECT_PREDICATES, True),
        (("GO:0000011",), ASPECT_PREDICATES, True),
        (("GO:0000012",), ASPECT_PREDICATES, True),
        (("GO:0000013",), ASPECT_PREDICATES, True),
    ]


def test_local_go_aspect_resolver_prefers_own_namespace_and_ignores_consider() -> None:
    adapter = FakeMetadataAdapter(
        [
            metadata_statement(
                "GO:0000020", "oio:hasOBONamespace", "molecular_function"
            ),
            metadata_statement("GO:0000020", "IAO:0100001", "GO:0000021"),
            metadata_statement("GO:0000020", "oio:consider", "GO:0000022"),
            metadata_statement(
                "GO:0000021", "oio:hasOBONamespace", "cellular_component"
            ),
            metadata_statement("GO:0000023", "oio:consider", "GO:0000022"),
            metadata_statement(
                "GO:0000022", "oio:hasOBONamespace", "biological_process"
            ),
        ]
    )
    resolver = LocalGoAspectResolver(adapter)

    assert resolver.resolve("GO:0000020") == "MF"
    with pytest.raises(GoAspectResolutionError, match="Unable to resolve GO aspect"):
        resolver.resolve("GO:0000023")
    assert adapter.calls == [
        (("GO:0000020",), ASPECT_PREDICATES, True),
        (("GO:0000023",), ASPECT_PREDICATES, True),
    ]


def test_local_go_aspect_resolver_rejects_replacement_cycles() -> None:
    adapter = FakeMetadataAdapter(
        [
            metadata_statement("GO:0000030", "IAO:0100001", "GO:0000031"),
            metadata_statement("GO:0000031", "IAO:0100001", "GO:0000030"),
        ]
    )

    with pytest.raises(GoAspectResolutionError, match="GO replacement cycle"):
        LocalGoAspectResolver(adapter).resolve("GO:0000030")


def test_local_go_aspect_resolver_rejects_conflicting_namespaces() -> None:
    adapter = FakeMetadataAdapter(
        [
            metadata_statement(
                "GO:0000040", "oio:hasOBONamespace", "molecular_function"
            ),
            metadata_statement(
                "GO:0000040", "oio:hasOBONamespace", "biological_process"
            ),
        ]
    )

    with pytest.raises(GoAspectResolutionError, match="Conflicting GO aspects"):
        LocalGoAspectResolver(adapter).resolve("GO:0000040")


def test_local_go_aspect_resolver_rejects_multiple_replacements() -> None:
    adapter = FakeMetadataAdapter(
        [
            metadata_statement("GO:0000050", "IAO:0100001", "GO:0000051"),
            metadata_statement("GO:0000050", "IAO:0100001", "GO:0000052"),
        ]
    )

    with pytest.raises(
        GoAspectResolutionError, match="Multiple authoritative GO replacements"
    ):
        LocalGoAspectResolver(adapter).resolve("GO:0000050")


def test_local_go_aspect_resolver_caches_unresolved_terms() -> None:
    adapter = FakeMetadataAdapter([])
    resolver = LocalGoAspectResolver(adapter)

    for _ in range(2):
        with pytest.raises(GoAspectResolutionError, match="Unable to resolve GO aspect"):
            resolver.resolve("GO:0073163")
    assert adapter.calls == [(("GO:0073163",), ASPECT_PREDICATES, True)]


def test_local_go_aspect_resolver_wraps_adapter_errors() -> None:
    adapter = FakeMetadataAdapter([], error=OSError("local GO cache unavailable"))

    with pytest.raises(
        GoAspectResolutionError, match="Unable to query local GO metadata"
    ) as error:
        LocalGoAspectResolver(adapter).resolve("GO:0000060")
    assert isinstance(error.value.__cause__, OSError)


def test_go_adapter_spec_comes_from_repository_config(tmp_path: Path) -> None:
    config = tmp_path / "oak_config.yaml"
    config.write_text("ontology_adapters:\n  GO: sqlite:custom-go\n")

    assert load_go_adapter_spec(config) == "sqlite:custom-go"


def test_preflight_review_terms_adds_gene_context_to_resolution_errors(
    tmp_path: Path,
) -> None:
    review = tmp_path / "GENE-ai-review.yaml"
    review.write_text(
        """
existing_annotations:
  - term: {id: GO:0000010}
    review: {action: NEW}
"""
    )
    genes = [("TEST", "GENE", tmp_path / "GENE-uniprot.txt", review)]

    with pytest.raises(
        GoAspectResolutionError,
        match=r"TEST/GENE .*Unable to resolve GO aspect.*GO:0000010",
    ):
        preflight_review_terms(genes, lambda _go_id: None)


def test_preflight_review_terms_reports_and_skips_other_input_errors(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    review = tmp_path / "GENE-ai-review.yaml"
    review.write_text("existing_annotations: [\n")
    genes = [("TEST", "GENE", tmp_path / "GENE-uniprot.txt", review)]

    assert preflight_review_terms(genes, lambda _go_id: "MF") == {}
    assert "ERROR TEST/GENE" in capsys.readouterr().out


@pytest.mark.integration
@pytest.mark.vcr_skip
def test_local_go_aspect_resolver_matches_real_configured_oak_snapshot() -> None:
    resolver = LocalGoAspectResolver()

    assert resolver.resolve("GO:0016020") == "CC"
    assert resolver.resolve("GO:0003700") == "MF"
    assert resolver.resolve("GO:0006355") == "BP"


def test_batch_reference_loader_rejects_unresolved_new_go_term(
    tmp_path: Path,
) -> None:
    goa = tmp_path / "gene-goa.tsv"
    goa.write_text("GO TERM\tGO ASPECT\n")
    review = tmp_path / "gene-ai-review.yaml"
    review.write_text(
        """
existing_annotations:
  - term: {id: GO:0000010}
    review: {action: NEW}
"""
    )

    with pytest.raises(
        GoAspectResolutionError, match="Unable to resolve GO aspect.*GO:0000010"
    ):
        load_review_terms(review, goa, aspect_resolver=lambda _go_id: None)
