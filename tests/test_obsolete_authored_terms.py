"""Tests for the obsolete author-supplied GO term check.

The check exists because neither of the two mechanisms that validate term ids
reaches an obsolete id an author wrote. ``existing_annotations[].term.id`` is
deliberately not hard-validated (those ids come from GOA, which is trusted),
and the ``core_functions`` dynamic enums test branch *reachability*, which an
obsoleted term still satisfies. So an author-supplied retired id passes today.
"""

from pathlib import Path

import pytest

from ai_gene_review.validation.obsolete_authored_terms import (
    OBSOLETE_AUTHORED_CHECK,
    AuthoredTerm,
    check_obsolete_authored_terms,
    goa_obsolete_labels,
    iter_authored_go_terms,
)
from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)


def paths(data) -> list[str]:
    return [t.path for t in iter_authored_go_terms(data)]


def curies(data) -> list[str]:
    return [t.curie for t in iter_authored_go_terms(data)]


# --------------------------------------------------------------------------
# Which slots count as author-supplied
# --------------------------------------------------------------------------


def test_proposed_replacement_terms_are_authored():
    data = {
        "existing_annotations": [
            {
                "term": {"id": "GO:0000001", "label": "a"},
                "review": {
                    "action": "MODIFY",
                    "proposed_replacement_terms": [
                        {"id": "GO:0000002", "label": "b"},
                        {"id": "GO:0000003", "label": "c"},
                    ],
                },
            }
        ]
    }
    assert curies(data) == ["GO:0000002", "GO:0000003"]
    assert paths(data) == [
        "existing_annotations[0].review.proposed_replacement_terms[0]",
        "existing_annotations[0].review.proposed_replacement_terms[1]",
    ]


def test_goa_supplied_term_is_not_authored():
    """A reviewed GOA row's own term id came from GOA, so it is not checked.

    This is the deliberate asymmetry in CLAUDE.md: machine-sourced ids are
    trusted, author-supplied ids are checked.
    """
    data = {
        "existing_annotations": [
            {"term": {"id": "GO:0000001", "label": "a"}, "review": {"action": "ACCEPT"}}
        ]
    }
    assert curies(data) == []


@pytest.mark.parametrize("action", ["ACCEPT", "REMOVE", "TOO_GENERAL", "UNDECIDED"])
def test_non_new_actions_do_not_make_the_row_term_authored(action):
    data = {
        "existing_annotations": [
            {"term": {"id": "GO:0000001", "label": "a"}, "review": {"action": action}}
        ]
    }
    assert curies(data) == []


def test_new_row_term_is_authored():
    """A NEW row is an annotation the reviewer proposes, so its id is theirs."""
    data = {
        "existing_annotations": [
            {"term": {"id": "GO:0000009", "label": "n"}, "review": {"action": "NEW"}}
        ]
    }
    assert curies(data) == ["GO:0000009"]
    assert paths(data) == ["existing_annotations[0].term"]


@pytest.mark.parametrize(
    "slot,expected_path",
    [
        ("molecular_function", "core_functions[0].molecular_function"),
        (
            "contributes_to_molecular_function",
            "core_functions[0].contributes_to_molecular_function",
        ),
        ("in_complex", "core_functions[0].in_complex"),
    ],
)
def test_single_valued_core_function_slots(slot, expected_path):
    data = {"core_functions": [{slot: {"id": "GO:0000004", "label": "d"}}]}
    assert curies(data) == ["GO:0000004"]
    assert paths(data) == [expected_path]


@pytest.mark.parametrize(
    "slot",
    ["directly_involved_in", "locations", "anatomical_locations", "substrates"],
)
def test_multivalued_core_function_slots(slot):
    data = {"core_functions": [{slot: [{"id": "GO:0000005", "label": "e"}]}]}
    assert curies(data) == ["GO:0000005"]
    assert paths(data) == [f"core_functions[0].{slot}[0]"]


