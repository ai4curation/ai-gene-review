#!/usr/bin/env python3
"""First-pass curation for transition-metal, magnesium, and cobalt transporters."""

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
    "module_transport_membrane_efflux_ion_metal_transition_metal_magnesium_cobalt_transporters.tsv"
)
MODULE_PATH = ROOT / "modules/transition_metal_magnesium_cobalt_transport_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on inter-ontology links",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0000041": "transition metal ion transport",
    "GO:0000287": "magnesium ion binding",
    "GO:0005385": "zinc ion transmembrane transporter activity",
    "GO:0005886": "plasma membrane",
    "GO:0006812": "monoatomic cation transport",
    "GO:0006824": "cobalt ion transport",
    "GO:0006882": "intracellular zinc ion homeostasis",
    "GO:0008324": "monoatomic cation transmembrane transporter activity",
    "GO:0010045": "response to nickel cation",
    "GO:0015086": "cadmium ion transmembrane transporter activity",
    "GO:0015087": "cobalt ion transmembrane transporter activity",
    "GO:0015093": "ferrous iron transmembrane transporter activity",
    "GO:0015095": "magnesium ion transmembrane transporter activity",
    "GO:0015099": "nickel cation transmembrane transporter activity",
    "GO:0015341": "zinc efflux antiporter activity",
    "GO:0016020": "membrane",
    "GO:0030001": "metal ion transport",
    "GO:0032025": "response to cobalt ion",
    "GO:0034755": "iron ion transmembrane transport",
    "GO:0035444": "nickel cation transmembrane transport",
    "GO:0046583": "monoatomic cation efflux transmembrane transporter activity",
    "GO:0046872": "metal ion binding",
    "GO:0046873": "metal ion transmembrane transporter activity",
    "GO:0050660": "flavin adenine dinucleotide binding",
    "GO:0050897": "cobalt ion binding",
    "GO:0055085": "transmembrane transport",
    "GO:0070574": "cadmium ion transmembrane transport",
    "GO:0071577": "zinc ion transmembrane transport",
    "GO:0098655": "monoatomic cation transmembrane transport",
    "GO:1903830": "magnesium ion transmembrane transport",
}

