#!/usr/bin/env python3
"""First-pass curation for DMT/EamA small drug/metabolite transporter split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = ROOT / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_dmt_eama_small_drug_metabolite_transporters.tsv"
MODULE_PATH = ROOT / "modules/dmt_eama_transport_boundary.yaml"

TAXON = {
    "id": "NCBITaxon:160488",
    "label": "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)",
}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0005886": "plasma membrane",
    "GO:0015199": "amino-acid betaine transmembrane transporter activity",
    "GO:0015220": "choline transmembrane transporter activity",
    "GO:0015297": "antiporter activity",
    "GO:0015871": "choline transport",
    "GO:0016020": "membrane",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0031460": "glycine betaine transport",
    "GO:0042910": "xenobiotic transmembrane transporter activity",
    "GO:0055085": "transmembrane transport",
    "GO:1990961": "xenobiotic detoxification by transmembrane export across the plasma membrane",
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
    interpro = row["interpro_ids"]
    if gene in {"sugE", "emrE"} or "small_multidrug_res" in interpro or "small multidrug" in product:
        return "smr_efflux"
    if "IPR004626" in interpro or "rard" in product or "chloramphenicol-sensitive" in product:
        return "rard_like"
    if "IPR051258" in interpro:
        return "diverse_substrate_eama"
    if "IPR004779" in interpro:
        return "co_aa_nh_transporter"
    if "IPR050638" in interpro or any(token in product for token in ("amino acid", "cysteine", "homoserine")):
        return "amino_acid_vitamin_eama"
    return "generic_eama"


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
        "function": first_line(uniprot_lines, "CC   -!- FUNCTION:", optional=True),
        "location_cell": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell membrane", optional=True),
        "location_membrane": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Membrane", optional=True),
        "kw_membrane": first_line(uniprot_lines, "KW   Membrane", optional=True),
        "family_eama": first_line(uniprot_lines, "CC   -!- SIMILARITY: Belongs to the EamA transporter family.", optional=True),
        "family_dmt": first_line(uniprot_lines, "CC   -!- SIMILARITY: Belongs to the drug/metabolite transporter (DMT)", optional=True),
        "interpro_eama": first_line(uniprot_lines, "DR   InterPro; IPR000620; EamA_dom.", optional=True),
        "interpro_emre": first_line(uniprot_lines, "DR   InterPro; IPR037185; EmrE-like.", optional=True),
        "interpro_rard": first_line(uniprot_lines, "DR   InterPro; IPR004626; RarD.", optional=True),
        "interpro_small_dmt": first_line(uniprot_lines, "DR   InterPro; IPR000390; Small_drug/metabolite_transptr.", optional=True),
        "interpro_smr": first_line(uniprot_lines, "DR   InterPro; IPR045324; Small_multidrug_res.", optional=True),
        "interpro_aa_vit": first_line(uniprot_lines, "DR   InterPro; IPR050638; AA-Vitamin_Transporters.", optional=True),
        "interpro_diverse": first_line(uniprot_lines, "DR   InterPro; IPR051258; Diverse_Substrate_Transporter.", optional=True),
        "interpro_co_aa_nh": first_line(uniprot_lines, "DR   InterPro; IPR004779; CO/AA/NH_transpt.", optional=True),
        "supfam_emre": first_line(uniprot_lines, "DR   SUPFAM; SSF103481; Multidrug resistance efflux transporter EmrE;", optional=True),
        "transmem": first_line(uniprot_lines, "FT   TRANSMEM", optional=True),
        "asta": first_line(asta_lines, "- **Protein Description:**"),
    }
    return {
        "gene": gene,
        "id": row["uniprot_accession"],
        "locus": row["ordered_locus"],
        "product": row["protein_name"],
        "category": category,
        "line_by_key": line_by_key,
        "go_ids": [ann["term"]["id"] for ann in review_doc.get("existing_annotations", [])],
        "existing_refs": {ref["id"]: ref for ref in review_doc.get("references", []) if "id" in ref},
    }


def core_keys(info: dict[str, object]) -> tuple[str, ...]:
    category = info["category"]
    if category == "smr_efflux":
        return ("de", "family_dmt", "interpro_emre", "interpro_small_dmt", "interpro_smr", "supfam_emre")
    if category == "rard_like":
        return ("de", "family_eama", "interpro_eama", "interpro_emre", "interpro_rard", "supfam_emre")
    if category == "diverse_substrate_eama":
        return ("de", "interpro_diverse", "interpro_eama", "interpro_emre")
    if category == "co_aa_nh_transporter":
        return ("de", "interpro_co_aa_nh", "interpro_eama", "interpro_emre")
    if category == "amino_acid_vitamin_eama":
        return ("de", "family_eama", "interpro_aa_vit", "interpro_eama", "interpro_emre")
    return ("de", "family_eama", "interpro_eama", "interpro_emre", "supfam_emre")


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
    if category == "smr_efflux":
        return f"{gene} encodes {product}, a small drug/metabolite resistance-family inner-membrane efflux transporter candidate."
    if category == "rard_like":
        return f"{gene} encodes {product}, a RarD/EamA-like membrane permease candidate with unresolved substrate specificity."
    if category in {"amino_acid_vitamin_eama", "co_aa_nh_transporter"}:
        return f"{gene} encodes {product}, an EamA-family membrane transporter candidate associated with amino-acid, vitamin, or related small-solute export context."
    if category == "diverse_substrate_eama":
        return f"{gene} encodes {product}, an EamA-domain diverse-substrate transporter candidate with unresolved substrate specificity."
    return f"{gene} encodes {product}, a predicted EamA/DMT-family transmembrane transporter with unresolved substrate specificity."


def replacement(go_id: str) -> list[dict[str, str]]:
    return [term(go_id)]


def review_for_annotation(info: dict[str, object], ann: dict[str, object]) -> dict[str, object]:
    go_id = ann["term"]["id"]
    category = info["category"]
    if go_id in {"GO:0005886", "GO:0016020"}:
        action = "ACCEPT"
        if go_id == "GO:0016020" and "GO:0005886" in info["go_ids"]:
            action = "KEEP_AS_NON_CORE"
        return {
            "summary": "The membrane localization matches the predicted multi-pass DMT/EamA transporter context.",
            "action": action,
            "reason": "The UniProt product, membrane keyword or subcellular-location, and DMT/EamA/EmrE transmembrane-domain evidence support membrane localization; plasma membrane is the more informative bacterial inner-membrane term when present.",
            "supported_by": support_lines(info, "de", "location_cell", "location_membrane", "kw_membrane", *core_keys(info)),
        }
    if go_id == "GO:0022857":
        return {
            "summary": "Broad transporter activity is supported by the DMT/EamA or SMR-family membrane-protein evidence.",
            "action": "KEEP_AS_NON_CORE" if category == "smr_efflux" else "ACCEPT",
            "reason": "The protein has DMT/EamA/EmrE-like transmembrane transporter evidence. For SMR-family efflux proteins this broad term is retained as non-core because xenobiotic/drug efflux is more informative.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0055085":
        return {
            "summary": "Broad transmembrane transport process context is appropriate for this DMT/EamA-family transporter candidate.",
            "action": "ACCEPT",
            "reason": "The product and DMT/EamA/EmrE-like domain evidence support a membrane-transport process while exact substrate specificity remains unresolved for most paralogs.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:1990961":
        return {
            "summary": "Xenobiotic export process context is appropriate for the SMR/SugE/EmrE-family efflux candidate.",
            "action": "ACCEPT" if category == "smr_efflux" else "KEEP_AS_NON_CORE",
            "reason": "The product and small multidrug resistance family evidence support an efflux/detoxification role at first-pass resolution, but exact substrates and physiological conditions remain unresolved.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0015199", "GO:0015220"}:
        return {
            "summary": "The choline/betaine substrate-specific transporter activity is over-specific for this SMR-family protein.",
            "action": "MODIFY",
            "reason": "The local product and family evidence support small multidrug/drug-metabolite efflux, but do not establish choline or amino-acid betaine as the transported substrate.",
            "proposed_replacement_terms": replacement("GO:0042910"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0015871", "GO:0031460"}:
        return {
            "summary": "The choline/glycine-betaine process annotation is over-specific for this SMR-family protein.",
            "action": "MODIFY",
            "reason": "The local product and family evidence support small multidrug/drug-metabolite efflux, but not a specific choline or glycine-betaine transport process.",
            "proposed_replacement_terms": replacement("GO:1990961"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0015297":
        return {
            "summary": "Broad antiporter activity is plausible SMR-family mechanism context but less informative than the efflux transporter assignment.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "Small multidrug resistance proteins are membrane efflux transporters, but this first-pass evidence does not resolve the coupled ion or substrate enough to make antiporter activity the core function.",
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
            "reason": "The product, family, and domain metadata support this transporter assignment in the first-pass review.",
            "supported_by": support_lines(info, *core_keys(info)),
        },
    }


def has_plasma_evidence(info: dict[str, object]) -> bool:
    lines = info["line_by_key"]
    return bool(lines.get("location_cell")) or "GO:0005886" in info["go_ids"]


def location_term_for_new(info: dict[str, object]) -> str:
    return "GO:0005886" if has_plasma_evidence(info) else "GO:0016020"


def add_missing_new_annotations(info: dict[str, object], annotations: list[dict[str, object]]) -> None:
    present = {ann["term"]["id"] for ann in annotations}

    def add(go_id: str, qualifier: str, summary: str | None = None) -> None:
        if go_id not in present:
            annotations.append(new_annotation(info, go_id, qualifier, summary))
            present.add(go_id)

    if not (present & {"GO:0005886", "GO:0016020"}):
        add(location_term_for_new(info), "located_in")
    if info["category"] == "smr_efflux":
        add("GO:0042910", "enables", "Adds xenobiotic/drug-efflux transporter activity for the SMR-family efflux candidate.")
        add("GO:1990961", "involved_in")
        return
    add("GO:0022857", "enables")
    add("GO:0055085", "involved_in")


def best_location(info: dict[str, object]) -> dict[str, str]:
    present = set(info["go_ids"])
    if "GO:0005886" in present or has_plasma_evidence(info):
        return term("GO:0005886")
    return term("GO:0016020")


def core_function_terms(info: dict[str, object]) -> tuple[str, list[str], str]:
    category = info["category"]
    if category == "smr_efflux":
        return "GO:0042910", ["GO:1990961"], "SMR-family drug/metabolite efflux transporter candidate."
    if category == "rard_like":
        return "GO:0022857", ["GO:0055085"], "RarD/EamA-like membrane transporter candidate with unresolved substrate specificity."
    if category == "amino_acid_vitamin_eama":
        return "GO:0022857", ["GO:0055085"], "EamA-family amino-acid, vitamin, or related small-solute transporter candidate."
    if category == "co_aa_nh_transporter":
        return "GO:0022857", ["GO:0055085"], "EamA-family carbon/nitrogen or amino-acid transporter candidate."
    if category == "diverse_substrate_eama":
        return "GO:0022857", ["GO:0055085"], "EamA-domain diverse-substrate transporter candidate."
    return "GO:0022857", ["GO:0055085"], "Generic EamA/DMT-family transmembrane transporter candidate with unresolved substrate specificity."


def core_functions(info: dict[str, object]) -> list[dict[str, object]]:
    mf, processes, desc = core_function_terms(info)
    core: dict[str, object] = {
        "description": desc,
        "molecular_function": term(mf),
        "locations": [best_location(info)],
        "supported_by": support_lines(info, *core_keys(info)),
    }
    if processes:
        core["directly_involved_in"] = [term(go_id) for go_id in processes]
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
        lines.get("function"),
        lines.get("location_cell"),
        lines.get("location_membrane"),
        lines.get("kw_membrane"),
        lines.get("family_eama"),
        lines.get("family_dmt"),
        lines.get("interpro_eama"),
        lines.get("interpro_emre"),
        lines.get("interpro_rard"),
        lines.get("interpro_small_dmt"),
        lines.get("interpro_smr"),
        lines.get("interpro_aa_vit"),
        lines.get("interpro_diverse"),
        lines.get("interpro_co_aa_nh"),
        lines.get("supfam_emre"),
        lines.get("transmem"),
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
                    "question": "What substrate, direction, coupling ion, and physiological condition apply to this DMT/EamA-family transporter in KT2440?"
                }
            ],
            "suggested_experiments": [
                {
                    "description": "Measure uptake or efflux of candidate substrates in wild-type, deletion, and complemented strains, prioritizing substrates suggested by product name, gene neighborhood, and DMT/EamA/SMR-family assignment.",
                    "experiment_type": "targeted transporter genetics and uptake/efflux assay",
                }
            ],
        }
    )
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def annoton(info: dict[str, object]) -> dict[str, object]:
    gene = info["gene"]
    core = core_functions(info)[0]
    entry: dict[str, object] = {
        "id": f"{gene}_dmt_eama_context",
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
    by_category: dict[str, list[dict[str, object]]] = {}
    for info in infos:
        by_category.setdefault(info["category"], []).append(info)
    doc = {
        "id": "MODULE:dmt_eama_transport_boundary",
        "title": "DMT/EamA small drug and metabolite transport boundary",
        "description": (
            "Boundary module for the PSEPK transport/membrane/efflux split containing DMT, EamA, RarD, YedA/RhtA, "
            "and SMR/SugE/EmrE-like small drug or metabolite transporter candidates. The module keeps substrate, "
            "direction, and coupling assignments conservative unless product or family evidence is specific."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK transport/membrane/efflux DMT/EamA transporter batch",
                "statement": "The partition groups 21 DMT/EamA/RarD/SMR-family transporter candidates for first-pass curation.",
            }
        ],
        "notes": (
            "First-pass interpretation: SMR/SugE/EmrE-family proteins are retained as efflux candidates. "
            "Most EamA/RarD-family paralogs remain broad transporter candidates because product and family evidence "
            "does not resolve the transported substrate, direction, or coupling ion."
        ),
        "module": {
            "id": "dmt_eama_transport_boundary",
            "label": "DMT/EamA small drug and metabolite transport boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                concept("GO:0022857", "Broad transporter activity for DMT/EamA-family candidates."),
                concept("GO:0055085", "Broad transport process for unresolved DMT/EamA-family candidates."),
                concept("GO:0042910", "Xenobiotic/drug transporter activity for SMR/SugE/EmrE-family efflux candidates."),
                concept("GO:1990961", "Xenobiotic detoxification/export process context for SMR-family efflux candidates."),
                concept("GO:0015297", "Antiporter activity retained as non-core mechanism context for SMR-family proteins where present in GOA."),
            ],
            "context": {
                "cellular_components": [
                    concept("GO:0005886", "Bacterial plasma/inner membrane location for resolved inner-membrane transporters."),
                    concept("GO:0016020", "Broad membrane context for low-resolution transporter candidates."),
                ]
            },
            "parts": [
                part(1, "SMR-family efflux candidates", "smr_family_efflux_candidates", "SMR-family efflux candidates", "SugE/EmrE-like small multidrug or drug/metabolite efflux candidates.", by_category.get("smr_efflux", [])),
                part(2, "RarD-like EamA permeases", "rard_like_eama_permeases", "RarD-like EamA permeases", "RarD-labeled and RarD-domain EamA transporter candidates with unresolved substrate specificity.", by_category.get("rard_like", [])),
                part(3, "Amino-acid and vitamin-associated EamA candidates", "amino_acid_vitamin_eama_candidates", "Amino-acid and vitamin-associated EamA candidates", "EamA-family proteins with amino-acid, vitamin, cysteine, homoserine, or related small-solute product/family context.", by_category.get("amino_acid_vitamin_eama", []) + by_category.get("co_aa_nh_transporter", [])),
                part(4, "Diverse-substrate EamA candidates", "diverse_substrate_eama_candidates", "Diverse-substrate EamA candidates", "EamA-domain proteins carrying the diverse-substrate-transporter family signal.", by_category.get("diverse_substrate_eama", [])),
                part(5, "Generic EamA/DMT membrane permeases", "generic_eama_dmt_membrane_permeases", "Generic EamA/DMT membrane permeases", "Generic EamA/DMT-family membrane proteins with broad transporter evidence but no resolved substrate.", by_category.get("generic_eama", [])),
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
