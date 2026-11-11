"""Tests for the per-gene phylogenetic extract (tree placement and alignment per IBA row).

The tree and alignment are the real PTHR10004 family of PANTHER 19.0 (see
``test_panther_release``). The GOA rows are written for the test: no reviewed gene sits
in a family this small, and the point is to exercise each placement case against a tree
whose shape is known:

    AN0 speciation Viridiplantae
      AN1 horizontal transfer -> AN2 GEOSL, AN3 CHLRE
      AN4 speciation Poaceae
        AN5 SETIT
        AN6 speciation BEP_clade
          AN7 ORYSJ
          AN8 speciation Pooideae
            AN9 BRADI
            AN10 speciation Triticeae
              AN11 HORVV
              AN12 duplication -> AN13 WHEAT (target), AN14 WHEAT
"""

from __future__ import annotations

import io
import sqlite3
import tarfile
from pathlib import Path

import pytest
import yaml

from ai_gene_review.etl.gene_phylo import (
    build_family_nodes,
    build_gene_phylo,
    family_nodes_path,
    phylo_path,
    read_iba_rows,
    render,
    render_family,
    write_family_nodes,
    write_gene_phylo,
)
from ai_gene_review.etl.panther_release import PantherRelease, build_database, store_sequences

FIXTURES = Path(__file__).parent / "input" / "panther_release"
FAMILY = "PTHR10004"
TARGET = "A0A3B6RI80"

HEADER = (
    "GENE PRODUCT DB\tGENE PRODUCT ID\tSYMBOL\tQUALIFIER\tGO TERM\tGO NAME\tGO ASPECT\tECO ID\t"
    "GO EVIDENCE CODE\tREFERENCE\tWITH/FROM\tTAXON ID\tTAXON NAME\tASSIGNED BY\tGENE NAME\tDATE"
)


def _goa_row(qualifier: str, term: str, name: str, aspect: str, code: str, with_from: str) -> str:
    return (
        f"UniProtKB\t{TARGET}\tTEST1\t{qualifier}\t{term}\t{name}\t{aspect}\tECO:0000318\t{code}\t"
        f"GO_REF:0000033\t{with_from}\t4565\tTriticum aestivum\tGO_Central\tTest protein\t20250101"
    )


GOA_ROWS = [
    # IBD at Poaceae; one seed shares the target's branch below it (rice), one does not (foxtail millet).
    _goa_row("enables", "GO:0003824", "catalytic activity", "molecular_function", "IBA",
             "PANTHER:PTN007416424|UniProtKB:A0A0P0WXX3|UniProtKB:K3XV71"),
    # IBD on the wheat duplication itself; the seed is the other wheat copy.
    _goa_row("located_in", "GO:0005737", "cytoplasm", "cellular_component", "IBA",
             "PANTHER:PTN008300302|UniProtKB:A0A3B6TTS2"),
    # Root IBD seeded by the target itself, a bacterial leaf reached across a transfer, and an unknown locus.
    _goa_row("involved_in", "GO:0008152", "metabolic process", "biological_process", "IBA",
             "AGI_LocusCode:AT0G00000|PANTHER:PTN007416421|UniProtKB:A0A3B6RI80|UniProtKB:Q747I8"),
    # A NOT row (PAINT loss carried to the leaf).
    _goa_row("NOT|enables", "GO:0016787", "hydrolase activity", "molecular_function", "IBA",
             "PANTHER:PTN008935992"),
    # A node the release does not know.
    _goa_row("enables", "GO:0005515", "protein binding", "molecular_function", "IBA",
             "PANTHER:PTN999999999|UniProtKB:Q747I8"),
    # Not an IBA row.
    _goa_row("enables", "GO:0003824", "catalytic activity", "molecular_function", "IDA", ""),
]

