#!/usr/bin/env python3
"""First-pass curation for TonB-dependent outer-membrane receptor split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = (
    ROOT
    / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_tonb_dependent_outer_membrane_receptors.tsv"
)
MODULE_PATH = ROOT / "modules/tonb_dependent_transport_boundary.yaml"
PRESERVE_GENE_REVIEWS = {"fpvA"}


TAXON = {
    "id": "NCBITaxon:160488",
    "label": "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)",
}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on on inter-ontology links",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0006829": "zinc ion transport",
    "GO:0009279": "cell outer membrane",
    "GO:0015232": "heme transmembrane transporter activity",
    "GO:0015343": "siderophore-iron transmembrane transporter activity",
    "GO:0015344": "siderophore uptake transmembrane transporter activity",
    "GO:0015675": "nickel cation transport",
    "GO:0015886": "heme transport",
    "GO:0015889": "cobalamin transport",
    "GO:0015891": "siderophore transport",
    "GO:0019867": "outer membrane",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0033214": "siderophore-iron import into cell",
    "GO:0038023": "signaling receptor activity",
    "GO:0044718": "siderophore transmembrane transport",
    "GO:0055085": "transmembrane transport",
}

SIDEROPHORE_TERMS = {"GO:0015343", "GO:0015344", "GO:0015891", "GO:0033214", "GO:0044718"}


def ref_file(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def term(go_id: str, label: str | None = None) -> dict[str, str]:
    return {"id": go_id, "label": label or TERMS[go_id]}


def support(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def first_line(lines: list[str], *needles: str, optional: bool = False) -> str | None:
    for line in lines:
        if all(needle in line for needle in needles):
            return line
    if optional:
        return None
    raise ValueError(f"Could not find line containing: {needles}")


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


def classify(product: str, uniprot_text: str) -> str:
    lower = product.lower()
    if "pseudopaline" in lower or " cnto" in lower:
        return "cnto"
    if "heme" in lower:
        return "heme"
    if "b12" in lower or "cobalamin" in uniprot_text:
        return "b12"
    if "copper" in lower or "IPR010100" in uniprot_text:
        return "copper"
    if any(
        token in lower
        for token in (
            "ferric",
            "ferrichrome",
            "ferripyoverdine",
            "aerobactin",
            "feca",
            "siderophore",
        )
    ):
        return "ferric_siderophore"
    if "IPR010105" in uniprot_text:
        return "ferric_siderophore"
    return "generic"


def load_info(row: dict[str, str]) -> dict[str, object]:
    gene = row["gene"]
    uniprot_path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta_path = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    review_path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    uniprot_lines = uniprot_path.read_text(encoding="utf-8").splitlines()
    asta_lines = asta_path.read_text(encoding="utf-8").splitlines()
    review_doc = yaml.safe_load(review_path.read_text(encoding="utf-8"))
    uniprot_text = "\n".join(uniprot_lines)
    product = row["protein_name"]
    category = classify(product, uniprot_text)

    line_by_key = {
        "de": first_line(uniprot_lines, "DE   "),
        "location": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell outer membrane", optional=True),
        "family": first_line(uniprot_lines, "Belongs to the TonB-dependent receptor family", optional=True),
        "barrel_domain": first_line(uniprot_lines, "DR   InterPro; IPR000531; Beta-barrel_TonB.", optional=True),
        "receptor_like": first_line(uniprot_lines, "DR   InterPro; IPR039426; TonB-dep_rcpt-like.", optional=True),
        "siderophore_domain": first_line(uniprot_lines, "DR   InterPro; IPR010105; TonB_sidphr_rcpt.", optional=True),
        "feca_domain": first_line(uniprot_lines, "DR   InterPro; IPR049654; FecA-like.", optional=True),
        "heme_domain": first_line(uniprot_lines, "DR   InterPro; IPR011276; TonB_haem/Hb_rcpt.", optional=True),
        "copper_domain": first_line(uniprot_lines, "DR   InterPro; IPR010100; TonB-dep_Cu_rcpt.", optional=True),
        "cnto_function": first_line(uniprot_lines, "FUNCTION: Transports the metallophore pseudopaline", optional=True),
        "cnto_metals": first_line(uniprot_lines, "in the acquisition of nickel and zinc", optional=True),
        "cobalamin_go": first_line(uniprot_lines, "DR   GO; GO:0015889; P:cobalamin transport", optional=True),
        "heme_mf_go": first_line(uniprot_lines, "DR   GO; GO:0015232; F:heme transmembrane transporter activity", optional=True),
        "heme_bp_go": first_line(uniprot_lines, "DR   GO; GO:0015886; P:heme transport", optional=True),
        "asta": first_line(asta_lines, "- **Protein Description:**"),
    }

    return {
        "gene": gene,
        "id": row["uniprot_accession"],
        "product": product,
        "category": category,
        "line_by_key": line_by_key,
        "go_ids": [ann["term"]["id"] for ann in review_doc.get("existing_annotations", [])],
    }


def support_lines(info: dict[str, object], *keys: str) -> list[dict[str, str]]:
    gene = info["gene"]
    lines = info["line_by_key"]
    uniprot_ref = ref_file(gene, "uniprot.txt")
    asta_ref = ref_file(gene, "deep-research-asta.md")
    requested = [lines.get(key) for key in keys]
    if not requested:
        requested = [lines["de"], lines.get("family"), lines.get("barrel_domain")]
    requested.append(lines["asta"])

    refs: list[dict[str, str]] = []
    for line in dedupe(requested):
        ref_id = asta_ref if line == lines["asta"] else uniprot_ref
        refs.append(support(ref_id, line))
    return refs


def description(info: dict[str, object]) -> str:
    gene = info["gene"]
    product = info["product"]
    category = info["category"]
    if category == "cnto":
        return (
            f"{gene} encodes a CntO-family TonB-dependent outer-membrane receptor predicted to import "
            "pseudopaline-metal complexes. UniProt metadata links CntO to pseudopaline-mediated acquisition "
            "of nickel and zinc, and the protein carries TonB-dependent receptor barrel/plug features. The "
            "supported role is metallophore-mediated metal uptake rather than a ferric-siderophore-specific receptor."
        )
    if category == "heme":
        return (
            f"{gene} encodes a TonB-dependent outer-membrane heme receptor. The protein has the "
            "beta-barrel/plug architecture of TonB-dependent receptors and heme/Hb-receptor family signatures, "
            "supporting heme uptake across the outer membrane as its primary substrate-specific role."
        )
    if category == "b12":
        return (
            f"{gene} encodes a B12-family TonB-dependent outer-membrane receptor. The protein is predicted to "
            "act in cobalamin uptake through a TonB-dependent receptor beta-barrel/plug architecture; a more "
            "specific molecular activity is not resolved from lightweight metadata."
        )
    if category == "copper":
        return (
            f"{gene} encodes OprC, a TonB-dependent outer-membrane copper-receptor-family protein. It carries "
            "TonB-dependent receptor barrel/plug features and a copper-receptor family signature, supporting a "
            "metal-uptake receptor role while leaving the exact transported copper species unresolved."
        )
    if category == "ferric_siderophore":
        return (
            f"{gene} encodes a TonB-dependent outer-membrane receptor in the ferric siderophore receptor class "
            f"({product}). The protein is predicted to mediate energy-dependent uptake of an iron-loaded "
            "siderophore or related ferric complex across the outer membrane through its TonB-dependent "
            "beta-barrel/plug receptor architecture."
        )
    return (
        f"{gene} encodes a predicted TonB-dependent receptor protein. The available metadata support a "
        "TonB-dependent receptor-like beta-barrel/plug protein, but do not resolve the transported ligand; "
        "substrate-specific siderophore claims should therefore be treated conservatively."
    )


def replacement_terms(category: str, go_id: str) -> list[dict[str, str]]:
    if category == "cnto":
        if go_id in {"GO:0015343", "GO:0015344"}:
            return [term("GO:0022857")]
        return [term("GO:0015675"), term("GO:0006829")]
    if category == "heme":
        if go_id in {"GO:0015343", "GO:0015344"}:
            return [term("GO:0015232")]
        return [term("GO:0015886")]
    if category == "b12":
        if go_id in {"GO:0015343", "GO:0015344"}:
            return [term("GO:0022857")]
        return [term("GO:0015889")]
    if category == "copper":
        if go_id in {"GO:0015343", "GO:0015344"}:
            return [term("GO:0022857")]
        return [term("GO:0055085")]
    return [term("GO:0022857")] if go_id.startswith("GO:00153") else [term("GO:0055085")]


def review_for_annotation(info: dict[str, object], go_id: str, label: str) -> dict[str, object]:
    category = info["category"]
    product = info["product"]

    if go_id == "GO:0009279":
        return {
            "summary": "Cell outer membrane localization is appropriate for this TonB-dependent receptor-family protein.",
            "action": "ACCEPT",
            "reason": "The UniProt entry places the protein at the cell outer membrane and the receptor-family architecture is consistent with a Gram-negative outer-membrane TonB-dependent receptor.",
            "supported_by": support_lines(info, "location", "barrel_domain"),
        }
    if go_id == "GO:0019867":
        return {
            "summary": "Outer membrane localization is correct but less specific than the bacterial cell outer membrane annotation.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The broader outer membrane row is retained as true location context, while GO:0009279 carries the more specific localization for this receptor.",
            "supported_by": support_lines(info, "location", "barrel_domain"),
        }
    if go_id == "GO:0038023":
        return {
            "summary": "A signaling-receptor role is plausible for STN-domain TonB receptor proteins but should remain secondary to transport.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The row is based on receptor-domain inference. For this first pass, transport is treated as the core role and signaling is retained as non-core domain-supported context.",
            "supported_by": support_lines(info, "family", "siderophore_domain", "feca_domain", "barrel_domain"),
        }
    if go_id in SIDEROPHORE_TERMS:
        if category == "ferric_siderophore":
            return {
                "summary": "The siderophore or siderophore-iron transport annotation matches the predicted ferric-siderophore receptor role.",
                "action": "ACCEPT",
                "reason": f"The product is annotated as {product}, and the UniProt/Asta metadata support a TonB-dependent ferric-siderophore receptor-family protein.",
                "supported_by": support_lines(info, "de", "siderophore_domain", "feca_domain", "barrel_domain"),
            }
        if category in {"cnto", "heme", "b12", "copper"}:
            category_reason = {
                "cnto": "the protein is a CntO pseudopaline-metal receptor rather than a ferric-siderophore receptor",
                "heme": "the protein is a heme receptor with heme-receptor domain support",
                "b12": "the protein is a B12-family receptor with cobalamin-transport support",
                "copper": "the protein is an OprC copper-receptor-family protein",
            }[category]
            return {
                "summary": f"The siderophore-specific term is too substrate-specific because {category_reason}.",
                "action": "MODIFY",
                "reason": "The TonB-dependent receptor architecture supports outer-membrane uptake, but the available product/domain evidence points to a different substrate class or only a generic receptor role.",
                "proposed_replacement_terms": replacement_terms(category, go_id),
                "supported_by": support_lines(
                    info,
                    "de",
                    "cnto_function",
                    "cnto_metals",
                    "heme_domain",
                    "copper_domain",
                    "cobalamin_go",
                    "barrel_domain",
                ),
            }
        return {
            "summary": "A siderophore-related family inference is plausible but the ligand is not resolved for this generic TonB-dependent receptor.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The protein has TonB-dependent receptor metadata, but neither product name nor domain evidence identifies a specific siderophore or ferric complex. Retain the automated inference as non-core until substrate evidence is available.",
            "supported_by": support_lines(info, "de", "family", "barrel_domain", "receptor_like"),
        }
    if go_id in {"GO:0015232", "GO:0015886"}:
        return {
            "summary": "The heme transport annotation matches the predicted outer-membrane heme receptor role.",
            "action": "ACCEPT",
            "reason": "The protein is annotated as an outer membrane heme receptor and carries heme/Hb-receptor family support.",
            "supported_by": support_lines(info, "de", "heme_domain", "heme_mf_go", "heme_bp_go"),
        }
    if go_id == "GO:0015889":
        return {
            "summary": "Cobalamin transport is the appropriate process for this B12-family TonB-dependent receptor.",
            "action": "ACCEPT",
            "reason": "The product is a B12-family TonB-dependent receptor and UniProt carries a cobalamin transport GO row.",
            "supported_by": support_lines(info, "de", "cobalamin_go", "barrel_domain"),
        }
    if go_id in {"GO:0006829", "GO:0015675"}:
        return {
            "summary": "Metal-ion transport is consistent with a CntO pseudopaline-metal receptor.",
            "action": "ACCEPT",
            "reason": "The UniProt function text links CntO to pseudopaline-mediated nickel and zinc acquisition.",
            "supported_by": support_lines(info, "cnto_function", "cnto_metals", "barrel_domain"),
        }
    if go_id in {"GO:0022857", "GO:0055085"}:
        return {
            "summary": "The broad transporter annotation is true but less informative than the substrate-specific receptor rows when those are available.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "TonB-dependent receptor architecture supports a transport role, but the heme, cobalamin, metal, or siderophore-specific terms capture the informative substrate context where supported.",
            "supported_by": support_lines(info, "de", "family", "barrel_domain", "receptor_like"),
        }
    raise ValueError(f"Unhandled annotation {info['gene']} {go_id} {label}")


def core_support_keys(info: dict[str, object]) -> tuple[str, ...]:
    category = info["category"]
    if category == "cnto":
        return ("cnto_function", "cnto_metals", "barrel_domain")
    if category == "heme":
        return ("de", "heme_domain", "heme_mf_go", "heme_bp_go")
    if category == "b12":
        return ("de", "cobalamin_go", "barrel_domain")
    if category == "copper":
        return ("de", "copper_domain", "barrel_domain")
    if category == "ferric_siderophore":
        return ("de", "siderophore_domain", "feca_domain", "barrel_domain")
    return ("de", "family", "barrel_domain", "receptor_like")


def core_function(info: dict[str, object], annotations: list[dict[str, object]]) -> dict[str, object]:
    category = info["category"]
    go_ids = {ann["term"]["id"] for ann in annotations} or set(info.get("go_ids", []))
    has_location = "GO:0009279" in go_ids or info["line_by_key"].get("location")

    if category == "cnto":
        core = {
            "description": "TonB-dependent CntO-family receptor for pseudopaline-metal complex uptake, linked to nickel and zinc acquisition.",
            "molecular_function": term("GO:0022857"),
            "directly_involved_in": [term("GO:0015675"), term("GO:0006829")],
            "supported_by": support_lines(info, *core_support_keys(info)),
        }
    elif category == "heme":
        core = {
            "description": "TonB-dependent outer-membrane heme receptor that mediates heme uptake.",
            "molecular_function": term("GO:0015232"),
            "directly_involved_in": [term("GO:0015886")],
            "supported_by": support_lines(info, *core_support_keys(info)),
        }
    elif category == "b12":
        core = {
            "description": "B12-family TonB-dependent receptor involved in cobalamin uptake.",
            "molecular_function": term("GO:0022857"),
            "directly_involved_in": [term("GO:0015889")],
            "supported_by": support_lines(info, *core_support_keys(info)),
        }
    elif category == "copper":
        core = {
            "description": "OprC-family TonB-dependent outer-membrane copper receptor with unresolved transported copper species.",
            "molecular_function": term("GO:0022857"),
            "directly_involved_in": [term("GO:0055085")],
            "supported_by": support_lines(info, *core_support_keys(info)),
        }
    elif category == "ferric_siderophore":
        mf = "GO:0015343" if "GO:0015343" in go_ids else "GO:0015344"
        process = "GO:0033214" if "GO:0033214" in go_ids else ("GO:0015891" if "GO:0015891" in go_ids else "GO:0044718")
        core = {
            "description": "TonB-dependent outer-membrane ferric-siderophore receptor mediating uptake of an iron-loaded siderophore or related ferric complex.",
            "molecular_function": term(mf),
            "directly_involved_in": [term(process)],
            "supported_by": support_lines(info, *core_support_keys(info)),
        }
    else:
        core = {
            "description": "Predicted TonB-dependent receptor-like transporter with unresolved ligand specificity.",
            "molecular_function": term("GO:0022857"),
            "directly_involved_in": [term("GO:0055085")],
            "supported_by": support_lines(info, *core_support_keys(info)),
        }

    if has_location:
        core["locations"] = [term("GO:0009279")]
    return core


def replacement_ids(annotations: list[dict[str, object]]) -> set[str]:
    ids: set[str] = set()
    for ann in annotations:
        for replacement in ann.get("review", {}).get("proposed_replacement_terms", []):
            if replacement.get("id"):
                ids.add(replacement["id"])
    return ids


def new_annotation(info: dict[str, object], target: dict[str, str], qualifier: str) -> dict[str, object]:
    return {
        "term": target,
        "evidence_type": "IEA",
        "original_reference_id": ref_file(info["gene"], "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": f"Adds {target['label']} as the review-supported core term missing from the fetched GOA rows.",
            "action": "NEW",
            "reason": "The lightweight UniProt/Asta evidence supports this broader receptor transport term, while the fetched GOA rows either lack a molecular function/process at this level or only provide substrate-specific inferences retained as non-core.",
            "supported_by": support_lines(info, *core_support_keys(info)),
        },
    }


def add_missing_core_new_annotations(info: dict[str, object], annotations: list[dict[str, object]]) -> None:
    present = {ann["term"]["id"] for ann in annotations}
    replacements = replacement_ids(annotations)
    core = core_function(info, annotations)
    mf = core["molecular_function"]
    if mf["id"] not in present and mf["id"] not in replacements:
        annotations.append(new_annotation(info, mf, "enables"))
        present.add(mf["id"])
    for process in core.get("directly_involved_in", []):
        if process["id"] not in present and process["id"] not in replacements:
            annotations.append(new_annotation(info, process, "involved_in"))
            present.add(process["id"])


def is_generated_new_annotation(info: dict[str, object], annotation: dict[str, object]) -> bool:
    return (
        annotation.get("review", {}).get("action") == "NEW"
        and annotation.get("original_reference_id") == ref_file(info["gene"], "uniprot.txt")
        and annotation.get("term", {}).get("id") in TERMS
    )


def references_for(info: dict[str, object], annotations: list[dict[str, object]]) -> list[dict[str, object]]:
    refs: list[dict[str, object]] = []
    for ref_id in sorted({ann.get("original_reference_id") for ann in annotations if ann.get("original_reference_id")}):
        if ref_id.startswith("file:"):
            continue
        refs.append({"id": ref_id, "title": GO_REF_TITLES.get(ref_id, ref_id), "findings": []})

    lines = info["line_by_key"]
    uniprot_findings = [
        {"supporting_text": line}
        for line in dedupe(
            [
                lines["de"],
                lines.get("location"),
                lines.get("family"),
                lines.get("barrel_domain"),
                lines.get("receptor_like"),
                lines.get("siderophore_domain"),
                lines.get("feca_domain"),
                lines.get("heme_domain"),
                lines.get("copper_domain"),
                lines.get("cnto_function"),
                lines.get("cnto_metals"),
                lines.get("cobalamin_go"),
                lines.get("heme_mf_go"),
                lines.get("heme_bp_go"),
            ]
        )
    ]
    refs.append({"id": ref_file(info["gene"], "uniprot.txt"), "title": f"UniProtKB entry for {info['gene']}", "findings": uniprot_findings})
    refs.append(
        {
            "id": ref_file(info["gene"], "deep-research-asta.md"),
            "title": f"Asta retrieval report for {info['gene']} ({info['id']})",
            "findings": [{"supporting_text": lines["asta"]}],
        }
    )
    return refs


def suggested_questions(info: dict[str, object]) -> list[dict[str, str]]:
    category = info["category"]
    if category == "generic":
        question = "Which ligand or nutrient class is recognized by this TonB-dependent receptor in P. putida KT2440?"
    elif category == "cnto":
        question = "Which pseudopaline-metal complexes are imported by this CntO paralog under KT2440 growth conditions?"
    elif category == "copper":
        question = "What copper species or copper-containing ligand is recognized by OprC in KT2440?"
    else:
        question = "Which TonB/ExbB/ExbD energy-transduction paralog energizes this receptor under nutrient-limited conditions?"
    return [{"question": question}]


def write_gene(info: dict[str, object]) -> None:
    gene = info["gene"]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    annotations = [ann for ann in doc.get("existing_annotations", []) if not is_generated_new_annotation(info, ann)]
    for ann in annotations:
        ann["review"] = review_for_annotation(info, ann["term"]["id"], ann["term"]["label"])
    add_missing_core_new_annotations(info, annotations)

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
            "core_functions": [core_function(info, annotations)],
            "proposed_new_terms": [],
            "suggested_questions": suggested_questions(info),
            "suggested_experiments": [
                {
                    "description": "Compare wild type and receptor deletion strains for uptake or growth rescue under the relevant ligand limitation, with paired TonB-system mutants to test energy coupling.",
                    "experiment_type": "transport genetics",
                }
            ],
        }
    )
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def annoton(info: dict[str, object]) -> dict[str, object]:
    core = core_function(info, [])
    gene = info["gene"]
    entry: dict[str, object] = {
        "id": f"{gene}_tonb_receptor_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {info['product']}",
        "function": {"preferred_term": core["molecular_function"]["label"], "term": core["molecular_function"]},
        "processes": [{"preferred_term": p["label"], "term": p} for p in core.get("directly_involved_in", [])],
    }
    if "locations" in core:
        entry["locations"] = [{"preferred_term": loc["label"], "term": loc} for loc in core["locations"]]
    return entry


def add_concept(concepts: list[dict[str, object]], go_id: str, description_text: str) -> None:
    if any(c.get("term", {}).get("id") == go_id for c in concepts):
        return
    concepts.append({"preferred_term": TERMS[go_id], "term": term(go_id), "description": description_text})


def write_module(infos: list[dict[str, object]]) -> None:
    doc = yaml.safe_load(MODULE_PATH.read_text(encoding="utf-8"))
    doc["title"] = "TonB-dependent transport energy-transduction and receptor boundary"
    doc["description"] = (
        "Boundary module for PSEPK TonB-dependent transport. It covers TonB/ExbB/ExbD "
        "energy-transduction proteins plus the first-pass TonB-dependent outer-membrane "
        "receptor panel, with substrate specificity represented gene by gene."
    )
    evidence = doc.setdefault("evidence", [])
    if not any(e.get("source_id") == f"file:{BATCH_PATH.relative_to(ROOT)}" for e in evidence):
        evidence.append(
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK transport/membrane/efflux TonB-dependent receptor partition batch",
                "statement": "The receptor split covers 30 TonB-dependent outer-membrane receptor genes, including ferric siderophore, CntO, heme, B12-family, copper-receptor, and generic receptor candidates.",
            }
        )

    module = doc["module"]
    module["label"] = "TonB-dependent transport energy-transduction and receptor boundary"
    concepts = module.setdefault("concepts", [])
    add_concept(concepts, "GO:0022857", "Broad transmembrane transporter activity for TonB-dependent receptors with unresolved ligands.")
    add_concept(concepts, "GO:0015343", "Ferric-siderophore receptor activity for substrate-specific receptor genes.")
    add_concept(concepts, "GO:0015344", "Siderophore uptake transporter activity for ferric-siderophore receptor-family genes.")
    add_concept(concepts, "GO:0033214", "Ferric-siderophore import process for ferric-siderophore receptor genes.")
    add_concept(concepts, "GO:0044718", "Siderophore transmembrane transport process for generic receptor-family inferences.")
    add_concept(concepts, "GO:0015232", "Heme transporter activity for the heme receptor subfamily.")
    add_concept(concepts, "GO:0015886", "Heme transport process for heme receptor genes.")
    add_concept(concepts, "GO:0015889", "Cobalamin transport process for B12-family receptor genes.")
    add_concept(concepts, "GO:0015675", "Nickel transport process for CntO pseudopaline-metal receptor candidates.")
    add_concept(concepts, "GO:0006829", "Zinc transport process for CntO pseudopaline-metal receptor candidates.")
    add_concept(concepts, "GO:0055085", "Broad transport process for receptors with unresolved ligand specificity.")

    context = module.setdefault("context", {})
    components = context.setdefault("cellular_components", [])
    if not any(c.get("term", {}).get("id") == "GO:0009279" for c in components):
        components.append(
            {
                "preferred_term": "cell outer membrane",
                "term": term("GO:0009279"),
                "description": "TonB-dependent receptor beta-barrels reside in the Gram-negative outer membrane.",
            }
        )

    parts = module.setdefault("parts", [])
    parts[:] = [part for part in parts if part.get("node", {}).get("id") != "tonb_dependent_outer_membrane_receptor_panel"]
    parts.append(
        {
            "order": 4,
            "role": "TonB-dependent outer-membrane receptor panel",
            "node": {
                "id": "tonb_dependent_outer_membrane_receptor_panel",
                "label": "TonB-dependent outer-membrane receptor panel",
                "module_type": "TRANSPORT_STEP",
                "description": "Thirty TonB-dependent receptor genes from the transport/membrane/efflux partition; substrate specificity is retained at gene level where supported.",
                "annotons": [annoton(info) for info in infos],
            },
        }
    )
    doc["notes"] = (
        "This boundary now separates inner-membrane energy transduction from the TonB-dependent "
        "outer-membrane receptor panel. Orphan TonB paralog/receptor pairing and the ligand "
        "specificity of generic receptor candidates remain open."
    )
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    infos = [load_info(row) for row in load_rows()]
    for info in infos:
        if info["gene"] in PRESERVE_GENE_REVIEWS:
            continue
        write_gene(info)
    write_module(infos)
    print(f"Wrote {len(infos) - len(PRESERVE_GENE_REVIEWS)} receptor gene reviews and {MODULE_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
