#!/usr/bin/env python3
"""First-pass curation for inorganic nutrient transport-bucket genes."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = ROOT / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_inorganic_nutrient_transporters.tsv"
MODULE_PATH = ROOT / "modules/inorganic_nutrient_transport_boundary.yaml"

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
    "GO:0008271": "secondary active sulfate transmembrane transporter activity",
    "GO:1902358": "sulfate transmembrane transport",
    "GO:0035435": "phosphate ion transmembrane transport",
    "GO:0006817": "phosphate ion transport",
}

PROFILES = {
    "PP_0075": ("SulP sulfate/organosulfate transporters", "GO:0008271", ["GO:1902358"], ["GO:0016020"]),
    "PP_0101": ("SulP sulfate/organosulfate transporters", "GO:0008271", ["GO:1902358"], ["GO:0016020"]),
    "yjbB": ("YjbB sodium/phosphate cotransporter candidates", None, ["GO:0035435"], ["GO:0005886"]),
    "modR": ("ModE molybdate-responsive transcription regulators", "GO:0003700", ["GO:0006355"], []),
    "PP_0718": ("SulP sulfate/organosulfate transporters", "GO:0008271", ["GO:1902358"], ["GO:0016020"]),
    "cysZ": ("CysZ proton-dependent sulfate transporters", "GO:0008271", ["GO:1902358"], ["GO:0005886"]),
    "pitB": ("PiT phosphate transporters", None, ["GO:0035435", "GO:0006817"], ["GO:0005886"]),
    "PP_1407": ("SulP sulfate/organosulfate transporters", "GO:0008271", ["GO:1902358"], ["GO:0016020"]),
    "PP_2094": ("NasS nitrate-binding side nodes", None, [], []),
    "PP_4103": ("PiT phosphate transporters", None, ["GO:0035435", "GO:0006817"], ["GO:0005886"]),
    "PP_4112": ("SulP sulfate/organosulfate transporters", "GO:0008271", ["GO:1902358"], ["GO:0016020"]),
    "phoU": ("PhoU phosphate-transport accessory/regulatory proteins", None, [], ["GO:0005737"]),
    "PP_5475": ("Low-confidence nitrite-transporter-name-only records", None, [], []),
}

DESCRIPTIONS = {
    "PP_2094": "PP_2094 encodes a NasS-like nitrate-binding protein with no current GOA rows; first-pass curation keeps it as nitrate-sensing or nitrate-transport-associated side context rather than a transporter.",
    "PP_5475": "PP_5475 has a nitrite-transporter product name but no GOA rows, domains, or family support in the current local evidence; first-pass curation leaves its molecular function unresolved.",
}


class GeneInfo(dict[str, Any]):
    gene: str


def load_rows() -> list[dict[str, str]]:
    with BATCH_PATH.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def collect_existing_terms(rows: list[dict[str, str]]) -> None:
    for row in rows:
        gene = row["gene"]
        path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        for ann in doc.get("existing_annotations", []):
            TERMS.setdefault(ann["term"]["id"], ann["term"]["label"])


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


def goa_term_ids(gene: str) -> set[str]:
    path = GENE_ROOT / gene / f"{gene}-goa.tsv"
    with path.open() as handle:
        return {row["GO TERM"] for row in csv.DictReader(handle, delimiter="\t")}


def load_info(row: dict[str, str]) -> GeneInfo:
    gene = row["gene"]
    group, primary, processes, locations = PROFILES[gene]
    uniprot_lines = (GENE_ROOT / gene / f"{gene}-uniprot.txt").read_text(encoding="utf-8").splitlines()
    asta_lines = (GENE_ROOT / gene / f"{gene}-deep-research-asta.md").read_text(encoding="utf-8").splitlines()
    review_doc = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text(encoding="utf-8"))
    info = GeneInfo(
        gene=gene,
        accession=row["uniprot_accession"],
        product=row["protein_name"],
        group=group,
        primary=primary,
        processes=processes,
        locations=locations,
        uniprot_lines=uniprot_lines,
        asta_lines=asta_lines,
        existing_refs={ref["id"]: ref for ref in review_doc.get("references", []) if "id" in ref},
    )
    info["de"] = first_de_line(uniprot_lines)
    info["asta_product"] = first_line(asta_lines, "- **Protein Description:**")
    info["asta_domains"] = first_line(asta_lines, "- **Key Domains:**")
    info["location_line"] = first_line(uniprot_lines, "SUBCELLULAR LOCATION", optional=True)
    return info


def base_support(info: GeneInfo) -> list[dict[str, str]]:
    gene = info["gene"]
    items = [
        support(ref_file(gene, "uniprot.txt"), info["de"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_product"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_domains"]),
    ]
    if info.get("location_line"):
        items.append(support(ref_file(gene, "uniprot.txt"), info["location_line"]))
    return dedupe(items)


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
    gene = info["gene"]
    primary = info.get("primary")

    if go_id == "GO:0005886":
        return review(info, "Plasma membrane localization is appropriate for this bacterial transporter.", "ACCEPT", "The UniProt/GOA membrane context supports plasma or inner-membrane localization.")
    if go_id == "GO:0016020":
        if "GO:0005886" in info["go_ids"]:
            return review(info, "Generic membrane localization is true but less informative than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "A more specific plasma-membrane annotation is present.")
        return review(info, "Membrane localization is appropriate for this membrane protein.", "ACCEPT", "The UniProt/GOA membrane context supports this localization.")
    if go_id == "GO:0055085":
        if primary:
            return review(info, "Generic transmembrane transport is true but broad relative to the substrate/family-specific transporter call.", "MARK_AS_OVER_ANNOTATED", "A more informative transporter term is available for the core function.", [primary])
        if info["processes"]:
            return review(info, "Generic transmembrane transport is true but broad relative to the more specific transport process.", "MARK_AS_OVER_ANNOTATED", "A more informative transport-process term is available.", [info["processes"][0]])
        return review(info, "Generic transmembrane transport is retained as broad context.", "KEEP_AS_NON_CORE", "The exact substrate and transporter activity are unresolved.")

    if go_id in {"GO:0005315", "GO:0005436", "GO:0044341"}:
        return review(info, f"{label} is appropriate sodium/phosphate transporter context.", "ACCEPT", "The Na/Pi cotransporter product and domains support phosphate transmembrane transport.")
    if go_id == "GO:0035725":
        return review(info, "Sodium ion transmembrane transport is retained as coupling context.", "KEEP_AS_NON_CORE", "The phosphate cotransport process is the clearer core process.")
    if go_id in {"GO:0006817", "GO:0035435"}:
        return review(info, f"{label} is appropriate phosphate transporter process context.", "ACCEPT", "The PiT/phosphate transporter product and domains support phosphate transport.")
    if go_id == "GO:0015293":
        return review(info, "Symporter activity is retained as coupling context.", "KEEP_AS_NON_CORE", "The substrate-specific phosphate transporter/process term is the clearer core call.")

    if go_id in {"GO:0009675", "GO:0015116"}:
        return review(info, f"{label} is appropriate CysZ sulfate-transporter context.", "ACCEPT", "The CysZ product, HAMAP rule, and sulfate-transporter domains support sulfate transport.")
    if go_id == "GO:1902358":
        return review(info, "Sulfate transmembrane transport is appropriate sulfate-transporter process context.", "ACCEPT", "The sulfate-transporter product and domains support sulfate transport.")
    if go_id == "GO:0000103":
        return review(info, "Sulfate assimilation is retained as non-core pathway context for sulfate uptake.", "KEEP_AS_NON_CORE", "The direct role is sulfate transmembrane transport.")
    if go_id == "GO:0019344":
        return review(info, "L-cysteine biosynthetic process is pathway-level context rather than the direct transporter function.", "MARK_AS_OVER_ANNOTATED", "CysZ supplies sulfate for assimilation but is not a cysteine-biosynthetic enzyme.")
    if go_id == "GO:1902600":
        return review(info, "Proton transmembrane transport is retained as non-core coupling context.", "KEEP_AS_NON_CORE", "This reflects proton coupling rather than an independent core proton transporter function.")

    if go_id == "GO:0003700":
        return review(info, "DNA-binding transcription factor activity is appropriate for ModR/ModE-family regulator context.", "ACCEPT", "The HTH and ModE-family domains support transcription-regulator function.")
    if go_id == "GO:0006355":
        return review(info, "Regulation of DNA-templated transcription is appropriate regulator process context.", "ACCEPT", "The ModE-family regulator domains support transcriptional regulation.")
    if go_id == "GO:0030151":
        return review(info, "Molybdenum ion binding is appropriate ligand-binding context for ModR.", "KEEP_AS_NON_CORE", "The molybdate/tungstate-binding domain supports metal oxyanion sensing, while DNA-binding regulation is the core function.")
    if go_id == "GO:0015689":
        return review(info, "Molybdate ion transport is over-propagated pathway context for a transcription regulator.", "MARK_AS_OVER_ANNOTATED", "ModR regulates molybdate transport genes but is not itself a transporter.")

    if go_id == "GO:0005737":
        return review(info, "Cytoplasm localization is appropriate for PhoU accessory/regulatory context.", "ACCEPT", "UniProt/GOA localization supports cytoplasmic PhoU.")
    if go_id in {"GO:0030643", "GO:0045936"}:
        return review(info, f"{label} is appropriate PhoU phosphate-homeostasis/accessory context.", "ACCEPT", "PhoU-family evidence supports phosphate-transport accessory/regulatory function rather than direct transmembrane transport.")

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
    go_ids = set(info["go_ids"])
    out: list[dict[str, Any]] = []
    primary = info.get("primary")
    if primary and primary not in go_ids:
        out.append(new_annotation(info, primary, "enables", f"Adds {TERMS[primary]} for this transporter/regulator profile.", "Product, domain, and Asta context support this conservative first-pass core term."))
    for process in info["processes"]:
        if process not in go_ids:
            out.append(new_annotation(info, process, "involved_in", f"Adds {TERMS[process]} process context.", "The supported function implies this conservative process annotation."))
    for location in info["locations"]:
        if location not in go_ids:
            out.append(new_annotation(info, location, "located_in", f"Adds {TERMS[location]} localization context.", "The UniProt/GOA localization context supports this term."))
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


def description(info: GeneInfo) -> str:
    gene = info["gene"]
    if gene in DESCRIPTIONS:
        return DESCRIPTIONS[gene]
    if info.get("primary"):
        return f"{gene} encodes {info['product']}, curated in the {info['group']} subgroup with core {TERMS[info['primary']]} context."
    if info["processes"]:
        return f"{gene} encodes {info['product']}, curated in the {info['group']} subgroup with core {TERMS[info['processes'][0]]} context."
    return f"{gene} encodes {info['product']}, retained as unresolved side context in the inorganic nutrient transport bucket."


def core_function(info: GeneInfo) -> dict[str, Any]:
    core: dict[str, Any] = {"description": description(info), "supported_by": base_support(info)}
    if info.get("primary"):
        core["molecular_function"] = term(info["primary"])
    if info["processes"]:
        core["directly_involved_in"] = [term(go_id) for go_id in info["processes"]]
    if info["locations"]:
        core["locations"] = [term(go_id) for go_id in info["locations"]]
    return core


def curate_gene(row: dict[str, str]) -> GeneInfo:
    info = load_info(row)
    gene = info["gene"]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    goa_ids = goa_term_ids(gene)
    goa_annotations = [ann for ann in doc.get("existing_annotations", []) if ann["term"]["id"] in goa_ids]
    info["go_ids"] = [ann["term"]["id"] for ann in goa_annotations]
    for ann in goa_annotations:
        ann["review"] = existing_review(info, ann)
        ann["review"]["supported_by"].insert(0, goa_support(info, ann["term"]["id"], ann["term"]["label"]))
        ann["review"]["supported_by"] = dedupe(ann["review"]["supported_by"])
    doc["existing_annotations"] = goa_annotations + suggested_new_annotations(info)
    doc["description"] = description(info)
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
    doc["suggested_questions"] = [{"question": "Which substrates and regulatory targets are experimentally supported for the low-resolution SulP, NasS, and nitrite-name-only records?"}]
    doc["suggested_experiments"] = [
        {
            "description": "Measure sulfate, phosphate, nitrate/nitrite, and organosulfate uptake or regulatory reporter activity in knockout/complement strains, with substrate-specific growth or transport assays.",
            "experiment_type": "transport genetics, substrate uptake, and regulatory reporter assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_inorganic_nutrient_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {info['product']}",
    }
    if info.get("primary"):
        annoton["function"] = descriptor(info["primary"])
    if info["processes"]:
        annoton["processes"] = [descriptor(go_id) for go_id in info["processes"]]
    if info["locations"]:
        annoton["locations"] = [descriptor(go_id) for go_id in info["locations"]]
    return annoton


def build_module(infos: list[GeneInfo]) -> None:
    grouped: dict[str, list[GeneInfo]] = defaultdict(list)
    for info in infos:
        grouped[info["group"]].append(info)
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
                    "description": f"First-pass inorganic nutrient transport subgroup: {group}.",
                    "annotons": [module_annoton(info) for info in group_infos],
                },
            }
        )
    concept_ids = [
        "GO:0008271",
        "GO:1902358",
        "GO:0035435",
        "GO:0006817",
        "GO:0003700",
        "GO:0006355",
        "GO:0030151",
        "GO:0005737",
        "GO:0005886",
        "GO:0016020",
    ]
    doc = {
        "id": "MODULE:inorganic_nutrient_transport_boundary",
        "title": "Inorganic nutrient transport boundary",
        "description": (
            "Boundary module for PSEPK SulP/CysZ sulfate or organosulfate transporters, phosphate transport/accessory proteins, "
            "molybdate-responsive regulation, nitrate-binding side context, and low-confidence nitrite-name-only context."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK inorganic nutrient transporter batch",
                "statement": "The batch table records 13 PSEPK transport-bucket genes assigned to phosphate, sulfate, molybdate, nitrate/nitrite, and related inorganic nutrient context.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_partition.tsv",
                "title": "PSEPK transport/membrane/efflux partition",
                "statement": "The parent transport partition separates this inorganic-nutrient panel from ion/metal, ABC, MFS/DMT, amino-acid/amine, organic-acid, carbohydrate/nucleoside, redox, and low-information membrane buckets.",
            },
        ],
        "notes": (
            "First-pass interpretation: keep CysZ/Pit/YjbB transport calls where GOA and domains agree, add conservative cached sulfate or phosphate process terms for low-resolution SulP/Pi candidates, keep ModR/PhoU/NasS as regulatory or accessory side context, and leave PP_5475 unresolved."
        ),
        "module": {
            "id": "inorganic_nutrient_transport_boundary",
            "label": "Inorganic nutrient transport boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [descriptor(go_id, "Concept used for first-pass inorganic nutrient transporter curation.") for go_id in concept_ids],
            "parts": parts,
        },
    }
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    rows = load_rows()
    collect_existing_terms(rows)
    infos = [curate_gene(row) for row in rows]
    build_module(infos)
    print(f"Curated {len(infos)} genes")
    print(f"Wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
