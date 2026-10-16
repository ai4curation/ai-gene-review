"""A folded scalar must not silently rewrite prose.

``>-`` turns a single newline into a space, so a hyphenated compound split across lines
renders as two words. Both forms are valid YAML, so nothing that inspects the *parsed*
document can see it -- the damage appears only once the text is rendered, which is how
``A-kinase- anchoring`` reached the published AKAP12 page after a reflow that had been
justified as whitespace-only.
"""

import pytest

from ai_gene_review.validation.folded_scalar import (
    FoldedHyphenSplit,
    can_precede_hyphen,
    check_folded_scalar_hyphens,
    find_folded_hyphen_splits,
)
from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)
from ai_gene_review.validation.validator import check_best_practices_rules


def block(*body: str) -> str:
    """Build a one-key folded scalar from *body* lines."""
    return "reason: >-\n" + "".join(f"  {line}\n" for line in body)


def test_detects_a_split_compound():
    hits = list(find_folded_hyphen_splits(block("the loss-of-", "function phenotype")))
    assert hits == [FoldedHyphenSplit(line=2, tail="loss-of-", next_word="function")]


def test_reports_both_the_rendered_and_intended_forms():
    """The message must show the damage, not just the location."""
    (hit,) = list(find_folded_hyphen_splits(block("an A-kinase-", "anchoring region")))
    assert hit.rendered == "A-kinase- anchoring"
    assert hit.intended == "A-kinase-anchoring"


@pytest.mark.parametrize(
    "follower",
    ["and", "or", "nor", "to", "through", "versus"],
)
def test_suspended_hyphen_is_not_a_split(follower):
    """``betaB2- and betaA3-crystallins`` is correct English.

    This is the false-positive class that would make the check untrustworthy: the space
    after the hyphen is intended, and a check that fires on correct prose gets switched
    off.
    """
    assert not list(find_folded_hyphen_splits(block("betaB2-", f"{follower} betaA3-crystallins")))


def test_em_dash_folds_correctly():
    assert not list(find_folded_hyphen_splits(block("an aside --", "continues here")))


def test_clean_prose_is_silent():
    assert not list(find_folded_hyphen_splits(block("nothing wrong", "at all")))


def test_capitalised_continuation_is_still_a_split():
    """``ER-to-`` / ``Golgi`` renders as ``ER-to- Golgi`` and must be reported.

    An earlier version required a lowercase continuation, which dropped this real
    published split in LRIT3. The test that justified the gate was vacuous: its tail was a
    bare ``-``, excluded by ``len(tail) > 1`` before the case test was ever reached, so
    deleting the gate broke nothing.
    """
    (hit,) = list(find_folded_hyphen_splits(block("quantify ER-to-", "Golgi trafficking")))
    assert hit.rendered == "ER-to- Golgi"


def test_numeric_continuation_is_a_split():
    """``interleukin-`` / ``6`` is the same defect with a digit."""
    (hit,) = list(find_folded_hyphen_splits(block("the cytokine interleukin-", "6 receptor")))
    assert hit.intended == "interleukin-6"


def test_sequence_item_folded_heads_are_scanned():
    """``- statement: >-`` is a folded scalar too.

    The original BLOCK_HEAD could not match it, so thousands of blocks went unscanned and
    real splits in SLC25A24 and SDHB were invisible.
    """
    text = "references:\n- id: PMID:1\n  findings:\n  - statement: >-\n      cause Gorlin-\n      Chaudhry-Moss syndrome\n"
    assert [h.intended for h in find_folded_hyphen_splits(text)] == ["Gorlin-Chaudhry-Moss"]


def test_lookahead_stops_at_the_block_boundary():
    """The continuation must be inside the block.

    Without an indent test the lookahead reads the next dedented key and reports nonsense
    such as ``renders as 'oyl- action:'``.
    """
    text = "reason: >-\n  ends in acyl-\naction: REMOVE\n"
    assert not list(find_folded_hyphen_splits(text))


