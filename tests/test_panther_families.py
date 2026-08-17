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
    emit_yaml_scalar,
    label_drift,
    rewrite_panther_labels,
    build_member_index,
    load_member_index,
    load_unresolved_accessions,
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
    assert load_unresolved_accessions(path) == set()


def test_member_index_round_trips_unresolved_accessions(tmp_path):
    """The unresolved block must survive write -> read without polluting rows."""
    index = {"O14521": "PTHR13337:SF6"}
    path = write_member_index(index, tmp_path / "members.tsv", {"Q88ND1", "Q94ET8"})

    assert load_member_index(path) == index, "comments must not become rows"
    assert load_unresolved_accessions(path) == {"Q88ND1", "Q94ET8"}


def test_member_index_records_that_uniprot_was_not_consulted(tmp_path):
    """Under --no-uniprot-fallback the file must not claim UniProt was checked.

    Writing "not found in UniProt" when UniProt was never asked puts a false
    statement into a committed artifact -- worse than the omission the block
    replaced, because silence is recoverable and a confident wrong claim is not.
    """
    checked = write_member_index(
        {"P1": "PTHR1"}, tmp_path / "a.tsv", {"P9"}, consulted_uniprot=True
    ).read_text()
    skipped = write_member_index(
        {"P1": "PTHR1"}, tmp_path / "b.tsv", {"P9"}, consulted_uniprot=False
    ).read_text()

    assert "UniProt's xref_panther" in checked
    assert "NOT consulted" not in checked
    assert "NOT consulted" in skipped
    assert "unchecked rather than absent" in skipped
    # Either way the accession itself round-trips.
    assert load_unresolved_accessions(tmp_path / "b.tsv") == {"P9"}


def test_load_member_index_missing_file_is_empty(tmp_path):
    """A fresh checkout must degrade to 'not checkable', not crash."""
    assert load_member_index(tmp_path / "absent.tsv") == {}


def test_build_member_index_prunes_to_requested_accessions(tmp_path):
    source = tmp_path / "org"
    source.write_text(
        "HUMAN|UniProtKB=O14521\tO14521\tSDHD\tPTHR13337:SF6\tSDH\n"
        "HUMAN|UniProtKB=P99999\tP99999\tOTHER\tPTHR1:SF1\tX\n"
    )
    assert build_member_index({"O14521"}, [source]) == {"O14521": "PTHR13337:SF6"}


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
