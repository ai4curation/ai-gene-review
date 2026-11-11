"""Tests for the PANTHER release reader (trees with events, node table, family alignment).

The fixture under ``tests/input/panther_release`` is the real PTHR10004 family from the
PANTHER 19.0 TreeGrafter data bundle: eight leaves, with a speciation root, a horizontal
transfer node (AN1) and a duplication node (AN12), so all three event types are covered.
"""

from __future__ import annotations

import io
import tarfile
from pathlib import Path

import pytest

from ai_gene_review.etl.panther_release import (
    FamilyTree,
    PantherRelease,
    build_database,
    column_of_position,
    embed_row,
    pairwise_alignment_stats,
    parse_fasta,
    parse_locus_table,
    parse_long_id,
    parse_node_table,
    parse_tree,
    store_aliases,
    store_sequences,
)

FIXTURES = Path(__file__).parent / "input" / "panther_release"
FAMILY = "PTHR10004"


def _tree() -> FamilyTree:
    nodes = parse_tree((FIXTURES / f"{FAMILY}.tree").read_text())
    table = parse_node_table((FIXTURES / "PAINT_Annotatations_TOTAL.txt").read_text().splitlines())
    return FamilyTree.build(FAMILY, nodes, table[FAMILY])


def _bundle(extra_first: bool = False) -> io.BytesIO:
    """A tar.gz laid out like PANTHER's bundle, built from the fixture files."""
    members = [
        ("PANTHER19.0_data/PAINT_Annotations/PAINT_Annotatations_TOTAL.txt", FIXTURES / "PAINT_Annotatations_TOTAL.txt"),
        (f"PANTHER19.0_data/Tree_MSF/{FAMILY}.AN.fasta", FIXTURES / f"{FAMILY}.AN.fasta"),
        (f"PANTHER19.0_data/Tree_MSF/{FAMILY}.tree", FIXTURES / f"{FAMILY}.tree"),
    ]
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        def add(name: str, data: bytes) -> None:
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))

        if extra_first:
            add("PANTHER19.0_data/README", b"not wanted\n")
        for name, path in members:
            add(name, path.read_bytes())
        add(f"PANTHER19.0_data/Tree_MSF/{FAMILY}.newick", b"(ignored);\n")
        add(f"PANTHER19.0_data/famhmm/{FAMILY}.hmm", b"HMMER3/f\n")
    buf.seek(0)
    return buf


@pytest.fixture()
def release(tmp_path: Path) -> PantherRelease:
    db = tmp_path / "release.sqlite"
    build_database(_bundle(), db, release="19.0", source="fixture")
    return PantherRelease(db)


def test_parse_tree_topology_events_and_lengths() -> None:
    nodes = parse_tree((FIXTURES / f"{FAMILY}.tree").read_text())
    assert len(nodes) == 15
    assert nodes["AN0"].parent is None
    assert nodes["AN0"].children == ("AN1", "AN4")
    assert nodes["AN0"].branch_length is None
    assert (nodes["AN0"].event, nodes["AN0"].taxon) == ("SPECIATION", "Viridiplantae")
    assert (nodes["AN1"].event, nodes["AN1"].taxon) == ("HORIZONTAL_TRANSFER", "")
    assert (nodes["AN12"].event, nodes["AN12"].taxon) == ("DUPLICATION", "")
    assert nodes["AN12"].branch_length == pytest.approx(0.105)
    assert nodes["AN13"].event == "LEAF"
    assert nodes["AN13"].parent == "AN12"
    assert nodes["AN13"].branch_length == pytest.approx(0.030)
    assert nodes["AN13"].long_id == "WHEAT|EnsemblGenome=TraesCS7A02G346100|UniProtKB=A0A3B6RI80"


@pytest.mark.parametrize(
    "text",
    [
        "(AN1:0.1,AN2:0.2)[&&NHX:Ev=0>1:S=SAR/HA_supergroup:ID=AN0];\nAN1:A|Gene=x|UniProtKB=P1;\nAN2:B|Gene=y|UniProtKB=P2;\n",
        "(AN1:0.1,AN2:0.2)[&&NHX:Ev=UNK:ID=AN0];\nAN1:A|Gene=x|UniProtKB=P1;\nAN2:B|Gene=y|UniProtKB=P2;",
    ],
)
def test_parse_tree_handles_slash_taxon_and_unknown_event(text: str) -> None:
    nodes = parse_tree(text)
    assert set(nodes) == {"AN0", "AN1", "AN2"}
    assert nodes["AN0"].event in {"SPECIATION", "UNKNOWN"}
    if nodes["AN0"].event == "SPECIATION":
        assert nodes["AN0"].taxon == "SAR/HA_supergroup"


