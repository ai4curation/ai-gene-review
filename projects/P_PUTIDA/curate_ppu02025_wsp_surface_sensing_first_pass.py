#!/usr/bin/env python3
"""First-pass curation for the ppu02025 Wsp-like surface-sensing/c-di-GMP bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/wsp_surface_sensing_c_di_gmp_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "biofilm": {"id": "GO:0042710", "label": "biofilm formation"},
    "chemotaxis": {"id": "GO:0006935", "label": "chemotaxis"},
    "phosphorelay": {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
    "response_regulator": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
    "sensor_kinase": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
    "histidine_kinase": {"id": "GO:0004673", "label": "protein histidine kinase activity"},
    "kinase": {"id": "GO:0016301", "label": "kinase activity"},
    "transferase": {"id": "GO:0016740", "label": "transferase activity"},
    "phosphorus_transferase": {"id": "GO:0016772", "label": "transferase activity, transferring phosphorus-containing groups"},
    "methylesterase": {"id": "GO:0008984", "label": "protein-glutamate methylesterase activity"},
    "glutaminase": {"id": "GO:0050568", "label": "protein-glutamine glutaminase activity"},
    "methyltransferase": {"id": "GO:0008983", "label": "protein-glutamate O-methyltransferase activity"},
    "diguanylate_cyclase": {"id": "GO:0052621", "label": "diguanylate cyclase activity"},
    "catalytic_activity": {"id": "GO:0003824", "label": "catalytic activity"},
    "signal_transduction": {"id": "GO:0007165", "label": "signal transduction"},
    "biofilm_adhesion": {"id": "GO:0043709", "label": "cell adhesion involved in single-species biofilm formation"},
    "negative_flagellar_motility": {"id": "GO:1902201", "label": "negative regulation of bacterial-type flagellum-dependent cell motility"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
    "cytoplasm": {"id": "GO:0005737", "label": "cytoplasm"},
    "cytosol": {"id": "GO:0005829", "label": "cytosol"},
}


GENES = {
    "PP_1488": {
        "id": "Q88MT0",
        "description": (
            "PP_1488 encodes a predicted methyl-accepting chemotaxis transducer in the "
            "PP_1488-PP_1494 Wsp-like surface-sensing cluster of Pseudomonas putida KT2440. "
            "It has HAMP and MCP signaling domains consistent with a membrane chemoreceptor "
            "or transducer that feeds the local CheW/CheA/CheB/GGDEF signaling branch; the "
            "specific ligand or surface cue is unresolved in this first pass."
        ),
        "uniprot": "DE   SubName: Full=Methyl-accepting chemotaxis transducer",
        "asta": "Protein Description:** SubName: Full=Methyl-accepting chemotaxis transducer",
        "extra": [
            "CC   -!- SUBCELLULAR LOCATION: Cell membrane",
            "DR   InterPro; IPR004089; MCPsignal_dom.",
            "DR   Pfam; PF00672; HAMP; 1.",
        ],
        "reviews": {
            "GO:0005886": ("ACCEPT", "Plasma membrane localization is appropriate for a bacterial MCP-like transducer.", None),
            "GO:0006935": ("ACCEPT", "Chemotaxis is the correct broad process for an MCP/HAMP-domain chemosensory transducer.", None),
            "GO:0007165": ("KEEP_AS_NON_CORE", "Signal transduction is true but less informative than the chemotaxis/Wsp-like surface-sensing context.", None),
            "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane localization is less informative than the plasma-membrane call already present.", None),
        },
        "core_functions": [
            {
                "description": "Ligand-unresolved membrane MCP-like transducer in the Wsp-like surface-sensing/c-di-GMP cluster.",
                "directly_involved_in": [TERMS["chemotaxis"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "suggested_question": "What surface cue or ligand is sensed by PP_1488 in the PP_1488-PP_1494 Wsp-like cluster?",
        "suggested_experiment": "Delete PP_1488 and measure surface attachment, c-di-GMP output, and chemotaxis or surface-sensing phenotypes.",
        "experiment_type": "surface-sensing mutant phenotype assay",
    },
    "PP_1489": {
        "id": "Q88MS9",
        "description": (
            "PP_1489 encodes a small CheW-domain protein in the PP_1488-PP_1494 Wsp-like "
            "surface-sensing cluster. It is likely an adaptor or scaffold candidate that links "
            "the MCP-like transducer layer to CheA-family signaling, but GO lacks a specific "
            "CheW molecular-function term and its exact partner set remains unresolved."
        ),
        "uniprot": "DE   SubName: Full=CheW domain protein",
        "asta": "Protein Description:** SubName: Full=CheW domain protein",
        "extra": [
            "DR   InterPro; IPR039315; CheW.",
            "DR   Pfam; PF01584; CheW; 1.",
        ],
        "reviews": {
            "GO:0005829": ("KEEP_AS_NON_CORE", "Cytosol is plausible for a soluble CheW-domain adaptor but is not the core pathway role.", None),
            "GO:0006935": ("ACCEPT", "Chemotaxis is appropriate for a CheW-domain protein in a Wsp/Che-like signaling cluster.", None),
            "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is a broad parent of the more informative chemotaxis context.", None),
        },
        "core_functions": [
            {
                "description": "CheW-domain adaptor/scaffold candidate in the Wsp-like surface-sensing/c-di-GMP cluster.",
                "directly_involved_in": [TERMS["chemotaxis"]],
            }
        ],
        "suggested_question": "Does PP_1489 bind PP_1488, PP_1492, or PP_1491 in a Wsp-like receptor-kinase array?",
        "suggested_experiment": "Test PP_1489 interactions with PP_1488, PP_1491, and PP_1492 using bacterial two-hybrid or pull-down assays.",
        "experiment_type": "protein interaction assay",
    },
    "PP_1491": {
        "id": "Q88MS7",
        "description": (
            "PP_1491 encodes a CheW-family chemotaxis protein in the PP_1488-PP_1494 "
            "Wsp-like cluster. The protein likely acts as a CheW-like adaptor or scaffold "
            "within a local surface-sensing chemosensory array rather than as an enzyme."
        ),
        "uniprot": "DE   RecName: Full=Chemotaxis protein CheW",
        "asta": "Protein Description:** RecName: Full=Chemotaxis protein CheW",
        "extra": [
            "CC   -!- SUBCELLULAR LOCATION: Cytoplasm",
            "DR   InterPro; IPR039315; CheW.",
            "DR   Pfam; PF01584; CheW; 1.",
        ],
        "reviews": {
            "GO:0005737": ("KEEP_AS_NON_CORE", "Cytoplasm is plausible for a soluble CheW-family protein but not the core signaling role.", None),
            "GO:0005829": ("KEEP_AS_NON_CORE", "Cytosol is plausible for a soluble CheW-family protein but is not more informative than the pathway role.", None),
            "GO:0006935": ("ACCEPT", "Chemotaxis is appropriate for a CheW-family protein in a Wsp/Che-like signaling cluster.", None),
            "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is a broad parent of the more informative chemotaxis context.", None),
        },
        "core_functions": [
            {
                "description": "CheW-family adaptor/scaffold candidate in the Wsp-like surface-sensing/c-di-GMP cluster.",
                "directly_involved_in": [TERMS["chemotaxis"]],
            }
        ],
        "suggested_question": "Is PP_1491 functionally redundant with PP_1489 or does each CheW-domain protein support a distinct receptor-kinase interface?",
        "suggested_experiment": "Compare single and double PP_1489/PP_1491 deletions for surface-associated c-di-GMP and biofilm phenotypes.",
        "experiment_type": "comparative mutant phenotype assay",
    },
    "PP_1492": {
        "id": "Q88MS6",
        "description": (
            "PP_1492 encodes a CheA-family histidine kinase in the PP_1488-PP_1494 Wsp-like "
            "surface-sensing cluster. Its CheW-like, receiver, HPt, and histidine-kinase "
            "domains support a local phosphorelay role that likely couples receptor/adaptor "
            "input to downstream c-di-GMP output rather than the canonical PP_4338 CheA "
            "flagellar chemotaxis branch."
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
            "GO:0000160": ("ACCEPT", "Phosphorelay signaling is the mechanistic context for a CheA-family histidine kinase.", None),
            "GO:0004673": ("ACCEPT", "Protein histidine kinase activity is the most specific existing molecular-function annotation for this CheA-family kinase.", None),
            "GO:0006935": ("ACCEPT", "Chemotaxis is appropriate for a CheA-family protein in this Wsp/Che-like cluster, with the local output likely tied to surface sensing and c-di-GMP.", None),
            "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than phosphorelay signaling and chemotaxis.", None),
            "GO:0016301": ("MARK_AS_OVER_ANNOTATED", "Broad kinase activity is redundant with protein histidine kinase activity.", None),
            "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "Broad transferase activity is redundant with the specific histidine kinase term.", None),
            "GO:0016772": ("MARK_AS_OVER_ANNOTATED", "Broad phosphorus-transferase activity is redundant with the specific histidine kinase term.", None),
        },
        "core_functions": [
            {
                "description": "CheA-family histidine kinase/phosphorelay node in the Wsp-like surface-sensing/c-di-GMP cluster.",
                "molecular_function": TERMS["histidine_kinase"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["chemotaxis"]],
            }
        ],
        "suggested_question": "Which PP_1488-PP_1494 cluster response-regulator or GGDEF-domain partner receives phosphoryl-group input from PP_1492?",
        "suggested_experiment": "Purify PP_1492 and candidate receiver-domain partners, then test ATP-dependent autophosphorylation and phosphotransfer.",
        "experiment_type": "biochemical phosphotransfer assay",
    },
    "cheB3": {
        "id": "Q88MS5",
        "ordered_locus": "PP_1493",
        "description": (
            "cheB3 encodes a CheB-family chemotaxis adaptation enzyme in the PP_1488-PP_1494 "
            "Wsp-like cluster. It has an N-terminal receiver domain and C-terminal CheB "
            "methylesterase domain and is predicted to demethylate and deamidate MCP-family "
            "receptor substrates during local surface-sensing or chemotaxis adaptation."
        ),
        "uniprot": "DE   RecName: Full=Protein-glutamate methylesterase/protein-glutamine glutaminase of group 3 operon",
        "asta": "Protein Description:** RecName: Full=Protein-glutamate methylesterase/protein-glutamine",
        "extra": [
            "CC   -!- FUNCTION: Involved in chemotaxis. Part of a chemotaxis signal",
            "CC       residues introduced into the chemoreceptors (methyl-accepting",
            "CC       deamidation of specific glutamine residues to glutamic acid.",
            "DR   InterPro; IPR008248; CheB-like.",
            "DR   Pfam; PF01339; CheB_methylest; 1.",
        ],
        "reviews": {
            "GO:0000156": ("ACCEPT", "Receiver-domain response-regulator activity is appropriate for CheB3.", None),
            "GO:0000160": ("ACCEPT", "Phosphorelay signaling is appropriate for CheB3's receiver-domain regulation in a Che-like cluster.", None),
            "GO:0005737": ("ACCEPT", "Cytoplasm is appropriate for this soluble CheB-family adaptation enzyme.", None),
            "GO:0006935": ("ACCEPT", "Chemotaxis is the correct process context for CheB3 receptor-adaptation chemistry.", None),
            "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than phosphorelay and chemotaxis context.", None),
            "GO:0008984": ("ACCEPT", "Protein-glutamate methylesterase activity is a core CheB catalytic function.", None),
            "GO:0050568": ("ACCEPT", "Protein-glutamine glutaminase activity is a second core CheB catalytic function.", None),
        },
        "core_functions": [
            {
                "description": "CheB-family receptor methylesterase activity for chemotaxis/surface-sensing adaptation.",
                "molecular_function": TERMS["methylesterase"],
                "directly_involved_in": [TERMS["chemotaxis"], TERMS["phosphorelay"]],
                "locations": [TERMS["cytoplasm"]],
            },
            {
                "description": "CheB-family receptor glutaminase activity that deamidates MCP glutamine residues during adaptation.",
                "molecular_function": TERMS["glutaminase"],
                "directly_involved_in": [TERMS["chemotaxis"], TERMS["phosphorelay"]],
                "locations": [TERMS["cytoplasm"]],
            },
        ],
        "suggested_question": "Which MCP-like receptor in the PP_1488-PP_1494 cluster is the direct CheB3 substrate?",
        "suggested_experiment": "Assay CheB3 methylesterase and glutaminase activity on PP_1488-derived receptor peptides or intact receptor domains.",
        "experiment_type": "enzyme-substrate assay",
    },
    "PP_1494": {
        "id": "Q88MS4",
        "description": (
            "PP_1494 encodes a receiver-domain GGDEF diguanylate cyclase in the PP_1488-PP_1494 "
            "Wsp-like surface-sensing cluster. It likely converts local Che-like signaling into "
            "c-di-GMP production that promotes biofilm-associated adhesion and reduces flagellar "
            "motility, although direct substrates and regulatory inputs remain unresolved."
        ),
        "uniprot": "DE   RecName: Full=diguanylate cyclase",
        "asta": "Protein Description:** RecName: Full=diguanylate cyclase",
        "extra": [
            "CC       Reaction=2 GTP = 3',3'-c-di-GMP + 2 diphosphate;",
            "CC   -!- SUBCELLULAR LOCATION: Cell inner membrane",
            "DR   InterPro; IPR050469; Diguanylate_Cyclase.",
            "DR   Pfam; PF00990; GGDEF; 1.",
        ],
        "reviews": {
            "GO:0000160": ("KEEP_AS_NON_CORE", "The receiver-domain architecture supports phosphorelay context, but the core output is c-di-GMP synthesis.", None),
            "GO:0003824": ("MODIFY", "Generic catalytic activity should be replaced by the specific diguanylate cyclase activity already present.", [TERMS["diguanylate_cyclase"]]),
            "GO:0005886": ("ACCEPT", "Plasma membrane localization is appropriate for the UniProt cell-inner-membrane assignment.", None),
            "GO:0043709": ("ACCEPT", "Biofilm-associated adhesion is plausible for a Wsp-like GGDEF output enzyme and is the specific TreeGrafter process call.", None),
            "GO:0052621": ("ACCEPT", "Diguanylate cyclase activity is the core GGDEF-domain molecular function.", None),
            "GO:1902201": ("ACCEPT", "Negative regulation of flagellum-dependent motility fits elevated c-di-GMP output from a GGDEF enzyme in a biofilm-associated branch.", None),
        },
        "core_functions": [
            {
                "description": "Receiver-domain GGDEF diguanylate cyclase activity that produces c-di-GMP in a Wsp-like surface-sensing branch.",
                "molecular_function": TERMS["diguanylate_cyclase"],
                "directly_involved_in": [TERMS["biofilm_adhesion"], TERMS["negative_flagellar_motility"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ],
        "suggested_question": "Is PP_1494 activated by PP_1492-dependent phosphorelay signaling, and how much does it contribute to local c-di-GMP pools?",
        "suggested_experiment": "Measure c-di-GMP levels and biofilm/flagellar phenotypes in PP_1494 catalytic-site and receiver-domain mutants.",
        "experiment_type": "c-di-GMP and biofilm phenotype assay",
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

    for annotation in data.get("existing_annotations", []):
        go_id = annotation["term"]["id"]
        if go_id not in cfg["reviews"]:
            raise KeyError(f"Unhandled annotation {go_id} for {gene}")
        annotation["review"] = make_review(gene, cfg, rows, go_id)

    for core in cfg["core_functions"]:
        core["supported_by"] = base_support(gene, cfg)
    data["core_functions"] = cfg["core_functions"]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": cfg["suggested_question"]}]
    data["suggested_experiments"] = [
        {
            "description": cfg["suggested_experiment"],
            "experiment_type": cfg["experiment_type"],
        }
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def annoton(gene: str, label: str, processes: list[dict], role: str, function: dict | None = None, locations: list[dict] | None = None) -> dict:
    item = {
        "id": label.lower().replace(":", "").replace(" ", "_").replace("/", "_").replace("-", "_"),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [{"preferred_term": term["label"], "term": term} for term in processes],
        "locations": [{"preferred_term": term["label"], "term": term} for term in (locations or [])],
        "role_description": role,
    }
    if function:
        item["function"] = {"preferred_term": function["label"], "term": function}
    return item


def build_module() -> None:
    module = {
        "id": "MODULE:wsp_surface_sensing_c_di_gmp_boundary",
        "title": "Wsp-like surface sensing and c-di-GMP boundary",
        "description": (
            "Boundary module for the PP_1488-PP_1494 Wsp-like surface-sensing cluster "
            "selected from KEGG ppu02025 biofilm formation in Pseudomonas putida KT2440. "
            "The module links an MCP-like transducer, CheW-like adaptors, WspC/CheR1 "
            "methyltransferase context, a CheA-family kinase, CheB3 adaptation chemistry, "
            "and a GGDEF diguanylate cyclase output. The first pass treats this as a "
            "biofilm/surface-sensing boundary rather than the canonical flagellar "
            "chemotaxis core."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.tsv",
                "title": "PSEPK ppu02025 biofilm partition table",
                "statement": (
                    "The partition table selects PP_1488, PP_1489, PP_1491, PP_1492, "
                    "cheB3, and PP_1494 as the Wsp-like chemotaxis/c-di-GMP cluster."
                ),
            },
            {
                "source_id": "file:PSEPK/wspC/wspC-ai-review.yaml",
                "title": "Curated wspC review",
                "statement": "The wspC review places CheR1/WspC in a biofilm-control chemosensory route.",
            },
        ]
        + [
            {
                "source_id": f"file:PSEPK/{gene}/{gene}-ai-review.yaml",
                "title": f"Curated {gene} review",
                "statement": f"The {gene} review supports its Wsp-like surface-sensing/c-di-GMP cluster role.",
            }
            for gene in ["PP_1488", "PP_1489", "PP_1491", "PP_1492", "cheB3", "PP_1494"]
        ],
        "notes": (
            "WspC/PP_1490 was already curated during the ppu02020 alginate/biofilm "
            "boundary pass and is included here as local cluster context. PP_1494 is "
            "the current c-di-GMP output candidate for this selected ppu02025 bucket; "
            "the separately named KT2440 WspR/PP_4959 remains outside this sub-batch."
        ),
        "module": {
            "id": "wsp_surface_sensing_c_di_gmp_boundary",
            "label": "Wsp-like surface sensing and c-di-GMP boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                {"preferred_term": term["label"], "term": term}
                for term in [
                    TERMS["chemotaxis"],
                    TERMS["phosphorelay"],
                    TERMS["histidine_kinase"],
                    TERMS["methyltransferase"],
                    TERMS["methylesterase"],
                    TERMS["glutaminase"],
                    TERMS["diguanylate_cyclase"],
                    TERMS["biofilm"],
                    TERMS["biofilm_adhesion"],
                    TERMS["negative_flagellar_motility"],
                ]
            ],
            "context": {
                "cellular_components": [
                    {
                        "preferred_term": "plasma membrane",
                        "term": TERMS["plasma_membrane"],
                        "description": "Membrane-proximal receptor and GGDEF output context.",
                    },
                    {
                        "preferred_term": "cytoplasm",
                        "term": TERMS["cytoplasm"],
                        "description": "Soluble adaptor, kinase, and adaptation enzymes act from the cytoplasmic side.",
                    },
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "Wsp-like receptor/adaptor input layer",
                    "node": {
                        "id": "wsp_like_receptor_adaptor_input",
                        "label": "Wsp-like receptor/adaptor input",
                        "module_type": "SIGNALING_PATHWAY",
                        "description": "MCP-like transducer and CheW-domain proteins that likely assemble a local receptor-kinase signaling array.",
                        "annotons": [
                            annoton("PP_1488", "PP_1488: MCP-like transducer", [TERMS["chemotaxis"]], "Ligand-unresolved MCP-like transducer.", locations=[TERMS["plasma_membrane"]]),
                            annoton("PP_1489", "PP_1489: CheW-domain adaptor candidate", [TERMS["chemotaxis"]], "CheW-domain adaptor/scaffold candidate."),
                            annoton("PP_1491", "PP_1491: CheW-family adaptor candidate", [TERMS["chemotaxis"]], "CheW-family adaptor/scaffold candidate."),
                            annoton("wspC", "wspC: Wsp/CheR1 methyltransferase context", [TERMS["biofilm"]], "CheR-type methyltransferase in the local Wsp biofilm-control route.", function=TERMS["methyltransferase"]),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "CheA/CheB phosphorelay and adaptation layer",
                    "node": {
                        "id": "wsp_like_phosphorelay_adaptation",
                        "label": "Wsp-like phosphorelay and adaptation",
                        "module_type": "SIGNALING_PATHWAY",
                        "description": "CheA-family kinase and CheB3 adaptation enzyme that likely transmit and tune local Wsp-like signaling.",
                        "annotons": [
                            annoton("PP_1492", "PP_1492: CheA-family histidine kinase", [TERMS["phosphorelay"], TERMS["chemotaxis"]], "CheA-family kinase in the Wsp-like branch.", function=TERMS["histidine_kinase"]),
                            annoton("cheB3", "cheB3: CheB methylesterase adaptation enzyme", [TERMS["phosphorelay"], TERMS["chemotaxis"]], "CheB-family methylesterase/glutaminase adaptation enzyme.", function=TERMS["methylesterase"], locations=[TERMS["cytoplasm"]]),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "c-di-GMP output layer",
                    "node": {
                        "id": "wsp_like_c_di_gmp_output",
                        "label": "Wsp-like c-di-GMP output",
                        "module_type": "SIGNALING_PATHWAY",
                        "description": "GGDEF output candidate that produces c-di-GMP and shifts cells toward biofilm-associated adhesion and reduced flagellar motility.",
                        "annotons": [
                            annoton("PP_1494", "PP_1494: GGDEF diguanylate cyclase", [TERMS["biofilm_adhesion"], TERMS["negative_flagellar_motility"]], "Receiver-domain GGDEF diguanylate cyclase output candidate.", function=TERMS["diguanylate_cyclase"], locations=[TERMS["plasma_membrane"]]),
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
