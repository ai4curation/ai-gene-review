#!/usr/bin/env python3
"""First-pass curation for transport-bucket domain-resolved membrane spillovers."""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = (
    ROOT
    / "projects/P_PUTIDA/batches/"
    "module_transport_membrane_efflux_other_domain_resolved_membrane_proteins.tsv"
)
MODULE_PATH = ROOT / "modules/transport_membrane_domain_spillover_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0003333": "amino acid transmembrane transport",
    "GO:0003676": "nucleic acid binding",
    "GO:0003677": "DNA binding",
    "GO:0003700": "DNA-binding transcription factor activity",
    "GO:0004364": "glutathione transferase activity",
    "GO:0005737": "cytoplasm",
    "GO:0005829": "cytosol",
    "GO:0005886": "plasma membrane",
    "GO:0006310": "DNA recombination",
    "GO:0006352": "DNA-templated transcription initiation",
    "GO:0006355": "regulation of DNA-templated transcription",
    "GO:0006457": "protein folding",
    "GO:0006811": "ion transport",
    "GO:0006826": "iron ion transport",
    "GO:0006865": "amino acid transport",
    "GO:0008360": "regulation of cell shape",
    "GO:0008641": "ubiquitin-like modifier activating enzyme activity",
    "GO:0009267": "cellular response to starvation",
    "GO:0015171": "amino acid transmembrane transporter activity",
    "GO:0015689": "molybdate ion transport",
    "GO:0016020": "membrane",
    "GO:0016036": "cellular response to phosphate starvation",
    "GO:0016987": "sigma factor activity",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0030001": "metal ion transport",
    "GO:0030244": "cellulose biosynthetic process",
    "GO:0030288": "outer membrane-bounded periplasmic space",
    "GO:0030313": "cell envelope",
    "GO:0030420": "establishment of competence for transformation",
    "GO:0031177": "phosphopantetheine binding",
    "GO:0031669": "cellular response to nutrient levels",
    "GO:0043041": "amino acid activation for nonribosomal peptide biosynthetic process",
    "GO:0043190": "ATP-binding cassette (ABC) transporter complex",
    "GO:0044550": "secondary metabolite biosynthetic process",
    "GO:0046873": "metal ion transmembrane transporter activity",
    "GO:0050660": "flavin adenine dinucleotide binding",
    "GO:0055085": "transmembrane transport",
    "GO:0061503": "tRNA threonylcarbamoyladenosine dehydratase activity",
    "GO:0061504": "cyclic threonylcarbamoyladenosine biosynthetic process",
    "GO:0140359": "ABC-type transporter activity",
    "GO:1901678": "iron coordination entity transport",
    "GO:2000142": "regulation of DNA-templated transcription initiation",
}

