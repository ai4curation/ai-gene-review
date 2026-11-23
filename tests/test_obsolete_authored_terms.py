"""Tests for the obsolete author-supplied GO term check.

The check exists because neither of the two mechanisms that validate term ids
reaches an obsolete id an author wrote. ``existing_annotations[].term.id`` is
deliberately not hard-validated (those ids come from GOA, which is trusted),
and the ``core_functions`` dynamic enums test branch *reachability*, which an
obsoleted term still satisfies. So an author-supplied retired id passes today.
"""

from pathlib import Path

import pytest

from ai_gene_review.validation.module_validator import is_obsolete_label
from ai_gene_review.validation.obsolete_authored_terms import (
    OBSOLETE_AUTHORED_CHECK,
    AuthoredTerm,
    build_label_lookup,
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
        return [("the GO snapshot", "obsolete unfolded protein binding")]
    return []


def lookup_live(curie: str):
    return [("the GO snapshot", "unfolded protein binding")]


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
    assert "the GO snapshot" in report.issues[0].message


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


def test_authored_term_is_hashable():
    """Callers de-duplicate these; ordering is not used, so it is not declared.

    ``order=True`` would raise TypeError comparing a None label with a str.
    """
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
    """A majority of unprefixed files does not clear a term.

    This is `GO:0005615` as the corpus actually held it: 218 rows across 88
    files carried `extracellular space`, against six rows in the *single* file
    `genes/human/ANG/ANG-goa.tsv` carrying `obsolete extracellular space` --
    and QuickGO confirms that one file. So the fixture writes one prefixed file
    against many unprefixed ones, not six against six: a stale file misses an
    obsoletion, it does not invent one, and the rule is not a vote.
    """
    for name in "CDEFGH":
        write_goa(
            tmp_path, f"human/{name}/{name}-goa.tsv", [("GO:0005615", "live", "20200101")]
        )
    write_goa(
        tmp_path, "human/B/B-goa.tsv", [("GO:0005615", "obsolete live", "20200101")]
    )
    index = goa_obsolete_labels(tmp_path)
    assert "GO:0005615" in index
    assert index["GO:0005615"][1] == "genes/human/B/B-goa.tsv"


def test_new_row_extensions_are_authored():
    """``extensions[].term`` is author-written on a NEW row, GOA's elsewhere."""
    data = {
        "existing_annotations": [
            {
                "term": {"id": "GO:0000020", "label": "t"},
                "extensions": [
                    {"predicate": "part_of", "term": {"id": "GO:0000021", "label": "e"}}
                ],
                "review": {"action": "NEW"},
            },
            {
                "term": {"id": "GO:0000022", "label": "u"},
                "extensions": [
                    {"predicate": "part_of", "term": {"id": "GO:0000023", "label": "f"}}
                ],
                "review": {"action": "ACCEPT"},
            },
        ]
    }
    assert curies(data) == ["GO:0000020", "GO:0000021"]
    assert paths(data)[1] == "existing_annotations[0].extensions[0].term"


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


# --------------------------------------------------------------------------
# Review round 1: slot coverage and citation precision
# --------------------------------------------------------------------------


def test_isoform_specific_terms_are_authored():
    """``functional_isoforms[].isoform_specific_terms[]`` is a fifth authored slot.

    It is `range: Term`, author-written, and in use in 24 corpus reviews, so
    omitting it left a real coverage hole.
    """
    data = {
        "functional_isoforms": [
            {
                "isoform_id": "P1-2",
                "isoform_specific_terms": [
                    {"id": "GO:0000007", "label": "g"},
                    {"id": "GO:0000008", "label": "h"},
                ],
            }
        ]
    }
    assert curies(data) == ["GO:0000007", "GO:0000008"]
    assert paths(data) == [
        "functional_isoforms[0].isoform_specific_terms[0]",
        "functional_isoforms[0].isoform_specific_terms[1]",
    ]


def test_proposed_ontology_changes_are_deliberately_not_walked():
    """Its ``Term`` slots name retired terms on purpose -- that is their job.

    ``about_node``, ``has_direct_replacement`` and ``has_nondirect_replacement``
    are author-supplied and `range: Term`, so they look like candidates; walking
    them would flag every correctly-recorded obsoletion.
    """
    data = {
        "proposed_ontology_changes": [
            {
                "about_node": {"id": "GO:0051082", "label": "unfolded protein binding"},
                "has_direct_replacement": {"id": "GO:0000010", "label": "x"},
            }
        ]
    }
    assert curies(data) == []


def test_goa_source_is_a_repo_relative_path(tmp_path):
    """A bare basename is ambiguous: two organisms can share a gene symbol."""
    write_goa(
        tmp_path, "yeast/ACO2/ACO2-goa.tsv", [("GO:0000112", "obsolete y", "20260101")]
    )
    _, source = goa_obsolete_labels(tmp_path)["GO:0000112"]
    assert source == "genes/yeast/ACO2/ACO2-goa.tsv"


def test_distinct_organisms_sharing_a_symbol_are_distinguishable(tmp_path):
    write_goa(
        tmp_path, "human/ACO2/ACO2-goa.tsv", [("GO:0000113", "obsolete z", "20260101")]
    )
    write_goa(
        tmp_path, "yeast/ACO2/ACO2-goa.tsv", [("GO:0000114", "obsolete z", "20260101")]
    )
    index = goa_obsolete_labels(tmp_path)
    assert index["GO:0000113"][1] == "genes/human/ACO2/ACO2-goa.tsv"
    assert index["GO:0000114"][1] == "genes/yeast/ACO2/ACO2-goa.tsv"


def test_issue_details_record_the_written_and_detected_labels():
    """``AuthoredTerm.label`` was collected but never surfaced anywhere."""
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, lookup_obsolete)
    details = report.issues[0].details
    assert details is not None
    assert details["written_label"] == "unfolded protein binding"
    assert details["detected_labels"] == ["obsolete unfolded protein binding"]
    assert details["detected_by_sources"] == ["the GO snapshot"]


