"""Tests for the tree-evidence policy on gene-review rows that overrule an IBA."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from ai_gene_review.validation.tree_evidence import (
    adverse_sentences,
    check_tree_evidence,
    phylo_reference_ids,
    quotes_from,
    sentences,
)
from ai_gene_review.validation.validation_report import ValidationReport, ValidationSeverity

REVIEW = Path("genes/human/TEST/TEST-ai-review.yaml")
OWN = "file:human/TEST/TEST-phylo.yaml"
QUOTE = "GO:0000398 (mRNA splicing, via spliceosome): PAINT node PTN000391532 is a speciation node at Eukaryota"


def review(
    action: str = "REMOVE",
    evidence: str = "IBA",
    supported_by: list[dict[str, str]] | None = None,
    propagation_review: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """A gene review with one row on GO:0000398."""
    body: dict[str, Any] = {"action": action, "reason": "x"}
    if supported_by is not None:
        body["supported_by"] = supported_by
    if propagation_review is not None:
        body["propagation_review"] = propagation_review
    return {
        "existing_annotations": [
            {"term": {"id": "GO:0000398", "label": "mRNA splicing, via spliceosome"}, "evidence_type": evidence, "review": body}
        ]
    }


def check(data: dict[str, Any], yaml_file: Path | None = REVIEW) -> list[tuple[str | None, str]]:
    """``(check_type, message)`` of every issue the policy raises."""
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_tree_evidence(data, report, yaml_file)
    assert all(i.severity == ValidationSeverity.WARNING for i in report.issues)
    return [(i.check_type, i.message) for i in report.issues]


def test_phylo_reference_ids_follow_the_review_path() -> None:
    assert phylo_reference_ids(REVIEW) == {OWN, "file:genes/human/TEST/TEST-phylo.yaml"}
    assert phylo_reference_ids(Path("/abs/repo/genes/worm/sta-1/sta-1-ai-review.yaml")) == {
        "file:worm/sta-1/sta-1-phylo.yaml",
        "file:genes/worm/sta-1/sta-1-phylo.yaml",
    }
    # A review outside genes/ has no extract of its own to name.
    assert phylo_reference_ids(Path("tests/input/CFAP300-ai-review.yaml")) == set()
    assert phylo_reference_ids(None) == set()


@pytest.mark.parametrize("action", ["REMOVE", "MARK_AS_OVER_ANNOTATED"])
def test_overruling_an_iba_without_the_tree_warns(action: str) -> None:
    issues = check(review(action))
    assert [kind for kind, _ in issues] == ["missing_tree_evidence"]
    assert "GO:0000398" in issues[0][1] and action in issues[0][1]


def test_overruling_with_the_rows_own_summary_passes() -> None:
    assert check(review(supported_by=[{"reference_id": OWN, "supporting_text": QUOTE}])) == []
    assert check(review(supported_by=[{"reference_id": "file:genes/human/TEST/TEST-phylo.yaml", "supporting_text": QUOTE}])) == []


def test_other_support_does_not_stand_in_for_the_tree() -> None:
    issues = check(review(supported_by=[{"reference_id": "PMID:1", "supporting_text": "no splicing role"}]))
    assert [kind for kind, _ in issues] == ["missing_tree_evidence"]


def test_another_genes_extract_does_not_count() -> None:
    cited = [{"reference_id": "file:human/OTHER/OTHER-phylo.yaml", "supporting_text": QUOTE}]
    assert [kind for kind, _ in check(review(supported_by=cited))] == ["missing_tree_evidence"]


def test_quote_must_be_about_this_row() -> None:
    cited = [{"reference_id": OWN, "supporting_text": "GO:0005681 (spliceosomal complex): PAINT node PTN000391532 is"}]
    issues = check(review(supported_by=cited))
    assert [kind for kind, _ in issues] == ["tree_evidence_other_row"]
    assert "GO:0000398" in issues[0][1]


@pytest.mark.parametrize("action", ["ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "UNDECIDED", "TOO_GENERAL"])
def test_actions_that_keep_the_claim_are_not_asked_for_the_tree(action: str) -> None:
    assert check(review(action)) == []


@pytest.mark.parametrize("evidence", ["IEA", "ISS", "ISO", "IDA"])
def test_only_iba_rows_are_covered(evidence: str) -> None:
    assert check(review(evidence=evidence)) == []


def test_without_a_gene_folder_any_phylo_extract_is_accepted() -> None:
    cited = [{"reference_id": "file:human/OTHER/OTHER-phylo.yaml", "supporting_text": QUOTE}]
    assert check(review(supported_by=cited), yaml_file=None) == []
    assert [kind for kind, _ in check(review(), yaml_file=None)] == ["missing_tree_evidence"]


def test_residue_loss_argument_needs_a_residue_claim() -> None:
    cited = [{"reference_id": OWN, "supporting_text": QUOTE}]
    loss = {"root_cause": "PROPAGATION_BAD", "failure_modes": ["PSEUDO_OR_SUBACTIVITY_LOSS"]}
    issues = check(review(supported_by=cited, propagation_review=loss))
    assert [kind for kind, _ in issues] == ["missing_residue_evidence"]

    with_claim = {**loss, "residue_claims": [{"claim_type": "LOST"}]}
    assert check(review(supported_by=cited, propagation_review=with_claim)) == []
    waived = {**loss, "residue_claims_not_applicable": "capping versus severing, not a point residue"}
    assert check(review(supported_by=cited, propagation_review=waived)) == []


def test_residue_rule_covers_other_propagated_rows_but_only_when_overruled() -> None:
    loss = {"root_cause": "PROPAGATION_BAD", "failure_modes": ["PSEUDO_OR_SUBACTIVITY_LOSS"]}
    assert [k for k, _ in check(review(evidence="IEA", propagation_review=loss))] == ["missing_residue_evidence"]
    assert check(review("KEEP_AS_NON_CORE", evidence="IEA", propagation_review=loss)) == []


def test_rows_without_a_review_are_skipped() -> None:
    assert check({"existing_annotations": [{"term": {"id": "GO:1"}, "evidence_type": "IBA"}, "junk"]}) == []
    assert check({}) == []


GOA_COLUMNS = ["GENE PRODUCT DB", "GENE PRODUCT ID", "SYMBOL", "QUALIFIER", "GO TERM", "GO NAME", "GO ASPECT", "GO EVIDENCE CODE", "WITH/FROM"]


def gene_folder(tmp_path: Path, goa_rows: list[tuple[str, str, str]]) -> Path:
    """A ``genes/human/TEST`` folder whose GOA file holds ``(qualifier, term, evidence)`` rows."""
    folder = tmp_path / "genes" / "human" / "TEST"
    folder.mkdir(parents=True)
    lines = ["\t".join(GOA_COLUMNS)]
    for qualifier, term, evidence in goa_rows:
        lines.append("\t".join(["UniProtKB", "P00001", "TEST", qualifier, term, "a term", "biological_process", evidence, "PANTHER:PTN000391532|UniProtKB:P62995"]))
    (folder / "TEST-goa.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return folder / "TEST-ai-review.yaml"


def test_a_row_still_in_the_goa_file_is_asked_for_the_tree(tmp_path: Path) -> None:
    yaml_file = gene_folder(tmp_path, [("involved_in", "GO:0000398", "IBA")])
    assert [kind for kind, _ in check(review(), yaml_file)] == ["missing_tree_evidence"]


def test_a_row_paint_has_withdrawn_is_not_asked_for_the_tree(tmp_path: Path) -> None:
    # The gene's GOA file no longer has this IBA row, so its extract has no row to quote.
    yaml_file = gene_folder(tmp_path, [("involved_in", "GO:0005681", "IBA"), ("involved_in", "GO:0000398", "IEA")])
    assert check(review(), yaml_file) == []


def test_a_positive_row_is_not_matched_by_a_negated_goa_row(tmp_path: Path) -> None:
    yaml_file = gene_folder(tmp_path, [("NOT|involved_in", "GO:0000398", "IBA")])
    assert check(review(), yaml_file) == []
    negated = review()
    negated["existing_annotations"][0]["negated"] = True
    assert [kind for kind, _ in check(negated, yaml_file)] == ["missing_tree_evidence"]


def test_a_withdrawn_row_is_still_asked_for_its_residue_claim(tmp_path: Path) -> None:
    yaml_file = gene_folder(tmp_path, [("involved_in", "GO:0005681", "IBA")])
    loss = {"root_cause": "PROPAGATION_BAD", "failure_modes": ["PSEUDO_OR_SUBACTIVITY_LOSS"]}
    assert [kind for kind, _ in check(review(propagation_review=loss), yaml_file)] == ["missing_residue_evidence"]


# --- the sentences a verdict has to face ---------------------------------------------

NODE = "GO:0000398 (mRNA splicing, via spliceosome): PAINT node PTN000391532 is a speciation node at Eukaryota, with 373 leaves in 84 species and 21 subfamilies."
PATH = "TEST (PTN002553788, PTHR48034:SF5) is 24 steps below it, across 5 duplications; path length 3.554."
SEEDS = "Seeds: 5 of 5 resolved to leaves of this tree."
ONE_BRANCH_INSIDE = "They all sit in one branch below the node: their common ancestor is PTN002690243, a speciation node at Bilateria, covering 213 leaves, 6 steps below the PAINT node; TEST is inside that clade."
ONE_BRANCH_OUTSIDE = ONE_BRANCH_INSIDE.replace("is inside that clade", "is outside that clade")
BRACKET_SHARED = "They sit in 2 of the 2 branches below the node, so the node is their common ancestor; 3 of them share TEST's own branch below it (PTN000391533)."
BRACKET_ONE_SHARED = BRACKET_SHARED.replace("3 of them share", "1 of the other seeds shares")
BRACKET_NONE = BRACKET_SHARED.replace("3 of them share", "none of them shares")
SELF_SEED = "TEST is itself a seed: its own experimental annotation is among the evidence for the node."
PARALOGS = "By the tree the seeds are 1 ortholog across later duplications and 4 paralogs of TEST."
ORTHOLOGS = "By the tree the seeds are 2 one-to-one orthologs and 4 orthologs across horizontal-transfer nodes of TEST."
NEAREST = "The nearest, RGD:1565256 (RAT), joins TEST at PTN009224850, a duplication node after Craniata-Tunicata before Euteleostomi, at tree distance 1.023; 52% identity over 157 aligned columns, which span 91% of TEST and 40% of the seed."
LOSS = "PAINT IRD at PTN000824099 (20260828) removes this term on the path to TEST."
LOSS_LIFTED = "PAINT IRD at PTN000824099 (20260828) removes this term on the path to TEST, and PAINT asserts it again below the loss at PTN008300302."


def summary(*parts: str) -> str:
    return " ".join(parts)


def test_a_summary_splits_into_sentences_that_join_back() -> None:
    text = summary(NODE, PATH, SEEDS, ONE_BRANCH_INSIDE, PARALOGS, NEAREST)
    assert sentences(text) == [NODE, PATH, SEEDS, ONE_BRANCH_INSIDE, PARALOGS, NEAREST]
    assert " ".join(sentences(text)) == text


def test_quotes_join_neighbouring_sentences_and_always_name_the_term() -> None:
    text = summary(NODE, PATH, SEEDS, ONE_BRANCH_INSIDE, PARALOGS, NEAREST)
    assert quotes_from(text, [5, 4, 6]) == [NODE, f"{ONE_BRANCH_INSIDE} {PARALOGS} {NEAREST}"]
    assert quotes_from(text, [2]) == [f"{NODE} {PATH}"]
    # Numbers that are not sentences of the summary are ignored; sentence 1 is always there.
    assert quotes_from(text, [0, 99]) == [NODE]
    assert all(quote in text for quote in quotes_from(text, [1, 3, 5]))


@pytest.mark.parametrize(
    ("parts", "kwargs", "expected"),
    [
        # Nothing to face: seeds in another branch, the gene outside their clade.
        ((NODE, PATH, SEEDS, ONE_BRANCH_OUTSIDE, PARALOGS, NEAREST), {}, []),
        ((NODE, PATH, SEEDS, BRACKET_NONE, PARALOGS), {}, []),
        # The gene inside the clade the seeds span.
        ((NODE, PATH, SEEDS, ONE_BRANCH_INSIDE, PARALOGS), {}, [(4, "the gene is inside the clade the seeds span")]),
        # Seeds on the gene's own branch below a node they bracket.
        ((NODE, PATH, SEEDS, BRACKET_SHARED, PARALOGS), {}, [(4, "seeds share the gene's own branch below the node")]),
        ((NODE, PATH, SEEDS, BRACKET_ONE_SHARED, SELF_SEED, PARALOGS), {}, [
            (4, "seeds share the gene's own branch below the node"),
            (5, "the gene is itself a seed of the node"),
        ]),
        # A paralog claim against a tree that calls every seed an ortholog.
        ((NODE, PATH, SEEDS, BRACKET_NONE, ORTHOLOGS), {"failure_modes": ["WRONG_ORTHOLOG_OR_PARALOG"]}, [
            (5, "the tree relates every seed to the gene as an ortholog"),
        ]),
        ((NODE, PATH, SEEDS, BRACKET_NONE, ORTHOLOGS), {"failure_modes": ["FUNCTIONAL_DIVERGENCE"]}, []),
        ((NODE, PATH, SEEDS, BRACKET_NONE, PARALOGS), {"failure_modes": ["WRONG_ORTHOLOG_OR_PARALOG"]}, []),
        # A PAINT loss supports an overruling and is in the way of keeping the row.
        ((NODE, PATH, SEEDS, BRACKET_NONE, PARALOGS, LOSS), {}, []),
        ((NODE, PATH, SEEDS, BRACKET_NONE, PARALOGS, LOSS), {"kept": True}, [
            (6, "PAINT has removed the term on the path to the gene"),
        ]),
        ((NODE, PATH, SEEDS, BRACKET_NONE, PARALOGS, LOSS_LIFTED), {"kept": True}, []),
        # A kept row is not asked to face what supports it.
        ((NODE, PATH, SEEDS, ONE_BRANCH_INSIDE, SELF_SEED, PARALOGS), {"kept": True}, []),
    ],
)
def test_adverse_sentences(parts: tuple[str, ...], kwargs: dict[str, Any], expected: list[tuple[int, str]]) -> None:
    found = adverse_sentences(summary(*parts), **kwargs)
    assert [(number, what) for number, what, _ in found] == expected
    assert all(sentence == parts[number - 1] for number, _, sentence in found)


def with_extract(tmp_path: Path, text: str, term: str = "GO:0000398", negated: bool = False) -> Path:
    """A gene folder whose extract has one row with the given summary."""
    yaml_file = gene_folder(tmp_path, [("involved_in", term, "IBA")])
    extract = {"trees": [{"family": "PTHR48034", "rows": [{"term": {"id": term, "label": "x"}, "negated": negated, "summary": text}]}]}
    import yaml

    (yaml_file.parent / "TEST-phylo.yaml").write_text(yaml.safe_dump(extract, width=100000), encoding="utf-8")
    return yaml_file


def quoting(*quotes: str) -> list[dict[str, str]]:
    return [{"reference_id": OWN, "supporting_text": quote} for quote in quotes]


def test_overruling_while_quoting_around_an_adverse_sentence_warns(tmp_path: Path) -> None:
    text = summary(NODE, PATH, SEEDS, ONE_BRANCH_INSIDE, SELF_SEED, PARALOGS)
    yaml_file = with_extract(tmp_path, text)
    issues = check(review(supported_by=quoting(NODE, PARALOGS)), yaml_file)
    assert [kind for kind, _ in issues] == ["tree_evidence_adverse_unquoted"]
    assert "inside the clade the seeds span" in issues[0][1] and "itself a seed" in issues[0][1]
    # Quoting one of the two still leaves the other.
    issues = check(review(supported_by=quoting(NODE, f"{ONE_BRANCH_INSIDE}")), yaml_file)
    assert [kind for kind, _ in issues] == ["tree_evidence_adverse_unquoted"]
    assert "itself a seed" in issues[0][1] and "inside the clade" not in issues[0][1]
    # Quoting both, alone or inside a longer quote, satisfies the check.
    assert check(review(supported_by=quoting(NODE, f"{ONE_BRANCH_INSIDE} {SELF_SEED} {PARALOGS}")), yaml_file) == []


def test_a_row_with_no_adverse_sentence_needs_only_its_own_summary(tmp_path: Path) -> None:
    yaml_file = with_extract(tmp_path, summary(NODE, PATH, SEEDS, ONE_BRANCH_OUTSIDE, PARALOGS))
    assert check(review(supported_by=quoting(NODE)), yaml_file) == []


def test_a_row_that_does_not_cite_the_extract_gets_one_warning_not_two(tmp_path: Path) -> None:
    yaml_file = with_extract(tmp_path, summary(NODE, PATH, SEEDS, ONE_BRANCH_INSIDE, PARALOGS))
    assert [kind for kind, _ in check(review(), yaml_file)] == ["missing_tree_evidence"]


def test_a_paralog_claim_has_to_face_ortholog_only_seeds(tmp_path: Path) -> None:
    yaml_file = with_extract(tmp_path, summary(NODE, PATH, SEEDS, BRACKET_NONE, ORTHOLOGS))
    claim = {"root_cause": "PROPAGATION_BAD", "failure_modes": ["WRONG_ORTHOLOG_OR_PARALOG"]}
    issues = check(review(supported_by=quoting(NODE), propagation_review=claim), yaml_file)
    assert [kind for kind, _ in issues] == ["tree_evidence_adverse_unquoted"]
    assert "every seed to the gene as an ortholog" in issues[0][1]
    assert check(review(supported_by=quoting(NODE, ORTHOLOGS), propagation_review=claim), yaml_file) == []
    other = {"root_cause": "PROPAGATION_BAD", "failure_modes": ["FUNCTIONAL_DIVERGENCE"]}
    assert check(review(supported_by=quoting(NODE), propagation_review=other), yaml_file) == []


@pytest.mark.parametrize("action", ["ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "TOO_GENERAL"])
def test_keeping_a_row_paint_has_removed_warns_until_the_loss_is_quoted(tmp_path: Path, action: str) -> None:
    yaml_file = with_extract(tmp_path, summary(NODE, PATH, SEEDS, BRACKET_NONE, PARALOGS, LOSS))
    issues = check(review(action=action), yaml_file)
    assert [kind for kind, _ in issues] == ["kept_under_paint_loss"]
    assert "PTN000824099" in issues[0][1]
    assert check(review(action=action, supported_by=quoting(LOSS)), yaml_file) == []


def test_a_loss_paint_lifted_below_is_no_obstacle_to_keeping_the_row(tmp_path: Path) -> None:
    yaml_file = with_extract(tmp_path, summary(NODE, PATH, SEEDS, BRACKET_NONE, PARALOGS, LOSS_LIFTED))
    assert check(review(action="ACCEPT"), yaml_file) == []


def test_undecided_rows_and_rows_without_an_extract_are_left_alone(tmp_path: Path) -> None:
    yaml_file = with_extract(tmp_path, summary(NODE, PATH, SEEDS, BRACKET_NONE, PARALOGS, LOSS))
    assert check(review(action="UNDECIDED"), yaml_file) == []
    (yaml_file.parent / "TEST-phylo.yaml").unlink()
    assert check(review(action="ACCEPT"), yaml_file) == []
    assert [kind for kind, _ in check(review(supported_by=quoting(NODE)), yaml_file)] == []


def test_an_extract_row_for_the_negated_annotation_is_not_used_for_the_positive_one(tmp_path: Path) -> None:
    yaml_file = with_extract(tmp_path, summary("NOT " + NODE, PATH, SEEDS, ONE_BRANCH_INSIDE, PARALOGS), negated=True)
    assert check(review(supported_by=quoting(NODE)), yaml_file) == []


def test_a_label_with_a_full_stop_shifts_the_numbering_but_not_the_finding() -> None:
    """Sentences are split at a full stop and a space, which a term label could contain.

    The split is then one fragment longer, but joining gives the text back, the adverse
    statement is still at the end of its fragment, and the quotes are still verbatim; the
    reader and the script number the fragments with this same function.
    """
    node = NODE.replace("mRNA splicing, via spliceosome", "response to St. Louis encephalitis virus")
    text = summary(node, PATH, SEEDS, ONE_BRANCH_INSIDE, PARALOGS)
    parts = sentences(text)
    assert len(parts) == 6 and " ".join(parts) == text
    assert [(number, what) for number, what, _ in adverse_sentences(text)] == [(5, "the gene is inside the clade the seeds span")]
    assert all(quote in text for quote in quotes_from(text, [5]))