PAINT = (
    "family\tnode\tgo_id\taspect\tevidence\tnegated\tseeds\ttaxon\tdate\n"
    f"{FAMILY}\tPTN007416424\tGO:0003824\tF\tIBD\tfalse\tUniProtKB:A0A0P0WXX3|UniProtKB:K3XV71\ttaxon:4479\t20200101\n"
    # A loss of the same term on the target's path, below the IBD node.
    f"{FAMILY}\tPTN008935992\tGO:0003824\tF\tIRD\ttrue\tPANTHER:PTN007416424\ttaxon:147389\t20240202\n"
    # A loss of another term, and a loss off the target's path: neither bears on row 1.
    f"{FAMILY}\tPTN008935992\tGO:0005737\tC\tIRD\ttrue\tPANTHER:PTN007416421\ttaxon:147389\t20240202\n"
    f"{FAMILY}\tPTN007416422\tGO:0003824\tF\tIRD\ttrue\tPANTHER:PTN007416421\ttaxon:\t20240202\n"
)

OBO = (
    "[Term]\nid: PANTHER:PTHR10004\nname: FAMILY NOT NAMED\n\n"
    "[Term]\nid: PANTHER:PTHR10004:SF8\nname: PROTEIN XRI1\n\n"
)


@pytest.fixture()
def release(tmp_path: Path) -> PantherRelease:
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for name, path in [
            ("PANTHER19.0_data/PAINT_Annotations/PAINT_Annotatations_TOTAL.txt", FIXTURES / "PAINT_Annotatations_TOTAL.txt"),
            (f"PANTHER19.0_data/Tree_MSF/{FAMILY}.AN.fasta", FIXTURES / f"{FAMILY}.AN.fasta"),
            (f"PANTHER19.0_data/Tree_MSF/{FAMILY}.tree", FIXTURES / f"{FAMILY}.tree"),
        ]:
            data = path.read_bytes()
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
    buf.seek(0)
    db = tmp_path / "release.sqlite"
    build_database(buf, db, release="19.0", source="fixture")
    fasta = io.BytesIO()
    with tarfile.open(fileobj=fasta, mode="w:gz") as tar:
        data = (FIXTURES / f"{FAMILY}.fasta").read_bytes()
        info = tarfile.TarInfo(f"PANTHER19.0_fasta/{FAMILY}.fasta")
        info.size = len(data)
        tar.addfile(info, io.BytesIO(data))
    fasta.seek(0)
    con = sqlite3.connect(db)
    store_sequences(con, fasta)
    con.commit()
    con.close()
    return PantherRelease(db)


@pytest.fixture()
def release_without_sequences(tmp_path: Path) -> PantherRelease:
    """A release database built from the tree and alignment bundle alone."""
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for name, path in [
            ("PANTHER19.0_data/PAINT_Annotations/PAINT_Annotatations_TOTAL.txt", FIXTURES / "PAINT_Annotatations_TOTAL.txt"),
            (f"PANTHER19.0_data/Tree_MSF/{FAMILY}.AN.fasta", FIXTURES / f"{FAMILY}.AN.fasta"),
            (f"PANTHER19.0_data/Tree_MSF/{FAMILY}.tree", FIXTURES / f"{FAMILY}.tree"),
        ]:
            data = path.read_bytes()
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
    buf.seek(0)
    db = tmp_path / "bare.sqlite"
    build_database(buf, db, release="19.0", source="fixture")
    return PantherRelease(db)


