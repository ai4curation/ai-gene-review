"""Tests for emitting curated MOD gene descriptions as deep-research files."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.etl.mod_description_deep_research import (
    emit_mod_deep_research,
    identity_gate,
    render_mod_deep_research,
    uniprot_gene_names,
)
from ai_gene_review.etl.publication_type import classify_reference_id
from ai_gene_review.render import provider_from_deep_research_filename

TEXT = "rab-11.1 encodes a small GTPase; RAB-11.1 localizes to recycling endosomes."


def _doc() -> str:
    return render_mod_deep_research(
        "worm", "rab-11.1", "WormBase", "WB:WBGene00004274", TEXT, "2026-10-30",
        url="https://www.wormbase.org/db/get?name=WBGene00004274;class=Gene",
        uniprot_accession="Q94986",
    )


def test_render_keeps_text_verbatim_and_frontmatter_parses():
    doc = _doc()
    assert TEXT in doc
    front = yaml.safe_load(doc.split("---")[1])
    assert front["provider"] == "wormbase"
    assert front["mod_gene_id"] == "WB:WBGene00004274"
    assert front["citations_provided"] is False
    assert front["fetch_date"] == "2026-10-30"


def test_filename_is_recognised_as_deep_research():
    name = "rab-11.1-deep-research-wormbase.md"
    assert provider_from_deep_research_filename(name) == "wormbase"
    assert classify_reference_id(f"file:worm/rab-11.1/{name}") == "DEEP_RESEARCH"


@pytest.mark.parametrize(
    "gene,uniprot,symbol,systematic,blocked",
    [
        ("rab-11.1", "GN   Name=rab-11.1;", "rab-11.1", "F53G12.1", False),
        ("C28G1.2", "GN   ORFNames=C28G1.2;", "C28G1.2", "C28G1.2", False),
        ("J7SF87", "GN   Name=lin-4;", "lin-4", None, False),
        ("rab-11.1", "GN   Name=rab-11.1;", "rab-10", "T23H2.5", True),
    ],
)
def test_identity_gate(gene, uniprot, symbol, systematic, blocked):
    assert (identity_gate(gene, uniprot, symbol, systematic) is not None) is blocked


def test_uniprot_gene_names_strips_evidence():
    data = "GN   Name=daf-16 {ECO:0000312|WormBase:R13H8.1};\nGN   Synonyms=foxo, x;\n"
    assert uniprot_gene_names(data) == {"daf-16", "foxo", "x"}


def test_human_is_out_of_scope(tmp_path: Path):
    status, path, _ = emit_mod_deep_research("human", "TP53", tmp_path, write=True)
    assert status == "skipped" and path is None


@pytest.mark.integration
def test_emit_worm_gene_from_alliance(tmp_path: Path):
    repo = Path(__file__).resolve().parents[1]
    gene_dir = tmp_path / "genes" / "worm" / "rab-11.1"
    gene_dir.mkdir(parents=True)
    src = repo / "genes" / "worm" / "rab-11.1" / "rab-11.1-uniprot.txt"
    (gene_dir / "rab-11.1-uniprot.txt").write_text(src.read_text())
    status, path, _ = emit_mod_deep_research("worm", "rab-11.1", tmp_path, write=True)
    assert status == "written"
    assert path is not None and "small GTPase" in path.read_text()


@pytest.mark.parametrize("folder,mod", [("CAEEL", "WB"), ("DROME", "FB"), ("fly", "FB"), ("DANRE", "ZFIN"), ("XENLA", "Xenbase"), ("worm", "WB")])
def test_organism_folder_aliases(folder, mod):
    """Repo folders named by UniProt species code resolve to the same MOD as the short names."""
    from ai_gene_review.etl.descriptions import ORGANISM_CONFIG
    assert ORGANISM_CONFIG[folder]["mod"] == mod


@pytest.mark.parametrize(
    "curated,automated,expected",
    [
        ("Enables GTP binding activity. Involved in vesicle transport.", "Something else.", True),
        ("Predicted to enable kinase activity.", None, True),
        ("Enables heterocyclic compound binding activity; metallopeptidase activity; and peptidyl-dipeptidase activity.", "Different.", True),
        ("Same text.", "Same text.", True),
        ("rab-11.1 encodes a small GTPase homologous to Rab proteins.", "Predicted to enable GTP binding.", False),
        ("Ubiquitin-protein ligase; role in proteasome-dependent degradation", "Enables ligase activity.", False),
        ("Part of the CCR4-NOT transcriptional regulatory complex; involved in controlling mRNA initiation", None, False),
        ("Involved in vulval development. rab-11.1 encodes a small GTPase.", None, False),
    ],
)
def test_looks_automated(curated, automated, expected):
    from ai_gene_review.etl.descriptions import looks_automated
    assert looks_automated(curated, automated) is expected
