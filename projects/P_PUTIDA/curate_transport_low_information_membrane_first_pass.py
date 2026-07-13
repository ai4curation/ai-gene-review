#!/usr/bin/env python3
"""First-pass curation for low-information transport-bucket membrane proteins."""

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
    "module_transport_membrane_efflux_low_information_membrane_proteins.tsv"
)
MODULE_PATH = ROOT / "modules/low_information_membrane_protein_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0005886": "plasma membrane",
    "GO:0008490": "arsenite secondary active transmembrane transporter activity",
    "GO:0009403": "toxin biosynthetic process",
    "GO:0015031": "protein transport",
    "GO:0015105": "arsenite transmembrane transporter activity",
    "GO:0015499": "formate transmembrane transporter activity",
    "GO:0015699": "antimonite transmembrane transport",
    "GO:0015700": "arsenite transport",
    "GO:0015724": "formate transport",
    "GO:0016020": "membrane",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0030288": "outer membrane-bounded periplasmic space",
    "GO:0031992": "energy transducer activity",
    "GO:0042960": "antimonite secondary active transmembrane transporter activity",
    "GO:0046677": "response to antibiotic",
    "GO:0055085": "transmembrane transport",
    "GO:0098797": "plasma membrane protein complex",
}

GROUP_SPECS: dict[str, dict[str, Any]] = {
    "Clear low-information transporter candidates": {
        "genes": {
            "PP_0926", "PP_1150", "PP_1196", "PP_1275", "PP_1456", "PP_2251", "PP_2853",
            "PP_3083", "PP_3305", "PP_3447", "PP_3512", "PP_4652", "PP_4850", "yicG",
        },
        "class": "broad_transport",
        "primary": "GO:0022857",
        "processes": ["GO:0055085"],
        "locations": ["GO:0016020"],
        "summary": "low-information membrane transporter candidate.",
    },
    "ArsB arsenical pumps": {
        "genes": {"arsB-I", "arsB-II"},
        "class": "arsb",
        "primary": "GO:0015105",
        "processes": ["GO:0015700", "GO:0015699"],
        "locations": ["GO:0005886", "GO:0016020"],
        "summary": "ArsB-family arsenite/antimonite pump.",
    },
    "YfdC formate/nitrite transporter candidate": {
        "genes": {"yfdC"},
        "class": "yfdc",
        "primary": "GO:0015499",
        "processes": ["GO:0015724"],
        "locations": ["GO:0005886", "GO:0016020"],
        "summary": "YfdC/formate-nitrite transporter-family membrane protein.",
    },
    "TonB-family energy-transducer singleton": {
        "genes": {"PP_4994"},
        "class": "tonb",
        "primary": "GO:0031992",
        "processes": ["GO:0015031", "GO:0055085"],
        "locations": ["GO:0005886", "GO:0030288"],
        "summary": "TonB C-terminal-domain energy-transducer candidate with unresolved receptor partners.",
    },
    "Envelope, outer-membrane, biofilm, and toxin side nodes": {
        "genes": {"oprH", "cvpA", "PP_1774", "PP_2006", "PP_2028", "PP_2104", "PP_2669", "PP_2854", "PP_4815", "PP_5152"},
        "class": "envelope_side_node",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "summary": "envelope, outer-membrane, biofilm, holin, or toxin-production side node.",
    },
    "Domain-only membrane proteins with unresolved activity": {
        "genes": {
            "PP_0007", "PP_0027", "PP_0108", "PP_0349", "yqaE", "PP_0439", "dedA", "PP_0790",
            "PP_0919", "PP_0984", "PP_1004", "PP_1130", "PP_1359", "PP_1404", "PP_1448",
            "yohC", "PP_1837", "PP_1882", "PP_1936", "PP_2202", "PP_2309", "cigR", "PP_2840",
            "PP_2889", "PP_2996", "PP_3109", "PP_3524", "PP_3688", "PP_3769", "PP_3971",
            "yedI", "PP_4518", "PP_4839", "PP_4910", "PP_5091", "ygdD", "PP_5353", "PP_5505",
            "PP_5563", "PP_4652", "PP_4815",
        },
        "class": "low_info",
        "primary": None,
        "processes": [],
        "locations": ["GO:0016020"],
        "summary": "low-information membrane-domain protein with unresolved activity.",
    },
}