@pytest.fixture()
def root(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    gene = repo / "genes" / "WHEAT" / "TEST1"
    gene.mkdir(parents=True)
    (gene / "TEST1-goa.tsv").write_text("\n".join([HEADER, *GOA_ROWS]) + "\n")
    family = repo / "interpro" / "panther" / FAMILY
    family.mkdir(parents=True)
    (family / f"{FAMILY}-paint.tsv").write_text(PAINT)
    (repo / "interpro" / "panther" / "panther.obo").write_text(OBO)
    return repo


def test_read_iba_rows_keeps_only_iba_and_splits_with_from(root: Path) -> None:
    rows = read_iba_rows(root / "genes" / "WHEAT" / "TEST1" / "TEST1-goa.tsv")
    assert [r.term_id for r in rows] == ["GO:0003824", "GO:0005737", "GO:0008152", "GO:0016787", "GO:0005515"]
    assert rows[0].nodes == ["PTN007416424"]
    assert rows[0].seeds == ["UniProtKB:A0A0P0WXX3", "UniProtKB:K3XV71"]
    assert rows[0].accession == TARGET
    assert not rows[0].negated and rows[3].negated
    assert rows[3].seeds == []


def test_build_places_target_and_describes_lineage(root: Path, release: PantherRelease) -> None:
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release)
    assert doc is not None
    assert doc["gene"] == "WHEAT/TEST1"
    assert doc["accession"] == f"UniProtKB:{TARGET}"
    assert doc["panther_release"] == "19.0"
    assert doc["iba_rows"] == 5
    (tree,) = doc["trees"]
    assert tree["family"] == FAMILY
    assert tree["tree_leaves"] == 8
    assert tree["alignment_columns"] == 921
    target = tree["target"]
    assert target["leaf"] == "PTN007465329"
    assert target["subfamily"] == "PTHR10004:SF8"
    assert target["subfamily_name"] == "PROTEIN XRI1"
    assert target["matched_by"] == "accession"
    # 911 of the protein's 1232 residues are in the family alignment.
    assert (target["length"], target["aligned_residues"]) == (1232, 911)
    assert "same_as_uniprot_file" not in target  # the test gene has no UniProt file
    lineage = tree["lineage"]
    assert [x["node"] for x in lineage] == [
        "PTN007416421", "PTN007416424", "PTN007416426", "PTN008300301", "PTN008935992", "PTN008300302", "PTN007465329",
    ]
    assert lineage[0] == {"node": "PTN007416421", "event": "SPECIATION", "taxon": "Viridiplantae", "leaves": 8}
    assert lineage[5] == {
        "node": "PTN008300302", "event": "DUPLICATION", "after": "Triticeae", "before": ["WHEAT"],
        "branch": 0.105, "leaves": 2,
    }
    assert lineage[6]["event"] == "LEAF" and lineage[6]["branch"] == 0.03


def test_row_at_speciation_node_with_bracketing_seed(root: Path, release: PantherRelease) -> None:
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release)
    assert doc is not None
    tree = doc["trees"][0]
    row = tree["rows"][0]
    assert row["term"] == {"id": "GO:0003824", "label": "catalytic activity"}
    assert row["ibd_node"] == "PTN007416424"
    assert row["steps"] == 5
    assert row["duplications_on_path"] == 1
    assert row["transfers_on_path"] == 0
    assert row["path_length"] == pytest.approx(0.725)
    assert row["target_branch"] == "PTN007416426"
    assert row["seeds"] == ["UniProtKB:A0A0P0WXX3", "UniProtKB:K3XV71"]
    assert (row["seeds_resolved"], row["seeds_unresolved"]) == (2, 0)
    assert row["seeds_on_target_branch"] == 1
    # Rice and millet sit in different branches below Poaceae, so the node is their common ancestor.
    assert (row["seed_branches"], row["node_branches"]) == (2, 2)
    assert (row["seed_mrca"], row["seed_mrca_steps_below_node"]) == ("PTN007416424", 0)
    assert row["target_in_seed_clade"] is True
    assert (
        "They sit in 2 of the 2 branches below the node, so the node is their common ancestor; "
        "1 of them shares TEST1's own branch below it (PTN007416426)." in row["summary"]
    )
    # Both seeds join wheat at a speciation, but wheat duplicated afterwards: neither is one-to-one.
    assert (row["orthologs"], row["one_to_one_orthologs"], row["paralogs"], row["xenologs"]) == (2, 0, 0, 0)
    assert "By the tree the seeds are 2 orthologs across later duplications of TEST1." in row["summary"]
    assert row["self_seed"] is False
    assert row["nearest_seed"] == "UniProtKB:A0A0P0WXX3"
    # The IRD at Triticeae is below the IBD node and above the target; the other two losses are not.
    assert row["paint_losses_on_path"] == [{"node": "PTN008935992", "evidence": "IRD", "date": "20240202"}]
    assert "GO:0003824" in row["summary"] and "PTN007416424" in row["summary"]
    assert "speciation node at Poaceae" in row["summary"]
    assert "1 duplication" in row["summary"]
    assert "IRD at PTN008935992" in row["summary"]

    seeds = {s["id"]: s for s in tree["seeds"]}
    rice = seeds["UniProtKB:A0A0P0WXX3"]
    assert rice["leaf"] == "PTN001597169"
    assert rice["organism"] == "ORYSJ"
    assert rice["relation"] == "ORTHOLOG"
    assert (rice["mrca"], rice["mrca_event"], rice["mrca_taxon"]) == ("PTN007416426", "SPECIATION", "BEP_clade")
    assert rice["tree_distance"] == pytest.approx(0.807)
    assert (rice["aligned"], rice["identity"]) == (798, 0.571)
    # Coverage is of the whole proteins (wheat 1232 residues, rice 957), not of the alignment rows.
    assert (rice["length"], rice["covers_target"], rice["covers_seed"]) == (957, 0.648, 0.834)
    # The wheat protein has an N-terminal stretch with no aligned rice residue, in wheat numbering.
    assert rice["target_regions_without_seed"] == ["1-106"]
    assert "seed_regions_without_target" not in rice
    assert "57% identity over 798 aligned columns, which span 65% of TEST1 and 83% of the seed" in row["summary"]
    millet = seeds["UniProtKB:K3XV71"]
    assert millet["mrca"] == "PTN007416424"
    assert millet["tree_distance"] == pytest.approx(1.017)


