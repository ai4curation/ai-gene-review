"""Tests for PANTHER PAINT (PTN node-level) annotation ingest.

These tests exercise the pure parsing/joining logic with small in-memory
fixtures. The network download is covered by an integration test.
"""

from pathlib import Path

from ai_gene_review.etl.panther_paint import (
    parse_ptn_nodes,
    parse_ibd_gaf,
    family_member_ids,
    family_member_subfamilies,
    iter_losses,
    leaf_nodes_for_members,
    write_family_paint,
    load_all_family_members,
    family_nodes_from_leaf,
    fetch_all_family_paint,
)


# A trimmed IBD.gaf: two annotations on one node, plus an IRD (loss) on a
# different node, plus a header line to be ignored.
IBD_FIXTURE = "\n".join(
    [
        "!gaf-version: 2.1",
        "!PANTHER version: v.19.0.",
        # node\tobjid\tqual\tGO\tref\tevidence\twithfrom\taspect ...
        "PANTHER\tPTN000019791\tPTN000019791\t\tGO:0016538\tGO_REF:0000033\tIBD\t"
        "UniProtKB:P20248|UniProtKB:P14635\tF\t\t\tprotein\ttaxon:\t20250902\tGO_Central\t\t",
        "PANTHER\tPTN000019791\tPTN000019791\t\tGO:0000307\tGO_REF:0000033\tIBD\t"
        "UniProtKB:P24864\tC\t\t\tprotein\ttaxon:\t20260528\tGO_Central\t\t",
        "PANTHER\tPTN002681965\tPTN002681965\tNOT\tGO:0008823\tGO_REF:0000033\tIRD\t"
        "PANTHER:PTN001800605\tF\t\t\tprotein\ttaxon:117571\t20250903\tGO_Central\t\t",
    ]
)


# A trimmed leaf gaf (UniProt-centric IBA). col2 = UniProt, col8 (idx 7) = with/from
# containing the ancestral PTN node + experimental seeds.
LEAF_FIXTURE = "\n".join(
    [
        "!gaf-version: 2.1",
        "UniProtKB\tP14635\tCCNB1\tinvolved_in\tGO:0016538\tGO_REF:0000033\tIBA\t"
        "PANTHER:PTN000019791|UniProtKB:P20248\tF\t\t\tprotein\ttaxon:9606\t20250101\tGO_Central\t\t",
        "UniProtKB\tP14635\tCCNB1\tpart_of\tGO:0000307\tGO_REF:0000033\tIBA\t"
        "PANTHER:PTN000019791\tC\t\t\tprotein\ttaxon:9606\t20250101\tGO_Central\t\t",
        # an unrelated leaf in a different family/node
        "UniProtKB\tQ99999\tOTHER\tinvolved_in\tGO:0000001\tGO_REF:0000033\tIBA\t"
        "PANTHER:PTN999999999\tP\t\t\tprotein\ttaxon:9606\t20250101\tGO_Central\t\t",
    ]
)


def test_parse_ptn_nodes_handles_prefixed_and_bare():
    field = "PANTHER:PTN000019791|UniProtKB:P20248|PTN000000001"
    assert parse_ptn_nodes(field) == ["PTN000019791", "PTN000000001"]


def test_parse_ptn_nodes_empty():
    assert parse_ptn_nodes("") == []
    assert parse_ptn_nodes("UniProtKB:P20248") == []


def test_parse_ibd_gaf_indexes_by_node():
    index = parse_ibd_gaf(IBD_FIXTURE.splitlines())
    assert set(index) == {"PTN000019791", "PTN002681965"}
    recs = index["PTN000019791"]
    assert len(recs) == 2
    by_go = {r.go_id: r for r in recs}
    assert by_go["GO:0016538"].evidence == "IBD"
    assert by_go["GO:0016538"].aspect == "F"
    assert by_go["GO:0016538"].seeds == ["UniProtKB:P20248", "UniProtKB:P14635"]
    assert by_go["GO:0016538"].negated is False


def test_parse_ibd_gaf_marks_loss_annotations():
    index = parse_ibd_gaf(IBD_FIXTURE.splitlines())
    loss = index["PTN002681965"][0]
    assert loss.evidence == "IRD"
    assert loss.negated is True
    assert loss.go_id == "GO:0008823"


def test_family_member_ids(tmp_path: Path):
    csv_path = tmp_path / "PTHR1-entries.csv"
    csv_path.write_text(
        "id,name,subfamily\n"
        "P14635,cyclin B1,PTHR1:SF1\n"
        "P24864,cyclin E1,PTHR1:SF2\n"
        ",missing id row,PTHR1:SF3\n"
    )
    assert family_member_ids(csv_path) == {"P14635", "P24864"}