OVERRIDES: dict[str, dict[str, Any]] = {
    "dedA": {"primary": None, "processes": [], "locations": ["GO:0005886"]},
    "PP_0790": {"processes": ["GO:0046677"], "locations": ["GO:0005886"]},
    "cvpA": {"processes": ["GO:0009403"], "locations": ["GO:0016020"]},
    "oprH": {"locations": ["GO:0016020"]},
    "PP_2669": {"locations": ["GO:0016020"]},
    "PP_2854": {"locations": ["GO:0016020"]},
    "PP_4652": {"primary": "GO:0022857", "processes": ["GO:0055085"], "locations": ["GO:0005886"]},
    "PP_4815": {"primary": None, "processes": [], "locations": ["GO:0016020"]},
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
        "This first-pass review keeps the call conservative because this transport-bucket member has limited direct functional signal."
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


def review(info: GeneInfo, summary: str, action: str, reason: str, replacement_ids: list[str] | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {"summary": summary, "action": action, "reason": reason, "supported_by": base_support(info)}
    if replacement_ids:
        item["proposed_replacement_terms"] = [term(go_id) for go_id in replacement_ids]
    return item


def location_review(info: GeneInfo, go_id: str) -> dict[str, Any]:
    if go_id == "GO:0005886":
        return review(info, "Plasma-membrane localization is appropriate for this low-information membrane protein.", "ACCEPT", "UniProt/GOA membrane and transmembrane evidence supports bacterial plasma-membrane context.")
    if go_id == "GO:0016020":
        if "GO:0005886" in info.get("go_ids", []):
            return review(info, "Generic membrane localization is true but less informative than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "A more specific plasma-membrane annotation is present.")
        return review(info, "Membrane localization is appropriate for this low-information membrane protein.", "ACCEPT", "UniProt membrane/transmembrane evidence supports membrane localization.")
    if go_id == "GO:0030288":
        return review(info, "Outer membrane-bounded periplasmic-space localization is appropriate TonB-family envelope context.", "ACCEPT", "TonB-family energy transducers act in the bacterial envelope.")
    raise ValueError(f"Unhandled location term {go_id}")


def existing_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]
    gene = info["gene"]
    cls = info["profile"]["class"]

    if go_id in {"GO:0005886", "GO:0016020", "GO:0030288"}:
        return location_review(info, go_id)

    if cls == "arsb" and go_id in {"GO:0008490", "GO:0015105", "GO:0042960"}:
        return review(info, f"{label} is appropriate for this ArsB-family arsenical pump.", "ACCEPT", "ArsB family and product evidence support arsenite/antimonite transporter activity.")
    if cls == "arsb" and go_id in {"GO:0015699", "GO:0015700"}:
        return review(info, f"{label} is appropriate process context for this ArsB-family pump.", "ACCEPT", "The supported transporter activity directly supports arsenite/antimonite transport.")

    if cls == "yfdc" and go_id in {"GO:0015499", "GO:0015724"}:
        return review(info, f"{label} is appropriate for this formate/nitrite transporter-family protein.", "ACCEPT", "YfdC product/domain evidence supports formate/nitrite transporter-family context.")
    if cls == "yfdc" and go_id in {"GO:0022857", "GO:0055085"}:
        return review(info, f"{label} is true but less informative than the formate transporter-family annotation.", "MARK_AS_OVER_ANNOTATED", "The formate transporter-family term is more informative for this protein.", ["GO:0015499"])

    if go_id in {"GO:0022857", "GO:0055085"}:
        if gene == "dedA":
            return review(info, f"{label} is likely over-propagated for this low-information DedA-family protein.", "MARK_AS_OVER_ANNOTATED", "The available evidence supports conserved inner-membrane/DedA context but not a resolved transporter activity.")
        return review(info, f"{label} is appropriate broad transporter context for this low-information transporter-family protein.", "ACCEPT", "Product/domain evidence supports transporter-family context while substrate and partners remain unresolved.")

    if go_id == "GO:0046677":
        return review(info, "Response to antibiotic is retained as AmpE/beta-lactamase-regulation context.", "ACCEPT", "AmpE-family evidence supports antibiotic-response context, but the exact mechanism remains unresolved.")
    if go_id == "GO:0009403":
        return review(info, "Toxin biosynthetic process is retained as CvpA/colicin-production context.", "ACCEPT", "CvpA product/family evidence supports colicin/toxin-production context, not a transporter pathway core.")
    if cls == "tonb" and go_id in {"GO:0015031", "GO:0031992", "GO:0055085", "GO:0098797"}:
        return review(info, f"{label} is appropriate TonB-family envelope energy-transduction context.", "ACCEPT", "TonB C-terminal-domain evidence supports component-level TonB energy transduction with unresolved receptor partners.")

    return review(info, f"{label} is retained only as non-core automated side context.", "KEEP_AS_NON_CORE", "The first pass does not resolve this low-information term as a confident core role.")


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
        out.append(new_annotation(info, primary, "enables", f"Adds {TERMS[primary]} for this low-information membrane boundary member.", "Product/domain evidence and Asta retrieval context support this conservative first-pass assignment."))
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
    refs[ref_file(gene, "uniprot.txt")] = {"id": ref_file(gene, "uniprot.txt"), "title": f"UniProtKB entry for {gene} ({info['accession']})", "findings": [{"supporting_text": info["de"]}]}
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
        {"question": "What substrate, partner system, localization, and physiological condition, if any, can be experimentally assigned to this low-information KT2440 membrane protein?"}
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Use tagged localization, fitness/phenotype screening under stress and transport conditions, and targeted partner/substrate assays only after a phenotype or conserved neighborhood suggests a testable role.",
            "experiment_type": "low-information membrane protein phenotyping and localization",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    safe_gene = re.sub(r"[^A-Za-z0-9_]+", "_", gene)
    annoton: dict[str, Any] = {
        "id": f"{safe_gene}_low_information_membrane_context",
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
    return {concept.get("term", {}).get("id") for concept in doc.get("module", {}).get("concepts", []) if concept.get("term", {}).get("id")}


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
        "id": "MODULE:low_information_membrane_protein_boundary",
        "title": "Low-information membrane protein boundary",
        "description": "",
        "status": "DRAFT",
        "evidence": [],
        "notes": "",
        "module": {
            "id": "low_information_membrane_protein_boundary",
            "label": "Low-information membrane protein boundary",
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
                    "description": f"First-pass low-information membrane subgroup: {group}.",
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
    concepts = doc.setdefault("module", {}).setdefault("concepts", [])
    existing_concepts = concept_ids_from_module(doc)
    for go_id in sorted(needed_concepts - existing_concepts):
        concepts.append(descriptor(go_id, "Concept used for first-pass low-information membrane protein curation."))
    source_id = f"file:{BATCH_PATH.relative_to(ROOT)}"
    evidence = doc.setdefault("evidence", [])
    if not any(item.get("source_id") == source_id for item in evidence):
        evidence.append(
            {
                "source_id": source_id,
                "title": "PSEPK transport-bucket low-information membrane protein batch",
                "statement": "The batch table records 67 PSEPK transport/membrane/efflux-bucket proteins with product-name-only or weak domain signal.",
            }
        )
    doc["description"] = (
        "Boundary module for low-information PSEPK membrane proteins pulled into transport buckets by weak membrane, transport, or family-name signal. "
        "It separates clear low-information transporter candidates, ArsB and YfdC specific transporter cases, a TonB-domain singleton, envelope/"
        "outer-membrane/biofilm/toxin side nodes, and domain-only membrane proteins left unresolved."
    )
    doc["notes"] = (
        "First-pass interpretation: this is a conservative holding boundary, not a satisfiable transport pathway. "
        "Only ArsB, YfdC, TonB-domain, and clearer PACE/FUSC/PIN/MFS/TerC/AI-2E-like transporter-family cases receive transporter functions. "
        "Most proteins are retained as membrane or side-node context until gene-specific evidence supports substrate, partner, or pathway claims."
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