GROUP_SPECS: dict[str, dict[str, Any]] = {
    "TauE/TSUP-family transporter candidates": {
        "genes": {"PP_0054", "PP_0487", "PP_1029", "PP_1862", "PP_2244", "PP_3933", "PP_4663", "PP_5143"},
        "class": "broad_transport",
        "primary": "GO:0022857",
        "processes": ["GO:0055085"],
        "locations": ["GO:0016020"],
        "summary": "TauE/TSUP-family membrane transporter candidate with unresolved substrate.",
    },
    "AI-2E/PerM and small permease candidates": {
        "genes": {"PP_0714", "PP_1234", "PP_1667", "PP_2207", "PP_4162"},
        "class": "broad_transport",
        "primary": "GO:0022857",
        "processes": ["GO:0055085"],
        "locations": ["GO:0016020"],
        "summary": "AI-2E/PerM-family membrane permease candidate with unresolved substrate.",
    },
    "Other broad transporter-family candidates": {
        "genes": {"PP_0176", "PP_1956", "PP_2248", "PP_2787", "PP_2812", "PP_3202", "PP_3296", "PP_3561", "sdaC", "PP_3955", "yfeH", "yjiY"},
        "class": "broad_transport",
        "primary": "GO:0022857",
        "processes": ["GO:0055085"],
        "locations": ["GO:0016020"],
        "summary": "Domain-resolved membrane transporter-family candidate with unresolved substrate.",
    },
    "ABC-type permease and substrate-binding side nodes": {
        "genes": {"yadH", "PP_2667", "yhhJ", "fatB"},
        "class": "abc_component",
        "primary": "GO:0140359",
        "processes": ["GO:0055085"],
        "locations": ["GO:0016020"],
        "summary": "ABC-family transport component or substrate-binding side node.",
    },
    "Metal, TerC, GDT1, and MgtC homeostasis membrane proteins": {
        "genes": {"ygdQ", "PP_0241", "PP_0760", "alx", "PP_2445", "ureJ", "mgtC", "PP_3541", "PP_3295", "yegH"},
        "class": "metal_homeostasis",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "summary": "Domain-resolved metal, TerC/GDT1, or MgtC-family membrane-homeostasis protein.",
    },
    "Envelope, cell-shape, curli, and biofilm assembly side nodes": {
        "genes": {"mreD", "PP_1897", "fimV", "bcsG", "csgF", "PP_3474", "yccA", "yciB", "PP_5096", "atpI"},
        "class": "envelope_side_node",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "summary": "Envelope, cell-shape, curli/biofilm, or membrane-complex accessory side node.",
    },
    "Cytosolic nucleic-acid, tRNA, and transcription spillovers": {
        "genes": {"PP_0636", "PP_1209", "tcdA", "rmuC", "PP_4070"},
        "class": "cytosolic_spillover",
        "primary": None,
        "processes": [],
        "locations": [],
        "summary": "Nucleic-acid, tRNA-modification, recombination, or sigma-factor spillover pulled into the membrane bucket by weak membrane signal.",
    },
    "NRPS, RHS, and toxin/effector side nodes": {
        "genes": {"PP_2563", "PP_3788", "PP_4085", "PP_0828"},
        "class": "toxin_secondary_metabolite",
        "primary": None,
        "processes": [],
        "locations": [],
        "summary": "Secondary-metabolite, RHS/toxin, or effector side node pulled into the membrane bucket by weak membrane signal.",
    },
    "DoxX, SURF1, DedA, PAP2, MAPEG, and low-information membrane proteins": {
        "genes": {
            "PP_0107", "djlA", "PP_0621", "PP_0642", "PP_0900", "PP_0990", "PP_1149", "PP_1459",
            "PP_2029", "PP_2313", "PP_2331", "PP_2349", "PP_2380", "PP_2400", "PP_2950", "PP_3800",
            "yphA", "PP_4615", "PP_4813", "PP_4816", "PP_4833", "PP_4972", "PP_5218", "PP_5427",
            "PP_5699",
        },
        "class": "low_info_membrane",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "summary": "Domain-resolved but low-information membrane protein or side-node family.",
    },
}

