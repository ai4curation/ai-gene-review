"""Tests for text-level edits of one row of a gene review."""

from __future__ import annotations

import difflib
from pathlib import Path

import pytest
import yaml

from ai_gene_review.tools.review_row_edit import RowEdit, RowEditError, apply_row_edits, block_scalar

REVIEW = """\
id: P00001
gene_symbol: TEST
existing_annotations:
- term:
    id: GO:0000398
    label: mRNA splicing, via spliceosome
  evidence_type: IBA
  original_reference_id: GO_REF:0000033
  review:
    summary: A plain summary that runs
      over two lines.
    action: REMOVE
    reason: >-
      The seeds are splicing factors and
      the gene is not.

    propagation_review:
      root_cause: PROPAGATION_BAD
      failure_modes:
      - WRONG_ORTHOLOG_OR_PARALOG
      - FUNCTIONAL_DIVERGENCE
    supported_by:
    - reference_id: PMID:1
      supporting_text: "a quote"
    - reference_id: PMID:2
      supporting_text: >-
        a folded
        quote

- term:
    id: GO:0005681
    label: spliceosomal complex
  evidence_type: IBA
  review:
    action: MARK_AS_OVER_ANNOTATED
    reason: 'A quoted reason'
# a trailing comment
- term:
    id: GO:0005681
    label: spliceosomal complex
  evidence_type: IEA
  review:
    action: MARK_AS_OVER_ANNOTATED
    reason: No change here.
core_functions: []
"""

OWN = "file:human/TEST/TEST-phylo.yaml"
QUOTE = "GO:0000398 (mRNA splicing, via spliceosome): PAINT node PTN000391532 is a speciation node at Eukaryota."


def rows(text: str) -> list[dict]:
    return yaml.safe_load(text)["existing_annotations"]


def changed_lines(before: str, after: str) -> tuple[list[str], list[str]]:
    """The lines a diff removes from ``before`` and the lines it adds in ``after``."""
    diff = list(difflib.ndiff(before.splitlines(), after.splitlines()))
    return [line[2:] for line in diff if line.startswith("- ")], [line[2:] for line in diff if line.startswith("+ ")]


def test_support_is_appended_to_an_existing_list_and_nothing_else_moves() -> None:
    out = apply_row_edits(REVIEW, [RowEdit("GO:0000398", add_support=((OWN, QUOTE),))])
    assert rows(out)[0]["review"]["supported_by"][-1] == {"reference_id": OWN, "supporting_text": QUOTE}
    removed, added = changed_lines(REVIEW, out)
    assert removed == []
    assert added == [f"    - reference_id: {OWN}", f'      supporting_text: "{QUOTE}"']
    # The new item sits right after the last item, before the blank line that follows the list.
    assert out.index(OWN) < out.index("- term:\n    id: GO:0005681")
    assert "        quote\n    - reference_id: file:" in out


def test_support_list_is_created_at_the_end_of_the_review_before_trailing_comments() -> None:
    out = apply_row_edits(REVIEW, [RowEdit("GO:0005681", add_support=((OWN, "GO:0005681 (spliceosomal complex): x"),))])
    assert rows(out)[1]["review"]["supported_by"] == [
        {"reference_id": OWN, "supporting_text": "GO:0005681 (spliceosomal complex): x"}
    ]
    assert "    reason: 'A quoted reason'\n    supported_by:\n    - reference_id: file:" in out
    assert out.index("supported_by:\n    - reference_id: file:") < out.index("# a trailing comment")
    # The IEA row with the same term is not an IBA row and is left alone.
    assert "supported_by" not in rows(out)[2]["review"]


@pytest.mark.parametrize(
    ("term", "before"),
    [
        ("GO:0000398", "The seeds are splicing factors and the gene is not."),
        ("GO:0005681", "A quoted reason"),
    ],
)
def test_reason_is_appended_whatever_its_style(term: str, before: str) -> None:
    out = apply_row_edits(REVIEW, [RowEdit(term, append_reason="Tree: all five seeds sit in one branch.")])
    data = rows(out)
    row = next(r for r in data if r["term"]["id"] == term and r["evidence_type"] == "IBA")
    assert row["review"]["reason"] == f"{before}{'' if before.endswith('.') else '.'} Tree: all five seeds sit in one branch."
    # Every other row is untouched.
    others = [r for r in data if r is not row]
    assert others == [r for r in rows(REVIEW) if not (r["term"]["id"] == term and r["evidence_type"] == "IBA")]


