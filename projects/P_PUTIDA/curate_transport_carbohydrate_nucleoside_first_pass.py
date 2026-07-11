#!/usr/bin/env python3
"""First-pass curation for carbohydrate/nucleoside transport-bucket genes."""

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
    "module_transport_membrane_efflux_carbohydrate_nucleoside_transporters.tsv"
)
MODULE_PATH = ROOT / "modules/carbohydrate_nucleoside_transport_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on inter-ontology links",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS: dict[str, str] = {}

PROFILES = {
    "PP_0138": ("SpmB/Gate-domain membrane side nodes", None, [], ["GO:0005886"]),
    "PP_0652": ("GntP-family gluconate transporters", "GO:0015128", ["GO:0035429"], ["GO:0005886"]),
    "PP_0709": ("NCS1 purine-cytosine/nucleobase permeases", "GO:0015205", ["GO:0015851"], ["GO:0005886"]),
    "PP_1740": ("Membrane carbohydrate-enzyme side nodes", "GO:0004553", ["GO:0005975"], ["GO:0005886"]),
    "PP_2860": ("PnuC nicotinamide-riboside transporters", "GO:0034257", ["GO:0034258"], ["GO:0005886"]),
    "PP_3048": ("Prophage structural side nodes", None, ["GO:0019068"], []),
    "PP_3142": ("Membrane sugar-transferase side nodes", "GO:0016780", [], ["GO:0016020"]),
    "codB": ("CodB cytosine transporters", "GO:0015209", ["GO:0015856"], ["GO:0005886"]),
    "gntT": ("GntP-family gluconate transporters", "GO:0015128", ["GO:0035429"], ["GO:0005886"]),
    "PP_3641": ("NCS1 purine-cytosine/nucleobase permeases", "GO:0015205", ["GO:0015851"], ["GO:0005886"]),
    "PP_3655": ("NCS1 purine-cytosine/nucleobase permeases", "GO:0015205", ["GO:0015851"], ["GO:0005886"]),
    "pydP": ("NCS1 purine-cytosine/nucleobase permeases", "GO:0015205", ["GO:0015851"], ["GO:0005886"]),
    "PP_4309": ("NCS1 purine-cytosine/nucleobase permeases", "GO:0015205", ["GO:0015851"], ["GO:0005886"]),
    "PP_4921": ("CodB cytosine transporters", "GO:0015209", ["GO:0015856"], ["GO:0005886"]),
}