OVERRIDES: dict[str, dict[str, Any]] = {
    "fatB": {"primary": None, "processes": ["GO:0006826", "GO:1901678"], "locations": ["GO:0030288", "GO:0030313"]},
    "PP_0241": {"processes": ["GO:0015689"], "locations": []},
    "PP_0760": {"primary": "GO:0046873", "processes": ["GO:0030001"]},
    "ureJ": {"primary": "GO:0046873", "processes": ["GO:0030001"]},
    "mgtC": {"processes": [], "locations": ["GO:0016020"]},
    "PP_3541": {"processes": [], "locations": ["GO:0016020"]},
    "yegH": {"processes": [], "locations": ["GO:0016020"]},
    "mreD": {"processes": ["GO:0008360"], "locations": ["GO:0005886"]},
    "PP_1897": {"processes": ["GO:0030420"], "locations": ["GO:0005886", "GO:0016020"]},
    "PP_5096": {"processes": ["GO:0008360"], "locations": ["GO:0016020"]},
    "bcsG": {"processes": ["GO:0030244"], "locations": ["GO:0016020"]},
    "PP_0636": {"primary": "GO:0003676", "locations": ["GO:0005829"]},
    "PP_1209": {"primary": "GO:0003676", "locations": ["GO:0005737", "GO:0005829"]},
    "tcdA": {"primary": "GO:0061503", "processes": ["GO:0061504"], "locations": []},
    "rmuC": {"processes": ["GO:0006310"], "locations": []},
    "PP_4070": {"primary": "GO:0016987", "processes": ["GO:0006352", "GO:0006355", "GO:2000142"], "locations": []},
    "PP_2563": {"primary": "GO:0031177", "processes": ["GO:0043041", "GO:0044550"], "locations": ["GO:0005737"]},
    "PP_3788": {"primary": "GO:0031177", "processes": ["GO:0043041", "GO:0044550"], "locations": ["GO:0005737"]},
    "PP_0828": {"processes": ["GO:0006811"], "locations": ["GO:0005886"]},
    "djlA": {"processes": ["GO:0006457"], "locations": ["GO:0016020"]},
    "PP_4972": {"primary": "GO:0004364", "locations": ["GO:0016020"]},
    "PP_4615": {"processes": ["GO:0016036"], "locations": ["GO:0005886"]},
    "PP_4813": {"primary": None, "processes": [], "locations": ["GO:0005886"]},
    "yjiY": {"processes": ["GO:0055085", "GO:0009267", "GO:0031669"]},
    "sdaC": {"primary": "GO:0015171", "processes": ["GO:0003333", "GO:0006865"], "locations": ["GO:0005886", "GO:0016020"]},
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


def profile_for(row: dict[str, str]) -> dict[str, Any]:
    gene = row["gene"]
    for group, spec in GROUP_SPECS.items():
        if gene in spec["genes"]:
            profile = {k: v for k, v in spec.items() if k != "genes"}
            profile["group"] = group
            break
    else:
        raise ValueError(f"No profile group for {gene}")
    profile.update(OVERRIDES.get(gene, {}))
    profile["description"] = (
        f"{gene} encodes {row['protein_name']}, a {profile['summary']} "
        "This first-pass review treats it as a domain-resolved transport-bucket boundary member rather than evidence for a single coherent transport pathway."
    )
    return profile


def load_info(row: dict[str, str]) -> GeneInfo:
    gene = row["gene"]
    uniprot_lines = (GENE_ROOT / gene / f"{gene}-uniprot.txt").read_text(encoding="utf-8").splitlines()
    asta_lines = (GENE_ROOT / gene / f"{gene}-deep-research-asta.md").read_text(encoding="utf-8").splitlines()
    review_doc = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text(encoding="utf-8"))
    info = GeneInfo(
        gene=gene,
        accession=row["uniprot_accession"],
        product=row["protein_name"],
        profile=profile_for(row),
        uniprot_lines=uniprot_lines,
        asta_lines=asta_lines,
        existing_refs={ref["id"]: ref for ref in review_doc.get("references", []) if "id" in ref},
    )
    info["de"] = first_de_line(uniprot_lines)
    info["asta_identity"] = first_line(asta_lines, "- **Protein Description:**")
    info["asta_domains"] = first_line(asta_lines, "- **Key Domains:**")
    info["location"] = first_line(uniprot_lines, "SUBCELLULAR LOCATION", optional=True)
    return info


def base_support(info: GeneInfo) -> list[dict[str, str]]:
    out = [
        support(ref_file(info["gene"], "uniprot.txt"), info["de"]),
        support(ref_file(info["gene"], "deep-research-asta.md"), info["asta_identity"]),
        support(ref_file(info["gene"], "deep-research-asta.md"), info["asta_domains"]),
    ]
    if info.get("location"):
        out.append(support(ref_file(info["gene"], "uniprot.txt"), info["location"]))
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


