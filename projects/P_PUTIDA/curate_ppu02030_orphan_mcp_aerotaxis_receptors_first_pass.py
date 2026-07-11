#!/usr/bin/env python3
"""First-pass curation for ppu02030 orphan MCP/aerotaxis receptor genes."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


GENES = {
    "PP_0317": {
        "accession": "Q88R17",
        "description": "methyl-accepting chemotaxis transducer with HAMP and MCP signaling domains",
        "mode": "mcp_receptor",
        "core_location": ("GO:0005886", "plasma membrane"),
        "product_quote": "DE   SubName: Full=Methyl-accepting chemotaxis transducer",
        "domain_quote": "DR   InterPro; IPR004090; Chemotax_Me-accpt_rcpt.",
    },
    "PP_0584": {
        "accession": "Q88QB0",
        "description": "methyl-accepting chemotaxis transducer with dCache, HAMP, and MCP signaling domains",
        "mode": "mcp_receptor",
        "core_location": ("GO:0005886", "plasma membrane"),
        "product_quote": "DE   SubName: Full=Methyl-accepting chemotaxis transducer",
        "domain_quote": "DR   InterPro; IPR004090; Chemotax_Me-accpt_rcpt.",
    },
    "PP_0779": {
        "accession": "Q88PR9",
        "description": "methyl-accepting chemotaxis transducer/sensory-box protein with MCP signaling and PAS/PAC sensory domains",
        "mode": "mcp_signaling",
        "core_location": ("GO:0005886", "plasma membrane"),
        "product_quote": "DE   SubName: Full=Methyl-accepting chemotaxis transducer/sensory",
        "domain_quote": "DR   InterPro; IPR004089; MCPsignal_dom.",
    },
    "PP_1819": {
        "accession": "Q88LV8",
        "description": "methyl-accepting chemotaxis transducer with HAMP/HBM and MCP signaling domains",
        "mode": "mcp_signaling",
        "core_location": ("GO:0005886", "plasma membrane"),
        "product_quote": "DE   SubName: Full=Methyl-accepting chemotaxis transducer",
        "domain_quote": "DR   InterPro; IPR004089; MCPsignal_dom.",
    },
    "PP_1940": {
        "accession": "Q88LJ2",
        "description": "methyl-accepting chemotaxis transducer with HAMP, immunoglobulin-like, and MCP signaling domains",
        "mode": "mcp_signaling",
        "core_location": ("GO:0005886", "plasma membrane"),
        "product_quote": "DE   SubName: Full=Methyl-accepting chemotaxis transducer",
        "domain_quote": "DR   InterPro; IPR004089; MCPsignal_dom.",
    },
    "PP_2111": {
        "accession": "Q88L25",
        "description": "predicted aerotaxis receptor in the MCP family with PAS and MCP signaling domains",
        "mode": "aerotaxis",
        "core_location": ("GO:0005886", "plasma membrane"),
        "product_quote": "DE   SubName: Full=Aerotaxis receptor",
        "domain_quote": "DR   InterPro; IPR004090; Chemotax_Me-accpt_rcpt.",
    },
    "ctpH": {
        "accession": "Q88L17",
        "description": "methyl-accepting chemotaxis protein CtpH with HAMP and MCP signaling domains",
        "mode": "mcp_receptor",
        "core_location": ("GO:0005886", "plasma membrane"),
        "product_quote": "DE   SubName: Full=Methyl-accepting chemotaxis protein CtpH",
        "domain_quote": "DR   InterPro; IPR004090; Chemotax_Me-accpt_rcpt.",
    },
    "PP_2257": {
        "accession": "Q88KN3",
        "description": "predicted aerotaxis receptor in the MCP family with PAS and MCP signaling domains",
        "mode": "aerotaxis",
        "core_location": ("GO:0005886", "plasma membrane"),
        "product_quote": "DE   SubName: Full=Aerotaxis receptor",
        "domain_quote": "DR   InterPro; IPR004090; Chemotax_Me-accpt_rcpt.",
    },
    "PP_2823": {
        "accession": "Q88J26",
        "description": "methyl-accepting chemotaxis transducer with HAMP and MCP signaling domains",
        "mode": "mcp_signaling",
        "core_location": ("GO:0005886", "plasma membrane"),
        "product_quote": "DE   SubName: Full=Methyl-accepting chemotaxis transducer",
        "domain_quote": "DR   InterPro; IPR004089; MCPsignal_dom.",
    },
    "PP_3414": {
        "accession": "Q88HE6",
        "description": "methyl-accepting chemotaxis transducer/sensory-box protein with MCP signaling and PAS sensory domains",
        "mode": "mcp_receptor",
        "core_location": ("GO:0016020", "membrane"),
        "product_quote": "DE   SubName: Full=Methyl-accepting chemotaxis transducer/sensory",
        "domain_quote": "DR   InterPro; IPR004090; Chemotax_Me-accpt_rcpt.",
    },
    "PP_3557": {
        "accession": "Q88H08",
        "description": "methyl-accepting chemotaxis transducer with HAMP and MCP signaling domains",
        "mode": "mcp_signaling",
        "core_location": ("GO:0005886", "plasma membrane"),
        "product_quote": "DE   SubName: Full=Methyl-accepting chemotaxis transducer",
        "domain_quote": "DR   InterPro; IPR004089; MCPsignal_dom.",
    },
    "PP_4521": {
        "accession": "Q88EE4",
        "description": "predicted aerotaxis receptor in the MCP family with PAS and MCP signaling domains",
        "mode": "aerotaxis",
        "core_location": ("GO:0005886", "plasma membrane"),
        "product_quote": "DE   SubName: Full=Aerotaxis receptor",
        "domain_quote": "DR   InterPro; IPR004090; Chemotax_Me-accpt_rcpt.",
    },
    "PP_5021": {
        "accession": "Q88D08",
        "description": "methyl-accepting chemotaxis transducer with HAMP/HBM and MCP signaling domains",
        "mode": "mcp_receptor",
        "core_location": ("GO:0005886", "plasma membrane"),
        "product_quote": "DE   SubName: Full=Methyl-accepting chemotaxis transducer",
        "domain_quote": "DR   InterPro; IPR004090; Chemotax_Me-accpt_rcpt.",
    },
}


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping",
    "GO_REF:0000108": "Automatic transfer of experimentally verified manual GO annotation data to orthologs using Ensembl Compara",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


def ref(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def review(summary: str, action: str, reason: str, supported_by: list[dict[str, str]]) -> dict:
    return {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }


def file_ref(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def goa_rows(gene: str) -> dict[str, dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-goa.tsv"
    with path.open(encoding="utf-8") as handle:
        return {row["GO TERM"]: row for row in csv.DictReader(handle, delimiter="\t")}


def goa_quote(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def ensure_references(data: dict, gene: str, cfg: dict) -> None:
    refs = {entry["id"]: entry for entry in data.get("references", [])}
    for ref_id, title in GO_REF_TITLES.items():
        refs.setdefault(ref_id, {"id": ref_id, "title": title, "findings": []})

    goa_id = file_ref(gene, "goa.tsv")
    refs[goa_id] = {
        "id": goa_id,
        "title": f"QuickGO/GOA annotation table for {gene} in Pseudomonas putida KT2440",
        "findings": [],
    }
    uniprot_id = file_ref(gene, "uniprot.txt")
    refs[uniprot_id] = {
        "id": uniprot_id,
        "title": f"UniProt record {cfg['accession']} for {gene} in Pseudomonas putida KT2440",
        "findings": [
            {
                "statement": "UniProt product naming supports the first-pass MCP/aerotaxis receptor assignment.",
                "supporting_text": cfg["product_quote"],
            },
            {
                "statement": "Conserved domain annotation supports a chemotaxis-signaling role.",
                "supporting_text": cfg["domain_quote"],
            },
        ],
    }
    asta_id = file_ref(gene, "deep-research-asta.md")
    refs[asta_id] = {
        "id": asta_id,
        "title": f"Asta retrieval report for {gene} in Pseudomonas putida KT2440",
        "findings": [
            {
                "statement": "Asta retrieval was checked for this first pass; it mainly recapitulates UniProt/domain evidence for this orphan receptor panel.",
                "supporting_text": f"gene_symbol: {gene}",
            }
        ],
    }
    data["references"] = list(refs.values())


def common_support(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> list[dict[str, str]]:
    support = [ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id]))]
    support.append(ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]))
    support.append(ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]))
    support.append(
        ref(
            file_ref(gene, "deep-research-asta.md"),
            cfg["product_quote"].replace("DE   ", "protein_description: '"),
        )
    )
    return support


def review_for_term(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    goa_ref_id = file_ref(gene, "goa.tsv")
    uniprot_ref_id = file_ref(gene, "uniprot.txt")
    if go_id == "GO:0004888":
        return review(
            "Transmembrane signaling receptor activity is appropriate for the MCP/aerotaxis receptor architecture.",
            "ACCEPT",
            "The annotation is an electronic InterPro inference from the methyl-accepting chemotaxis receptor family domain. It is broad, but it is the best available GO molecular-function term for these ligand-unresolved receptor candidates.",
            common_support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0005886":
        return review(
            "Plasma membrane localization is appropriate for a bacterial cell/inner-membrane chemotaxis receptor or transducer.",
            "ACCEPT",
            "The UniProt subcellular-location mapping places the protein at the bacterial cell membrane; for bacterial proteins this is captured by GO:0005886 plasma membrane.",
            [
                ref(goa_ref_id, goa_quote(rows[go_id])),
                ref(uniprot_ref_id, "SUBCELLULAR LOCATION: Cell"),
            ],
        )
    if go_id == "GO:0006935":
        return review(
            "Chemotaxis is the correct broad biological process for this orphan MCP/aerotaxis-receptor panel member.",
            "ACCEPT",
            "The protein name and MCP signaling-domain evidence support a role as a chemotaxis transducer, but the specific ligand and signaling branch remain unresolved in this first pass.",
            common_support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0007165":
        return review(
            "Signal transduction is correct but non-core relative to the more specific chemotaxis-receptor role.",
            "KEEP_AS_NON_CORE",
            "MCP-family proteins transduce sensory input into chemotaxis signaling; the annotation is retained, but chemotaxis and receptor/transducer context are more informative.",
            [
                ref(goa_ref_id, goa_quote(rows[go_id])),
                ref(uniprot_ref_id, cfg["domain_quote"]),
            ],
        )
    if go_id == "GO:0016020":
        if "GO:0005886" in rows:
            return review(
                "Generic membrane localization is supported but less informative than the plasma-membrane annotation.",
                "MARK_AS_OVER_ANNOTATED",
                "The protein is a membrane-associated chemotaxis receptor/transducer, and GOA already carries the more specific bacterial plasma-membrane location.",
                [
                    ref(goa_ref_id, goa_quote(rows[go_id])),
                    ref(goa_ref_id, goa_quote(rows["GO:0005886"])),
                ],
            )
        return review(
            "Generic membrane localization is the only current location annotation for this sensory-box transducer.",
            "ACCEPT",
            "The term is broad, but in the absence of a more specific GOA location it is the best supported location context for the core chemotaxis-transducer assignment.",
            [ref(goa_ref_id, goa_quote(rows[go_id]))],
        )
    if go_id == "GO:0052131":
        return review(
            "Positive aerotaxis is appropriate for entries explicitly named as aerotaxis receptors.",
            "ACCEPT",
            "The protein is named as an aerotaxis receptor and also carries MCP/PAS-family sensory architecture, supporting an aerotaxis-specific chemotaxis process annotation at first-pass depth.",
            [
                ref(goa_ref_id, goa_quote(rows[go_id])),
                ref(uniprot_ref_id, cfg["product_quote"]),
                ref(uniprot_ref_id, "DR   InterPro; IPR000014; PAS."),
            ],
        )
    if go_id == "GO:0005484":
        return review(
            "SNAP receptor activity is not supported for this bacterial aerotaxis receptor.",
            "REMOVE",
            "This looks like InterPro2GO spillover from a syntaxin/SNARE-like signature on an otherwise MCP-family aerotaxis receptor. The bacterial protein context supports chemotaxis sensing, not vesicle-SNARE receptor activity.",
            [
                ref(goa_ref_id, goa_quote(rows[go_id])),
                ref(uniprot_ref_id, "DR   InterPro; IPR006012; Syntaxin/epimorphin_CS."),
                ref(uniprot_ref_id, cfg["product_quote"]),
            ],
        )
    if go_id == "GO:0006886":
        return review(
            "Intracellular protein transport is unsupported for this bacterial aerotaxis receptor.",
            "REMOVE",
            "The transport annotation is an electronic consequence of the same syntaxin/SNARE-like InterPro hit that also produced SNAP receptor activity. The rest of the entry supports MCP-family chemotaxis signaling, not intracellular vesicle/protein transport.",
            [
                ref(goa_ref_id, goa_quote(rows[go_id])),
                ref(uniprot_ref_id, "DR   InterPro; IPR006012; Syntaxin/epimorphin_CS."),
                ref(uniprot_ref_id, cfg["domain_quote"]),
            ],
        )
    if go_id == "GO:0061025":
        return review(
            "Membrane fusion is unsupported for this bacterial aerotaxis receptor.",
            "REMOVE",
            "This annotation is propagated from GO:0005484 rather than from bacterial chemotaxis biology. The entry should be curated as an MCP-family aerotaxis receptor, not a membrane-fusion factor.",
            [
                ref(goa_ref_id, goa_quote(rows[go_id])),
                ref(goa_ref_id, goa_quote(rows["GO:0005484"])),
                ref(uniprot_ref_id, cfg["product_quote"]),
            ],
        )
    raise KeyError(f"Unhandled GO term {go_id} for {gene}")


def core_function(gene: str, cfg: dict, rows: dict[str, dict[str, str]]) -> dict:
    location_id, location_label = cfg["core_location"]
    support = [
        ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
        ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
    ]
    if "GO:0006935" in rows:
        support.append(ref(file_ref(gene, "goa.tsv"), goa_quote(rows["GO:0006935"])))

    if cfg["mode"] == "aerotaxis":
        core = {
            "description": (
                "Predicted MCP-family aerotaxis receptor that contributes sensory input to bacterial chemotaxis; "
                "the direct oxygen/redox-sensing mechanism remains unresolved for KT2440."
            ),
            "molecular_function": {
                "id": "GO:0004888",
                "label": "transmembrane signaling receptor activity",
            },
            "directly_involved_in": [
                {"id": "GO:0052131", "label": "positive aerotaxis"},
                {"id": "GO:0006935", "label": "chemotaxis"},
            ],
            "locations": [{"id": location_id, "label": location_label}],
            "supported_by": support + [ref(file_ref(gene, "goa.tsv"), goa_quote(rows["GO:0052131"]))],
        }
    elif cfg["mode"] == "mcp_receptor":
        core = {
            "description": (
                "Ligand-unresolved methyl-accepting chemotaxis receptor/transducer that likely feeds sensory information into chemotaxis signaling."
            ),
            "molecular_function": {
                "id": "GO:0004888",
                "label": "transmembrane signaling receptor activity",
            },
            "directly_involved_in": [{"id": "GO:0006935", "label": "chemotaxis"}],
            "locations": [{"id": location_id, "label": location_label}],
            "supported_by": support,
        }
    else:
        core = {
            "description": (
                "Ligand-unresolved methyl-accepting chemotaxis transducer/sensory protein that likely contributes to chemotaxis signaling."
            ),
            "directly_involved_in": [{"id": "GO:0006935", "label": "chemotaxis"}],
            "locations": [{"id": location_id, "label": location_label}],
            "supported_by": support,
        }
    return core


def suggested_questions(gene: str, cfg: dict) -> list[dict[str, str]]:
    if cfg["mode"] == "aerotaxis":
        question = (
            f"What oxygen, redox, or energy-state signal is sensed by {gene}, and does it signal through the main Che cluster or a distinct chemosensory branch?"
        )
    else:
        question = (
            f"What chemoeffector ligand is sensed by {gene}, and under which nutrient or root-exudate conditions is this receptor active?"
        )
    return [{"question": question}]


def suggested_experiments(gene: str, cfg: dict) -> list[dict[str, str]]:
    if cfg["mode"] == "aerotaxis":
        description = (
            f"Compare wild type, {gene} deletion, and complemented strains in oxygen-gradient/aerotaxis capillary assays, then test PAS-domain cofactor or redox responsiveness in vitro."
        )
        experiment_type = "aerotaxis assay and PAS-domain biochemical test"
    else:
        description = (
            f"Screen {gene} deletion and complemented strains against candidate carbon, nitrogen, and root-exudate ligands using capillary or microfluidic chemotaxis assays."
        )
        experiment_type = "ligand-screen chemotaxis assay"
    return [{"description": description, "experiment_type": experiment_type}]


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = goa_rows(gene)

    data["status"] = "DRAFT"
    data["gene_symbol"] = gene
    data["description"] = (
        f"{gene} encodes a {cfg['description']} in Pseudomonas putida KT2440. "
        "The receptor is assigned to the ppu02030 chemotaxis boundary, but this first-pass curation does not assign a specific chemoeffector ligand."
    )

    ensure_references(data, gene, cfg)
    for annotation in data["existing_annotations"]:
        go_id = annotation["term"]["id"]
        annotation["review"] = review_for_term(gene, cfg, rows, go_id)

    data["core_functions"] = [core_function(gene, cfg, rows)]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions(gene, cfg)
    data["suggested_experiments"] = suggested_experiments(gene, cfg)

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
