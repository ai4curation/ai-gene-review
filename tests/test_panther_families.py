"""Tests for the PANTHER family/subfamily artifact builders.

The OBO artifact only earns its keep if OAK can actually read it back, so the
round-trip test drives a generated file through the same ``simpleobo:`` adapter
that ``conf/oak_config.yaml`` configures -- including the awkward
``PANTHER:PTHR1:SF2`` CURIE, whose second colon several OAK backends mishandle.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.etl.panther_families import (
    PantherEntry,
    UniProtPantherLookup,
    emit_yaml_scalar,
    label_drift,
    lookup_from_uniprot_payload,
    MemberIndexConflict,
    build_member_index,
    incremental_member_index,
    load_member_index,
    load_member_index_alternates,
    load_member_index_gaps,
    member_index_path,
    panther_assignments_conflict,
    parse_hmm_classifications,
    parse_sequence_classification,
    render_obo,
    rewrite_panther_labels,
    write_member_index,
    write_panther_obo,
)
from ai_gene_review.validation.module_validator import validate_family_members

PROJECT_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def entries() -> list[PantherEntry]:
    return [
        PantherEntry("PTHR13337", "SUCCINATE DEHYDROGENASE"),
        PantherEntry("PTHR13337:SF6", "SDHD, MITOCHONDRIAL"),
        PantherEntry("PTHR11375", "ACIDIC LEUCINE-RICH NUCLEAR PHOSPHOPROTEIN 32"),
    ]


@pytest.mark.parametrize(
    "line,expected",
    [
        ("PTHR1\tNAME\textra", [("PTHR1", "NAME")]),
        ("PTHR1:SF2\tSUBNAME", [("PTHR1:SF2", "SUBNAME")]),
        ("PTHR1\t", []),  # no name
        ("NOTPANTHER\tNAME", []),  # not a PANTHER accession
        ("", []),  # blank
        ("PTHR1", []),  # single column
    ],
)
def test_parse_hmm_classifications_filters_rows(line, expected):
    parsed = [(e.accession, e.name) for e in parse_hmm_classifications([line])]
    assert parsed == expected


def test_render_obo_orders_subfamilies_numerically():
    entries = [
        PantherEntry("PTHR1:SF10", "TEN"),
        PantherEntry("PTHR1:SF2", "TWO"),
        PantherEntry("PTHR1", "FAM"),
    ]
    ids = [line for line in render_obo(entries) if line.startswith("id:")]
    assert ids == [
        "id: PANTHER:PTHR1",
        "id: PANTHER:PTHR1:SF2",
        "id: PANTHER:PTHR1:SF10",
    ]


def test_write_panther_obo_is_readable_by_oak(tmp_path, entries):
    """The whole design rests on OAK reading this back through simpleobo:."""
    from oaklib import get_adapter

    path = write_panther_obo(entries, tmp_path / "panther.obo")
    adapter = get_adapter(f"simpleobo:{path}")

    assert adapter.label("PANTHER:PTHR13337") == "SUCCINATE DEHYDROGENASE"
    assert adapter.label("PANTHER:PTHR13337:SF6") == "SDHD, MITOCHONDRIAL"
    assert adapter.label("PANTHER:PTHR99999") is None
    assert list(adapter.hierarchical_parents("PANTHER:PTHR13337:SF6")) == [
        "PANTHER:PTHR13337"
    ]


def test_write_panther_obo_is_deterministic(tmp_path, entries):
    first = write_panther_obo(entries, tmp_path / "a.obo").read_text()
    second = write_panther_obo(list(reversed(entries)), tmp_path / "b.obo").read_text()
    assert first == second


def test_parse_sequence_classification_skips_rows_without_uniprot():
    rows = [
        "HUMAN|HGNC=10683|UniProtKB=O14521\tO14521\tSDHD\tPTHR13337:SF6\tSDH",
        "HUMAN|HGNC=1|Gene=xyz\t\tXYZ\tPTHR1:SF1\tX",
        "HUMAN|UniProtKB=P00001\tP00001\tNOFAM\t\t",
        "short\trow",
    ]
    assert parse_sequence_classification(rows) == {"O14521": "PTHR13337:SF6"}


def test_member_index_round_trip(tmp_path):
    index = {"O14521": "PTHR13337:SF6", "P00001": "PTHR1"}
    path = write_member_index(index, tmp_path / "members.tsv")
    assert load_member_index(path) == index
    assert load_member_index_gaps(path) == (set(), set(), set())


def test_member_index_round_trips_unresolved_accessions(tmp_path):
    """The unresolved block must survive write -> read without polluting rows."""
    index = {"O14521": "PTHR13337:SF6"}
    path = write_member_index(index, tmp_path / "members.tsv", {"Q88ND1", "Q94ET8"})

    assert load_member_index(path) == index, "comments must not become rows"
    assert load_member_index_gaps(path).absent == {"Q88ND1", "Q94ET8"}


def test_member_index_records_that_uniprot_was_not_consulted(tmp_path):
    """Under --no-uniprot-fallback the file must not claim UniProt was checked.

    Writing "not found in UniProt" when UniProt was never asked puts a false
    statement into a committed artifact -- worse than the omission the block
    replaced, because silence is recoverable and a confident wrong claim is not.
    """
    checked = write_member_index({"P1": "PTHR1"}, tmp_path / "a.tsv", {"P9"}).read_text()
    skipped = write_member_index(
        {"P1": "PTHR1"}, tmp_path / "b.tsv", unchecked={"P9"}
    ).read_text()

    assert "UniProt's xref_panther" in checked
    assert "NOT consulted" not in checked
    assert "NOT consulted" in skipped
    assert "unchecked rather than absent" in skipped

    # The MARKER must differ too, not only the prose. A shared marker lets a
    # consumer read a skipped lookup as a completed one and report "no PANTHER
    # family exists" about a protein nobody asked about -- which moves the false
    # claim out of the artifact and into the tool's output.
    asked = load_member_index_gaps(tmp_path / "a.tsv")
    skipped_gaps = load_member_index_gaps(tmp_path / "b.tsv")
    assert (asked.absent, asked.unchecked, asked.unknown) == ({"P9"}, set(), set())
    assert (skipped_gaps.absent, skipped_gaps.unchecked, skipped_gaps.unknown) == (
        set(),
        {"P9"},
        set(),
    )


def test_an_unknown_accession_is_not_labelled_as_a_skipped_lookup(tmp_path):
    """The artifact must not claim a flag was passed that never was."""
    path = write_member_index(
        {"P1": "PTHR1"}, tmp_path / "m.tsv", unknown={"TYPO"}
    )
    text = path.read_text()

    assert "no-uniprot-fallback" not in text
    assert "returned no record for" in text
    gaps = load_member_index_gaps(path)
    assert (gaps.absent, gaps.unchecked, gaps.unknown) == (set(), set(), {"TYPO"})


def test_load_member_index_missing_file_is_empty(tmp_path):
    """A fresh checkout must degrade to 'not checkable', not crash."""
    assert load_member_index(tmp_path / "absent.tsv") == {}


def test_build_member_index_retains_uncited_classified_accessions(tmp_path):
    source = tmp_path / "org"
    source.write_text(
        "HUMAN|UniProtKB=O14521\tO14521\tSDHD\tPTHR13337:SF6\tSDH\n"
        "HUMAN|UniProtKB=P99999\tP99999\tOTHER\tPTHR1:SF1\tX\n"
    )
    assert build_member_index({"O14521"}, [source]) == {
        "O14521": "PTHR13337:SF6",
        "P99999": "PTHR1:SF1",
    }


def test_build_member_index_tolerates_missing_files(tmp_path):
    assert build_member_index({"O14521"}, [tmp_path / "nope"]) == {}


def test_committed_panther_obo_covers_ids_used_in_modules():
    """Guard against the artifact drifting out of sync with cited ids."""
    obo = PROJECT_ROOT / "interpro" / "panther" / "panther.obo"
    if not obo.exists():
        pytest.skip("panther.obo not built; run `just build-panther-obo`")
    ids = {
        line.split("id: ", 1)[1]
        for line in obo.read_text().splitlines()
        if line.startswith("id: ")
    }
    assert "PANTHER:PTHR13337" in ids
    assert "PANTHER:PTHR13337:SF6" in ids
    assert len(ids) > 100_000


# --------------------------------------------------------------------------- #
# Label repair
# --------------------------------------------------------------------------- #

NAMES = {"PANTHER:PTHR1": "REAL NAME", "PANTHER:PTHR1:SF2": "REAL SUB"}


# "REAL NAME" vs "REAL NAMES OF THINGS" stays cosmetic; use a near-miss label so
# these fixtures exercise the rewrite path rather than the divergence guard.
NEAR = "REAL NAMED"


def test_rewrite_panther_labels_handles_list_item_form():
    """`family_terms` entries are list items (`- id:`), indented past the dash."""
    text = f"  family_terms:\n    - id: PANTHER:PTHR1\n      label: {NEAR}\n"
    new, changes, deferred = rewrite_panther_labels(text, NAMES)
    assert changes == [("PANTHER:PTHR1", NEAR, "REAL NAME")]
    assert deferred == []
    assert new == "  family_terms:\n    - id: PANTHER:PTHR1\n      label: REAL NAME\n"


def test_rewrite_panther_labels_skips_disputed_grounding():
    """Relabelling a mis-grounded id would hide it behind an official name."""
    text = f"  term:\n    id: PANTHER:PTHR1\n    label: {NEAR}\n"
    new, changes, _ = rewrite_panther_labels(
        text, NAMES, skip_curies={"PANTHER:PTHR1"}
    )
    assert changes == []
    assert new == text


def test_rewrite_panther_labels_defers_divergent_labels():
    """A label naming a different protein means the ID is probably wrong.

    A randomly guessed id that happens to resolve is still a hallucination, so
    normalising its label would manufacture consistency and hide the error.
    """
    text = "  term:\n    id: PANTHER:PTHR1\n    label: SUCCINATE DEHYDROGENASE\n"
    new, changes, deferred = rewrite_panther_labels(text, NAMES)
    assert changes == []
    assert deferred == [("PANTHER:PTHR1", "SUCCINATE DEHYDROGENASE", "REAL NAME")]
    assert new == text


def test_rewrite_panther_labels_allow_divergent_overrides():
    text = "  term:\n    id: PANTHER:PTHR1\n    label: SUCCINATE DEHYDROGENASE\n"
    new, changes, deferred = rewrite_panther_labels(
        text, NAMES, allow_divergent=True
    )
    assert len(changes) == 1
    assert deferred == []
    assert "label: REAL NAME" in new


def test_rewrite_panther_labels_is_idempotent():
    text = f"  term:\n    id: PANTHER:PTHR1\n    label: {NEAR}\n"
    once, _, _ = rewrite_panther_labels(text, NAMES)
    twice, changes, deferred = rewrite_panther_labels(once, NAMES)
    assert (changes, deferred) == ([], [])
    assert twice == once


def test_rewrite_panther_labels_ignores_unknown_and_unadjacent():
    unknown = "  term:\n    id: PANTHER:PTHR999\n    label: whatever\n"
    assert rewrite_panther_labels(unknown, NAMES)[1] == []

    # A `label:` at the wrong indent belongs to a different mapping.
    misaligned = f"  term:\n    id: PANTHER:PTHR1\n  label: {NEAR}\n"
    assert rewrite_panther_labels(misaligned, NAMES)[1] == []


def test_rewrite_panther_labels_quotes_when_needed():
    names = {"PANTHER:PTHR1": "REAL NAME: WITH COLON"}
    text = f"  term:\n    id: PANTHER:PTHR1\n    label: {NEAR}\n"
    new, _, _ = rewrite_panther_labels(text, names)
    assert '    label: "REAL NAME: WITH COLON"\n' in new
    assert yaml.safe_load(new)["term"]["label"] == "REAL NAME: WITH COLON"


@pytest.mark.parametrize(
    "old,new,expected",
    [
        ("ALDO-KETO REDUCTASE", "ALDO/KETO REDUCTASE", "cosmetic"),
        ("SUBGROUP III AMINOTRANSFERASE", "SUBGROUP IIII AMINOTRANSFERASE", "cosmetic"),
        ("XANTHINE DEHYDROGENASE OXIDASE", "XANTHINE PHOSPHORIBOSYLTRANSFERASE", "partial"),
        # The real SDHD/ANP32 mis-grounding found on main.
        (
            "SUCCINATE DEHYDROGENASE CYTOCHROME B SMALL SUBUNIT",
            "ACIDIC LEUCINE-RICH NUCLEAR PHOSPHOPROTEIN 32",
            "divergent",
        ),
        # Uninformative words alone must not count as agreement.
        ("ZINC FINGER PROTEIN", "MEMBRANE TRANSPORT PROTEIN", "divergent"),
    ],
)
def test_label_drift_classification(old, new, expected):
    assert label_drift(old, new) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ("PLAIN NAME", "PLAIN NAME"),
        ("HAS: COLON", '"HAS: COLON"'),
        ("#HASH", '"#HASH"'),
        # Embedded quotes are legal in a plain scalar; only leading ones aren't.
        ('HAS "QUOTE"', 'HAS "QUOTE"'),
    ],
)
def test_emit_yaml_scalar(value, expected):
    assert emit_yaml_scalar(value) == expected


def test_rewrite_panther_labels_fills_a_placeholder_label():
    """`label: PTHR13190` is a missing label, not a claim about another protein.

    The divergence guard exists to stop a label naming a *different* protein
    being overwritten, since that means the id was guessed. An id shares no
    words with its own official name, so without this exception every
    placeholder reads as divergent and is deferred forever -- which is how a
    module merged to main with this convention broke CI.
    """
    names = {"PANTHER:PTHR13190": "AUTOPHAGY-RELATED 2, ISOFORM A"}
    text = "  term:\n    id: PANTHER:PTHR13190\n    label: PTHR13190\n"

    new, applied, deferred = rewrite_panther_labels(text, names)

    assert deferred == []
    assert applied == [
        ("PANTHER:PTHR13190", "PTHR13190", "AUTOPHAGY-RELATED 2, ISOFORM A")
    ]
    assert "label: AUTOPHAGY-RELATED 2, ISOFORM A" in new


def test_rewrite_panther_labels_still_defers_a_real_divergence():
    """The placeholder exception must not weaken the guard it sits inside."""
    names = {"PANTHER:PTHR11375": "ACIDIC LEUCINE-RICH NUCLEAR PHOSPHOPROTEIN 32"}
    text = (
        "  term:\n    id: PANTHER:PTHR11375\n"
        "    label: SUCCINATE DEHYDROGENASE CYTOCHROME B SMALL SUBUNIT\n"
    )

    new, applied, deferred = rewrite_panther_labels(text, names)

    assert applied == []
    assert len(deferred) == 1
    assert new == text


def test_member_index_footer_has_no_count(tmp_path):
    """A count line changes with every PR and turns each merge into a conflict."""
    text = write_member_index({"P1": "PTHR1"}, tmp_path / "m.tsv", {"P8", "P9"}).read_text()
    assert "accession(s)" not in text
    assert "# unresolved: P8" in text and "# unresolved: P9" in text


def test_load_member_index_rejects_conflicting_families(tmp_path):
    path = tmp_path / "m.tsv"
    path.write_text("uniprot_accession\tpanther_family_sf\nP1\tPTHR1\nP1\tPTHR2\n")
    with pytest.raises(MemberIndexConflict):
        load_member_index(path)


def test_incremental_refresh_keeps_existing_rows():
    """The default refresh must not re-resolve or rewrite rows it already has."""
    asked = []

    def resolve(acc):
        asked.append(set(acc))
        return {a: "PTHR_NEW" for a in acc}

    out = incremental_member_index({"P1": "PTHR_OLD"}, {"P1", "P2"}, resolve)
    assert out == {"P1": "PTHR_OLD", "P2": "PTHR_NEW"}
    assert asked == [{"P2"}]
    assert incremental_member_index({"P1": "PTHR_OLD"}, {"P1"}, resolve) == {"P1": "PTHR_OLD"}
    assert len(asked) == 1, "nothing missing, so nothing to resolve"



def test_member_index_round_trips_alternates(tmp_path):
    """UniProt's disagreeing family is a third column the primary loader ignores."""
    index = {"O14521": "PTHR13337:SF6", "P00001": "PTHR1"}
    path = write_member_index(
        index, tmp_path / "members.tsv", alternates={"O14521": "PTHR11375:SF2"}
    )

    assert load_member_index(path) == index
    assert load_member_index_alternates(path) == {"O14521": "PTHR11375:SF2"}
    assert "O14521\tPTHR13337:SF6\tPTHR11375:SF2" in path.read_text()


