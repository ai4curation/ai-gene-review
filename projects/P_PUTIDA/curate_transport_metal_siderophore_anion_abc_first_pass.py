#!/usr/bin/env python3
"""First-pass curation for metal/siderophore/anion ABC transporter split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = ROOT / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_metal_siderophore_anion_abc_transporters.tsv"
MODULE_PATH = ROOT / "modules/metal_siderophore_anion_abc_transport_boundary.yaml"

TAXON = {
    "id": "NCBITaxon:160488",
    "label": "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)",
}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on inter-ontology links",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0000166": "nucleotide binding",
    "GO:0005524": "ATP binding",
    "GO:0005886": "plasma membrane",
    "GO:0006826": "iron ion transport",
    "GO:0016020": "membrane",
    "GO:0016887": "ATP hydrolysis activity",
    "GO:0020037": "heme binding",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0030001": "metal ion transport",
    "GO:0030313": "cell envelope",
    "GO:0033214": "siderophore-iron import into cell",
    "GO:0043190": "ATP-binding cassette (ABC) transporter complex",
    "GO:0046872": "metal ion binding",
    "GO:0055085": "transmembrane transport",
}


def term(go_id: str) -> dict[str, str]:
    return {"id": go_id, "label": TERMS[go_id]}


def ref_file(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def first_line(lines: list[str], *needles: str, optional: bool = False) -> str | None:
    for line in lines:
        if all(needle in line for needle in needles):
            return line
    if optional:
        return None
    raise ValueError(f"Could not find line containing {needles}")


def dedupe(items: list[str | None]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if not item or item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out


def load_rows() -> list[dict[str, str]]:
    with BATCH_PATH.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def classify(row: dict[str, str]) -> str:
    gene = row["gene"]
    product = row["protein_name"].lower()
    if "atp-binding" in product or "atpase" in product:
        return "abc_atpase"
    if "heme" in product and "binding" in product:
        return "heme_binding_protein"
    if "substrate-binding" in product:
        return "metal_binding_protein"
    if "heme" in product:
        return "heme_permease"
    if "siderophore" in product or gene == "fatD":
        return "ferric_siderophore_permease"
    return "iron_metal_permease"


def load_info(row: dict[str, str]) -> dict[str, object]:
    gene = row["gene"]
    uniprot_path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta_path = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    review_path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    uniprot_lines = uniprot_path.read_text(encoding="utf-8").splitlines()
    asta_lines = asta_path.read_text(encoding="utf-8").splitlines()
    review_doc = yaml.safe_load(review_path.read_text(encoding="utf-8"))
    category = classify(row)
    line_by_key = {
        "de": first_line(uniprot_lines, "DE   "),
        "location_cell": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell membrane", optional=True),
        "family": first_line(uniprot_lines, "CC   -!- SIMILARITY:", optional=True),
        "btu_like": first_line(uniprot_lines, "DR   InterPro; IPR037294; ABC_BtuC-like.", optional=True),
        "btu_permease": first_line(uniprot_lines, "DR   InterPro; IPR000522; ABC_transptr_permease_BtuC.", optional=True),
        "atpase": first_line(uniprot_lines, "DR   InterPro; IPR003593; AAA+_ATPase.", optional=True),
        "abc_atp": first_line(uniprot_lines, "DR   InterPro; IPR003439; ABC_transporter-like_ATP-bd.", optional=True),
        "siderophore_atpase": first_line(uniprot_lines, "DR   InterPro; IPR051535; Siderophore_ABC-ATPase.", optional=True),
        "metal_atpase": first_line(uniprot_lines, "DR   InterPro; IPR045508; DUF6482.", optional=True),
        "metal_binding": first_line(uniprot_lines, "DR   InterPro; IPR050492; Bact_metal-bind_prot9.", optional=True),
        "znua": first_line(uniprot_lines, "DR   InterPro; IPR006127; ZnuA-like.", optional=True),
        "heme_binding": first_line(uniprot_lines, "DR   InterPro; IPR050902; ABC_Transporter_SBP.", optional=True),
        "heme_periplasmic": first_line(uniprot_lines, "DR   InterPro; IPR002491; ABC_transptr_periplasmic_BD.", optional=True),
        "kw_iron": first_line(uniprot_lines, "KW   Iron transport", optional=True),
        "kw_membrane": first_line(uniprot_lines, "KW   Membrane", optional=True),
        "kw_signal": first_line(uniprot_lines, "KW   Signal", optional=True),
        "asta": first_line(asta_lines, "- **Protein Description:**"),
    }
    return {
        "gene": gene,
        "id": row["uniprot_accession"],
        "product": row["protein_name"],
        "category": category,
        "line_by_key": line_by_key,
        "go_ids": [ann["term"]["id"] for ann in review_doc.get("existing_annotations", [])],
        "existing_refs": {ref["id"]: ref for ref in review_doc.get("references", []) if "id" in ref},
    }


def core_keys(info: dict[str, object]) -> tuple[str, ...]:
    category = info["category"]
    if category == "abc_atpase":
        return ("de", "family", "atpase", "abc_atp", "siderophore_atpase", "metal_atpase", "kw_iron")
    if category == "heme_binding_protein":
        return ("de", "heme_binding", "heme_periplasmic", "kw_signal")
    if category == "metal_binding_protein":
        return ("de", "metal_binding", "znua", "kw_signal")
    return ("de", "location_cell", "family", "btu_like", "btu_permease", "kw_membrane", "kw_iron")


def support_lines(info: dict[str, object], *keys: str) -> list[dict[str, str]]:
    gene = info["gene"]
    lines = info["line_by_key"]
    uniprot_ref = ref_file(gene, "uniprot.txt")
    asta_ref = ref_file(gene, "deep-research-asta.md")
    requested = [lines.get(key) for key in (keys or core_keys(info))]
    requested.append(lines["asta"])
    out: list[dict[str, str]] = []
    for line in dedupe(requested):
        out.append(support(asta_ref if line == lines["asta"] else uniprot_ref, line))
    return out


def description(info: dict[str, object]) -> str:
    gene = info["gene"]
    product = info["product"]
    category = info["category"]
    if category == "abc_atpase":
        return f"{gene} encodes {product}, an ATP-hydrolyzing component of a predicted metal or siderophore ABC importer."
    if category == "heme_binding_protein":
        return f"{gene} encodes {product}, a periplasmic heme/hemin-binding component of a predicted ABC importer."
    if category == "metal_binding_protein":
        return f"{gene} encodes {product}, a metal-binding substrate-binding component of a predicted ABC importer."
    if category == "heme_permease":
        return f"{gene} encodes {product}, an inner-membrane permease component of a predicted heme/hemin ABC importer."
    return f"{gene} encodes {product}, an inner-membrane permease or component of a predicted iron/siderophore ABC importer."


def replacement(go_id: str) -> list[dict[str, str]]:
    return [term(go_id)]


def review_for_annotation(info: dict[str, object], ann: dict[str, object]) -> dict[str, object]:
    go_id = ann["term"]["id"]
    gene = info["gene"]
    category = info["category"]
    if go_id in {"GO:0005886", "GO:0016020"}:
        return {
            "summary": "The membrane localization matches the ABC importer permease or ATPase-associated transporter context.",
            "action": "KEEP_AS_NON_CORE" if go_id == "GO:0016020" and "GO:0005886" in info["go_ids"] else "ACCEPT",
            "reason": "The product, subcellular-location, membrane keyword, and ABC transporter family evidence support membrane localization.",
            "supported_by": support_lines(info, "de", "location_cell", "kw_membrane", *core_keys(info)),
        }
    if go_id in {"GO:0000166", "GO:0005524"}:
        return {
            "summary": "Nucleotide/ATP binding is supported for the ABC ATPase but is less informative than ATP hydrolysis.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The ATPase component carries ABC transporter ATP-binding evidence; ATP hydrolysis better captures the active energy-coupling function.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0016887":
        return {
            "summary": "ATP hydrolysis activity is appropriate for the ABC ATPase component.",
            "action": "ACCEPT",
            "reason": "The product and ABC ATPase domains support ATP hydrolysis as the energy-coupling activity for a metal/siderophore importer.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0022857", "GO:0055085"}:
        return {
            "summary": "Broad transporter activity/process context is appropriate for this ABC permease component.",
            "action": "ACCEPT",
            "reason": "The BtuC-like ABC permease evidence supports a transmembrane transporter component while exact substrate/system pairing remains at family-level resolution.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0033214":
        if category == "ferric_siderophore_permease":
            return {
                "summary": "Ferric-siderophore import is appropriate for the ferric siderophore/FatD permease context.",
                "action": "ACCEPT",
                "reason": "The product and BtuC-like permease evidence support ferric-siderophore ABC import context.",
                "supported_by": support_lines(info, *core_keys(info)),
            }
        return {
            "summary": "Siderophore-iron import is too specific for this non-siderophore-labeled permease.",
            "action": "MODIFY",
            "reason": "The product supports iron or heme/hemin ABC permease context, but not siderophore-iron import specifically.",
            "proposed_replacement_terms": replacement("GO:0006826" if gene == "PP_2417" else "GO:0055085"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0030001", "GO:0046872"}:
        return {
            "summary": "Metal ion transport/binding context is appropriate for this metal-binding ABC substrate-binding protein.",
            "action": "ACCEPT",
            "reason": "The product, ZnuA-like, and bacterial metal-binding protein family evidence support metal-binding/import context.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    raise ValueError(f"Unhandled annotation {info['gene']} {go_id} {ann['term']['label']}")


def new_annotation(info: dict[str, object], go_id: str, qualifier: str, summary: str | None = None) -> dict[str, object]:
    return {
        "term": term(go_id),
        "evidence_type": "IEA",
        "original_reference_id": ref_file(info["gene"], "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": summary or f"Adds {TERMS[go_id]} as a conservative first-pass term absent from fetched GOA rows.",
            "action": "NEW",
            "reason": "The product, family, and domain metadata support this ABC importer component assignment in the first-pass review.",
            "supported_by": support_lines(info, *core_keys(info)),
        },
    }


def add_missing_new_annotations(info: dict[str, object], annotations: list[dict[str, object]]) -> None:
    present = {ann["term"]["id"] for ann in annotations}

    def add(go_id: str, qualifier: str, summary: str | None = None) -> None:
        if go_id not in present:
            annotations.append(new_annotation(info, go_id, qualifier, summary))
            present.add(go_id)

    category = info["category"]
    if not (present & {"GO:0005886", "GO:0016020", "GO:0030313"}):
        add("GO:0030313" if category in {"metal_binding_protein", "heme_binding_protein"} else "GO:0005886", "located_in")
    if category == "abc_atpase":
        add("GO:0016887", "enables")
        add("GO:0030001", "involved_in")
    elif category == "heme_binding_protein":
        add("GO:0020037", "enables")
    elif category == "metal_binding_protein":
        add("GO:0046872", "enables")
        add("GO:0030001", "involved_in")
    elif category == "heme_permease":
        add("GO:0022857", "enables")
        add("GO:0055085", "involved_in")
    elif category == "iron_metal_permease":
        add("GO:0022857", "enables")
        add("GO:0006826", "involved_in")


def core_function_terms(info: dict[str, object]) -> tuple[str | None, list[str], str, str]:
    category = info["category"]
    if category == "abc_atpase":
        return "GO:0016887", ["GO:0030001"], "GO:0005886", "ATP-hydrolyzing ABC ATPase component of a metal/siderophore importer."
    if category == "heme_binding_protein":
        return "GO:0020037", [], "GO:0030313", "Periplasmic heme/hemin-binding ABC importer component."
    if category == "metal_binding_protein":
        return "GO:0046872", ["GO:0030001"], "GO:0030313", "Metal-binding substrate-binding component of a metal ABC importer."
    if category == "ferric_siderophore_permease":
        return "GO:0022857", ["GO:0033214"], "GO:0005886", "Ferric-siderophore ABC importer permease component."
    if category == "heme_permease":
        return "GO:0022857", ["GO:0055085"], "GO:0005886", "Heme/hemin ABC importer permease component."
    return "GO:0022857", ["GO:0006826"], "GO:0005886", "Iron/metal ABC importer permease component."


def core_functions(info: dict[str, object]) -> list[dict[str, object]]:
    mf, processes, loc, desc = core_function_terms(info)
    core: dict[str, object] = {
        "description": desc,
        "locations": [term(loc)],
        "supported_by": support_lines(info, *core_keys(info)),
    }
    if mf:
        core["molecular_function"] = term(mf)
    if processes:
        core["directly_involved_in"] = [term(go_id) for go_id in processes]
    if info["category"] not in {"metal_binding_protein", "heme_binding_protein"}:
        core["in_complex"] = term("GO:0043190")
    return [core]


def references_for(info: dict[str, object], annotations: list[dict[str, object]]) -> list[dict[str, object]]:
    refs: list[dict[str, object]] = []
    existing_refs = info["existing_refs"]
    for ref_id in sorted({ann.get("original_reference_id") for ann in annotations if ann.get("original_reference_id")}):
        if ref_id.startswith("file:"):
            continue
        refs.append(existing_refs.get(ref_id, {"id": ref_id, "title": GO_REF_TITLES.get(ref_id, ref_id), "findings": []}))
    lines = info["line_by_key"]
    uniprot_lines = [
        lines["de"],
        lines.get("location_cell"),
        lines.get("family"),
        lines.get("btu_like"),
        lines.get("btu_permease"),
        lines.get("atpase"),
        lines.get("abc_atp"),
        lines.get("siderophore_atpase"),
        lines.get("metal_atpase"),
        lines.get("metal_binding"),
        lines.get("znua"),
        lines.get("heme_binding"),
        lines.get("heme_periplasmic"),
        lines.get("kw_iron"),
        lines.get("kw_membrane"),
        lines.get("kw_signal"),
    ]
    refs.append(
        {
            "id": ref_file(info["gene"], "uniprot.txt"),
            "title": f"UniProtKB entry for {info['gene']} ({info['id']})",
            "findings": [{"supporting_text": line} for line in dedupe(uniprot_lines)],
        }
    )
    refs.append(
        {
            "id": ref_file(info["gene"], "deep-research-asta.md"),
            "title": f"Asta retrieval report for {info['gene']} ({info['id']})",
            "findings": [{"supporting_text": lines["asta"]}],
        }
    )
    return refs


def write_gene(info: dict[str, object]) -> None:
    gene = info["gene"]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    annotations = [
        ann
        for ann in doc.get("existing_annotations", [])
        if not (ann.get("review", {}).get("action") == "NEW" and ann.get("original_reference_id") == ref_file(gene, "uniprot.txt"))
    ]
    for ann in annotations:
        ann["review"] = review_for_annotation(info, ann)
    add_missing_new_annotations(info, annotations)
    doc.update(
        {
            "id": info["id"],
            "gene_symbol": gene,
            "product_type": "PROTEIN",
            "status": "DRAFT",
            "taxon": TAXON,
            "description": description(info),
            "existing_annotations": annotations,
            "references": references_for(info, annotations),
            "core_functions": core_functions(info),
            "proposed_new_terms": [],
            "suggested_questions": [
                {
                    "question": "Which metal, siderophore, heme, or inorganic substrate and partner subunits define this ABC importer in KT2440?"
                }
            ],
            "suggested_experiments": [
                {
                    "description": "Measure metal, siderophore, heme/hemin, or phosphate uptake in wild-type, deletion, and complemented strains, pairing ATPase, permease, and substrate-binding genes from the same locus where possible.",
                    "experiment_type": "ABC importer genetics and uptake assay",
                }
            ],
        }
    )
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def annoton(info: dict[str, object]) -> dict[str, object]:
    gene = info["gene"]
    core = core_functions(info)[0]
    entry = {
        "id": f"{gene}_metal_siderophore_abc_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {info['product']}",
        "function": {"preferred_term": core["molecular_function"]["label"], "term": core["molecular_function"]},
        "locations": [{"preferred_term": loc["label"], "term": loc} for loc in core.get("locations", [])],
    }
    if core.get("directly_involved_in"):
        entry["processes"] = [{"preferred_term": proc["label"], "term": proc} for proc in core["directly_involved_in"]]
    return entry


def concept(go_id: str, description_text: str) -> dict[str, object]:
    return {"preferred_term": TERMS[go_id], "term": term(go_id), "description": description_text}


def part(order: int, role: str, node_id: str, label: str, description_text: str, infos: list[dict[str, object]]) -> dict[str, object]:
    return {
        "order": order,
        "role": role,
        "node": {
            "id": node_id,
            "label": label,
            "module_type": "TRANSPORT_STEP",
            "description": description_text,
            "annotons": [annoton(info) for info in infos],
        },
    }


def write_module(infos: list[dict[str, object]]) -> None:
    by_gene = {info["gene"]: info for info in infos}
    doc = {
        "id": "MODULE:metal_siderophore_anion_abc_transport_boundary",
        "title": "Metal, siderophore, and anion ABC transport boundary",
        "description": "Boundary module for PSEPK ABC importer components associated with iron, ferric siderophores, heme/hemin, phosphate, and generic metal substrates.",
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK transport/membrane/efflux metal/siderophore/anion ABC transporter batch",
                "statement": "The partition groups 11 ATPase, permease, and substrate-binding components for first-pass metal/siderophore/anion ABC importer curation.",
            }
        ],
        "notes": "First-pass interpretation: keep ATPase, permease, and substrate-binding roles component-level. Ferric-siderophore import is retained only for ferric-siderophore/FatD permeases; iron/heme/generic metal components are broadened where needed.",
        "module": {
            "id": "metal_siderophore_anion_abc_transport_boundary",
            "label": "Metal, siderophore, and anion ABC transport boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                concept("GO:0016887", "ATP hydrolysis activity for ABC ATPase components."),
                concept("GO:0022857", "Transmembrane transporter activity for ABC permease components."),
                concept("GO:0033214", "Ferric-siderophore import process for ferric-siderophore/FatD permeases."),
                concept("GO:0006826", "Iron transport context for iron ABC components."),
                concept("GO:0030001", "Metal ion transport context for generic metal ABC components."),
                concept("GO:0046872", "Metal ion binding for substrate-binding proteins."),
                concept("GO:0020037", "Heme binding for heme/hemin substrate-binding proteins."),
            ],
            "context": {
                "cellular_components": [
                    concept("GO:0005886", "Inner membrane location for ATPase/permease importer components."),
                    concept("GO:0030313", "Cell-envelope/periplasmic context for substrate-binding proteins."),
                    concept("GO:0043190", "ABC transporter complex context for importer components."),
                ]
            },
            "parts": [
                part(1, "Iron ABC importer candidate", "iron_abc_importer_candidate", "Iron ABC importer candidate", "PP_2416/PP_2417 ATPase and permease context, kept broader than siderophore-specific import.", [by_gene["PP_2416"], by_gene["PP_2417"]]),
                part(2, "Ferric siderophore ABC importer candidates", "ferric_siderophore_abc_importer_candidates", "Ferric siderophore ABC importer candidates", "PP_2592/PP_2593/fatD ferric-siderophore or ferric-anguibactin ABC importer components.", [by_gene["PP_2592"], by_gene["PP_2593"], by_gene["fatD"]]),
                part(3, "Generic metal and phosphate binding context", "generic_metal_phosphate_abc_context", "Generic metal and phosphate binding context", "Low-resolution metal ATPases and substrate-binding proteins including phosphate and ZnuA-like metal-binding candidates.", [by_gene["PP_2731"], by_gene["PP_2821"], by_gene["PP_3804"], by_gene["PP_4933"]]),
                part(4, "Heme/hemin ABC importer candidate", "heme_hemin_abc_importer_candidate", "Heme/hemin ABC importer candidate", "PP_4688/PP_4689 heme/hemin permease and substrate-binding components.", [by_gene["PP_4688"], by_gene["PP_4689"]]),
            ],
        },
    }
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    infos = [load_info(row) for row in load_rows()]
    for info in infos:
        write_gene(info)
    write_module(infos)
    print(f"Wrote {len(infos)} gene reviews and {MODULE_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
