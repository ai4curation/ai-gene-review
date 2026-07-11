#!/usr/bin/env python3
"""First-pass curation for monovalent cation antiporters and potassium systems."""

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
    "module_transport_membrane_efflux_ion_metal_monovalent_cation_antiporters_potassium_systems.tsv"
)
MODULE_PATH = ROOT / "modules/monovalent_cation_antiporter_boundary.yaml"

TAXON = {
    "id": "NCBITaxon:160488",
    "label": "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)",
}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on inter-ontology links",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0001508": "action potential",
    "GO:0005216": "monoatomic ion channel activity",
    "GO:0005249": "voltage-gated potassium channel activity",
    "GO:0005262": "calcium channel activity",
    "GO:0005886": "plasma membrane",
    "GO:0006811": "monoatomic ion transport",
    "GO:0006812": "monoatomic cation transport",
    "GO:0006813": "potassium ion transport",
    "GO:0006814": "sodium ion transport",
    "GO:0006874": "intracellular calcium ion homeostasis",
    "GO:0006884": "cell volume homeostasis",
    "GO:0006885": "regulation of pH",
    "GO:0008076": "voltage-gated potassium channel complex",
    "GO:0008273": "calcium, potassium:sodium antiporter activity",
    "GO:0008324": "monoatomic cation transmembrane transporter activity",
    "GO:0015075": "monoatomic ion transmembrane transporter activity",
    "GO:0015079": "potassium ion transmembrane transporter activity",
    "GO:0015081": "sodium ion transmembrane transporter activity",
    "GO:0015293": "symporter activity",
    "GO:0015297": "antiporter activity",
    "GO:0015379": "potassium:chloride symporter activity",
    "GO:0015385": "sodium:proton antiporter activity",
    "GO:0015386": "potassium:proton antiporter activity",
    "GO:0015459": "potassium channel regulator activity",
    "GO:0016020": "membrane",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0030001": "metal ion transport",
    "GO:0034220": "monoatomic ion transmembrane transport",
    "GO:0035725": "sodium ion transmembrane transport",
    "GO:0043266": "regulation of potassium ion transport",
    "GO:0050660": "flavin adenine dinucleotide binding",
    "GO:0051453": "regulation of intracellular pH",
    "GO:0055085": "transmembrane transport",
    "GO:0070588": "calcium ion transmembrane transport",
    "GO:0071805": "potassium ion transmembrane transport",
    "GO:0098655": "monoatomic cation transmembrane transport",
    "GO:0098719": "sodium ion import across plasma membrane",
    "GO:1902600": "proton transmembrane transport",
}

CATEGORY = {
    "trkA": "trk_regulator",
    "trkH-I": "trk_permease",
    "trkH-II": "trk_permease",
    "kup": "kup_transporter",
    "kefB-I": "kef_cpa2",
    "kefB-II": "kef_cpa2",
    "kefB-III": "kef_cpa2",
    "PP_0928": "knc_exchanger",
    "nhaA1": "nhaA",
    "nhaA2": "nhaA",
    "nhaB": "nhaB",
    "PP_1467": "mixed_cpa1",
    "PP_1587": "mixed_cpa1",
    "nhaP": "mixed_cpa1",
    "nhaP2": "nhaP2",
    "PP_5355": "cpa2_sodium_proton",
    "mrpG": "mrp_subunit",
    "mrpF": "mrp_subunit",
    "mrpE": "mrp_subunit",
    "mrpD": "mrp_subunit",
    "mrpC": "mrp_subunit",
    "mrpAB": "mrp_subunit",
    "PP_3293": "potassium_channel_domain",
    "PP_4304": "vic_potassium_channel",
    "PP_3556": "nhaC_like",
    "yfbS": "dass_related",
}

GROUP = {
    "trk_regulator": "Trk/Kup potassium uptake and regulation",
    "trk_permease": "Trk/Kup potassium uptake and regulation",
    "kup_transporter": "Trk/Kup potassium uptake and regulation",
    "kef_cpa2": "Kef/CPA2 potassium-proton antiporter candidates",
    "cpa2_sodium_proton": "Kef/CPA2 potassium-proton antiporter candidates",
    "nhaA": "NhaA/NhaB sodium-proton antiporters",
    "nhaB": "NhaA/NhaB sodium-proton antiporters",
    "mixed_cpa1": "NhaP/CPA1 mixed monovalent-cation antiporters",
    "nhaP2": "NhaP/CPA1 mixed monovalent-cation antiporters",
    "mrp_subunit": "Mrp multicomponent monovalent-cation antiporter locus",
    "knc_exchanger": "Potassium/calcium/channel candidates",
    "potassium_channel_domain": "Potassium/calcium/channel candidates",
    "vic_potassium_channel": "Potassium/calcium/channel candidates",
    "nhaC_like": "Conservative side candidates",
    "dass_related": "Conservative side candidates",
}

