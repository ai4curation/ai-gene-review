"""Tests for the tree re-read campaign script (``projects/IBA_REVIEW/tree-rereview/tree_rereview.py``).

The script is a project tool, not a package module, so it is loaded by path. What is
tested here is what it guarantees about its edits: which readings it applies, which it
leaves for a curator, and what its history records say.
"""

from __future__ import annotations

import doctest
import importlib.util
import re
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest

from ai_gene_review.tools.review_row_edit import RowEdit

SCRIPT = Path(__file__).parent.parent / "projects" / "IBA_REVIEW" / "tree-rereview" / "tree_rereview.py"


def _load() -> ModuleType:
    spec = importlib.util.spec_from_file_location("tree_rereview", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["tree_rereview"] = module
    spec.loader.exec_module(module)
    return module


tr = _load()

NODE = "GO:0000398 (mRNA splicing, via spliceosome): PAINT node PTN000391532 is a speciation node at Eukaryota, with 373 leaves in 84 species and 21 subfamilies."
PATH = "TEST (PTN002553788, PTHR48034:SF5) is 24 steps below it, across 5 duplications; path length 3.554."
SEEDS = "Seeds: 5 of 5 resolved to leaves of this tree."
INSIDE = "They all sit in one branch below the node: their common ancestor is PTN002690243, a speciation node at Bilateria, covering 213 leaves, 6 steps below the PAINT node; TEST is inside that clade."
OUTSIDE = INSIDE.replace("is inside that clade", "is outside that clade")
PARALOGS = "By the tree the seeds are 1 ortholog across later duplications and 4 paralogs of TEST."
ORTHOLOGS = "By the tree the seeds are 2 one-to-one orthologs of TEST."
REFERENCE = "file:human/TEST/TEST-phylo.yaml"
SENTENCE = "In the PANTHER 19.0 tree the five seeds are paralogs of TEST, which is what the review says."
REPLACEMENT = "The seeds are splicing factors and the gene is not. In the PANTHER 19.0 tree four of the five seeds are paralogs of TEST."


def source(*parts: str) -> tuple[str, str, str]:
    text = " ".join(parts)
    return text, f"summary: >-\n  {text}\n", REFERENCE


def row(**fields: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "gene": "human/TEST", "term": "GO:0000398", "negated": False, "kind": "overruled", "action": "REMOVE",
        "tree_reading": "SUPPORTS", "quote_sentences": [1, 2, 4, 5], "tree_sentence": SENTENCE,
    }
    return {**base, **fields}


REVIEW_ROW = {"action": "REMOVE", "reason": "The seeds are splicing factors and the gene is not."}
AGREED = {"agrees": True}


def test_the_scripts_doctests_pass() -> None:
    """`just doctest` collects `src` only, so the script's doctests are run from here."""
    result = doctest.testmod(tr)
    assert result.attempted > 0 and result.failed == 0


def test_an_additive_reading_becomes_a_quote_and_a_sentence() -> None:
    edit = tr.row_edit(row(), [REVIEW_ROW], source(NODE, PATH, SEEDS, OUTSIDE, PARALOGS))
    assert edit == RowEdit(
        "GO:0000398",
        add_support=((REFERENCE, f"{NODE} {PATH}"), (REFERENCE, f"{OUTSIDE} {PARALOGS}")),
        append_reason=SENTENCE,
    )


def test_a_verified_reason_correction_replaces_the_reason_and_nothing_else() -> None:
    reading = row(
        tree_reading="REASON_CONTRADICTED", verifier=AGREED, reason_replacement=REPLACEMENT,
        false_claims=["all five seeds are paralogs: one is an ortholog"], false_claim_fields=["reason"],
    )
    edit = tr.row_edit(reading, [REVIEW_ROW], source(NODE, PATH, SEEDS, OUTSIDE, PARALOGS))
    assert isinstance(edit, RowEdit)
    assert (edit.replace_reason, edit.append_reason) == (REPLACEMENT, "")
    assert (edit.add_failure_modes, edit.remove_failure_modes, edit.new_action, edit.replace_summary) == ((), (), None, None)


CORRECTION = {"tree_reading": "REASON_CONTRADICTED", "verifier": AGREED, "reason_replacement": REPLACEMENT, "false_claim_fields": ["reason"]}


@pytest.mark.parametrize(
    ("fields", "reached", "parts", "why"),
    [
        # Judgements the script never makes.
        ({"tree_reading": "VERDICT_UNSUPPORTED"}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "calls for a judgement"),
        ({"tree_reading": "CANNOT_TELL"}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "calls for a judgement"),
        ({"proposed_action": "ACCEPT"}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "change of verdict"),
        ({"kind": "kept_under_loss", "action": "ACCEPT"}, [REVIEW_ROW], (NODE, PATH), "needs a decision on the loss"),
        # Failure modes are a curator's to change, whatever the reading.
        ({**CORRECTION, "failure_modes_remove": ["WRONG_ORTHOLOG_OR_PARALOG"]}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS),
         "change of failure modes is proposed \\(remove WRONG_ORTHOLOG_OR_PARALOG\\)"),
        ({**CORRECTION, "failure_modes_add": ["GRANULARITY_MISMATCH"]}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS),
         "add GRANULARITY_MISMATCH"),
        # A correction is applied only where the script can make the whole of it.
        ({**CORRECTION, "verifier": None}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "not checked by the verifier"),
        ({**CORRECTION, "false_claim_fields": []}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "does not say which field"),
        ({**CORRECTION, "false_claim_fields": ["reason", "summary"]}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS),
         "contradicted claim is in summary, which the script does not rewrite"),
        ({**CORRECTION, "false_claim_fields": ["propagation_review"]}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS),
         "contradicted claim is in propagation_review"),
        (CORRECTION, [{"action": "REMOVE", "summary": "No reason on this row."}], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "no reason to correct"),
        ({**CORRECTION, "reason_replacement": "Too short."}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "without a replacement reason"),
        # The edit must be for exactly one row of the review.
        ({}, [REVIEW_ROW, {"action": "ACCEPT"}], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "2 rows of the review match"),
        ({}, [], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "no row of the review matches"),
        # The quotes have to carry the evidence, the adverse part included.
        ({"quote_sentences": []}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "quotes only the sentence that names the term"),
        ({"quote_sentences": [1]}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "quotes only the sentence that names the term"),
        ({"quote_sentences": [1, 2, 5]}, [REVIEW_ROW], (NODE, PATH, SEEDS, INSIDE, PARALOGS),
         "does not quote what stands against the verdict: the gene is inside the clade the seeds span"),
        ({"quote_sentences": [1, 2]}, [{**REVIEW_ROW, "propagation_review": {"failure_modes": ["WRONG_ORTHOLOG_OR_PARALOG"]}}],
         (NODE, PATH, SEEDS, OUTSIDE, ORTHOLOGS), "the tree relates every seed to the gene as an ortholog"),
        ({"tree_sentence": "Too short."}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "no sentence on what the tree shows"),
        # A row on the candidate list has to have been verified.
        ({"flags": ["overruled_though_gene_is_a_seed"]}, [REVIEW_ROW], (NODE, PATH, SEEDS, OUTSIDE, PARALOGS), "must be verified"),
    ],
)
def test_readings_the_script_leaves_for_a_curator(
    fields: dict[str, Any], reached: list[dict[str, Any]], parts: tuple[str, ...], why: str
) -> None:
    outcome = tr.row_edit(row(**fields), reached, source(*parts))
    assert isinstance(outcome, str)
    assert re.search(why, outcome), outcome


