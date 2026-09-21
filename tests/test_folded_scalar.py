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
    find_folded_hyphen_splits,
)


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


def test_capitalised_next_word_is_not_a_split():
    """A trailing hyphen before a new sentence is not a broken compound."""
    assert not list(find_folded_hyphen_splits(block("an aside -", "Then a new sentence")))


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
