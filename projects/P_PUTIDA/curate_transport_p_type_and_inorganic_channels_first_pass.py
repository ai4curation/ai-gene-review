#!/usr/bin/env python3
"""First-pass curation for P-type metal ATPases and inorganic ion channels."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_DIR = ROOT / "projects/P_PUTIDA/batches"
P_TYPE_BATCH = BATCH_DIR / "module_transport_membrane_efflux_ion_metal_p_type_metal_atpases.tsv"
INORG_BATCH = BATCH_DIR / "module_transport_membrane_efflux_ion_metal_chromate_fluoride_and_other_inorganic_channels.tsv"
P_TYPE_MODULE = ROOT / "modules/p_type_metal_atpase_transport_boundary.yaml"
INORG_MODULE = ROOT / "modules/inorganic_ion_channel_resistance_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000003": "Gene Ontology annotation based on Enzyme Commission mapping",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on inter-ontology links",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0000166": "nucleotide binding",
    "GO:0005507": "copper ion binding",
    "GO:0005524": "ATP binding",
    "GO:0005886": "plasma membrane",
    "GO:0006812": "monoatomic cation transport",
    "GO:0015086": "cadmium ion transmembrane transporter activity",
    "GO:0015109": "chromate transmembrane transporter activity",
    "GO:0015444": "P-type magnesium transporter activity",
    "GO:0015662": "P-type ion transporter activity",
    "GO:0015693": "magnesium ion transport",
    "GO:0015703": "chromate transport",
    "GO:0016020": "membrane",
    "GO:0016463": "P-type zinc transporter activity",
    "GO:0016887": "ATP hydrolysis activity",
    "GO:0019829": "ATPase-coupled monoatomic cation transmembrane transporter activity",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0030001": "metal ion transport",
    "GO:0035434": "copper ion transmembrane transport",
    "GO:0043682": "P-type divalent copper transporter activity",
    "GO:0046872": "metal ion binding",
    "GO:0046915": "transition metal ion transmembrane transporter activity",
    "GO:0055070": "copper ion homeostasis",
    "GO:0055085": "transmembrane transport",
    "GO:0060003": "copper ion export",
    "GO:0062054": "fluoride channel activity",
    "GO:0070574": "cadmium ion transmembrane transport",
    "GO:0071577": "zinc ion transmembrane transport",
    "GO:0098655": "monoatomic cation transmembrane transport",
    "GO:0140114": "cellular detoxification of fluoride",
    "GO:0140581": "P-type monovalent copper transporter activity",
    "GO:0140911": "pore-forming activity",
    "GO:1903424": "fluoride transmembrane transport",
    "GO:1903425": "fluoride transmembrane transporter activity",
    "GO:1903830": "magnesium ion transmembrane transport",
}

PROFILE = {
    "cadA-I": {
        "class": "p_type_zinc",
        "group": "Type IB zinc/cadmium-export ATPases",
        "primary_mf": "GO:0016463",
        "processes": ["GO:0071577"],
        "description": "cadA-I encodes a type-IB P-type ATPase predicted to export Zn(2+) across the cytoplasmic membrane.",
    },
    "cadA-II": {
        "class": "p_type_copper",
        "group": "Copper-associated type IB P-type ATPases",
        "primary_mf": "GO:0140581",
        "processes": ["GO:0060003", "GO:0055070"],
        "description": "cadA-II encodes a type-IB P-type copper ATPase predicted to export Cu(+) and contribute to copper homeostasis.",
    },
    "mgtA": {
        "class": "p_type_magnesium",
        "group": "P-type magnesium ATPase",
        "primary_mf": "GO:0015444",
        "processes": ["GO:1903830"],
        "description": "mgtA encodes a type-IIIB P-type magnesium ATPase predicted to import Mg(2+) across the inner membrane.",
    },
    "PP_4261": {
        "class": "p_type_copper_candidate",
        "group": "Copper-associated type IB P-type ATPases",
        "primary_mf": "GO:0015662",
        "processes": [],
        "description": "PP_4261 encodes a type-IB cation-transporting P-type ATPase with HMA/copper-associated domain evidence, but its exact transported metal and valence remain unresolved.",
    },
    "cadA-III": {
        "class": "p_type_zinc",
        "group": "Type IB zinc/cadmium-export ATPases",
        "primary_mf": "GO:0016463",
        "processes": ["GO:0071577"],
        "description": "cadA-III encodes a type-IB P-type ATPase predicted to export Zn(2+), with possible cadmium-transport context from phylogenetic transfer.",
    },
    "PP_2556": {
        "class": "chromate",
        "group": "Chromate resistance transporter",
        "primary_mf": "GO:0015109",
        "processes": ["GO:0015703"],
        "description": "PP_2556 encodes a CHR-family chromate transporter predicted to support chromate efflux or resistance at the membrane.",
    },
    "fluC": {
        "class": "fluoride",
        "group": "Fluoride detoxification channel",
        "primary_mf": "GO:0062054",
        "processes": ["GO:0140114", "GO:1903424"],
        "description": "fluC encodes a reviewed FluC/CrcB-family fluoride channel that lowers intracellular fluoride by fluoride export across the inner membrane.",
    },
    "PP_4986": {
        "class": "hlyiii",
        "group": "HlyIII-family pore-forming candidate",
        "primary_mf": "GO:0140911",
        "processes": [],
        "description": "PP_4986 encodes an HlyIII/UPF0073-family membrane protein with family-level pore-forming/channel evidence but unresolved physiological substrate or role.",
    },
}

DOMAIN_NEEDLES = {
    "cadA-I": ["CATALYTIC ACTIVITY", "Reaction=Zn(2+)(in)", "Type IB subfamily", "Cation_Transport_ATPase_IB"],
    "cadA-II": ["P-type Cu(+)", "HMA_Cu_ion-bd", "P-typ_ATPase_IB", "Copper transport"],
    "mgtA": ["Reaction=Mg(2+)(out)", "Type IIIB subfamily", "P-type_ATPase_IIIB"],
    "PP_4261": ["Cation-transporting P-type ATPase", "HMA_dom", "P-typ_ATPase_IB"],
    "cadA-III": ["CATALYTIC ACTIVITY", "Reaction=Zn(2+)(in)", "P-typ_ATPase_IB", "HMA_dom"],
    "PP_2556": ["Chromate transporter", "chromate ion transporter", "Chromate_transpt"],
    "fluC": ["Fluoride-specific ion channel", "Reaction=fluoride(in)", "FluC/FEX", "CRCB"],
    "PP_4986": ["Channel protein, hemolysin III family", "UPF0073", "Hy-lIII"],
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


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open() as handle:
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


def has_specific_p_type(info: GeneInfo) -> bool:
    return info["profile"]["class"] in {"p_type_zinc", "p_type_copper", "p_type_magnesium"}


def p_type_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    gene = info["gene"]
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]
    profile_class = info["profile"]["class"]

    if go_id == "GO:0000166":
        return review(
            info,
            "Nucleotide binding is true but too broad for a P-type ATPase transporter.",
            "MARK_AS_OVER_ANNOTATED",
            "ATP binding, ATP hydrolysis, and P-type transporter terms capture the relevant nucleotide-dependent transport function more informatively.",
            ["GO:0005524", "GO:0015662"],
        )
    if go_id == "GO:0005524":
        return review(info, "ATP binding is part of the P-type ATPase transport cycle.", "ACCEPT", "The P-type ATPase domain architecture supports ATP-dependent cation transport.")
    if go_id == "GO:0016887":
        return review(info, "ATP hydrolysis activity is part of the P-type ATPase transport cycle.", "ACCEPT", "The P-type ATPase catalytic domains support ATP hydrolysis coupled to transport.")
    if go_id == "GO:0005886":
        return review(info, "Plasma membrane localization is appropriate for this bacterial membrane transporter.", "ACCEPT", "The UniProt subcellular-location evidence supports cell/inner-membrane localization.")
    if go_id == "GO:0016020":
        return review(info, "Generic membrane localization is true but less informative than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "A more specific bacterial plasma-membrane annotation is present.")
    if go_id in {"GO:0006812", "GO:0030001", "GO:0055085", "GO:0098655", "GO:0022857"}:
        action = "MARK_AS_OVER_ANNOTATED" if has_specific_p_type(info) else "ACCEPT"
        reason = (
            "A more specific P-type metal transporter annotation captures the core transport function."
            if action == "MARK_AS_OVER_ANNOTATED"
            else "The current evidence supports a P-type cation-transporter role, but the exact transported metal remains unresolved."
        )
        replacement = [info["profile"]["primary_mf"]] if action == "MARK_AS_OVER_ANNOTATED" else None
        return review(info, f"{label} is broad transport context.", action, reason, replacement)
    if go_id in {"GO:0015662", "GO:0019829"}:
        return review(info, f"{label} is an appropriate P-type ATPase transporter activity.", "ACCEPT", "The conserved P-type ATPase transport domains support ATPase-coupled cation transport.")
    if go_id in {"GO:0046872", "GO:0005507"}:
        action = "ACCEPT" if profile_class in {"p_type_copper", "p_type_copper_candidate"} or go_id == "GO:0046872" else "KEEP_AS_NON_CORE"
        return review(info, f"{label} is consistent with the metal-binding P-type ATPase domain context.", action, "Metal-binding/HMA or transporter-family evidence supports metal association, although the transported substrate is captured by the transporter terms.")
    if go_id == "GO:0016463":
        return review(info, "P-type zinc transporter activity is the supported specific function for this CadA-family ATPase.", "ACCEPT", "The UniProt catalytic activity and type-IB cation ATPase family evidence support ATP-dependent zinc export.")
    if go_id == "GO:0071577":
        return review(info, "Zinc ion transmembrane transport is appropriate for this zinc-exporting P-type ATPase.", "ACCEPT", "The supported P-type zinc transporter activity implies zinc movement across the membrane.")
    if go_id == "GO:0015086":
        return review(info, "Cadmium transporter activity is plausible type-IB CadA-family context but not the primary UniProt substrate call.", "KEEP_AS_NON_CORE", "The reviewed first-pass core keeps zinc transport as primary; cadmium transport remains a plausible transferred substrate context.")
    if go_id == "GO:0070574":
        return review(info, "Cadmium transmembrane transport is plausible side substrate context for cadA-III.", "KEEP_AS_NON_CORE", "CadA-family ATPases often carry heavy-metal context, but the UniProt catalytic activity in this record is zinc export.")
    if go_id == "GO:0015444":
        return review(info, "P-type magnesium transporter activity is the supported specific function for MgtA.", "ACCEPT", "The UniProt catalytic activity and type-IIIB P-type ATPase family evidence support ATP-dependent magnesium transport.")
    if go_id in {"GO:0015693", "GO:1903830"}:
        return review(info, f"{label} is appropriate magnesium transport context for MgtA.", "ACCEPT", "The P-type magnesium transporter activity supports magnesium movement across the membrane.")
    if go_id == "GO:0140581":
        return review(info, "P-type monovalent copper transporter activity is the supported specific function for cadA-II.", "ACCEPT", "The UniProt EC/name and HMA/copper-associated domains support ATP-dependent Cu(+) transport.")
    if go_id == "GO:0043682":
        if gene == "cadA-II":
            return review(info, "Divalent copper transporter activity conflicts with the Cu(+) transporter call in UniProt.", "MODIFY", "The specific UniProt EC/name supports monovalent copper transport; keep copper ATPase context but use the monovalent term.", ["GO:0140581"])
        return review(info, "Divalent copper transporter activity is too specific for PP_4261 at first-pass resolution.", "MODIFY", "PP_4261 is a type-IB P-type ATPase with HMA/copper-associated evidence, but exact substrate valence is unresolved.", ["GO:0015662"])
    if go_id == "GO:0046915":
        return review(info, "Transition-metal transporter activity is broad but consistent with type-IB metal ATPase context.", "KEEP_AS_NON_CORE", "The more specific copper ATPase term captures the core function for cadA-II.")
    if go_id == "GO:0060003":
        return review(info, "Copper ion export is appropriate process context for the Cu(+) P-type ATPase.", "ACCEPT", "The P-type copper transporter activity supports ATP-dependent copper export.")
    if go_id == "GO:0055070":
        action = "ACCEPT" if gene == "cadA-II" else "KEEP_AS_NON_CORE"
        return review(info, "Copper ion homeostasis is retained as physiological context.", action, "Copper/cation ATPase evidence supports a copper-homeostasis role, but exact substrate resolution is weaker for PP_4261 than for cadA-II.")
    if go_id == "GO:0035434":
        return review(info, "Copper transmembrane transport is plausible for PP_4261 but exact substrate specificity is unresolved.", "KEEP_AS_NON_CORE", "HMA/copper-associated TreeGrafter evidence supports copper context; the first-pass core remains broader P-type ion transporter activity.")

    raise ValueError(f"No P-type review rule for {gene} {go_id} {label}")


def inorganic_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    gene = info["gene"]
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]

    if go_id == "GO:0005886":
        return review(info, "Plasma membrane localization is appropriate for this bacterial membrane channel/transporter.", "ACCEPT", "The UniProt subcellular-location evidence supports membrane localization.")
    if go_id == "GO:0016020":
        if "GO:0005886" in info["go_ids"]:
            return review(info, "Generic membrane localization is true but less informative than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "A more specific plasma-membrane localization annotation is present.")
        return review(info, "Membrane localization is appropriate for this predicted channel candidate.", "ACCEPT", "The UniProt record supports membrane/transmembrane context.")
    if go_id == "GO:0015109":
        return review(info, "Chromate transmembrane transporter activity is the supported function for PP_2556.", "ACCEPT", "The CHR-family product/domain evidence supports chromate transport.")
    if go_id == "GO:0015703":
        return review(info, "Chromate transport is appropriate biological-process context for PP_2556.", "ACCEPT", "The chromate transporter activity supports chromate movement across the membrane.")
    if go_id == "GO:0062054":
        return review(info, "Fluoride channel activity is the supported core function for FluC.", "ACCEPT", "The reviewed UniProt FluC entry supports a fluoride-specific channel activity.")
    if go_id == "GO:0140114":
        return review(info, "Cellular detoxification of fluoride is appropriate process context for FluC.", "ACCEPT", "FluC-mediated fluoride export lowers intracellular fluoride toxicity.")
    if go_id in {"GO:1903424", "GO:1903425"}:
        return review(info, f"{label} is appropriate fluoride transport context for FluC.", "ACCEPT", "The reviewed FluC record supports fluoride-specific transmembrane channel function.")
    if go_id == "GO:0140911":
        return review(info, "Pore-forming activity is retained as family-supported candidate function for PP_4986.", "ACCEPT", "The HlyIII/UPF0073 family and InterPro transfer support pore-forming/channel context, but the physiological substrate remains unresolved.")

    raise ValueError(f"No inorganic review rule for {gene} {go_id} {label}")


def references(info: GeneInfo) -> list[dict[str, Any]]:
    refs: dict[str, dict[str, Any]] = {}
    for ref_id, ref in info["existing_refs"].items():
        refs[ref_id] = ref
    for ref_id, title in GO_REF_TITLES.items():
        if ref_id in refs:
            refs[ref_id]["title"] = title
    gene = info["gene"]
    refs[ref_file(gene, "goa.tsv")] = {
        "id": ref_file(gene, "goa.tsv"),
        "title": f"QuickGO GOA annotations for {gene}",
        "findings": [],
    }
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
        "molecular_function": term(profile["primary_mf"]),
        "supported_by": base_support(info),
    }
    if profile["processes"]:
        core["directly_involved_in"] = [term(go_id) for go_id in profile["processes"]]
    if profile["class"] in {"p_type_zinc", "p_type_copper", "p_type_magnesium", "p_type_copper_candidate", "chromate", "fluoride"}:
        core["locations"] = [term("GO:0005886")]
    elif profile["class"] == "hlyiii":
        core["locations"] = [term("GO:0016020")]
    return core


def curate_gene(row: dict[str, str], review_fn) -> GeneInfo:
    info = load_info(row)
    gene = info["gene"]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    annotations = doc.get("existing_annotations", [])
    info["go_ids"] = [ann["term"]["id"] for ann in annotations]
    for ann in annotations:
        ann["review"] = review_fn(info, ann)
        ann["review"]["supported_by"].insert(0, goa_support(info, ann["term"]["id"], ann["term"]["label"]))
        ann["review"]["supported_by"] = dedupe(ann["review"]["supported_by"])
    doc["existing_annotations"] = annotations
    doc["description"] = info["profile"]["description"]
    doc["status"] = "COMPLETE"
    doc["references"] = references(info)
    reflected_ids = {
        ann["term"]["id"]
        for ann in annotations
        if (ann.get("review") or {}).get("action") in {"ACCEPT", "NEW"}
    }
    core = core_function(info)
    if core.get("molecular_function", {}).get("id") not in reflected_ids:
        core.pop("molecular_function", None)
    for slot in ("directly_involved_in", "locations"):
        if slot in core:
            core[slot] = [item for item in core[slot] if item["id"] in reflected_ids]
            if not core[slot]:
                core.pop(slot)
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    if info["profile"]["class"] == "p_type_copper_candidate":
        question = "Which metal ion and valence does PP_4261 transport in KT2440, and under which copper or heavy-metal stress conditions is it required?"
    elif info["profile"]["class"] == "hlyiii":
        question = "Does PP_4986 form a physiologically relevant pore/channel in KT2440, and what substrate or stress condition defines its role?"
    else:
        question = "What substrate specificity, directionality, and physiological stress condition best define this membrane transport protein in KT2440?"
    doc["suggested_questions"] = [{"question": question}]
    doc["suggested_experiments"] = [
        {
            "description": "Test ion- or metal-dependent growth, accumulation, and transport phenotypes in deletion and complementation strains under defined substrate stress.",
            "experiment_type": "membrane transport genetics and ion-stress assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_transport_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {info['product']}",
    }
    mf = info["profile"]["primary_mf"]
    annoton["function"] = descriptor(mf)
    if info["profile"]["processes"]:
        annoton["processes"] = [descriptor(go_id) for go_id in info["profile"]["processes"]]
    if info["profile"]["class"] in {"p_type_zinc", "p_type_copper", "p_type_magnesium", "p_type_copper_candidate", "chromate", "fluoride"}:
        annoton["locations"] = [descriptor("GO:0005886")]
    elif info["profile"]["class"] == "hlyiii":
        annoton["locations"] = [descriptor("GO:0016020")]
    return annoton


def build_module(
    infos: list[GeneInfo],
    path: Path,
    module_id: str,
    title: str,
    description: str,
    batch_path: Path,
    concepts: list[str],
    notes: str,
) -> None:
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
                    "id": group.lower().replace("/", "_").replace(" ", "_").replace("-", "_").replace("(", "").replace(")", ""),
                    "label": group,
                    "module_type": "TRANSPORT_STEP",
                    "description": f"First-pass transport subgroup: {group}.",
                    "annotons": [module_annoton(info) for info in group_infos],
                },
            }
        )
    doc = {
        "id": f"MODULE:{module_id}",
        "title": title,
        "description": description,
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{batch_path.relative_to(ROOT)}",
                "title": title + " batch",
                "statement": f"The batch table records {len(infos)} PSEPK ion/metal-bucket genes assigned to this first-pass boundary module.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_ion_metal_partition.tsv",
                "title": "PSEPK transport ion/metal sub-bucket partition",
                "statement": "The deeper ion/metal partition separates monovalent-cation systems, P-type metal ATPases, inorganic channels, transition-metal transporters, redox spillovers, and membrane metalloenzyme side nodes.",
            },
        ],
        "notes": notes,
        "module": {
            "id": module_id,
            "label": title,
            "module_type": "TRANSPORT_STEP",
            "concepts": [descriptor(go_id, "Concept used for first-pass transport curation.") for go_id in concepts],
            "parts": parts,
        },
    }
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    p_type_infos = [curate_gene(row, p_type_review) for row in load_rows(P_TYPE_BATCH)]
    inorganic_infos = [curate_gene(row, inorganic_review) for row in load_rows(INORG_BATCH)]
    build_module(
        p_type_infos,
        P_TYPE_MODULE,
        "p_type_metal_atpase_transport_boundary",
        "P-type metal ATPase transport boundary",
        "Boundary module for PSEPK type-IB and type-IIIB P-type metal ATPases in the transport ion/metal split.",
        P_TYPE_BATCH,
        [
            "GO:0005524",
            "GO:0016887",
            "GO:0015662",
            "GO:0019829",
            "GO:0016463",
            "GO:0140581",
            "GO:0015444",
            "GO:0071577",
            "GO:0060003",
            "GO:0055070",
            "GO:1903830",
            "GO:0005886",
        ],
        "First-pass interpretation: keep ATPase chemistry and membrane localization, but treat metal specificity conservatively when UniProt/product evidence does not resolve exact substrate or valence.",
    )
    build_module(
        inorganic_infos,
        INORG_MODULE,
        "inorganic_ion_channel_resistance_boundary",
        "Inorganic ion channel and resistance boundary",
        "Boundary module for chromate, fluoride, and HlyIII-family inorganic-channel/resistance entries in the PSEPK transport ion/metal split.",
        INORG_BATCH,
        [
            "GO:0015109",
            "GO:0015703",
            "GO:0062054",
            "GO:1903425",
            "GO:1903424",
            "GO:0140114",
            "GO:0140911",
            "GO:0005886",
            "GO:0016020",
        ],
        "First-pass interpretation: PP_2556 and fluC have substrate-specific chromate/fluoride support; PP_4986 is retained as an HlyIII-family pore-forming candidate with unresolved physiological substrate.",
    )
    print(f"Curated {len(p_type_infos)} P-type ATPase genes -> {P_TYPE_MODULE}")
    print(f"Curated {len(inorganic_infos)} inorganic channel genes -> {INORG_MODULE}")


if __name__ == "__main__":
    main()