def test_quoting_the_adverse_sentence_lets_a_verified_reading_through() -> None:
    reading = row(quote_sentences=[1, 4, 5], verifier=AGREED)
    edit = tr.row_edit(reading, [REVIEW_ROW], source(NODE, PATH, SEEDS, INSIDE, PARALOGS))
    assert isinstance(edit, RowEdit)
    assert edit.add_support == ((REFERENCE, NODE), (REFERENCE, f"{INSIDE} {PARALOGS}"))


def test_a_row_with_an_adverse_sentence_is_not_applied_unverified() -> None:
    """Whether the sentence faces the adverse fact is a judgement, so a second reader has to have looked."""
    outcome = tr.row_edit(row(quote_sentences=[1, 4, 5]), [REVIEW_ROW], source(NODE, PATH, SEEDS, INSIDE, PARALOGS))
    assert outcome == "a row whose tree file has a sentence against the verdict was not checked by the verifier"
    # A row with nothing adverse may be applied on the reader's word alone.
    assert isinstance(tr.row_edit(row(), [REVIEW_ROW], source(NODE, PATH, SEEDS, OUTSIDE, PARALOGS)), RowEdit)


def test_a_verifiers_correction_is_used_whole_and_brings_its_own_quotes() -> None:
    faulted = row(
        tree_reading="REASON_CONTRADICTED", reason_replacement=REPLACEMENT, false_claim_fields=["reason"],
        failure_modes_remove=["WRONG_ORTHOLOG_OR_PARALOG"], quote_sentences=[1, 2, 3],
        verifier={"agrees": False, "problem": "x", "fixed": {"tree_reading": "SUPPORTS", "quote_sentences": [1, 5], "tree_sentence": SENTENCE}},
    )
    edit = tr.row_edit(faulted, [REVIEW_ROW], source(NODE, PATH, SEEDS, OUTSIDE, PARALOGS))
    assert isinstance(edit, RowEdit)
    # Neither the faulted reading's quotes nor its proposals survive.
    assert edit.add_support == ((REFERENCE, NODE), (REFERENCE, PARALOGS))
    assert (edit.append_reason, edit.replace_reason, edit.remove_failure_modes) == (SENTENCE, None, ())