def test_load_member_index_alternates_reads_two_column_files(tmp_path):
    path = write_member_index({"O14521": "PTHR13337:SF6"}, tmp_path / "members.tsv")
    assert load_member_index_alternates(path) == {}
    assert load_member_index_alternates(tmp_path / "missing.tsv") == {}


def test_a_record_without_a_panther_xref_is_still_seen():
    """A UniProt hit without xref_panther is not the same as no UniProt hit."""
    payload = {
        "results": [
            {
                "primaryAccession": "HASXREF",
                "uniProtKBCrossReferences": [
                    {"database": "PANTHER", "id": "PTHR1:SF2"}
                ],
            },
            {
                "primaryAccession": "NOXREF",
                "uniProtKBCrossReferences": [{"database": "Pfam", "id": "PF00001"}],
            },
        ]
    }

    lookup = lookup_from_uniprot_payload(payload)

    assert lookup.families == {"HASXREF": "PTHR1:SF2"}
    assert lookup.seen == {"HASXREF", "NOXREF"}
    assert "NEVERASKED" not in lookup.seen


def test_refresh_records_accessions_uniprot_never_returned_separately(
    tmp_path, monkeypatch
):
    """A typo'd or invented member must not be called "PANTHER has no family"."""
    from typer.testing import CliRunner

    from ai_gene_review.cli import app

    repo = tmp_path
    (repo / "modules").mkdir()

    def _member(accession: str) -> dict:
        return {"term": {"id": f"UniProtKB:{accession}", "label": accession}}

    (repo / "modules" / "m.yaml").write_text(
        yaml.safe_dump(
            {
                "module": {
                    "id": "m",
                    "parts": [
                        {
                            "node": {
                                "annotons": [
                                    {
                                        "participant": {
                                            "family": {
                                                "term": {
                                                    "id": "PANTHER:PTHR9",
                                                    "label": "f",
                                                },
                                                "representative_members": [
                                                    _member("REAL"),
                                                    _member("TYPO"),
                                                ],
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ],
                }
            }
        )
    )
    monkeypatch.setattr(
        "ai_gene_review.etl.panther_families.fetch_sequence_classification",
        lambda slug, cache: None,
    )
    # REAL exists but carries no PANTHER xref; TYPO is not in UniProt at all.
    monkeypatch.setattr(
        "ai_gene_review.etl.panther_families.fetch_panther_from_uniprot",
        lambda accessions: UniProtPantherLookup({}, {"REAL"}),
    )

    result = CliRunner().invoke(
        app, ["refresh-panther-members", "--output-dir", str(repo)]
    )

    assert result.exit_code == 0, result.output
    gaps = load_member_index_gaps(member_index_path(repo))
    assert gaps.absent == {"REAL"}, "a returned record with no xref is absent"
    assert gaps.unknown == {"TYPO"}, "asked-and-not-returned is its own state"
    assert gaps.unchecked == set()


def test_fix_panther_labels_passes_unknown_accessions_to_the_validator(
    tmp_path, monkeypatch
):
    """The label fixer should feed all member-index gaps to the shared check."""
    from typer.testing import CliRunner

    from ai_gene_review.cli import app

    repo = tmp_path
    (repo / "modules").mkdir()
    panther = repo / "interpro" / "panther"
    panther.mkdir(parents=True)
    write_panther_obo([PantherEntry("PTHR9", "OFFICIAL NAME")], panther / "panther.obo")
    write_member_index({}, member_index_path(repo), unknown={"TYPO"})
    module = repo / "modules" / "m.yaml"
    module.write_text(
        "module:\n"
        "  id: m\n"
        "  parts:\n"
        "  - node:\n"
        "      annotons:\n"
        "      - participant:\n"
        "          family:\n"
        "            term:\n"
        "              id: PANTHER:PTHR9\n"
        "              label: OFFICIAL NAME\n"
        "            representative_members:\n"
        "            - term:\n"
        "                id: UniProtKB:TYPO\n"
        "                label: rep\n"
    )

    seen: list[set[str]] = []

    def _validate(*args, unknown_to_uniprot=None, **kwargs):
        seen.append(unknown_to_uniprot)
        return ["unindexed"], []

    monkeypatch.setattr(
        "ai_gene_review.validation.module_validator.validate_family_members",
        _validate,
    )

    result = CliRunner().invoke(app, ["fix-panther-labels", "--output-dir", str(repo)])

    assert result.exit_code == 0, result.output
    assert seen == [{"TYPO"}]


def test_validate_family_members_does_not_exempt_a_memberless_descriptor():
    """An empty set is a subset of anything, so the guard must test emptiness."""
    from ai_gene_review.validation.module_validator import FamilyMemberUse

    use = FamilyMemberUse(
        path="$.family.term",
        declared_family_curies=frozenset({"PANTHER:PTHR13337"}),
        representative_accessions=frozenset(),
    )

    errors, warnings = validate_family_members([use], {}, permanently_absent={"X"})

    assert not any("PANTHER has no family for" in w for w in warnings)
    assert len(errors) == 1
    assert "none of the representative members" in errors[0]


def test_the_error_for_an_unknown_accession_does_not_advise_a_refresh():
    """A refresh can never resolve a typo, so advising one is a loop."""
    from ai_gene_review.validation.module_validator import iter_family_member_uses

    doc = {
        "family": {
            "term": {"id": "PANTHER:PTHR13337", "label": "f"},
            "representative_members": [
                {"term": {"id": "UniProtKB:Q88ND9", "label": "typo"}}
            ],
        }
    }
    uses = list(iter_family_member_uses(doc))

    errors, _ = validate_family_members(
        uses, {}, unknown_to_uniprot={"Q88ND9"}
    )

    assert len(errors) == 1
    assert "refresh-panther-members" not in errors[0]
    assert "verify the accession exists" in errors[0]
    assert "Q88ND9" in errors[0]


@pytest.mark.parametrize(
    "first, second, expected",
    [
        ("PTHR1:SF2", "PTHR1", False),
        ("PTHR1", "PTHR1:SF2", False),
        ("PTHR1:SF2", "PTHR1:SF3", True),
        ("PTHR1", "PTHR9", True),
    ],
)
def test_panther_assignments_conflict(first, second, expected):
    assert panther_assignments_conflict(first, second) is expected


def test_load_member_overrides_requires_a_reason(tmp_path):
    from ai_gene_review.etl.panther_families import load_member_overrides

    path = tmp_path / "overrides.tsv"
    path.write_text("uniprot_accession\tpanther_family_sf\treason\nP1\tPTHR1:SF2\t\n")
    with pytest.raises(ValueError, match="non-empty"):
        load_member_overrides(path)


def test_load_member_overrides_rejects_duplicate_accessions(tmp_path):
    from ai_gene_review.etl.panther_families import load_member_overrides

    path = tmp_path / "overrides.tsv"
    path.write_text(
        "uniprot_accession\tpanther_family_sf\treason\n"
        "P1\tPTHR1:SF2\tfirst\n"
        "P1\tPTHR9\tsecond\n"
    )

    with pytest.raises(ValueError) as exc:
        load_member_overrides(path)

    message = str(exc.value)
    assert "duplicate override for 'P1'" in message
    assert ":3:" in message
    assert "line 2" in message


def test_apply_member_overrides_wins_over_classification(tmp_path):
    from ai_gene_review.etl.panther_families import (
        apply_member_overrides,
        load_member_overrides,
    )

    path = tmp_path / "overrides.tsv"
    path.write_text(
        "uniprot_accession\tpanther_family_sf\treason\n"
        "P1\tPTHR1:SF2\tcurated\n"
        "P9\tPTHR9\tno longer cited\n"
    )
    merged = apply_member_overrides(
        {"P1": "PTHR5:SF1", "P2": "PTHR2"}, load_member_overrides(path), {"P1", "P2"}
    )
    assert merged == {"P1": "PTHR1:SF2", "P2": "PTHR2"}


def test_repo_member_overrides_are_reflected_in_index():
    from ai_gene_review.etl.panther_families import load_member_overrides

    panther_dir = PROJECT_ROOT / "interpro" / "panther"
    overrides = load_member_overrides(panther_dir / "panther-members-overrides.tsv")
    members_path = member_index_path(PROJECT_ROOT)
    if not members_path.exists():
        pytest.skip("member index not built (run just refresh-panther-members)")
    index = load_member_index(members_path)
    for accession, (family_sf, _reason) in overrides.items():
        if accession in index:
            assert index[accession] == family_sf, accession
