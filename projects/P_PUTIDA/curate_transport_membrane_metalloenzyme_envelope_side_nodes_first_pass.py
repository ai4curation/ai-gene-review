#!/usr/bin/env python3
"""First-pass curation for membrane metalloenzymes and envelope side nodes."""

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
    "module_transport_membrane_efflux_ion_metal_membrane_metalloenzymes_and_envelope_side_nodes.tsv"
)
MODULE_PATH = ROOT / "modules/transport_membrane_enzyme_spillover_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0004176": "ATP-dependent peptidase activity",
    "GO:0004222": "metalloendopeptidase activity",
    "GO:0004553": "hydrolase activity, hydrolyzing O-glycosyl compounds",
    "GO:0005524": "ATP binding",
    "GO:0005886": "plasma membrane",
    "GO:0005975": "carbohydrate metabolic process",
    "GO:0006508": "proteolysis",
    "GO:0008233": "peptidase activity",
    "GO:0008237": "metallopeptidase activity",
    "GO:0008270": "zinc ion binding",
    "GO:0009103": "lipopolysaccharide biosynthetic process",
    "GO:0009306": "protein secretion",
    "GO:0016020": "membrane",
    "GO:0016758": "hexosyltransferase activity",
    "GO:0016780": "phosphotransferase activity, for other substituted phosphate groups",
    "GO:0016887": "ATP hydrolysis activity",
    "GO:0030163": "protein catabolic process",
    "GO:0044038": "cell wall macromolecule biosynthetic process",
    "GO:0046872": "metal ion binding",
    "GO:0071555": "cell wall organization",
    "GO:0097347": "TAM protein secretion complex",
}

PROFILE = {
    "PP_0093": {
        "class": "broad_protease",
        "group": "Membrane protease and metalloprotease side nodes",
        "primary": "GO:0008233",
        "processes": ["GO:0006508"],
        "locations": ["GO:0016020"],
        "description": "PP_0093 encodes a membrane-associated zinc-protease/aminopeptidase-domain candidate, curated conservatively as a broad peptidase side node.",
    },
    "PP_0144": {
        "class": "m16_protease",
        "group": "Membrane protease and metalloprotease side nodes",
        "primary": "GO:0008237",
        "processes": ["GO:0006508"],
        "locations": ["GO:0016020"],
        "description": "PP_0144 encodes an M16-family metalloprotease candidate with membrane/signal evidence, curated as a metallopeptidase side node.",
    },
    "PP_1124": {
        "class": "copd",
        "group": "Copper/cytochrome membrane side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_1124 encodes a CopD-domain copper-resistance membrane protein candidate with unresolved molecular function.",
    },
    "PP_1526": {
        "class": "glucosyltransferase",
        "group": "Membrane lipid/cell-wall glycosylation side nodes",
        "primary": "GO:0016758",
        "processes": ["GO:0005975"],
        "locations": ["GO:0005886"],
        "description": "PP_1526 encodes a membrane beta-monoglucosyldiacylglycerol synthase, curated as a hexosyltransferase/lipid-glycosylation side node rather than an ion transporter.",
    },
    "rseP": {
        "class": "m50_protease",
        "group": "Membrane protease and metalloprotease side nodes",
        "primary": "GO:0004222",
        "processes": ["GO:0006508"],
        "locations": ["GO:0016020"],
        "description": "rseP encodes an intramembrane M50-family zinc metalloprotease involved in membrane proteolysis and sigma-factor quality-control context.",
    },
    "wbpL": {
        "class": "wbpl",
        "group": "Membrane lipid/cell-wall glycosylation side nodes",
        "primary": "GO:0016780",
        "processes": ["GO:0009103"],
        "locations": ["GO:0005886"],
        "description": "wbpL encodes a membrane glycosyltransferase/phosphotransferase-family protein associated with LPS or cell-wall glycoconjugate biosynthesis.",
    },
    "PP_1838": {
        "class": "opgb_ltas",
        "group": "Membrane lipid/cell-wall glycosylation side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0005886"],
        "description": "PP_1838 encodes an OpgB/LTA-synthase-like membrane protein with sulfatase_N/LtaS-like domains; catalytic substrate and pathway role remain unresolved.",
    },
    "htpX": {
        "class": "m48_protease",
        "group": "Membrane protease and metalloprotease side nodes",
        "primary": "GO:0004222",
        "processes": ["GO:0006508"],
        "locations": ["GO:0005886"],
        "description": "htpX encodes the reviewed inner-membrane HtpX zinc metalloprotease, a membrane protein-quality-control protease.",
    },
    "PP_2893": {
        "class": "tamb",
        "group": "Envelope assembly side nodes",
        "primary": None,
        "processes": ["GO:0009306"],
        "locations": ["GO:0005886"],
        "in_complex": "GO:0097347",
        "description": "PP_2893 encodes a TamB-domain translocation and assembly module protein, curated as TAM/envelope protein-secretion context.",
    },
    "PP_2974": {
        "class": "opgb_ltas",
        "group": "Membrane lipid/cell-wall glycosylation side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0005886"],
        "description": "PP_2974 encodes a sulfatase_N/OpgB-LTA-synthase-like membrane protein with unresolved catalytic substrate and pathway role.",
    },
    "ybhN": {
        "class": "phospholipid_mod",
        "group": "Membrane lipid/cell-wall glycosylation side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0005886"],
        "description": "ybhN encodes an L-PG synthase/AglD-like phospholipid-modification membrane protein candidate with unresolved molecular function.",
    },
    "PP_4263": {
        "class": "cycz_copper",
        "group": "Copper/cytochrome membrane side nodes",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_4263 encodes a CycZ/DsbD-like membrane protein annotated as copper tolerance or cytochrome-biogenesis context, with unresolved molecular function.",
    },
    "ypfJ": {
        "class": "ypfj_protease",
        "group": "Membrane protease and metalloprotease side nodes",
        "primary": "GO:0008237",
        "processes": ["GO:0006508"],
        "locations": ["GO:0016020"],
        "description": "ypfJ encodes a membrane zinc-metalloprotease candidate, curated as a broad metallopeptidase side node.",
    },
    "ftsH": {
        "class": "ftsh",
        "group": "Membrane protease and metalloprotease side nodes",
        "primary": "GO:0004176",
        "processes": ["GO:0030163", "GO:0006508"],
        "locations": ["GO:0005886"],
        "description": "ftsH encodes the membrane AAA+ ATP-dependent zinc metalloprotease FtsH, a protein-quality-control protease.",
    },
}