def test_row_on_duplication_node_has_paralog_seed(root: Path, release: PantherRelease) -> None:
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release)
    assert doc is not None
    tree = doc["trees"][0]
    row = tree["rows"][1]
    assert row["ibd_node"] == "PTN008300302"
    assert (row["steps"], row["duplications_on_path"]) == (1, 0)
    assert row["target_branch"] == "PTN007465329"
    assert (row["orthologs"], row["paralogs"]) == (0, 1)
    assert row["seeds_on_target_branch"] == 0
    # A single seed is its own common ancestor, one step below the node, and the target is not in it.
    assert (row["seed_mrca"], row["seed_mrca_steps_below_node"]) == ("PTN004199303", 1)
    assert row["target_in_seed_clade"] is False
    assert "duplication node" in row["summary"]
    assert "The single seed leaf PTN004199303 is 1 step below the PAINT node." in row["summary"]
    assert "By the tree the seed is a paralog of TEST1." in row["summary"]
    seed = {s["id"]: s for s in tree["seeds"]}["UniProtKB:A0A3B6TTS2"]
    assert seed["relation"] == "PARALOG"
    assert seed["mrca_event"] == "DUPLICATION"
    assert seed["identity"] == pytest.approx(873 / 911, abs=0.0005)
    assert seed["aligned"] == 911
    node = {n["node"]: n for n in tree["nodes"]}["PTN008300302"]
    assert node["event"] == "DUPLICATION"
    assert (node["after"], node["before"]) == ("Triticeae", ["WHEAT"])
    assert node["leaves"] == 2 and node["species"] == 1


def test_root_row_with_self_seed_transfer_and_unresolved_token(root: Path, release: PantherRelease) -> None:
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release)
    assert doc is not None
    tree = doc["trees"][0]
    row = tree["rows"][2]
    assert row["ibd_node"] == "PTN007416421"
    assert row["self_seed"] is True
    assert (row["seeds_resolved"], row["seeds_unresolved"]) == (2, 1)
    assert row["unresolved_seeds"] == ["AGI_LocusCode:AT0G00000"]
    # The bacterial leaf joins the target at the speciation root; the transfer node on the way
    # is counted, not read as making the pair xenologs.
    assert (row["orthologs"], row["paralogs"], row["xenologs"]) == (1, 0, 0)
    assert "its own experimental annotation" in row["summary"]
    assert "By the tree the other seed is an ortholog across later duplications of TEST1." in row["summary"]
    assert "none of the other seeds shares TEST1's own branch below it (PTN007416424)." in row["summary"]
    seeds = {s["id"]: s for s in tree["seeds"]}
    assert seeds[f"UniProtKB:{TARGET}"]["relation"] == "SELF"
    assert seeds["UniProtKB:Q747I8"]["relation"] == "ORTHOLOG"
    assert seeds["UniProtKB:Q747I8"]["transfers_between"] == 1
    node = {n["node"]: n for n in tree["nodes"]}["PTN007416421"]
    assert node["is_root"] is True
    assert node["leaves"] == 8 and node["species"] == 7
    branches = {b["node"]: b for b in node["branches"]}
    assert branches["PTN007416424"]["has_target"] is True
    assert branches["PTN007416422"]["has_target"] is False
    assert branches["PTN007416422"]["event"] == "HORIZONTAL_TRANSFER"