def location_review(info: GeneInfo, go_id: str) -> dict[str, Any]:
    if go_id == "GO:0005886":
        return review(info, "Plasma-membrane localization is appropriate membrane context for this domain-resolved protein.", "ACCEPT", "UniProt/GOA membrane and transmembrane evidence supports bacterial plasma-membrane context.")
    if go_id == "GO:0016020":
        if "GO:0005886" in info.get("go_ids", []):
            return review(info, "Generic membrane localization is true but less informative than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "A more specific plasma-membrane annotation is present.")
        return review(info, "Membrane localization is appropriate context for this domain-resolved membrane protein.", "ACCEPT", "UniProt membrane/transmembrane evidence supports membrane localization.")
    if go_id in {"GO:0005737", "GO:0005829"}:
        return review(info, f"{TERMS[go_id]} localization is appropriate for this cytosolic spillover annotation.", "ACCEPT", "The product/domain profile supports a cytosolic nucleic-acid, transcription, or secondary-metabolite side role.")
    if go_id in {"GO:0030288", "GO:0030313"}:
        return review(info, f"{TERMS[go_id]} localization is appropriate envelope context for this binding/transport side node.", "ACCEPT", "The product/domain profile supports a cell-envelope or periplasmic binding-protein role.")
    raise ValueError(f"Unhandled location term {go_id}")


def existing_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]
    gene = info["gene"]
    cls = info["profile"]["class"]
    primary = info["profile"].get("primary")

    if go_id in {"GO:0005886", "GO:0016020", "GO:0005737", "GO:0005829", "GO:0030288", "GO:0030313"}:
        return location_review(info, go_id)

    if go_id in {"GO:0022857", "GO:0055085"}:
        if gene == "PP_4813":
            return review(info, f"{label} is an over-propagated transporter-family call for this PAP2/DedA membrane protein.", "MARK_AS_OVER_ANNOTATED", "The available domain evidence supports PAP2/DedA membrane context but not a resolved transporter function.")
        return review(info, f"{label} is appropriate broad transporter context for this domain-resolved permease candidate.", "ACCEPT", "Product and domain evidence support a membrane transporter-family assignment while substrate remains unresolved.")

    if go_id in {"GO:0043190", "GO:0140359"}:
        return review(info, f"{label} is retained as ABC-family component context.", "ACCEPT", "The protein is an ABC-2 permease or related ABC-family component; substrate and complete partner set remain unresolved.")

    if go_id in {"GO:0015689", "GO:0030001", "GO:0046873", "GO:0006811", "GO:0006826", "GO:1901678"}:
        return review(info, f"{label} is appropriate conservative transport or ion-homeostasis context.", "ACCEPT", "Product/domain evidence supports broad ion, metal, or siderophore-associated transport context, but substrate specificity is kept conservative.")

    if go_id in {"GO:0003333", "GO:0006865", "GO:0015171"}:
        return review(info, f"{label} is appropriate for the SdaC hydroxy-amino-acid transporter.", "ACCEPT", "SdaC product/family evidence supports amino-acid transmembrane transport.")

    if go_id in {"GO:0003676", "GO:0003677", "GO:0003700", "GO:0016987"}:
        return review(info, f"{label} is appropriate for this nucleic-acid-binding or sigma-factor spillover.", "ACCEPT", "The product/domain profile supports nucleic-acid binding, transcription-factor, or sigma-factor function.")

    if go_id in {"GO:0006352", "GO:0006355", "GO:2000142"}:
        return review(info, f"{label} is appropriate transcription context for the sigma-factor protein.", "ACCEPT", "Sigma-factor and DNA-binding domains support transcription-initiation/regulatory context.")

    if go_id == "GO:0050660":
        return review(info, "FAD binding is retained as non-core domain/cofactor context.", "KEEP_AS_NON_CORE", "The first pass does not resolve a direct redox or transporter activity for this CBS/FAD-domain membrane protein.")

    if go_id == "GO:0008641":
        return review(info, "Ubiquitin-like modifier activating enzyme activity is over-specific family-transfer context for bacterial TcdA.", "MARK_AS_OVER_ANNOTATED", "The supported core activity is tRNA threonylcarbamoyladenosine dehydratase, not eukaryotic ubiquitin-like modifier activation.", ["GO:0061503"])
    if go_id in {"GO:0061503", "GO:0061504"}:
        return review(info, f"{label} is appropriate for TcdA.", "ACCEPT", "ThiF/TcdA family evidence supports cyclic t6A biosynthesis through tRNA threonylcarbamoyladenosine dehydratase activity.")

    if go_id in {"GO:0031177", "GO:0043041", "GO:0044550"}:
        return review(info, f"{label} is appropriate NRPS/secondary-metabolite context.", "ACCEPT", "AMP-binding and phosphopantetheine carrier-domain evidence supports nonribosomal-peptide/secondary-metabolite biosynthetic context.")

    if go_id == "GO:0008360":
        return review(info, "Regulation of cell shape is appropriate envelope context.", "ACCEPT", "MreD or shape-determination product/domain evidence supports bacterial cell-shape context.")

    if go_id in {"GO:0016036", "GO:0009267", "GO:0031669"}:
        return review(info, f"{label} is retained as condition-response context.", "ACCEPT", "Product/family annotations support starvation or phosphate-response context, while exact transport or signaling output remains unresolved.")

    if primary and go_id == primary:
        return review(info, f"{label} is appropriate for this domain-resolved family assignment.", "ACCEPT", "Product/domain evidence supports this conservative molecular-function call.")
    if go_id in info["profile"].get("processes", []):
        return review(info, f"{label} is appropriate process context for this domain-resolved family assignment.", "ACCEPT", "Product/domain evidence supports this conservative process context.")
    if cls in {"low_info_membrane", "envelope_side_node", "cytosolic_spillover", "toxin_secondary_metabolite"}:
        return review(info, f"{label} is retained only as non-core automated side context.", "KEEP_AS_NON_CORE", "The first pass does not resolve this term as the core role of the protein.")
    return review(info, f"{label} is retained as broad domain-resolved context.", "KEEP_AS_NON_CORE", "The first pass does not resolve a sharper or more confident core function.")