PROFILE = {
    "PP_0026": {
        "class": "cdf_zinc",
        "group": "CDF/ZIP zinc and mixed-metal transporters",
        "primary": "GO:0005385",
        "processes": ["GO:0071577"],
        "locations": ["GO:0005886"],
        "description": "PP_0026 encodes a CDF/SLC30A-family cobalt/cadmium/zinc exporter candidate, curated at first pass as a membrane zinc/mixed-metal transporter.",
    },
    "PP_0629": {
        "class": "cbim",
        "group": "CbiM/CbtA cobalt transporter components",
        "primary": "GO:0015087",
        "contributes": True,
        "processes": ["GO:0006824"],
        "locations": ["GO:0005886"],
        "description": "PP_0629 encodes a CbiM/NikMN-family cobalt transport protein, likely a membrane component of a cobalt or transition-metal uptake system.",
    },
    "PP_0683": {
        "class": "low_cation",
        "group": "Low-information cation transporter candidates",
        "primary": "GO:0008324",
        "processes": ["GO:0006812"],
        "locations": [],
        "description": "PP_0683 encodes a low-information cation transporter candidate with DUF6482 domain evidence and unresolved substrate specificity.",
    },
    "PP_0947": {
        "class": "zip_zinc",
        "group": "CDF/ZIP zinc and mixed-metal transporters",
        "primary": "GO:0005385",
        "processes": ["GO:0071577"],
        "locations": ["GO:0005886"],
        "description": "PP_0947 encodes a ZIP-family membrane metal transporter with zinc-transporter annotations.",
    },
    "PP_1227": {
        "class": "cdf_fief",
        "group": "CDF/ZIP zinc and mixed-metal transporters",
        "primary": "GO:0008324",
        "processes": ["GO:0098655"],
        "locations": ["GO:0005886"],
        "description": "PP_1227 encodes a FieF-like CDF membrane protein, curated conservatively as a monoatomic cation transporter because transferred cadmium, iron, and zinc specificity calls are broader than the local product name.",
    },
    "PP_1836": {
        "class": "zip_zinc",
        "group": "CDF/ZIP zinc and mixed-metal transporters",
        "primary": "GO:0005385",
        "processes": ["GO:0071577"],
        "locations": ["GO:0005886"],
        "description": "PP_1836 encodes a ZIP-family membrane metal transporter with zinc-transporter annotations.",
    },
    "PP_1843": {
        "class": "cora_mg",
        "group": "CorA/MgtE magnesium-cobalt transporters",
        "primary": "GO:0015095",
        "processes": ["GO:1903830"],
        "locations": ["GO:0005886"],
        "description": "PP_1843 encodes a CorA/MIT-family Mg2+/Co2+ transporter; UniProt function supports magnesium influx as the primary first-pass role.",
    },
    "cmaX": {
        "class": "cora_broad",
        "group": "CorA/MgtE magnesium-cobalt transporters",
        "primary": "GO:0046873",
        "processes": ["GO:0055085"],
        "locations": ["GO:0005886"],
        "description": "cmaX encodes a CorA/MIT-family membrane metal transporter candidate with magnesium/cobalt-family context but unresolved physiological substrate.",
    },
    "PP_2955": {
        "class": "cora_broad",
        "group": "CorA/MgtE magnesium-cobalt transporters",
        "primary": "GO:0046873",
        "processes": ["GO:0055085"],
        "locations": ["GO:0016020"],
        "description": "PP_2955 encodes a CorA-family magnesium/cobalt transporter candidate, curated at broad metal-transporter resolution.",
    },
    "PP_2968": {
        "class": "nicot",
        "group": "NiCoT nickel/cobalt efflux and response context",
        "primary": "GO:0015099",
        "processes": ["GO:0035444", "GO:0006824"],
        "locations": ["GO:0005886"],
        "description": "PP_2968 encodes a NiCoT/RcnA-family nickel/cobalt efflux system protein.",
    },
    "cbtA": {
        "class": "cbta",
        "group": "CbiM/CbtA cobalt transporter components",
        "primary": "GO:0015087",
        "contributes": True,
        "processes": ["GO:0006824"],
        "locations": ["GO:0016020"],
        "description": "cbtA encodes a CbtA-domain cobalt transporter subunit candidate, curated as contributing to cobalt transmembrane transport.",
    },
    "PP_3928": {
        "class": "rcnb",
        "group": "NiCoT nickel/cobalt efflux and response context",
        "primary": None,
        "processes": ["GO:0010045", "GO:0032025"],
        "locations": [],
        "description": "PP_3928 encodes an RcnB-domain nickel/cobalt transporter regulator or accessory candidate, retained as nickel/cobalt response context rather than a transporter pore.",
    },
    "mgtE": {
        "class": "mgte",
        "group": "CorA/MgtE magnesium-cobalt transporters",
        "primary": "GO:0015095",
        "processes": ["GO:1903830"],
        "locations": ["GO:0005886"],
        "description": "mgtE encodes a magnesium transporter MgtE/SLC41-family membrane protein.",
    },
    "corC": {
        "class": "corc",
        "group": "CorC/CNNM-UPF0053 magnesium-cobalt transport candidates",
        "primary": "GO:0046873",
        "processes": ["GO:1903830", "GO:0006824"],
        "locations": ["GO:0005886"],
        "description": "corC encodes a UPF0053-family CorC protein implicated in magnesium and cobalt transport, with FAD/CBS-domain context retained as non-core.",
    },
    "PP_5322": {
        "class": "cnnm_upf0053",
        "group": "CorC/CNNM-UPF0053 magnesium-cobalt transport candidates",
        "primary": "GO:0046873",
        "processes": ["GO:0030001"],
        "locations": ["GO:0016020"],
        "description": "PP_5322 encodes a CNNM/UPF0053-domain metal ion transporter candidate with unresolved exact cation substrate.",
    },
}