def test_negated_row_and_unknown_node(root: Path, release: PantherRelease) -> None:
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release)
    assert doc is not None
    tree = doc["trees"][0]
    assert [r["term"]["id"] for r in tree["rows"]] == ["GO:0003824", "GO:0005737", "GO:0008152", "GO:0016787"]
    not_row = tree["rows"][3]
    assert not_row["negated"] is True
    assert not_row["summary"].startswith("NOT GO:0016787")
    assert doc["unplaced_rows"] == [
        {
            "term": {"id": "GO:0005515", "label": "protein binding"},
            "with_from": "PANTHER:PTN999999999|UniProtKB:Q747I8",
            "reason": "PTN999999999 is not a node of any PANTHER 19.0 tree",
        }
    ]


def test_render_round_trips_and_keeps_summaries_on_one_line(root: Path, release: PantherRelease) -> None:
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release)
    assert doc is not None
    text = render(doc)
    assert text.startswith("# ")
    assert yaml.safe_load(text) == doc
    for row in doc["trees"][0]["rows"]:
        assert row["summary"] in text  # verbatim, so a review can quote it


def test_write_gene_phylo_is_idempotent_and_skips_genes_without_iba(root: Path, release: PantherRelease) -> None:
    path = write_gene_phylo(root, "WHEAT", "TEST1", release)
    assert path == phylo_path(root, "WHEAT", "TEST1")
    assert path is not None and path.name == "TEST1-phylo.yaml"
    first = path.read_text()
    assert write_gene_phylo(root, "WHEAT", "TEST1", release) == path
    assert path.read_text() == first

    other = root / "genes" / "WHEAT" / "TEST2"
    other.mkdir()
    (other / "TEST2-goa.tsv").write_text(HEADER + "\n" + GOA_ROWS[-1] + "\n")
    assert write_gene_phylo(root, "WHEAT", "TEST2", release) is None
    assert not phylo_path(root, "WHEAT", "TEST2").exists()


def test_target_found_through_secondary_accession(root: Path, release: PantherRelease) -> None:
    gene = root / "genes" / "WHEAT" / "TEST3"
    gene.mkdir()
    rows = [r.replace(TARGET, "P00001") if "\tIBA\t" in r else r for r in GOA_ROWS[:1]]
    (gene / "TEST3-goa.tsv").write_text("\n".join([HEADER, *rows]) + "\n")
    (gene / "TEST3-uniprot.txt").write_text(f"ID   TEST3_WHEAT  Reviewed;  911 AA.\nAC   P00001; {TARGET};\n")
    doc = build_gene_phylo(root, "WHEAT", "TEST3", release)
    assert doc is not None
    target = doc["trees"][0]["target"]
    assert target["leaf"] == "PTN007465329"
    assert target["matched_by"] == f"secondary accession {TARGET}"


def test_target_missing_from_tree_is_reported_not_guessed(root: Path, release: PantherRelease) -> None:
    gene = root / "genes" / "WHEAT" / "TEST4"
    gene.mkdir()
    rows = [r.replace(TARGET, "P00002") for r in GOA_ROWS[:1]]
    (gene / "TEST4-goa.tsv").write_text("\n".join([HEADER, *rows]) + "\n")
    doc = build_gene_phylo(root, "WHEAT", "TEST4", release)
    assert doc is not None
    tree = doc["trees"][0]
    assert tree["target"] is None
    assert "lineage" not in tree
    row = tree["rows"][0]
    assert "steps" not in row
    assert "P00002 is not a leaf of PTHR10004" in row["summary"]
    # The node itself is still described.
    assert tree["nodes"][0]["node"] == "PTN007416424"


def test_leaves_joined_at_a_transfer_node_are_xenologs(root: Path, release: PantherRelease) -> None:
    gene = root / "genes" / "GEOSL" / "TEST5"
    gene.mkdir(parents=True)
    row = _goa_row("enables", "GO:0003824", "catalytic activity", "molecular_function", "IBA",
                   "PANTHER:PTN007416422|UniProtKB:A0A2K3DLW7").replace(TARGET, "Q747I8")
    (gene / "TEST5-goa.tsv").write_text(HEADER + "\n" + row + "\n")
    doc = build_gene_phylo(root, "GEOSL", "TEST5", release)
    assert doc is not None
    tree = doc["trees"][0]
    assert tree["seeds"][0]["relation"] == "XENOLOG"
    assert tree["rows"][0]["xenologs"] == 1
    assert "By the tree the seed is a xenolog of TEST5." in tree["rows"][0]["summary"]


