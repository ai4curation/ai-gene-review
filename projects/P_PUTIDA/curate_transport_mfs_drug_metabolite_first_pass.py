#!/usr/bin/env python3
"""First-pass curation for MFS drug/metabolite transporter split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = ROOT / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_mfs_drug_metabolite_transporters.tsv"
MODULE_PATH = ROOT / "modules/mfs_drug_metabolite_transport_boundary.yaml"
PRESERVE_GENE_REVIEWS = {"pcaK", "nicT"}

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
    "GO:0005886": "plasma membrane",
    "GO:0005975": "carbohydrate metabolic process",
    "GO:0008643": "carbohydrate transport",
    "GO:0008028": "monocarboxylic acid transmembrane transporter activity",
    "GO:0015134": "hexuronate transmembrane transporter activity",
    "GO:0015144": "carbohydrate transmembrane transporter activity",
    "GO:0015293": "symporter activity",
    "GO:0015385": "sodium:proton antiporter activity",
    "GO:0015528": "lactose:proton symporter activity",
    "GO:0015718": "monocarboxylic acid transport",
    "GO:0015736": "hexuronate transmembrane transport",
    "GO:0015767": "lactose transport",
    "GO:0015778": "hexuronide transmembrane transport",
    "GO:0016020": "membrane",
    "GO:0016746": "acyltransferase activity",
    "GO:0019752": "carboxylic acid metabolic process",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0030395": "lactose binding",
    "GO:0034219": "carbohydrate transmembrane transport",
    "GO:0035725": "sodium ion transmembrane transport",
    "GO:0042910": "xenobiotic transmembrane transporter activity",
    "GO:0046942": "carboxylic acid transport",
    "GO:0046943": "carboxylic acid transmembrane transporter activity",
    "GO:0055085": "transmembrane transport",
    "GO:1905039": "carboxylic acid transmembrane transport",
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


def classify(row: dict[str, str], uniprot_text: str) -> str:
    gene = row["gene"]
    product = row["protein_name"].lower()
    interpro = row["interpro_ids"]
    go_ids = set(row["go_ids"].split("; ")) if row["go_ids"] else set()
    if gene == "pcaK":
        return "pcaK_anchor"
    if gene == "nicT":
        return "nicotinate_context"
    if gene == "PP_1700":
        return "membrane_acyltransferase"
    if gene in {"pcaT", "kgtP"}:
        return "alpha_ketoglutarate_symporter"
    if gene == "proP":
        return "compatible_solute_symporter"
    if "cyanate" in product or "IPR052524" in interpro:
        return "cyanate_transporter"
    if gene in {"ydgK", "PP_3304", "PP_3588"}:
        return "bcr_cmla_efflux"
    if "emrb/qaca" in product or "drug resistance transporter" in product:
        return "emrb_qaca_efflux"
    if gene in {"fsr-I", "fsr-II"} or "fosmidomycin" in product:
        return "fosmidomycin_efflux"
    if gene == "sotB" or "sugar efflux" in product:
        return "sugar_efflux"
    if any(token in product for token in ("benzoate", "hydroxyphenylpropionate", "hydroxycinnamate", "aromatic compound")):
        return "aromatic_carboxylate_transporter"
    if any(token in product for token in ("oxalate", "formate", "phthalate", "uronate", "glucarate", "ketogluconate", "tartrate")):
        return "carboxylate_transporter"
    if "GO:0015293" in go_ids or "IPR051084" in interpro:
        return "mfs_symporter_candidate"
    if "amino acid" in product:
        return "amino_acid_mfs"
    if "efflux" in product:
        return "mfs_efflux_candidate"
    return "generic_mfs"


def load_info(row: dict[str, str]) -> dict[str, object]:
    gene = row["gene"]
    uniprot_path = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta_path = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    review_path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    uniprot_lines = uniprot_path.read_text(encoding="utf-8").splitlines()
    asta_lines = asta_path.read_text(encoding="utf-8").splitlines()
    review_doc = yaml.safe_load(review_path.read_text(encoding="utf-8"))
    uniprot_text = "\n".join(uniprot_lines)
    category = classify(row, uniprot_text)

    line_by_key = {
        "de": first_line(uniprot_lines, "DE   "),
        "function": first_line(uniprot_lines, "CC   -!- FUNCTION:", optional=True),
        "location_inner": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell inner membrane", optional=True),
        "location_cell": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell membrane", optional=True),
        "location_membrane": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Membrane", optional=True),
        "family": first_line(uniprot_lines, "CC   -!- SIMILARITY:", optional=True),
        "mfs": first_line(uniprot_lines, "DR   InterPro; IPR011701; MFS.", optional=True),
        "mfs_dom": first_line(uniprot_lines, "DR   InterPro; IPR020846; MFS_dom.", optional=True),
        "mfs_superfamily": first_line(uniprot_lines, "DR   InterPro; IPR036259; MFS_trans_sf.", optional=True),
        "h_symporter": first_line(uniprot_lines, "DR   InterPro; IPR051084; H+-coupled_symporters.", optional=True),
        "mhs": first_line(uniprot_lines, "DR   InterPro; IPR004736; MHS_symport.", optional=True),
        "bcr": first_line(uniprot_lines, "DR   InterPro; IPR004812; Efflux_drug-R_Bcr/CmlA.", optional=True),
        "emrb": first_line(uniprot_lines, "DR   InterPro; IPR004638; EmrB-like.", optional=True),
        "cynx": first_line(uniprot_lines, "DR   InterPro; IPR052524; MFS_Cyanate_Porter.", optional=True),
        "sugar_p": first_line(uniprot_lines, "DR   InterPro; IPR000849; Sugar_P_transporter.", optional=True),
        "sugar_cs": first_line(uniprot_lines, "DR   InterPro; IPR005829; Sugar_transporter_CS.", optional=True),
        "sotb": first_line(uniprot_lines, "DR   InterPro; IPR023495; Sugar_effux_transptr_put.", optional=True),
        "phthalate": first_line(uniprot_lines, "DR   InterPro; IPR050382; MFS_Na/Anion_cotransporter.", optional=True),
        "acyltransferase": first_line(uniprot_lines, "DR   InterPro; IPR002123; Plipid/glycerol_acylTrfase.", optional=True),
        "mfs4": first_line(uniprot_lines, "DR   InterPro; IPR010645; MFS_4.", optional=True),
        "tm_effector": first_line(uniprot_lines, "DR   InterPro; IPR010290; TM_effector.", optional=True),
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
    if category in {"bcr_cmla_efflux", "emrb_qaca_efflux", "fosmidomycin_efflux", "mfs_efflux_candidate"}:
        return ("de", "family", "bcr", "emrb", "mfs", "mfs_dom", "mfs_superfamily")
    if category in {"pcaK_anchor", "aromatic_carboxylate_transporter"}:
        return ("de", "family", "mfs", "mfs_dom", "mfs_superfamily", "sugar_cs")
    if category in {"carboxylate_transporter", "carboxylate_candidate"}:
        return ("de", "family", "phthalate", "sugar_p", "mfs", "mfs_dom", "mfs_superfamily")
    if category in {"alpha_ketoglutarate_symporter", "compatible_solute_symporter", "mfs_symporter_candidate", "amino_acid_mfs"}:
        return ("de", "function", "family", "h_symporter", "mhs", "mfs", "mfs_dom", "mfs_superfamily", "sugar_cs")
    if category in {"cyanate_transporter"}:
        return ("de", "cynx", "mfs", "mfs_superfamily")
    if category in {"sugar_efflux"}:
        return ("de", "family", "sotb", "mfs", "mfs_dom", "mfs_superfamily")
    if category == "membrane_acyltransferase":
        return ("de", "acyltransferase", "mfs", "mfs_superfamily")
    if category == "nicotinate_context":
        return ("de", "function", "family", "mfs", "mfs_dom", "mfs_superfamily")
    return ("de", "family", "mfs", "mfs_dom", "mfs_superfamily", "mfs4", "tm_effector")


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
    if category == "membrane_acyltransferase":
        return f"{gene} encodes a predicted membrane acyltransferase with MFS-fold/transmembrane context in Pseudomonas putida KT2440."
    if category in {"bcr_cmla_efflux", "emrb_qaca_efflux", "fosmidomycin_efflux"}:
        return f"{gene} encodes {product}, an inner-membrane MFS-family efflux transporter candidate."
    if category in {"pcaK_anchor", "aromatic_carboxylate_transporter"}:
        return f"{gene} encodes {product}, an MFS-family transporter associated with aromatic carboxylate uptake or efflux context."
    if category == "nicotinate_context":
        return f"{gene} encodes {product}, an MFS-family transporter candidate associated with the aerobic nicotinate degradation gene cluster."
    if category in {"alpha_ketoglutarate_symporter", "compatible_solute_symporter", "mfs_symporter_candidate", "amino_acid_mfs"}:
        return f"{gene} encodes {product}, a predicted MFS-family secondary transporter or symporter."
    if category in {"carboxylate_transporter", "carboxylate_candidate"}:
        return f"{gene} encodes {product}, a predicted MFS-family organic-acid or carboxylate transporter candidate."
    if category == "cyanate_transporter":
        return f"{gene} encodes {product}, a CynX-like MFS cyanate transporter candidate."
    if category == "sugar_efflux":
        return f"{gene} encodes {product}, a probable MFS sugar/carbohydrate efflux transporter."
    return f"{gene} encodes {product}, a predicted MFS-family transmembrane transporter with unresolved substrate specificity."


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
            "summary": "The membrane localization matches the predicted multi-pass inner-membrane transporter context.",
            "action": action,
            "reason": "The UniProt product, subcellular-location, keyword, and MFS/transmembrane domain evidence support membrane localization; plasma membrane is the more informative bacterial inner-membrane term when present.",
            "supported_by": support_lines(info, "de", "location_inner", "location_cell", "location_membrane", *core_keys(info)),
        }
    if go_id == "GO:0022857":
        action = "ACCEPT"
        if category in {"pcaK_anchor", "aromatic_carboxylate_transporter", "carboxylate_transporter", "sugar_efflux", "bcr_cmla_efflux", "emrb_qaca_efflux", "fosmidomycin_efflux", "membrane_acyltransferase"}:
            action = "KEEP_AS_NON_CORE" if category != "membrane_acyltransferase" else "MARK_AS_OVER_ANNOTATED"
        return {
            "summary": "Broad transporter activity is supported, but more specific substrate or enzyme context may be more informative.",
            "action": action,
            "reason": "The protein carries MFS/transmembrane transporter evidence. For named or family-resolved carriers this broad term is retained as non-core; for the membrane acyltransferase side node, transporter activity is treated as an automated family over-annotation.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0055085":
        return {
            "summary": "Broad transmembrane transport is appropriate process context for this MFS transporter candidate.",
            "action": "ACCEPT",
            "reason": "The product and MFS/transmembrane domain evidence support a membrane-transport process while substrate specificity remains partly unresolved for most paralogs.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0015293":
        return {
            "summary": "Symporter activity is appropriate for the H+-coupled/MHS-like MFS transporter context.",
            "action": "ACCEPT",
            "reason": "The protein has H+-coupled symporter, MHS, or product-name support for secondary symport, but exact substrate is kept conservative unless directly named.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0046943", "GO:0008028"}:
        return {
            "summary": "Carboxylic-acid transporter activity is appropriate substrate-class context for this named or family-supported MFS transporter.",
            "action": "ACCEPT" if category in {"pcaK_anchor", "aromatic_carboxylate_transporter", "carboxylate_transporter"} else "KEEP_AS_NON_CORE",
            "reason": "The product, family, or TreeGrafter context supports carboxylate/organic-acid transport, but substrate-specific claims beyond the product name remain unresolved.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0046942", "GO:1905039", "GO:0015718"}:
        return {
            "summary": "Carboxylic-acid transport process context is consistent with the substrate-class evidence.",
            "action": "ACCEPT",
            "reason": "The product/family context supports carboxylate or monocarboxylate transmembrane transport for this named MFS carrier.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0042910", "GO:1990961"}:
        return {
            "summary": "Xenobiotic or drug-efflux context is appropriate for this Bcr/CmlA, EmrB/QacA, fosmidomycin, or efflux-labeled MFS transporter.",
            "action": "ACCEPT" if category in {"bcr_cmla_efflux", "emrb_qaca_efflux", "fosmidomycin_efflux", "mfs_efflux_candidate"} else "KEEP_AS_NON_CORE",
            "reason": "The product or efflux-family domain evidence supports a multidrug/xenobiotic export role at first-pass resolution; exact substrates and regulation remain unresolved.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0015385":
        return {
            "summary": "Sodium:proton antiporter activity is over-specific for this Bcr/CmlA-family drug-efflux transporter.",
            "action": "MODIFY",
            "reason": "The local product/domain evidence supports MFS drug/xenobiotic efflux, but not sodium:proton antiport as the specific molecular activity.",
            "proposed_replacement_terms": replacement("GO:0042910"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0035725":
        return {
            "summary": "Sodium transmembrane transport is over-specific for this Bcr/CmlA-family drug-efflux transporter.",
            "action": "MODIFY",
            "reason": "The local product/domain evidence supports MFS drug/xenobiotic efflux, but not sodium as the transported substrate.",
            "proposed_replacement_terms": replacement("GO:1990961"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0015528":
        return {
            "summary": "Lactose:proton symporter activity is not supported by the lightweight evidence for this HcaT-like MFS protein.",
            "action": "MODIFY",
            "reason": "The protein is an HcaT/MFS-domain membrane protein, but product and domain context do not establish lactose as the substrate.",
            "proposed_replacement_terms": replacement("GO:0022857"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0030395":
        return {
            "summary": "Lactose binding is not supported for this HcaT-like MFS protein.",
            "action": "REMOVE",
            "reason": "The annotation appears to be an over-propagated substrate-specific TreeGrafter inference; no local product or domain evidence supports lactose binding.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0015767":
        return {
            "summary": "Lactose transport is not supported by the lightweight evidence for this HcaT-like MFS protein.",
            "action": "MODIFY",
            "reason": "The protein is an HcaT/MFS-domain membrane protein, but product and domain context do not establish lactose as the transported substrate.",
            "proposed_replacement_terms": replacement("GO:0055085"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0015144":
        return {
            "summary": "Carbohydrate transporter activity is appropriate for the SotB-like sugar-efflux transporter.",
            "action": "ACCEPT",
            "reason": "The product and SotB/sugar-efflux family evidence support carbohydrate transmembrane transporter activity.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0008643", "GO:0034219"}:
        return {
            "summary": "Carbohydrate transport is appropriate process context for the SotB-like sugar-efflux transporter.",
            "action": "ACCEPT",
            "reason": "The product and SotB/sugar-efflux family evidence support carbohydrate/sugar transport process context.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0015134":
        return {
            "summary": "Hexuronate transporter activity is probably too specific for this generic phthalate-family MFS transporter.",
            "action": "MODIFY",
            "reason": "The family context supports organic-acid/carboxylate transport, but the local product does not establish hexuronate as the substrate.",
            "proposed_replacement_terms": replacement("GO:0046943"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0015736", "GO:0015778"}:
        return {
            "summary": "Hexuronate/hexuronide transmembrane transport is probably too specific for this generic phthalate-family MFS transporter.",
            "action": "MODIFY",
            "reason": "The family context supports organic-acid/carboxylate transport, but the local product does not establish hexuronate as the substrate.",
            "proposed_replacement_terms": replacement("GO:1905039"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0016746":
        return {
            "summary": "Acyltransferase activity is supported for this membrane acyltransferase side node.",
            "action": "ACCEPT",
            "reason": "The product name and phospholipid/glycerol acyltransferase domain support acyltransferase activity more directly than a transporter role.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0005975", "GO:0019752"}:
        return {
            "summary": "The metabolic-process annotation is pathway context rather than the core function of this transporter.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": "The gene product is a membrane transporter candidate; carbohydrate or carboxylic-acid metabolism is indirect pathway context unless transporter genetics establish a pathway-specific role.",
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


def add_missing_new_annotations(info: dict[str, object], annotations: list[dict[str, object]]) -> None:
    present = {ann["term"]["id"] for ann in annotations}
    category = info["category"]

    def add(go_id: str, qualifier: str, summary: str | None = None) -> None:
        if go_id not in present:
            annotations.append(new_annotation(info, go_id, qualifier, summary))
            present.add(go_id)

    if not (present & {"GO:0005886", "GO:0016020"}):
        add("GO:0005886" if category != "generic_mfs" else "GO:0016020", "located_in")
    if category == "membrane_acyltransferase":
        add("GO:0016746", "enables", "Adds acyltransferase activity as the best-supported function for the membrane acyltransferase side node.")
        return
    if category in {"bcr_cmla_efflux", "emrb_qaca_efflux", "fosmidomycin_efflux", "mfs_efflux_candidate"}:
        add("GO:0042910", "enables", "Adds xenobiotic/drug-efflux transporter activity for the efflux-family MFS carrier.")
        add("GO:1990961", "involved_in")
        return
    if category in {"pcaK_anchor", "aromatic_carboxylate_transporter", "carboxylate_transporter"}:
        add("GO:0046943", "enables", "Adds carboxylic-acid transporter activity for a named organic-acid/aromatic-acid MFS carrier.")
        add("GO:1905039", "involved_in")
        return
    if category == "sugar_efflux":
        add("GO:0015144", "enables", "Adds carbohydrate transporter activity for the SotB-like sugar-efflux carrier.")
        add("GO:0055085", "involved_in")
        return
    if category in {"alpha_ketoglutarate_symporter", "compatible_solute_symporter", "mfs_symporter_candidate", "amino_acid_mfs"}:
        add("GO:0015293", "enables")
        add("GO:0055085", "involved_in")
        return
    add("GO:0022857", "enables")
    add("GO:0055085", "involved_in")


def best_location(info: dict[str, object]) -> dict[str, str]:
    present = set(info["go_ids"])
    if "GO:0005886" in present:
        return term("GO:0005886")
    if "GO:0016020" in present:
        return term("GO:0016020")
    if info["category"] == "generic_mfs":
        return term("GO:0016020")
    return term("GO:0005886")


def core_function_terms(info: dict[str, object]) -> tuple[str, list[str], str]:
    category = info["category"]
    if category == "pcaK_anchor":
        return "GO:0008028", ["GO:0015718"], "4-hydroxybenzoate/aromatic monocarboxylate transporter context."
    if category in {"aromatic_carboxylate_transporter", "carboxylate_transporter", "carboxylate_candidate"}:
        return "GO:0046943", ["GO:1905039"], "Organic-acid or aromatic-carboxylate MFS transporter candidate."
    if category in {"bcr_cmla_efflux", "emrb_qaca_efflux", "fosmidomycin_efflux", "mfs_efflux_candidate"}:
        return "GO:0042910", ["GO:1990961"], "MFS-family xenobiotic/drug-efflux transporter candidate."
    if category == "sugar_efflux":
        return "GO:0015144", ["GO:0055085"], "SotB-like sugar/carbohydrate efflux transporter candidate."
    if category in {"alpha_ketoglutarate_symporter", "compatible_solute_symporter", "mfs_symporter_candidate", "amino_acid_mfs"}:
        return "GO:0015293", ["GO:0055085"], "MFS-family secondary transporter or symporter candidate."
    if category == "membrane_acyltransferase":
        return "GO:0016746", [], "Membrane acyltransferase side node with MFS/transmembrane context."
    return "GO:0022857", ["GO:0055085"], "MFS-family transmembrane transporter candidate with unresolved substrate specificity."


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
        lines.get("location_inner"),
        lines.get("location_cell"),
        lines.get("location_membrane"),
        lines.get("family"),
        lines.get("mfs"),
        lines.get("mfs_dom"),
        lines.get("mfs_superfamily"),
        lines.get("h_symporter"),
        lines.get("mhs"),
        lines.get("bcr"),
        lines.get("emrb"),
        lines.get("cynx"),
        lines.get("sugar_p"),
        lines.get("sugar_cs"),
        lines.get("sotb"),
        lines.get("phthalate"),
        lines.get("acyltransferase"),
        lines.get("mfs4"),
        lines.get("tm_effector"),
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
    if gene in PRESERVE_GENE_REVIEWS:
        patch_preserved_reference(info)
        return
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
                {"question": "What substrate, transport direction, coupling ion, and physiological induction condition apply to this MFS transporter in KT2440?"}
            ],
            "suggested_experiments": [
                {
                    "description": "Measure uptake or efflux of candidate substrates in wild-type, deletion, and complemented strains, prioritizing substrates suggested by product name, operon context, and transporter-family assignment.",
                    "experiment_type": "targeted transporter genetics and uptake/efflux assay",
                }
            ],
        }
    )
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def patch_preserved_reference(info: dict[str, object]) -> None:
    gene = info["gene"]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    refs = doc.setdefault("references", [])
    ref_id = ref_file(gene, "deep-research-asta.md")
    if not any(ref.get("id") == ref_id for ref in refs):
        refs.append(
            {
                "id": ref_id,
                "title": f"Asta retrieval report for {gene} ({info['id']})",
                "findings": [{"supporting_text": info["line_by_key"]["asta"]}],
            }
        )
        path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def annoton(info: dict[str, object]) -> dict[str, object]:
    gene = info["gene"]
    core = core_functions(info)[0]
    entry: dict[str, object] = {
        "id": f"{gene}_mfs_context",
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
        "id": "MODULE:mfs_drug_metabolite_transport_boundary",
        "title": "MFS drug and metabolite transport boundary",
        "description": (
            "Boundary module for the PSEPK transport/membrane/efflux split containing MFS drug, aromatic-acid, "
            "organic-acid, sugar, cyanate, compatible-solute, and low-resolution metabolite transporter candidates. "
            "The module keeps substrate claims conservative unless product, family, or prior curated evidence is specific."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK transport/membrane/efflux MFS drug/metabolite transporter batch",
                "statement": "The partition groups 80 MFS-family drug, metabolite, aromatic-acid, sugar, cyanate, compatible-solute, and generic transporter candidates for first-pass curation.",
            }
        ],
        "notes": (
            "First-pass interpretation: named substrate labels are retained at substrate-class level where supported. "
            "Generic MFS paralogs are not assigned a specific substrate, direction, or coupling ion without product/family support."
        ),
        "module": {
            "id": "mfs_drug_metabolite_transport_boundary",
            "label": "MFS drug and metabolite transport boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                concept("GO:0022857", "Broad transporter activity for generic MFS paralogs."),
                concept("GO:0055085", "Broad transport process for unresolved MFS carriers."),
                concept("GO:0042910", "Xenobiotic/drug transporter activity for Bcr/CmlA, EmrB/QacA, fosmidomycin, and efflux-labeled MFS carriers."),
                concept("GO:1990961", "Xenobiotic detoxification/export process context for multidrug efflux carriers."),
                concept("GO:0046943", "Carboxylic-acid transporter activity for named organic-acid and aromatic-acid carriers."),
                concept("GO:1905039", "Carboxylic-acid transmembrane transport process context."),
                concept("GO:0015293", "Symporter activity for H+-coupled/MHS-like MFS candidates."),
                concept("GO:0015144", "Carbohydrate transporter activity for SotB/sugar-efflux context."),
                concept("GO:0016746", "Acyltransferase activity for the PP_1700 membrane acyltransferase side node."),
            ],
            "context": {
                "cellular_components": [
                    concept("GO:0005886", "Bacterial plasma/inner membrane location for resolved inner-membrane MFS transporters."),
                    concept("GO:0016020", "Broad membrane context for low-resolution membrane transporter candidates."),
                ]
            },
            "parts": [
                part(1, "Aromatic and carboxylate MFS transporters", "aromatic_carboxylate_mfs_transporters", "Aromatic and carboxylate MFS transporters", "Named or substrate-class-supported aromatic-acid, organic-acid, uronate, glucarate, tartrate, and related carboxylate transporter candidates.", by_category.get("pcaK_anchor", []) + by_category.get("aromatic_carboxylate_transporter", []) + by_category.get("carboxylate_transporter", []) + by_category.get("carboxylate_candidate", [])),
                part(2, "MFS symporter and compatible-solute candidates", "mfs_symporter_compatible_solute_candidates", "MFS symporter and compatible-solute candidates", "H+-coupled/MHS-like symporters, alpha-ketoglutarate permease candidates, ProP-like compatible-solute context, and amino-acid MFS candidates.", by_category.get("alpha_ketoglutarate_symporter", []) + by_category.get("compatible_solute_symporter", []) + by_category.get("mfs_symporter_candidate", []) + by_category.get("amino_acid_mfs", [])),
                part(3, "Drug and xenobiotic efflux MFS transporters", "drug_xenobiotic_efflux_mfs_transporters", "Drug and xenobiotic efflux MFS transporters", "Bcr/CmlA, EmrB/QacA, fosmidomycin-efflux, and generic efflux-labeled MFS transporter candidates.", by_category.get("bcr_cmla_efflux", []) + by_category.get("emrb_qaca_efflux", []) + by_category.get("fosmidomycin_efflux", []) + by_category.get("mfs_efflux_candidate", [])),
                part(4, "Sugar and cyanate MFS transporters", "sugar_cyanate_mfs_transporters", "Sugar and cyanate MFS transporters", "SotB/sugar-efflux, sugar-like, and CynX/cyanate MFS transporter candidates.", by_category.get("sugar_efflux", []) + by_category.get("cyanate_transporter", [])),
                part(5, "Nicotinate transporter context", "nicotinate_transporter_context", "Nicotinate transporter context", "Curated NicT anchor retained as nicotinate-pathway-associated MFS transporter context.", by_category.get("nicotinate_context", [])),
                part(6, "Generic or low-resolution MFS transporters", "generic_low_resolution_mfs_transporters", "Generic or low-resolution MFS transporters", "MFS-family proteins with broad transporter, membrane, or transmembrane domain support but unresolved substrate specificity.", by_category.get("generic_mfs", [])),
                part(7, "Membrane acyltransferase side node", "membrane_acyltransferase_side_node", "Membrane acyltransferase side node", "PP_1700 is retained as a membrane acyltransferase/MFS-fold side node rather than a confident substrate transporter.", by_category.get("membrane_acyltransferase", [])),
            ],
        },
    }
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    infos = [load_info(row) for row in load_rows()]
    for info in infos:
        write_gene(info)
    write_module(infos)
    print(
        f"Wrote {sum(1 for info in infos if info['gene'] not in PRESERVE_GENE_REVIEWS)} gene reviews, "
        f"patched {len(PRESERVE_GENE_REVIEWS)} preserved anchors, and wrote {MODULE_PATH.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