def test_lookup_does_not_scan_the_corpus_until_a_term_is_looked_up(tmp_path):
    """Building the lookup must be free: most files have no authored GO ids."""
    calls = []

    def counting_scan(root):
        calls.append(root)
        return {}

    lookup = build_label_lookup(
        tmp_path, use_ontology=False, goa_index_loader=counting_scan
    )
    assert calls == []
    lookup("GO:0000001")
    assert calls == [tmp_path.resolve()]
    lookup("GO:0000002")
    assert calls == [tmp_path.resolve()], "the index should be built at most once"


# --------------------------------------------------------------------------
# Review round 4: corroboration by both signals
# --------------------------------------------------------------------------


def lookup_both_signals(curie: str):
    """Both offline signals mark the term obsolete -- the strongest case."""
    if curie == "GO:0051082":
        return [
            ("GOA file genes/human/X/X-goa.tsv", "obsolete unfolded protein binding"),
            ("the GO snapshot", "obsolete unfolded protein binding"),
        ]
    return []


def test_both_signals_are_named_not_just_the_first():
    """Corroboration must not read like a single-signal hit.

    Which signal fired is the useful part of this check, so a term both the
    corpus GOA files and the GO snapshot mark obsolete is the strongest case it
    can make.
    """
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, lookup_both_signals)
    assert len(report.issues) == 1
    issue = report.issues[0]
    assert "GOA file genes/human/X/X-goa.tsv" in issue.message
    assert "the GO snapshot" in issue.message
    assert issue.details is not None
    assert len(issue.details["detected_by_sources"]) == 2
    assert issue.details["detected_by_sources"] == [
        "GOA file genes/human/X/X-goa.tsv",
        "the GO snapshot",
    ]


def test_single_signal_reports_one_source():
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, lookup_obsolete)
    assert report.issues[0].details["detected_by_sources"] == ["the GO snapshot"]


def test_a_live_signal_alongside_an_obsolete_one_is_not_counted():
    """Only signals that actually say "obsolete" are named.

    A stale snapshot reporting the live label while a GOA file reports the
    obsoletion is the normal case, not corroboration.
    """

    def mixed(curie: str):
        return [
            ("GOA file genes/human/X/X-goa.tsv", "obsolete unfolded protein binding"),
            ("the GO snapshot", "unfolded protein binding"),
        ]

    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, mixed)
    assert report.issues[0].details["detected_by_sources"] == [
        "GOA file genes/human/X/X-goa.tsv"
    ]
    assert "the GO snapshot" not in report.issues[0].message


def test_cached_index_is_read_only(tmp_path):
    """The cached dict is process-wide; handing out the mutable original makes
    "nothing mutates it" an observed invariant rather than an enforced one.

    Keyed on ``tmp_path``, so this asserts the property without scanning the
    real 12,281-file corpus and without depending on pytest's cwd.
    """
    from ai_gene_review.validation.obsolete_authored_terms import (
        _cached_goa_obsolete_labels,
    )

    write_goa(tmp_path, "human/A/A-goa.tsv", [("GO:0000115", "obsolete q", "20260101")])
    index = _cached_goa_obsolete_labels(tmp_path.resolve())
    assert "GO:0000115" in index
    with pytest.raises(TypeError):
        index["GO:0000001"] = ("x", "y")  # type: ignore[index]


# --------------------------------------------------------------------------
# Review round 5: per-source labels and the live-signal trace
# --------------------------------------------------------------------------


