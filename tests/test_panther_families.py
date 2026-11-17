"""Tests for the PANTHER family/subfamily artifact builders.

The OBO artifact only earns its keep if OAK can actually read it back, so the
round-trip test drives a generated file through the same ``simpleobo:`` adapter
that ``conf/oak_config.yaml`` configures -- including the awkward
``PANTHER:PTHR1:SF2`` CURIE, whose second colon several OAK backends mishandle.
"""

import io
import json
import urllib.error
from pathlib import Path

import pytest
import yaml

from ai_gene_review.etl import panther_families
from ai_gene_review.etl.panther_families import (
    PantherEntry,
    fetch_panther_from_uniprot,
    parent_accession,
    emit_yaml_scalar,
    label_drift,
    rewrite_panther_labels,
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
        {"P1": "PTHR1"}, tmp_path / "a.tsv", {"P9"}, consulted_uniprot=True
    ).read_text()
    skipped = write_member_index(
        {"P1": "PTHR1"}, tmp_path / "b.tsv", {"P9"}, consulted_uniprot=False
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
    assert (asked.absent, asked.unchecked) == ({"P9"}, set())
    assert (skipped_gaps.absent, skipped_gaps.unchecked) == (set(), {"P9"})


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


@pytest.mark.parametrize(
    "override, expect_alternate",
    [
        ("PTHR1:SF2", False),  # adopts PANTHER's own placement: UniProt rejected
        ("PTHR9:SF9", False),  # adopts UniProt's value: no conflict left
        (None, True),  # no curated decision: both sources stay accepted
    ],
)
def test_settle_member_alternates(override, expect_alternate):
    from ai_gene_review.etl.panther_families import settle_member_alternates

    overrides = {"P1": (override, "curated")} if override else {}
    index = {"P1": override or "PTHR1:SF2"}
    settled = settle_member_alternates({"P1": "PTHR9:SF9"}, index, overrides)
    assert ("P1" in settled) is expect_alternate


def test_repo_member_overrides_are_reflected_in_index():
    from ai_gene_review.etl.panther_families import load_member_overrides

    panther_dir = PROJECT_ROOT / "interpro" / "panther"
    overrides = load_member_overrides(panther_dir / "panther-members-overrides.tsv")
    members_path = member_index_path(PROJECT_ROOT)
    if not members_path.exists():
        pytest.skip("member index not built (run just refresh-panther-members)")
    index = load_member_index(members_path)
    alternates = load_member_index_alternates(members_path)
    for accession, (family_sf, _reason) in overrides.items():
        if accession in index:
            assert index[accession] == family_sf, accession
            assert accession not in alternates, accession


# --------------------------------------------------------------------------- #
# UniProt fallback: chain and isoform ids, and a poisoned batch
#
# ``/uniprotkb/accessions`` rejects the WHOLE request with HTTP 400 when any id
# in it is not a bare accession, and modules legitimately cite UniProt chain ids
# (``P57764-PRO_0000437526``, the gasdermin-D N-terminal fragment). One such id
# therefore used to abort the entire member-index build, which made
# ``validate-families`` report "not indexed yet" for the whole corpus.
# --------------------------------------------------------------------------- #


def _panther_payload(*records: tuple[str, str]) -> bytes:
    """UniProt-shaped JSON for ``(accession, panther_subfamily)`` pairs."""
    return json.dumps(
        {
            "results": [
                {
                    "primaryAccession": accession,
                    "uniProtKBCrossReferences": [
                        {"database": "PANTHER", "id": family_sf.split(":")[0]},
                        {"database": "PANTHER", "id": family_sf},
                    ],
                }
                for accession, family_sf in records
            ]
        }
    ).encode()


class _FakeResponse(io.BytesIO):
    """Context-manager response, as ``urlopen`` returns."""

    def __enter__(self):  # noqa: D105 - trivial
        return self

    def __exit__(self, *_exc):  # noqa: D105 - trivial
        self.close()
        return False


@pytest.mark.parametrize(
    "cited,expected",
    [
        ("P57764-PRO_0000437526", "P57764"),  # chain (cleavage product)
        ("Q9D8T2-PRO_0000437528", "Q9D8T2"),
        ("P19544-1", "P19544"),  # displayed isoform
        ("Q9UJF2-2", "Q9UJF2"),  # non-displayed isoform
        ("P0AEK4", "P0AEK4"),  # already bare
        ("A0A0B4J2F0", "A0A0B4J2F0"),  # long-form accession, untouched
    ],
)
def test_parent_accession_strips_chain_and_isoform_suffixes(cited, expected):
    assert parent_accession(cited) == expected


def test_fetch_panther_from_uniprot_resolves_chain_ids_through_their_parent(monkeypatch):
    """A cited chain id gets its parent's family, keyed by the id as cited.

    A ``PRO_`` chain has no PANTHER cross-reference of its own, so querying the
    parent is the correct answer rather than merely a way round the 400.
    """
    queried: list[str] = []

    def fake_urlopen(url, timeout=None):
        queried.append(url)
        assert "PRO_" not in url, "chain ids must not reach the endpoint"
        return _FakeResponse(
            _panther_payload(("P57764", "PTHR20750:SF4"), ("P0AEK4", "PTHR43159:SF2"))
        )

    monkeypatch.setattr(panther_families.urllib.request, "urlopen", fake_urlopen)
    resolved = fetch_panther_from_uniprot(
        ["P57764-PRO_0000437526", "P57764", "P0AEK4"]
    )

    assert resolved == {
        "P57764-PRO_0000437526": "PTHR20750:SF4",
        "P57764": "PTHR20750:SF4",
        "P0AEK4": "PTHR43159:SF2",
    }
    # One request, and the parent is asked for once however many of its chains
    # and isoforms are cited.
    assert len(queried) == 1
    assert queried[0].count("P57764") == 1


def test_fetch_panther_from_uniprot_falls_back_per_accession_when_a_batch_is_rejected(
    monkeypatch,
):
    """One unusable id costs one row, not the whole index.

    The suffix stripping above is the fix for the ids we know about; this is the
    guard for the next odd id someone cites, since aborting the build turns a
    single bad row into a corpus-wide "membership not indexed yet".
    """
    calls: list[str] = []

    def fake_urlopen(url, timeout=None):
        calls.append(url)
        if "BOGUS" in url:
            raise urllib.error.HTTPError(url, 400, "Bad Request", {}, None)
        accession = url.split("accessions=")[1].split("&")[0]
        return _FakeResponse(_panther_payload((accession, "PTHR43159:SF2")))

    monkeypatch.setattr(panther_families.urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr(panther_families, "UNIPROT_BATCH_SIZE", 3)

    resolved = fetch_panther_from_uniprot(["P0AEK4", "P0A6R0", "BOGUS_ID"])

    assert resolved == {"P0AEK4": "PTHR43159:SF2", "P0A6R0": "PTHR43159:SF2"}
    # The rejected batch is retried one accession at a time: the batch call plus
    # one call per member of it.
    assert len(calls) == 4


def test_fetch_panther_from_uniprot_gives_up_quietly_on_a_single_bad_accession(monkeypatch):
    def fake_urlopen(url, timeout=None):
        raise urllib.error.HTTPError(url, 400, "Bad Request", {}, None)

    monkeypatch.setattr(panther_families.urllib.request, "urlopen", fake_urlopen)
    assert fetch_panther_from_uniprot(["BOGUS_ID"]) == {}


@pytest.mark.parametrize("code", [429, 500, 503])
def test_fetch_panther_from_uniprot_propagates_transient_http_failures(monkeypatch, code):
    """"Ask again later" must not be recorded as "this protein has no family".

    The caller writes every accession missing from the result under
    ``UNRESOLVED_MARKER``, which ``load_member_index_gaps`` classifies as
    ``absent`` and the next incremental run then treats as ``known_absent`` and
    never re-queries short of ``--rebuild``. Swallowing a 429 or a 5xx would
    therefore turn one throttled request into a sticky false absence for up to a
    whole batch, so only a 400 is tolerated and the rest propagate. One failed
    call must also not fan out into a batch's worth of un-backed-off retries.
    """
    calls: list[str] = []

    def fake_urlopen(url, timeout=None):
        calls.append(url)
        raise urllib.error.HTTPError(url, code, "Transient", {}, None)

    monkeypatch.setattr(panther_families.urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr(panther_families, "UNIPROT_BATCH_SIZE", 3)

    with pytest.raises(urllib.error.HTTPError) as raised:
        fetch_panther_from_uniprot(["P0AEK4", "P0A6R0", "P0A6Q6"])
    assert raised.value.code == code
    assert len(calls) == 1


def test_fetch_panther_from_uniprot_propagates_a_transient_failure_on_one_accession(
    monkeypatch,
):
    """The single-accession path takes the same gate as the batch path."""

    def fake_urlopen(url, timeout=None):
        raise urllib.error.HTTPError(url, 503, "Service Unavailable", {}, None)

    monkeypatch.setattr(panther_families.urllib.request, "urlopen", fake_urlopen)
    with pytest.raises(urllib.error.HTTPError):
        fetch_panther_from_uniprot(["P0AEK4"])


def test_fetch_panther_from_uniprot_propagates_a_transient_failure_during_retries(
    monkeypatch,
):
    """A 400 opens the per-accession retry; a 5xx inside it still propagates."""
    calls: list[str] = []

    def fake_urlopen(url, timeout=None):
        calls.append(url)
        asked = url.split("accessions=")[1].split("&")[0]
        if "%2C" in asked:  # the whole batch in one request
            raise urllib.error.HTTPError(url, 400, "Bad Request", {}, None)
        if "P0A6R0" in asked:
            raise urllib.error.HTTPError(url, 503, "Service Unavailable", {}, None)
        accession = url.split("accessions=")[1].split("&")[0]
        return _FakeResponse(_panther_payload((accession, "PTHR43159:SF2")))

    monkeypatch.setattr(panther_families.urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr(panther_families, "UNIPROT_BATCH_SIZE", 3)

    with pytest.raises(urllib.error.HTTPError) as raised:
        fetch_panther_from_uniprot(["P0AEK4", "P0A6R0", "P0A6Q6"])
    assert raised.value.code == 503