DESCRIPTIONS = {
    "PP_0138": (
        "PP_0138 encodes a SpmB/Gate-domain membrane protein with a nucleoside-transporter-like product name but no "
        "GOA transporter activity; first-pass curation leaves its molecular function unresolved."
    ),
    "PP_3048": (
        "PP_3048 encodes a prophage-associated phage attachment/head-tail connector domain protein; first-pass curation "
        "treats it as virion-assembly side context rather than a carbohydrate transporter."
    ),
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
    primary = info.get("primary")
    gene = info["gene"]

    if go_id == "GO:0005886":
        return review(
            info,
            "Plasma membrane localization is appropriate for this bacterial membrane protein.",
            "ACCEPT",
            "The UniProt/GOA membrane context supports plasma or inner-membrane localization.",
        )
    if go_id == "GO:0016020":
        if "GO:0005886" in info["go_ids"]:
            return review(
                info,
                "Generic membrane localization is true but less informative than plasma membrane.",
                "MARK_AS_OVER_ANNOTATED",
                "A more specific plasma-membrane annotation is present.",
            )
        return review(
            info,
            "Membrane localization is appropriate for this membrane-associated side-node protein.",
            "ACCEPT",
            "The UniProt/GOA membrane context supports this localization.",
        )
    if go_id in {"GO:0022857", "GO:0055085"}:
        if primary:
            return review(
                info,
                f"{label} is true but broad relative to the substrate/family-specific transporter call.",
                "MARK_AS_OVER_ANNOTATED",
                "A more informative transporter term is available for the core function.",
                [primary],
            )
        return review(
            info,
            f"{label} is broad transporter context but the substrate and transporter activity are unresolved.",
            "KEEP_AS_NON_CORE",
            "The first-pass evidence does not support a specific transporter molecular function.",
        )
    if go_id in {"GO:0015128", "GO:0035429"}:
        return review(
            info,
            f"{label} is appropriate for the GntP-family gluconate transporter.",
            "ACCEPT",
            "The product, GntP family, and gluconate-transporter domains support gluconate transmembrane transport.",
        )
    if go_id in {"GO:0015205", "GO:0015851"}:
        return review(
            info,
            f"{label} is appropriate broad NCS1-family nucleobase transport context.",
            "ACCEPT",
            "The purine-cytosine permease/NCS1 family evidence supports nucleobase transport, but not a narrower substrate for every paralog.",
        )
    if go_id in {"GO:0015209", "GO:0015856"}:
        return review(
            info,
            f"{label} is appropriate for the CodB-family cytosine transporter.",
            "ACCEPT",
            "The CodB/purine-cytosine permease family evidence supports cytosine transport.",
        )
    if go_id in {"GO:0034257", "GO:0034258"}:
        return review(
            info,
            f"{label} is appropriate for the PnuC nicotinamide-riboside transporter.",
            "ACCEPT",
            "The PnuC/NMN transporter family and product evidence support nicotinamide riboside transport.",
        )
    if go_id in {"GO:0004553", "GO:0005975"}:
        return review(
            info,
            f"{label} is appropriate enzyme/process context for the beta-glucanase side node.",
            "ACCEPT",
            "The beta-glucan modifier/glycoside hydrolase domain evidence supports carbohydrate hydrolysis rather than transporter function.",
        )
    if go_id == "GO:0019068":
        return review(
            info,
            "Virion assembly is appropriate prophage structural side context.",
            "ACCEPT",
            "The phage attachment/head-tail connector domains support prophage structural context rather than carbohydrate transport.",
        )
    if go_id == "GO:0016780":
        return review(
            info,
            "This broad phosphotransferase term is retained as conservative sugar-transferase family context.",
            "ACCEPT",
            "The bacterial sugar-transferase/undecaprenyl-phosphate glycosyltransferase domains support a membrane sugar-transferase side-node assignment, but a narrower GO term was not available in the local cache.",
        )

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
        out.append(
            new_annotation(
                info,
                primary,
                "enables",
                f"Adds {TERMS[primary]} for this transporter or enzyme profile.",
                "Product, domain, and Asta context support this conservative first-pass core term.",
            )
        )
    for process in info["processes"]:
        if process not in go_ids:
            out.append(
                new_annotation(
                    info,
                    process,
                    "involved_in",
                    f"Adds {TERMS[process]} process context.",
                    "The supported molecular function or side-node family implies this conservative process annotation.",
                )
            )
    for location in info["locations"]:
        if location not in go_ids:
            out.append(
                new_annotation(
                    info,
                    location,
                    "located_in",
                    f"Adds {TERMS[location]} localization context.",
                    "The UniProt/GOA membrane context supports this localization.",
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


def description(info: GeneInfo) -> str:
    gene = info["gene"]
    if gene in DESCRIPTIONS:
        return DESCRIPTIONS[gene]
    primary = info.get("primary")
    if primary:
        return f"{gene} encodes {info['product']}, curated in the {info['group']} subgroup with core {TERMS[primary]} context."
    return f"{gene} encodes {info['product']}, retained as unresolved side context in the carbohydrate/nucleoside transport bucket."


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
    doc["suggested_questions"] = [
        {"question": "What are the exact substrates, direction, and coupling mechanisms for the unresolved NCS1/Gate-domain transporter candidates?"}
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure uptake or growth rescue for candidate gluconate, cytosine, purine/pyrimidine, nucleoside, nicotinamide-riboside, or related substrates in knockout/complement strains and heterologous expression systems.",
            "experiment_type": "transport genetics and substrate uptake assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_carbohydrate_nucleoside_context",
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
                    "description": f"First-pass carbohydrate/nucleoside transport-bucket subgroup: {group}.",
                    "annotons": [module_annoton(info) for info in group_infos],
                },
            }
        )
    concept_ids = [
        "GO:0015128",
        "GO:0035429",
        "GO:0015205",
        "GO:0015851",
        "GO:0015209",
        "GO:0015856",
        "GO:0034257",
        "GO:0034258",
        "GO:0004553",
        "GO:0005975",
        "GO:0016780",
        "GO:0019068",
        "GO:0005886",
        "GO:0016020",
    ]
    doc = {
        "id": "MODULE:carbohydrate_nucleoside_transport_boundary",
        "title": "Carbohydrate and nucleoside transport boundary",
        "description": (
            "Boundary module for PSEPK non-ABC gluconate, nucleobase/cytosine, and nicotinamide-riboside "
            "transporters plus beta-glucanase, sugar-transferase, prophage, and low-confidence membrane side nodes."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK carbohydrate/nucleoside transporter batch",
                "statement": "The batch table records 14 PSEPK transport-bucket genes assigned to carbohydrate, nucleoside, nucleobase, and related side-node context.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_partition.tsv",
                "title": "PSEPK transport/membrane/efflux partition",
                "statement": "The parent transport partition separates this carbohydrate/nucleoside panel from ABC transporters, MFS/DMT, ion/metal, amino-acid/amine, redox, and low-information membrane buckets.",
            },
        ],
        "notes": (
            "First-pass interpretation: keep GntP gluconate, CodB/cytosine, NCS1/nucleobase, and PnuC calls where product and domains agree; keep PP_1740, PP_3048, and PP_3142 as enzyme/prophage side nodes; leave PP_0138 unresolved beyond membrane context."
        ),
        "module": {
            "id": "carbohydrate_nucleoside_transport_boundary",
            "label": "Carbohydrate and nucleoside transport boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [descriptor(go_id, "Concept used for first-pass carbohydrate/nucleoside transporter curation.") for go_id in concept_ids],
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