DOMAIN_NEEDLES = {
    "trk_regulator": ["Trk_Ktr_HKT_K-transport", "K_uptake_TrkA", "RCK_N"],
    "trk_permease": ["TrkH potassium transport family", "TrkH.", "Cat_transpt"],
    "kup_transporter": ["HAK/KUP transporter", "K+_transporter", "Kup."],
    "kef_cpa2": ["KefB/KefC", "K/H_exchanger", "monovalent cation:proton antiporter 2"],
    "cpa2_sodium_proton": ["monovalent cation:proton antiporter 2", "Cation/H_exchanger_TM"],
    "nhaA": ["NhaA Na(+)/H(+)", "Na/H_antiporter_dom_sf", "Na_H_antiport_1"],
    "nhaB": ["NhaB Na(+)/H(+)", "Na+/H+_antiporter_NhaB"],
    "mixed_cpa1": ["monovalent cation:proton antiporter 1", "Cation/H_exchanger_CPA1", "Cation/H_exchanger_TM"],
    "nhaP2": ["K(+)/H(+) antiporter NhaP2", "NhaP2.", "monovalent cation:proton antiporter 1"],
    "mrp_subunit": ["CPA3", "Mnh", "Mrp", "antiporter subunit"],
    "knc_exchanger": ["K/Na/Ca-exchanger", "NaCa_Exmemb"],
    "potassium_channel_domain": ["Potassium channel domain-containing", "K_chnl_dom", "Ion_trans_2"],
    "vic_potassium_channel": ["VIC family", "VG_K_chnl", "Ion_trans_dom"],
    "nhaC_like": ["Sodium:proton antiporter", "Na/H_Antiport_NhaC-like_C", "Na_H_antiport_2"],
    "dass_related": ["DASS-Related_Transporters", "Cit_transptr-like_dom", "Na/sul_symport_CS"],
}


class GeneInfo(dict[str, Any]):
    gene: str


def term(go_id: str) -> dict[str, str]:
    return {"id": go_id, "label": TERMS[go_id]}