def test_render_puts_each_record_on_one_line(root: Path, release: PantherRelease) -> None:
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release)
    assert doc is not None
    lines = render(doc).splitlines()
    assert "  - {node: PTN008300302, event: DUPLICATION, after: Triticeae, before: [WHEAT], branch: 0.105, leaves: 2}" in lines
    assert any(line.startswith("  target: {leaf: PTN007465329,") for line in lines)
    assert any(line.startswith("  - {id: 'UniProtKB:A0A3B6TTS2', leaf: PTN004199303,") for line in lines)


def test_family_nodes_describe_each_paint_node_and_its_seed_spread(root: Path, release: PantherRelease) -> None:
    doc = build_family_nodes(root, FAMILY, release)
    assert doc is not None
    assert doc["family"] == FAMILY and doc["tree_leaves"] == 8 and doc["tree_species"] == 7
    nodes = {n["node"]: n for n in doc["nodes"]}
    assert set(nodes) == {"PTN007416424", "PTN008935992", "PTN007416422"}
    poaceae = nodes["PTN007416424"]
    assert (poaceae["event"], poaceae["taxon"], poaceae["leaves"]) == ("SPECIATION", "Poaceae", 6)
    (gain,) = poaceae["assertions"]
    assert gain["term"] == "GO:0003824" and gain["evidence"] == "IBD" and gain["negated"] is False
    assert (gain["seeds"], gain["seeds_resolved"], gain["seed_branches"], gain["node_branches"]) == (2, 2, 2, 2)
    assert gain["seed_mrca_steps_below_node"] == 0
    assert gain["summary"].startswith("PTN007416424 GO:0003824 IBD: PAINT node PTN007416424 is a speciation node at Poaceae")
    assert "so the node is their common ancestor" in gain["summary"]
    losses = nodes["PTN008935992"]["assertions"]
    assert [(a["term"], a["evidence"], a["negated"]) for a in losses] == [
        ("GO:0003824", "IRD", True), ("GO:0005737", "IRD", True),
    ]
    assert losses[0]["blocks"] == ["PTN007416424"]
    assert losses[0]["summary"].startswith("PTN008935992 NOT GO:0003824 IRD:")
    assert "stops the term asserted at PTN007416424" in losses[0]["summary"]
    text = render_family(doc)
    assert yaml.safe_load(text) == doc
    assert gain["summary"] in text


def test_family_nodes_report_one_sided_seeds(root: Path, release: PantherRelease) -> None:
    """An IBD whose seeds all sit in one branch is placed above their common ancestor."""
    paint = root / "interpro" / "panther" / FAMILY / f"{FAMILY}-paint.tsv"
    paint.write_text(
        "family\tnode\tgo_id\taspect\tevidence\tnegated\tseeds\ttaxon\tdate\n"
        f"{FAMILY}\tPTN007416421\tGO:0003824\tF\tIBD\tfalse\tUniProtKB:A0A3B6RI80|UniProtKB:A0A8I6Z3U3\ttaxon:\t20200101\n"
        f"{FAMILY}\tPTN900000000\tGO:0003824\tF\tIBD\tfalse\tUniProtKB:P1\ttaxon:\t20200101\n"
    )
    doc = build_family_nodes(root, FAMILY, release)
    assert doc is not None
    (node,) = doc["nodes"]
    (gain,) = node["assertions"]
    # Wheat and barley join at Triticeae, four steps below the Viridiplantae root.
    assert (gain["seed_branches"], gain["seed_mrca"], gain["seed_mrca_steps_below_node"]) == (1, "PTN008935992", 4)
    assert "their common ancestor is PTN008935992, a speciation node at Triticeae, covering 3 leaves, 4 steps below the PAINT node" in gain["summary"]
    assert doc["other_tree_nodes"] == ["PTN900000000"]