DOMAIN_NEEDLES = {
    "PP_0093": ["Zinc protease protein", "Aminopept", "KW   Membrane"],
    "PP_0144": ["Metalloprotease, insulinase family", "peptidase M16", "Peptidase_M16"],
    "PP_1124": ["Copper resistance protein D domain-containing protein", "Cu-R_CopD_dom", "KW   Membrane"],
    "PP_1526": ["Beta-monoglucosyldiacylglycerol synthase", "UDP-glucose:1,2-diacylglycerol", "Glycosyltr_2/OpgH_subfam"],
    "rseP": ["Zinc metalloprotease", "peptidase M50B", "Pept_M50_Zn"],
    "wbpL": ["Glycosyl transferase WbpL", "Glycosyl_transferase_4", "KW   Magnesium"],
    "PP_1838": ["Sulfatase N-terminal domain-containing protein", "OpgB/LTA_synthase_biosynth", "Sulfatase_N"],
    "htpX": ["Protease HtpX", "peptidase M48B", "HtpX_protease"],
    "PP_2893": ["Translocation and assembly module TamB", "TamB_C", "TamB (PF04357)"],
    "PP_2974": ["Sulfatase", "OpgB/LTA_synthase_biosynth", "Sulfatase_N"],
    "ybhN": ["Phospholipid modification enzyme", "L-PG_synthase/AglD", "LPG_synthase_TM"],
    "PP_4263": ["cytochrome biogenesis cycZ-like", "UreH-like_TM_dom", "KW   Membrane"],
    "ypfJ": ["Zinc metalloprotease", "Uncharacterised_pept_Zn_put", "Zn_peptidase"],
    "ftsH": ["ATP-dependent zinc metalloprotease FtsH", "Acts as a processive", "Peptidase_M41"],
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
        return review(info, "Plasma membrane localization is appropriate for this bacterial membrane or envelope protein.", "ACCEPT", "UniProt/GOA membrane and transmembrane evidence supports membrane localization.")
    if go_id == "GO:0016020":
        if "GO:0005886" in info["go_ids"]:
            return review(info, "Generic membrane localization is true but less informative than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "A more specific plasma-membrane annotation is present.")
        return review(info, "Membrane localization is appropriate for this membrane/envelope side-node protein.", "ACCEPT", "UniProt membrane/transmembrane evidence supports membrane localization.")
    if go_id == "GO:0046872":
        return review(info, "Metal ion binding is retained as non-core cofactor/domain context.", "KEEP_AS_NON_CORE", "The core role is a metalloprotease, glycosyltransferase, or membrane side-node function rather than metal binding alone.")
    if go_id == "GO:0008270":
        return review(info, "Zinc ion binding is retained as non-core metalloprotease cofactor context.", "KEEP_AS_NON_CORE", "The protease activity captures the core role more directly than zinc binding alone.")
    if go_id == "GO:0004553":
        return review(info, "O-glycosyl hydrolase activity conflicts with the beta-monoglucosyldiacylglycerol synthase/transferase assignment.", "REMOVE", "The product name and EC 2.4.1.336 support glycosyltransferase chemistry, not hydrolysis.", ["GO:0016758"])
    if go_id == "GO:0005975":
        return review(info, "Carbohydrate metabolic process is retained as broad non-core context for the glycosyltransferase side node.", "KEEP_AS_NON_CORE", "The specific membrane glucosyltransferase activity is the clearer core function.")
    if go_id == "GO:0016758":
        return review(info, "Hexosyltransferase activity is appropriate for beta-monoglucosyldiacylglycerol synthase.", "ACCEPT", "The product name, EC, and glycosyltransferase-family evidence support this molecular function.")
    if go_id == "GO:0004222":
        return review(info, f"{label} is appropriate for this membrane zinc metalloprotease.", "ACCEPT", "The product/family evidence supports membrane metalloprotease activity.")
    if go_id == "GO:0008233":
        if cls == "ftsh":
            return review(info, "Broad peptidase activity is true but less informative than ATP-dependent peptidase activity.", "MARK_AS_OVER_ANNOTATED", "FtsH is better captured by ATP-dependent peptidase activity.", ["GO:0004176"])
        return review(info, "Broad peptidase activity is appropriate for this low-resolution protease candidate.", "ACCEPT", "The product/domain evidence supports a protease role while substrate and catalytic class remain unresolved.")
    if go_id == "GO:0008237":
        return review(info, "Metallopeptidase activity is appropriate for this membrane metalloprotease candidate.", "ACCEPT", "The product and zinc/metalloprotease domain evidence support metallopeptidase activity.")
    if go_id == "GO:0006508":
        return review(info, "Proteolysis is appropriate process context for this protease.", "ACCEPT", "The supported peptidase/metalloprotease activity implies proteolysis.")
    if go_id == "GO:0004176":
        return review(info, "ATP-dependent peptidase activity is the core FtsH molecular function.", "ACCEPT", "The FtsH product and AAA+/M41 protease domains support ATP-dependent proteolysis.")
    if go_id == "GO:0016887":
        return review(info, "ATP hydrolysis activity is retained as non-core AAA+ motor context for FtsH.", "KEEP_AS_NON_CORE", "The core biological role is ATP-dependent protease activity; ATP hydrolysis is a mechanistic component.")
    if go_id == "GO:0005524":
        return review(info, "ATP binding is retained as non-core AAA+ domain context for FtsH.", "KEEP_AS_NON_CORE", "The core biological role is ATP-dependent protease activity rather than nucleotide binding alone.")
    if go_id == "GO:0030163":
        return review(info, "Protein catabolic process is appropriate process context for FtsH.", "ACCEPT", "FtsH-dependent proteolysis supports protein catabolism.")
    if go_id == "GO:0016780":
        return review(info, "Phosphotransferase activity is appropriate first-pass molecular-function context for WbpL-family glycoconjugate initiation.", "ACCEPT", "The WbpL product/family and GOA support this cell-envelope glycan biosynthesis activity.")
    if go_id == "GO:0009103":
        return review(info, "Lipopolysaccharide biosynthetic process is appropriate WbpL pathway context.", "ACCEPT", "WbpL-family membrane glycosyltransferases support LPS or related cell-envelope glycan biosynthesis.")
    if go_id in {"GO:0044038", "GO:0071555"}:
        return review(info, f"{label} is retained as broad cell-envelope biosynthesis context.", "KEEP_AS_NON_CORE", "The LPS/glycoconjugate biosynthesis term is the more specific process call for WbpL.")
    if go_id == "GO:0009306":
        return review(info, "Protein secretion is appropriate envelope-assembly process context for the TamB-domain protein.", "ACCEPT", "TamB-domain evidence and GOA support TAM-associated protein secretion/outer-membrane assembly context.")
    if go_id == "GO:0097347":
        return review(info, "TAM protein secretion complex membership is appropriate for the TamB-domain protein.", "ACCEPT", "The TamB-domain product and GOA support TAM complex context.")

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
                f"Adds {TERMS[primary]} for this membrane/envelope side-node protein.",
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
                    "The supported molecular function or envelope-complex context implies this conservative process annotation.",
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
    complex_id = info["profile"].get("in_complex")
    if complex_id and complex_id not in go_ids:
        out.append(
            new_annotation(
                info,
                complex_id,
                "part_of",
                f"Adds {TERMS[complex_id]} complex context.",
                "The TamB product/domain evidence supports TAM protein secretion complex context.",
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
    if profile.get("primary"):
        core["molecular_function"] = term(profile["primary"])
    if profile.get("processes"):
        core["directly_involved_in"] = [term(go_id) for go_id in profile["processes"]]
    if profile.get("locations"):
        core["locations"] = [term(go_id) for go_id in profile["locations"]]
    if profile.get("in_complex"):
        core["in_complex"] = term(profile["in_complex"])
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
    if "molecular_function" in core and core["molecular_function"]["id"] not in reflected_ids:
        core.pop("molecular_function")
    if "in_complex" in core and core["in_complex"]["id"] not in reflected_ids:
        core.pop("in_complex")
    for slot in ("directly_involved_in", "locations"):
        if slot in core:
            core[slot] = [item for item in core[slot] if item["id"] in reflected_ids]
            if not core[slot]:
                core.pop(slot)
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "What is the direct substrate, envelope pathway partner, and physiological condition for this membrane enzyme or envelope side-node protein in KT2440?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure protease, glycosyltransferase, envelope-assembly, copper-tolerance, or membrane-lipid phenotypes in targeted knockouts and complemented strains under envelope stress and metal-stress conditions.",
            "experiment_type": "membrane enzyme genetics and biochemical/phenotypic assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_membrane_enzyme_side_context",
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
                    "description": f"First-pass membrane enzyme/envelope side-node subgroup: {group}.",
                    "annotons": [module_annoton(info) for info in group_infos],
                },
            }
        )
    concept_ids = [
        "GO:0008233",
        "GO:0008237",
        "GO:0004222",
        "GO:0004176",
        "GO:0016758",
        "GO:0016780",
        "GO:0006508",
        "GO:0030163",
        "GO:0009103",
        "GO:0009306",
        "GO:0097347",
        "GO:0005886",
        "GO:0016020",
    ]
    doc = {
        "id": "MODULE:transport_membrane_enzyme_spillover_boundary",
        "title": "Transport-bucket membrane enzyme and envelope side-node boundary",
        "description": (
            "Boundary module for PSEPK membrane proteases, membrane glycosylation/lipid side nodes, TamB envelope assembly, "
            "CopD/CycZ-like copper/cytochrome side nodes, and other metalloenzyme-like entries pulled into the ion/metal split."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK membrane metalloenzyme/envelope side-node batch",
                "statement": "The batch table records 14 PSEPK ion/metal-bucket genes that are membrane enzymes or envelope side nodes rather than ion transporters.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_ion_metal_partition.tsv",
                "title": "PSEPK transport ion/metal sub-bucket partition",
                "statement": "The deeper ion/metal partition separates these side nodes from true cation transporters and redox membrane proteins.",
            },
        ],
        "notes": (
            "First-pass interpretation: keep this as a spillover boundary, not an ion-transport module. "
            "Protease and glycosyltransferase calls are retained where product/family support them; CopD/CycZ-like, OpgB/LTA-like, and phospholipid-modification candidates remain low-resolution membrane/envelope context."
        ),
        "module": {
            "id": "transport_membrane_enzyme_spillover_boundary",
            "label": "Transport-bucket membrane enzyme and envelope side-node boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [descriptor(go_id, "Concept used for first-pass membrane enzyme/envelope side-node curation.") for go_id in concept_ids],
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
