"""Tests for the PANTHER family/subfamily artifact builders.

The OBO artifact only earns its keep if OAK can actually read it back, so the
round-trip test drives a generated file through the same ``simpleobo:`` adapter
that ``conf/oak_config.yaml`` configures -- including the awkward
``PANTHER:PTHR1:SF2`` CURIE, whose second colon several OAK backends mishandle.
"""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.validation.module_validator import validate_family_members
from ai_gene_review.etl.panther_families import (
    PantherEntry,
    emit_yaml_scalar,
    label_drift,
    rewrite_panther_labels,
    build_member_index,
    load_member_index,
    load_member_index_gaps,
    UniProtPantherLookup,
    lookup_from_uniprot_payload,
    parse_hmm_classifications,
    parse_sequence_classification,
    render_obo,
    write_member_index,
    write_panther_obo,
)

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
    assert load_member_index_gaps(path) == (set(), set())


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
    checked = write_member_index(
        {"P1": "PTHR1"}, tmp_path / "a.tsv", {"P9"}
    ).read_text()
    skipped = write_member_index(
        {"P1": "PTHR1"}, tmp_path / "b.tsv", None, {"P9"}
    ).read_text()

    assert "UniProt's xref_panther" in checked
    assert "NOT run" not in checked
    assert "NOT run" in skipped
    assert "unchecked rather than absent" in skipped

    # The MARKER must differ too, not only the prose. A shared marker lets a
    # consumer read a skipped lookup as a completed one and report "no PANTHER
    # family exists" about a protein nobody asked about -- which moves the false
    # claim out of the artifact and into the tool's output.
    asked = load_member_index_gaps(tmp_path / "a.tsv")
    skipped_gaps = load_member_index_gaps(tmp_path / "b.tsv")
    assert (asked.absent, asked.unchecked) == ({"P9"}, set())
    assert (skipped_gaps.absent, skipped_gaps.unchecked) == (set(), {"P9"})


def test_load_member_index_missing_file_is_empty(tmp_path):
    """A fresh checkout must degrade to 'not checkable', not crash."""
    assert load_member_index(tmp_path / "absent.tsv") == {}


def test_build_member_index_retains_uncited_accessions(tmp_path):
    """The index must not be pruned to what is currently cited.

    Pruning made the artifact lag the repository by construction: a PR citing a
    new protein found the index silent about exactly the protein under review,
    so the member-consistency check -- the only one that can catch a guessed
    family id -- was skipped rather than run. Across the open-PR backlog that
    silently disabled 78% of those checks.
    """
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


def test_refresh_merges_rather_than_replaces(tmp_path, monkeypatch):
    """`--no-uniprot-fallback` must not delete UniProt-resolved rows.

    A UniProt xref row can only be produced by asking UniProt, so a run that
    skips the fallback rebuilds the index without them. Before this, that
    dropped 436 of the 1,457 cited accessions -- and since a missing accession
    is now an error, the command documented as the remedy would have been the
    thing that turned the repository red.
    """
    from typer.testing import CliRunner

    from ai_gene_review.cli import app

    repo = tmp_path
    (repo / "modules").mkdir()
    panther = repo / "interpro" / "panther"
    panther.mkdir(parents=True)
    # Q00000 could only have come from a previous UniProt lookup: it is in no
    # organism classification here.
    (panther / "panther-members.tsv").write_text(
        "uniprot_accession\tpanther_family_sf\nQ00000\tPTHR9:SF1\n"
    )
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
                                                    {
                                                        "term": {
                                                            "id": "UniProtKB:Q00000",
                                                            "label": "r",
                                                        }
                                                    }
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

    result = CliRunner().invoke(
        app,
        [
            "refresh-panther-members",
            "--output-dir",
            str(repo),
            "--no-uniprot-fallback",
        ],
    )

    assert result.exit_code == 0, result.output
    assert load_member_index(panther / "panther-members.tsv") == {"Q00000": "PTHR9:SF1"}


def test_a_skipped_refresh_preserves_absence_for_the_others(tmp_path, monkeypatch):
    """One newly-cited accession must not relabel every absent one as unchecked.

    The old guard was all-or-nothing: it kept the `# unresolved` markers only if
    EVERY still-unresolved accession was already absent. Cite one new protein
    and a `--no-uniprot-fallback` run rewrote all 35 absent lines as
    `# unchecked`, emptying the set the validator uses to exempt them --
    restoring the permanent-error bug via the command documented as its remedy,
    and asserting in a committed artifact that 35 proteins were never looked up
    when they were.
    """
    from typer.testing import CliRunner

    from ai_gene_review.cli import app

    repo = tmp_path
    (repo / "modules").mkdir()
    panther = repo / "interpro" / "panther"
    panther.mkdir(parents=True)
    # OLD is known to have no PANTHER family; NEW has never been looked up.
    write_member_index({}, panther / "panther-members.tsv", {"OLD"}, None)

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
                                                    _member("OLD"),
                                                    _member("NEW"),
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

    result = CliRunner().invoke(
        app,
        ["refresh-panther-members", "--output-dir", str(repo), "--no-uniprot-fallback"],
    )

    assert result.exit_code == 0, result.output
    gaps = load_member_index_gaps(panther / "panther-members.tsv")
    assert gaps.absent == {"OLD"}, "a prior verdict must survive a skipped run"
    assert gaps.unchecked == {"NEW"}