def new_annotation(info: GeneInfo, go_id: str, qualifier: str, summary: str, reason: str) -> dict[str, Any]:
    gene = info["gene"]
    return {
        "term": term(go_id),
        "evidence_type": "IEA",
        "original_reference_id": ref_file(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {"summary": summary, "action": "NEW", "reason": reason, "supported_by": base_support(info)},
    }


def suggested_new_annotations(info: GeneInfo) -> list[dict[str, Any]]:
    go_ids = set(info["go_ids"])
    out: list[dict[str, Any]] = []
    primary = info["profile"].get("primary")
    if primary and primary not in go_ids:
        out.append(new_annotation(info, primary, "enables", f"Adds {TERMS[primary]} for this domain-resolved boundary member.", "UniProt product/domain evidence and Asta retrieval context support this conservative first-pass assignment."))
    for process in info["profile"].get("processes", []):
        if process not in go_ids:
            out.append(new_annotation(info, process, "involved_in", f"Adds {TERMS[process]} process context.", "The supported product, family, or domain context implies this conservative process annotation."))
    for location in info["profile"].get("locations", []):
        if location not in go_ids:
            out.append(new_annotation(info, location, "located_in", f"Adds {TERMS[location]} localization context.", "UniProt membrane, compartment, or transmembrane evidence supports this localization."))
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
        "findings": [{"supporting_text": info["asta_identity"]}, {"supporting_text": info["asta_domains"]}],
    }
    return list(refs.values())


