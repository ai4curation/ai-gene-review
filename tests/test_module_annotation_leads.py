"""A module that places a gene in a process the gene's review lacks is a lead."""

from pathlib import Path

import yaml

from ai_gene_review.module_annotation_leads import (
    LEAD_COLUMNS,
    collect_leads,
    write_leads,
)
from tests.test_module_process_conformance import (
    ADRENERGIC_CAMP,
    GPCR_ACTIVITY,
    GRAPH,
    KINASE,
    PLC,
    module,
    write_gene,
)

LABELS = {PLC: "PLC-activating GPCR signaling"}


def write_module(modules_dir: Path, stem: str, doc: dict) -> None:
    """Write one module document into a modules directory."""
    modules_dir.mkdir(exist_ok=True)
    (modules_dir / f"{stem}.yaml").write_text(yaml.safe_dump(doc))


def leads(tmp_path: Path, index: dict) -> list[dict]:
    """Collect leads from ``tmp_path/modules`` with the toy ontology."""
    return collect_leads(
        tmp_path / "modules", gene_index=index, graph=GRAPH, label=LABELS.get
    )


def test_unannotated_process_is_a_lead_and_supported_ones_are_not(tmp_path):
    index = write_gene(tmp_path, "P1", [("involved_in", ADRENERGIC_CAMP, "IBA")])
    index |= write_gene(tmp_path, "P2", [("involved_in", PLC, "IMP")])
    write_module(tmp_path / "modules", "gap", module("P1"))
    write_module(tmp_path / "modules", "fine", module("P2"))
    write_module(tmp_path / "modules", "no_gene_folder", module("P3"))
    rows = leads(tmp_path, index)
    assert [(row["module"], row["gene"]) for row in rows] == [("gap", "UniProtKB:P1")]
    row = rows[0]
    assert row["process_id"] == PLC
    assert row["process_label"] == "PLC-activating GPCR signaling"
    assert row["annoton"] == "receptor"
    assert row["gene_review"].endswith("P1-ai-review.yaml")
    assert set(row) == set(LEAD_COLUMNS)


def test_a_process_the_review_already_asserts_is_not_a_lead(tmp_path):
    index = write_gene(tmp_path, "P1", [("involved_in", ADRENERGIC_CAMP, "IDA")])
    index["P1"].write_text(
        yaml.safe_dump(
            {
                "id": "P1",
                "existing_annotations": [
                    {"term": {"id": PLC}, "review": {"action": "NEW"}}
                ],
            }
        )
    )
    write_module(tmp_path / "modules", "done", module("P1"))
    assert leads(tmp_path, index) == []


def test_leads_are_ranked_by_how_directly_the_module_makes_the_claim(tmp_path):
    """Annoton-stated process first, then receptors and ligands, then the rest."""
    index: dict = {}
    for accession in ("P1", "P2", "P3"):
        index |= write_gene(
            tmp_path, accession, [("involved_in", ADRENERGIC_CAMP, "IBA")]
        )
    write_module(
        tmp_path / "modules", "a_inherited_kinase", module("P1", function=KINASE)
    )
    write_module(
        tmp_path / "modules",
        "b_inherited_receptor",
        module("P2", function=GPCR_ACTIVITY),
    )
    write_module(
        tmp_path / "modules",
        "c_stated_kinase",
        module("P3", function=KINASE, processes=[PLC]),
    )
    rows = leads(tmp_path, index)
    assert [row["module"] for row in rows] == [
        "c_stated_kinase",
        "b_inherited_receptor",
        "a_inherited_kinase",
    ]
    assert [row["process_source"] for row in rows] == ["annoton", "node", "node"]
    assert [row["receptor_or_ligand"] for row in rows] == ["no", "yes", "no"]


def test_annoton_evidence_is_carried_as_the_place_to_start_reading(tmp_path):
    index = write_gene(tmp_path, "P1", [("involved_in", ADRENERGIC_CAMP, "IDA")])
    doc = module("P1")
    doc["module"]["parts"][0]["node"]["annotons"][0]["evidence"] = [
        {"source_id": "PMID:1"},
        {"source_id": "GO_REF:0000033"},
    ]
    write_module(tmp_path / "modules", "m", doc)
    row = leads(tmp_path, index)[0]
    assert row["module_evidence"] == "PMID:1|GO_REF:0000033"
    assert row["goa_sibling_processes"] == ADRENERGIC_CAMP


def test_write_leads_round_trips_as_tsv(tmp_path):
    index = write_gene(tmp_path, "P1", [("involved_in", ADRENERGIC_CAMP, "IBA")])
    write_module(tmp_path / "modules", "gap", module("P1"))
    out = tmp_path / "leads.tsv"
    write_leads(leads(tmp_path, index), out)
    lines = out.read_text().splitlines()
    assert lines[0].split("\t") == list(LEAD_COLUMNS)
    assert len(lines) == 2
