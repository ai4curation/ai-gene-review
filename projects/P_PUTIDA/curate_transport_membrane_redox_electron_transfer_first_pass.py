#!/usr/bin/env python3
"""First-pass curation for membrane redox and electron-transfer spillover genes."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = (
    ROOT
    / "projects/P_PUTIDA/batches/"
    "module_transport_membrane_efflux_ion_metal_membrane_redox_electron_transfer_spillovers.tsv"
)
MODULE_PATH = ROOT / "modules/membrane_redox_electron_transfer_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0004174": "electron-transferring-flavoprotein dehydrogenase activity",
    "GO:0005344": "oxygen carrier activity",
    "GO:0005381": "iron ion transmembrane transporter activity",
    "GO:0005506": "iron ion binding",
    "GO:0005507": "copper ion binding",
    "GO:0005737": "cytoplasm",
    "GO:0005886": "plasma membrane",
    "GO:0008941": "nitric oxide dioxygenase NAD(P)H activity",
    "GO:0009055": "electron transfer activity",
    "GO:0010181": "FMN binding",
    "GO:0015093": "ferrous iron transmembrane transporter activity",
    "GO:0015671": "oxygen transport",
    "GO:0016020": "membrane",
    "GO:0016491": "oxidoreductase activity",
    "GO:0016679": "oxidoreductase activity, acting on diphenols and related substances as donors",
    "GO:0016829": "lyase activity",
    "GO:0017003": "protein-heme linkage",
    "GO:0017004": "cytochrome complex assembly",
    "GO:0019825": "oxygen binding",
    "GO:0020037": "heme binding",
    "GO:0022900": "electron transport chain",
    "GO:0022904": "respiratory electron transport chain",
    "GO:0030091": "protein repair",
    "GO:0030288": "outer membrane-bounded periplasmic space",
    "GO:0033573": "high-affinity iron permease complex",
    "GO:0034755": "iron ion transmembrane transport",
    "GO:0042597": "periplasmic space",
    "GO:0045454": "cell redox homeostasis",
    "GO:0046210": "nitric oxide catabolic process",
    "GO:0046872": "metal ion binding",
    "GO:0051409": "response to nitrosative stress",
    "GO:0051536": "iron-sulfur cluster binding",
    "GO:0051537": "2 iron, 2 sulfur cluster binding",
    "GO:0051538": "3 iron, 4 sulfur cluster binding",
    "GO:0051539": "4 iron, 4 sulfur cluster binding",
    "GO:0071500": "cellular response to nitrosative stress",
    "GO:0071949": "FAD binding",
}

PROFILE = {
    "PP_0111": {
        "class": "sco_senc",
        "group": "SCO/SenC copper-redox assembly proteins",
        "primary": None,
        "processes": ["GO:0045454"],
        "locations": [],
        "description": "PP_0111 encodes a SCO1/SenC-family copper/redox protein associated with cytochrome oxidase or copper-center assembly; first-pass curation keeps the supported role at cell redox homeostasis level.",
    },
    "PP_0125": {
        "class": "cytochrome_c",
        "group": "c-type cytochrome electron carriers",
        "primary": "GO:0009055",
        "processes": [],
        "locations": [],
        "description": "PP_0125 encodes a c-type cytochrome-family electron-transfer protein with heme/iron-binding context.",
    },
    "cc": {
        "class": "cytochrome_c",
        "group": "c-type cytochrome electron carriers",
        "primary": "GO:0009055",
        "processes": [],
        "locations": ["GO:0042597"],
        "description": "cc encodes cytochrome c4, a periplasmic diheme c-type cytochrome electron-transfer protein.",
    },
    "PP_0180": {
        "class": "iron_transporter",
        "group": "OFeT/FTR1-like iron transporter redox nodes",
        "primary": "GO:0015093",
        "processes": ["GO:0034755"],
        "locations": ["GO:0005886"],
        "description": "PP_0180 encodes a cytochrome-c/FTR1-family membrane protein curated as an oxidase-dependent ferrous-iron transporter, with heme/electron-transfer context.",
    },
    "hmp": {
        "class": "flavohemoglobin",
        "group": "Nitrosative-stress redox detoxification",
        "primary": "GO:0008941",
        "processes": ["GO:0046210", "GO:0071500"],
        "locations": [],
        "description": "hmp encodes flavohemoprotein, a nitric oxide dioxygenase that uses O2 and NAD(P)H to detoxify nitric oxide to nitrate during nitrosative stress.",
    },
    "cumA": {
        "class": "multicopper_oxidase",
        "group": "Copper redox enzymes",
        "primary": "GO:0016491",
        "processes": [],
        "locations": ["GO:0030288"],
        "description": "cumA encodes a membrane-associated multicopper oxidase, curated as a copper-dependent oxidoreductase side node.",
    },
    "PP_1083": {
        "class": "ferredoxin",
        "group": "Ferredoxin and iron-sulfur electron-transfer proteins",
        "primary": "GO:0009055",
        "processes": [],
        "locations": [],
        "description": "PP_1083 encodes a bacterioferritin-associated 2Fe-2S ferredoxin, curated as an electron-transfer protein.",
    },
    "fdxA": {
        "class": "ferredoxin",
        "group": "Ferredoxin and iron-sulfur electron-transfer proteins",
        "primary": "GO:0009055",
        "processes": [],
        "locations": [],
        "description": "fdxA encodes ferredoxin 1, an iron-sulfur protein that transfers electrons using 3Fe-4S and 4Fe-4S clusters.",
    },
    "PP_1841": {
        "class": "cytochrome_c",
        "group": "c-type cytochrome electron carriers",
        "primary": "GO:0009055",
        "processes": [],
        "locations": [],
        "description": "PP_1841 encodes a c-type cytochrome/cytochrome c553-like electron-transfer protein.",
    },
    "PP_2010": {
        "class": "cytochrome_b561",
        "group": "Membrane cytochrome b561 electron-transfer proteins",
        "primary": "GO:0009055",
        "processes": ["GO:0022904"],
        "locations": ["GO:0005886"],
        "description": "PP_2010 encodes a membrane cytochrome b561-family heme protein with respiratory electron-transfer context.",
    },
    "PP_2675": {
        "class": "cytochrome_c",
        "group": "c-type cytochrome electron carriers",
        "primary": "GO:0009055",
        "processes": [],
        "locations": [],
        "description": "PP_2675 encodes a c-type cytochrome/cytochrome c550-c551-like electron-transfer protein.",
    },
    "PP_2886": {
        "class": "cytochrome_b561",
        "group": "Membrane cytochrome b561 electron-transfer proteins",
        "primary": "GO:0009055",
        "processes": ["GO:0022904"],
        "locations": ["GO:0005886"],
        "description": "PP_2886 encodes a membrane cytochrome b561-family heme protein with respiratory electron-transfer context.",
    },
    "PP_3332": {
        "class": "cytochrome_c",
        "group": "c-type cytochrome electron carriers",
        "primary": "GO:0009055",
        "processes": [],
        "locations": [],
        "description": "PP_3332 encodes a c-type cytochrome-family electron-transfer protein with heme/iron-binding context.",
    },
    "PP_3543": {
        "class": "membrane_fes",
        "group": "Membrane FixG/NapH-like iron-sulfur redox proteins",
        "primary": "GO:0009055",
        "processes": [],
        "locations": ["GO:0005886"],
        "description": "PP_3543 encodes a membrane FixG/NapH-like iron-sulfur redox protein with 4Fe-4S and transmembrane features.",
    },
    "PP_4203": {
        "class": "etf_qo",
        "group": "ETF-ubiquinone oxidoreductase",
        "primary": "GO:0004174",
        "processes": ["GO:0022900"],
        "locations": [],
        "description": "PP_4203 encodes electron transfer flavoprotein-ubiquinone oxidoreductase, which accepts electrons from ETF and reduces ubiquinone.",
    },
    "PP_4259": {
        "class": "membrane_fes",
        "group": "Membrane FixG/NapH-like iron-sulfur redox proteins",
        "primary": "GO:0009055",
        "processes": [],
        "locations": ["GO:0005886"],
        "description": "PP_4259 encodes a membrane FixG/NapH-like iron-sulfur redox protein with 4Fe-4S and transmembrane features.",
    },
    "PP_4289": {
        "class": "membrane_cytochrome_c",
        "group": "Membrane c-type cytochrome redox proteins",
        "primary": "GO:0009055",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_4289 encodes a multi-pass membrane protein with a c-type cytochrome domain and heme/electron-transfer context.",
    },
    "ccmE": {
        "class": "ccm",
        "group": "Cytochrome c maturation proteins",
        "primary": None,
        "processes": ["GO:0017004", "GO:0017003"],
        "locations": ["GO:0005886"],
        "description": "ccmE encodes the CcmE heme chaperone required for c-type cytochrome biogenesis, transient heme binding, and transfer to apo-cytochromes.",
    },
    "msrQ": {
        "class": "msrq",
        "group": "Methionine-sulfoxide repair redox proteins",
        "primary": "GO:0009055",
        "processes": ["GO:0030091"],
        "locations": ["GO:0005886"],
        "description": "msrQ encodes the membrane flavocytochrome subunit of the MsrPQ system, transferring electrons for periplasmic methionine-sulfoxide protein repair.",
    },
    "PP_4870": {
        "class": "azurin",
        "group": "Blue-copper electron carriers",
        "primary": "GO:0009055",
        "processes": [],
        "locations": ["GO:0042597"],
        "description": "PP_4870 encodes azurin, a periplasmic blue-copper electron-transfer protein.",
    },
    "PP_4970": {
        "class": "cytochrome_c",
        "group": "c-type cytochrome electron carriers",
        "primary": "GO:0009055",
        "processes": ["GO:0022900"],
        "locations": ["GO:0042597"],
        "description": "PP_4970 encodes a cytochrome c-family electron-transfer protein with periplasmic/electron-transport-chain context.",
    },
    "yceJ": {
        "class": "cytochrome_b561",
        "group": "Membrane cytochrome b561 electron-transfer proteins",
        "primary": "GO:0009055",
        "processes": ["GO:0022904"],
        "locations": ["GO:0005886"],
        "description": "yceJ encodes an iron-regulated membrane cytochrome b561-family heme protein with respiratory electron-transfer context.",
    },
    "yfhL": {
        "class": "ferredoxin",
        "group": "Ferredoxin and iron-sulfur electron-transfer proteins",
        "primary": "GO:0009055",
        "processes": [],
        "locations": ["GO:0005737"],
        "description": "yfhL encodes a 4Fe-4S cluster-containing ferredoxin-like protein, curated as a cytoplasmic iron-sulfur electron-transfer candidate.",
    },
    "PP_5267": {
        "class": "cytochrome_c",
        "group": "c-type cytochrome electron carriers",
        "primary": "GO:0009055",
        "processes": [],
        "locations": [],
        "description": "PP_5267 encodes cytochrome c5, a c-type cytochrome-family electron-transfer protein.",
    },
    "ccmH": {
        "class": "ccm",
        "group": "Cytochrome c maturation proteins",
        "primary": None,
        "processes": ["GO:0017004"],
        "locations": ["GO:0005886"],
        "description": "ccmH encodes a membrane cytochrome c-type biogenesis protein, likely part of the Ccm heme-lyase/maturation machinery.",
    },
}

DOMAIN_NEEDLES = {
    "PP_0111": ["Electron transport protein SCO1/SenC", "SCO1-SenC", "KW   Copper"],
    "PP_0125": ["Cytochrome c-type protein", "Cytochrome_CBB3", "KW   Electron transport"],
    "cc": ["Cytochrome c4", "Diheme, high potential cytochrome c", "Cytochrom_C"],
    "PP_0180": ["Cytochrome c family protein", "PLASMA MEMBRANE IRON PERMEASE", "FTR1/Fip1/EfeU"],
    "hmp": ["Flavohemoprotein", "EC=1.14.12.17", "nitric oxide dioxygenase"],
    "cumA": ["Multicopper oxidase", "Cu-oxidase_2", "Cu-oxidase_3"],
    "PP_1083": ["Bacterioferritin-associated ferredoxin", "Fer2_BFD", "KW   2Fe-2S"],
    "fdxA": ["Ferredoxin 1", "Ferredoxins are iron-sulfur proteins", "Fer4"],
    "PP_1841": ["Cytochrome c family protein", "Cytochrome_c550/c551-like", "Cytochrom_C"],
    "PP_2010": ["Cytochrome b561", "Cytochrome_b561_oxidase", "Ni_hydr_CYTB"],
    "PP_2675": ["Cytochrome c-type protein", "c550_proteobact", "Cytochrome_CBB3"],
    "PP_2886": ["Cytochrome b561", "Cytochrome_b561_oxidase", "Ni_hydr_CYTB"],
    "PP_3332": ["Cytochrome c-type protein", "Cytochrome_CBB3", "KW   Electron transport"],
    "PP_3543": ["Iron-sulfur cluster-binding protein", "Cyt_c_oxidase_cbb3_FixG", "FixG_C"],
    "PP_4203": ["Electron transfer flavoprotein-ubiquinone oxidoreductase", "Accepts electrons from ETF", "ETF-QO"],
    "PP_4259": ["Iron-sulfur cluster-binding protein", "Cyt_c_oxidase_cbb3_FixG", "FixG_C"],
    "PP_4289": ["Cytochrome c domain-containing protein", "Urate_ox_N", "FT   TRANSMEM"],
    "ccmE": ["Cytochrome c-type biogenesis protein CcmE", "Heme chaperone required", "CcmE"],
    "msrQ": ["Protein-methionine-sulfoxide reductase heme-binding subunit MsrQ", "Part of the MsrPQ system", "Ferric_reduct"],
    "PP_4870": ["Azurin", "Transfers electrons from cytochrome c551", "BlueCu_1"],
    "PP_4970": ["Cytochrome c", "Cytochrom_C_2", "KW   Electron transport"],
    "yceJ": ["Cytochrome b561, iron-regulated", "Cytochrome_b561_oxidase", "Ni_hydr_CYTB"],
    "yfhL": ["4Fe-4S cluster-containing protein", "YfhL-like", "Fer4_7"],
    "PP_5267": ["Cytochrome c5", "Cytochrome_CBB3", "KW   Electron transport"],
    "ccmH": ["Cytochrome c-type biogenesis protein", "Possible subunit of a heme lyase", "CcmH"],
}


class GeneInfo(dict[str, Any]):
    gene: str


def term(go_id: str) -> dict[str, str]:
    return {"id": go_id, "label": TERMS[go_id]}


def descriptor(go_id: str, description: str | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {"preferred_term": TERMS[go_id], "term": term(go_id)}
    if description:
        item["description"] = description
    return item


def ref_file(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def dedupe(items: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    out: list[dict[str, str]] = []
    for item in items:
        key = (item["reference_id"], item["supporting_text"])
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def first_line(lines: list[str], needle: str, optional: bool = False) -> str | None:
    for line in lines:
        if needle in line:
            return line
    if optional:
        return None
    raise ValueError(f"Could not find {needle!r}")


def first_de_line(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("DE   RecName") or line.startswith("DE   SubName"):
            return line
    for line in lines:
        if line.startswith("DE   "):
            return line
    raise ValueError("No UniProt DE line found")


def load_rows() -> list[dict[str, str]]:
    with BATCH_PATH.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_info(row: dict[str, str]) -> GeneInfo:
    gene = row["gene"]
    uniprot_lines = (GENE_ROOT / gene / f"{gene}-uniprot.txt").read_text(encoding="utf-8").splitlines()
    asta_lines = (GENE_ROOT / gene / f"{gene}-deep-research-asta.md").read_text(encoding="utf-8").splitlines()
    review_doc = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text(encoding="utf-8"))
    info = GeneInfo(
        gene=gene,
        accession=row["uniprot_accession"],
        product=row["protein_name"],
        profile=PROFILE[gene],
        uniprot_lines=uniprot_lines,
        asta_lines=asta_lines,
        existing_refs={ref["id"]: ref for ref in review_doc.get("references", []) if "id" in ref},
    )
    info["de"] = first_de_line(uniprot_lines)
    info["asta_product"] = first_line(asta_lines, "- **Protein Description:**")
    info["asta_domains"] = first_line(asta_lines, "- **Key Domains:**")
    info["location"] = first_line(uniprot_lines, "SUBCELLULAR LOCATION", optional=True)
    return info


def base_support(info: GeneInfo) -> list[dict[str, str]]:
    gene = info["gene"]
    out = [
        support(ref_file(gene, "uniprot.txt"), info["de"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_product"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_domains"]),
    ]
    if info.get("location"):
        out.append(support(ref_file(gene, "uniprot.txt"), info["location"]))
    for needle in DOMAIN_NEEDLES[gene]:
        line = first_line(info["uniprot_lines"], needle, optional=True)
        if line:
            out.append(support(ref_file(gene, "uniprot.txt"), line))
    return dedupe(out)


def goa_support(info: GeneInfo, go_id: str, label: str) -> dict[str, str]:
    return support(ref_file(info["gene"], "goa.tsv"), f"{go_id}\t{label}")


def review(
    info: GeneInfo,
    summary: str,
    action: str,
    reason: str,
    replacement_ids: list[str] | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": base_support(info),
    }
    if replacement_ids:
        item["proposed_replacement_terms"] = [term(go_id) for go_id in replacement_ids]
    return item


def existing_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]
    cls = info["profile"]["class"]
    primary = info["profile"].get("primary")

    if go_id == "GO:0005886":
        return review(info, "Plasma membrane localization is appropriate for this bacterial membrane redox or assembly protein.", "ACCEPT", "UniProt/GOA membrane and transmembrane evidence supports plasma/inner membrane localization.")
    if go_id == "GO:0016020":
        if "GO:0005886" in info["go_ids"]:
            return review(info, "Generic membrane localization is true but less informative than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "A more specific plasma-membrane annotation is present.")
        return review(info, "Membrane localization is appropriate for this transmembrane redox protein.", "ACCEPT", "UniProt membrane/transmembrane evidence supports membrane localization.")
    if go_id in {"GO:0042597", "GO:0030288", "GO:0005737"}:
        return review(info, f"{label} localization is appropriate for this protein.", "ACCEPT", "The UniProt/GOA localization context supports this cellular location.")
    if go_id in {"GO:0005506", "GO:0005507", "GO:0020037", "GO:0046872", "GO:0010181", "GO:0071949", "GO:0051536", "GO:0051537", "GO:0051538", "GO:0051539"}:
        return review(info, f"{label} is retained as cofactor or metal-binding context rather than the core activity.", "KEEP_AS_NON_CORE", "The core role is electron transfer, oxidoreductase activity, iron transport, or cytochrome biogenesis; metal/cofactor binding supports but does not by itself define that role.")
    if go_id == "GO:0009055":
        if cls == "iron_transporter":
            return review(info, "Electron transfer activity is relevant to the cytochrome/FTR1 architecture but secondary to the iron-transport assignment.", "KEEP_AS_NON_CORE", "The specific ferrous-iron transporter activity and iron-transmembrane-transport process are the clearer core role.")
        return review(info, "Electron transfer activity is the core molecular function for this cytochrome, ferredoxin, azurin, or MsrQ-like redox protein.", "ACCEPT", "Product, keyword, and domain evidence all support electron transfer.")
    if go_id == "GO:0005381":
        return review(info, "Iron ion transmembrane transporter activity is correct but broader than the ferrous-iron transporter call.", "KEEP_AS_NON_CORE", "The FTR1/OFeT family and existing ferrous-iron transporter term better capture the core activity.", ["GO:0015093"])
    if go_id == "GO:0015093":
        return review(info, "Ferrous iron transmembrane transporter activity is appropriate for the FTR1/OFeT-like membrane protein.", "ACCEPT", "The FTR1/Fip1/EfeU domain and iron-permease family assignment support ferrous iron transport.")
    if go_id == "GO:0034755":
        return review(info, "Iron ion transmembrane transport is appropriate process context for the FTR1/OFeT-like transporter.", "ACCEPT", "The supported ferrous iron transporter activity implies iron ion transmembrane transport.")
    if go_id == "GO:0033573":
        return review(info, "High-affinity iron permease complex is retained as complex context for the OFeT/FTR1-like iron transporter.", "ACCEPT", "The FTR1 iron-permease family assignment supports this complex-context annotation, although direct KT2440 subunit composition remains to be resolved.")
    if go_id == "GO:0016491":
        if cls == "multicopper_oxidase":
            return review(info, "Oxidoreductase activity is an appropriate first-pass molecular function for the multicopper oxidase.", "ACCEPT", "The product, EC class, and copper oxidase domains support oxidoreductase activity.")
        return review(info, "Oxidoreductase activity is true but broad relative to the more specific catalytic or electron-transfer role.", "MARK_AS_OVER_ANNOTATED", "A more specific redox molecular function is available for this protein.", [primary] if primary else None)
    if go_id == "GO:0004174":
        return review(info, "Electron-transferring-flavoprotein dehydrogenase activity is the core ETF-QO molecular function.", "ACCEPT", "UniProt states that this protein accepts electrons from ETF and reduces ubiquinone.")
    if go_id in {"GO:0022900", "GO:0022904"}:
        return review(info, f"{label} is appropriate process context for this membrane or soluble electron-transfer protein.", "ACCEPT", "The protein's electron-transfer role supports electron-transport-chain context.")
    if go_id == "GO:0045454":
        return review(info, "Cell redox homeostasis is appropriate broad process context for the SCO1/SenC copper-redox assembly protein.", "ACCEPT", "The SCO1/SenC family supports a redox/copper-center assembly role, while the exact partner pathway is not resolved in this first pass.")
    if go_id == "GO:0017003":
        return review(info, "Protein-heme linkage is appropriate for the CcmE heme chaperone in c-type cytochrome maturation.", "ACCEPT", "CcmE transiently binds heme and transfers it during cytochrome c biogenesis.")
    if go_id == "GO:0017004":
        return review(info, "Cytochrome complex assembly is appropriate for CcmE/CcmH cytochrome c maturation proteins.", "ACCEPT", "The Ccm product/family evidence supports cytochrome c-type biogenesis.")
    if go_id == "GO:0016829":
        return review(info, "Lyase activity is retained as broad CcmH heme-lyase context.", "KEEP_AS_NON_CORE", "The core supported process is cytochrome c-type complex assembly; the standalone lyase term is lower resolution.")
    if go_id == "GO:0016679":
        return review(info, "This oxidoreductase term is retained as non-core redox context for MsrQ.", "KEEP_AS_NON_CORE", "MsrQ is best captured as a membrane electron-transfer subunit for MsrPQ protein repair.")
    if go_id == "GO:0030091":
        return review(info, "Protein repair is appropriate process context for the MsrPQ system subunit MsrQ.", "ACCEPT", "UniProt identifies MsrQ as part of the system repairing oxidized periplasmic proteins.")
    if go_id == "GO:0008941":
        return review(info, "Nitric oxide dioxygenase NAD(P)H activity is the core flavohemoglobin molecular function.", "ACCEPT", "The EC number and UniProt functional statement support NO dioxygenation.")
    if go_id == "GO:0046210":
        return review(info, "Nitric oxide catabolic process is the core biological process for flavohemoglobin.", "ACCEPT", "The enzyme detoxifies nitric oxide by converting it to nitrate.")
    if go_id == "GO:0071500":
        return review(info, "Cellular response to nitrosative stress is appropriate for Hmp-mediated NO detoxification.", "ACCEPT", "Hmp protects cells from nitric oxide/reactive nitrogen species.")
    if go_id == "GO:0051409":
        return review(info, "Response to nitrosative stress is true but broader than the cellular response term also present.", "KEEP_AS_NON_CORE", "The specific cellular response to nitrosative stress term is preferred as the core process.", ["GO:0071500"])
    if go_id in {"GO:0005344", "GO:0015671"}:
        return review(info, f"{label} mischaracterizes flavohemoglobin as an oxygen carrier/transporter.", "REMOVE", "Hmp uses oxygen as a substrate in nitric oxide dioxygenation rather than carrying or transporting oxygen.")
    if go_id == "GO:0019825":
        return review(info, "Oxygen binding is true as substrate/cofactor context but is not the core biological role.", "MARK_AS_OVER_ANNOTATED", "The nitric oxide dioxygenase activity captures the functional use of oxygen more specifically.")

    raise ValueError(f"No review rule for {info['gene']} {go_id} {label}")


def new_annotation(info: GeneInfo, go_id: str, qualifier: str, summary: str, reason: str) -> dict[str, Any]:
    gene = info["gene"]
    return {
        "term": term(go_id),
        "evidence_type": "IEA",
        "original_reference_id": ref_file(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": base_support(info),
        },
    }


def suggested_new_annotations(info: GeneInfo) -> list[dict[str, Any]]:
    go_ids = set(info["go_ids"])
    out: list[dict[str, Any]] = []
    primary = info["profile"].get("primary")
    if primary and primary not in go_ids:
        out.append(
            new_annotation(
                info,
                primary,
                "enables",
                f"Adds {TERMS[primary]} for this redox protein.",
                "The UniProt product/domain context and Asta retrieval header support this conservative first-pass assignment.",
            )
        )
    for process in info["profile"].get("processes", []):
        if process not in go_ids:
            out.append(
                new_annotation(
                    info,
                    process,
                    "involved_in",
                    f"Adds {TERMS[process]} process context.",
                    "The supported molecular function or cytochrome-biogenesis context implies this conservative process annotation.",
                )
            )
    for location in info["profile"].get("locations", []):
        if location not in go_ids:
            out.append(
                new_annotation(
                    info,
                    location,
                    "located_in",
                    f"Adds {TERMS[location]} localization context.",
                    "The UniProt record supports this localization or membrane/transmembrane context.",
                )
            )
    return out


def references(info: GeneInfo) -> list[dict[str, Any]]:
    refs: dict[str, dict[str, Any]] = {}
    for ref_id, ref in info["existing_refs"].items():
        refs[ref_id] = ref
    for ref_id, title in GO_REF_TITLES.items():
        if ref_id in refs:
            refs[ref_id]["title"] = title
    gene = info["gene"]
    refs[ref_file(gene, "goa.tsv")] = {"id": ref_file(gene, "goa.tsv"), "title": f"QuickGO GOA annotations for {gene}", "findings": []}
    refs[ref_file(gene, "uniprot.txt")] = {
        "id": ref_file(gene, "uniprot.txt"),
        "title": f"UniProtKB entry for {gene} ({info['accession']})",
        "findings": [{"supporting_text": info["de"]}],
    }
    refs[ref_file(gene, "deep-research-asta.md")] = {
        "id": ref_file(gene, "deep-research-asta.md"),
        "title": f"Asta retrieval report for {gene} ({info['accession']})",
        "findings": [{"supporting_text": info["asta_product"]}, {"supporting_text": info["asta_domains"]}],
    }
    return list(refs.values())


def core_function(info: GeneInfo) -> dict[str, Any]:
    profile = info["profile"]
    core: dict[str, Any] = {
        "description": profile["description"],
        "supported_by": base_support(info),
    }
    primary = profile.get("primary")
    if primary:
        core["molecular_function"] = term(primary)
    if profile.get("processes"):
        core["directly_involved_in"] = [term(go_id) for go_id in profile["processes"]]
    if profile.get("locations"):
        core["locations"] = [term(go_id) for go_id in profile["locations"]]
    return core


def curate_gene(row: dict[str, str]) -> GeneInfo:
    info = load_info(row)
    gene = info["gene"]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    goa_annotations = [
        ann
        for ann in doc.get("existing_annotations", [])
        if not (
            ann.get("original_reference_id") == ref_file(gene, "uniprot.txt")
            and (ann.get("review") or {}).get("action") == "NEW"
        )
    ]
    info["go_ids"] = [ann["term"]["id"] for ann in goa_annotations]
    for ann in goa_annotations:
        existing = ann.get("review") or {}
        if gene == "hmp" and existing.get("action") and existing.get("action") != "PENDING":
            ann["review"] = existing
            ann["review"].setdefault("supported_by", [])
            ann["review"]["supported_by"].insert(0, goa_support(info, ann["term"]["id"], ann["term"]["label"]))
            ann["review"]["supported_by"].extend(base_support(info))
            ann["review"]["supported_by"] = dedupe(ann["review"]["supported_by"])
        else:
            ann["review"] = existing_review(info, ann)
            ann["review"]["supported_by"].insert(0, goa_support(info, ann["term"]["id"], ann["term"]["label"]))
            ann["review"]["supported_by"] = dedupe(ann["review"]["supported_by"])
    doc["existing_annotations"] = goa_annotations + suggested_new_annotations(info)
    doc["description"] = info["profile"]["description"]
    doc["status"] = "COMPLETE"
    doc["references"] = references(info)
    reflected_ids = {
        ann["term"]["id"]
        for ann in doc["existing_annotations"]
        if (ann.get("review") or {}).get("action") in {"ACCEPT", "NEW"}
    }
    core = core_function(info)
    if "molecular_function" in core and core["molecular_function"]["id"] not in reflected_ids:
        core.pop("molecular_function")
    for slot in ("directly_involved_in", "locations"):
        if slot in core:
            core[slot] = [item for item in core[slot] if item["id"] in reflected_ids]
            if not core[slot]:
                core.pop(slot)
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "What are the direct electron donor, electron acceptor, metal cofactor occupancy, and physiological condition for this KT2440 redox protein?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Test targeted mutants and purified proteins for electron-transfer partners, metal/cofactor content, redox potentials, and condition-specific phenotypes under iron limitation, copper stress, respiratory shift, nitrosative stress, or oxidative protein-damage conditions as appropriate.",
            "experiment_type": "redox biochemistry and condition-specific genetics",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_redox_electron_transfer_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {info['product']}",
    }
    primary = info["profile"].get("primary")
    if primary:
        annoton["function"] = descriptor(primary)
    if info["profile"].get("processes"):
        annoton["processes"] = [descriptor(go_id) for go_id in info["profile"]["processes"]]
    if info["profile"].get("locations"):
        annoton["locations"] = [descriptor(go_id) for go_id in info["profile"]["locations"]]
    return annoton


def build_module(infos: list[GeneInfo]) -> None:
    grouped: dict[str, list[GeneInfo]] = defaultdict(list)
    for info in infos:
        grouped[info["profile"]["group"]].append(info)
    parts = []
    for order, (group, group_infos) in enumerate(grouped.items(), start=1):
        parts.append(
            {
                "order": order,
                "role": group,
                "node": {
                    "id": group.lower().replace("/", "_").replace(" ", "_").replace("-", "_"),
                    "label": group,
                    "module_type": "TRANSPORT_STEP",
                    "description": f"First-pass membrane redox/electron-transfer subgroup: {group}.",
                    "annotons": [module_annoton(info) for info in group_infos],
                },
            }
        )
    concept_ids = [
        "GO:0009055",
        "GO:0015093",
        "GO:0004174",
        "GO:0008941",
        "GO:0016491",
        "GO:0017003",
        "GO:0017004",
        "GO:0030091",
        "GO:0045454",
        "GO:0022900",
        "GO:0022904",
        "GO:0034755",
        "GO:0046210",
        "GO:0071500",
        "GO:0005886",
        "GO:0016020",
        "GO:0042597",
        "GO:0030288",
        "GO:0005737",
    ]
    doc = {
        "id": "MODULE:membrane_redox_electron_transfer_boundary",
        "title": "Membrane redox and electron-transfer spillover boundary",
        "description": (
            "Boundary module for PSEPK cytochromes, ferredoxins, blue-copper electron carriers, "
            "cytochrome c maturation proteins, MsrQ/Hmp redox detoxification nodes, and the OFeT/FTR1-like iron transporter "
            "pulled into the transport ion/metal split by metal-binding, heme, iron-sulfur, or electron-transport evidence."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK membrane redox/electron-transfer spillover batch",
                "statement": "The batch table records 25 PSEPK ion/metal-bucket genes assigned to cytochrome, ferredoxin, Ccm, flavohemoglobin, MsrQ, multicopper, azurin, and OFeT/FTR1-like redox/transport contexts.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_ion_metal_partition.tsv",
                "title": "PSEPK transport ion/metal sub-bucket partition",
                "statement": "The deeper ion/metal partition separates redox spillovers from true cation transporters, ABC metal systems, P-type ATPases, and membrane-enzyme side nodes.",
            },
        ],
        "notes": (
            "First-pass interpretation: treat this as a boundary/spillover module, not a single canonical pathway. "
            "Specific electron-transfer, iron-transport, cytochrome-c biogenesis, nitric-oxide-detoxification, protein-repair, and multicopper-oxidase calls are retained where product/family and GOA agree; metal/heme/FAD/Fe-S binding terms are kept as supporting context rather than standalone core functions."
        ),
        "module": {
            "id": "membrane_redox_electron_transfer_boundary",
            "label": "Membrane redox and electron-transfer spillover boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [descriptor(go_id, "Concept used for first-pass membrane redox/electron-transfer curation.") for go_id in concept_ids],
            "parts": parts,
        },
    }
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    infos = [curate_gene(row) for row in load_rows()]
    build_module(infos)
    print(f"Curated {len(infos)} genes")
    print(f"Wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
