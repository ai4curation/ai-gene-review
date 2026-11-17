"""Exercise refresh with real LTV and a local ontology; no network or mocks."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.tools.ontology_cache_coverage import DocumentKind
from ai_gene_review.tools.ontology_cache_refresh import refresh


@pytest.fixture
def corpus(tmp_path: Path):
    """A tiny ontology and LinkML binding, with a deliberately stale label cache."""
    ontology = tmp_path / "test.obo"
    ontology.write_text(
        "format-version: 1.2\nontology: test\n\n"
        "[Term]\nid: TEST:0\nname: root\n\n"
        "[Term]\nid: TEST:1\nname: current label\nis_a: TEST:0 ! root\n\n"
        "[Term]\nid: TEST:2\nname: outside the closure\n"
    )
    config = tmp_path / "oak.yaml"
    config.write_text(
        yaml.safe_dump({"ontology_adapters": {"TEST": f"simpleobo:{ontology}"}})
    )
    schema = tmp_path / "schema.yaml"
    schema.write_text("""id: https://example.org/refresh
name: refresh
imports: [linkml:types]
prefixes:
  linkml: https://w3id.org/linkml/
  TEST: http://purl.obolibrary.org/obo/TEST_
  refresh: https://example.org/refresh/
default_prefix: refresh
classes:
  Record:
    attributes:
      term:
        range: Term
        inlined: true
        bindings:
        - range: TestEnum
          binds_value_of: id
  Term:
    attributes:
      id:
        range: uriorcurie
      label:
        range: string
enums:
  TestEnum:
    reachable_from:
      source_nodes: [TEST:0]
      relationship_types: [rdfs:subClassOf]
      include_self: true
""")
    record = tmp_path / "one-ai-review.yaml"
    record.write_text("term: {id: 'TEST:1', label: current label}\n")
    cache = tmp_path / "cache"
    (cache / "test").mkdir(parents=True)
    (cache / "test/terms.csv").write_text(
        "curie,label,retrieved_at\nTEST:1,stale label,2020-01-01\n"
    )
    (cache / "unrelated.txt").write_text("preserve this other cache\n")
    return dict(
        grouped={DocumentKind(schema, "Record"): [record]},
        root=tmp_path,
        cache_dir=cache,
        output_dir=tmp_path / "report",
        oak_config=config,
        attempts=1,
        timeout=30.0,
    )


def snapshot(folder: Path) -> dict[str, bytes]:
    """Read all retained bytes to detect any change on unsuccessful refreshes."""
    return {
        p.relative_to(folder).as_posix(): p.read_bytes()
        for p in folder.rglob("*")
        if p.is_file()
    }


def test_refresh_rechecks_stale_labels_and_verifies_membership(corpus):
    before = snapshot(corpus["cache_dir"])
    report = refresh(**corpus)
    assert report["ready"] is True
    assert report["offline"]["covered"] is True
    assert report["offline"]["complete"] is True
    assert snapshot(corpus["cache_dir"]) == before  # preview is read-only
    assert report["changes"]["labels_changed"] == [
        {"curie": "TEST:1", "before": "stale label", "after": "current label"}
    ]
    assert report["changes"]["enum_memberships_added"] == 1
    assert report["provenance"]["local_sources"][0]["sha256"]
    candidate = corpus["output_dir"] / "candidate-cache"
    assert "stale label" not in (candidate / "test/terms.csv").read_text()
    assert not list(candidate.rglob("*.complete"))


def test_apply_preserves_unrelated_files_and_avoids_timestamp_only_churn(corpus):
    first = refresh(**corpus, apply=True)
    assert first["applied"] is True
    cache = corpus["cache_dir"]
    assert (cache / "unrelated.txt").read_text() == "preserve this other cache\n"
    before = snapshot(cache)
    corpus["output_dir"] = corpus["root"] / "second-report"
    second = refresh(**corpus, apply=True)
    assert second["ready"] is True
    assert second["changed_files"] == []
    assert snapshot(cache) == before


def test_refresh_does_not_reuse_stale_positive_membership(corpus):
    assert refresh(**corpus, apply=True)["ready"]
    before = snapshot(corpus["cache_dir"])
    ontology = corpus["root"] / "test.obo"
    ontology.write_text(ontology.read_text().replace("is_a: TEST:0 ! root\n", ""))
    corpus["output_dir"] = corpus["root"] / "changed-ontology"
    report = refresh(**corpus, apply=True)
    assert not report["ready"]
    assert report["offline"]["missing_enum_memberships"]
    assert snapshot(corpus["cache_dir"]) == before


def test_refreshed_partial_enum_drops_old_complete_marker(corpus):
    assert refresh(**corpus, apply=True)["ready"]
    enum = next((corpus["cache_dir"] / "enums").glob("*.csv"))
    enum.with_suffix(".csv.complete").touch()
    corpus["output_dir"] = corpus["root"] / "second-report"
    assert refresh(**corpus, apply=True)["ready"]
    assert not enum.with_suffix(".csv.complete").exists()


@pytest.mark.parametrize(
    "content",
    [
        "term: {id: 'TEST:2', label: outside the closure}\n",
        "term: {id: 'TEST:1', label: [\n",
    ],
)
def test_invalid_or_unreadable_input_never_replaces_retained_cache(corpus, content):
    record = next(iter(corpus["grouped"].values()))[0]
    record.write_text(content)
    before = snapshot(corpus["cache_dir"])
    report = refresh(**corpus, apply=True)
    assert report["ready"] is False
    assert report["applied"] is False
    assert snapshot(corpus["cache_dir"]) == before
    assert (corpus["output_dir"] / "report.yaml").exists()


def test_timeout_retains_cache_and_records_failure(corpus):
    corpus["timeout"] = 0.000001
    before = snapshot(corpus["cache_dir"])
    report = refresh(**corpus, apply=True)
    assert not report["ready"]
    assert report["failures"][0]["reason"] == "timeout"
    assert snapshot(corpus["cache_dir"]) == before


def test_empty_input_cannot_produce_a_successful_refresh(corpus):
    corpus["grouped"] = {}
    with pytest.raises(ValueError, match="No review files"):
        refresh(**corpus, apply=True)


def test_output_may_not_overlap_retained_cache(corpus):
    corpus["output_dir"] = corpus["cache_dir"] / "report"
    with pytest.raises(ValueError, match="overlap"):
        refresh(**corpus, apply=True)