DOMAIN_NEEDLES = {
    "PP_0026": ["Cobalt/cadmium/zinc exporter", "cation diffusion facilitator", "CDF/SLC30A"],
    "PP_0629": ["Cobalt transport protein CbiM", "CbiM/NikMN", "CbiM"],
    "PP_0683": ["Cation transporter", "DUF6482"],
    "PP_0947": ["ZIP family metal transporter", "ZIP transporter", "IPR003689"],
    "PP_1227": ["FieF-like", "Cation_efflux", "PF01545"],
    "PP_1836": ["Metal transporter, ZIP family", "ZIP transporter", "IPR003689"],
    "PP_1843": ["Mg2+/Co2+ transporter", "Mediates influx of magnesium ions", "CorA metal ion transporter"],
    "cmaX": ["CmaX protein", "CorA metal ion transporter", "MgTranspt_CorA"],
    "PP_2955": ["Magnesium/cobalt transporter, CorA family", "CorA metal ion transporter", "CorA-like"],
    "PP_2968": ["Nickel/cobalt efflux system", "Efflux system for nickel and cobalt", "NiCoT transporter"],
    "cbtA": ["Cobalt transporter subunit A", "CbtA_put", "CbtA"],
    "PP_3928": ["Nickel/cobalt transporter regulator", "RcnB"],
    "mgtE": ["Magnesium transporter MgtE", "Acts as a magnesium transporter", "MgtE_transporter"],
    "corC": ["Magnesium and cobalt efflux protein CorC", "transport of magnesium and cobalt ions", "CorC_N"],
    "PP_5322": ["Metal ion transporter", "CNNM", "UPF0053_domain"],
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
    gene = info["gene"]
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]
    cls = info["profile"]["class"]

    if go_id == "GO:0005886":
        return review(info, "Plasma membrane localization is appropriate for this bacterial membrane transporter or candidate.", "ACCEPT", "UniProt/GOA subcellular evidence supports membrane localization.")
    if go_id == "GO:0016020":
        if "GO:0005886" in info["go_ids"]:
            return review(info, "Generic membrane localization is true but less informative than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "A more specific plasma-membrane annotation is present.")
        return review(info, "Membrane localization is appropriate for this transporter-family protein.", "ACCEPT", "UniProt membrane/transmembrane evidence supports membrane localization.")
    if go_id in {"GO:0006812", "GO:0055085", "GO:0098655", "GO:0030001"}:
        if info["profile"]["primary"] in {"GO:0005385", "GO:0015095", "GO:0015099", "GO:0015341", "GO:0046873"}:
            return review(info, f"{label} is true but broad relative to the supported transporter function.", "MARK_AS_OVER_ANNOTATED", "A more specific metal, magnesium, nickel, zinc, or cation transporter term captures the core function.", [info["profile"]["primary"]])
        return review(info, f"{label} is appropriate broad transporter context.", "ACCEPT", "The product and transporter-family/domain evidence support a cation transport role.")
    if go_id == "GO:0000041":
        return review(info, "Transition-metal ion transport is appropriate context for the CbiM-family cobalt transporter component.", "ACCEPT", "The CbiM/NikMN product and domain evidence support transition-metal transport context.")
    if go_id == "GO:0005385":
        return review(info, "Zinc ion transmembrane transporter activity is appropriate for this CDF/ZIP transporter context.", "ACCEPT", "Product, ZIP/CDF family, or TreeGrafter evidence supports zinc transporter activity.")
    if go_id == "GO:0071577":
        return review(info, "Zinc ion transmembrane transport is appropriate process context for this zinc transporter.", "ACCEPT", "The supported zinc transporter activity implies zinc transport across the membrane.")
    if go_id == "GO:0046873":
        return review(info, "Broad metal ion transmembrane transporter activity is appropriate at first-pass resolution.", "ACCEPT", "The product and CorA/CDF/CNNM-family evidence support metal ion transporter context while exact substrate remains unresolved.")
    if go_id == "GO:0008324":
        action = "ACCEPT" if cls in {"cdf_fief", "low_cation"} else "MARK_AS_OVER_ANNOTATED"
        reason = (
            "This is the most conservative supported transporter activity for this low-resolution CDF/cation transporter candidate."
            if action == "ACCEPT"
            else "A more specific metal transporter annotation is present."
        )
        replacement = None if action == "ACCEPT" else [info["profile"]["primary"]]
        return review(info, "Monoatomic cation transporter activity is reviewed as broad cation-transporter context.", action, reason, replacement)
    if go_id in {"GO:0015086", "GO:0015093", "GO:0015341"}:
        if cls == "cdf_fief":
            action = "ACCEPT" if go_id == "GO:0015341" else "KEEP_AS_NON_CORE"
            return review(info, f"{label} is retained as CDF/FieF substrate context.", action, "The FieF/CDF family supports metal-efflux context, but the exact cadmium, iron, and zinc substrate range is transferred and should remain conservative.")
        return review(info, f"{label} is substrate-specific context for a metal transporter.", "KEEP_AS_NON_CORE", "The broader local evidence supports metal transport, but exact substrate specificity is not the primary first-pass call.")
    if go_id in {"GO:0070574", "GO:0034755", "GO:0006882"}:
        return review(info, f"{label} is retained as non-core transferred substrate or homeostasis context.", "KEEP_AS_NON_CORE", "The FieF/CDF family supports metal-homeostasis context, but exact physiological metal specificity requires direct evidence.")
    if go_id in {"GO:0000287", "GO:0050897"}:
        return review(info, f"{label} is retained as non-core metal-binding context.", "KEEP_AS_NON_CORE", "The CorA/MIT-family transporter role is better captured by magnesium/metal transporter activity; ion binding is supporting domain context.")
    if go_id == "GO:0015087":
        if cls in {"cora_mg", "cora_broad"}:
            return review(info, "Cobalt transporter activity is plausible CorA-family substrate context.", "KEEP_AS_NON_CORE", "The product/family includes Mg2+/Co2+ context, but magnesium or broad metal transport is the safer core call.")
        return review(info, "Cobalt transporter activity is appropriate for this cobalt transporter component.", "ACCEPT", "The CbiM/CbtA product/domain evidence supports cobalt transport context.")
    if go_id == "GO:0006824":
        action = "ACCEPT" if cls in {"nicot", "cbim", "cbta"} else "KEEP_AS_NON_CORE"
        return review(info, "Cobalt ion transport is retained as cobalt or magnesium/cobalt transporter context.", action, "Product, NiCoT, CbiM/CbtA, or CorA-family evidence supports cobalt transport context, with exact role varying by family.")
    if go_id == "GO:0015095":
        return review(info, "Magnesium ion transmembrane transporter activity is appropriate for this CorA/MgtE-family transporter.", "ACCEPT", "The product/family evidence supports magnesium transmembrane transport.")
    if go_id in {"GO:0015693", "GO:1903830"}:
        return review(info, f"{label} is appropriate magnesium transport process context.", "ACCEPT", "The supported magnesium transporter activity implies magnesium movement across the membrane.")
    if go_id == "GO:0046872":
        return review(info, "Metal ion binding is retained as supporting non-core context for MgtE.", "KEEP_AS_NON_CORE", "The core function is magnesium transmembrane transporter activity; metal binding is accessory/domain context.")
    if go_id == "GO:0015099":
        return review(info, "Nickel cation transporter activity is appropriate for the NiCoT/RcnA efflux protein.", "ACCEPT", "The NiCoT/RcnA product and UniProt evidence support nickel/cobalt efflux context.")
    if go_id == "GO:0046583":
        return review(info, "Generic cation efflux transporter activity is true but less specific than nickel transporter context.", "KEEP_AS_NON_CORE", "The NiCoT/RcnA product supports nickel/cobalt efflux, with nickel transporter activity as the more specific molecular function.")
    if go_id == "GO:0035444":
        return review(info, "Nickel cation transmembrane transport is appropriate process context for the NiCoT/RcnA efflux protein.", "ACCEPT", "The nickel transporter activity supports nickel movement across the membrane.")
    if go_id in {"GO:0010045", "GO:0032025"}:
        return review(info, f"{label} is appropriate metal-stress response context for NiCoT/RcnA or RcnB-family proteins.", "ACCEPT", "The product/family evidence supports nickel/cobalt efflux or response context.")
    if go_id == "GO:0050660":
        if cls in {"corc", "cnnm_upf0053"}:
            return review(info, "FAD binding is retained as non-core UPF0053/FAD-domain context.", "KEEP_AS_NON_CORE", "The transport-related product/domain evidence supports metal transporter context as the main role; FAD binding is a domain property.")
        return review(info, "FAD binding is not the core transporter function.", "KEEP_AS_NON_CORE", "The core role is transport-related rather than cofactor binding.")

    raise ValueError(f"No review rule for {gene} {go_id} {label}")


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
    gene = info["gene"]
    go_ids = set(info["go_ids"])
    out: list[dict[str, Any]] = []
    primary = info["profile"].get("primary")
    if primary and primary not in go_ids:
        qualifier = "contributes_to" if info["profile"].get("contributes") else "enables"
        out.append(
            new_annotation(
                info,
                primary,
                qualifier,
                f"Adds {TERMS[primary]} for the transporter-family candidate.",
                "The product, UniProt context, and local domain evidence support this first-pass transporter assignment.",
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
                    "The product and transporter-family context support this conservative biological-process annotation.",
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
                    "The UniProt record supports membrane/transmembrane localization.",
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
        if profile.get("contributes"):
            core["contributes_to_molecular_function"] = term(primary)
        else:
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
    for slot in ("molecular_function", "contributes_to_molecular_function"):
        if slot in core and core[slot]["id"] not in reflected_ids:
            core.pop(slot)
    for slot in ("directly_involved_in", "locations"):
        if slot in core:
            core[slot] = [item for item in core[slot] if item["id"] in reflected_ids]
            if not core[slot]:
                core.pop(slot)
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "What is the exact transported metal ion, directionality, regulatory cue, and physiological condition for this transporter or accessory protein in KT2440?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure metal-dependent growth, accumulation, efflux or uptake, and complementation phenotypes under defined Zn, Cd, Fe, Mg, Co, and Ni conditions.",
            "experiment_type": "metal-transport genetics and ion accumulation assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_transition_metal_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {info['product']}",
    }
    primary = info["profile"].get("primary")
    if primary:
        if info["profile"].get("contributes"):
            annoton["function"] = {
                "preferred_term": f"contributes to {TERMS[primary]}",
                "term": term(primary),
            }
        else:
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
                    "description": f"First-pass transition-metal/magnesium/cobalt transport subgroup: {group}.",
                    "annotons": [module_annoton(info) for info in group_infos],
                },
            }
        )
    concept_ids = [
        "GO:0005385",
        "GO:0015341",
        "GO:0008324",
        "GO:0015087",
        "GO:0015095",
        "GO:0046873",
        "GO:0015099",
        "GO:0046583",
        "GO:0006824",
        "GO:0035444",
        "GO:1903830",
        "GO:0010045",
        "GO:0032025",
        "GO:0005886",
        "GO:0016020",
    ]
    doc = {
        "id": "MODULE:transition_metal_magnesium_cobalt_transport_boundary",
        "title": "Transition-metal, magnesium, and cobalt transport boundary",
        "description": (
            "Boundary module for PSEPK CDF, ZIP, CorA/MgtE, NiCoT, CbiM/CbtA, and CorC/CNNM-UPF0053 "
            "transport-family entries from the transport ion/metal split."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK transition-metal/magnesium/cobalt transporter batch",
                "statement": "The batch table records 15 PSEPK ion/metal-bucket genes assigned to transition-metal, magnesium, cobalt, nickel, zinc, and low-resolution metal-transporter context.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_ion_metal_partition.tsv",
                "title": "PSEPK transport ion/metal sub-bucket partition",
                "statement": "The deeper ion/metal partition separates this transporter-family set from P-type ATPases, monovalent-cation antiporters, redox spillovers, and membrane enzyme side nodes.",
            },
        ],
        "notes": (
            "First-pass interpretation: keep substrate calls evidence-driven. ZIP/CDF and MgtE/MIT entries keep specific metal calls where product/GOA support them; "
            "CmaX, PP_2955, CorC, PP_5322, and PP_0683 are kept broad when substrate specificity is unresolved; PP_3928 is regulatory/response context rather than a transporter pore."
        ),
        "module": {
            "id": "transition_metal_magnesium_cobalt_transport_boundary",
            "label": "Transition-metal, magnesium, and cobalt transport boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [descriptor(go_id, "Concept used for first-pass transition-metal/magnesium/cobalt transport curation.") for go_id in concept_ids],
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
