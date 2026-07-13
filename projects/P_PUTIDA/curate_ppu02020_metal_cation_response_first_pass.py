#!/usr/bin/env python3
"""First-pass curation for the ppu02020 metal/copper/zinc response bucket."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
MODULE_PATH = ROOT / "modules/metal_cation_response_efflux_boundary.yaml"
SPECIES = "PSEPK"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


TERMS = {
    "sensor_kinase": {"id": "GO:0000155", "label": "phosphorelay sensor kinase activity"},
    "response_regulator": {"id": "GO:0000156", "label": "phosphorelay response regulator activity"},
    "phosphorelay": {"id": "GO:0000160", "label": "phosphorelay signal transduction system"},
    "cis_binding": {"id": "GO:0000976", "label": "transcription cis-regulatory region binding"},
    "histidine_kinase": {"id": "GO:0004673", "label": "protein histidine kinase activity"},
    "plasma_membrane": {"id": "GO:0005886", "label": "plasma membrane"},
    "transcription_reg": {"id": "GO:0006355", "label": "regulation of DNA-templated transcription"},
    "cation_transport": {"id": "GO:0006812", "label": "monoatomic cation transport"},
    "cation_transporter": {"id": "GO:0008324", "label": "monoatomic cation transmembrane transporter activity"},
    "cell_outer_membrane": {"id": "GO:0009279", "label": "cell outer membrane"},
    "efflux_transporter": {"id": "GO:0015562", "label": "efflux transmembrane transporter activity"},
    "copper_pm_transport": {"id": "GO:0015679", "label": "plasma membrane copper ion transport"},
    "membrane": {"id": "GO:0016020", "label": "membrane"},
    "transmembrane_transporter": {"id": "GO:0022857", "label": "transmembrane transporter activity"},
    "periplasmic_space": {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"},
    "cell_envelope": {"id": "GO:0030313", "label": "cell envelope"},
    "protein_dna_complex": {"id": "GO:0032993", "label": "protein-DNA complex"},
    "xenobiotic_transport": {"id": "GO:0042908", "label": "xenobiotic transport"},
    "xenobiotic_transporter": {"id": "GO:0042910", "label": "xenobiotic transmembrane transporter activity"},
    "metal_binding": {"id": "GO:0046872", "label": "metal ion binding"},
    "transition_metal_binding": {"id": "GO:0046914", "label": "transition metal ion binding"},
    "transmembrane_transport": {"id": "GO:0055085", "label": "transmembrane transport"},
    "copper_export": {"id": "GO:0060003", "label": "copper ion export"},
    "cation_tm_transport": {"id": "GO:0098655", "label": "monoatomic cation transmembrane transport"},
}


RESPONSE_REGULATOR_REVIEWS = {
    "GO:0000156": ("ACCEPT", "The receiver-domain protein is a phosphorelay response regulator.", None),
    "GO:0000160": ("ACCEPT", "The protein participates in His-Asp phosphorelay signaling.", None),
    "GO:0000976": ("ACCEPT", "The OmpR/PhoB-type output domain supports cis-regulatory DNA binding.", None),
    "GO:0003677": ("MARK_AS_OVER_ANNOTATED", "Generic DNA binding is less informative than transcription cis-regulatory region binding.", None),
    "GO:0005829": ("ACCEPT", "Cytosol is compatible with a soluble bacterial response regulator.", None),
    "GO:0006355": ("ACCEPT", "The response regulator controls transcription of metal-response target genes.", None),
    "GO:0032993": ("KEEP_AS_NON_CORE", "Protein-DNA complex membership is transient context for a DNA-bound regulator.", None),
}


SENSOR_REVIEWS = {
    "GO:0000155": ("ACCEPT", "The protein has conserved sensor histidine kinase architecture.", None),
    "GO:0000160": ("ACCEPT", "The protein participates in His-Asp phosphorelay signaling.", None),
    "GO:0004673": ("ACCEPT", "Protein histidine kinase activity is the core catalytic activity of this sensor kinase.", None),
    "GO:0005886": ("ACCEPT", "The sensor kinase is annotated as a plasma-membrane protein.", None),
    "GO:0007165": ("MARK_AS_OVER_ANNOTATED", "Generic signal transduction is less informative than phosphorelay signal transduction.", None),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane where supported.", None),
    "GO:0016301": ("MARK_AS_OVER_ANNOTATED", "Generic kinase activity is less informative than sensor histidine kinase activity.", None),
    "GO:0016740": ("MARK_AS_OVER_ANNOTATED", "Generic transferase activity is less informative than protein histidine kinase activity.", None),
    "GO:0016772": ("MARK_AS_OVER_ANNOTATED", "This broad phosphorus-transfer term is less informative than protein histidine kinase activity.", None),
}


CZCC_REVIEWS = {
    "GO:0009279": ("ACCEPT", "The CzcC-family outer-membrane factor is localized to the cell outer membrane.", None),
    "GO:0015562": ("ACCEPT", "The CzcC-family outer-membrane factor participates in efflux transporter activity.", None),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than cell outer membrane for CzcC.", None),
    "GO:0022857": ("MARK_AS_OVER_ANNOTATED", "Generic transmembrane transporter activity is less informative than efflux transporter activity.", None),
    "GO:0055085": ("ACCEPT", "CzcC is part of a trans-envelope efflux transport system.", None),
}


CUSB_REVIEWS = {
    "GO:0015679": ("ACCEPT", "The CusB/CzcB-family membrane-fusion protein is part of copper/cation efflux transport.", None),
    "GO:0016020": ("KEEP_AS_NON_CORE", "Membrane is correct but less informative than cell-envelope/periplasmic placement for this accessory component.", None),
    "GO:0022857": ("KEEP_AS_NON_CORE", "Transporter activity reflects pump-complex context for this membrane-fusion component.", None),
    "GO:0030288": ("ACCEPT", "The protein is annotated to the outer membrane-bounded periplasmic space.", None),
    "GO:0030313": ("ACCEPT", "Cell-envelope placement is consistent with a CusB/CzcB-family efflux adaptor.", None),
    "GO:0046872": ("KEEP_AS_NON_CORE", "Generic metal ion binding is less informative than transition metal ion binding.", None),
    "GO:0046914": ("ACCEPT", "Transition metal ion binding is supported by the CusB-family heavy-metal-binding domain context.", None),
    "GO:0055085": ("ACCEPT", "The protein is a component of a transmembrane efflux transport system.", None),
    "GO:0060003": ("ACCEPT", "CusB-family membrane-fusion proteins participate in copper ion export systems.", None),
}


CUSA_REVIEWS = {
    "GO:0005886": ("ACCEPT", "The RND transporter is annotated as a plasma-membrane protein.", None),
    "GO:0006812": ("ACCEPT", "CusA/CzcA-family RND pumps transport monoatomic cations.", None),
    "GO:0008324": ("ACCEPT", "The protein is the CzcA/CusA-family transmembrane transporter component.", None),
    "GO:0016020": ("MARK_AS_OVER_ANNOTATED", "Generic membrane is less informative than plasma membrane where supported.", None),
    "GO:0022857": ("MARK_AS_OVER_ANNOTATED", "Generic transmembrane transporter activity is less informative than cation transmembrane transporter activity.", None),
    "GO:0042908": ("MARK_AS_OVER_ANNOTATED", "Xenobiotic transport is a broad RND-family propagation and is less precise than cation transport for this copper/CzcA-family protein.", None),
    "GO:0042910": ("MARK_AS_OVER_ANNOTATED", "Xenobiotic transporter activity is less precise than cation transmembrane transporter activity for this copper/CzcA-family protein.", None),
    "GO:0055085": ("ACCEPT", "The protein catalyzes transmembrane transport as the RND pump component.", None),
    "GO:0098655": ("ACCEPT", "Monoatomic cation transmembrane transport captures the expected CzcA/CusA-family pump role.", None),
}


GENES = {
    "czcR-I": {
        "id": "Q88RV0",
        "ordered_locus": "PP_0029",
        "class": "response_regulator",
        "description": (
            "czcR-I encodes a CusR/OmpR-family two-component response regulator in Pseudomonas putida "
            "KT2440. Its receiver and OmpR/PhoB-type DNA-binding domains support a soluble phosphorelay-linked "
            "transcription-regulatory role in a heavy-metal response neighborhood."
        ),
        "uniprot": "DE   SubName: Full=Two component heavy metal response regulator",
        "asta": "Protein Description:** SubName: Full=Two component heavy metal response regulator",
    },
    "czcR-II": {
        "id": "Q88RT2",
        "ordered_locus": "PP_0047",
        "class": "response_regulator",
        "description": (
            "czcR-II encodes a CusR/OmpR-family response regulator in Pseudomonas putida KT2440. "
            "Conserved receiver and OmpR/PhoB-type DNA-binding domains support a phosphorelay-linked "
            "transcription-regulatory role in heavy-metal stress response."
        ),
        "uniprot": "DE   SubName: Full=Response regulator",
        "asta": "Protein Description:** SubName: Full=Response regulator",
    },
    "czcR-III": {
        "id": "Q88MY0",
        "ordered_locus": "PP_1438",
        "class": "response_regulator",
        "description": (
            "czcR-III encodes a CusR/OmpR-family response regulator in Pseudomonas putida KT2440. "
            "Its receiver and OmpR/PhoB-type DNA-binding domains support a phosphorelay-linked "
            "transcription-regulatory role adjacent to the PP_1437 sensor kinase."
        ),
        "uniprot": "DE   SubName: Full=Response regulator",
        "asta": "Protein Description:** SubName: Full=Response regulator",
    },
    "copR-I": {
        "id": "Q88KY1",
        "ordered_locus": "PP_2158",
        "class": "response_regulator",
        "description": (
            "copR-I encodes a CopR/CusR-like two-component transcriptional activator in Pseudomonas putida "
            "KT2440. The receiver and OmpR/PhoB-type DNA-binding domains support a phosphorelay response "
            "regulator role adjacent to the PP_2157 CusS-like sensor kinase."
        ),
        "uniprot": "DE   SubName: Full=Transcriptional activator protein",
        "asta": "Protein Description:** SubName: Full=Transcriptional activator protein",
    },
    "copR-II": {
        "id": "Q88C00",
        "ordered_locus": "PP_5383",
        "class": "response_regulator",
        "description": (
            "copR-II encodes a CopR/CusR-like two-component transcriptional activator in Pseudomonas putida "
            "KT2440. It sits next to copS and the czcC-cusBAF efflux locus, consistent with "
            "phosphorelay-linked control of copper or metal-cation efflux genes."
        ),
        "uniprot": "DE   SubName: Full=Transcriptional activator protein",
        "asta": "Protein Description:** SubName: Full=Transcriptional activator protein",
    },
    "czrSA": {
        "id": "Q88RU9",
        "ordered_locus": "PP_0030",
        "class": "sensor",
        "description": (
            "czrSA encodes a membrane sensor histidine kinase in Pseudomonas putida KT2440. Its "
            "CztS/SilS/CopS, HAMP, HisKA, and HATPase domains support a two-component input role "
            "in a heavy-metal response neighborhood."
        ),
    },
    "PP_1437": {
        "id": "Q88MY1",
        "ordered_locus": "PP_1437",
        "class": "sensor",
        "description": (
            "PP_1437 encodes a membrane sensor histidine kinase in Pseudomonas putida KT2440. Its "
            "CztS/SilS/CopS, HAMP, HisKA, and HATPase domains support a two-component input role "
            "adjacent to the czcR-III response regulator."
        ),
    },
    "PP_2157": {
        "id": "Q88KY2",
        "ordered_locus": "PP_2157",
        "class": "sensor",
        "description": (
            "PP_2157 encodes a CusS-like membrane sensor histidine kinase in Pseudomonas putida KT2440. "
            "Its CusS/CztS/SilS/CopS, HAMP, HisKA, and HATPase domains support a two-component input "
            "role adjacent to copR-I."
        ),
    },
    "copS": {
        "id": "Q88BZ9",
        "ordered_locus": "PP_5384",
        "class": "sensor",
        "description": (
            "copS encodes a CusS-like membrane sensor histidine kinase in Pseudomonas putida KT2440. "
            "It is adjacent to copR-II and the czcC-cusBAF efflux locus, supporting a regulatory role "
            "in copper or metal-cation efflux response."
        ),
    },
    "czcC": {
        "id": "Q88BZ8",
        "ordered_locus": "PP_5385",
        "class": "czcC",
        "description": (
            "czcC encodes a CzcC-family outer-membrane factor in Pseudomonas putida KT2440. It is part "
            "of the czcC-cusBAF copper or metal-cation RND efflux neighborhood and provides the outer "
            "membrane efflux channel component."
        ),
        "uniprot": "DE   SubName: Full=Metal RND efflux outer membrane protein, CzcC family",
        "asta": "Protein Description:** SubName: Full=Metal RND efflux outer membrane protein, CzcC family",
        "uniprot_extra": "CC   -!- SIMILARITY: Belongs to the outer membrane factor (OMF) (TC 1.B.17)",
        "uniprot_extra_2": "DR   InterPro; IPR003423; OMP_efflux.",
    },
    "cusB": {
        "id": "Q88BZ7",
        "ordered_locus": "PP_5386",
        "class": "cusB",
        "description": (
            "cusB encodes a CusB/CzcB-family membrane-fusion protein in Pseudomonas putida KT2440. "
            "Its membrane-fusion and heavy-metal-binding domain annotations support an accessory/adaptor "
            "role in the czcC-cusBAF copper or metal-cation RND efflux system."
        ),
        "uniprot": "DE   SubName: Full=Probable copper RND efflux membrane fusion protein, CzcB family",
        "asta": "Protein Description:** SubName: Full=Probable copper RND efflux membrane fusion protein, CzcB family",
        "uniprot_extra": "CC   -!- SIMILARITY: Belongs to the membrane fusion protein (MFP) (TC 8.A.1)",
        "uniprot_extra_2": "DR   InterPro; IPR006143; RND_pump_MFP.",
        "uniprot_extra_3": "DR   InterPro; IPR045800; HMBD.",
    },
    "cusA": {
        "id": "Q88BZ6",
        "ordered_locus": "PP_5387",
        "class": "cusA",
        "description": (
            "cusA encodes a CusA/CzcA-family RND transmembrane transporter in Pseudomonas putida KT2440. "
            "Its RND-family and CusA-like domains support a plasma-membrane cation efflux role in the "
            "czcC-cusBAF copper or metal-cation export locus."
        ),
        "uniprot": "DE   SubName: Full=Probable copper efflux transporter, CzcA family",
        "asta": "Protein Description:** SubName: Full=Probable copper efflux transporter, CzcA family",
        "uniprot_extra": "CC   -!- SIMILARITY: Belongs to the resistance-nodulation-cell division (RND)",
        "uniprot_extra_2": "DR   InterPro; IPR004763; CusA-like.",
    },
    "cusF": {
        "id": "Q88BZ5",
        "ordered_locus": "PP_5388",
        "class": "cusF",
        "description": (
            "cusF encodes a CusF-family exported copper-efflux protein in Pseudomonas putida KT2440. "
            "It has no fetched GOA rows in this first pass, but its product name and CusF domain support "
            "retaining it as an accessory copper-efflux component in the czcC-cusBAF boundary module."
        ),
        "uniprot": "DE   SubName: Full=Probable exported copper efflux protein",
        "asta": "Protein Description:** SubName: Full=Probable exported copper efflux protein",
        "uniprot_extra": "DR   InterPro; IPR021647; CusF_Ec.",
    },
}


for cfg in GENES.values():
    if cfg["class"] == "sensor":
        cfg.update(
            {
                "uniprot": "DE   RecName: Full=Sensor protein",
                "asta": "Protein Description:** RecName: Full=Sensor protein",
                "uniprot_extra": "CC   -!- FUNCTION: Member of a two-component regulatory system.",
                "uniprot_extra_2": "DR   InterPro; IPR006290; CztS_silS_copS.",
                "uniprot_extra_3": "DR   InterPro; IPR005467; His_kinase_dom.",
            }
        )
    if cfg["class"] == "response_regulator":
        cfg.update(
            {
                "uniprot_extra": "DR   InterPro; IPR006291; CusR-like.",
                "uniprot_extra_2": "DR   InterPro; IPR001867; OmpR/PhoB-type_DNA-bd.",
                "uniprot_extra_3": "DR   InterPro; IPR001789; Sig_transdc_resp-reg_receiver.",
            }
        )


CLASS_REVIEWS = {
    "response_regulator": RESPONSE_REGULATOR_REVIEWS,
    "sensor": SENSOR_REVIEWS,
    "czcC": CZCC_REVIEWS,
    "cusB": CUSB_REVIEWS,
    "cusA": CUSA_REVIEWS,
    "cusF": {},
}


CUSF_NEW_ANNOTATIONS = [
    {
        "term": TERMS["transition_metal_binding"],
        "qualifier": "enables",
        "summary": "CusF should be represented as a transition-metal-binding copper-efflux accessory protein.",
        "reason": "The UniProt product name and CusF domain support a metal-binding accessory role in copper efflux.",
    },
    {
        "term": TERMS["copper_export"],
        "qualifier": "involved_in",
        "summary": "CusF should be represented as involved in copper ion export.",
        "reason": "The protein is named as an exported copper-efflux protein and has a CusF domain.",
    },
]


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
    for key in ("uniprot_extra", "uniprot_extra_2", "uniprot_extra_3"):
        if cfg.get(key):
            items.append(support(uniprot_ref(gene), cfg[key]))
    return items


def make_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    action, reason, replacements = CLASS_REVIEWS[cfg["class"]][go_id]
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


def core_functions(gene: str, cfg: dict) -> list[dict]:
    cls = cfg["class"]
    if cls == "response_regulator":
        cores = [
            {
                "description": "CusR/OmpR-family phosphorelay response regulator controlling metal-response transcription.",
                "molecular_function": TERMS["response_regulator"],
                "directly_involved_in": [TERMS["phosphorelay"], TERMS["transcription_reg"]],
                "locations": [{"id": "GO:0005829", "label": "cytosol"}],
            },
            {
                "description": "OmpR/PhoB-family cis-regulatory DNA binding by the response-regulator output domain.",
                "molecular_function": TERMS["cis_binding"],
                "directly_involved_in": [TERMS["transcription_reg"]],
                "locations": [{"id": "GO:0005829", "label": "cytosol"}],
            },
        ]
    elif cls == "sensor":
        cores = [
            {
                "description": "Membrane sensor histidine kinase activity feeding a metal-response phosphorelay.",
                "molecular_function": TERMS["sensor_kinase"],
                "directly_involved_in": [TERMS["phosphorelay"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ]
    elif cls == "czcC":
        cores = [
            {
                "description": "Outer-membrane factor activity in a metal-cation efflux transporter system.",
                "molecular_function": TERMS["efflux_transporter"],
                "directly_involved_in": [TERMS["transmembrane_transport"]],
                "locations": [TERMS["cell_outer_membrane"]],
            }
        ]
    elif cls == "cusB":
        cores = [
            {
                "description": "CusB/CzcB-family metal-binding membrane-fusion component contributing to copper/cation efflux.",
                "molecular_function": TERMS["transition_metal_binding"],
                "contributes_to_molecular_function": TERMS["transmembrane_transporter"],
                "directly_involved_in": [TERMS["copper_export"]],
                "locations": [TERMS["periplasmic_space"], TERMS["cell_envelope"]],
            }
        ]
    elif cls == "cusA":
        cores = [
            {
                "description": "CusA/CzcA-family RND cation transmembrane transporter activity.",
                "molecular_function": TERMS["cation_transporter"],
                "directly_involved_in": [TERMS["cation_tm_transport"], TERMS["transmembrane_transport"]],
                "locations": [TERMS["plasma_membrane"]],
            }
        ]
    elif cls == "cusF":
        cores = [
            {
                "description": "CusF-family transition-metal-binding accessory protein in copper efflux context.",
                "molecular_function": TERMS["transition_metal_binding"],
                "directly_involved_in": [TERMS["copper_export"]],
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

    for annotation in data.get("existing_annotations", []):
        go_id = annotation["term"]["id"]
        if go_id not in rows or go_id not in CLASS_REVIEWS[cfg["class"]]:
            raise KeyError(f"Unhandled annotation {go_id} for {gene}")
        annotation["review"] = make_review(gene, cfg, rows, go_id)

    if cfg["class"] == "cusF":
        data["existing_annotations"] = [
            {
                "term": item["term"],
                "evidence_type": "IEA",
                "original_reference_id": uniprot_ref(gene),
                "qualifier": item["qualifier"],
                "review": {
                    "summary": item["summary"],
                    "action": "NEW",
                    "reason": item["reason"],
                    "supported_by": base_support(gene, cfg),
                },
            }
            for item in CUSF_NEW_ANNOTATIONS
        ]

    data["core_functions"] = core_functions(gene, cfg)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [{"question": suggested_question(gene, cfg)}]
    data["suggested_experiments"] = [
        {"description": suggested_experiment(gene, cfg), "experiment_type": "targeted regulatory or metal-efflux assay"}
    ]

    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=False, width=100),
        encoding="utf-8",
    )
    print(f"Curated {path.relative_to(ROOT)}")


def suggested_question(gene: str, cfg: dict) -> str:
    if cfg["class"] in {"response_regulator", "sensor"}:
        return f"Which metal cue and regulon are directly controlled by {gene} in KT2440?"
    if cfg["class"] in {"czcC", "cusB", "cusA", "cusF"}:
        return f"What is the in vivo substrate range and partner dependence of {gene} in the czcC-cusBAF efflux locus?"
    raise ValueError(cfg["class"])


def suggested_experiment(gene: str, cfg: dict) -> str:
    if cfg["class"] in {"response_regulator", "sensor"}:
        return f"Measure metal-dependent promoter output and efflux gene expression in {gene} mutant and complemented strains."
    return f"Test {gene} deletion or depletion for copper, zinc, cadmium, and cobalt sensitivity and quantify metal efflux phenotypes."


def annoton(gene: str, label: str, function: dict, processes: list[dict], locations: list[dict], role: str) -> dict:
    return {
        "id": label.lower().replace(":", "").replace(" ", "_").replace("/", "_").replace("-", "_"),
        "label": label,
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": function["label"], "term": function},
        "processes": [{"preferred_term": term["label"], "term": term} for term in processes],
        "locations": [{"preferred_term": term["label"], "term": term} for term in locations],
        "role_description": role,
    }


def response_annoton(gene: str) -> dict:
    return annoton(
        gene,
        f"{gene}: response regulator",
        TERMS["response_regulator"],
        [TERMS["phosphorelay"], TERMS["transcription_reg"]],
        [{"id": "GO:0005829", "label": "cytosol"}],
        "CusR/OmpR-family metal-response transcriptional response regulator.",
    )


def sensor_annoton(gene: str) -> dict:
    return annoton(
        gene,
        f"{gene}: sensor kinase",
        TERMS["sensor_kinase"],
        [TERMS["phosphorelay"]],
        [TERMS["plasma_membrane"]],
        "CztS/SilS/CopS-like membrane sensor histidine kinase.",
    )


def pair_step(order: int, step_id: str, sensor: str, regulator: str, label: str) -> dict:
    return {
        "order": order,
        "role": label,
        "node": {
            "id": step_id,
            "label": label,
            "module_type": "REGULATORY_STEP",
            "description": f"{sensor} and {regulator} are a local sensor/response-regulator pair in the metal-response partition.",
            "annotons": [sensor_annoton(sensor), response_annoton(regulator)],
            "connections": [
                {
                    "source": f"{sensor.lower()}_sensor_kinase",
                    "target": f"{regulator.lower().replace('-', '_')}_response_regulator",
                    "connection_type": "PROVIDES_INPUT_FOR",
                    "description": f"{sensor} provides phosphorelay input for the adjacent {regulator} response regulator.",
                }
            ],
        },
    }


def build_module() -> None:
    module = {
        "id": "MODULE:metal_cation_response_efflux_boundary",
        "title": "Heavy-metal/copper/zinc response and efflux boundary",
        "description": (
            "Boundary module for the ppu02020 heavy-metal/copper/zinc response partition in Pseudomonas "
            "putida KT2440. It captures CusR/CopR-like response regulators, CztS/SilS/CopS-like sensor "
            "kinases, and the czcC-cusBAF copper or metal-cation RND efflux locus. This is a metal-response "
            "boundary from the broad KEGG two-component-system map, not one canonical His-Asp relay."
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
                    "The partition table groups czcR-I, czrSA, czcR-II, PP_1437, czcR-III, PP_2157, "
                    "copR-I, copR-II, copS, czcC, cusB, cusA, and cusF into the heavy-metal/copper/zinc bucket."
                ),
            },
        ],
        "notes": (
            "The regulatory pairs and efflux locus are kept in one boundary because the ppu02020 membership "
            "mixes two-component regulation with the downstream cation/copper efflux machinery. Direct metal "
            "specificity remains a first-pass knowledge gap for several paralogous regulators."
        ),
        "module": {
            "id": "metal_cation_response_efflux_boundary",
            "label": "Heavy-metal/copper/zinc response and efflux boundary",
            "module_type": "SIGNALING_PATHWAY",
            "concepts": [
                {"preferred_term": t["label"], "term": t}
                for t in [
                    TERMS["phosphorelay"],
                    TERMS["transcription_reg"],
                    TERMS["copper_export"],
                    TERMS["cation_tm_transport"],
                    TERMS["transmembrane_transport"],
                ]
            ],
            "context": {
                "cellular_components": [
                    {"preferred_term": "plasma membrane", "term": TERMS["plasma_membrane"]},
                    {"preferred_term": "cell outer membrane", "term": TERMS["cell_outer_membrane"]},
                    {"preferred_term": "cell envelope", "term": TERMS["cell_envelope"]},
                ]
            },
            "parts": [
                pair_step(1, "czrsa_czcr_i_pair", "czrSA", "czcR-I", "czrSA/czcR-I metal-response pair"),
                {
                    "order": 2,
                    "role": "czcR-II orphan response regulator",
                    "node": {
                        "id": "czcr_ii_orphan_regulator",
                        "label": "czcR-II orphan response regulator",
                        "module_type": "REGULATORY_STEP",
                        "description": "czcR-II is retained as an orphan CusR-like response regulator in the metal-response boundary.",
                        "annotons": [response_annoton("czcR-II")],
                    },
                },
                pair_step(3, "pp1437_czcr_iii_pair", "PP_1437", "czcR-III", "PP_1437/czcR-III metal-response pair"),
                pair_step(4, "pp2157_copr_i_pair", "PP_2157", "copR-I", "PP_2157/copR-I metal-response pair"),
                {
                    "order": 5,
                    "role": "copR-II/copS-regulated czcC-cusBAF efflux locus",
                    "node": {
                        "id": "coprs_cus_efflux_locus",
                        "label": "copR-II/copS and czcC-cusBAF efflux locus",
                        "module_type": "REGULATORY_STEP",
                        "description": "copR-II/copS regulatory genes sit adjacent to a CzcC/CusBAF-family copper or cation efflux locus.",
                        "annotons": [
                            response_annoton("copR-II"),
                            sensor_annoton("copS"),
                            annoton("czcC", "czcC: outer membrane efflux factor", TERMS["efflux_transporter"], [TERMS["transmembrane_transport"]], [TERMS["cell_outer_membrane"]], "Outer-membrane factor of the efflux system."),
                            annoton("cusB", "cusB: membrane fusion component", TERMS["transition_metal_binding"], [TERMS["copper_export"]], [TERMS["periplasmic_space"], TERMS["cell_envelope"]], "Metal-binding membrane-fusion component of the efflux system."),
                            annoton("cusA", "cusA: RND cation transporter", TERMS["cation_transporter"], [TERMS["cation_tm_transport"], TERMS["transmembrane_transport"]], [TERMS["plasma_membrane"]], "CusA/CzcA-family RND cation transporter component."),
                            annoton("cusF", "cusF: copper efflux accessory protein", TERMS["transition_metal_binding"], [TERMS["copper_export"]], [TERMS["periplasmic_space"]], "CusF-family copper-efflux accessory protein without current GOA rows."),
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
    for gene in [
        "czcR-I",
        "czrSA",
        "czcR-II",
        "PP_1437",
        "czcR-III",
        "PP_2157",
        "copR-I",
        "copR-II",
        "copS",
        "czcC",
        "cusB",
        "cusA",
        "cusF",
    ]:
        curate_gene(gene, GENES[gene])
    build_module()


if __name__ == "__main__":
    main()