def test_fix_panther_labels_is_not_deadlocked_by_an_absent_member(tmp_path):
    """A provably-absent member must not freeze its label mismatch forever.

    Escalating "unindexed" to an error puts the descriptor in `skip`, which is
    right for a stale index -- a disputed grounding should not have its label
    rewritten. But for an accession PANTHER has no family for, no refresh can
    ever clear it, so the validator reports the label mismatch as a blocking
    error while this tool permanently refuses to touch the label.
    """
    from typer.testing import CliRunner

    from ai_gene_review.cli import app

    repo = tmp_path
    (repo / "modules").mkdir()
    panther = repo / "interpro" / "panther"
    panther.mkdir(parents=True)
    write_panther_obo([PantherEntry("PTHR9", "OFFICIAL NAME")], panther / "panther.obo")
    write_member_index({}, panther / "panther-members.tsv", {"ABSENT"}, None)
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
        "              label: official name\n"
        "            representative_members:\n"
        "            - term:\n"
        "                id: UniProtKB:ABSENT\n"
        "                label: rep\n"
    )

    result = CliRunner().invoke(
        app, ["fix-panther-labels", "--output-dir", str(repo), "--apply"]
    )

    assert result.exit_code == 0, result.output
    assert "OFFICIAL NAME" in module.read_text(), result.output


def test_an_accession_uniprot_never_returned_is_not_recorded_as_absent(
    tmp_path, monkeypatch
):
    """A typo'd or invented member must not be called "PANTHER has no family".

    fetch_panther_from_uniprot used to return only successes, so a record that
    came back without an xref_panther and an accession UniProt has never heard of
    were indistinguishable. Both landed under `# unresolved:`, which feeds
    permanently_absent, which downgrades the grounding check to a warning saying
    "PANTHER has no family for (...)" -- committing a positive claim about a
    protein that may not exist, and silencing the check on the permissive side of
    a distinction nobody drew.
    """
    from typer.testing import CliRunner

    from ai_gene_review.cli import app

    repo = tmp_path
    (repo / "modules").mkdir()
    panther = repo / "interpro" / "panther"
    panther.mkdir(parents=True)
    write_member_index({}, panther / "panther-members.tsv")

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
    gaps = load_member_index_gaps(panther / "panther-members.tsv")
    assert gaps.absent == {"REAL"}, "a returned record with no xref is genuinely absent"
    assert gaps.unchecked == {"TYPO"}, "an accession UniProt never returned is unknown"


def test_a_record_without_a_panther_xref_is_still_seen():
    """The distinction the whole exemption rests on, at its source.

    Returning only successes discarded the fact that UniProt had answered at
    all, so "real protein, PANTHER does not classify it" and "no such accession"
    became the same thing one layer up.
    """
    payload = {
        "results": [
            {"primaryAccession": "HASXREF", "uniProtKBCrossReferences": [
                {"database": "PANTHER", "id": "PTHR1:SF2"}
            ]},
            {"primaryAccession": "NOXREF", "uniProtKBCrossReferences": [
                {"database": "Pfam", "id": "PF00001"}
            ]},
        ]
    }

    lookup = lookup_from_uniprot_payload(payload)

    assert lookup.families == {"HASXREF": "PTHR1:SF2"}
    assert lookup.seen == {"HASXREF", "NOXREF"}
    # An accession never returned appears in neither.
    assert "NEVERASKED" not in lookup.seen


def test_validate_family_members_does_not_exempt_a_memberless_descriptor():
    """An empty set is a subset of anything, so the guard must test emptiness.

    Unreachable through iter_family_member_uses, which requires a member -- but
    validate_family_members is public, and an exemption firing for a descriptor
    naming no members would silently pass the one case with nothing to check.
    """
    from ai_gene_review.validation.module_validator import FamilyMemberUse

    use = FamilyMemberUse(
        path="$.family.term",
        declared_family_curies=frozenset({"PANTHER:PTHR13337"}),
        representative_accessions=frozenset(),
    )

    errors, warnings = validate_family_members([use], {}, permanently_absent={"X"})

    assert not any("PANTHER has no family for" in w for w in warnings)