def test_divergent_labels_are_attributed_per_source():
    """Independent fetches can word the same obsoletion differently.

    Showing one label for both sources would assert something neither said.
    """

    def divergent(curie: str):
        return [
            ("GOA file genes/human/X/X-goa.tsv", "obsolete unfolded protein binding"),
            ("the GO snapshot", "obsolete chaperone binding"),
        ]

    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, divergent)
    message = report.issues[0].message
    assert 'genes/human/X/X-goa.tsv ("obsolete unfolded protein binding")' in message
    assert 'the GO snapshot ("obsolete chaperone binding")' in message
    assert report.issues[0].details["detected_labels"] == [
        "obsolete unfolded protein binding",
        "obsolete chaperone binding",
    ]


def test_agreeing_labels_are_not_repeated():
    """When the sources agree, the label is stated once, not per source."""
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, lookup_both_signals)
    message = report.issues[0].message
    assert message.count("obsolete unfolded protein binding") == 1
    assert (
        'GOA file genes/human/X/X-goa.tsv and the GO snapshot '
        '("obsolete unfolded protein binding")' in message
    )


def test_sources_are_queryable_as_a_list():
    """``details`` is JSON-serialised, so consumers should not split a string."""
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, lookup_both_signals)
    assert report.issues[0].details["detected_by_sources"] == [
        "GOA file genes/human/X/X-goa.tsv",
        "the GO snapshot",
    ]


def test_a_live_signal_is_recorded_not_discarded():
    """The stale-snapshot disagreement is kept, without counting as a hit."""

    def mixed(curie: str):
        return [
            ("GOA file genes/human/X/X-goa.tsv", "obsolete unfolded protein binding"),
            ("the GO snapshot", "unfolded protein binding"),
        ]

    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, mixed)
    details = report.issues[0].details
    assert details["detected_by_sources"] == ["GOA file genes/human/X/X-goa.tsv"]
    assert details["live_according_to"] == ["the GO snapshot"]


def test_no_live_signal_leaves_an_empty_trace():
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, lookup_both_signals)
    assert report.issues[0].details["live_according_to"] == []


def test_goa_index_never_yields_a_live_label(tmp_path):
    """Why ``live_according_to`` can only ever name the snapshot.

    ``goa_obsolete_labels`` indexes a row only when its label already carries
    the ``obsolete `` prefix, so the GOA pair ``lookup`` appends is always a hit
    and can never be the live source. This pins that structurally, because it
    is what bounds the field's domain -- the GOA-versus-GOA disagreement
    (CPT1C's own stale file versus its fresh siblings) is not recordable.
    """
    write_goa(
        tmp_path,
        "human/A/A-goa.tsv",
        [("GO:0000116", "live label", "20260101"), ("GO:0000117", "obsolete x", "20260101")],
    )
    index = goa_obsolete_labels(tmp_path)
    assert set(index) == {"GO:0000117"}
    assert all(is_obsolete_label(label) for label, _ in index.values())


def test_a_label_containing_quotes_reads_cleanly():
    """GO labels contain single quotes, so the wrapping must not nest.

    The corpus holds `obsolete 'de novo' NAD+ biosynthetic process from
    L-tryptophan`; wrapping that in single quotes produced three apostrophes in
    a row and no way to see where the label ended.
    """

    def quoted(curie: str):
        return [("the GO snapshot", "obsolete 'de novo' NAD+ biosynthetic process")]

    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, quoted)
    assert (
        'the GO snapshot ("obsolete \'de novo\' NAD+ biosynthetic process")'
        in report.issues[0].message
    )


def test_consulted_sources_distinguishes_silence_from_not_asking(tmp_path):
    """An empty ``live_according_to`` means two different things without this.

    With ``use_ontology=False`` the snapshot is never consulted at all -- the
    whole ``--no-ontology`` audit path, and a plain ``validate`` without
    ``--terms`` -- so an empty list would read as "nothing disagreed" when it
    means "nothing was asked". That is the ambiguity the field itself exists to
    remove, so it must not reproduce it.
    """
    write_goa(
        tmp_path, "human/A/A-goa.tsv", [("GO:0051082", "obsolete unfolded", "20260101")]
    )
    doc = {"core_functions": [{"molecular_function": {"id": "GO:0051082", "label": "u"}}]}

    offline = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(
        doc,
        offline,
        build_label_lookup(tmp_path, use_ontology=False, snapshot_available=lambda: True),
    )
    assert offline.issues[0].details["consulted_sources"] == ["the corpus GOA files"]
    assert offline.issues[0].details["live_according_to"] == []