def test_parse_tree_rejects_internal_node_without_id() -> None:
    with pytest.raises(ValueError, match="no NHX ID"):
        parse_tree("(AN1:0.1,AN2:0.2):0.3[&&NHX:Ev=0>1];\n")


def test_parse_long_id() -> None:
    leaf = parse_long_id("MOUSE|MGI=MGI=1333783|UniProtKB=Q9WU84")
    assert (leaf.organism, leaf.db, leaf.gene_id, leaf.accession) == ("MOUSE", "MGI", "MGI=1333783", "Q9WU84")
    assert leaf.keys() >= {"UniProtKB:Q9WU84", "MGI:MGI:1333783"}
    assert "TAIR:locus:2034740" in parse_long_id("ARATH|TAIR=locus=2034740|UniProtKB=Q9LD47").keys()
    assert "FB:FBgn0010531" in parse_long_id("DROME|FlyBase=FBgn0010531|UniProtKB=E1JH26").keys()
    assert "WB:WBGene00004933" in parse_long_id("CAEEL|WormBase=WBGene00004933|UniProtKB=P34461").keys()


def test_node_table_maps_an_to_ptn_and_subfamily() -> None:
    table = parse_node_table((FIXTURES / "PAINT_Annotatations_TOTAL.txt").read_text().splitlines())
    assert set(table) == {FAMILY}
    assert table[FAMILY]["AN12"] == ("PTN008300302", "PTHR10004:SF8")
    assert "root" not in table[FAMILY]
    assert len(table[FAMILY]) == 15


def test_family_tree_queries() -> None:
    tree = _tree()
    assert tree.root == "AN0"
    assert tree.lineage("AN13") == ["AN0", "AN4", "AN6", "AN8", "AN10", "AN12", "AN13"]
    assert tree.mrca("AN13", "AN14") == "AN12"
    assert tree.mrca("AN13", "AN11") == "AN10"
    assert tree.mrca("AN2", "AN13") == "AN0"
    assert tree.mrca("AN13", "AN13") == "AN13"
    assert tree.distance("AN13", "AN14") == pytest.approx(0.051)
    assert tree.distance("AN13", "AN11") == pytest.approx(0.286)
    assert tree.leaves_below("AN10") == ["AN11", "AN13", "AN14"]
    assert tree.leaves_below("AN13") == ["AN13"]
    assert tree.is_ancestor("AN4", "AN13") and not tree.is_ancestor("AN1", "AN13")
    assert tree.ptn_of["AN12"] == "PTN008300302"
    assert tree.an_of["PTN008300302"] == "AN12"
    assert tree.subfamily_of["AN13"] == "PTHR10004:SF8"
    assert tree.path("AN4", "AN13") == ["AN4", "AN6", "AN8", "AN10", "AN12", "AN13"]
    with pytest.raises(ValueError, match="not an ancestor"):
        tree.path("AN1", "AN13")


def test_taxon_bounds_of_non_speciation_nodes() -> None:
    tree = _tree()
    # A speciation node is its own bound.
    assert tree.taxon_bounds("AN4") == ("Poaceae", ["Poaceae"])
    # The wheat duplication happened after Triticeae; both copies are wheat leaves.
    assert tree.taxon_bounds("AN12") == ("Triticeae", ["WHEAT"])
    # The transfer node sits below the Viridiplantae root, above two leaves.
    assert tree.taxon_bounds("AN1") == ("Viridiplantae", ["CHLRE", "GEOSL"])


def test_find_leaf_by_accession_and_database_id() -> None:
    tree = _tree()
    assert tree.find_leaf("UniProtKB:A0A3B6RI80") == "AN13"
    assert tree.find_leaf("EnsemblGenome:GSU3278") == "AN2"
    assert tree.find_leaf("UniProtKB:P99999") is None