def test_reason_and_summary_can_be_replaced_and_long_text_is_folded() -> None:
    long = "The tree shows " + "a one-to-one ortholog seed inside the seed clade, " * 6 + "so paralogy is not the argument."
    out = apply_row_edits(REVIEW, [RowEdit("GO:0000398", replace_reason=long, replace_summary="Short summary.")])
    review = rows(out)[0]["review"]
    assert review["reason"] == long and review["summary"] == "Short summary."
    assert max(len(line) for line in out.splitlines()) <= 100
    assert "    reason: >-\n      The tree shows" in out
    # The blank line that followed the old reason is still there.
    assert "\n\n    propagation_review:" in out


def test_action_and_failure_modes_change_in_place() -> None:
    edit = RowEdit(
        "GO:0000398",
        new_action="KEEP_AS_NON_CORE",
        remove_failure_modes=("WRONG_ORTHOLOG_OR_PARALOG",),
        add_failure_modes=("GRANULARITY_MISMATCH",),
    )
    out = apply_row_edits(REVIEW, [edit])
    review = rows(out)[0]["review"]
    assert review["action"] == "KEEP_AS_NON_CORE"
    assert review["propagation_review"]["failure_modes"] == ["FUNCTIONAL_DIVERGENCE", "GRANULARITY_MISMATCH"]
    removed, added = changed_lines(REVIEW, out)
    assert removed == ["    action: REMOVE", "      - WRONG_ORTHOLOG_OR_PARALOG"]
    assert added == ["    action: KEEP_AS_NON_CORE", "      - GRANULARITY_MISMATCH"]


def test_several_edits_apply_together() -> None:
    edits = [
        RowEdit("GO:0000398", add_support=((OWN, QUOTE),), append_reason="Tree: paralogs only."),
        RowEdit("GO:0005681", add_support=((OWN, "GO:0005681 (spliceosomal complex): y"),), append_reason="Tree: same node."),
    ]
    out = apply_row_edits(REVIEW, edits)
    data = rows(out)
    assert data[0]["review"]["reason"].endswith("the gene is not. Tree: paralogs only.")
    assert data[1]["review"]["reason"] == "A quoted reason. Tree: same node."
    assert data[0]["review"]["supported_by"][-1]["supporting_text"] == QUOTE
    assert data[1]["review"]["supported_by"][0]["reference_id"] == OWN
    assert data[2] == rows(REVIEW)[2]


def test_insertions_at_the_same_place_keep_the_deeper_one_first() -> None:
    text = REVIEW.replace(
        """    supported_by:
    - reference_id: PMID:1
      supporting_text: "a quote"
    - reference_id: PMID:2
      supporting_text: >-
        a folded
        quote
""",
        "",
    )
    edit = RowEdit("GO:0000398", add_support=((OWN, QUOTE),), add_failure_modes=("GRANULARITY_MISMATCH",))
    review = rows(apply_row_edits(text, [edit]))[0]["review"]
    assert review["propagation_review"]["failure_modes"][-1] == "GRANULARITY_MISMATCH"
    assert review["supported_by"] == [{"reference_id": OWN, "supporting_text": QUOTE}]


def test_every_matching_row_is_edited_and_negation_is_part_of_the_match() -> None:
    twice = REVIEW.replace("  evidence_type: IEA\n", "  evidence_type: IBA\n")
    out = apply_row_edits(twice, [RowEdit("GO:0005681", append_reason="Tree: x.")])
    assert [r["review"]["reason"] for r in rows(out)[1:]] == ["A quoted reason. Tree: x.", "No change here. Tree: x."]

    negated = REVIEW.replace("  evidence_type: IBA\n  original_reference_id", "  evidence_type: IBA\n  negated: true\n  original_reference_id")
    with pytest.raises(RowEditError, match="no IBA row"):
        apply_row_edits(negated, [RowEdit("GO:0000398", append_reason="Tree: x.")])
    out = apply_row_edits(negated, [RowEdit("GO:0000398", negated=True, append_reason="Tree: x.")])
    assert rows(out)[0]["review"]["reason"].endswith("Tree: x.")