def core_function(info: GeneInfo) -> dict[str, Any]:
    profile = info["profile"]
    core: dict[str, Any] = {"description": profile["description"], "supported_by": base_support(info)}
    if profile.get("primary"):
        core["molecular_function"] = term(profile["primary"])
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
        if not (ann.get("original_reference_id") == ref_file(gene, "uniprot.txt") and (ann.get("review") or {}).get("action") == "NEW")
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
    reflected_ids = {ann["term"]["id"] for ann in doc["existing_annotations"] if (ann.get("review") or {}).get("action") in {"ACCEPT", "NEW"}}
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
        {"question": "What is the direct substrate, partner system, localization, and physiological condition for this KT2440 domain-resolved membrane or spillover protein?"}
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Test targeted mutants and tagged proteins for membrane localization, partner-system dependence, substrate specificity, and condition-specific transport, envelope, biofilm, stress, or transcriptional phenotypes as appropriate.",
            "experiment_type": "domain-guided membrane protein genetics and localization",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    safe_gene = re.sub(r"[^A-Za-z0-9_]+", "_", gene)
    annoton: dict[str, Any] = {
        "id": f"{safe_gene}_domain_resolved_membrane_context",
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


def node_id(group: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", group.lower()).strip("_")


def concept_ids_from_module(doc: dict[str, Any]) -> set[str]:
    return {
        concept.get("term", {}).get("id")
        for concept in doc.get("module", {}).get("concepts", [])
        if concept.get("term", {}).get("id")
    }


def remove_current_annotons(doc: dict[str, Any], genes: set[str]) -> None:
    for part in doc.get("module", {}).get("parts", []):
        node = part.get("node", {})
        node["annotons"] = [
            annoton
            for annoton in node.get("annotons", [])
            if annoton.get("participant", {}).get("gene", {}).get("preferred_term") not in genes
        ]


def normalize_term_labels(value: Any) -> None:
    if isinstance(value, dict):
        term_id = value.get("id")
        if term_id in TERMS and "label" in value:
            value["label"] = TERMS[term_id]
        nested_term = value.get("term")
        if isinstance(nested_term, dict):
            nested_id = nested_term.get("id")
            if nested_id in TERMS:
                nested_term["label"] = TERMS[nested_id]
                if "preferred_term" in value:
                    value["preferred_term"] = TERMS[nested_id]
        for child in value.values():
            normalize_term_labels(child)
    elif isinstance(value, list):
        for item in value:
            normalize_term_labels(item)


def initial_module() -> dict[str, Any]:
    return {
        "id": "MODULE:transport_membrane_domain_spillover_boundary",
        "title": "Transport-bucket domain-resolved membrane protein boundary",
        "description": "",
        "status": "DRAFT",
        "evidence": [],
        "notes": "",
        "module": {
            "id": "transport_membrane_domain_spillover_boundary",
            "label": "Transport-bucket domain-resolved membrane protein boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [],
            "parts": [],
        },
    }


def build_module(infos: list[GeneInfo]) -> None:
    doc = yaml.safe_load(MODULE_PATH.read_text(encoding="utf-8")) if MODULE_PATH.exists() else initial_module()
    genes = {info["gene"] for info in infos}
    remove_current_annotons(doc, genes)
    parts = doc.setdefault("module", {}).setdefault("parts", [])
    group_to_part = {part.get("role", ""): part for part in parts}
    next_order = max((part.get("order", 0) for part in parts), default=0) + 1
    grouped: dict[str, list[GeneInfo]] = defaultdict(list)
    for info in infos:
        grouped[info["profile"]["group"]].append(info)
    for group, group_infos in grouped.items():
        if group in group_to_part:
            part = group_to_part[group]
        else:
            part = {
                "order": next_order,
                "role": group,
                "node": {
                    "id": node_id(group),
                    "label": group,
                    "module_type": "TRANSPORT_STEP",
                    "description": f"First-pass domain-resolved membrane subgroup: {group}.",
                    "annotons": [],
                },
            }
            next_order += 1
            parts.append(part)
        part.setdefault("node", {}).setdefault("annotons", []).extend(module_annoton(info) for info in group_infos)
    needed_concepts = {
        go_id
        for info in infos
        for go_id in ([info["profile"].get("primary")] + info["profile"].get("processes", []) + info["profile"].get("locations", []))
        if go_id
    }
    existing_concepts = concept_ids_from_module(doc)
    concepts = doc.setdefault("module", {}).setdefault("concepts", [])
    for go_id in sorted(needed_concepts - existing_concepts):
        concepts.append(descriptor(go_id, "Concept used for first-pass domain-resolved membrane protein boundary curation."))
    source_id = f"file:{BATCH_PATH.relative_to(ROOT)}"
    evidence = doc.setdefault("evidence", [])
    if not any(item.get("source_id") == source_id for item in evidence):
        evidence.append(
            {
                "source_id": source_id,
                "title": "PSEPK transport-bucket other domain-resolved membrane protein batch",
                "statement": "The batch table records 83 PSEPK transport/membrane/efflux-bucket genes with domain or family signal but no compact transport, secretion, redox, envelope, stress, or enzyme bucket.",
            }
        )
    doc["description"] = (
        "Boundary module for PSEPK domain-resolved membrane proteins and spillovers pulled into transport buckets by membrane, "
        "transport, or weak family/domain signal. It separates broad transporter-family candidates, isolated ABC/permease pieces, "
        "metal/TerC/GDT1/MgtC homeostasis proteins, envelope and curli/cell-shape side nodes, cytosolic nucleic-acid/tRNA/"
        "transcription spillovers, NRPS/RHS/toxin side nodes, and low-information DoxX/SURF1/DedA/PAP2/MAPEG membrane proteins."
    )
    doc["notes"] = (
        "First-pass interpretation: keep this as a boundary/spillover module rather than a satisfiable transport pathway. "
        "Broad transporter activity is retained only where product/domain evidence supports a transporter-family call. "
        "Isolated ABC permeases and binding proteins are treated as component-level context with unresolved partners/substrates. "
        "Cytosolic tRNA, sigma-factor, cold-shock, NRPS, and recombination proteins are retained as spillovers, and low-information "
        "membrane-domain proteins are not promoted to unsupported pathway or substrate-specific functions."
    )
    normalize_term_labels(doc)
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    infos = [curate_gene(row) for row in load_rows()]
    build_module(infos)
    print(f"Curated {len(infos)} genes")
    print(f"Wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
