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
    listed = check_document(doc, yaml_file, baseline={key: {quote_digest(TP53, bad)}})
    assert [r.blocking for r in unlisted] == [True]
    assert [(r.blocking, r.baselined) for r in listed] == [(False, True)]


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
    for prefix in ("modules/", "interpro/panther/", "gocams/", "rules/", "projects/"):
        assert any(r.startswith(prefix) for r in rel), prefix
    assert not any(r.endswith("-ai-review.yaml") and r.startswith("genes/") for r in rel)
    assert not any("recapitulation-experiment" in r for r in rel)