def test_write_family_nodes(root: Path, release: PantherRelease) -> None:
    path = write_family_nodes(root, FAMILY, release)
    assert path == family_nodes_path(root, FAMILY)
    assert path is not None and path.name == f"{FAMILY}-tree-nodes.yaml"
    assert write_family_nodes(root, "PTHR99999", release) is None


FAMILY_REVIEW = """
family_id: PANTHER:PTHR10004
residue_sites:
- site_id: demo_site
  label: Demonstration site
  anchor:
    id: UniProtKB:A0A0P0WXX3
    label: rice protein
  residues:
  - {position: 2, expected: [P], role: kept}
  - {position: 5, expected: [K], role: changed}
  - {position: 421, expected: [D], role: missing}
  - {position: 269, expected: [E]}
  required_for:
  - term: {id: "GO:0003824", label: catalytic activity}
    strength: REQUIRED
- site_id: unreadable
  label: Positions that cannot be carried over
  anchor:
    id: UniProtKB:A0A0P0WXX3
  residues:
  - {position: 2, expected: [W]}
  - {position: 7, expected: [P]}
  - {position: 6, expected: [A]}
  - {position: 5000, expected: [K]}
- site_id: absent_anchor
  label: Anchor that is not in the tree
  anchor:
    id: UniProtKB:P99999
  residues:
  - {position: 2, expected: [P]}
"""


def test_family_residue_sites_are_read_off_the_family_alignment(root: Path, release: PantherRelease) -> None:
    """Positions are in each protein's own numbering, not counted along the alignment row."""
    (root / "interpro" / "panther" / FAMILY / f"{FAMILY}-review.yaml").write_text(FAMILY_REVIEW)
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release)
    assert doc is not None
    sites = {s["site"]: s for s in doc["trees"][0]["residue_sites"]}
    demo = sites["PANTHER:PTHR10004#demo_site"]
    assert demo["anchor"] == "UniProtKB:A0A0P0WXX3"
    assert demo["required_for"] == ["GO:0003824"]
    assert demo["positions"] == [
        {"anchor_position": 2, "anchor_residue": "P", "expected": ["P"], "role": "kept",
         "target_residue": "P", "target_position": 110, "status": "RETAINED"},
        {"anchor_position": 5, "anchor_residue": "K", "expected": ["K"], "role": "changed",
         "target_residue": "R", "target_position": 113, "status": "SUBSTITUTED"},
        {"anchor_position": 421, "anchor_residue": "D", "expected": ["D"], "role": "missing",
         "target_residue": "-", "status": "ABSENT"},
        # The residue is certain (it is in the column); its number in the wheat protein is not.
        {"anchor_position": 269, "anchor_residue": "E", "expected": ["E"],
         "target_residue": "E", "target_position": 377, "target_position_uncertain": True, "status": "RETAINED"},
    ]
    assert demo["summary"] == (
        "PANTHER:PTHR10004#demo_site (Demonstration site): in the PANTHER 19.0 family alignment TEST1 has "
        "P110 at anchor UniProtKB:A0A0P0WXX3 P2 (retained), R113 at K5 (substituted), a gap at D421 (absent) "
        "and E377 at E269 (retained)."
    )
    unreadable = sites["PANTHER:PTHR10004#unreadable"]
    assert [p["status"] for p in unreadable["positions"]] == [
        "ANCHOR_MISMATCH",  # rice has P, not W, at position 2
        "NOT_ALIGNED",  # rice P7 is in a stretch PANTHER left out of the alignment
        "AMBIGUOUS",  # rice A6 could sit in either of two columns
        "ANCHOR_MISMATCH",  # the rice protein has no residue 5000
    ]
    assert all("target_residue" not in p for p in unreadable["positions"])
    assert "does not have W at position 2 in its PANTHER 19.0 sequence (it has P)" in unreadable["summary"]
    assert "anchor residue P7 is outside the aligned columns" in unreadable["summary"]
    assert "anchor residue A6 cannot be tied to one alignment column" in unreadable["summary"]
    assert "(the sequence is shorter)" in unreadable["summary"]
    assert sites["PANTHER:PTHR10004#absent_anchor"]["status"] == "ANCHOR_NOT_IN_ALIGNMENT"
    assert yaml.safe_load(render(doc)) == doc


