#!/usr/bin/env python3
"""First-pass curation for lipoprotein/envelope accessory transport spillovers."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = ROOT / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_lipoprotein_envelope_accessory_spillovers.tsv"
MODULE_PATH = ROOT / "modules/transport_envelope_spillover_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0003755": "peptidyl-prolyl cis-trans isomerase activity",
    "GO:0005886": "plasma membrane",
    "GO:0016020": "membrane",
    "GO:0016853": "isomerase activity",
    "GO:0006457": "protein folding",
    "GO:0030288": "outer membrane-bounded periplasmic space",
    "GO:0009306": "protein secretion",
}

PROFILES = {
    "PP_1501": ("Low-information lipoprotein side node", None, [], []),
    "PP_2304": ("PpiD periplasmic folding chaperone", "GO:0003755", ["GO:0006457"], ["GO:0005886"]),
    "csgG": ("CsgG curli assembly/transport component", None, ["GO:0009306"], ["GO:0030288"]),
}

DESCRIPTIONS = {
    "PP_1501": "PP_1501 encodes a product-name-only lipoprotein with no GOA rows or supporting domains in the current local evidence; first-pass curation leaves its molecular function unresolved.",
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


def existing_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]

    if go_id == "GO:0003755":
        return review(info, "Peptidyl-prolyl cis-trans isomerase activity is appropriate for PpiD.", "ACCEPT", "The PpiD product and PPIase-domain evidence support this enzymatic/folding-chaperone activity.")
    if go_id == "GO:0016853":
        return review(info, "Generic isomerase activity is true but less informative than the PPIase term.", "KEEP_AS_NON_CORE", "Peptidyl-prolyl cis-trans isomerase activity captures the specific core molecular function.")
    if go_id == "GO:0005886":
        return review(info, "Plasma membrane localization is appropriate for this inner-membrane/periplasmic folding chaperone.", "ACCEPT", "The UniProt/GOA membrane context supports plasma or inner-membrane localization.")
    if go_id == "GO:0030288":
        return review(info, "Outer membrane-bounded periplasmic space localization is appropriate for CsgG envelope assembly context.", "ACCEPT", "The CsgG family/product evidence supports an envelope/periplasmic assembly or secretion component.")

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
    if info.get("primary") and info["primary"] not in go_ids:
        out.append(new_annotation(info, info["primary"], "enables", f"Adds {TERMS[info['primary']]} for this envelope accessory profile.", "Product, family, domain, and Asta context support this first-pass core term."))
    for process in info["processes"]:
        if process not in go_ids:
            out.append(new_annotation(info, process, "involved_in", f"Adds {TERMS[process]} process context.", "The supported family/product role implies this conservative process annotation."))
    for location in info["locations"]:
        if location not in go_ids:
            out.append(new_annotation(info, location, "located_in", f"Adds {TERMS[location]} localization context.", "The UniProt/GOA envelope context supports this localization."))
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
    return f"{gene} encodes {info['product']}, retained as unresolved side context in the lipoprotein/envelope accessory spillover bucket."


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
    doc["suggested_questions"] = [{"question": "What specific envelope partner, substrate, or assembly pathway is supported for this accessory protein in KT2440?"}]
    doc["suggested_experiments"] = [
        {
            "description": "Test envelope localization, folding/assembly phenotypes, and partner interactions using tagged proteins, knockout/complement strains, and substrate or secretion readouts where relevant.",
            "experiment_type": "envelope localization, genetics, and protein-interaction assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_transport_bucket_envelope_accessory_context",
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


def extend_module(infos: list[GeneInfo]) -> None:
    doc = yaml.safe_load(MODULE_PATH.read_text(encoding="utf-8"))
    evidence = doc.setdefault("evidence", [])
    source_id = f"file:{BATCH_PATH.relative_to(ROOT)}"
    if not any(item.get("source_id") == source_id for item in evidence):
        evidence.append(
            {
                "source_id": source_id,
                "title": "PSEPK transport lipoprotein/envelope accessory spillover batch",
                "statement": "The transport partition routes three lipoprotein or envelope accessory genes into the existing transport/envelope spillover boundary rather than treating them as standalone transporter systems.",
            }
        )
    notes = doc.get("notes", "")
    add_note = (
        " The transport-bucket lipoprotein/envelope accessory extension adds PP_1501 as unresolved product-name-only "
        "lipoprotein context, PP_2304 as PpiD periplasmic PPIase/folding-chaperone context, and csgG as curli "
        "assembly/transport component context."
    )
    if "transport-bucket lipoprotein/envelope accessory extension" not in notes:
        doc["notes"] = (notes.rstrip() + add_note).strip()

    module = doc.setdefault("module", {})
    concepts = module.setdefault("concepts", [])
    concept_ids = {
        (item.get("term") or {}).get("id")
        for item in concepts
        if isinstance(item, dict)
    }
    for go_id in ["GO:0003755", "GO:0006457", "GO:0030288", "GO:0009306", "GO:0005886", "GO:0016020"]:
        if go_id not in concept_ids:
            concepts.append(descriptor(go_id, "Concept used for transport-bucket lipoprotein/envelope accessory spillover curation."))

    parts = module.setdefault("parts", [])
    parts[:] = [
        part
        for part in parts
        if (part.get("node") or {}).get("id") != "transport_bucket_lipoprotein_envelope_accessory_spillovers"
    ]
    next_order = max((part.get("order", 0) or 0 for part in parts), default=0) + 1
    parts.append(
        {
            "order": next_order,
            "role": "Transport-bucket lipoprotein and envelope accessory spillovers",
            "node": {
                "id": "transport_bucket_lipoprotein_envelope_accessory_spillovers",
                "label": "Transport-bucket lipoprotein and envelope accessory spillovers",
                "module_type": "TRANSPORT_STEP",
                "description": "Transport/membrane/efflux partition extension for lipoprotein, PpiD folding chaperone, and CsgG curli assembly/transport side nodes.",
                "annotons": [module_annoton(info) for info in infos],
            },
        }
    )
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    rows = load_rows()
    collect_existing_terms(rows)
    infos = [curate_gene(row) for row in rows]
    extend_module(infos)
    print(f"Curated {len(infos)} genes")
    print(f"Extended {MODULE_PATH}")


if __name__ == "__main__":
    main()