def test_a_correction_that_gives_no_quotes_does_not_fall_back_on_the_faulted_ones() -> None:
    faulted = row(
        quote_sentences=[1, 2, 5],
        verifier={"agrees": False, "problem": "the quotes do not carry the fact", "fixed": {"tree_reading": "SUPPORTS", "quote_sentences": [], "tree_sentence": SENTENCE}},
    )
    outcome = tr.row_edit(faulted, [REVIEW_ROW], source(NODE, PATH, SEEDS, OUTSIDE, PARALOGS))
    assert outcome == "the reading quotes only the sentence that names the term and the node"


def test_a_disagreement_without_a_usable_correction_goes_to_a_curator() -> None:
    assert tr.row_edit(row(verifier={"agrees": False, "problem": "wrong"}), [REVIEW_ROW], source(NODE, PATH)) == "the verifier disagrees with the reading"


LISTING = "PTN000391532 GO:0000398 IBD: PAINT node PTN000391532 is a speciation node at Eukaryota, with 373 leaves in 84 species and 21 subfamilies."
BRACKET = "They sit in 2 of the 2 branches below the node, so the node is their common ancestor."


@pytest.mark.parametrize(("assessment", "quoted", "applied"), [("TOO_DEEP", [1, 2], False), ("TOO_DEEP", [1, 3], True), ("NEEDS_PRUNING", [1, 2], True)])
def test_a_too_deep_assessment_has_to_quote_that_the_seeds_bracket_the_node(assessment: str, quoted: list[int], applied: bool) -> None:
    reading = {
        "family": "PTHR48034", "node": "PANTHER:PTN000391532", "term": "GO:0000398", "negated": False, "kind": "node",
        "action": assessment, "tree_reading": "NOT_A_TREE_ARGUMENT", "quote_sentences": quoted, "tree_sentence": SENTENCE,
        "verifier": AGREED,
    }
    text = " ".join([LISTING, SEEDS, BRACKET])
    outcome = tr.row_edit(reading, [{"assessment": assessment, "assessment_reason": "x"}], (text, text, "file:interpro/panther/PTHR48034/PTHR48034-tree-nodes.yaml"))
    assert isinstance(outcome, RowEdit) is applied
    if not applied:
        assert "the seeds bracket the node" in str(outcome)
    else:
        assert isinstance(outcome, RowEdit) and outcome.node_id == "PANTHER:PTN000391532"