@pytest.mark.parametrize(
    ("text", "edit", "message"),
    [
        (REVIEW, RowEdit("GO:9999999", append_reason="x"), "no IBA row"),
        (REVIEW.replace("    supported_by:\n    - reference_id: PMID:1\n      supporting_text: \"a quote\"\n    - reference_id: PMID:2\n      supporting_text: >-\n        a folded\n        quote\n", "    supported_by: []\n"), RowEdit("GO:0000398", add_support=((OWN, QUOTE),)), "supported_by"),
        (REVIEW, RowEdit("GO:0005681", remove_failure_modes=("FUNCTIONAL_DIVERGENCE",)), "failure_modes"),
        (REVIEW, RowEdit("GO:0000398", remove_failure_modes=("GRANULARITY_MISMATCH",)), "GRANULARITY_MISMATCH"),
        (REVIEW, RowEdit("GO:0000398", append_reason="x", replace_reason="y"), "both"),
    ],
)
def test_an_edit_that_cannot_be_placed_is_refused(text: str, edit: RowEdit, message: str) -> None:
    with pytest.raises(RowEditError, match=message):
        apply_row_edits(text, [edit])


def test_an_edit_with_nothing_to_do_returns_the_text_unchanged() -> None:
    assert apply_row_edits(REVIEW, [RowEdit("GO:0000398")]) == REVIEW
    assert apply_row_edits(REVIEW, []) == REVIEW


@pytest.mark.parametrize(
    "value",
    [
        "One short sentence.",
        "word " * 60 + "end.",
        "Two paragraphs.\nThe second one: with a colon, a # hash and 'quotes'.",
        "Double  spaces stay as they are, and so does a trailing colon:",
        "- starts like a list item",
        "has \"double quotes\" and a back\\slash",
    ],
)
def test_block_scalar_round_trips_any_value(value: str) -> None:
    emitted = block_scalar(value, key_column=4)
    assert yaml.safe_load("    key: " + emitted + "\n")["key"] == value


def test_a_real_review_changes_only_where_asked(tmp_path: Path) -> None:
    source = Path("genes/human/CIRBP/CIRBP-ai-review.yaml").read_text(encoding="utf-8")
    edit = RowEdit("GO:0003729", add_support=(("file:human/CIRBP/CIRBP-phylo.yaml", "GO:0003729 (mRNA binding): PAINT node"),))
    out = apply_row_edits(source, [edit])
    removed, added = changed_lines(source, out)
    assert removed == [] and len(added) == 2
    before, after = yaml.safe_load(source), yaml.safe_load(out)
    index = next(
        i for i, r in enumerate(before["existing_annotations"])
        if r["term"]["id"] == "GO:0003729" and r["evidence_type"] == "IBA"
    )
    assert after["existing_annotations"][index]["review"]["supported_by"][-1]["reference_id"].endswith("CIRBP-phylo.yaml")
    del after["existing_annotations"][index]["review"]["supported_by"][-1]
    if not after["existing_annotations"][index]["review"]["supported_by"]:
        del after["existing_annotations"][index]["review"]["supported_by"]
    assert before == after


SHARED = """\
existing_annotations:
- term:
    id: GO:0000001
  evidence_type: IBA
  review:
    summary: First row; its support list is anchored.
    action: REMOVE
    supported_by: &id001
    - reference_id: PMID:1
      supporting_text: 'first: quote'
    - &id002
      reference_id: PMID:2
      supporting_text: second quote
- term:
    id: GO:0000002
  evidence_type: IBA
  review:
    summary: Second row; it reuses the first row's list.
    action: REMOVE
    reason: Shares the support.
    supported_by: *id001
- term:
    id: GO:0000003
  evidence_type: IEA
  review:
    action: ACCEPT
    supported_by:
    - *id002
"""


def test_a_row_that_reuses_another_rows_support_gets_its_own_copy() -> None:
    out = apply_row_edits(SHARED, [RowEdit("GO:0000002", add_support=((OWN, "GO:0000002 (x): y"),))])
    before, after = rows(SHARED), rows(out)
    assert after[1]["review"]["supported_by"] == [
        *before[1]["review"]["supported_by"],
        {"reference_id": OWN, "supporting_text": "GO:0000002 (x): y"},
    ]
    # The row whose list it was, and the row that reuses one item of it, are as they were.
    assert after[0] == before[0] and after[2] == before[2]
    assert "supported_by: &id001" in out and "supported_by: *id001" not in out


