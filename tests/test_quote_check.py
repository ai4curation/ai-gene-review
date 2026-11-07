"""Tests for the document-kind-independent quote check (issue #6021).

They run against real files in the repository (UniProt flat files, cached Reactome
entries, cached publications), so they exercise the same matcher validation uses.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.local_source_text import PROJECT_ROOT, quote_digest
from ai_gene_review.validation.quote_check import (
    Outcome,
    Quote,
    check_document,
    check_quote,
    default_files,
    iter_quotes,
    load_baseline,
    main,
)

TP53 = "file:human/TP53/TP53-uniprot.txt"
GOOD_TP53 = "Nucleus. Cytoplasm. Note=Predominantly nuclear but localizes to the cytoplasm"


@pytest.mark.parametrize(
    "reference_id,text,outcome",
    [
        (TP53, GOOD_TP53, Outcome.VERIFIED),
        (TP53, "a sentence that is in no UniProt record", Outcome.NOT_FOUND),
        ("Reactome:R-HSA-73912", "catalyzes the reversible reaction of acetoacetate", Outcome.VERIFIED),
        ("Reactome:R-HSA-0", "anything", Outcome.UNRESOLVED),
        ("file:does/not/exist.md", "anything", Outcome.UNRESOLVED),
        ("url:https://example.org", "anything", Outcome.UNCHECKED),
        ("GO:0005515", "anything", Outcome.UNCHECKED),
        (None, "anything", Outcome.UNCHECKED),
    ],
)
def test_check_quote_outcomes(reference_id, text, outcome):
    assert check_quote(Quote("x", reference_id, text)).outcome is outcome


@pytest.mark.integration
@pytest.mark.parametrize(
    "text,outcome",
    [
        ("Bmp4 homozygous null embryos contain no PGCs", Outcome.VERIFIED),
        ("this fabricated sentence appears in no abstract", Outcome.NOT_FOUND),
    ],
)
def test_check_quote_literature(text, outcome):
    pytest.importorskip("linkml_reference_validator")
    if not (PROJECT_ROOT / "publications" / "PMID_10049358.md").exists():
        pytest.skip("cached publication PMID_10049358 not present")
    assert check_quote(Quote("x", "PMID:10049358", text)).outcome is outcome


def test_iter_quotes_finds_every_slot_kind():
    """source_id, reference_id, reference and inherited findings ids are all read."""
    doc = {
        "references": [{"id": "PMID:1", "findings": [{"supporting_text": "a"}]}],
        "activity_reviews": [{"evidence": [{"source_id": "PMID:2", "supporting_text": "b"}]}],
        "node_assessments": [{"supported_by": [{"reference_id": "file:x", "supporting_text": "c"}]}],
        "items": [{"reference": "PMID:3", "supporting_text": "d"}],
        "empty": [{"reference_id": "PMID:4", "supporting_text": "  "}],
    }
    assert [(q.reference_id, q.text) for q in iter_quotes(doc)] == [
        ("PMID:1", "a"),
        ("PMID:2", "b"),
        ("file:x", "c"),
        ("PMID:3", "d"),
    ]


def test_baselined_failure_warns_instead_of_blocking(tmp_path):
    bad = "a sentence that is in no UniProt record"
    doc = {"evidence": [{"source_id": TP53, "supporting_text": bad}]}
    yaml_file = PROJECT_ROOT / "modules" / "x.yaml"  # key only; not read
    key = "modules/x.yaml"
    unlisted = check_document(doc, yaml_file, baseline={})
    listed = check_document(
        doc, yaml_file, baseline={key: {"not_found": {quote_digest(TP53, bad)}}}
    )
    assert [r.blocking for r in unlisted] == [True]
    assert [(r.blocking, r.baselined) for r in listed] == [(False, True)]


def test_baseline_entry_only_covers_its_own_outcome():
    """A quote baselined as unresolved blocks once its source exists but lacks it."""
    bad = "a sentence that is in no UniProt record"
    doc = {"evidence": [{"source_id": TP53, "supporting_text": bad}]}
    yaml_file = PROJECT_ROOT / "modules" / "x.yaml"
    results = check_document(
        doc, yaml_file, baseline={"modules/x.yaml": {"unresolved": {quote_digest(TP53, bad)}}}
    )
    assert [(r.outcome, r.blocking) for r in results] == [(Outcome.NOT_FOUND, True)]


def test_init_baseline_refuses_partial_scope_and_existing_file(tmp_path, monkeypatch):
    """--init-baseline cannot shrink the scope or overwrite a baseline (it only shrinks)."""
    good = tmp_path / "good.yaml"
    good.write_text(yaml.safe_dump({"evidence": [{"source_id": TP53, "supporting_text": GOOD_TP53}]}))
    with pytest.raises(SystemExit):
        main(["--init-baseline", str(good)])
    existing = tmp_path / "baseline.yaml"
    existing.write_text("entries: {}\n")
    monkeypatch.setattr("ai_gene_review.validation.quote_check.BASELINE_PATH", existing)
    with pytest.raises(SystemExit):
        main(["--init-baseline"])
    assert existing.read_text() == "entries: {}\n"


def test_committed_baseline_uses_known_outcomes():
    """Every committed entry is filed under not_found or unresolved."""
    baseline = load_baseline()
    assert baseline, "conf/quote_check_baseline.yaml should exist"
    assert all(set(v) <= {"not_found", "unresolved"} for v in baseline.values())


def test_main_exit_code(tmp_path: Path):
    good = tmp_path / "good.yaml"
    good.write_text(yaml.safe_dump({"evidence": [{"source_id": TP53, "supporting_text": GOOD_TP53}]}))
    bad = tmp_path / "bad.yaml"
    bad.write_text(yaml.safe_dump({"evidence": [{"source_id": TP53, "supporting_text": "invented"}]}))
    assert main([str(good)]) == 0
    assert main([str(bad)]) == 1


def test_default_scope_covers_every_non_gene_review_kind():
    """The gate reaches modules, families, GO-CAM reviews, rules and projects."""
    rel = {p.relative_to(PROJECT_ROOT).as_posix() for p in default_files()}
    for prefix in ("modules/", "interpro/panther/", "interpro/pfam/", "gocams/", "rules/", "projects/"):
        assert any(r.startswith(prefix) for r in rel), prefix
    assert not any(r.endswith("-ai-review.yaml") and r.startswith("genes/") for r in rel)
    assert not any("recapitulation-experiment" in r for r in rel)


def test_main_reports_unparseable_yaml_and_fails(tmp_path: Path, capsys):
    bad = tmp_path / "broken.yaml"
    bad.write_text("key: [unclosed\n")
    assert main([str(bad)]) == 1
    out = capsys.readouterr().out
    assert "broken.yaml: not valid YAML" in out
    assert "(0 blocking, 0 baselined); 1 unparseable file;" in out


def test_prune_refuses_when_a_file_is_unparseable(tmp_path, monkeypatch, capsys):
    """Pruning with an unreadable file would drop that file's entries, so it refuses."""
    bad = tmp_path / "broken.yaml"
    bad.write_text("key: [unclosed\n")
    baseline = tmp_path / "baseline.yaml"
    baseline.write_text("entries:\n  broken.yaml:\n    not_found:\n    - abc\n")
    before = baseline.read_text()
    monkeypatch.setattr("ai_gene_review.validation.quote_check.BASELINE_PATH", baseline)
    monkeypatch.setattr("ai_gene_review.validation.quote_check.default_files", lambda: [bad])
    assert main(["--prune-baseline"]) == 1
    assert baseline.read_text() == before
    assert "Not pruning" in capsys.readouterr().out