def test_residue_sites_need_full_sequences(root: Path, release_without_sequences: PantherRelease) -> None:
    """Without the full sequences a row's residues have no numbers, so no site is read."""
    (root / "interpro" / "panther" / FAMILY / f"{FAMILY}-review.yaml").write_text(FAMILY_REVIEW)
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release_without_sequences)
    assert doc is not None
    tree = doc["trees"][0]
    assert {s["status"] for s in tree["residue_sites"]} == {"ANCHOR_NOT_IN_ALIGNMENT"}
    assert "length" not in tree["target"]
    seed = {s["id"]: s for s in tree["seeds"]}["UniProtKB:A0A0P0WXX3"]
    assert "identity" in seed and "covers_target" not in seed
    assert "seed_regions_without_target" not in seed and "target_regions_without_seed" not in seed
    assert "aligned columns." in tree["rows"][0]["summary"]


def test_target_sequence_is_compared_with_the_uniprot_file(root: Path, release: PantherRelease) -> None:
    sequence = release.sequences(FAMILY)["WHEAT|EnsemblGenome=TraesCS7A02G346100|UniProtKB=A0A3B6RI80"]
    block = "\n".join("     " + sequence[i : i + 60] for i in range(0, len(sequence), 60))
    uniprot = root / "genes" / "WHEAT" / "TEST1" / "TEST1-uniprot.txt"
    uniprot.write_text(f"ID   TEST1_WHEAT\nAC   {TARGET};\nSQ   SEQUENCE   1232 AA;\n{block}\n//\n")
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release)
    assert doc is not None and doc["trees"][0]["target"]["same_as_uniprot_file"] is True
    uniprot.write_text(f"ID   TEST1_WHEAT\nAC   {TARGET};\nSQ   SEQUENCE   3 AA;\n     MKL\n//\n")
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release)
    assert doc is not None and doc["trees"][0]["target"]["same_as_uniprot_file"] is False


def test_no_residue_sites_without_a_family_review(root: Path, release: PantherRelease) -> None:
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release)
    assert doc is not None
    assert "residue_sites" not in doc["trees"][0]


def test_one_to_one_ortholog_is_told_apart_from_an_ortholog_across_duplications(root: Path, release: PantherRelease) -> None:
    """Barley and Brachypodium never duplicated after they split: a one-to-one pair."""
    gene = root / "genes" / "HORVV" / "TEST6"
    gene.mkdir(parents=True)
    row = _goa_row("enables", "GO:0003824", "catalytic activity", "molecular_function", "IBA",
                   "PANTHER:PTN008300301|UniProtKB:A0A0Q3IKV9|UniProtKB:A0A3B6RI80").replace(f"\t{TARGET}\t", "\tA0A8I6Z3U3\t")
    (gene / "TEST6-goa.tsv").write_text(HEADER + "\n" + row + "\n")
    doc = build_gene_phylo(root, "HORVV", "TEST6", release)
    assert doc is not None
    facts = doc["trees"][0]["rows"][0]
    # Brachypodium joins barley at Pooideae with no duplication on either side; wheat joins it
    # at Triticeae, but the wheat lineage duplicated afterwards.
    assert (facts["orthologs"], facts["one_to_one_orthologs"]) == (2, 1)
    assert "1 one-to-one ortholog and 1 ortholog across later duplications of TEST6" in facts["summary"]


def test_loss_lifted_by_a_reassertion_below_it(root: Path, release: PantherRelease) -> None:
    """PAINT can remove a term on a branch and assert it again further down the same path."""
    paint = root / "interpro" / "panther" / FAMILY / f"{FAMILY}-paint.tsv"
    paint.write_text(
        PAINT + f"{FAMILY}\tPTN008300302\tGO:0003824\tF\tIBD\tfalse\tUniProtKB:A0A3B6TTS2\ttaxon:\t20250303\n"
    )
    doc = build_gene_phylo(root, "WHEAT", "TEST1", release)
    assert doc is not None
    row = doc["trees"][0]["rows"][0]
    assert row["paint_losses_on_path"] == [
        {"node": "PTN008935992", "evidence": "IRD", "date": "20240202", "reasserted_below": "PTN008300302"}
    ]
    assert "and PAINT asserts it again below the loss at PTN008300302." in row["summary"]