def test_only_looks_inside_folded_blocks():
    """A hyphen at the end of an ordinary scalar does not fold, so it is not reported."""
    text = "title: some-\nother: value\n"
    assert not list(find_folded_hyphen_splits(text))


def test_block_ends_at_dedent():
    """Content after the block dedents is outside the scalar."""
    text = "reason: >-\n  fine text here\nnext_key: some-\nvalue: x\n"
    assert not list(find_folded_hyphen_splits(text))


def test_multiple_splits_are_all_reported():
    hits = list(
        find_folded_hyphen_splits(
            block("the loss-of-", "function and the gain-of-", "function alleles")
        )
    )
    assert [h.intended for h in hits] == ["loss-of-function", "gain-of-function"]


@pytest.mark.parametrize(
    "tail,intended",
    [
        ("(Rab GTPase)-", "GTPase)-dependent"),
        ("24(S)-", "24(S)-dependent"),
        ("5-fluoro-2'-", "5-fluoro-2'-dependent"),
        # ']' is live in this corpus: PSEPK/ada has 'methylated-DNA-[protein]-' / 'cysteine'
        ("methylated-DNA-[protein]-", "methylated-DNA-[protein]-dependent"),
        ("{beta}-", "{beta}-dependent"),
        ("2\u2019-", "2\u2019-dependent"),
    ],
)
def test_closing_punctuation_before_the_hyphen_is_still_a_split(tail, intended):
    """Compounds ending in a bracket or apostrophe were silently dropped.

    ``tail[-2].isalnum()`` excluded em-dashes, which was its documented purpose, but also
    excluded ``)-``, ``]-`` and ``'-`` -- 16 live sites including VAM10's
    ``(Rab GTPase)-dependent`` and CYP46A1's ``24(S)-hydroxylation``, both rendering with
    the spurious space today.
    """
    (hit,) = list(find_folded_hyphen_splits(block(f"the {tail}", "dependent step")))
    assert hit.intended == intended


def test_a_hyphen_cannot_precede_the_hyphen():
    """This is what keeps em-dashes out, and it must stay true."""
    assert not can_precede_hyphen("-")
    assert can_precede_hyphen("a") and can_precede_hyphen(")")


SPLIT_DOC = (
    "id: X\n"
    "gene_symbol: X\n"
    "existing_annotations: []\n"
    "description: >-\n"
    "  carries an A-kinase-\n"
    "  anchoring region\n"
)


def test_check_reports_a_warning_with_the_documented_keys(tmp_path):
    """The reported keys are a contract, not decoration.

    ``check_type`` is a **TSV column** -- ``to_tsv_rows`` and ``tsv_header`` in
    validation_report.py both emit it -- so ``reports/validation-all.tsv`` keys on the
    literal ``folded_scalar_hyphen``. A typo there degrades silently to a row nobody can
    filter, which no other test would notice.
    """
    f = tmp_path / "X-ai-review.yaml"
    f.write_text(SPLIT_DOC)
    report = ValidationReport(file_path=f, is_valid=True)
    check_folded_scalar_hyphens(f, report)

    issues = [i for i in report.issues if i.check_type == "folded_scalar_hyphen"]
    assert len(issues) == 1
    assert issues[0].severity == ValidationSeverity.WARNING
    assert issues[0].validation_category == "BestPractices"
    assert "A-kinase- anchoring" in issues[0].message
    assert report.is_valid is True, "a warning must not invalidate the report"


def test_best_practices_rules_actually_reaches_the_check(tmp_path):
    """The wiring itself, which was the one part no test touched.

    Deleting the call site left all tests passing, so a merge resolution that dropped it
    -- and one did have to be hand-resolved -- would have been caught by nothing in CI.
    """
    f = tmp_path / "X-ai-review.yaml"
    f.write_text(SPLIT_DOC)
    import yaml

    report = ValidationReport(file_path=f, is_valid=True)
    check_best_practices_rules(
        yaml.safe_load(SPLIT_DOC), report, yaml_file=f, check_supporting_text=False
    )
    assert any(i.check_type == "folded_scalar_hyphen" for i in report.issues)