def test_family_member_subfamilies(tmp_path: Path):
    csv_path = tmp_path / "PTHR1-entries.csv"
    csv_path.write_text(
        "id,name,subfamily\n"
        "P14635,cyclin B1,PTHR1:SF1\n"
        "P24864,cyclin E1,\n"  # no subfamily
        ",missing id,PTHR1:SF3\n"
    )
    assert family_member_subfamilies(csv_path) == {"P14635": "PTHR1:SF1", "P24864": ""}


def test_iter_losses_returns_only_losses_with_ancestor():
    losses = list(iter_losses(parse_ibd_gaf(IBD_FIXTURE.splitlines())))
    assert len(losses) == 1
    rec, ancestors = losses[0]
    assert rec.node == "PTN002681965"
    assert rec.evidence == "IRD"
    assert rec.negated is True
    assert ancestors == ["PTN001800605"]


def test_leaf_nodes_for_members_streams_and_filters():
    members = {"P14635"}
    nodes = leaf_nodes_for_members(LEAF_FIXTURE.splitlines(), members)
    assert nodes == {"PTN000019791"}


def test_leaf_nodes_for_members_ignores_unrelated_leaves():
    members = {"P14635", "P24864"}  # P24864 not in leaf fixture
    nodes = leaf_nodes_for_members(LEAF_FIXTURE.splitlines(), members)
    assert "PTN999999999" not in nodes


def test_write_family_paint_emits_gaf_and_tsv(tmp_path: Path):
    index = parse_ibd_gaf(IBD_FIXTURE.splitlines())
    nodes = {"PTN000019791"}
    out_dir = tmp_path / "PTHR000"
    out_dir.mkdir()
    gaf_path, tsv_path = write_family_paint("PTHR000", nodes, index, out_dir)

    assert gaf_path == out_dir / "PTHR000-paint.gaf"
    assert tsv_path == out_dir / "PTHR000-paint.tsv"

    gaf_text = gaf_path.read_text()
    # header preserved, both node rows present, unrelated node excluded
    assert gaf_text.startswith("!")
    data_lines = [ln for ln in gaf_text.splitlines() if not ln.startswith("!")]
    assert len(data_lines) == 2
    assert all("PTN000019791" in ln for ln in data_lines)
    assert "PTN002681965" not in gaf_text

    tsv_lines = tsv_path.read_text().strip().splitlines()
    assert tsv_lines[0].split("\t")[:5] == [
        "family",
        "node",
        "go_id",
        "aspect",
        "evidence",
    ]
    # two data rows for the single node
    assert len(tsv_lines) == 3
    assert all(line.startswith("PTHR000\tPTN000019791") for line in tsv_lines[1:])


def test_write_family_paint_empty_nodes(tmp_path: Path):
    index = parse_ibd_gaf(IBD_FIXTURE.splitlines())
    out_dir = tmp_path / "PTHRX"
    out_dir.mkdir()
    gaf_path, tsv_path = write_family_paint("PTHRX", set(), index, out_dir)
    # still writes (empty) files with just headers so downstream code is uniform
    assert gaf_path.exists() and tsv_path.exists()
    assert tsv_path.read_text().strip().splitlines() == [
        "family\tnode\tgo_id\taspect\tevidence\tnegated\tseeds\ttaxon\tdate"
    ]


def test_fetch_family_paint_end_to_end_with_seeded_cache(tmp_path: Path):
    """Exercise the full orchestration with a pre-seeded cache (no network).

    ``fetch_family_paint`` reuses cached source GAFs when present, so writing
    fixture GAFs into the cache dir lets us test member->node->slice resolution
    deterministically and offline.
    """
    import gzip

    from ai_gene_review.etl.panther_paint import (
        fetch_family_paint,
        IBD_GAF_URL,
        LEAF_GAF_URL,
    )

    cache_dir = tmp_path / ".cache"
    cache_dir.mkdir()
    # Cache files are keyed by URL basename.
    (cache_dir / IBD_GAF_URL.rsplit("/", 1)[1]).write_text(IBD_FIXTURE)
    with gzip.open(cache_dir / LEAF_GAF_URL.rsplit("/", 1)[1], "wt") as fh:
        fh.write(LEAF_FIXTURE)

    entries_csv = tmp_path / "PTHRX-entries.csv"
    entries_csv.write_text("id,name\nP14635,cyclin B1\n")

    out_dir = tmp_path / "PTHRX"
    out_dir.mkdir()
    gaf_path, tsv_path, nodes = fetch_family_paint(
        "PTHRX",
        entries_csv=entries_csv,
        out_dir=out_dir,
        cache_dir=cache_dir,
    )

    # P14635's leaf rows cite PTN000019791, which has 2 IBD annotations.
    assert nodes == {"PTN000019791"}
    tsv_rows = tsv_path.read_text().strip().splitlines()
    assert len(tsv_rows) == 3  # header + 2 annotations
    assert all(r.startswith("PTHRX\tPTN000019791") for r in tsv_rows[1:])