def test_history_says_whether_a_reason_was_added_to_or_rewritten() -> None:
    added = row(action="REMOVE")
    rewritten = row(term="GO:0005681", tree_reading="REASON_CONTRADICTED", false_claims=["seeds are paralogs: 2 are orthologs"])
    text = tr.history_details("human/TEST", [added, rewritten], unshared=True)
    assert f"- GO:0000398 (REMOVE): the tree agrees with the stated reason. Added to the reason: {SENTENCE}" in text
    assert "- GO:0005681 (REMOVE): the reason made a claim the tree contradicts (seeds are paralogs: 2 are orthologs). The reason was rewritten" in text
    assert "Added to the reason" not in text.split("- GO:0005681")[1].splitlines()[0]
    assert "written out in full" in text
    assert "written out in full" not in tr.history_details("human/TEST", [added])


def test_history_describes_a_verifier_corrected_row_by_the_corrected_reading() -> None:
    corrected = row(
        tree_reading="REASON_CONTRADICTED", outcome_detail=tr.CORRECTED_BY_VERIFIER,
        verifier={"agrees": False, "fixed": {"tree_reading": "NOT_A_TREE_ARGUMENT", "quote_sentences": [1, 5], "tree_sentence": SENTENCE}},
    )
    line = tr.history_details("human/TEST", [corrected]).splitlines()[2]
    assert line.startswith("- GO:0000398 (REMOVE): the verdict rests on evidence the tree does not speak to") and line.endswith(SENTENCE)


def test_matching_rows_finds_family_assessments_by_node_term_and_negation() -> None:
    doc = {"node_assessments": [
        {"node_id": "PANTHER:PTN1", "asserted_term": {"id": "GO:1"}, "assessment": "TOO_DEEP"},
        {"node_id": "PANTHER:PTN1", "asserted_term": {"id": "GO:1"}, "negated": True, "assessment": "LOSS_TOO_BROAD"},
        {"node_id": "PANTHER:PTN2", "asserted_term": {"id": "GO:1"}, "assessment": "TOO_DEEP"},
    ]}
    found = tr.matching_rows(doc, {"family": "PTHR1", "node": "PANTHER:PTN1", "term": "GO:1", "negated": False})
    assert [item["assessment"] for item in found] == ["TOO_DEEP"]


WITH_LIST = "id: P1\nreferences:\n- id: PMID:1\n  title: A paper\n"
WITHOUT_LIST = "id: P1\nexisting_annotations: []\n"


def test_a_review_with_a_reference_list_gets_its_tree_file_listed() -> None:
    text, problem = tr.with_tree_reference(WITH_LIST, "human/CIRBP")
    assert problem == ""
    assert text.endswith("- id: file:human/CIRBP/CIRBP-phylo.yaml\n  title: Placement of the IBA rows of CIRBP in the PANTHER 19.0 tree and family alignment\n")
    # Listing it again changes nothing and is no problem.
    assert tr.with_tree_reference(text, "human/CIRBP") == (text, "")


def test_a_review_without_a_reference_list_is_left_alone_and_says_why() -> None:
    text, problem = tr.with_tree_reference(WITHOUT_LIST, "human/CIRBP")
    assert text == WITHOUT_LIST
    assert "references" in problem


def test_the_first_error_of_a_validator_run_is_what_gets_reported() -> None:
    output = "checking\n  ❌ ERROR: [reference] quote not found in PMID:1\n  ⚠ WARNING: something else\n"
    assert tr._first_error(output) == "❌ ERROR: [reference] quote not found in PMID:1"
    assert tr._first_error("all quiet") == "no longer validates"


def test_the_worklist_says_that_notes_predate_the_edit() -> None:
    assert "as it stood before the edit" in tr.worklist()["about"]


def test_a_review_that_was_put_back_leaves_no_trace_of_an_edit_in_the_record() -> None:
    record = {tr.NOT_LISTED: {"human/TEST": "no references list"}}
    rows = [row(outcome="applied"), row(term="GO:0005681", outcome="applied", outcome_detail=tr.CORRECTED_BY_VERIFIER)]
    tr.undo_applied(record, "human/TEST", rows, "ERROR: quote not found")
    assert [(r["outcome"], r["outcome_detail"]) for r in rows] == [
        ("adjudicate", "edit undone, the review no longer validated: ERROR: quote not found")
    ] * 2
    # The review is as it was, so it is not one whose tree file went unlisted.
    assert tr.NOT_LISTED not in record


