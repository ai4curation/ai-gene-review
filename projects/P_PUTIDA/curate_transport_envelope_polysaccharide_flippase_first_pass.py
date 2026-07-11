#!/usr/bin/env python3
"""First-pass curation for envelope polysaccharide/flippase transport spillovers."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = ROOT / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_envelope_polysaccharide_export_and_flippase_context.tsv"
MODULE_PATH = ROOT / "modules/envelope_polysaccharide_export_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000003": "Gene Ontology annotation based on Enzyme Commission mapping",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0000030": "mannosyltransferase activity",
    "GO:0000271": "polysaccharide biosynthetic process",
    "GO:0004713": "protein tyrosine kinase activity",
    "GO:0005886": "plasma membrane",
    "GO:0006493": "protein O-linked glycosylation",
    "GO:0008932": "lytic endotransglycosylase activity",
    "GO:0008933": "peptidoglycan lytic transglycosylase activity",
    "GO:0009103": "lipopolysaccharide biosynthetic process",
    "GO:0009243": "O antigen biosynthetic process",
    "GO:0009252": "peptidoglycan biosynthetic process",
    "GO:0010041": "response to iron(III) ion",
    "GO:0015159": "polysaccharide transmembrane transporter activity",
    "GO:0015774": "polysaccharide transport",
    "GO:0016020": "membrane",
    "GO:0016740": "transferase activity",
    "GO:0016757": "glycosyltransferase activity",
    "GO:0016758": "hexosyltransferase activity",
    "GO:0016763": "pentosyltransferase activity",
}

PROFILES: dict[str, dict[str, Any]] = {
    "PP_0033": {
        "group": "ArnT-like lipid A/LPS glycan modification",
        "description": "PP_0033 is an inner-membrane ArnT-like undecaprenyl-glycosyltransferase related to lipid A and lipopolysaccharide glycan modification.",
        "primary": "GO:0016763",
        "processes": ["GO:0009103"],
        "locations": ["GO:0005886"],
        "new": [],
    },
    "PP_0034": {
        "group": "Phage-associated bactoprenol glycosyltransferase",
        "description": "PP_0034 is a membrane GT2-family bactoprenol glycosyltransferase of phage-associated origin, consistent with lipid-linked glycan or envelope polysaccharide precursor modification.",
        "primary": "GO:0016757",
        "processes": ["GO:0000271"],
        "locations": ["GO:0005886"],
        "new": [("GO:0016757", "enables"), ("GO:0000271", "involved_in")],
    },
    "PP_0035": {
        "group": "GtrA-family bactoprenol-linked glycose handling",
        "description": "PP_0035 is a GtrA-family membrane protein associated with bactoprenol-linked glycose handling in envelope polysaccharide biosynthesis.",
        "primary": None,
        "processes": ["GO:0000271"],
        "locations": ["GO:0005886"],
        "new": [],
    },
    "yceG": {
        "group": "MltG/YceG peptidoglycan transglycosylase side node",
        "description": "YceG/MltG is an inner-membrane endolytic murein transglycosylase that terminates nascent peptidoglycan strand elongation during cell-wall synthesis.",
        "primary": "GO:0008933",
        "processes": ["GO:0009252"],
        "locations": ["GO:0005886"],
        "new": [],
    },
    "PP_3127": {
        "group": "Wzz-like polysaccharide chain-length and export context",
        "description": "PP_3127 is a Wzz/chain-length-determinant family inner-membrane protein associated with polysaccharide export and chain-length control.",
        "primary": None,
        "processes": ["GO:0015774"],
        "locations": ["GO:0005886"],
        "new": [("GO:0015774", "involved_in")],
    },
    "PP_3131": {
        "group": "O-antigen ligase-related membrane assembly context",
        "description": "PP_3131 is a membrane O-antigen ligase-related/Wzy_C-domain protein likely acting in O-antigen or related envelope polysaccharide assembly.",
        "primary": None,
        "processes": ["GO:0009243"],
        "locations": ["GO:0016020"],
        "new": [("GO:0009243", "involved_in")],
    },
    "PP_3132": {
        "group": "Polysaccharide transporter/synthase-family protein",
        "description": "PP_3132 is a membrane polysaccharide transporter/synthase-family protein associated with envelope polysaccharide translocation.",
        "primary": "GO:0015159",
        "processes": ["GO:0015774"],
        "locations": ["GO:0005886"],
        "new": [("GO:0015159", "enables"), ("GO:0015774", "involved_in")],
    },
    "PP_3135": {
        "group": "WbbL-like GT2 glycosyltransferase candidate",
        "description": "PP_3135 is a GT2-family glycosyltransferase related to WbbL/rhamnosyltransferase proteins and likely contributes to envelope glycan assembly.",
        "primary": "GO:0016757",
        "processes": ["GO:0000271"],
        "locations": [],
        "new": [("GO:0016757", "enables"), ("GO:0000271", "involved_in")],
    },
    "PP_3137": {
        "group": "Generic GT2 glycosyltransferase side candidate",
        "description": "PP_3137 is a GT2-family glycosyltransferase candidate encoded in the polysaccharide-associated locus; its specific sugar donor and acceptor are unresolved.",
        "primary": "GO:0016757",
        "processes": [],
        "locations": [],
        "new": [("GO:0016757", "enables")],
    },
    "PP_3140": {
        "group": "Generic GT2 glycosyltransferase side candidate",
        "description": "PP_3140 is a GT2-family glycosyltransferase candidate encoded in the polysaccharide-associated locus; its specific sugar donor and acceptor are unresolved.",
        "primary": "GO:0016757",
        "processes": [],
        "locations": [],
        "new": [("GO:0016757", "enables")],
    },
    "PP_3141": {
        "group": "WecB/TagA/CpsF-family glycosyltransferase",
        "description": "PP_3141 is a WecB/TagA/CpsF-family glycosyltransferase and hexosyltransferase candidate that likely contributes to envelope glycan biosynthesis.",
        "primary": "GO:0016758",
        "processes": ["GO:0000271"],
        "locations": [],
        "new": [("GO:0000271", "involved_in")],
    },
    "wzy": {
        "group": "Wzy O-antigen polymerase",
        "description": "Wzy is a membrane O-antigen polymerase/Wzy_C-domain protein involved in O-antigen biosynthesis.",
        "primary": None,
        "processes": ["GO:0009243"],
        "locations": ["GO:0016020"],
        "new": [("GO:0009243", "involved_in")],
    },
    "PP_5334": {
        "group": "UPF0410 membrane transglycosylase side candidate",
        "description": "PP_5334 is a membrane-associated UPF0410-family protein annotated as a transglycosylase; its physiological glycan substrate and pathway context are unresolved.",
        "primary": None,
        "processes": [],
        "locations": ["GO:0005886"],
        "new": [],
    },
}


class GeneInfo(dict[str, Any]):
    pass


def load_rows() -> list[dict[str, str]]:
    with BATCH_PATH.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


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


def collect_multiline_start(lines: list[str], prefix: str) -> str | None:
    for line in lines:
        if line.startswith(prefix):
            return line
    return None


def goa_rows(gene: str) -> list[dict[str, str]]:
    path = GENE_ROOT / gene / f"{gene}-goa.tsv"
    with path.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_info(row: dict[str, str]) -> GeneInfo:
    gene = row["gene"]
    profile = PROFILES[gene]
    uniprot_lines = (GENE_ROOT / gene / f"{gene}-uniprot.txt").read_text(encoding="utf-8").splitlines()
    asta_lines = (GENE_ROOT / gene / f"{gene}-deep-research-asta.md").read_text(encoding="utf-8").splitlines()
    review_doc = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text(encoding="utf-8"))
    info = GeneInfo(
        gene=gene,
        accession=row["uniprot_accession"],
        product=row["protein_name"],
        profile=profile,
        existing_refs={ref["id"]: ref for ref in review_doc.get("references", []) if "id" in ref},
    )
    info["de"] = first_de_line(uniprot_lines)
    info["asta_product"] = first_line(asta_lines, "- **Protein Description:**")
    info["asta_domains"] = first_line(asta_lines, "- **Key Domains:**")
    info["location_line"] = first_line(uniprot_lines, "SUBCELLULAR LOCATION", optional=True)
    info["similarity_line"] = first_line(uniprot_lines, "SIMILARITY", optional=True)
    info["function_line"] = collect_multiline_start(uniprot_lines, "CC   -!- FUNCTION:")
    return info


def base_support(info: GeneInfo) -> list[dict[str, str]]:
    gene = info["gene"]
    items = [
        support(ref_file(gene, "uniprot.txt"), info["de"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_product"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_domains"]),
    ]
    for optional_key in ("function_line", "similarity_line", "location_line"):
        if info.get(optional_key):
            items.append(support(ref_file(gene, "uniprot.txt"), info[optional_key]))
    return dedupe(items)


def goa_support(info: GeneInfo, go_id: str, label: str) -> dict[str, str]:
    return support(ref_file(info["gene"], "goa.tsv"), f"{go_id}\t{label}")


def review(info: GeneInfo, summary: str, action: str, reason: str, replacement_ids: list[str] | None = None) -> dict[str, Any]:
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
    profile = info["profile"]
    if go_id == "GO:0005886":
        return review(info, "Plasma membrane localization is appropriate for this membrane-associated envelope protein.", "ACCEPT", "The UniProt subcellular-location line and transmembrane/domain context support bacterial plasma/inner-membrane association.")
    if go_id == "GO:0016020":
        action = "ACCEPT" if go_id in profile.get("locations", []) and "GO:0005886" not in profile.get("locations", []) else "KEEP_AS_NON_CORE"
        reason = "The broader membrane term is appropriate localization context, but a more specific plasma-membrane row is available." if action == "KEEP_AS_NON_CORE" else "Only broad membrane localization is available for this predicted multi-pass envelope protein."
        return review(info, "Membrane localization is appropriate but broad.", action, reason)
    raise ValueError(go_id)


def existing_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    gene = info["gene"]
    go_id = ann["term"]["id"]

    if go_id in {"GO:0005886", "GO:0016020"}:
        return location_review(info, go_id)

    if gene == "PP_0033":
        if go_id == "GO:0000030":
            return review(info, "The product is an ArnT-like undecaprenyl-glycosyltransferase, but mannosyltransferase specificity is not supported.", "MODIFY", "The local product/domain evidence supports broad glycosyltransferase and pentosyltransferase/LPS-modification context, not mannose-specific transfer.", ["GO:0016763"])
        if go_id == "GO:0006493":
            return review(info, "Protein O-linked glycosylation is not the supported biological target for this bacterial membrane glycosyltransferase.", "REMOVE", "The product/domain evidence points to lipid-linked envelope glycan or lipid A/LPS modification rather than protein O-glycosylation.")
        if go_id == "GO:0009103":
            return review(info, "Lipopolysaccharide biosynthetic process is appropriate for the ArnT-like lipid A/LPS modification context.", "ACCEPT", "The ArnT-like and lipid-A-modifying glycosyltransferase domains support an LPS/lipid-A envelope glycan role.")
        if go_id == "GO:0010041":
            return review(info, "Response to iron(III) ion is a pathway-response over-propagation for this enzyme-like membrane glycosyltransferase.", "MARK_AS_OVER_ANNOTATED", "The local evidence supports a membrane glycosyltransferase role, not a direct iron-response function.")
        if go_id == "GO:0016757":
            return review(info, "Glycosyltransferase activity is true but broader than the supported pentosyltransferase/LPS-modification call.", "KEEP_AS_NON_CORE", "The broad activity is consistent with the domain evidence but is less informative than pentosyltransferase activity.")
        if go_id == "GO:0016763":
            return review(info, "Pentosyltransferase activity is appropriate for the ArnT-like lipid A/LPS modification context.", "ACCEPT", "The ArnT-like and lipid-A-modifying glycosyltransferase domains support this core activity.")

    if gene == "PP_0035" and go_id == "GO:0000271":
        return review(info, "Polysaccharide biosynthetic process is appropriate for the GtrA-family bactoprenol-linked glycose context.", "ACCEPT", "The product and GtrA-domain evidence support envelope glycan or polysaccharide biosynthesis context.")

    if gene == "yceG":
        if go_id == "GO:0008932":
            return review(info, "Lytic endotransglycosylase activity is valid but broader than the peptidoglycan-specific activity.", "KEEP_AS_NON_CORE", "The specific peptidoglycan lytic transglycosylase term captures the core molecular function.")
        if go_id == "GO:0008933":
            return review(info, "Peptidoglycan lytic transglycosylase activity is the core YceG/MltG molecular function.", "ACCEPT", "The UniProt function line and EC mapping describe endolytic cleavage of nascent peptidoglycan strands.")
        if go_id == "GO:0009252":
            return review(info, "Peptidoglycan biosynthetic process is appropriate for MltG/YceG as a peptidoglycan polymerization terminase.", "ACCEPT", "The UniProt function line describes termination of nascent peptidoglycan strand elongation.")

    if gene == "PP_3127" and go_id == "GO:0004713":
        return review(info, "Protein tyrosine kinase activity is not supported for this Wzz/chain-length-determinant protein.", "REMOVE", "The product and local domains support polysaccharide export or chain-length-determinant context, not a protein kinase catalytic domain.")

    if gene == "PP_3141":
        if go_id == "GO:0016740":
            return review(info, "Generic transferase activity is true but less informative than the hexosyltransferase row.", "KEEP_AS_NON_CORE", "The WecB/TagA/CpsF-family product and seeded GOA include the more specific hexosyltransferase activity.")
        if go_id == "GO:0016758":
            return review(info, "Hexosyltransferase activity is appropriate for this WecB/TagA/CpsF-family glycosyltransferase.", "ACCEPT", "The product, domain, and TreeGrafter evidence support a hexosyltransferase/glycan-biosynthesis role.")

    raise ValueError(f"No review rule for {gene} {go_id} {ann['term']['label']}")


def new_annotation(info: GeneInfo, go_id: str, qualifier: str) -> dict[str, Any]:
    gene = info["gene"]
    label = TERMS[go_id]
    return {
        "term": term(go_id),
        "evidence_type": "IEA",
        "original_reference_id": ref_file(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": f"Adds conservative {label} context for this envelope polysaccharide/flippase profile.",
            "action": "NEW",
            "reason": "The UniProt product, family/domain evidence, and Asta retrieval support this first-pass term, while substrate and partner specificity remain unresolved where not directly named.",
            "supported_by": base_support(info),
        },
    }


def suggested_new_annotations(info: GeneInfo) -> list[dict[str, Any]]:
    existing_ids = set(info["go_ids"])
    out: list[dict[str, Any]] = []
    for go_id, qualifier in info["profile"].get("new", []):
        if go_id not in existing_ids:
            out.append(new_annotation(info, go_id, qualifier))
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
    rows = goa_rows(gene)
    goa_ids = {row["GO TERM"] for row in rows}
    goa_annotations = [ann for ann in doc.get("existing_annotations", []) if ann["term"]["id"] in goa_ids]
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
            "question": "What precise glycan substrate, polymer, or envelope assembly partner is supported for this protein in KT2440?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Map envelope localization, glycan composition, and loss-of-function phenotypes using targeted mutants, complementation, membrane fractionation, and LPS or exopolysaccharide profiling.",
            "experiment_type": "envelope glycan genetics and biochemical profiling",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    profile = info["profile"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_envelope_polysaccharide_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {profile['group']}",
    }
    if profile.get("primary"):
        annoton["function"] = descriptor(profile["primary"])
    if profile.get("processes"):
        annoton["processes"] = [descriptor(go_id) for go_id in profile["processes"]]
    if profile.get("locations"):
        annoton["locations"] = [descriptor(go_id) for go_id in profile["locations"]]
    return annoton


def part(order: int, role: str, node_id: str, label: str, description: str, infos: list[GeneInfo], module_type: str = "METABOLIC_PATHWAY") -> dict[str, Any]:
    return {
        "order": order,
        "role": role,
        "node": {
            "id": node_id,
            "label": label,
            "module_type": module_type,
            "description": description,
            "annotons": [module_annoton(info) for info in infos],
        },
    }


def create_module(infos: list[GeneInfo]) -> None:
    by_gene = {info["gene"]: info for info in infos}
    concept_ids = [
        "GO:0016757",
        "GO:0016758",
        "GO:0016763",
        "GO:0000271",
        "GO:0009103",
        "GO:0009243",
        "GO:0015159",
        "GO:0015774",
        "GO:0008933",
        "GO:0009252",
        "GO:0005886",
        "GO:0016020",
    ]
    doc: dict[str, Any] = {
        "id": "MODULE:envelope_polysaccharide_export_boundary",
        "title": "Envelope polysaccharide export and flippase boundary",
        "description": (
            "Boundary module for the PSEPK transport/membrane/efflux envelope-polysaccharide "
            "and flippase split. The set contains lipid-linked glycan transfer proteins, "
            "O-antigen/Wzy/Wzz-like assembly context, polysaccharide transporter candidates, "
            "and peptidoglycan or low-resolution transglycosylase side nodes rather than one "
            "single satisfiable transport pathway."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK transport envelope-polysaccharide/flippase batch",
                "statement": (
                    "The transport partition routes 13 Wzy/O-antigen, exopolysaccharide, "
                    "bactoprenol/undecaprenyl-linked glycan, glycosyltransferase, and "
                    "transglycosylase genes into a boundary module for first-pass curation."
                ),
            }
        ],
        "notes": (
            "Substrate and polymer specificity are intentionally conservative. PP_3127 is treated "
            "as Wzz-like polysaccharide export/chain-length context, not protein kinase activity; "
            "yceG is peptidoglycan transglycosylase context; PP_5334 remains an unresolved "
            "UPF0410 transglycosylase side candidate."
        ),
        "module": {
            "id": "envelope_polysaccharide_export_boundary",
            "label": "Envelope polysaccharide export and flippase boundary",
            "module_type": "METABOLIC_PATHWAY",
            "concepts": [descriptor(go_id) for go_id in concept_ids],
            "context": {
                "cellular_components": [
                    descriptor("GO:0005886", "Inner/plasma membrane context for multi-pass envelope glycan proteins."),
                    descriptor("GO:0016020", "Broad membrane context when UniProt does not provide a more specific bacterial compartment."),
                ]
            },
            "parts": [
                part(
                    1,
                    "ArnT/GtrA and bactoprenol-linked glycan transfer context",
                    "lipid_linked_glycan_transfer_context",
                    "Lipid-linked glycan transfer context",
                    "PP_0033-PP_0035 capture ArnT-like, GT2, and GtrA-family membrane glycan-transfer or glycan-handling proteins.",
                    [by_gene["PP_0033"], by_gene["PP_0034"], by_gene["PP_0035"]],
                ),
                part(
                    2,
                    "Wzz/Wzy/O-antigen and polysaccharide export context",
                    "o_antigen_polysaccharide_export_context",
                    "O-antigen and polysaccharide export context",
                    "The PP_3127-PP_3141 locus separates Wzz-like chain-length/export context, Wzy/WaaL-like membrane proteins, a polysaccharide transporter, and GT2/WecB-family glycosyltransferase candidates.",
                    [
                        by_gene["PP_3127"],
                        by_gene["PP_3131"],
                        by_gene["PP_3132"],
                        by_gene["PP_3135"],
                        by_gene["PP_3137"],
                        by_gene["PP_3140"],
                        by_gene["PP_3141"],
                    ],
                ),
                part(
                    3,
                    "Wzy O-antigen polymerase singleton",
                    "wzy_o_antigen_polymerase",
                    "Wzy O-antigen polymerase",
                    "wzy is retained as O-antigen biosynthesis context with membrane localization, without asserting a more specific molecular-function term absent from the local GO cache.",
                    [by_gene["wzy"]],
                ),
                part(
                    4,
                    "Peptidoglycan and unresolved transglycosylase side nodes",
                    "peptidoglycan_transglycosylase_side_nodes",
                    "Peptidoglycan and transglycosylase side nodes",
                    "yceG is a peptidoglycan lytic transglycosylase/polymerization terminase, while PP_5334 is retained as an unresolved membrane transglycosylase-side candidate.",
                    [by_gene["yceG"], by_gene["PP_5334"]],
                ),
            ],
        },
    }
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    rows = load_rows()
    infos = [curate_gene(row) for row in rows]
    create_module(infos)
    print(f"Curated {len(infos)} genes")
    print(f"Wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