def test_proposed_parent_is_authored():
    data = {
        "proposed_new_terms": [
            {
                "proposed_name": "x",
                "proposed_parent": {"id": "GO:0000006", "label": "f"},
            }
        ]
    }
    assert curies(data) == ["GO:0000006"]
    assert paths(data) == ["proposed_new_terms[0].proposed_parent"]


def test_ntr_placeholder_is_skipped():
    """``NTR`` is the schema's marker for a term that does not exist yet."""
    data = {
        "existing_annotations": [
            {
                "term": {"id": "GO:0000001", "label": "a"},
                "review": {
                    "action": "MODIFY",
                    "proposed_replacement_terms": [
                        {"id": "NTR", "label": "holdase activity"}
                    ],
                },
            }
        ]
    }
    assert curies(data) == []


def test_non_go_prefixes_are_skipped():
    data = {"core_functions": [{"in_complex": {"id": "CHEBI:1234", "label": "c"}}]}
    assert curies(data) == []


def test_empty_document_yields_nothing():
    assert list(iter_authored_go_terms({})) == []
    assert list(iter_authored_go_terms(None)) == []


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

OBSOLETE_DOC = {
    "core_functions": [
        {"molecular_function": {"id": "GO:0051082", "label": "unfolded protein binding"}}
    ]
}


def lookup_obsolete(curie: str):
    if curie == "GO:0051082":
        return [("GO snapshot", "obsolete unfolded protein binding")]
    return []


def lookup_live(curie: str):
    return [("GO snapshot", "unfolded protein binding")]


def test_obsolete_term_is_reported_as_a_warning():
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, lookup_obsolete)
    assert len(report.issues) == 1
    issue = report.issues[0]
    assert issue.severity == ValidationSeverity.WARNING
    assert issue.check_type == OBSOLETE_AUTHORED_CHECK
    assert issue.path == "core_functions[0].molecular_function"
    assert "GO:0051082" in issue.message


def test_warning_names_the_source_that_detected_the_obsoletion():
    """Which signal fired matters: the snapshot and the GOA files disagree."""
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, lookup_obsolete)
    assert "GO snapshot" in report.issues[0].message


def test_warning_does_not_invalidate_the_file():
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, lookup_obsolete)
    assert report.is_valid


def test_live_term_is_not_reported():
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, lookup_live)
    assert report.issues == []


def test_each_obsolete_slot_is_reported_once():
    data = {
        "core_functions": [
            {
                "molecular_function": {"id": "GO:0051082", "label": "u"},
                "locations": [{"id": "GO:0051082", "label": "u"}],
            }
        ]
    }
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(data, report, lookup_obsolete)
    assert len(report.issues) == 2


def test_authored_term_is_hashable_and_ordered():
    """Deterministic output: callers sort and de-duplicate these."""
    a = AuthoredTerm(path="p", curie="GO:1", label="x")
    assert a == AuthoredTerm(path="p", curie="GO:1", label="x")
    assert len({a, AuthoredTerm(path="p", curie="GO:1", label="x")}) == 1


# --------------------------------------------------------------------------
# The GOA label index
# --------------------------------------------------------------------------

GOA_HEADER = (
    "GENE PRODUCT DB\tGENE PRODUCT ID\tSYMBOL\tQUALIFIER\tGO TERM\tGO NAME\t"
    "GO ASPECT\tECO ID\tGO EVIDENCE CODE\tREFERENCE\tWITH/FROM\tTAXON ID\t"
    "TAXON NAME\tASSIGNED BY\tGENE NAME\tDATE"
)


def write_goa(root: Path, rel: str, rows: list[tuple[str, str, str]]) -> None:
    path = root / "genes" / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [GOA_HEADER]
    for term, name, date in rows:
        lines.append(
            "UniProtKB\tP1\tg\tinvolved_in\t"
            + term
            + "\t"
            + name
            + "\tbiological_process\tECO:1\tIEA\tGO_REF:1\t\t9606\tHuman\tGOC\tn\t"
            + date
        )
    path.write_text("\n".join(lines) + "\n")