def test_only_the_review_that_was_put_back_is_taken_off_the_unlisted_list() -> None:
    record = {tr.NOT_LISTED: {"human/TEST": "no references list", "human/OTHER": "no references list"}}
    tr.undo_applied(record, "human/TEST", [row(outcome="applied")], "ERROR: x")
    assert record[tr.NOT_LISTED] == {"human/OTHER": "no references list"}


def test_failed_units_are_those_whose_review_stopped_validating() -> None:
    results = {"human/A": (True, "✓ Valid"), "PTHR1": (False, "ERROR in --schema\n  ✗ not valid\n"), "human/B": (False, "nothing recognisable")}
    assert tr.failed_units(results) == {"PTHR1": "ERROR in --schema", "human/B": "no longer validates"}


def test_quotes_added_to_a_review_that_was_put_back_are_forgotten() -> None:
    rows = [row(outcome="applied", quotes_added=[4]), row(term="GO:0005681", outcome="applied")]
    tr.forget_added_quotes(rows)
    assert all("quotes_added" not in r for r in rows)


def test_a_contradiction_both_agents_agree_on_that_the_script_left_is_named() -> None:
    left = row(
        tree_reading="REASON_CONTRADICTED", outcome="adjudicate", verifier=AGREED,
        outcome_detail="the contradicted claim is in summary, which the script does not rewrite",
    )
    rows = [
        left,
        # corrected by the script
        row(term="GO:0005681", tree_reading="REASON_CONTRADICTED", outcome="applied", verifier=AGREED),
        # the verifier did not accept the reading: not an agreed finding
        row(term="GO:0005682", tree_reading="REASON_CONTRADICTED", outcome="adjudicate", verifier={"agrees": False, "problem": "x"}),
        # a verdict to judge, not a statement to correct
        row(term="GO:0005683", tree_reading="VERDICT_UNSUPPORTED", outcome="adjudicate", verifier=AGREED),
        # never checked
        row(term="GO:0005684", tree_reading="REASON_CONTRADICTED", outcome="adjudicate"),
    ]
    assert tr.standing_contradictions(rows) == [left]


def test_a_contradiction_whose_draft_the_verifier_faulted_is_counted_apart() -> None:
    agreed = row(tree_reading="REASON_CONTRADICTED", outcome="adjudicate", verifier=AGREED)
    faulted = row(
        term="GO:0005681", tree_reading="REASON_CONTRADICTED", outcome="adjudicate",
        verifier={"agrees": False, "problem": "The reading and the false claim hold; the replacement overstates."},
    )
    rows = [
        agreed,
        faulted,
        # the review changed on main after the reading: a new reading is needed, so it is in neither class
        row(term="GO:0005682", tree_reading="REASON_CONTRADICTED", outcome="adjudicate", verifier=AGREED, outcome_detail=tr.NOT_REAPPLIED),
        row(term="GO:0005683", tree_reading="REASON_CONTRADICTED", outcome="applied", verifier=AGREED),
        row(term="GO:0005684", tree_reading="NOT_A_TREE_ARGUMENT", outcome="adjudicate", verifier={"agrees": False, "problem": "x"}),
    ]
    assert tr.standing_contradictions(rows) == [agreed]
    assert tr.disputed_contradictions(rows) == [faulted]