def test_parse_fasta_and_pairwise_stats() -> None:
    seqs = parse_fasta((FIXTURES / f"{FAMILY}.AN.fasta").read_text())
    assert len(seqs) == 8
    assert {len(s) for s in seqs.values()} == {921}
    close = pairwise_alignment_stats(seqs["AN13"], seqs["AN14"])
    assert (close.aligned, close.identical) == (911, 873)
    assert close.identity == pytest.approx(873 / 911)
    assert close.coverage_of_other == pytest.approx(911 / 912)
    far = pairwise_alignment_stats(seqs["AN13"], seqs["AN2"])
    assert (far.aligned, far.identical) == (806, 121)
    assert far.coverage_of_other == pytest.approx(806 / 816)


def test_pairwise_stats_report_missing_regions_in_native_coordinates() -> None:
    target = "MK" + "-" * 40 + "LLLL"
    other = "MK" + "A" * 40 + "LLLL"
    stats = pairwise_alignment_stats(target, other, min_region=30)
    assert stats.aligned == 6
    # Residues 3-42 of the other sequence have no aligned residue in the target.
    assert stats.other_regions_missing_in_self == [(3, 42)]
    assert stats.self_regions_missing_in_other == []


def test_pairwise_stats_reject_unequal_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        pairwise_alignment_stats("MK-", "MK")


@pytest.mark.parametrize("extra_first", [False, True])
def test_build_database_and_read_back(tmp_path: Path, extra_first: bool) -> None:
    db = tmp_path / "release.sqlite"
    manifest = build_database(_bundle(extra_first), db, release="19.0", source="fixture")
    assert manifest["families"] == "1"
    rel = PantherRelease(db)
    assert rel.manifest()["release"] == "19.0"
    assert rel.locate_node("PTN008300302") == (FAMILY, "AN12")
    assert rel.locate_node("PANTHER:PTN008300302") == (FAMILY, "AN12")
    assert rel.locate_node("PTN000000001") is None
    assert rel.locate_accession("A0A3B6RI80") == [(FAMILY, "AN13")]
    tree = rel.tree(FAMILY)
    assert tree is not None and tree.mrca("AN13", "AN14") == "AN12"
    assert rel.tree("PTHR99999") is None
    aln = rel.alignment(FAMILY)
    assert len(aln) == 8 and len(aln["AN13"]) == 921


def test_build_database_refuses_incomplete_bundle(tmp_path: Path) -> None:
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        data = (FIXTURES / "PAINT_Annotatations_TOTAL.txt").read_bytes()
        info = tarfile.TarInfo("PANTHER19.0_data/PAINT_Annotations/PAINT_Annotatations_TOTAL.txt")
        info.size = len(data)
        tar.addfile(info, io.BytesIO(data))
    buf.seek(0)
    with pytest.raises(RuntimeError, match="without a tree"):
        build_database(buf, tmp_path / "x.sqlite", release="19.0", source="fixture")


def test_release_requires_existing_database(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="fetch-panther-release"):
        PantherRelease(tmp_path / "missing.sqlite")


def test_node_table_rows_of_one_family_need_not_be_contiguous(tmp_path: Path) -> None:
    """PANTHER lists a family's internal nodes and its leaves in different places."""
    lines = (FIXTURES / "PAINT_Annotatations_TOTAL.txt").read_text().splitlines()
    internal = [x for x in lines if x.split("\t")[0] in {f"{FAMILY}:root", f"{FAMILY}:AN0", f"{FAMILY}:AN12"}]
    rest = [x for x in lines if x not in internal]
    other = ["PTHR00001:AN0\tPTHR00001:SF1  \tPTN900000000", "PTHR00001:AN1\tPTHR00001:SF1  \tPTN900000001",
             "PTHR00001:AN2\tPTHR00001:SF1  \tPTN900000002"]
    table = "\n".join(internal + other + rest) + "\n"
    other_tree = "(AN1:0.1,AN2:0.2)[&&NHX:Ev=0>1:S=Bilateria:ID=AN0];\nAN1:A|Gene=x|UniProtKB=P1;\nAN2:B|Gene=y|UniProtKB=P2;\n"
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for name, data in [
            ("PANTHER19.0_data/PAINT_Annotations/PAINT_Annotatations_TOTAL.txt", table.encode()),
            (f"PANTHER19.0_data/Tree_MSF/{FAMILY}.tree", (FIXTURES / f"{FAMILY}.tree").read_bytes()),
            ("PANTHER19.0_data/Tree_MSF/PTHR00001.tree", other_tree.encode()),
        ]:
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
    buf.seek(0)
    db = tmp_path / "release.sqlite"
    build_database(buf, db, release="19.0", source="fixture")
    tree = PantherRelease(db).tree(FAMILY)
    assert tree is not None
    assert tree.ptn_of["AN0"] == "PTN007416421"  # internal node, listed before the other family
    assert tree.ptn_of["AN12"] == "PTN008300302"
    assert tree.ptn_of["AN13"] == "PTN007465329"  # leaf, listed after it
    assert len(tree.ptn_of) == 15


