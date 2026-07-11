#!/usr/bin/env python3
"""First-pass curation for organic-acid and aromatic-anion transporters."""

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
    "module_transport_membrane_efflux_organic_acid_aromatic_anion_transporters.tsv"
)
MODULE_PATH = ROOT / "modules/organic_acid_aromatic_anion_transport_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on inter-ontology links",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0015355": "secondary active monocarboxylate transmembrane transporter activity",
    "GO:0015718": "monocarboxylic acid transport",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0055085": "transmembrane transport",
}

PROFILES = {
    "citN": ("CitMHS citrate transporters", "GO:0015137", ["GO:0015746"], ["GO:0016020"]),
    "PP_1820": ("BenE benzoate transporters", "GO:0042925", ["GO:0042919"], ["GO:0005886"]),
    "benE-I": ("BenE benzoate transporters", "GO:0042925", ["GO:0042919"], ["GO:0005886"]),
    "bhbP": ("BhbP hydroxybutyrate/monocarboxylate permease candidates", "GO:0015355", ["GO:0015718"], ["GO:0005886"]),
    "benE-II": ("BenE benzoate transporters", "GO:0042925", ["GO:0042919"], ["GO:0005886"]),
    "PP_3247": ("Bile-acid/Na+ symporter-family unresolved transporters", "GO:0022857", ["GO:0055085"], ["GO:0016020"]),
    "lldP": ("LldP lactate proton symporters", "GO:0015129", ["GO:0035873", "GO:0015727"], ["GO:0005886"]),
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
    primary = info["primary"]

    if go_id == "GO:0005886":
        return review(info, "Plasma membrane localization is appropriate for this bacterial transporter.", "ACCEPT", "The UniProt/GOA membrane context supports plasma or inner-membrane localization.")
    if go_id == "GO:0016020":
        if "GO:0005886" in info["go_ids"]:
            return review(info, "Generic membrane localization is true but less informative than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "A more specific plasma-membrane annotation is present.")
        return review(info, "Membrane localization is appropriate for this transporter.", "ACCEPT", "The UniProt/GOA membrane context supports this localization.")
    if go_id == "GO:0055085":
        if primary != "GO:0022857":
            return review(info, "Generic transmembrane transport is true but broad relative to the substrate-specific transporter call.", "MARK_AS_OVER_ANNOTATED", "A more informative transporter term is available for the core function.", [primary])
        return review(info, "Transmembrane transport is retained as broad process context for this unresolved solute transporter.", "ACCEPT", "The bile-acid/Na+ symporter-family domains support transport but not a confident substrate.")
    if go_id == "GO:0022857":
        if primary == "GO:0022857":
            return review(info, "Transmembrane transporter activity is the appropriate conservative molecular function.", "ACCEPT", "The family/domain evidence supports a transporter, but substrate is unresolved.")
        return review(info, "Generic transporter activity is true but broad relative to the substrate-specific transporter call.", "MARK_AS_OVER_ANNOTATED", "A more informative transporter term is available for the core function.", [primary])
    if go_id in {"GO:0015137", "GO:0015746"}:
        return review(info, f"{label} is appropriate CitMHS citrate-transporter context.", "ACCEPT", "The citrate transporter product and CitMHS domains support citrate transport.")
    if go_id in {"GO:0042925", "GO:0042919"}:
        return review(info, f"{label} is appropriate for the BenE-family benzoate transporter.", "ACCEPT", "The benzoate-transporter product and BenE domains support benzoate transport.")
    if go_id in {"GO:0015128", "GO:0035429"} and gene == "bhbP":
        return review(
            info,
            f"{label} is likely over-specific for BhbP.",
            "MODIFY",
            "BhbP is named D-beta-hydroxybutyrate permease and only shares a gluconate-transporter-family domain; no beta-hydroxybutyrate-specific GO term is available locally, so broad monocarboxylate transport is safer.",
            ["GO:0015355"] if go_id == "GO:0015128" else ["GO:0015718"],
        )
    if go_id in {"GO:0015128", "GO:0035429"}:
        return review(info, f"{label} is appropriate gluconate-transporter context.", "ACCEPT", "The GntP product/domain evidence supports gluconate transport.")
    if go_id == "GO:0015129":
        return review(info, "Lactate transmembrane transporter activity is appropriate for LldP.", "ACCEPT", "The L-lactate permease product and lactate-permease domains support lactate transport.")
    if go_id in {"GO:0015727", "GO:0035873"}:
        return review(info, f"{label} is appropriate lactate transport process context.", "ACCEPT", "The L-lactate permease product and lactate-permease domains support lactate transport.")
    if go_id == "GO:0015295":
        return review(info, "Solute:proton symporter activity is retained as coupling context for LldP.", "KEEP_AS_NON_CORE", "The substrate-specific lactate transporter activity is the clearer core molecular function.")
    if go_id == "GO:1902600":
        return review(info, "Proton transmembrane transport is retained as non-core coupling context.", "KEEP_AS_NON_CORE", "This reflects coupling for lactate symport rather than an independent proton-transport core function.")

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
        out.append(new_annotation(info, primary, "enables", f"Adds {TERMS[primary]} for this transporter profile.", "Product, domain, and Asta context support this conservative first-pass core term."))
    for process in info["processes"]:
        if process not in go_ids:
            out.append(new_annotation(info, process, "involved_in", f"Adds {TERMS[process]} process context.", "The supported molecular function implies this conservative process annotation."))
    for location in info["locations"]:
        if location not in go_ids:
            out.append(new_annotation(info, location, "located_in", f"Adds {TERMS[location]} localization context.", "The UniProt/GOA membrane context supports this localization."))
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
    primary = info.get("primary")
    if primary:
        return f"{info['gene']} encodes {info['product']}, curated in the {info['group']} subgroup with core {TERMS[primary]} context."
    return f"{info['gene']} encodes {info['product']}, retained as unresolved side context in the organic-acid/aromatic-anion transport bucket."


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
    doc["suggested_questions"] = [{"question": "What are the exact substrates, direction, and ion-coupling mechanisms for the less-resolved organic-acid transporter paralogs?"}]
    doc["suggested_experiments"] = [
        {
            "description": "Measure uptake or growth rescue for candidate citrate, benzoate, hydroxybutyrate, lactate, bile-acid-like, and related organic-acid substrates in knockout/complement strains and heterologous expression systems.",
            "experiment_type": "transport genetics and substrate uptake assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_organic_acid_anion_context",
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
                    "id": group.lower().replace("/", "_").replace(" ", "_").replace("-", "_").replace("+", "plus"),
                    "label": group,
                    "module_type": "TRANSPORT_STEP",
                    "description": f"First-pass organic-acid/aromatic-anion transporter subgroup: {group}.",
                    "annotons": [module_annoton(info) for info in group_infos],
                },
            }
        )
    concept_ids = [
        "GO:0015137",
        "GO:0015746",
        "GO:0042925",
        "GO:0042919",
        "GO:0015355",
        "GO:0015718",
        "GO:0022857",
        "GO:0055085",
        "GO:0015129",
        "GO:0035873",
        "GO:0015727",
        "GO:0015295",
        "GO:0005886",
        "GO:0016020",
    ]
    doc = {
        "id": "MODULE:organic_acid_aromatic_anion_transport_boundary",
        "title": "Organic-acid and aromatic-anion transport boundary",
        "description": (
            "Boundary module for PSEPK citrate, benzoate, hydroxybutyrate/monocarboxylate, lactate, "
            "and unresolved bile-acid/Na+-symporter-family transport-bucket genes."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK organic-acid/aromatic-anion transporter batch",
                "statement": "The batch table records seven PSEPK transport-bucket genes assigned to citrate, benzoate, hydroxybutyrate, bile-acid-family, and lactate transporter context.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_partition.tsv",
                "title": "PSEPK transport/membrane/efflux partition",
                "statement": "The parent transport partition separates this organic-acid/aromatic-anion panel from ABC, MFS/DMT, ion/metal, amino-acid/amine, carbohydrate/nucleoside, redox, and low-information membrane buckets.",
            },
        ],
        "notes": (
            "First-pass interpretation: keep CitN citrate, BenE benzoate, and LldP lactate calls; broaden BhbP away from unsupported gluconate specificity to monocarboxylate transport; keep PP_3247 substrate-unresolved."
        ),
        "module": {
            "id": "organic_acid_aromatic_anion_transport_boundary",
            "label": "Organic-acid and aromatic-anion transport boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [descriptor(go_id, "Concept used for first-pass organic-acid/aromatic-anion transporter curation.") for go_id in concept_ids],
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