def test_the_worklist_marks_and_counts_both_kinds_of_contradiction(tmp_path: Path) -> None:
    left = row(
        tree_reading="REASON_CONTRADICTED", outcome="adjudicate", verifier=AGREED,
        outcome_detail="the contradicted claim is in summary, which the script does not rewrite",
    )
    faulted = row(
        term="GO:0005681", tree_reading="REASON_CONTRADICTED", outcome="adjudicate",
        verifier={"agrees": False, "problem": "The finding holds; the drafted reason overstates."},
        outcome_detail="the verifier disagrees with the reading",
    )
    moved = row(term="GO:0005682", tree_reading="REASON_CONTRADICTED", outcome="adjudicate", verifier=AGREED, outcome_detail=tr.NOT_REAPPLIED)
    noted = row(term="GO:0005683", outcome="applied", note="the failure mode no longer fits")
    plain = row(term="GO:0005684", outcome="applied")
    (tmp_path / "g900.yaml").write_text(
        tr.dump({"batch": "g900", "rows": [left, faulted, moved, noted, plain]}), encoding="utf-8"
    )

    worklist = tr.worklist(tmp_path)

    assert worklist["counts"] == {
        "adjudicate": 3, "not_read": 0, "applied_with_note": 1, "contradicted_and_left": 1, "contradiction_disputed": 1,
        "needs_new_reading": 1,
    }
    by_term = {entry["term"]: entry for entry in worklist["adjudicate"]}
    assert by_term["GO:0000398"]["contradicted_and_left"] is True and "contradiction_disputed" not in by_term["GO:0000398"]
    assert by_term["GO:0005681"]["contradiction_disputed"] is True and "contradicted_and_left" not in by_term["GO:0005681"]
    assert by_term["GO:0005681"]["verifier_problem"] == "The finding holds; the drafted reason overstates."
    assert not {"contradicted_and_left", "contradiction_disputed"} & set(by_term["GO:0005682"])
    # the review changed on main after the reading: what the entry says describes the review as it was read
    assert by_term["GO:0005682"]["needs_new_reading"] is True
    assert not any(entry.get("needs_new_reading") for term, entry in by_term.items() if term != "GO:0005682")
    assert [entry["term"] for entry in worklist["applied_with_note"]] == ["GO:0005683"]


def test_the_committed_worklist_agrees_with_its_own_counts() -> None:
    worklist = tr.worklist()
    for key in ("contradicted_and_left", "contradiction_disputed"):
        marked = [entry for entry in worklist["adjudicate"] if entry.get(key)]
        assert worklist["counts"][key] == len(marked)
        assert all(entry["tree_reading"] == "REASON_CONTRADICTED" for entry in marked)
        assert key in worklist["about"]
    moved = [entry for entry in worklist["adjudicate"] if entry.get("needs_new_reading")]
    # no lower bound here: the count goes to 0 once these rows are read again (the fixture test has a row)
    assert worklist["counts"]["needs_new_reading"] == len(moved)
    assert all(entry["outcome_detail"].startswith(tr.NOT_REAPPLIED) for entry in moved)
    assert not any(entry.get("contradicted_and_left") or entry.get("contradiction_disputed") for entry in moved)


def test_the_worklist_says_what_its_markers_cover() -> None:
    about = tr.worklist()["about"]
    # a contradiction the verifier never saw is disputed too, and the gloss has to say so
    assert "or never saw the row" in about
    # a row not re-applied keeps its fields as read
    assert "needs_new_reading" in about and "as it was read" in about


def test_a_row_whose_review_changed_on_main_needs_a_new_reading() -> None:
    moved = row(outcome="adjudicate", outcome_detail=tr.NOT_REAPPLIED + ": the review changed on main after the reading")
    assert tr.needs_new_reading(moved)
    assert not tr.needs_new_reading(row(outcome="adjudicate", outcome_detail="the verifier disagrees with the reading"))
    assert not tr.needs_new_reading(row(outcome="applied"))


def test_what_finish_reports_about_a_batch_beyond_its_outcomes() -> None:
    left = row(
        tree_reading="REASON_CONTRADICTED", outcome="adjudicate", verifier=AGREED,
        outcome_detail="the contradicted claim is in summary, which the script does not rewrite",
    )
    faulted = [
        row(term=term, tree_reading="REASON_CONTRADICTED", outcome="adjudicate", verifier={"agrees": False, "problem": "x"})
        for term in ("GO:0005681", "GO:0005682")
    ]
    record = {"batch": "g900", "rows": [left, *faulted, row(term="GO:0005683", outcome="applied")], tr.NOT_LISTED: {"human/OTHER": "no references list"}}

    lines = tr.batch_notes(record)

    assert lines[0] == "  human/OTHER: tree file not listed under references: no references list"
    assert "human/TEST" in lines[1] and "GO:0000398" in lines[1] and "correct it by hand" in lines[1]
    assert lines[2].startswith("  2 rows where a contradiction was read") and "new reading" in lines[2]
    assert len(lines) == 3
    assert tr.batch_notes({"batch": "g901", "rows": [row(outcome="applied")]}) == []
