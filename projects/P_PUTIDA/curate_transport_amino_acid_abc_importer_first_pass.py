#!/usr/bin/env python3
"""First-pass curation for amino-acid/peptide/polyamine ABC importer split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = ROOT / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_amino_acid_peptide_polyamine_abc_importers.tsv"
MODULE_PATH = ROOT / "modules/amino_acid_peptide_polyamine_abc_transport_boundary.yaml"

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
    "GO:0003333": "amino acid transmembrane transport",
    "GO:0005524": "ATP binding",
    "GO:0005886": "plasma membrane",
    "GO:0006865": "amino acid transport",
    "GO:0015276": "ligand-gated monoatomic ion channel activity",
    "GO:0015424": "ABC-type amino acid transporter activity",
    "GO:0016020": "membrane",
    "GO:0016887": "ATP hydrolysis activity",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0030313": "cell envelope",
    "GO:0033294": "ectoine binding",
    "GO:0034220": "monoatomic ion transmembrane transport",
    "GO:0043190": "ATP-binding cassette (ABC) transporter complex",
    "GO:0051470": "ectoine transmembrane transport",
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
    interpro = row["interpro_ids"]
    if gene == "PP_4751" or "atp-binding protein" in product:
        return "abc_atpase"
    if gene == "PP_4428" or "IPR014337" in interpro:
        return "ectoine_binding_protein"
    if "periplasmic" in product or "IPR001638" in interpro or "IPR018313" in interpro:
        return "periplasmic_binding_protein"
    if gene == "PP_2384" or "IPR008407" in interpro:
        return "azld_branched_chain_membrane"
    return "abc_permease"


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
        "location_inner": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell inner membrane", optional=True),
        "location_envelope": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell envelope", optional=True),
        "location_membrane": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Membrane", optional=True),
        "family": first_line(uniprot_lines, "CC   -!- SIMILARITY:", optional=True),
        "permease_domain": first_line(uniprot_lines, "DR   InterPro; IPR010065; AA_ABC_transptr_permease_3TM.", optional=True),
        "artm_gltk": first_line(uniprot_lines, "DR   InterPro; IPR043429; ArtM/GltK/GlnP/TcyL/YhdX-like.", optional=True),
        "his_mq": first_line(uniprot_lines, "DR   InterPro; IPR051613; ABC_transp_permease_HisMQ.", optional=True),
        "azld": first_line(uniprot_lines, "DR   InterPro; IPR008407; Brnchd-chn_aa_trnsp_AzlD.", optional=True),
        "binding_sbp3": first_line(uniprot_lines, "DR   InterPro; IPR001638; Solute-binding_3/MltF_N.", optional=True),
        "sbp3_cs": first_line(uniprot_lines, "DR   InterPro; IPR018313; SBP_3_CS.", optional=True),
        "ectoine_ehub": first_line(uniprot_lines, "DR   InterPro; IPR014337; Ectoine_EhuB.", optional=True),
        "ectoine_ehuc": first_line(uniprot_lines, "DR   InterPro; IPR014342; Ectoine_EhuC.", optional=True),
        "ectoine_ehud": first_line(uniprot_lines, "DR   InterPro; IPR014341; Ectoine_EhuD.", optional=True),
        "iontro": first_line(uniprot_lines, "DR   InterPro; IPR001320; Iontro_rcpt_C.", optional=True),
        "atpase": first_line(uniprot_lines, "DR   InterPro; IPR003593; AAA+_ATPase.", optional=True),
        "abc_atp": first_line(uniprot_lines, "DR   InterPro; IPR003439; ABC_transporter-like_ATP-bd.", optional=True),
        "metn": first_line(uniprot_lines, "DR   InterPro; IPR050086; MetN_ABC_transporter-like.", optional=True),
        "kw_amino": first_line(uniprot_lines, "KW   Amino-acid transport", optional=True),
        "kw_atp": first_line(uniprot_lines, "KW   ATP-binding", optional=True),
        "kw_signal": first_line(uniprot_lines, "KW   Signal", optional=True),
        "kw_membrane": first_line(uniprot_lines, "KW   Membrane", optional=True),
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
    if category == "abc_atpase":
        return ("de", "location_inner", "family", "atpase", "abc_atp", "metn", "kw_atp", "kw_amino")
    if category == "ectoine_binding_protein":
        return ("de", "family", "binding_sbp3", "ectoine_ehub", "kw_signal")
    if category == "periplasmic_binding_protein":
        return ("de", "location_envelope", "family", "binding_sbp3", "sbp3_cs", "iontro", "kw_signal")
    if category == "azld_branched_chain_membrane":
        return ("de", "azld", "kw_membrane")
    return ("de", "function", "location_inner", "family", "permease_domain", "artm_gltk", "his_mq", "ectoine_ehuc", "ectoine_ehud", "kw_amino")


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
        return f"{gene} encodes {product}, the ATP-binding energy-coupling component of a predicted amino-acid ABC importer."
    if category == "ectoine_binding_protein":
        return f"{gene} encodes {product}, an EhuB-like periplasmic ectoine/osmoprotectant-binding component of a predicted ABC importer."
    if category == "periplasmic_binding_protein":
        return f"{gene} encodes {product}, a periplasmic/cell-envelope substrate-binding component of a predicted amino-acid ABC importer."
    if category == "azld_branched_chain_membrane":
        return f"{gene} encodes {product}, a predicted branched-chain amino-acid ABC transporter membrane component."
    return f"{gene} encodes {product}, an inner-membrane permease component of a predicted amino-acid ABC importer."


def replacement(go_id: str) -> list[dict[str, str]]:
    return [term(go_id)]


def review_for_annotation(info: dict[str, object], ann: dict[str, object]) -> dict[str, object]:
    go_id = ann["term"]["id"]
    category = info["category"]
    if go_id in {"GO:0005886", "GO:0016020", "GO:0030313"}:
        action = "ACCEPT"
        if go_id == "GO:0016020" and "GO:0005886" in info["go_ids"]:
            action = "KEEP_AS_NON_CORE"
        return {
            "summary": "The membrane, plasma-membrane, or cell-envelope localization matches the ABC importer subunit context.",
            "action": action,
            "reason": "The UniProt product, subcellular-location or signal/membrane evidence, and ABC permease or substrate-binding domain context support this localization.",
            "supported_by": support_lines(info, "de", "location_inner", "location_envelope", "location_membrane", "kw_signal", "kw_membrane", *core_keys(info)),
        }
    if go_id in {"GO:0022857", "GO:0055085", "GO:0006865"}:
        return {
            "summary": "Transporter activity or amino-acid transport process context is appropriate for this ABC importer component.",
            "action": "ACCEPT",
            "reason": "The protein is an ABC importer permease or associated transporter component; exact substrate remains at amino-acid or family-level resolution unless the product/family evidence is more specific.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0043190":
        return {
            "summary": "ABC transporter complex membership is appropriate for this importer component.",
            "action": "ACCEPT",
            "reason": "The product and ABC permease family evidence support component membership in an ABC importer complex.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0000166", "GO:0005524"}:
        return {
            "summary": "Nucleotide/ATP binding is supported for the ABC ATPase but is less informative than ATP hydrolysis.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The ATPase component has ABC transporter ATP-binding domains; ATP hydrolysis better captures the active energy-coupling function.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0016887", "GO:0015424", "GO:0003333"}:
        return {
            "summary": "ATP hydrolysis and ABC-type amino-acid transporter context are appropriate for the ATP-binding subunit.",
            "action": "ACCEPT",
            "reason": "The ABC ATPase domains and amino-acid-transporter product evidence support ATP hydrolysis and component-level ABC-type amino-acid transport.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0033294", "GO:0051470"}:
        return {
            "summary": "Ectoine binding/transport context is appropriate for the EhuB-family periplasmic binding protein.",
            "action": "ACCEPT",
            "reason": "The EhuB family evidence supports ectoine/osmoprotectant-binding component context for this substrate-binding protein.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0015276":
        return {
            "summary": "Ligand-gated ion channel activity is over-specific and mechanistically wrong for this periplasmic ABC substrate-binding protein.",
            "action": "MODIFY",
            "reason": "The protein carries bacterial solute-binding protein evidence and is annotated as an amino-acid ABC transporter binding protein, not an ion-channel pore.",
            "proposed_replacement_terms": replacement("GO:0015424"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0034220":
        return {
            "summary": "Monoatomic ion transmembrane transport is over-specific for this periplasmic ABC substrate-binding protein.",
            "action": "MODIFY",
            "reason": "The product and domain evidence support ABC amino-acid/importer substrate-binding context, not ion-channel-mediated ion transport.",
            "proposed_replacement_terms": replacement("GO:0006865"),
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


def location_id(info: dict[str, object]) -> str:
    category = info["category"]
    if category in {"periplasmic_binding_protein", "ectoine_binding_protein"}:
        return "GO:0030313"
    if category in {"abc_permease", "abc_atpase"}:
        return "GO:0005886"
    return "GO:0016020"


def add_missing_new_annotations(info: dict[str, object], annotations: list[dict[str, object]]) -> None:
    present = {ann["term"]["id"] for ann in annotations}

    def add(go_id: str, qualifier: str, summary: str | None = None) -> None:
        if go_id not in present:
            annotations.append(new_annotation(info, go_id, qualifier, summary))
            present.add(go_id)

    if not (present & {"GO:0005886", "GO:0016020", "GO:0030313"}):
        add(location_id(info), "located_in")
    category = info["category"]
    if category == "abc_atpase":
        add("GO:0016887", "enables")
        add("GO:0003333", "involved_in")
    elif category == "ectoine_binding_protein":
        add("GO:0033294", "enables")
        add("GO:0051470", "involved_in")
    elif category == "periplasmic_binding_protein":
        add("GO:0006865", "involved_in")
    elif category in {"abc_permease", "azld_branched_chain_membrane"}:
        add("GO:0022857", "enables")
        add("GO:0006865", "involved_in")


def core_function_terms(info: dict[str, object]) -> tuple[str | None, str | None, list[str], str | None, str]:
    category = info["category"]
    if category == "abc_atpase":
        return "GO:0016887", "GO:0015424", ["GO:0003333"], "GO:0043190", "ATP-hydrolyzing ABC ATPase component of an amino-acid importer."
    if category == "ectoine_binding_protein":
        return "GO:0033294", None, ["GO:0051470"], None, "EhuB-family ectoine/osmoprotectant-binding component of an ABC importer."
    if category == "periplasmic_binding_protein":
        return None, "GO:0015424", ["GO:0006865"], None, "Periplasmic substrate-binding contributor to amino-acid ABC import."
    if category == "azld_branched_chain_membrane":
        return "GO:0022857", "GO:0015424", ["GO:0006865"], None, "Branched-chain amino-acid ABC transporter membrane component candidate."
    return "GO:0022857", "GO:0015424", ["GO:0006865"], "GO:0043190", "Inner-membrane permease component of an amino-acid ABC importer."


def core_functions(info: dict[str, object]) -> list[dict[str, object]]:
    mf, contributes_to, processes, complex_id, desc = core_function_terms(info)
    core: dict[str, object] = {
        "description": desc,
        "locations": [term(location_id(info))],
        "supported_by": support_lines(info, *core_keys(info)),
    }
    if mf:
        core["molecular_function"] = term(mf)
    if contributes_to:
        core["contributes_to_molecular_function"] = term(contributes_to)
    if processes:
        core["directly_involved_in"] = [term(go_id) for go_id in processes]
    if complex_id:
        core["in_complex"] = term(complex_id)
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
        lines.get("location_inner"),
        lines.get("location_envelope"),
        lines.get("location_membrane"),
        lines.get("family"),
        lines.get("permease_domain"),
        lines.get("artm_gltk"),
        lines.get("his_mq"),
        lines.get("azld"),
        lines.get("binding_sbp3"),
        lines.get("sbp3_cs"),
        lines.get("ectoine_ehub"),
        lines.get("ectoine_ehuc"),
        lines.get("ectoine_ehud"),
        lines.get("iontro"),
        lines.get("atpase"),
        lines.get("abc_atp"),
        lines.get("metn"),
        lines.get("kw_amino"),
        lines.get("kw_atp"),
        lines.get("kw_signal"),
        lines.get("kw_membrane"),
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
                    "question": "Which substrate and partner ATPase/permease/binding-protein components define this ABC importer system in KT2440?"
                }
            ],
            "suggested_experiments": [
                {
                    "description": "Test uptake of candidate amino acids or osmoprotectants in wild-type, deletion, and complemented strains, ideally with operon-level mutants that separate binding-protein, permease, and ATPase contributions.",
                    "experiment_type": "ABC importer genetics and uptake assay",
                }
            ],
        }
    )
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def annoton(info: dict[str, object]) -> dict[str, object]:
    gene = info["gene"]
    core = core_functions(info)[0]
    entry: dict[str, object] = {
        "id": f"{gene}_amino_acid_abc_importer_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {info['product']}",
        "locations": [{"preferred_term": loc["label"], "term": loc} for loc in core.get("locations", [])],
    }
    if core.get("molecular_function"):
        entry["function"] = {"preferred_term": core["molecular_function"]["label"], "term": core["molecular_function"]}
    elif core.get("contributes_to_molecular_function"):
        entry["function"] = {
            "preferred_term": core["contributes_to_molecular_function"]["label"],
            "term": core["contributes_to_molecular_function"],
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
    by_category: dict[str, list[dict[str, object]]] = {}
    for info in infos:
        by_category.setdefault(info["category"], []).append(info)
    doc = {
        "id": "MODULE:amino_acid_peptide_polyamine_abc_transport_boundary",
        "title": "Amino-acid, peptide, and polyamine ABC importer boundary",
        "description": (
            "Boundary module for the PSEPK transport/membrane/efflux split containing amino-acid, ectoine/osmoprotectant, "
            "and related ABC importer binding proteins, permeases, and ATPase components. Component-level roles are kept "
            "separate unless substrate and partner evidence support a complete importer assignment."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK transport/membrane/efflux amino-acid/peptide/polyamine ABC importer batch",
                "statement": "The partition groups 15 amino-acid, ectoine/osmoprotectant, or related ABC importer components for first-pass curation.",
            }
        ],
        "notes": (
            "First-pass interpretation: membrane permeases, periplasmic binding proteins, and ATP-binding proteins are modeled as "
            "ABC importer components. The split avoids asserting exact substrates except where product/family evidence supports "
            "glutamate/aspartate, arginine/amino-acid, ectoine/Ehu, branched-chain amino-acid, or glutamine-like context."
        ),
        "module": {
            "id": "amino_acid_peptide_polyamine_abc_transport_boundary",
            "label": "Amino-acid, peptide, and polyamine ABC importer boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                concept("GO:0015424", "ABC-type amino-acid transporter activity for importer complexes and ATPase/permease contributors."),
                concept("GO:0006865", "Amino-acid transport process context for predicted amino-acid ABC importers."),
                concept("GO:0003333", "Amino-acid transmembrane transport process context for the ATPase-supported importer."),
                concept("GO:0022857", "Broad transporter activity for ABC permease components."),
                concept("GO:0016887", "ATP hydrolysis activity for ABC ATP-binding components."),
                concept("GO:0033294", "Ectoine binding for the EhuB-family periplasmic substrate-binding component."),
                concept("GO:0051470", "Ectoine transport process context for the Ehu-family importer candidate."),
            ],
            "context": {
                "cellular_components": [
                    concept("GO:0005886", "Inner/cytoplasmic membrane location for ABC permease and ATPase-associated importer components."),
                    concept("GO:0016020", "Broad membrane location for low-resolution membrane components."),
                    concept("GO:0030313", "Cell-envelope/periplasmic context for substrate-binding proteins."),
                    concept("GO:0043190", "ABC transporter complex context for membrane and ATPase components."),
                ]
            },
            "parts": [
                part(1, "Glt/Gln amino-acid importer candidates", "glt_gln_amino_acid_abc_importer_candidates", "Glt/Gln amino-acid importer candidates", "Glutamate/aspartate and glutamine-like ABC importer component candidates.", [by_gene[g] for g in ["PP_0656", "PP_0657", "PP_5023", "PP_5024"]]),
                part(2, "Arginine/amino-acid ABC importer candidates", "arginine_amino_acid_abc_importer_candidates", "Arginine/amino-acid ABC importer candidates", "PP_3593-PP_3595 substrate-binding and permease components with ArtM/GltK-like amino-acid importer evidence.", [by_gene[g] for g in ["PP_3593", "PP_3594", "PP_3595"]]),
                part(3, "Ectoine/osmoprotectant ABC importer candidates", "ectoine_osmoprotectant_abc_importer_candidates", "Ectoine/osmoprotectant ABC importer candidates", "PP_4426-PP_4428 EhuD/EhuC/EhuB-like components, with ectoine binding retained for PP_4428.", [by_gene[g] for g in ["PP_4426", "PP_4427", "PP_4428"]]),
                part(4, "Branched-chain and generic amino-acid ABC importer candidates", "branched_chain_generic_amino_acid_abc_importer_candidates", "Branched-chain and generic amino-acid ABC importer candidates", "PP_2384 plus the PP_4748-PP_4751 substrate-binding, permease, and ATPase components of a predicted amino-acid ABC importer.", [by_gene[g] for g in ["PP_2384", "PP_4748", "PP_4749", "PP_4750", "PP_4751"]]),
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
