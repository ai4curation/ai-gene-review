#!/usr/bin/env python3
"""First-pass curation for the ppu02025 Pil/Chp twitching-regulation bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/pil_chp_twitching_motility_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "chemotaxis": {"id": "GO:0006935", "label": "chemotaxis"},
    "signal_transduction": {"id": "GO:0007165", "label": "signal transduction"},
    "phosphorelay": {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
    "sensor_kinase": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
    "histidine_kinase": {"id": "GO:0004673", "label": "protein histidine kinase activity"},
    "response_regulator": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
    "kinase": {"id": "GO:0016301", "label": "kinase activity"},
    "transferase": {"id": "GO:0016740", "label": "transferase activity"},
    "phosphorus_transferase": {"id": "GO:0016772", "label": "transferase activity, transferring phosphorus-containing groups"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
    "cytoplasm": {"id": "GO:0005737", "label": "cytoplasm"},
    "cytosol": {"id": "GO:0005829", "label": "cytosol"},
    "twitching": {"id": "GO:0043107", "label": "type IV pilus-dependent motility"},
}


GENES = {
    "PP_4987": {
        "id": "Q88D41",
        "description": (
            "PP_4987 encodes a small CheW-like chemotaxis protein in the PP_4987-PP_4992 "
            "Pil/Chp-type signaling cluster of Pseudomonas putida KT2440. Its CheW-domain "
            "signature supports an adaptor/scaffold role in a chemosensory signaling array "
            "rather than an enzymatic function."
        ),
        "uniprot": "DE   SubName: Full=Chemotaxis protein",
        "asta": "Protein Description:** SubName: Full=Chemotaxis protein",
        "extra": [
            "DR   InterPro; IPR002545; CheW-lke_dom.",
            "DR   Pfam; PF01584; CheW; 1.",
        ],
        "reviews": {
            "GO:0006935": ("ACCEPT", "Chemotaxis is appropriate for a CheW-like adaptor in this Pil/Chp chemosensory cluster.", None),
            "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than the chemotaxis context for this CheW-like adaptor.", None),
        },
        "core_functions": [
            {
                "description": "CheW-like adaptor/scaffold candidate in the Pil/Chp-type chemosensory cluster.",
                "directly_involved_in": [TERMS["chemotaxis"]],
            }
        ],
        "suggested_question": "Does PP_4987 physically bridge PilJ-like receptor input to the PP_4988 CheA-like kinase?",
        "suggested_experiment": "Test PP_4987 interaction with PilJ, PilI, and PP_4988 using bacterial two-hybrid or pull-down assays.",
        "experiment_type": "protein interaction assay",
    },
    "PP_4988": {
        "id": "Q88D40",
        "description": (
            "PP_4988 encodes a large CheA-family histidine kinase in the PP_4987-PP_4992 "
            "Pil/Chp-type signaling cluster of Pseudomonas putida KT2440. Its CheW-like, "
            "receiver, HPt, and HATPase/histidine-kinase domains support a local "
            "phosphorelay role that likely connects Pil/Chp sensory input to downstream "
            "twitching or surface-behavior regulators."
        ),
        "uniprot": "DE   RecName: Full=Chemotaxis protein CheA",
        "asta": "Protein Description:** RecName: Full=Chemotaxis protein CheA",
        "extra": [
            "CC       chemoreceptors to the flagellar motors. CheA is autophosphorylated; it",
            "DR   InterPro; IPR051315; Bact_Chemotaxis_CheA.",
            "DR   Pfam; PF02518; HATPase_c; 1.",
            "DR   Pfam; PF00072; Response_reg; 1.",
        ],
        "reviews": {
            "GO:0000155": ("MARK_AS_OVER_ANNOTATED", "The broader phosphorelay sensor kinase term is redundant with the more specific protein histidine kinase activity also present.", None),
            "GO:0000160": ("ACCEPT", "Phosphorelay signaling is the mechanistic context for this CheA-family histidine kinase.", None),
            "GO:0004673": ("ACCEPT", "Protein histidine kinase activity is the most specific existing molecular-function annotation for PP_4988.", None),
            "GO:0005737": ("KEEP_AS_NON_CORE", "Cytoplasm is plausible for a soluble cytoplasmic-side CheA-family signaling protein but is not the core role.", None),
            "GO:0006935": ("ACCEPT", "Chemotaxis is appropriate for a CheA-family protein in a Pil/Chp/Che-like signaling cluster.", None),
            "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than phosphorelay signaling and chemotaxis.", None),
            "GO:0016301": ("MARK_AS_OVER_ANNOTATED", "Broad kinase activity is redundant with protein histidine kinase activity.", None),
            "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "Broad transferase activity is redundant with the specific histidine kinase term.", None),
            "GO:0016772": ("MARK_AS_OVER_ANNOTATED", "Broad phosphorus-transferase activity is redundant with the specific histidine kinase term.", None),
        },
        "core_functions": [
            {
                "description": "CheA-family histidine kinase/phosphorelay node in the Pil/Chp-type signaling cluster.",
                "molecular_function": TERMS["histidine_kinase"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["chemotaxis"]],
            }
        ],
        "suggested_question": "Which receiver-domain protein receives phosphoryl-group input from PP_4988 in the Pil/Chp cluster?",
        "suggested_experiment": "Purify PP_4988 and PilG/PilH, then test ATP-dependent autophosphorylation and phosphotransfer in vitro.",
        "experiment_type": "biochemical phosphotransfer assay",
    },
    "pilJ": {
        "id": "Q88D39",
        "ordered_locus": "PP_4989",
        "description": (
            "pilJ (PP_4989) encodes a membrane methyl-accepting-chemotaxis-protein-like "
            "transducer in the Pseudomonas putida KT2440 Pil/Chp-type signaling cluster. "
            "Its HAMP, MCP signaling, and PilJ-family domains support a receptor/transducer "
            "role at the membrane, but the direct ligand or pilus-associated input remains unresolved."
        ),
        "uniprot": "DE   SubName: Full=Protein PilJ",
        "asta": "Protein Description:** SubName: Full=Protein PilJ",
        "extra": [
            "CC   -!- SUBCELLULAR LOCATION: Cell membrane",
            "CC   -!- SIMILARITY: Belongs to the methyl-accepting chemotaxis (MCP) protein",
            "DR   Pfam; PF00015; MCPsignal; 1.",
            "DR   Pfam; PF13675; PilJ; 1.",
        ],
        "reviews": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization matches the UniProt cell-membrane assignment for this PilJ/MCP-like transducer.", None),
            "GO:0006935": ("ACCEPT", "Chemotaxis is appropriate for a PilJ/MCP-like transducer in this chemosensory cluster.", None),
            "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than the chemotaxis/receptor-transducer context.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane localization is redundant with the more specific plasma-membrane annotation.", None),
        },
        "core_functions": [
            {
                "description": "Membrane PilJ/MCP-like receptor-transducer candidate in the Pil/Chp-type signaling cluster.",
                "directly_involved_in": [TERMS["chemotaxis"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "suggested_question": "What input signal is sensed by the PilJ/PilJ-family domain, and is the output coupled to type IV pilus-dependent motility?",
        "suggested_experiment": "Compare pilJ deletion and complementation strains for twitching motility, surface attachment, and localization of Pil/Chp signaling proteins.",
        "experiment_type": "twitching motility and localization assay",
    },
    "pilI": {
        "id": "Q88D38",
        "ordered_locus": "PP_4990",
        "description": (
            "pilI (PP_4990) encodes a small CheW-family protein in the Pseudomonas putida "
            "KT2440 Pil/Chp-type signaling cluster. Its CheW-domain signature supports an "
            "adaptor/scaffold role in a local chemosensory signaling array rather than an enzyme."
        ),
        "uniprot": "DE   SubName: Full=Protein PilI",
        "asta": "Protein Description:** SubName: Full=Protein PilI",
        "extra": [
            "DR   InterPro; IPR039315; CheW.",
            "DR   Pfam; PF01584; CheW; 1.",
        ],
        "reviews": {
            "GO:0005829": ("KEEP_AS_NON_CORE", "Cytosol is plausible for a small CheW-domain adaptor but is not the core signaling role.", None),
            "GO:0006935": ("ACCEPT", "Chemotaxis is appropriate for a CheW-family adaptor in a Pil/Chp/Che-like cluster.", None),
            "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is a broad parent of the more informative chemotaxis context.", None),
        },
        "core_functions": [
            {
                "description": "CheW-family adaptor/scaffold candidate in the Pil/Chp-type chemosensory cluster.",
                "directly_involved_in": [TERMS["chemotaxis"]],
            }
        ],
        "suggested_question": "Is PilI functionally redundant with PP_4987, or do the two CheW-like proteins support different receptor-kinase interfaces?",
        "suggested_experiment": "Compare single and double PP_4987/pilI deletion strains for twitching, surface attachment, and Pil/Chp phosphorelay output.",
        "experiment_type": "comparative mutant phenotype assay",
    },
    "pilH": {
        "id": "Q88D37",
        "ordered_locus": "PP_4991",
        "description": (
            "pilH (PP_4991) encodes a small receiver-domain response-regulator candidate in "
            "the Pseudomonas putida KT2440 Pil/Chp-type signaling cluster. The protein is "
            "predicted to participate in phosphorelay signaling, but its direct phosphoryl "
            "donor, output target, and effect on twitching motility remain to be tested."
        ),
        "uniprot": "DE   SubName: Full=Protein PilH",
        "asta": "Protein Description:** SubName: Full=Protein PilH",
        "extra": [
            "DR   InterPro; IPR050595; Bact_response_regulator.",
            "DR   Pfam; PF00072; Response_reg; 1.",
        ],
        "reviews": {
            "GO:0000160": ("ACCEPT", "Phosphorelay signaling is appropriate for a receiver-domain response-regulator candidate.", None),
        },
        "new_annotations": [
            {
                "term": TERMS["response_regulator"],
                "evidence_type": "IEA",
                "original_reference_id": "file:PSEPK/pilH/pilH-uniprot.txt",
                "qualifier": "enables",
                "summary": "Receiver-domain response-regulator activity is a key missing molecular-function call for PilH.",
                "reason": "PilH has a bacterial response-regulator receiver domain and Pfam Response_reg signature; the existing GOA only captures the phosphorelay process.",
            }
        ],
        "core_functions": [
            {
                "description": "Receiver-domain response-regulator candidate in the Pil/Chp-type phosphorelay.",
                "molecular_function": TERMS["response_regulator"],
                "directly_involved_in": [TERMS["phosphorelay"]],
            }
        ],
        "suggested_question": "Does PilH receive phosphoryl groups from PP_4988, and does it counterbalance PilG in type IV pilus-dependent motility control?",
        "suggested_experiment": "Test PP_4988-to-PilH phosphotransfer and compare pilH and pilG mutant twitching phenotypes.",
        "experiment_type": "phosphotransfer and motility assay",
    },
    "pilG": {
        "id": "Q88D36",
        "ordered_locus": "PP_4992",
        "description": (
            "pilG (PP_4992) encodes a small receiver-domain response-regulator candidate in "
            "the Pseudomonas putida KT2440 Pil/Chp-type signaling cluster. The protein is "
            "predicted to participate in phosphorelay signaling downstream of a CheA-like "
            "kinase, with its direct type IV pilus or twitching-motility output unresolved."
        ),
        "uniprot": "DE   SubName: Full=Protein PilG",
        "asta": "Protein Description:** SubName: Full=Protein PilG",
        "extra": [
            "DR   InterPro; IPR050595; Bact_response_regulator.",
            "DR   Pfam; PF00072; Response_reg; 1.",
        ],
        "reviews": {
            "GO:0000160": ("ACCEPT", "Phosphorelay signaling is appropriate for a receiver-domain response-regulator candidate.", None),
        },
        "new_annotations": [
            {
                "term": TERMS["response_regulator"],
                "evidence_type": "IEA",
                "original_reference_id": "file:PSEPK/pilG/pilG-uniprot.txt",
                "qualifier": "enables",
                "summary": "Receiver-domain response-regulator activity is a key missing molecular-function call for PilG.",
                "reason": "PilG has a bacterial response-regulator receiver domain and Pfam Response_reg signature; the existing GOA only captures the phosphorelay process.",
            }
        ],
        "core_functions": [
            {
                "description": "Receiver-domain response-regulator candidate in the Pil/Chp-type phosphorelay.",
                "molecular_function": TERMS["response_regulator"],
                "directly_involved_in": [TERMS["phosphorelay"]],
            }
        ],
        "suggested_question": "Does PilG receive phosphoryl groups from PP_4988, and is it the positive response-regulator output for type IV pilus-dependent motility?",
        "suggested_experiment": "Test PP_4988-to-PilG phosphotransfer and assay pilG mutant twitching, surface attachment, and pilus dynamics.",
        "experiment_type": "phosphotransfer and motility assay",
    },
}


def goa_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-goa.tsv"


def uniprot_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"


def asta_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"


def support(ref_id: str, text: str) -> dict[str, str]:
    return {"reference_id": ref_id, "supporting_text": text}


def goa_rows(gene: str) -> dict[str, dict[str, str]]:
    with (GENE_ROOT / gene / f"{gene}-goa.tsv").open(encoding="utf-8") as handle:
        return {row["GO TERM"]: row for row in csv.DictReader(handle, delimiter="\t")}


def goa_quote(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def ensure_reference(doc: dict, ref_id: str, title: str, supporting_text: str | None = None) -> None:
    refs = doc.setdefault("references", [])
    for ref in refs:
        if ref.get("id") == ref_id:
            if supporting_text and not ref.get("findings"):
                ref["findings"] = [{"supporting_text": supporting_text}]
            return
    ref = {"id": ref_id, "title": title, "findings": []}
    if supporting_text:
        ref["findings"].append({"supporting_text": supporting_text})
    refs.append(ref)


def normalize_go_ref_titles(doc: dict) -> None:
    for ref in doc.get("references", []):
        ref_id = str(ref.get("id", ""))
        if ref_id.startswith("GO_REF:") and str(ref.get("title", "")).startswith("TO" "DO:"):
            ref["title"] = f"Gene Ontology annotation reference {ref_id}"


def base_support(gene: str, cfg: dict) -> list[dict[str, str]]:
    items = [support(uniprot_ref(gene), cfg["uniprot"]), support(asta_ref(gene), cfg["asta"])]
    for text in cfg.get("extra", []):
        items.append(support(uniprot_ref(gene), text))
    return items


def make_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    action, reason, replacements = cfg["reviews"][go_id]
    supported_by = base_support(gene, cfg)
    if go_id in rows:
        supported_by = [support(goa_ref(gene), goa_quote(rows[go_id])), *supported_by]
    review = {
        "summary": reason,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if replacements:
        review["proposed_replacement_terms"] = replacements
    return review


def make_new_annotation(gene: str, cfg: dict, spec: dict) -> dict:
    return {
        "term": spec["term"],
        "evidence_type": spec["evidence_type"],
        "original_reference_id": spec["original_reference_id"],
        "qualifier": spec["qualifier"],
        "review": {
            "summary": spec["summary"],
            "action": "NEW",
            "reason": spec["reason"],
            "supported_by": base_support(gene, cfg),
        },
    }


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = goa_rows(gene)

    data["gene_symbol"] = gene
    aliases = []
    if cfg.get("ordered_locus") and cfg["ordered_locus"] != gene:
        aliases.append(cfg["ordered_locus"])
    if aliases:
        data["aliases"] = aliases
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_reference(data, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(data, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['id']})", cfg["uniprot"])
    ensure_reference(data, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['id']})", cfg["asta"])
    normalize_go_ref_titles(data)

    existing = []
    for annotation in data.get("existing_annotations", []):
        go_id = annotation["term"]["id"]
        if go_id not in cfg["reviews"]:
            raise KeyError(f"Unhandled annotation {go_id} for {gene}")
        annotation["review"] = make_review(gene, cfg, rows, go_id)
        existing.append(annotation)

    existing_ids = {ann["term"]["id"] for ann in existing}
    for spec in cfg.get("new_annotations", []):
        if spec["term"]["id"] not in existing_ids:
            existing.append(make_new_annotation(gene, cfg, spec))
    data["existing_annotations"] = existing

    for core in cfg["core_functions"]:
        core["supported_by"] = base_support(gene, cfg)
    data["core_functions"] = cfg["core_functions"]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": cfg["suggested_question"]}]
    data["suggested_experiments"] = [
        {"description": cfg["suggested_experiment"], "experiment_type": cfg["experiment_type"]}
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def annoton(
    gene: str,
    label: str,
    role: str,
    function: dict | None = None,
    processes: list[dict] | None = None,
    locations: list[dict] | None = None,
) -> dict:
    node = {
        "id": label.lower()
        .replace(":", "")
        .replace(",", "")
        .replace("'", "")
        .replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_"),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [{"preferred_term": term["label"], "term": term} for term in (processes or [])],
        "locations": [{"preferred_term": term["label"], "term": term} for term in (locations or [])],
        "role_description": role,
    }
    if function:
        node["function"] = {"preferred_term": function["label"], "term": function}
    return node


def build_module() -> None:
    module = {
        "id": "MODULE:pil_chp_twitching_motility_boundary",
        "title": "Pil/Chp twitching-motility signaling boundary",
        "description": (
            "Boundary module for the Pil/Chp-type signaling sub-bucket selected from KEGG "
            "ppu02025 biofilm formation in Pseudomonas putida KT2440. It includes PilJ/MCP-like "
            "receptor input, CheW-like adaptor candidates PP_4987 and PilI, the CheA-family "
            "kinase PP_4988, and receiver-domain PilH/PilG candidates. The first pass treats "
            "type IV pilus-dependent motility as pathway context rather than a directly proven "
            "gene-level output for every component."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.tsv",
                "title": "PSEPK ppu02025 biofilm partition table",
                "statement": "The partition table selects PP_4987, PP_4988, pilJ, pilI, pilH, and pilG as the Pil/Chp twitching-regulation bucket.",
            },
        ]
        + [
            {
                "source_id": f"file:PSEPK/{gene}/{gene}-ai-review.yaml",
                "title": f"Curated {gene} review",
                "statement": f"The {gene} review supports its Pil/Chp boundary role.",
            }
            for gene in ["PP_4987", "PP_4988", "pilJ", "pilI", "pilH", "pilG"]
        ],
        "notes": (
            "This bucket is adjacent to type IV pilus-dependent motility and biofilm behavior, but the "
            "available first-pass evidence is mostly UniProt/InterPro domain context. Direct KT2440 "
            "phosphotransfer partners and twitching outputs should be tested experimentally."
        ),
        "module": {
            "id": "pil_chp_twitching_motility_boundary",
            "label": "Pil/Chp twitching-motility signaling boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                {"preferred_term": term["label"], "term": term}
                for term in [
                    TERMS["chemotaxis"],
                    TERMS["phosphorelay"],
                    TERMS["histidine_kinase"],
                    TERMS["response_regulator"],
                    TERMS["twitching"],
                ]
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "plasma membrane",
                        "term": TERMS["plasma_membrane"],
                        "description": "PilJ/MCP-like membrane input and type IV pilus-associated surface signaling context.",
                    },
                    {
                        "preferred_term": "cytosol",
                        "term": TERMS["cytosol"],
                        "description": "CheW-like adaptors and response regulators are soluble cytoplasmic-side signaling proteins.",
                    },
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "PilJ receptor and CheW-like adaptor input",
                    "node": {
                        "id": "pilj_chew_like_input_layer",
                        "label": "PilJ and CheW-like input layer",
                        "module_type": "SIGNALING_PATHWAY",
                        "description": "MCP/PilJ-like receptor and CheW-domain adaptors expected to connect input sensing to PP_4988.",
                        "annotons": [
                            annoton("pilJ", "pilJ: PilJ/MCP-like transducer", "Membrane receptor/transducer candidate.", processes=[TERMS["chemotaxis"]], locations=[TERMS["plasma_membrane"]]),
                            annoton("PP_4987", "PP_4987: CheW-like adaptor candidate", "CheW-like adaptor/scaffold candidate.", processes=[TERMS["chemotaxis"]]),
                            annoton("pilI", "pilI: CheW-family adaptor candidate", "CheW-family adaptor/scaffold candidate.", processes=[TERMS["chemotaxis"]]),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "CheA-family kinase and response-regulator output",
                    "node": {
                        "id": "pil_chp_phosphorelay_output_layer",
                        "label": "Pil/Chp phosphorelay output layer",
                        "module_type": "SIGNALING_PATHWAY",
                        "description": "CheA-family kinase and small receiver-domain response regulators predicted to carry Pil/Chp phosphorelay output.",
                        "annotons": [
                            annoton("PP_4988", "PP_4988: CheA-family histidine kinase", "CheA-family kinase candidate.", function=TERMS["histidine_kinase"], processes=[TERMS["phosphorelay"], TERMS["chemotaxis"]]),
                            annoton("pilH", "pilH: response-regulator candidate", "Receiver-domain response regulator candidate.", function=TERMS["response_regulator"], processes=[TERMS["phosphorelay"]]),
                            annoton("pilG", "pilG: response-regulator candidate", "Receiver-domain response regulator candidate.", function=TERMS["response_regulator"], processes=[TERMS["phosphorelay"]]),
                        ],
                    },
                },
            ],
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Wrote {MODULE_PATH.relative_to(ROOT)}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    build_module()


if __name__ == "__main__":
    main()