def test_fetch_family_paint_extra_uniprot_expands_nodes(tmp_path: Path):
    """``extra_uniprot`` adds members not present in entries.csv."""
    import gzip

    from ai_gene_review.etl.panther_paint import (
        fetch_family_paint,
        IBD_GAF_URL,
        LEAF_GAF_URL,
    )

    cache_dir = tmp_path / ".cache"
    cache_dir.mkdir()
    (cache_dir / IBD_GAF_URL.rsplit("/", 1)[1]).write_text(IBD_FIXTURE)
    with gzip.open(cache_dir / LEAF_GAF_URL.rsplit("/", 1)[1], "wt") as fh:
        fh.write(LEAF_FIXTURE)

    # Empty member list; supply the member via extra_uniprot instead.
    entries_csv = tmp_path / "PTHRX-entries.csv"
    entries_csv.write_text("id,name\n")

    out_dir = tmp_path / "PTHRX"
    out_dir.mkdir()
    _, _, nodes = fetch_family_paint(
        "PTHRX",
        entries_csv=entries_csv,
        out_dir=out_dir,
        cache_dir=cache_dir,
        extra_uniprot=["P14635"],
    )
    assert nodes == {"PTN000019791"}


def _seed_cache(cache_dir: Path) -> None:
    """Write the IBD + (gzipped) leaf fixtures into a cache dir."""
    import gzip

    from ai_gene_review.etl.panther_paint import IBD_GAF_URL, LEAF_GAF_URL

    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / IBD_GAF_URL.rsplit("/", 1)[1]).write_text(IBD_FIXTURE)
    with gzip.open(cache_dir / LEAF_GAF_URL.rsplit("/", 1)[1], "wt") as fh:
        fh.write(LEAF_FIXTURE)


def test_load_all_family_members_inverts_membership(tmp_path: Path):
    panther = tmp_path / "panther"
    (panther / "PTHR1").mkdir(parents=True)
    (panther / "PTHR2").mkdir(parents=True)
    (panther / "PTHR1" / "PTHR1-entries.csv").write_text("id,name\nP14635,a\nP1,b\n")
    (panther / "PTHR2" / "PTHR2-entries.csv").write_text("id,name\nP14635,a\n")

    member_to_families, family_dirs = load_all_family_members(panther)
    assert member_to_families["P14635"] == {"PTHR1", "PTHR2"}
    assert member_to_families["P1"] == {"PTHR1"}
    assert set(family_dirs) == {"PTHR1", "PTHR2"}


def test_family_nodes_from_leaf_multi_family():
    member_to_families = {"P14635": {"PTHR1", "PTHR2"}}
    nodes = family_nodes_from_leaf(LEAF_FIXTURE.splitlines(), member_to_families)
    assert nodes == {"PTHR1": {"PTN000019791"}, "PTHR2": {"PTN000019791"}}


def test_fetch_all_family_paint_bulk(tmp_path: Path):
    panther = tmp_path / "panther"
    (panther / "PTHR1").mkdir(parents=True)
    (panther / "EMPTY").mkdir(parents=True)
    (panther / "PTHR1" / "PTHR1-entries.csv").write_text("id,name\nP14635,a\n")
    # A family whose member never appears in the leaf GAF -> no nodes -> skipped.
    (panther / "EMPTY" / "EMPTY-entries.csv").write_text("id,name\nP00000,x\n")

    cache_dir = tmp_path / ".cache"
    _seed_cache(cache_dir)

    counts = fetch_all_family_paint(panther, cache_dir=cache_dir)
    assert counts == {"PTHR1": 2}
    assert (panther / "PTHR1" / "PTHR1-paint.gaf").exists()
    # Empty family is skipped by default.
    assert not (panther / "EMPTY" / "EMPTY-paint.gaf").exists()