def ref_file(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def load_rows() -> list[dict[str, str]]:
    with BATCH_PATH.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def first_de_line(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("DE   RecName") or line.startswith("DE   SubName"):
            return line
    for line in lines:
        if line.startswith("DE   "):
            return line
    raise ValueError("No UniProt DE line found")


def first_line(lines: list[str], needle: str, optional: bool = False) -> str | None:
    for line in lines:
        if needle in line:
            return line
    if optional:
        return None
    raise ValueError(f"Could not find {needle!r}")


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


def load_info(row: dict[str, str]) -> GeneInfo:
    gene = row["gene"]
    uniprot_path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta_path = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    review_path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    uniprot_lines = uniprot_path.read_text(encoding="utf-8").splitlines()
    asta_lines = asta_path.read_text(encoding="utf-8").splitlines()
    review_doc = yaml.safe_load(review_path.read_text(encoding="utf-8"))
    info = GeneInfo(
        gene=gene,
        accession=row["uniprot_accession"],
        product=row["protein_name"],
        category=CATEGORY[gene],
        group=GROUP[CATEGORY[gene]],
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
    for needle in DOMAIN_NEEDLES[info["category"]]:
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


def has_more_specific(info: GeneInfo, ids: set[str]) -> bool:
    return bool(set(info["go_ids"]) & ids)


def default_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]
    category = info["category"]

    if go_id == "GO:0005886":
        action = "KEEP_AS_NON_CORE" if category == "trk_regulator" else "ACCEPT"
        reason = (
            "TrkA is a cytosolic/peripheral regulatory subunit of a potassium uptake system; plasma-membrane context is useful but not the core function."
            if category == "trk_regulator"
            else "Bacterial inner/cytoplasmic membrane localization is appropriate for this monovalent-cation transport protein or subunit."
        )
        return review(info, "Plasma membrane localization is reviewed as bacterial membrane context.", action, reason)

    if go_id == "GO:0016020":
        if "GO:0005886" in info["go_ids"]:
            return review(
                info,
                "Generic membrane localization is true but less informative than plasma membrane.",
                "MARK_AS_OVER_ANNOTATED",
                "A more specific bacterial plasma-membrane annotation is present.",
            )
        return review(
            info,
            "Membrane localization is appropriate for this predicted transporter or channel candidate.",
            "ACCEPT",
            "The UniProt membrane/transmembrane metadata support membrane localization.",
        )

    if go_id in {"GO:0055085", "GO:0034220", "GO:0098655", "GO:0006811", "GO:0006812"}:
        if category in {"trk_regulator", "dass_related", "mrp_subunit"}:
            return review(
                info,
                f"{label} is retained as broad transporter-system context.",
                "KEEP_AS_NON_CORE" if category == "trk_regulator" else "ACCEPT",
                "The protein participates in a membrane transport context, but substrate and component boundaries are better captured by more specific family-level terms.",
            )
        if has_more_specific(info, {"GO:0015385", "GO:0015386", "GO:0015079", "GO:0005249", "GO:0008273"}):
            return review(
                info,
                f"{label} is true but broad relative to the supported transporter function.",
                "MARK_AS_OVER_ANNOTATED",
                "A more specific antiporter, channel, or potassium-transporter annotation captures the core function.",
            )
        return review(info, f"{label} is appropriate broad transport context.", "ACCEPT", "The product and domain evidence support a membrane transport role.")

    if go_id in {"GO:0006813", "GO:0071805"}:
        if category in {"trk_regulator", "dass_related"}:
            return review(
                info,
                "Potassium-transport context is not established as a direct substrate-transport activity for this protein.",
                "KEEP_AS_NON_CORE" if category == "trk_regulator" else "MARK_AS_OVER_ANNOTATED",
                "The evidence supports regulatory or broad transporter-family context rather than direct potassium transport by this protein.",
            )
        return review(
            info,
            "Potassium transmembrane transport is appropriate for this potassium transporter, antiporter, or channel candidate.",
            "ACCEPT",
            "Product names, domains, or GOA support potassium transport context for this membrane protein.",
        )

    if go_id in {"GO:0006814", "GO:0035725", "GO:0098719"}:
        if category in {"nhaA", "nhaB", "mixed_cpa1", "nhaC_like", "cpa2_sodium_proton", "mrp_subunit", "knc_exchanger"}:
            return review(
                info,
                "Sodium transmembrane transport is appropriate for this sodium/cation antiporter or exchanger context.",
                "ACCEPT",
                "The product, family, or antiporter-domain evidence supports sodium or sodium/cation transport across the membrane.",
            )
        return review(
            info,
            "Sodium transport is not the best-supported direct substrate call for this protein.",
            "MARK_AS_OVER_ANNOTATED",
            "The current family evidence supports a different potassium/channel or broad transporter context.",
        )

    if go_id == "GO:0006885":
        return review(
            info,
            "pH regulation is plausible physiological context for a sodium/proton antiporter.",
            "KEEP_AS_NON_CORE",
            "Na+/H+ exchange contributes to pH homeostasis, but the direct molecular function is antiporter activity.",
        )

    if go_id == "GO:0051453":
        return review(
            info,
            "Regulation of intracellular pH is retained as physiological context.",
            "KEEP_AS_NON_CORE",
            "NhaP-family cation/proton antiporters can affect pH homeostasis, but the direct function is cation/proton antiport.",
        )

    if go_id == "GO:1902600":
        if category in {"kef_cpa2", "mixed_cpa1", "nhaP2", "cpa2_sodium_proton"}:
            return review(
                info,
                "Proton transmembrane transport is part of the cation/proton antiport mechanism.",
                "ACCEPT",
                "The product and CPA-family domains support proton-coupled antiport.",
            )
        return review(
            info,
            "Proton transmembrane transport is broad context for this antiporter-family protein.",
            "KEEP_AS_NON_CORE",
            "The exact cation/proton exchange chemistry remains less resolved than the broad antiporter assignment.",
        )

    if go_id == "GO:0015297":
        if category in {"nhaA", "nhaB", "nhaP2"}:
            return review(
                info,
                "Generic antiporter activity is true but less informative than the specific cation/proton antiporter term.",
                "MARK_AS_OVER_ANNOTATED",
                "The product and GOA include a more specific sodium:proton or potassium:proton antiporter activity.",
            )
        return review(
            info,
            "Antiporter activity is an appropriate conservative function for this monovalent-cation/proton antiporter context.",
            "ACCEPT",
            "The product and cation/proton exchanger domains support antiporter activity while exact cation specificity may remain unresolved.",
        )

    if go_id == "GO:0015385":
        if category in {"nhaA", "nhaB", "mixed_cpa1", "nhaC_like", "cpa2_sodium_proton"}:
            return review(
                info,
                "Sodium:proton antiporter activity is appropriate for this Nha/CPA-family antiporter context.",
                "ACCEPT",
                "The product and Na+/H+ antiporter family/domain evidence support sodium/proton antiporter activity.",
            )
        if category == "mrp_subunit":
            return review(
                info,
                "Sodium:proton antiporter activity is too substrate-specific for this individual Mrp subunit.",
                "MODIFY",
                "The multicomponent Mrp locus supports antiporter-system participation, but the individual subunit evidence does not resolve sodium versus other monovalent cations.",
                ["GO:0015297"],
            )
        return review(
            info,
            "Sodium:proton antiporter activity is not the best-supported direct function for this protein.",
            "MARK_AS_OVER_ANNOTATED",
            "The evidence points to a potassium/channel/regulatory transporter context rather than a specific sodium:proton antiporter.",
        )

    if go_id == "GO:0015386":
        if category in {"mixed_cpa1", "nhaP2", "kef_cpa2"}:
            return review(
                info,
                "Potassium:proton antiporter activity is appropriate for this CPA/Kef/NhaP-family protein.",
                "ACCEPT",
                "The product and CPA-family domain evidence support potassium/proton antiport context.",
            )
        return review(
            info,
            "Potassium:proton antiporter activity is broader family context but not the strongest substrate-specific call here.",
            "KEEP_AS_NON_CORE",
            "The cation/proton antiporter family evidence is present, but another substrate-specific annotation better captures the core function.",
        )

    if go_id == "GO:0015081":
        return review(
            info,
            "Sodium ion transmembrane transporter activity is true but less specific than sodium:proton antiporter activity.",
            "MARK_AS_OVER_ANNOTATED",
            "The antiporter term captures both sodium transport and the proton-coupled exchange mechanism.",
            ["GO:0015385"],
        )

    if go_id == "GO:0015079":
        if category in {"trk_regulator"}:
            return review(
                info,
                "Direct potassium transporter activity is too strong for TrkA, a regulatory/RCK subunit.",
                "MODIFY",
                "TrkA supports or regulates potassium uptake but is not the membrane pore itself.",
                ["GO:0015459"],
            )
        return review(
            info,
            "Potassium ion transmembrane transporter activity is appropriate for this potassium transporter context.",
            "ACCEPT",
            "The product and potassium-transporter family evidence support potassium transmembrane transporter activity.",
        )

    if go_id == "GO:0015379":
        return review(
            info,
            "Potassium:chloride symporter activity is too specific for TrkH-family evidence in this bacterial transporter.",
            "MODIFY",
            "The product and TrkH family support potassium transmembrane transporter activity, but chloride symport is not established.",
            ["GO:0015079"],
        )

    if go_id == "GO:0015293":
        return review(
            info,
            "Symporter activity is appropriate for Kup or DASS-related transporter context.",
            "ACCEPT",
            "The product/domain evidence supports a symporter-family transporter, with exact coupling or substrate specificity unresolved where not named.",
        )

    if go_id == "GO:0008324":
        if category in {"trk_regulator", "yfbS"}:
            return review(
                info,
                "Generic cation transmembrane transporter activity overstates the direct function of this regulatory or DASS-related protein.",
                "MARK_AS_OVER_ANNOTATED",
                "The current evidence supports regulatory or unresolved transporter context rather than a clean cation-transporter activity.",
            )
        if has_more_specific(info, {"GO:0015079", "GO:0015385", "GO:0015386", "GO:0005249", "GO:0008273"}):
            return review(
                info,
                "Generic cation transporter activity is true but less informative than the specific transporter term.",
                "MARK_AS_OVER_ANNOTATED",
                "A more specific potassium, sodium/proton, potassium/proton, channel, or exchanger term is present.",
            )
        return review(info, "Generic cation transporter activity is appropriate at first-pass resolution.", "ACCEPT", "The family/domain evidence supports a cation-transport context.")

    if go_id == "GO:0015075":
        return review(
            info,
            "Generic ion transmembrane transporter activity is broad context for this antiporter subunit.",
            "KEEP_AS_NON_CORE",
            "A broader subunit contribution is appropriate, but antiporter-system context is more informative.",
        )

    if go_id == "GO:0015459":
        if category == "trk_regulator":
            return review(
                info,
                "Potassium channel regulator activity is the best-supported core activity for TrkA.",
                "ACCEPT",
                "TrkA/RCK domain evidence supports regulation of potassium transport rather than a pore-forming transporter role.",
            )
        return review(
            info,
            "Potassium channel regulator activity is not established for this transporter-family entry.",
            "MARK_AS_OVER_ANNOTATED",
            "The DASS-related product/domain evidence does not support a potassium-channel regulator function.",
        )

    if go_id == "GO:0043266":
        if category == "trk_regulator":
            return review(
                info,
                "Regulation of potassium ion transport is appropriate TrkA system context.",
                "ACCEPT",
                "TrkA/RCK domains support a regulatory role in potassium uptake systems.",
            )
        return review(
            info,
            "Regulation of potassium ion transport is not established for this transporter-family candidate.",
            "MARK_AS_OVER_ANNOTATED",
            "The current DASS-related evidence does not support potassium-channel regulation.",
        )

    if go_id == "GO:0008273":
        return review(
            info,
            "Calcium, potassium:sodium antiporter activity is the most specific supported activity for this exchanger candidate.",
            "ACCEPT",
            "The product and K/Na/Ca exchanger domains support cation-exchanger activity.",
        )

    if go_id == "GO:0005262":
        return review(
            info,
            "Calcium channel activity is too narrow for a K-dependent Na/Ca exchanger-related protein.",
            "MODIFY",
            "The exchanger product and domains support calcium/potassium:sodium antiporter activity rather than a calcium channel pore.",
            ["GO:0008273"],
        )

    if go_id in {"GO:0006874", "GO:0070588"}:
        return review(
            info,
            "Calcium homeostasis/transport is appropriate process context for this Na/Ca exchanger-related protein.",
            "ACCEPT" if go_id == "GO:0070588" else "KEEP_AS_NON_CORE",
            "The K/Na/Ca exchanger domains support calcium transmembrane transport context, while homeostasis is physiological context.",
        )

    if go_id == "GO:0005249":
        return review(
            info,
            "Voltage-gated potassium channel activity is appropriate for this VIC-family potassium-channel candidate.",
            "ACCEPT",
            "The product and voltage-gated potassium-channel family/domain evidence support this channel activity at first-pass resolution.",
        )

    if go_id == "GO:0005216":
        return review(
            info,
            "Generic ion channel activity is true but less informative than voltage-gated potassium channel activity for this candidate.",
            "KEEP_AS_NON_CORE",
            "A more specific voltage-gated potassium channel activity annotation is present.",
        )

    if go_id == "GO:0008076":
        return review(
            info,
            "Voltage-gated potassium channel complex is retained as component context but not as the core function.",
            "KEEP_AS_NON_CORE",
            "The protein is a potassium-channel candidate; the molecular channel activity and potassium transport process are more informative than complex membership.",
        )

    if go_id == "GO:0001508":
        return review(
            info,
            "Action potential is not appropriate biological-process context for this bacterial potassium-channel candidate.",
            "REMOVE",
            "Pseudomonas putida does not have animal-style action potentials; the supported function is channel/transmembrane ion transport.",
            ["GO:0071805"],
        )

    if go_id == "GO:0006884":
        return review(
            info,
            "Cell volume homeostasis is retained as non-core physiology for NhaP2.",
            "KEEP_AS_NON_CORE",
            "Potassium/proton antiport can affect cell volume and osmotic physiology, but the direct molecular function is antiporter activity.",
        )

    if go_id == "GO:0050660":
        return review(
            info,
            "FAD binding is retained only as possible domain context for NhaP2.",
            "KEEP_AS_NON_CORE",
            "The core role is potassium/proton antiport; FAD-binding-domain evidence is secondary and not enough to define the transporter function.",
        )

    if go_id == "GO:0030001":
        return review(
            info,
            "Metal ion transport is too broad and likely over-propagated for TrkH potassium transport context.",
            "MODIFY",
            "The product and TrkH-family evidence support potassium transmembrane transport rather than generic metal ion transport.",
            ["GO:0015079"],
        )

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
    category = info["category"]
    go_ids = set(info["go_ids"])
    out: list[dict[str, Any]] = []
    if category == "potassium_channel_domain":
        out.extend(
            [
                new_annotation(
                    info,
                    "GO:0005216",
                    "enables",
                    "Adds broad ion-channel activity for the potassium-channel-domain protein.",
                    "The product and PF07885/IPR013099 potassium-channel domain support a channel-function candidate, but voltage gating is not established.",
                ),
                new_annotation(
                    info,
                    "GO:0071805",
                    "involved_in",
                    "Adds potassium ion transmembrane transport context for the potassium-channel-domain protein.",
                    "The product and potassium-channel domain support potassium transport context at first-pass resolution.",
                ),
                new_annotation(
                    info,
                    "GO:0016020",
                    "located_in",
                    "Adds membrane localization for the potassium-channel-domain protein.",
                    "The UniProt record supports membrane/transmembrane context.",
                ),
            ]
        )
    if category == "nhaC_like" and "GO:0015385" not in go_ids:
        out.extend(
            [
                new_annotation(
                    info,
                    "GO:0015385",
                    "enables",
                    "Adds sodium:proton antiporter activity for the NhaC-like antiporter candidate.",
                    "The product name and Na/H antiporter domains support sodium/proton antiporter activity, despite broader amino-acid-transporter family signal.",
                ),
                new_annotation(
                    info,
                    "GO:0035725",
                    "involved_in",
                    "Adds sodium ion transmembrane transport for the NhaC-like antiporter candidate.",
                    "Sodium/proton antiport implies sodium transport across the membrane.",
                ),
            ]
        )
    if category == "dass_related" and "GO:0015293" not in go_ids:
        out.append(
            new_annotation(
                info,
                "GO:0015293",
                "enables",
                "Adds broad symporter activity for the DASS-related transporter candidate.",
                "The DASS/Na-sulfate symporter domains support symporter-family context, but the exact solute is unresolved.",
            )
        )
    if category == "mrp_subunit" and "GO:0015297" not in go_ids:
        out.append(
            new_annotation(
                info,
                "GO:0015297",
                "contributes_to",
                "Adds antiporter contribution for the Mrp multicomponent antiporter subunit.",
                "The Mrp/CPA3 subunit product and domain context support contribution to a multicomponent monovalent-cation antiporter.",
            )
        )
    if category == "kef_cpa2" and "GO:0015386" not in go_ids:
        out.append(
            new_annotation(
                info,
                "GO:0015386",
                "enables",
                "Adds potassium:proton antiporter activity for the Kef/CPA2-family protein.",
                "The product name and Kef/CPA2 K/H exchanger family evidence support potassium/proton antiporter activity.",
            )
        )
    if category == "kef_cpa2" and "GO:0071805" not in go_ids:
        out.append(
            new_annotation(
                info,
                "GO:0071805",
                "involved_in",
                "Adds potassium ion transmembrane transport context for the Kef/CPA2 antiporter.",
                "Potassium/proton antiport moves potassium across the membrane.",
            )
        )
    if category == "trk_permease" and "GO:0015079" not in go_ids:
        out.append(
            new_annotation(
                info,
                "GO:0015079",
                "enables",
                "Adds potassium ion transmembrane transporter activity for the TrkH permease.",
                "The TrkH product/family evidence supports potassium transmembrane transporter activity.",
            )
        )
    if category == "cpa2_sodium_proton" and "GO:0015385" not in go_ids:
        out.append(
            new_annotation(
                info,
                "GO:0015385",
                "enables",
                "Adds sodium:proton antiporter activity for the CPA2 sodium/proton antiporter candidate.",
                "The product name and CPA2 Na/H exchanger domain evidence support sodium/proton antiporter activity.",
            )
        )
    return out


def description(info: GeneInfo) -> str:
    gene = info["gene"]
    category = info["category"]
    product = info["product"]
    if category == "trk_regulator":
        return f"{gene} encodes a TrkA/RCK-family regulatory subunit associated with bacterial potassium uptake systems."
    if category == "trk_permease":
        return f"{gene} encodes a TrkH-family membrane protein predicted to mediate potassium uptake or potassium transport-system function."
    if category == "kup_transporter":
        return f"{gene} encodes a HAK/KUP-family potassium transporter involved in potassium uptake/homeostasis."
    if category == "kef_cpa2":
        return f"{gene} encodes a Kef/CPA2-family potassium/proton antiporter candidate, likely membrane-localized and associated with potassium efflux or cation/proton homeostasis."
    if category == "cpa2_sodium_proton":
        return f"{gene} encodes a CPA2-family sodium/proton antiporter candidate with unresolved exact physiological substrate preference."
    if category == "nhaA":
        return f"{gene} encodes an NhaA-family sodium/proton antiporter, an inner-membrane transporter that exports sodium in exchange for protons."
    if category == "nhaB":
        return f"{gene} encodes an NhaB-family sodium/proton antiporter, an inner-membrane transporter that exports sodium in exchange for protons."
    if category == "mixed_cpa1":
        return f"{gene} encodes an NhaP/CPA1-family cation/proton antiporter with sodium and/or potassium antiport context."
    if category == "nhaP2":
        return f"{gene} encodes NhaP2, a potassium/proton antiporter of the CPA1 family."
    if category == "mrp_subunit":
        return f"{gene} encodes {product}, a subunit of a multicomponent Mrp/CPA3 monovalent-cation antiporter locus."
    if category == "knc_exchanger":
        return f"{gene} encodes a K-dependent sodium/calcium exchanger-related membrane protein."
    if category == "potassium_channel_domain":
        return f"{gene} encodes a potassium-channel-domain membrane protein with unresolved gating and physiological role."
    if category == "vic_potassium_channel":
        return f"{gene} encodes a VIC-family potassium-channel candidate with voltage-gated channel-domain features."
    if category == "nhaC_like":
        return f"{gene} encodes a NhaC-like sodium/proton antiporter candidate; family evidence is mixed, so substrate context remains provisional."
    if category == "dass_related":
        return f"{gene} encodes a DASS-related sodium/anion symporter-family transporter candidate with unresolved substrate specificity."
    raise ValueError(f"Unhandled category {category}")


def core_function(info: GeneInfo) -> dict[str, Any]:
    category = info["category"]
    support_lines = base_support(info)
    if category == "trk_regulator":
        return {
            "description": "TrkA/RCK-family regulatory subunit for potassium uptake-system control.",
            "molecular_function": term("GO:0015459"),
            "directly_involved_in": [term("GO:0043266")],
            "supported_by": support_lines,
        }
    if category in {"trk_permease", "kup_transporter"}:
        return {
            "description": "Potassium transmembrane transporter component of Trk/Kup potassium uptake context.",
            "molecular_function": term("GO:0015079"),
            "directly_involved_in": [term("GO:0071805")],
            "locations": [term("GO:0005886")],
            "supported_by": support_lines,
        }
    if category in {"nhaA", "nhaB", "nhaC_like", "cpa2_sodium_proton"}:
        return {
            "description": "Sodium/proton antiporter supporting sodium transmembrane transport and ion/pH homeostasis.",
            "molecular_function": term("GO:0015385"),
            "directly_involved_in": [term("GO:0035725")],
            "locations": [term("GO:0005886")],
            "supported_by": support_lines,
        }
    if category == "kef_cpa2":
        return {
            "description": "Kef/CPA2-family potassium/proton antiporter candidate.",
            "molecular_function": term("GO:0015386"),
            "directly_involved_in": [term("GO:0071805"), term("GO:1902600")],
            "locations": [term("GO:0005886")],
            "supported_by": support_lines,
        }
    if category == "mixed_cpa1":
        return {
            "description": "NhaP/CPA1-family monovalent-cation/proton antiporter with unresolved sodium versus potassium preference.",
            "molecular_function": term("GO:0015297"),
            "directly_involved_in": [term("GO:0055085")],
            "locations": [term("GO:0005886")],
            "supported_by": support_lines,
        }
    if category == "nhaP2":
        return {
            "description": "NhaP2 potassium/proton antiporter.",
            "molecular_function": term("GO:0015386"),
            "directly_involved_in": [term("GO:0071805"), term("GO:1902600")],
            "locations": [term("GO:0005886")],
            "supported_by": support_lines,
        }
    if category == "mrp_subunit":
        return {
            "description": "Subunit contributing to a multicomponent Mrp/CPA3 monovalent-cation antiporter.",
            "contributes_to_molecular_function": term("GO:0015297"),
            "directly_involved_in": [term("GO:0055085")],
            "locations": [term("GO:0005886")],
            "supported_by": support_lines,
        }
    if category == "knc_exchanger":
        return {
            "description": "K-dependent sodium/calcium exchanger-related membrane transporter.",
            "molecular_function": term("GO:0008273"),
            "directly_involved_in": [term("GO:0070588"), term("GO:0071805")],
            "locations": [term("GO:0005886")],
            "supported_by": support_lines,
        }
    if category == "potassium_channel_domain":
        return {
            "description": "Potassium-channel-domain membrane protein with broad ion-channel activity at first-pass resolution.",
            "molecular_function": term("GO:0005216"),
            "directly_involved_in": [term("GO:0071805")],
            "locations": [term("GO:0016020")],
            "supported_by": support_lines,
        }
    if category == "vic_potassium_channel":
        return {
            "description": "VIC-family potassium-channel candidate.",
            "molecular_function": term("GO:0005249"),
            "directly_involved_in": [term("GO:0071805")],
            "locations": [term("GO:0016020")],
            "supported_by": support_lines,
        }
    if category == "dass_related":
        return {
            "description": "DASS-related sodium/anion symporter-family transporter candidate with unresolved substrate.",
            "molecular_function": term("GO:0015293"),
            "directly_involved_in": [term("GO:0055085")],
            "locations": [term("GO:0005886")],
            "supported_by": support_lines,
        }
    raise ValueError(f"Unhandled category {category}")


def references(info: GeneInfo) -> list[dict[str, Any]]:
    refs: dict[str, dict[str, Any]] = {}
    for ref_id, ref in info["existing_refs"].items():
        if ref_id.startswith("file:PSEPK/") and "deep-research-falcon" in ref_id:
            continue
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
        ann["review"] = default_review(info, ann)
        ann["review"]["supported_by"].insert(0, goa_support(info, ann["term"]["id"], ann["term"]["label"]))
        ann["review"]["supported_by"] = dedupe(ann["review"]["supported_by"])
    doc["existing_annotations"] = goa_annotations + suggested_new_annotations(info)
    doc["description"] = description(info)
    doc["status"] = "COMPLETE"
    doc["references"] = references(info)
    core = core_function(info)
    reflected_ids = {
        ann["term"]["id"]
        for ann in doc["existing_annotations"]
        if (ann.get("review") or {}).get("action") in {"ACCEPT", "NEW"}
    }
    if "molecular_function" in core and core["molecular_function"]["id"] not in reflected_ids:
        core.pop("molecular_function")
    if "contributes_to_molecular_function" in core and core["contributes_to_molecular_function"]["id"] not in reflected_ids:
        core.pop("contributes_to_molecular_function")
    for slot in ("directly_involved_in", "locations"):
        if slot in core:
            core[slot] = [item for item in core[slot] if item["id"] in reflected_ids]
            if not core[slot]:
                core.pop(slot)
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "What are the transported cation, directionality, partner subunits, and physiological conditions for this "
                "monovalent-cation transport protein in Pseudomonas putida KT2440?"
            )
        }
    ]
    if info["category"] in {"dass_related", "nhaC_like", "potassium_channel_domain"}:
        doc["suggested_questions"] = [
            {
                "question": "Does this candidate transport sodium, potassium, or another ion/solute in KT2440, and should it remain in this monovalent-cation boundary after experimental substrate testing?"
            }
        ]
    doc["suggested_experiments"] = [
        {
            "description": (
                "Measure ion-dependent growth and transport in single and combinatorial deletion strains under sodium, potassium, pH, osmotic, and electrophile stress conditions."
            ),
            "experiment_type": "ion-transport genetics and membrane transport assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def descriptor(go_id: str, description_text: str | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {"preferred_term": TERMS[go_id], "term": term(go_id)}
    if description_text:
        item["description"] = description_text
    return item


def module_function_for(info: GeneInfo) -> str | None:
    category = info["category"]
    if category == "trk_regulator":
        return "GO:0015459"
    if category in {"trk_permease", "kup_transporter"}:
        return "GO:0015079"
    if category in {"nhaA", "nhaB", "nhaC_like", "cpa2_sodium_proton"}:
        return "GO:0015385"
    if category in {"kef_cpa2", "nhaP2"}:
        return "GO:0015386"
    if category in {"mixed_cpa1", "mrp_subunit"}:
        return "GO:0015297"
    if category == "knc_exchanger":
        return "GO:0008273"
    if category == "potassium_channel_domain":
        return "GO:0005216"
    if category == "vic_potassium_channel":
        return "GO:0005249"
    if category == "dass_related":
        return "GO:0015293"
    return None


def module_processes_for(info: GeneInfo) -> list[str]:
    category = info["category"]
    if category == "trk_regulator":
        return ["GO:0043266"]
    if category in {"trk_permease", "kup_transporter", "kef_cpa2", "nhaP2", "potassium_channel_domain", "vic_potassium_channel"}:
        return ["GO:0071805"]
    if category in {"nhaA", "nhaB", "nhaC_like", "cpa2_sodium_proton"}:
        return ["GO:0035725"]
    if category == "knc_exchanger":
        return ["GO:0070588", "GO:0071805"]
    return ["GO:0055085"]


def module_locations_for(info: GeneInfo) -> list[str]:
    if info["category"] == "trk_regulator":
        return []
    if info["category"] in {"potassium_channel_domain", "vic_potassium_channel"}:
        return ["GO:0016020"]
    return ["GO:0005886"]


def build_module(infos: list[GeneInfo]) -> None:
    grouped: dict[str, list[GeneInfo]] = defaultdict(list)
    for info in infos:
        grouped[info["group"]].append(info)

    concept_ids = [
        "GO:0015459",
        "GO:0043266",
        "GO:0015079",
        "GO:0071805",
        "GO:0015385",
        "GO:0035725",
        "GO:0015386",
        "GO:0015297",
        "GO:0008273",
        "GO:0070588",
        "GO:0005216",
        "GO:0005249",
        "GO:0015293",
        "GO:0055085",
        "GO:0005886",
        "GO:0016020",
    ]

    parts = []
    for order, (group, group_infos) in enumerate(grouped.items(), start=1):
        annotons = []
        for info in group_infos:
            gene = info["gene"]
            annoton: dict[str, Any] = {
                "id": f"{gene}_monovalent_cation_context",
                "label": f"{gene}: {info['product']}",
                "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
                "role_description": f"{gene}: {info['product']} ({info['category'].replace('_', ' ')})",
            }
            function_id = module_function_for(info)
            if function_id:
                annoton["function"] = descriptor(function_id)
            processes = [descriptor(go_id) for go_id in module_processes_for(info)]
            if processes:
                annoton["processes"] = processes
            locations = [descriptor(go_id) for go_id in module_locations_for(info)]
            if locations:
                annoton["locations"] = locations
            annotons.append(annoton)
        parts.append(
            {
                "order": order,
                "role": group,
                "node": {
                    "id": group.lower().replace("/", "_").replace(" ", "_").replace("-", "_"),
                    "label": group,
                    "module_type": "TRANSPORT_STEP",
                    "description": f"First-pass monovalent-cation transport subgroup: {group}.",
                    "annotons": annotons,
                },
            }
        )

    doc = {
        "id": "MODULE:monovalent_cation_antiporter_boundary",
        "title": "Monovalent cation antiporters and potassium systems boundary",
        "description": (
            "Boundary module for the PSEPK transport ion/metal monovalent-cation sub-batch. "
            "The set contains Trk/Kup potassium uptake context, NhaA/NhaB/NhaP and Kef/CPA-family cation/proton antiporters, "
            "a six-gene Mrp multicomponent antiporter locus, potassium/calcium/channel candidates, and two conservative side candidates."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_ion_metal_monovalent_cation_antiporters_potassium_systems.tsv",
                "title": "PSEPK transport ion/metal monovalent-cation antiporter batch",
                "statement": "The partition groups 26 PSEPK ion/metal-bucket genes for first-pass curation of sodium, potassium, proton, and related monovalent-cation transport context.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_ion_metal_partition.tsv",
                "title": "PSEPK transport ion/metal sub-bucket partition",
                "statement": "The deeper ion/metal partition separates monovalent-cation systems from metal ATPases, transition-metal transporters, redox spillovers, and membrane metalloenzyme side nodes.",
            },
        ],
        "notes": (
            "First-pass interpretation: keep substrate and direction conservative. TrkA is treated as a regulatory/RCK subunit rather than a pore-forming transporter; "
            "Mrp components are modeled as subunits of a multicomponent antiporter; yfbS is DASS-related and may route better with sodium/anion solute symporters after deeper evidence review."
        ),
        "module": {
            "id": "monovalent_cation_antiporter_boundary",
            "label": "Monovalent cation antiporters and potassium systems boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                descriptor(go_id, "Concept used for first-pass monovalent-cation transport curation.")
                for go_id in concept_ids
            ],
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