def test_a_row_whose_support_is_reused_elsewhere_stops_sharing_it() -> None:
    out = apply_row_edits(SHARED, [RowEdit("GO:0000001", add_support=((OWN, "GO:0000001 (x): y"),))])
    before, after = rows(SHARED), rows(out)
    assert after[0]["review"]["supported_by"][-1] == {"reference_id": OWN, "supporting_text": "GO:0000001 (x): y"}
    assert after[0]["review"]["supported_by"][:-1] == before[0]["review"]["supported_by"]
    assert after[1] == before[1] and after[2] == before[2]
    assert "&id001" not in out and "*id001" not in out
    # The item-level anchor inside the list is still defined before its use.
    assert out.index("&id002") < out.index("*id002")


def test_both_sides_of_a_shared_list_can_be_edited_together() -> None:
    edits = [
        RowEdit("GO:0000001", add_support=((OWN, "GO:0000001 (x): a"),)),
        RowEdit("GO:0000002", add_support=((OWN, "GO:0000002 (x): b"),)),
    ]
    with pytest.raises(RowEditError, match="same text"):
        apply_row_edits(SHARED, edits)
    # One after the other works: the first edit ends the sharing.
    once = apply_row_edits(SHARED, edits[:1])
    twice = apply_row_edits(once, edits[1:])
    data = rows(twice)
    assert data[0]["review"]["supported_by"][-1]["supporting_text"] == "GO:0000001 (x): a"
    assert data[1]["review"]["supported_by"][-1]["supporting_text"] == "GO:0000002 (x): b"
    assert len(data[1]["review"]["supported_by"]) == 3


def test_a_missing_reason_is_created_after_the_action() -> None:
    out = apply_row_edits(SHARED, [RowEdit("GO:0000001", append_reason="Tree: the seeds are paralogs.")])
    assert rows(out)[0]["review"]["reason"] == "Tree: the seeds are paralogs."
    assert "    action: REMOVE\n    reason: >-\n      Tree: the seeds are paralogs.\n    supported_by: &id001" in out
    assert rows(out)[1:] == rows(SHARED)[1:]


def test_a_value_cut_short_by_a_comment_is_refused() -> None:
    text = REVIEW.replace("    reason: 'A quoted reason'", "    reason: Held on issue #29437 until fixed")
    assert rows(text)[1]["review"]["reason"] == "Held on issue"
    with pytest.raises(RowEditError, match="comment"):
        apply_row_edits(text, [RowEdit("GO:0005681", append_reason="Tree: x.")])


def test_failure_modes_shared_through_an_alias_are_refused() -> None:
    text = REVIEW.replace(
        "    action: MARK_AS_OVER_ANNOTATED\n    reason: 'A quoted reason'\n",
        "    action: MARK_AS_OVER_ANNOTATED\n    reason: 'A quoted reason'\n    propagation_review: *shared\n",
    ).replace("    propagation_review:\n      root_cause", "    propagation_review: &shared\n      root_cause")
    with pytest.raises(RowEditError, match="shared"):
        apply_row_edits(text, [RowEdit("GO:0005681", add_failure_modes=("GRANULARITY_MISMATCH",))])


STYLES = """\
existing_annotations:
- term: {id: 'GO:0000001'}
  evidence_type: IBA
  review:
    action: REMOVE
    reason: A plain reason that runs
      over two lines
- term: {id: 'GO:0000002'}
  evidence_type: IBA
  review:
    action: REMOVE
    reason: >-
      A folded reason
      on two lines.
    summary: after
- term: {id: 'GO:0000003'}
  evidence_type: IBA
  review:
    action: REMOVE
    reason: 'A single-quoted reason,
      it''s on two lines.'
- term: {id: 'GO:0000004'}
  evidence_type: IBA
  review:
    action: REMOVE
    reason: "A double-quoted reason."
- term: {id: 'GO:0000005'}
  evidence_type: IBA
  review:
    action: REMOVE
    reason: One line only.
- term: {id: 'GO:0000006'}
  evidence_type: IBA
  review:
    action: REMOVE
    reason: |-
      A literal reason.
      Second paragraph.
"""
ADDED = "In the tree the gene's \"own\" branch holds no seed."


@pytest.mark.parametrize("number", [1, 2, 3, 4, 5, 6])
def test_an_appended_sentence_leaves_the_existing_text_as_written(number: int) -> None:
    term = f"GO:000000{number}"
    out = apply_row_edits(STYLES, [RowEdit(term, append_reason=ADDED)])
    before, after = rows(STYLES), rows(out)
    old = before[number - 1]["review"]["reason"]
    assert after[number - 1]["review"]["reason"] == f"{old}{'' if old.endswith('.') else '.'} {ADDED}"
    assert [r for i, r in enumerate(after) if i != number - 1] == [r for i, r in enumerate(before) if i != number - 1]
    removed, added = changed_lines(STYLES, out)
    if number in (2, 5):
        # Folded, or one plain line: a pure addition.
        assert removed == [] and len(added) == 1
    elif number in (1, 3, 4, 6):
        # The last line gains a full stop, loses its closing quote, or (literal) takes the sentence.
        assert len(removed) == 1