def test_aliases_round_trip(tmp_path: Path) -> None:
    import sqlite3

    db = tmp_path / "release.sqlite"
    build_database(_bundle(), db, release="19.0", source="fixture")
    con = sqlite3.connect(db)
    stored = store_aliases(con, parse_locus_table(["Entry\tGene Names (ordered locus)", "Q38929\tAt5g16440"]))
    con.commit()
    con.close()
    assert stored == 1
    rel = PantherRelease(db)
    assert rel.alias_accessions("AGI_LocusCode:AT5G16440") == ["Q38929"]
    assert rel.alias_accessions("AGI_LocusCode:AT0G00000") == []


def _full_sequences() -> dict[str, str]:
    return parse_fasta((FIXTURES / f"{FAMILY}.fasta").read_text())


def test_alignment_rows_are_cut_from_longer_sequences() -> None:
    """The reason positions cannot be counted along a row: PANTHER drops unaligned stretches."""
    rows = parse_fasta((FIXTURES / f"{FAMILY}.AN.fasta").read_text())
    full = _full_sequences()
    tree = _tree()
    wheat = full[tree.nodes["AN13"].long_id]
    assert len(wheat) == 1232
    assert len(rows["AN13"].replace("-", "")) == 911


def test_embed_row_gives_positions_in_the_full_sequence() -> None:
    rows = parse_fasta((FIXTURES / f"{FAMILY}.AN.fasta").read_text())
    full = _full_sequences()
    tree = _tree()
    rice_full = full[tree.nodes["AN7"].long_id]
    wheat_full = full[tree.nodes["AN13"].long_id]
    rice = embed_row(rows["AN7"], rice_full)
    wheat = embed_row(rows["AN13"], wheat_full)
    assert rice is not None and wheat is not None
    assert len(rice) == len(wheat) == 921
    # Rice P2 and wheat P110 share a column; so do rice K5 and wheat R113.
    column = column_of_position(rice, 2)
    assert column is not None and wheat[column] == (110, True)
    assert rice_full[1] == "P" and wheat_full[109] == "P"
    column = column_of_position(rice, 5)
    assert column is not None and wheat[column] == (113, True)
    assert rice_full[4] == "K" and wheat_full[112] == "R"
    # Rice D421 falls in a wheat gap; rice P7 was left out of the alignment altogether.
    column = column_of_position(rice, 421)
    assert column is not None and wheat[column] == (0, True)
    assert column_of_position(rice, 7) is None
    # Rice A6 sits next to a left-out stretch that also offers an A: its column is not forced.
    column = column_of_position(rice, 6)
    assert column is not None and rice[column] == (6, False)


def test_embed_row_refuses_a_row_from_another_sequence() -> None:
    rows = parse_fasta((FIXTURES / f"{FAMILY}.AN.fasta").read_text())
    full = _full_sequences()
    tree = _tree()
    assert embed_row(rows["AN13"], full[tree.nodes["AN2"].long_id]) is None


def test_store_sequences_round_trip(tmp_path: Path) -> None:
    import sqlite3

    db = tmp_path / "release.sqlite"
    build_database(_bundle(), db, release="19.0", source="fixture")
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for name, data in [
            (f"PANTHER19.0_fasta/{FAMILY}.fasta", (FIXTURES / f"{FAMILY}.fasta").read_bytes()),
            ("PANTHER19.0_fasta/README", b"ignored\n"),
        ]:
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
    buf.seek(0)
    con = sqlite3.connect(db)
    assert store_sequences(con, buf) == 1
    con.commit()
    con.close()
    rel = PantherRelease(db)
    sequences = rel.sequences(FAMILY)
    assert len(sequences) == 8
    assert len(sequences["WHEAT|EnsemblGenome=TraesCS7A02G346100|UniProtKB=A0A3B6RI80"]) == 1232
    assert rel.sequences("PTHR99999") == {}
    # A database built without the sequence archive simply has none.
    bare = tmp_path / "bare.sqlite"
    build_database(_bundle(), bare, release="19.0", source="fixture")
    assert PantherRelease(bare).sequences(FAMILY) == {}