def test_prune_writes_to_the_redirected_baseline(tmp_path, monkeypatch):
    """Redirecting BASELINE_PATH redirects the write, so guard tests cannot touch the real file."""
    bad_quote = "a sentence that is in no UniProt record"
    doc_file = tmp_path / "doc.yaml"
    doc_file.write_text(yaml.safe_dump({"evidence": [{"source_id": TP53, "supporting_text": bad_quote}]}))
    baseline = tmp_path / "baseline.yaml"
    key = "tmp/doc.yaml"
    baseline.write_text(yaml.safe_dump({"entries": {key: {"not_found": ["stale0000"]}}}))
    real = load_baseline()
    monkeypatch.setattr("ai_gene_review.validation.quote_check.BASELINE_PATH", baseline)
    monkeypatch.setattr("ai_gene_review.validation.quote_check.default_files", lambda: [doc_file])
    main(["--prune-baseline"])
    assert "stale0000" not in baseline.read_text()  # the redirected file was rewritten
    monkeypatch.undo()
    assert load_baseline() == real  # the committed baseline was not touched


def test_init_refuses_when_a_file_is_unparseable(tmp_path, monkeypatch, capsys):
    """A first --init-baseline over a scope with unreadable YAML writes nothing and fails."""
    bad = tmp_path / "broken.yaml"
    bad.write_text("key: [unclosed\n")
    baseline = tmp_path / "baseline.yaml"  # does not exist yet
    monkeypatch.setattr("ai_gene_review.validation.quote_check.BASELINE_PATH", baseline)
    monkeypatch.setattr("ai_gene_review.validation.quote_check.default_files", lambda: [bad])
    assert main(["--init-baseline"]) == 1
    assert not baseline.exists()
    assert "Not writing a baseline" in capsys.readouterr().out
