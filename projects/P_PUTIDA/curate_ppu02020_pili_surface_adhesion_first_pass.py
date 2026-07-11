#!/usr/bin/env python3
"""First-pass curation for the ppu02020 pili/surface adhesion bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/pili_surface_adhesion_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "sensor_kinase": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
    "response_regulator": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
    "structural_molecule": {"id": "GO:0005198", "label": "structural molecule activity"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "transcription_reg": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "cell_adhesion": {"id": "GO:0007155", "label": "cell adhesion"},
    "signal_transduction": {"id": "GO:0007165", "label": "signal transduction"},
    "osmosensory": {"id": "GO:0007234", "label": "osmosensory signaling via phosphorelay pathway"},
    "detection_visible_light": {"id": "GO:0009584", "label": "detection of visible light"},
    "cell_outer_membrane": {"id": "GO:0009279", "label": "cell outer membrane"},
    "pilus": {"id": "GO:0009289", "label": "pilus"},
    "pilus_assembly": {"id": "GO:0009297", "label": "pilus assembly"},
    "fimbrial_usher": {"id": "GO:0015473", "label": "fimbrial usher porin activity"},
    "t2ss_complex": {"id": "GO:0015627", "label": "type II protein secretion system complex"},
    "t2ss_secretion": {"id": "GO:0015628", "label": "protein secretion by the type II secretion system"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
    "polysaccharide_transporter": {"id": "GO:0015159", "label": "polysaccharide transmembrane transporter activity"},
    "polysaccharide_transport": {"id": "GO:0015774", "label": "polysaccharide transport"},
    "periplasmic_space_omb": {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"},
    "protein_kinase_activator": {"id": "GO:0030295", "label": "protein kinase activator activity"},
    "type_iv_pilus": {"id": "GO:0044096", "label": "type IV pilus"},
    "periplasmic_space": {"id": "GO:0042597", "label": "periplasmic space"},
    "type_iv_motility": {"id": "GO:0043107", "label": "type IV pilus-dependent motility"},
    "transmembrane_transport": {"id": "GO:0055085", "label": "transmembrane transport"},
    "cell_wall_org": {"id": "GO:0071555", "label": "cell wall organization"},
}


USHER_REVIEWS = {
    "GO:0009279": ("ACCEPT", "The fimbrial usher is an outer-membrane assembly pore.", None),
    "GO:0009297": ("ACCEPT", "Fimbrial usher porins mediate pilus assembly.", None),
    "GO:0015473": ("ACCEPT", "Fimbrial usher porin activity is the core molecular function of this outer-membrane assembly protein.", None),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than cell outer membrane.", None),
    "GO:0055085": ("KEEP_AS_NON_CORE", "Transmembrane transport is broad context for usher-mediated pilus-subunit assembly.", None),
}


CHAPERONE_REVIEWS = {
    "GO:0030288": ("ACCEPT", "The chaperone is predicted to act in the outer membrane-bounded periplasmic space.", None),
    "GO:0042597": ("ACCEPT", "Periplasmic space is correct for a PapD-like pilus assembly chaperone.", None),
    "GO:0071555": (
        "MODIFY",
        "Cell wall organization is broad; the local domain context supports pilus assembly as the more specific process.",
        [TERMS["pilus_assembly"]],
    ),
}


SENSOR_REVIEWS = {
    "GO:0000155": ("ACCEPT", "The protein has conserved sensor histidine kinase architecture.", None),
    "GO:0000156": ("REMOVE", "The reviewed domain evidence supports a sensor histidine kinase, not an independent response regulator activity.", None),
    "GO:0004673": ("ACCEPT", "Protein histidine kinase activity is the core catalytic activity of this sensor kinase.", None),
    "GO:0005886": ("ACCEPT", "The sensor kinase is annotated as a plasma-membrane protein.", None),
    "GO:0006355": ("KEEP_AS_NON_CORE", "Transcription regulation is downstream context for this regulatory sensor.", None),
    "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than sensor histidine kinase signaling.", None),
    "GO:0007234": ("UNDECIDED", "The osmosensory assignment is a specific propagated inference not resolved in this first pass.", None),
    "GO:0009584": ("ACCEPT", "The phytochrome/GAF/PAS input-domain architecture supports visible-light detection.", None),
    "GO:0016301": ("MARK_AS_OVER_ANNOTATED", "Generic kinase activity is less informative than protein histidine kinase activity.", None),
    "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "Generic transferase activity is less informative than protein histidine kinase activity.", None),
    "GO:0030295": ("REMOVE", "Protein kinase activator activity is not supported as an independent function by the histidine-kinase domain architecture.", None),
}


POLY_EXPORT_REVIEWS = {
    "GO:0009279": ("ACCEPT", "The polysaccharide export protein is annotated as a cell outer-membrane protein.", None),
    "GO:0015159": ("ACCEPT", "Polysaccharide transmembrane transporter activity is the core inferred function.", None),
    "GO:0015774": ("ACCEPT", "Polysaccharide transport is the matching biological process for this export protein.", None),
}


GENES = {
    "fimD": {
        "id": "Q88LP0",
        "ordered_locus": "PP_1889",
        "class": "usher",
        "description": (
            "fimD encodes a predicted fimbrial usher protein in Pseudomonas putida KT2440. "
            "Its fimbrial usher/PapC-family domains support an outer-membrane porin role in "
            "chaperone-usher pilus assembly."
        ),
        "uniprot": "DE   SubName: Full=Type 1 pili subunit FimD",
        "asta": "Protein Description:** SubName: Full=Type 1 pili subunit FimD",
        "uniprot_extra": "CC   -!- SIMILARITY: Belongs to the fimbrial export usher family.",
        "uniprot_extra_2": "DR   InterPro; IPR000015; Fimb_usher.",
        "reviews": USHER_REVIEWS,
    },
    "PP_1890": {
        "id": "Q88LN9",
        "ordered_locus": "PP_1890",
        "class": "chaperone",
        "description": (
            "PP_1890 encodes a FimC/PapD-like periplasmic pilus chaperone in Pseudomonas putida KT2440. "
            "Its PapD-like and periplasmic pilus chaperone domains support a chaperone-usher pilus assembly role."
        ),
        "uniprot": "DE   SubName: Full=Type 1 pili chaperone protein FimC",
        "asta": "Protein Description:** SubName: Full=Type 1 pili chaperone protein FimC",
        "uniprot_extra": "CC   -!- SIMILARITY: Belongs to the periplasmic pilus chaperone family.",
        "uniprot_extra_2": "DR   InterPro; IPR001829; Pili_assmbl_chaperone_bac.",
        "reviews": CHAPERONE_REVIEWS,
    },
    "PP_2356": {
        "id": "Q88KD4",
        "ordered_locus": "PP_2356",
        "class": "sensor",
        "description": (
            "PP_2356 encodes a predicted phytochrome-like sensor histidine kinase in Pseudomonas putida KT2440. "
            "Its GAF/PAS/phytochrome input domains and HisKA/HATPase catalytic domains support a membrane-associated "
            "sensory phosphorelay role near a Csu-like surface-adhesion cluster."
        ),
        "uniprot": "DE   RecName: Full=histidine kinase",
        "asta": "Protein Description:** RecName: Full=histidine kinase",
        "uniprot_extra": "DR   InterPro; IPR001294; Phytochrome.",
        "uniprot_extra_2": "DR   InterPro; IPR005467; His_kinase_dom.",
        "uniprot_extra_3": "DR   InterPro; IPR003594; HATPase_dom.",
        "reviews": SENSOR_REVIEWS,
    },
    "PP_2361": {
        "id": "Q88KC9",
        "ordered_locus": "PP_2361",
        "class": "chaperone",
        "description": (
            "PP_2361 encodes a predicted PapD-like pilus chaperone in Pseudomonas putida KT2440. "
            "Its periplasmic pilus chaperone N-domain supports an accessory role in the adjacent Csu-like "
            "chaperone-usher surface-adhesion cluster."
        ),
        "uniprot": "DE   SubName: Full=Chaperone protein",
        "asta": "Protein Description:** SubName: Full=Chaperone protein",
        "uniprot_extra": "DR   InterPro; IPR050643; Periplasmic_pilus_chap.",
        "uniprot_extra_2": "DR   InterPro; IPR016147; Pili_assmbl_chaperone_N.",
        "reviews": {k: v for k, v in CHAPERONE_REVIEWS.items() if k != "GO:0042597"},
    },
    "PP_2362": {
        "id": "Q88KC8",
        "ordered_locus": "PP_2362",
        "class": "usher",
        "description": (
            "PP_2362 encodes a predicted fimbrial usher protein in Pseudomonas putida KT2440. "
            "Its Fimb_usher and PapC-like domains support an outer-membrane pilus assembly pore role "
            "in the adjacent Csu-like surface-adhesion cluster."
        ),
        "uniprot": "DE   SubName: Full=Usher protein",
        "asta": "Protein Description:** SubName: Full=Usher protein",
        "uniprot_extra": "DR   InterPro; IPR000015; Fimb_usher.",
        "uniprot_extra_2": "DR   InterPro; IPR042186; FimD_plug_dom.",
        "reviews": USHER_REVIEWS,
    },
    "PP_3126": {
        "id": "Q88I75",
        "ordered_locus": "PP_3126",
        "class": "poly_export",
        "description": (
            "PP_3126 encodes a predicted BexD/CtrA/VexA-family polysaccharide export protein in "
            "Pseudomonas putida KT2440. It is retained in this ppu02020 partition as surface-envelope "
            "context rather than a canonical two-component signaling protein."
        ),
        "uniprot": "DE   SubName: Full=Polysaccharide exported protein",
        "asta": "Protein Description:** SubName: Full=Polysaccharide exported protein",
        "uniprot_extra": "CC   -!- SIMILARITY: Belongs to the BexD/CtrA/VexA family.",
        "uniprot_extra_2": "DR   InterPro; IPR049712; Poly_export.",
        "reviews": POLY_EXPORT_REVIEWS,
    },
}


CSU_SUBUNITS = {
    "PP_2357": ("Q88KD3", "PP_2357", "Type 1 pili protein CsuB"),
    "PP_2358": ("Q88KD2", "PP_2358", "Type 1 pili subunit CsuA/B protein"),
    "PP_2359": ("Q88KD1", "PP_2359", "Type 1 pili subunit CsuA/B protein"),
    "PP_2360": ("Q88KD0", "PP_2360", "Type 1 pili subunit CsuA/B protein"),
    "PP_2363": ("Q88KC7", "PP_2363", "Spore coat protein U/FanG domain-containing protein"),
}


for gene, (accession, locus, product) in CSU_SUBUNITS.items():
    genes_extra = {
        "id": accession,
        "ordered_locus": locus,
        "class": "csu_subunit",
        "description": (
            f"{gene} encodes a predicted Csu/FanG-like surface-structure subunit in Pseudomonas putida KT2440. "
            "The product name and Spore coat U/FanG domain support a structural or accessory role in the adjacent "
            "Csu-like chaperone-usher surface-adhesion cluster, but the exact assembled structure remains unresolved."
        ),
        "uniprot": f"DE   SubName: Full={product}" if gene != "PP_2363" else "DE   RecName: Full=Spore coat protein U/FanG domain-containing protein",
        "asta": f"Protein Description:** SubName: Full={product}" if gene != "PP_2363" else "Protein Description:** RecName: Full=Spore coat protein U/FanG domain-containing protein",
        "uniprot_extra": "DR   InterPro; IPR007893; Spore_coat_U/FanG.",
        "reviews": {},
    }
    GENES[gene] = genes_extra


def goa_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-goa.tsv"


def uniprot_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"


def asta_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"


def falcon_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-falcon.md"


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
    for key in ("uniprot_extra", "uniprot_extra_2", "uniprot_extra_3"):
        if cfg.get(key):
            items.append(support(uniprot_ref(gene), cfg[key]))
    return items


def make_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    action, reason, replacements = cfg["reviews"][go_id]
    label = rows[go_id]["GO NAME"]
    review = {
        "summary": reason,
        "action": action,
        "reason": reason,
        "supported_by": [
            support(goa_ref(gene), goa_quote(rows[go_id])),
            *base_support(gene, cfg),
        ],
    }
    if replacements:
        review["proposed_replacement_terms"] = replacements
    if action == "MARK_AS_OVER_ANNOTATED":
        review["summary"] = f"{label} is plausible but too broad as a core annotation."
    return review


def new_annotation(gene: str, cfg: dict, term: dict, qualifier: str, summary: str, reason: str) -> dict:
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": uniprot_ref(gene),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": base_support(gene, cfg),
        },
    }


def core_functions(gene: str, cfg: dict) -> list[dict]:
    cls = cfg["class"]
    if cls == "usher":
        cores = [
            {
                "description": "Outer-membrane fimbrial usher porin supporting chaperone-usher pilus assembly.",
                "molecular_function": TERMS["fimbrial_usher"],
                "directly_involved_in": [TERMS["pilus_assembly"]],
                "locations": [TERMS["cell_outer_membrane"]],
            }
        ]
    elif cls == "chaperone":
        locations = [TERMS["periplasmic_space_omb"]]
        if gene == "PP_1890":
            locations.append(TERMS["periplasmic_space"])
        cores = [
            {
                "description": "Periplasmic PapD-like chaperone supporting pilus surface-structure assembly.",
                "directly_involved_in": [TERMS["pilus_assembly"]],
                "locations": locations,
            }
        ]
    elif cls == "sensor":
        cores = [
            {
                "description": "Phytochrome-like sensor histidine kinase in surface-adhesion cluster context.",
                "molecular_function": TERMS["sensor_kinase"],
                "directly_involved_in": [TERMS["detection_visible_light"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ]
    elif cls == "poly_export":
        cores = [
            {
                "description": "Outer-membrane polysaccharide transmembrane transporter/export protein.",
                "molecular_function": TERMS["polysaccharide_transporter"],
                "directly_involved_in": [TERMS["polysaccharide_transport"]],
                "locations": [TERMS["cell_outer_membrane"]],
            }
        ]
    elif cls == "csu_subunit":
        cores = [
            {
                "description": "Predicted Csu/FanG-like structural component of a surface-adhesion pilus-like assembly.",
                "molecular_function": TERMS["structural_molecule"],
                "directly_involved_in": [TERMS["pilus_assembly"]],
            }
        ]
    else:
        raise ValueError(cls)
    for core in cores:
        core["supported_by"] = base_support(gene, cfg)
    return cores


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = goa_rows(gene)

    data["gene_symbol"] = gene
    data["aliases"] = [cfg["ordered_locus"]]
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_reference(data, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(data, uniprot_ref(gene), f"UniProtKB entry for {gene} ({cfg['id']})", cfg["uniprot"])
    ensure_reference(data, asta_ref(gene), f"Asta retrieval report for {gene} ({cfg['id']})", cfg["asta"])
    normalize_go_ref_titles(data)

    synthetic_ids = set()
    if cfg["class"] == "csu_subunit":
        synthetic_ids = {TERMS["structural_molecule"]["id"], TERMS["pilus_assembly"]["id"]}
    elif cfg["class"] == "chaperone":
        synthetic_ids = {TERMS["pilus_assembly"]["id"]}
    if synthetic_ids:
        data["existing_annotations"] = [
            annotation
            for annotation in data.get("existing_annotations", [])
            if annotation.get("term", {}).get("id") not in synthetic_ids
            or annotation.get("review", {}).get("action") != "NEW"
        ]

    for annotation in data.get("existing_annotations", []):
        go_id = annotation["term"]["id"]
        if go_id not in rows or go_id not in cfg["reviews"]:
            raise KeyError(f"Unhandled annotation {go_id} for {gene}")
        annotation["review"] = make_review(gene, cfg, rows, go_id)

    if cfg["class"] == "csu_subunit":
        data["existing_annotations"] = [
            new_annotation(
                gene,
                cfg,
                TERMS["structural_molecule"],
                "enables",
                "Predicted Csu/FanG-like surface-structure subunit should be represented as a structural molecule.",
                "The product name and Spore coat U/FanG domain support a structural role in the local Csu-like surface assembly.",
            ),
            new_annotation(
                gene,
                cfg,
                TERMS["pilus_assembly"],
                "involved_in",
                "Predicted Csu/FanG-like surface-structure subunit should be represented as pilus-assembly context.",
                "The protein is in a local chaperone-usher/Csu-like surface-adhesion cluster and has a Csu/FanG-like domain.",
            ),
        ]
    elif cfg["class"] == "chaperone":
        if TERMS["pilus_assembly"]["id"] not in {a["term"]["id"] for a in data.get("existing_annotations", [])}:
            data.setdefault("existing_annotations", []).append(
                new_annotation(
                    gene,
                    cfg,
                    TERMS["pilus_assembly"],
                    "involved_in",
                    "Predicted PapD-like chaperone should be represented as supporting pilus assembly.",
                    "The product/domain context supports a periplasmic chaperone role in chaperone-usher pilus assembly.",
                )
            )

    data["core_functions"] = core_functions(gene, cfg)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": suggested_question(gene, cfg)}]
    data["suggested_experiments"] = [
        {"description": suggested_experiment(gene, cfg), "experiment_type": "targeted surface-structure or regulation assay"}
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def curate_pila() -> None:
    gene = "pilA"
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["aliases"] = ["PP_0634"]
    ensure_reference(data, uniprot_ref(gene), "UniProtKB entry for pilA (Q88Q62)", "DE   RecName: Full=Pilin")
    ensure_reference(data, asta_ref(gene), "Asta retrieval report for pilA (Q88Q62)", "Protein Description:** RecName: Full=Pilin")
    ensure_reference(
        data,
        falcon_ref(gene),
        "Falcon research report for pilA (Q88Q62)",
        "Major structural subunit polymerized into extracellular pilus fiber",
    )
    existing_ids = {annotation["term"]["id"] for annotation in data.get("existing_annotations", [])}
    if TERMS["structural_molecule"]["id"] not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            {
                "term": TERMS["structural_molecule"],
                "evidence_type": "IEA",
                "original_reference_id": falcon_ref(gene),
                "qualifier": "enables",
                "review": {
                    "summary": "PilA should be represented as a structural molecule because it is the major type IV pilin subunit.",
                    "action": "NEW",
                    "reason": "The Falcon report and UniProt/Asta identity support PilA as the major pilin structural subunit.",
                    "supported_by": [
                        support(falcon_ref(gene), "Major structural subunit polymerized into extracellular pilus fiber"),
                        support(uniprot_ref(gene), "DE   RecName: Full=Pilin"),
                        support(asta_ref(gene), "Protein Description:** RecName: Full=Pilin"),
                    ],
                },
            }
        )
    if TERMS["type_iv_motility"]["id"] not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            {
                "term": TERMS["type_iv_motility"],
                "evidence_type": "IEA",
                "original_reference_id": falcon_ref(gene),
                "qualifier": "involved_in",
                "review": {
                    "summary": "PilA-containing type IV pili support twitching motility by family-level inference.",
                    "action": "NEW",
                    "reason": "The existing review already treats type IV pilus-dependent motility as a core inferred process; this NEW entry records that authored core term explicitly.",
                    "supported_by": [
                        support(falcon_ref(gene), "twitching motility, adhesion, DNA uptake (competence), and biofilm-related behaviors"),
                        support(falcon_ref(gene), "Primary function (best-supported):** PilA (Q88Q62 / PP_0634) is inferred to be the **major pilin subunit"),
                    ],
                },
            }
        )
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Updated {path.relative_to(ROOT)}")


def suggested_question(gene: str, cfg: dict) -> str:
    if cfg["class"] == "sensor":
        return "Does PP_2356 regulate the adjacent Csu-like surface-adhesion cluster in response to light or another envelope cue?"
    if cfg["class"] == "poly_export":
        return "Which exported polysaccharide or surface polymer uses PP_3126 in KT2440?"
    return f"What assembled surface structure and adhesion phenotype depend on {gene} in KT2440?"


def suggested_experiment(gene: str, cfg: dict) -> str:
    if cfg["class"] == "sensor":
        return "Compare Csu-cluster expression and adhesion phenotypes in PP_2356 mutant and complemented strains under light and surface-growth conditions."
    if cfg["class"] == "poly_export":
        return "Delete PP_3126 and assay surface polysaccharide composition, biofilm attachment, and outer-membrane export phenotypes."
    return f"Delete {gene} and assay surface attachment, biofilm formation, and presence of fimbrial or Csu-like fibers by microscopy."


def annoton(gene: str, label: str, function: dict | None, processes: list[dict], locations: list[dict], role: str) -> dict:
    item = {
        "id": label.lower().replace(":", "").replace(" ", "_").replace("/", "_").replace("-", "_"),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [{"preferred_term": term["label"], "term": term} for term in processes],
        "locations": [{"preferred_term": term["label"], "term": term} for term in locations],
        "role_description": role,
    }
    if function:
        item["function"] = {"preferred_term": function["label"], "term": function}
    return item


def build_module() -> None:
    module = {
        "id": "MODULE:pili_surface_adhesion_boundary",
        "title": "Pili, adhesion, and surface-structure boundary",
        "description": (
            "Boundary module for the ppu02020 pili/surface-adhesion partition in Pseudomonas putida "
            "KT2440. It captures the existing PilA type IV pilin review, a FimC/FimD-like chaperone-usher "
            "pair, a PP_2356 phytochrome-like sensor near a Csu-like chaperone-usher cluster, and a PP_3126 "
            "polysaccharide-export side node. This is surface-structure context from the broad KEGG "
            "two-component-system map rather than one canonical signaling pathway."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "KEGG:ppu02020",
                "title": "Two-component system - Pseudomonas putida KT2440",
                "statement": "KEGG ppu02020 supplies the umbrella membership for this boundary module.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.tsv",
                "title": "PSEPK ppu02020 partition table",
                "statement": (
                    "The partition table groups pilA, fimD, PP_1890, PP_2356, PP_2357-PP_2363, "
                    "and PP_3126 into the pili/surface-adhesion bucket."
                ),
            },
        ],
        "notes": (
            "Several Csu-like subunits currently have no fetched GOA rows. They are represented conservatively "
            "as structural/pilus-assembly candidates from local gene context, product names, and FanG-like domains."
        ),
        "module": {
            "id": "pili_surface_adhesion_boundary",
            "label": "Pili, adhesion, and surface-structure boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {"preferred_term": t["label"], "term": t}
                for t in [
                    TERMS["cell_adhesion"],
                    TERMS["pilus_assembly"],
                    TERMS["type_iv_motility"],
                    TERMS["polysaccharide_transport"],
                    TERMS["detection_visible_light"],
                ]
            ],
            "context": {
                "cellular_components": [
                    {"preferred_term": "pilus", "term": TERMS["pilus"]},
                    {"preferred_term": "cell outer membrane", "term": TERMS["cell_outer_membrane"]},
                    {"preferred_term": "outer membrane-bounded periplasmic space", "term": TERMS["periplasmic_space_omb"]},
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "PilA type IV pilin context",
                    "node": {
                        "id": "pila_type_iv_pilus",
                        "label": "PilA type IV pilin",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "PilA is the major type IV pilin structural subunit already curated in the project.",
                        "annotons": [
                            annoton("pilA", "pilA: type IV pilin", TERMS["structural_molecule"], [TERMS["cell_adhesion"], TERMS["type_iv_motility"]], [TERMS["type_iv_pilus"]], "Major type IV pilin structural subunit."),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "FimC/FimD-like chaperone-usher pair",
                    "node": {
                        "id": "fimd_pp1890_chaperone_usher",
                        "label": "FimD/PP_1890 chaperone-usher pair",
                        "module_type": "REGULATORY_STEP",
                        "description": "FimD and PP_1890 form a predicted chaperone-usher pilus assembly pair.",
                        "annotons": [
                            annoton("fimD", "fimD: fimbrial usher", TERMS["fimbrial_usher"], [TERMS["pilus_assembly"]], [TERMS["cell_outer_membrane"]], "Outer-membrane fimbrial usher."),
                            annoton("PP_1890", "PP_1890: pilus chaperone", None, [TERMS["pilus_assembly"]], [TERMS["periplasmic_space_omb"]], "Periplasmic pilus chaperone."),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "PP_2356 sensory regulator",
                    "node": {
                        "id": "pp2356_surface_cluster_sensor",
                        "label": "PP_2356 surface-cluster sensor",
                        "module_type": "REGULATORY_STEP",
                        "description": "PP_2356 is a phytochrome-like sensor histidine kinase adjacent to the Csu-like cluster.",
                        "annotons": [
                            annoton("PP_2356", "PP_2356: sensor kinase", TERMS["sensor_kinase"], [TERMS["detection_visible_light"], TERMS["transcription_reg"]], [TERMS["plasma_membrane"]], "Phytochrome-like sensor histidine kinase."),
                        ],
                    },
                },
                {
                    "order": 4,
                    "role": "Csu-like chaperone-usher surface-structure cluster",
                    "node": {
                        "id": "pp2357_pp2363_csu_like_cluster",
                        "label": "PP_2357-PP_2363 Csu-like cluster",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "PP_2357-PP_2363 encode Csu/FanG-like subunits plus chaperone and usher proteins.",
                        "annotons": [
                            annoton("PP_2357", "PP_2357: CsuB-like subunit", TERMS["structural_molecule"], [TERMS["pilus_assembly"]], [], "Predicted Csu-like structural subunit."),
                            annoton("PP_2358", "PP_2358: CsuA/B-like subunit", TERMS["structural_molecule"], [TERMS["pilus_assembly"]], [], "Predicted Csu-like structural subunit."),
                            annoton("PP_2359", "PP_2359: CsuA/B-like subunit", TERMS["structural_molecule"], [TERMS["pilus_assembly"]], [], "Predicted Csu-like structural subunit."),
                            annoton("PP_2360", "PP_2360: CsuA/B-like subunit", TERMS["structural_molecule"], [TERMS["pilus_assembly"]], [], "Predicted Csu-like structural subunit."),
                            annoton("PP_2361", "PP_2361: pilus chaperone", None, [TERMS["pilus_assembly"]], [TERMS["periplasmic_space_omb"]], "Predicted PapD-like chaperone."),
                            annoton("PP_2362", "PP_2362: fimbrial usher", TERMS["fimbrial_usher"], [TERMS["pilus_assembly"]], [TERMS["cell_outer_membrane"]], "Predicted outer-membrane usher."),
                            annoton("PP_2363", "PP_2363: FanG-like subunit", TERMS["structural_molecule"], [TERMS["pilus_assembly"]], [], "Predicted FanG-like surface-structure subunit."),
                        ],
                    },
                },
                {
                    "order": 5,
                    "role": "PP_3126 polysaccharide export side context",
                    "node": {
                        "id": "pp3126_polysaccharide_export",
                        "label": "PP_3126 polysaccharide export context",
                        "module_type": "TRANSPORT_STEP",
                        "description": "PP_3126 is retained as a surface-envelope export side node rather than a pilus subunit.",
                        "annotons": [
                            annoton("PP_3126", "PP_3126: polysaccharide exporter", TERMS["polysaccharide_transporter"], [TERMS["polysaccharide_transport"]], [TERMS["cell_outer_membrane"]], "BexD/CtrA/VexA-family polysaccharide export protein."),
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
    curate_pila()
    for gene in [
        "fimD",
        "PP_1890",
        "PP_2356",
        "PP_2357",
        "PP_2358",
        "PP_2359",
        "PP_2360",
        "PP_2361",
        "PP_2362",
        "PP_2363",
        "PP_3126",
    ]:
        curate_gene(gene, GENES[gene])
    build_module()


if __name__ == "__main__":
    main()