def test_consulted_sources_lists_the_snapshot_when_it_can_answer(tmp_path):
    write_goa(tmp_path, "human/A/A-goa.tsv", [("GO:0000118", "live", "20260101")])
    lookup = build_label_lookup(
        tmp_path, use_ontology=True, snapshot_available=lambda: True
    )
    assert lookup.consulted_sources() == [  # type: ignore[attr-defined]
        "the corpus GOA files",
        "the GO snapshot",
    ]


def test_a_configured_but_unloadable_snapshot_is_not_reported_as_consulted(tmp_path):
    """Configured is not consulted, and the difference is observable.

    `_get_cached_adapter` returns None when the OAK build cannot load and
    remembers the failure, so every snapshot lookup then returns None. Reporting
    it as consulted would recreate, one level down, the ambiguity this field
    exists to remove -- the reader could not tell "asked, nothing to say" from
    "never loaded".
    """
    write_goa(tmp_path, "human/A/A-goa.tsv", [("GO:0000119", "live", "20260101")])
    lookup = build_label_lookup(
        tmp_path, use_ontology=True, snapshot_available=lambda: False
    )
    assert lookup.consulted_sources() == ["the corpus GOA files"]  # type: ignore[attr-defined]


def test_the_probe_is_not_called_at_build_time(tmp_path):
    """`build_label_lookup` runs per file, so probing there would reload the
    snapshot once for every document, including those with no authored GO ids.

    `use_ontology=True` is load-bearing: `consulted_sources` gates the probe as
    `use_ontology and snapshot_available()`, so with the flag false the probe is
    short-circuited and every assertion here holds vacuously. An earlier version
    of this test passed `False` and therefore survived the very regression it
    names -- verified by mutation, moving the resolution into the builder body
    left it green.

    Only the build-time property is asserted. "A hitless lookup does not probe"
    reads well and cannot fail: `lookup` has no reference to `snapshot_available`
    on any path, so no argument makes it false. An unfalsifiable assertion is
    the thing this file deleted a test for in round 3.
    """
    write_goa(tmp_path, "human/A/A-goa.tsv", [("GO:0000121", "live", "20260101")])
    probes = []

    def probe():
        probes.append(1)
        return True

    lookup = build_label_lookup(tmp_path, use_ontology=True, snapshot_available=probe)
    assert probes == [], "built without probing"

    lookup.consulted_sources()  # type: ignore[attr-defined]
    assert probes == [1], "and the probe is reached when the field is resolved"


def test_consulted_sources_is_none_for_an_injected_lookup():
    """A test double has no such attribute; the check must not require one."""
    report = ValidationReport(file_path=Path("x.yaml"), is_valid=True)
    check_obsolete_authored_terms(OBSOLETE_DOC, report, lookup_obsolete)
    assert report.issues[0].details["consulted_sources"] is None


def test_an_absent_corpus_is_not_reported_as_consulted(tmp_path):
    """The GOA half has the same mute state, and the snapshot fix missed it.

    With no `genes/` tree, `goa_obsolete_labels` returns an empty index
    silently rather than raising, so claiming the corpus was consulted is the
    same false statement the snapshot probe exists to prevent -- on the other
    source in the same expression.
    """
    lookup = build_label_lookup(
        tmp_path, use_ontology=True, snapshot_available=lambda: True
    )
    assert lookup.consulted_sources() == ["the GO snapshot"]  # type: ignore[attr-defined]


def test_neither_source_available_reports_neither(tmp_path):
    lookup = build_label_lookup(
        tmp_path, use_ontology=True, snapshot_available=lambda: False
    )
    assert lookup.consulted_sources() == []  # type: ignore[attr-defined]


def test_availability_is_probed_once(tmp_path):
    """Probed per hit, so the result is memoised in the closure."""
    write_goa(tmp_path, "human/A/A-goa.tsv", [("GO:0000120", "live", "20260101")])
    calls = []

    def probe():
        calls.append(1)
        return True

    lookup = build_label_lookup(tmp_path, use_ontology=True, snapshot_available=probe)
    lookup.consulted_sources()  # type: ignore[attr-defined]
    lookup.consulted_sources()  # type: ignore[attr-defined]
    assert calls == [1]


def test_an_observed_query_failure_makes_the_snapshot_unavailable():
    """Loading is not the only way to be mute.

    `_get_cached_adapter` catches construction failures only; `_snapshot_label`
    separately swallows per-curie query exceptions. A build that loads but
    whose queries raise would otherwise be reported as consulted while mute.
    """
    from ai_gene_review.validation import obsolete_authored_terms as mod

    original = mod._SNAPSHOT_QUERY_FAILED
    try:
        mod._SNAPSHOT_QUERY_FAILED = True
        assert mod._snapshot_adapter_available() is False
    finally:
        mod._SNAPSHOT_QUERY_FAILED = original
