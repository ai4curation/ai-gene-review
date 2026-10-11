"""Tests for the verbatim check on file:/Reactome: supporting_text quotes.

These run against real files in the repository (UniProt flat files and cached
Reactome entries), so they exercise the same matcher and renderings that
validation uses.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation import ValidationSeverity, validate_gene_review
from ai_gene_review.validation.local_source_text import (
    CHECK_TYPE,
    PROJECT_ROOT,
    find_local_quote_failures,
    quote_matches,
)

TP53 = "file:human/TP53/TP53-uniprot.txt"
CDK5 = "file:human/CDK5/CDK5-uniprot.txt"
EDEM3 = "file:human/EDEM3/EDEM3-uniprot.txt"
BDH1_REACTION = "Reactome:R-HSA-73912"


def _review(supported_by: list, findings_ref: dict | None = None) -> dict:
    return {
        "id": "Q00000",
        "gene_symbol": "TEST",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": "Test gene.",
        "references": [findings_ref] if findings_ref else [],
        "core_functions": [{"description": "x", "supported_by": supported_by}],
    }


def _local_issues(tmp_path: Path, data: dict):
    path = tmp_path / "TEST-ai-review.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False))
    report = validate_gene_review(path, check_goa=False, check_supporting_text=False)
    return [i for i in report.issues if i.check_type == CHECK_TYPE]


@pytest.mark.parametrize(
    "reference_id,quote",
    [
        # Runs across UniProt's line wraps ("CC       " continuation prefixes).
        (EDEM3, "Involved in endoplasmic reticulum-associated degradation (ERAD). Accelerates the glycoprotein ERAD"),
        # Quoted with the flat-file line codes, i.e. the raw text.
        (EDEM3, "CC       (ERAD). Accelerates the glycoprotein ERAD by proteasomes"),
        # Rhea bracket notation, which the matcher would strip as an editorial note.
        (CDK5, "Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP"),
        # Continuous once the {ECO:...} evidence tag is dropped.
        (TP53, "Nucleus. Cytoplasm. Note=Predominantly nuclear but localizes to the cytoplasm"),
        # Elision with "...", as for publication quotes.
        (TP53, "SUBCELLULAR LOCATION: [Isoform 1]: Nucleus ... Note=Predominantly nuclear"),
        (BDH1_REACTION, "catalyzes the reversible reaction of acetoacetate with NADH + H+ to form"),
    ],
)
def test_verbatim_local_quotes_pass(tmp_path, reference_id, quote):
    issues = _local_issues(tmp_path, _review([{"reference_id": reference_id, "supporting_text": quote}]))
    assert issues == []


@pytest.mark.parametrize(
    "reference_id,quote",
    [
        (TP53, "TP53 is a deliberately invented sentence zzqq that is not in UniProt"),
        # Elides "[Isoform 1]:" without "..." -- a real failure pattern in the corpus.
        (TP53, "SUBCELLULAR LOCATION: Nucleus. Cytoplasm. Note=Predominantly nuclear"),
        (BDH1_REACTION, "BDH1 converts acetoacetate to an invented product zzqq"),
        ("file:human/EDEM3/EDEM3-deep-research-falcon.md", "[Falcon deep-research synthesis used for this annotation decision.]"),
    ],
)
def test_non_verbatim_local_quotes_are_errors(tmp_path, reference_id, quote):
    issues = _local_issues(tmp_path, _review([{"reference_id": reference_id, "supporting_text": quote}]))
    assert [i.severity for i in issues] == [ValidationSeverity.ERROR]
    assert "not a verbatim substring" in issues[0].message


def test_unresolvable_reactome_id_is_an_error(tmp_path):
    issues = _local_issues(
        tmp_path,
        _review([{"reference_id": "Reactome:R-HSA-0", "supporting_text": "anything"}]),
    )
    assert [i.severity for i in issues] == [ValidationSeverity.ERROR]
    assert "cache_reactome_pathway" in (issues[0].suggestion or "")


def test_reference_findings_inherit_the_parent_id(tmp_path):
    findings_ref = {
        "id": TP53,
        "title": "TP53 UniProt entry",
        "findings": [{"statement": "x", "supporting_text": "an invented finding quote zzqq"}],
    }
    issues = _local_issues(tmp_path, _review([], findings_ref))
    assert [i.path for i in issues] == ["references[0].findings[0].supporting_text"]


def test_edited_source_is_reread(tmp_path):
    """A changed source must not be compared against a cached earlier read."""
    source = tmp_path / "genes" / "notes.md"
    source.parent.mkdir()
    data = _review([{"reference_id": "file:notes.md", "supporting_text": "second version"}])
    source.write_text("first version of the notes")
    assert len(find_local_quote_failures(data, tmp_path)) == 1
    source.write_text("the second version of the notes, longer")
    assert find_local_quote_failures(data, tmp_path) == []


@pytest.mark.parametrize(
    "review_path",
    ["genes/human/TP53/TP53-ai-review.yaml", "genes/human/AATF/AATF-ai-review.yaml"],
)
def test_baselined_failures_are_warnings(review_path):
    """Every failing quote in a baselined review is reported, but only as a warning.

    If a pinned review's quotes are fixed and pruned, pin another baselined review.
    """
    baseline = yaml.safe_load((PROJECT_ROOT / "conf" / "local_quote_baseline.yaml").read_text())
    assert review_path in baseline["entries"], f"{review_path} is no longer baselined"
    review = PROJECT_ROOT / review_path
    report = validate_gene_review(review, check_goa=False, check_supporting_text=False)
    issues = [i for i in report.issues if i.check_type == CHECK_TYPE]
    assert issues, f"{review} is baselined but reported no local-quote failures"
    assert {i.severity for i in issues} == {ValidationSeverity.WARNING}


def test_quote_matches_uses_validator_normalisation():
    path = PROJECT_ROOT / "genes" / "human" / "TP53" / "TP53-uniprot.txt"
    assert quote_matches("subcellular location:   [isoform 1]: NUCLEUS", path)