def test_goa_index_collects_obsolete_prefixed_labels(tmp_path):
    write_goa(
        tmp_path,
        "human/A/A-goa.tsv",
        [("GO:0098734", "obsolete macromolecule depalmitoylation", "20260727")],
    )
    index = goa_obsolete_labels(tmp_path)
    assert "GO:0098734" in index
    label, source = index["GO:0098734"]
    assert label == "obsolete macromolecule depalmitoylation"
    assert "A-goa.tsv" in source


def test_goa_index_ignores_live_labels(tmp_path):
    write_goa(tmp_path, "human/A/A-goa.tsv", [("GO:0008474", "palmitoyl", "20260727")])
    assert goa_obsolete_labels(tmp_path) == {}


def test_goa_index_reads_the_whole_corpus_not_one_gene(tmp_path):
    """The gene's own GOA file can be a stale fetch while a sibling's is fresh.

    This is the CPT1C case: ``CPT1C-goa.tsv`` carried the unprefixed label from
    a 20260106 fetch while four other genes' files carried the ``obsolete``
    prefix from 20260727. A per-gene check would have missed it.
    """
    write_goa(
        tmp_path, "human/STALE/STALE-goa.tsv", [("GO:0098734", "macromolecule", "20260106")]
    )
    write_goa(
        tmp_path,
        "DANRE/fresh/fresh-goa.tsv",
        [("GO:0098734", "obsolete macromolecule", "20260727")],
    )
    index = goa_obsolete_labels(tmp_path)
    assert "GO:0098734" in index
    assert "fresh-goa.tsv" in index["GO:0098734"][1]


def test_goa_index_names_a_deterministic_source(tmp_path):
    """Several files can carry the same obsoletion; the message must not vary.

    The row's ``DATE`` is the annotation date, not the fetch date, so it cannot
    rank the files -- here the alphabetically first one wins, and the old
    annotation date on it is deliberately not preferred away.
    """
    write_goa(tmp_path, "human/A/A-goa.tsv", [("GO:0000111", "obsolete x", "20250101")])
    write_goa(tmp_path, "human/B/B-goa.tsv", [("GO:0000111", "obsolete x", "20260727")])
    assert "A-goa.tsv" in goa_obsolete_labels(tmp_path)["GO:0000111"][1]


def test_one_prefixed_file_outweighs_many_unprefixed(tmp_path):
    """A majority of unprefixed rows does not clear a term.

    GO:0005615 was carried as ``extracellular space`` by 218 GOA files and as
    ``obsolete extracellular space`` by six; QuickGO confirms the six. A stale
    file misses an obsoletion, it does not invent one.
    """
    for name in "CDEFGH":
        write_goa(
            tmp_path, f"human/{name}/{name}-goa.tsv", [("GO:0005615", "live", "20200101")]
        )
    write_goa(
        tmp_path, "human/B/B-goa.tsv", [("GO:0005615", "obsolete live", "20200101")]
    )
    assert "GO:0005615" in goa_obsolete_labels(tmp_path)


def test_goa_index_on_empty_corpus(tmp_path):
    assert goa_obsolete_labels(tmp_path) == {}


# --------------------------------------------------------------------------
# Wiring
# --------------------------------------------------------------------------


@pytest.mark.integration
def test_check_runs_as_part_of_best_practices():
    """The check fires through ``check_best_practices_rules``, not only alone.

    Uses the real corpus GOA index (``check_ontology`` defaults to False, so
    the GO snapshot is not consulted). ``GO:0008379`` is obsolete in the
    corpus' own GOA files, which is how the one existing corpus hit was found.
    """
    from ai_gene_review.validation.validator import check_best_practices_rules

    data = {
        "core_functions": [
            {
                "molecular_function": {
                    "id": "GO:0008379",
                    "label": "thioredoxin peroxidase activity",
                }
            }
        ]
    }
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_best_practices_rules(data, report, check_supporting_text=False)
    hits = [i for i in report.issues if i.check_type == OBSOLETE_AUTHORED_CHECK]
    assert len(hits) == 1
    assert hits[0].severity == ValidationSeverity.WARNING
