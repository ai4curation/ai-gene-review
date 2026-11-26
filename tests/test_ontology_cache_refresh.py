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
    assert report["changes"]["enum_memberships_added"] == 2  # root + used member
    assert report["provenance"]["local_sources"][0]["sha256"]
    candidate = corpus["output_dir"] / "candidate-cache"
    assert "stale label" not in (candidate / "test/terms.csv").read_text()
    assert len(list(candidate.rglob("*.complete"))) == 1


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
    assert any(
        "TEST:1" in str(finding) and "not in dynamic enum" in str(finding)
        for finding in report["offline"]["other_findings"]
    )
    assert report["changes"]["enum_memberships_removed"] == 1
    assert snapshot(corpus["cache_dir"]) == before


def test_full_refresh_replaces_old_marker_with_fresh_completion(corpus):
    assert refresh(**corpus, apply=True)["ready"]
    enum = next((corpus["cache_dir"] / "enums").glob("*.csv"))
    enum.with_suffix(".csv.complete").touch()
    corpus["output_dir"] = corpus["root"] / "second-report"
    assert refresh(**corpus, apply=True)["ready"]
    assert enum.with_suffix(".csv.complete").read_text(encoding="utf-8") == "complete\n"


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


def test_refresh_materializes_members_not_mentioned_in_the_corpus(corpus):
    ontology = corpus["root"] / "test.obo"
    with ontology.open("a", encoding="utf-8") as stream:
        for number in range(3, 53):
            stream.write(
                f"\n[Term]\nid: TEST:{number}\nname: unused {number}\nis_a: TEST:0 ! root\n"
            )
    report = refresh(**corpus)
    assert report["ready"]
    enum = next((corpus["output_dir"] / "candidate-cache/enums").glob("*.csv"))
    assert "TEST:52" in enum.read_text(encoding="utf-8")
    assert len(enum.read_text(encoding="utf-8").splitlines()) == 53
    assert enum.with_suffix(".csv.complete").is_file()


def test_membership_removal_requires_explicit_budget(corpus):
    assert refresh(**corpus, apply=True)["ready"]
    enum = next((corpus["cache_dir"] / "enums").glob("*.csv"))
    enum.write_text(enum.read_text(encoding="utf-8") + "TEST:2\n", encoding="utf-8")
    before = snapshot(corpus["cache_dir"])
    corpus["output_dir"] = corpus["root"] / "guarded"
    report = refresh(**corpus, apply=True)
    assert not report["ready"]
    assert report["changes"]["enum_memberships_removed"] == 1
    assert snapshot(corpus["cache_dir"]) == before
    assert "removed: **1**" in (corpus["output_dir"] / "summary.md").read_text(
        encoding="utf-8"
    )
    corpus["output_dir"] = corpus["root"] / "allowed"
    assert refresh(**corpus, apply=True, max_enum_removals=1)["applied"]
    assert "TEST:2" not in enum.read_text(encoding="utf-8")
    assert enum.with_suffix(".csv.complete").is_file()


def test_candidate_failure_still_writes_durable_report(corpus):
    (corpus["cache_dir"] / "test/terms.csv").write_text(
        "curie,wrong_header\nTEST:1,old\n", encoding="utf-8"
    )
    before = snapshot(corpus["cache_dir"])
    report = refresh(**corpus, apply=True)
    assert not report["ready"] and not report["applied"]
    assert any("Cache format changed" in f["reason"] for f in report["failures"])
    assert (corpus["output_dir"] / "report.yaml").is_file()
    assert "Cache format changed" in (corpus["output_dir"] / "summary.md").read_text(
        encoding="utf-8"
    )
    assert snapshot(corpus["cache_dir"]) == before


def test_total_runtime_budget_leaves_checkpoint_and_retains_cache(corpus):
    before = snapshot(corpus["cache_dir"])
    report = refresh(**corpus, apply=True, max_runtime=0.000001)
    assert not report["ready"] and not report["applied"]
    assert any("runtime budget" in f["reason"] for f in report["failures"])
    saved = yaml.safe_load(
        (corpus["output_dir"] / "report.yaml").read_text(encoding="utf-8")
    )
    assert saved["progress"]["batches_planned"] == 2
    assert saved["progress"]["batches_completed"] == 0
    assert snapshot(corpus["cache_dir"]) == before


def test_summary_keeps_label_changes_and_advisories(corpus):
    report = refresh(**corpus)
    assert report["ready"]
    summary = (corpus["output_dir"] / "summary.md").read_text(encoding="utf-8")
    for text in [
        "TEST:1",
        "stale label",
        "current label",
        "Advisory label mismatches",
        "Memberships added",
    ]:
        assert text in summary


def test_utf8_refresh_under_ascii_locale(corpus):
    import os
    import subprocess
    import sys

    ontology = corpus["root"] / "test.obo"
    ontology.write_text(
        ontology.read_text(encoding="utf-8").replace("current label", "caf\u00e9"),
        encoding="utf-8",
    )
    record = next(iter(corpus["grouped"].values()))[0]
    record.write_text("term: {id: 'TEST:1', label: caf\u00e9}\n", encoding="utf-8")
    program = """
import sys
from pathlib import Path
from ai_gene_review.tools.ontology_cache_coverage import DocumentKind
from ai_gene_review.tools.ontology_cache_refresh import refresh
root = Path(sys.argv[1])
r = refresh({DocumentKind(root/'schema.yaml', 'Record'): [root/'one-ai-review.yaml']},
    root=root, cache_dir=root/'cache', output_dir=root/'report', oak_config=root/'oak.yaml', attempts=1)
assert r['ready'], r['failures']
"""
    result = subprocess.run(
        [sys.executable, "-c", program, str(corpus["root"])],
        env={
            **os.environ,
            "LC_ALL": "C",
            "PYTHONUTF8": "0",
            "PYTHONCOERCECLOCALE": "0",
        },
        capture_output=True,
        encoding="utf-8",
        timeout=60,
    )
    assert result.returncode == 0, result.stderr
    assert "caf\u00e9" in (corpus["output_dir"] / "summary.md").read_text(
        encoding="utf-8"
    )