def test_text_a_plain_scalar_cannot_hold_falls_back_to_rewriting_it() -> None:
    out = apply_row_edits(STYLES, [RowEdit("GO:0000005", append_reason="Tree: the seeds are paralogs # all of them.")])
    assert rows(out)[4]["review"]["reason"] == "One line only. Tree: the seeds are paralogs # all of them."
    assert "    reason: >-\n      One line only. Tree: the seeds are paralogs # all of them.\n" in out


FAMILY = """\
family_id: PANTHER:PTHR00001
node_assessments:
- node_id: PANTHER:PTN000000001
  asserted_term:
    id: GO:0005944
    label: a complex
  evidence: IBD
  assessment: TOO_DEEP
  assessment_reason: The complex is asserted at the class I node
    and descends to subunits that are not in it.
  supported_by:
  - reference_id: file:interpro/panther/PTHR00001/PTHR00001-paint.tsv
    supporting_text: "PTHR00001\\tPTN000000001\\tGO:0005944\\tC\\tIBD\\tfalse"
- node_id: PANTHER:PTN000000001
  asserted_term:
    id: GO:0016301
    label: kinase activity
  evidence: IBD
  assessment: SOUND
  assessment_reason: Fine.
- node_id: PANTHER:PTN000000002
  asserted_term:
    id: GO:0005944
    label: a complex
  evidence: IRD
  negated: true
  assessment: LOSS_TOO_BROAD
  assessment_reason: The loss covers a subfamily that has the complex.
notes: unchanged
"""
LISTING = "file:interpro/panther/PTHR00001/PTHR00001-tree-nodes.yaml"


def test_a_family_node_assessment_is_edited_by_node_and_term() -> None:
    edit = RowEdit(
        "GO:0005944",
        node_id="PANTHER:PTN000000001",
        add_support=((LISTING, "PTN000000001 GO:0005944 IBD: PAINT node PTN000000001 is a duplication node."),),
        append_reason="In the PANTHER 19.0 tree the single seed sits six steps below the node.",
    )
    out = apply_row_edits(FAMILY, [edit])
    before, after = yaml.safe_load(FAMILY), yaml.safe_load(out)
    first = after["node_assessments"][0]
    assert first["assessment_reason"].endswith("not in it. In the PANTHER 19.0 tree the single seed sits six steps below the node.")
    assert first["supported_by"][-1]["reference_id"] == LISTING
    assert after["node_assessments"][1:] == before["node_assessments"][1:] and after["notes"] == "unchanged"
    removed, added = changed_lines(FAMILY, out)
    assert removed == [] and len(added) == 3


def test_a_negated_node_assessment_gets_its_support_list_and_a_new_verdict() -> None:
    edit = RowEdit(
        "GO:0005944", negated=True, node_id="PANTHER:PTN000000002",
        add_support=((LISTING, "PTN000000002 NOT GO:0005944 IRD: PAINT node"),), new_action="UNRESOLVED",
    )
    out = apply_row_edits(FAMILY, [edit])
    last = yaml.safe_load(out)["node_assessments"][2]
    assert last["assessment"] == "UNRESOLVED" and last["supported_by"][0]["reference_id"] == LISTING
    assert "  assessment_reason: The loss covers a subfamily that has the complex.\n  supported_by:\n  - reference_id: file:" in out
    assert out.endswith("notes: unchanged\n")


@pytest.mark.parametrize(
    ("edit", "message"),
    [
        (RowEdit("GO:0005944", node_id="PANTHER:PTN000000009", append_reason="x"), "no assessment of PANTHER:PTN000000009"),
        (RowEdit("GO:0005944", node_id="PANTHER:PTN000000001", replace_summary="x"), "no summary"),
        (RowEdit("GO:0005944", node_id="PANTHER:PTN000000001", add_failure_modes=("ROLE_CONFLATION",)), "failure_modes"),
    ],
)
def test_node_assessment_edits_that_do_not_apply_are_refused(edit: RowEdit, message: str) -> None:
    with pytest.raises(RowEditError, match=message):
        apply_row_edits(FAMILY, [edit])
