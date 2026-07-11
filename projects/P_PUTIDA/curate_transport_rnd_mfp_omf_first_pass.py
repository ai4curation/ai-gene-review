#!/usr/bin/env python3
"""First-pass curation for RND/MFP/OMF transport split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = ROOT / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_rnd_tripartite_efflux_and_mfp_omf_systems.tsv"
MODULE_PATH = ROOT / "modules/rnd_multidrug_efflux_boundary.yaml"

TAXON = {
    "id": "NCBITaxon:160488",
    "label": "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)",
}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
    "PMID:36807028": "The ABC transporter family efflux pump PvdRT-OpmQ of Pseudomonas putida KT2440 facilitates pyoverdine secretion in addition to its other role in secretion of medium-chain-length polyhydroxyalkanoates",
}

TERMS = {
    "GO:0005886": "plasma membrane",
    "GO:0006812": "monoatomic cation transport",
    "GO:0006869": "lipid transport",
    "GO:0006882": "intracellular zinc ion homeostasis",
    "GO:0008324": "monoatomic cation transmembrane transporter activity",
    "GO:0009279": "cell outer membrane",
    "GO:0009306": "protein secretion",
    "GO:0015031": "protein transport",
    "GO:0015086": "cadmium ion transmembrane transporter activity",
    "GO:0015093": "ferrous iron transmembrane transporter activity",
    "GO:0015267": "channel activity",
    "GO:0015288": "porin activity",
    "GO:0015341": "zinc efflux antiporter activity",
    "GO:0015562": "efflux transmembrane transporter activity",
    "GO:0015679": "plasma membrane copper ion transport",
    "GO:0015718": "monocarboxylic acid transport",
    "GO:0015721": "bile acid and bile salt transport",
    "GO:0015891": "siderophore transport",
    "GO:0016020": "membrane",
    "GO:0019867": "outer membrane",
    "GO:0019898": "extrinsic component of membrane",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0030253": "protein secretion by the type I secretion system",
    "GO:0030256": "type I protein secretion system complex",
    "GO:0030288": "outer membrane-bounded periplasmic space",
    "GO:0030313": "cell envelope",
    "GO:0034755": "iron ion transmembrane transport",
    "GO:0042597": "periplasmic space",
    "GO:0042908": "xenobiotic transport",
    "GO:0042910": "xenobiotic transmembrane transporter activity",
    "GO:0046677": "response to antibiotic",
    "GO:0046914": "transition metal ion binding",
    "GO:0055085": "transmembrane transport",
    "GO:0060003": "copper ion export",
    "GO:0070574": "cadmium ion transmembrane transport",
    "GO:0071577": "zinc ion transmembrane transport",
    "GO:0098655": "monoatomic cation transmembrane transport",
    "GO:1990195": "macrolide transmembrane transporter complex",
    "GO:1990281": "efflux pump complex",
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


def classify(gene: str, product: str, uniprot_text: str) -> str:
    if gene in {"czcA-I", "czcA-II"}:
        return "czc_rnd"
    if gene in {"czcB-I", "czcB-II"}:
        return "czc_mfp"
    if gene in {"czcC-I", "czcC-II"}:
        return "czc_omf"
    if gene == "fieF":
        return "cdf_metal"
    if gene == "pvdR":
        return "pvdR"
    if gene == "tolC":
        return "tolc_anchor"
    lower = product.lower()
    if "eama" in uniprot_text.lower() or gene == "PP_4568":
        return "eamA_transporter"
    if "T1SS_HlyD" in uniprot_text or "Secretion_HlyD_CS" in uniprot_text:
        return "type_i_mfp"
    if "T1SS_OMP_TolC" in uniprot_text or "type_I_sec_TolC" in uniprot_text:
        return "type_i_omf"
    if "outer membrane factor" in uniprot_text.lower() or "outer membrane protein" in lower or "outer membrane efflux" in lower:
        return "omf"
    if "membrane fusion" in lower or "mfp" in uniprot_text.lower() or "rnd_pump_mfp" in uniprot_text.lower():
        return "mfp"
    if "mfs" in lower or "emrb" in uniprot_text.lower() or "major facilitator" in uniprot_text.lower():
        return "mfs_transporter"
    if "rnd" in lower or "acrflvin-r" in uniprot_text.lower() or "mmpl" in uniprot_text.lower():
        return "rnd_transporter"
    return "generic_transporter"


def load_info(row: dict[str, str]) -> dict[str, object]:
    gene = row["gene"]
    uniprot = GENE_ROOT / gene / f"{gene}-uniprot.txt"
    asta = GENE_ROOT / gene / f"{gene}-deep-research-asta.md"
    review = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    uniprot_lines = uniprot.read_text(encoding="utf-8").splitlines()
    asta_lines = asta.read_text(encoding="utf-8").splitlines()
    uniprot_text = "\n".join(uniprot_lines)
    product = row["protein_name"]
    category = classify(gene, product, uniprot_text)
    review_doc = yaml.safe_load(review.read_text(encoding="utf-8"))

    line_by_key = {
        "de": first_line(uniprot_lines, "DE   "),
        "function": first_line(uniprot_lines, "CC   -!- FUNCTION:", optional=True),
        "subunit": first_line(uniprot_lines, "CC   -!- SUBUNIT:", optional=True),
        "location_outer": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell outer membrane", optional=True),
        "location_inner": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell inner membrane", optional=True),
        "location_cell": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell membrane", optional=True),
        "location_membrane": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Membrane", optional=True),
        "location_periplasm": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Periplasm", optional=True),
        "family": first_line(uniprot_lines, "CC   -!- SIMILARITY:", optional=True),
        "rnd_domain": first_line(uniprot_lines, "DR   InterPro; IPR001036; Acrflvin-R.", optional=True),
        "mmp_domain": first_line(uniprot_lines, "DR   InterPro; IPR004869; MMPL_dom.", optional=True),
        "mfp_domain": first_line(uniprot_lines, "DR   InterPro; IPR006143; RND_pump_MFP.", optional=True)
        or first_line(uniprot_lines, "DR   InterPro; IPR050739; MFP.", optional=True),
        "omf_domain": first_line(uniprot_lines, "DR   InterPro; IPR003423; OMP_efflux.", optional=True),
        "t1ss_hlyd": first_line(uniprot_lines, "DR   InterPro; IPR010129; T1SS_HlyD.", optional=True),
        "t1ss_tolc": first_line(uniprot_lines, "DR   InterPro; IPR010130; T1SS_OMP_TolC.", optional=True),
        "mfs_domain": first_line(uniprot_lines, "DR   InterPro; IPR011701; MFS.", optional=True),
        "eamA_domain": first_line(uniprot_lines, "DR   InterPro; IPR000620; EamA_dom.", optional=True),
        "cdf_domain": first_line(uniprot_lines, "DR   InterPro; IPR002524; Cation_efflux.", optional=True),
        "fieF_domain": first_line(uniprot_lines, "DR   InterPro; IPR050291; FieF-like.", optional=True),
        "asta": first_line(asta_lines, "- **Protein Description:**"),
    }
    return {
        "gene": gene,
        "id": row["uniprot_accession"],
        "locus": row["ordered_locus"],
        "product": product,
        "category": category,
        "line_by_key": line_by_key,
        "go_ids": [ann["term"]["id"] for ann in review_doc.get("existing_annotations", [])],
        "existing_refs": {ref["id"]: ref for ref in review_doc.get("references", []) if "id" in ref},
    }


def support_lines(info: dict[str, object], *keys: str) -> list[dict[str, str]]:
    gene = info["gene"]
    lines = info["line_by_key"]
    uniprot_ref = ref_file(gene, "uniprot.txt")
    asta_ref = ref_file(gene, "deep-research-asta.md")
    requested = [lines.get(key) for key in keys] if keys else [lines["de"], lines.get("family")]
    requested.append(lines["asta"])
    out: list[dict[str, str]] = []
    for line in dedupe(requested):
        out.append(support(asta_ref if line == lines["asta"] else uniprot_ref, line))
    return out


def core_keys(info: dict[str, object]) -> tuple[str, ...]:
    category = info["category"]
    if category in {"czc_rnd", "rnd_transporter"}:
        return ("de", "family", "rnd_domain", "mmp_domain")
    if category in {"czc_mfp", "mfp"}:
        return ("de", "family", "mfp_domain")
    if category in {"czc_omf", "omf"}:
        return ("de", "family", "omf_domain")
    if category == "type_i_mfp":
        return ("de", "family", "mfp_domain", "t1ss_hlyd")
    if category == "type_i_omf":
        return ("de", "family", "omf_domain", "t1ss_tolc")
    if category == "mfs_transporter":
        return ("de", "family", "mfs_domain")
    if category == "eamA_transporter":
        return ("de", "family", "eamA_domain")
    if category == "cdf_metal":
        return ("de", "family", "cdf_domain", "fieF_domain")
    if category == "pvdR":
        return ("de", "function", "subunit", "location_periplasm", "mfp_domain")
    return ("de", "family")


def description(info: dict[str, object]) -> str:
    gene = info["gene"]
    product = info["product"]
    category = info["category"]
    if category == "czc_rnd":
        return f"{gene} encodes {product}, an inner-membrane RND-family cation-efflux transporter component of a predicted cobalt-zinc-cadmium resistance system."
    if category == "czc_mfp":
        return f"{gene} encodes {product}, a membrane-fusion/adaptor component associated with a predicted Czc cobalt-zinc-cadmium efflux system."
    if category == "czc_omf":
        return f"{gene} encodes {product}, a TolC/NodT-family outer-membrane factor associated with a predicted Czc cobalt-zinc-cadmium efflux system."
    if category == "rnd_transporter":
        return f"{gene} encodes {product}, an inner-membrane RND-family efflux transporter candidate with unresolved substrate range."
    if category == "mfp":
        return f"{gene} encodes {product}, a membrane-fusion/adaptor component candidate for a bacterial efflux pump or related envelope transport assembly."
    if category == "omf":
        return f"{gene} encodes {product}, a TolC/NodT-family outer-membrane factor candidate for an efflux or envelope transport assembly."
    if category == "type_i_mfp":
        return f"{gene} encodes {product}, a HlyD-family membrane-fusion component candidate with type-I secretion system domain context."
    if category == "type_i_omf":
        return f"{gene} encodes {product}, a TolC-like outer-membrane factor candidate with type-I secretion and efflux-channel domain context."
    if category == "mfs_transporter":
        return f"{gene} encodes {product}, an MFS-family efflux or metabolite transporter candidate with unresolved substrate range."
    if category == "eamA_transporter":
        return f"{gene} encodes {product}, an EamA-family small-molecule efflux transporter candidate."
    if category == "cdf_metal":
        return f"{gene} encodes {product}, a CDF-family metal-cation efflux transporter associated with zinc, cadmium, and ferrous-iron transport/homeostasis annotations."
    if category == "pvdR":
        return f"{gene} encodes {product}, the periplasmic membrane-fusion/adaptor subunit of the PvdRT-OpmQ pyoverdine export system."
    return f"{gene} encodes {product}."


def replacement(go_id: str) -> list[dict[str, str]]:
    return [term(go_id)]


def review_for_annotation(info: dict[str, object], ann: dict[str, object]) -> dict[str, object]:
    category = info["category"]
    go_id = ann["term"]["id"]

    if go_id in {"GO:0005886", "GO:0016020", "GO:0009279", "GO:0019867", "GO:0030288", "GO:0030313", "GO:0042597", "GO:0019898"}:
        return {
            "summary": "The cellular-component annotation matches the envelope or membrane context for this transporter or transport-system component.",
            "action": "ACCEPT",
            "reason": "The UniProt product, localization, family, or domain metadata support this broad cellular location.",
            "supported_by": support_lines(info, "de", "location_outer", "location_inner", "location_cell", "location_membrane", "location_periplasm", *core_keys(info)),
        }
    if go_id == "GO:1990281":
        return {
            "summary": "Efflux pump complex membership is appropriate component-level context.",
            "action": "ACCEPT",
            "reason": "The protein is annotated as an RND/MFP/OMF efflux component or a pyoverdine export pump adaptor, supporting pump-complex context while leaving exact partner assignments unresolved for generic paralogs.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0015562":
        if category in {"rnd_transporter", "czc_rnd"}:
            return {
                "summary": "Efflux transporter activity is consistent with the inner-membrane transporter component.",
                "action": "ACCEPT",
                "reason": "The product and RND-family domain evidence support efflux transporter activity for this inner-membrane component.",
                "supported_by": support_lines(info, *core_keys(info)),
            }
        return {
            "summary": "Efflux transporter activity is biologically close but too direct for an adaptor or outer-membrane channel component.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": "MFP and OMF components contribute to pump-level efflux but are not the standalone substrate-translocating inner-membrane transporter.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0022857":
        if category in {"rnd_transporter", "mfs_transporter", "eamA_transporter", "cdf_metal", "czc_rnd"}:
            return {
                "summary": "Broad transporter activity is consistent with this inner-membrane transporter candidate.",
                "action": "ACCEPT" if category in {"mfs_transporter", "eamA_transporter"} else "KEEP_AS_NON_CORE",
                "reason": "The product/domain evidence supports transporter activity; where a more specific efflux or cation term is available, this broad row is retained as non-core.",
                "supported_by": support_lines(info, *core_keys(info)),
            }
        return {
            "summary": "Direct transporter activity is likely over-specific for an MFP or OMF component.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": "Adaptor and outer-membrane factor proteins support pump assembly/function but are not by themselves the transmembrane transporter.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0055085":
        return {
            "summary": "Transmembrane transport is appropriate broad process context for this efflux or transport-system component.",
            "action": "ACCEPT",
            "reason": "The product/domain evidence supports participation in a membrane transport or efflux process, even when exact substrate specificity remains unresolved.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0042908", "GO:0042910"}:
        if category in {"czc_rnd", "czc_mfp", "czc_omf", "cdf_metal"}:
            return {
                "summary": "Xenobiotic transport is not the best substrate class for the metal-cation efflux context.",
                "action": "MODIFY",
                "reason": "The product and domain evidence support cation/metal efflux rather than xenobiotic export for this Czc/FieF-family protein.",
                "proposed_replacement_terms": replacement("GO:0098655" if go_id == "GO:0042908" else "GO:0008324"),
                "supported_by": support_lines(info, *core_keys(info)),
            }
        return {
            "summary": "Xenobiotic transport/activity is acceptable broad context for an RND multidrug efflux transporter.",
            "action": "ACCEPT",
            "reason": "The product/domain evidence supports an RND or multidrug efflux transporter; exact substrates remain unresolved.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0006812", "GO:0008324", "GO:0098655"}:
        return {
            "summary": "The cation transport annotation matches the Czc/FieF metal-efflux context.",
            "action": "ACCEPT",
            "reason": "The product and cation-efflux or Czc-family domain evidence support broad monoatomic cation transport.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0015679", "GO:0060003"}:
        return {
            "summary": "Copper transport/export is probably too specific for the fetched CzcB cobalt-zinc-cadmium resistance proteins.",
            "action": "MODIFY",
            "reason": "The local product name and CzcB-like domains support transition-metal/cation efflux context, but do not establish copper as the specific substrate.",
            "proposed_replacement_terms": replacement("GO:0098655"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0046914":
        return {
            "summary": "Transition-metal binding is plausible family context but is less informative than pump-component transport context.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The CzcB-like MFP assignment supports metal-efflux context; direct binding is retained as non-core until substrate and binding evidence are resolved.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0015288"}:
        return {
            "summary": "Porin activity is an imprecise description of a TolC/NodT-family outer-membrane factor.",
            "action": "MODIFY",
            "reason": "The protein is better modeled as an outer-membrane channel factor for an efflux or type-I secretion assembly rather than as a generic porin.",
            "proposed_replacement_terms": replacement("GO:0015267"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0009306":
        return {
            "summary": "Protein secretion is appropriate for the HlyD/type-I secretion component context, but a type-I secretion process is more specific.",
            "action": "MODIFY",
            "reason": "The HlyD/type-I secretion family/domain evidence supports type-I secretion-system context.",
            "proposed_replacement_terms": replacement("GO:0030253"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0015031":
        return {
            "summary": "Broad protein transport is plausible but less informative than type-I secretion context for HlyD-family components.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The type-I secretion/HlyD domain signal supports a secretion-system component role, but substrate specificity remains unresolved.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0046677":
        return {
            "summary": "Antibiotic response is plausible efflux phenotype context but is not the core molecular role.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The protein/domain evidence supports efflux-system component function; response-to-antibiotic is retained as phenotype context pending direct substrate/condition evidence.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0015718", "GO:0015721", "GO:0006869"}:
        return {
            "summary": "The substrate-specific transport process is not established by the lightweight evidence for this efflux component.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": "The product and domain evidence support broad multidrug/efflux-system context, not a specific lipid, bile-acid, or monocarboxylate substrate.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:1990961":
        if category == "pvdR":
            return {
                "summary": "Xenobiotic detoxification export is not the best description of the characterized PvdR pyoverdine export role.",
                "action": "MODIFY",
                "reason": "UniProt records PvdR as part of the PvdRT-OpmQ pyoverdine export system, not as a generic xenobiotic detoxification exporter.",
                "proposed_replacement_terms": replacement("GO:0015891"),
                "supported_by": support_lines(info, *core_keys(info)),
            }
        return {
            "summary": "Xenobiotic detoxification by export is acceptable broad context for this multidrug efflux transporter.",
            "action": "ACCEPT",
            "reason": "The MFS/Emr product and domain evidence support multidrug efflux context, with exact substrates unresolved.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:1990195":
        return {
            "summary": "Macrolide transporter-complex assignment is over-specific for PvdR.",
            "action": "MODIFY",
            "reason": "The UniProt function and subunit comments support the PvdRT-OpmQ pyoverdine export system rather than a macrolide transporter complex.",
            "proposed_replacement_terms": replacement("GO:1990281"),
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0015086", "GO:0015093", "GO:0015341", "GO:0006882", "GO:0034755", "GO:0070574", "GO:0071577"}:
        return {
            "summary": "The metal-cation transport or zinc-homeostasis annotation matches the FieF/CDF transporter context.",
            "action": "ACCEPT",
            "reason": "The UniProt product and CDF/FieF-like domain evidence support metal-cation efflux and zinc/iron/cadmium transport context.",
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
            "summary": summary or f"Adds {TERMS[go_id]} as a conservative first-pass term absent from the fetched GOA rows.",
            "action": "NEW",
            "reason": "The product and domain metadata support this component-level assignment in the first-pass review.",
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

    if category in {"mfp", "czc_mfp"}:
        add("GO:0015562", "contributes_to", "Adds pump-level efflux activity as a contributes-to term for an MFP/adaptor component.")
        add("GO:0055085", "involved_in")
        add("GO:1990281", "part_of")
        if not (present & {"GO:0016020", "GO:0030313", "GO:0030288"}):
            add("GO:0016020", "located_in")
    if category in {"omf", "czc_omf"}:
        add("GO:0015267", "enables", "Adds channel activity for a TolC/NodT-family outer-membrane factor.")
        add("GO:1990281", "part_of")
        if not (present & {"GO:0009279", "GO:0019867"}):
            add("GO:0009279", "located_in")
    if category in {"type_i_mfp", "type_i_omf"}:
        if category == "type_i_omf":
            add("GO:0015267", "enables", "Adds channel activity for a TolC-like outer-membrane factor.")
        add("GO:0030253", "involved_in")
        add("GO:0030256", "part_of")
    if category in {"rnd_transporter", "mfs_transporter", "eamA_transporter"}:
        add("GO:0022857", "enables")
        add("GO:0055085", "involved_in")
        if not (present & {"GO:0005886", "GO:0016020"}):
            add("GO:0016020", "located_in")
    if category == "pvdR":
        add("GO:0015891", "involved_in", "Adds siderophore transport to capture the characterized pyoverdine export role.")
    if category in {"czc_rnd"}:
        add("GO:1990281", "part_of")


def best_location(info: dict[str, object]) -> dict[str, str]:
    present = set(info["go_ids"])
    for go_id in ("GO:0009279", "GO:0019867", "GO:0042597", "GO:0030288", "GO:0030313", "GO:0005886", "GO:0016020"):
        if go_id in present:
            return term(go_id)
    category = info["category"]
    if category in {"omf", "czc_omf", "type_i_omf"}:
        return term("GO:0009279")
    if category == "pvdR":
        return term("GO:0042597")
    if category in {"rnd_transporter", "czc_rnd", "mfs_transporter", "cdf_metal"}:
        return term("GO:0005886")
    return term("GO:0016020")


def core_functions(info: dict[str, object]) -> list[dict[str, object]]:
    category = info["category"]
    base = {"description": "", "supported_by": support_lines(info, *core_keys(info))}
    if category == "czc_rnd":
        return [{**base, "description": "RND-family cation-efflux transporter component of a predicted Czc metal-resistance pump.", "molecular_function": term("GO:0008324"), "directly_involved_in": [term("GO:0098655")], "locations": [term("GO:0005886")]}]
    if category == "czc_mfp":
        return [{**base, "description": "Membrane-fusion/adaptor component of a predicted Czc metal-cation efflux pump.", "contributes_to_molecular_function": term("GO:0015562"), "directly_involved_in": [term("GO:0055085")], "locations": [best_location(info)], "in_complex": term("GO:1990281")}]
    if category == "czc_omf":
        return [{**base, "description": "Outer-membrane factor/channel component of a predicted Czc metal-cation efflux pump.", "molecular_function": term("GO:0015267"), "directly_involved_in": [term("GO:0055085")], "locations": [term("GO:0009279")], "in_complex": term("GO:1990281")}]
    if category == "rnd_transporter":
        mf = "GO:0042910" if "GO:0042910" in info["go_ids"] else "GO:0022857"
        bp = "GO:0042908" if "GO:0042908" in info["go_ids"] else "GO:0055085"
        return [{**base, "description": "Inner-membrane RND-family efflux transporter candidate with unresolved substrate range.", "molecular_function": term(mf), "directly_involved_in": [term(bp)], "locations": [best_location(info)]}]
    if category == "mfs_transporter":
        processes = [term("GO:0055085")]
        if "GO:1990961" in info["go_ids"]:
            processes.append(term("GO:1990961"))
        return [{**base, "description": "MFS-family efflux or small-molecule transporter candidate.", "molecular_function": term("GO:0022857"), "directly_involved_in": processes, "locations": [best_location(info)]}]
    if category == "eamA_transporter":
        return [{**base, "description": "EamA-family small-molecule efflux transporter candidate.", "molecular_function": term("GO:0022857"), "directly_involved_in": [term("GO:0055085")], "locations": [best_location(info)]}]
    if category == "mfp":
        return [{**base, "description": "Membrane-fusion/adaptor component candidate for an efflux pump complex.", "contributes_to_molecular_function": term("GO:0015562"), "directly_involved_in": [term("GO:0055085")], "locations": [best_location(info)], "in_complex": term("GO:1990281")}]
    if category == "omf":
        return [{**base, "description": "TolC/NodT-family outer-membrane factor/channel candidate for an efflux pump complex.", "molecular_function": term("GO:0015267"), "directly_involved_in": [term("GO:0055085")], "locations": [best_location(info)], "in_complex": term("GO:1990281")}]
    if category == "type_i_mfp":
        return [{**base, "description": "HlyD-family membrane-fusion component candidate for a type-I secretion or related envelope export assembly.", "contributes_to_molecular_function": term("GO:0015562"), "directly_involved_in": [term("GO:0030253")], "locations": [best_location(info)], "in_complex": term("GO:0030256")}]
    if category == "type_i_omf":
        return [{**base, "description": "TolC-like outer-membrane channel candidate for a type-I secretion or related efflux assembly.", "molecular_function": term("GO:0015267"), "directly_involved_in": [term("GO:0030253")], "locations": [best_location(info)], "in_complex": term("GO:0030256")}]
    if category == "cdf_metal":
        return [{**base, "description": "CDF-family metal-cation efflux transporter associated with zinc homeostasis.", "molecular_function": term("GO:0015341"), "directly_involved_in": [term("GO:0071577"), term("GO:0006882")], "locations": [term("GO:0005886")]}]
    if category == "pvdR":
        return [{**base, "description": "Periplasmic membrane-fusion/adaptor component of the PvdRT-OpmQ pyoverdine export system.", "contributes_to_molecular_function": term("GO:0015562"), "directly_involved_in": [term("GO:0015891")], "locations": [term("GO:0042597")], "in_complex": term("GO:1990281")}]
    return []


def references_for(info: dict[str, object], annotations: list[dict[str, object]]) -> list[dict[str, object]]:
    refs: list[dict[str, object]] = []
    existing_refs = info["existing_refs"]
    for ref_id in sorted({ann.get("original_reference_id") for ann in annotations if ann.get("original_reference_id")}):
        if ref_id.startswith("file:"):
            continue
        if ref_id in existing_refs:
            refs.append(existing_refs[ref_id])
        else:
            refs.append({"id": ref_id, "title": GO_REF_TITLES.get(ref_id, ref_id), "findings": []})
    lines = info["line_by_key"]
    uniprot_lines = [
        lines["de"],
        lines.get("function"),
        lines.get("subunit"),
        lines.get("location_outer"),
        lines.get("location_inner"),
        lines.get("location_cell"),
        lines.get("location_membrane"),
        lines.get("location_periplasm"),
        lines.get("family"),
        lines.get("rnd_domain"),
        lines.get("mmp_domain"),
        lines.get("mfp_domain"),
        lines.get("omf_domain"),
        lines.get("t1ss_hlyd"),
        lines.get("t1ss_tolc"),
        lines.get("mfs_domain"),
        lines.get("eamA_domain"),
        lines.get("cdf_domain"),
        lines.get("fieF_domain"),
    ]
    refs.append({"id": ref_file(info["gene"], "uniprot.txt"), "title": f"UniProtKB entry for {info['gene']}", "findings": [{"supporting_text": line} for line in dedupe(uniprot_lines)]})
    refs.append({"id": ref_file(info["gene"], "deep-research-asta.md"), "title": f"Asta retrieval report for {info['gene']} ({info['id']})", "findings": [{"supporting_text": lines["asta"]}]})
    return refs


def write_gene(info: dict[str, object]) -> None:
    gene = info["gene"]
    if gene == "tolC":
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
                {"question": "What are the cognate partner proteins, exported substrates, and induction conditions for this efflux or envelope export component in KT2440?"}
            ],
            "suggested_experiments": [
                {
                    "description": "Combine deletion or depletion with matched susceptibility, metal-resistance, siderophore-export, secretion, and efflux assays based on the predicted system context.",
                    "experiment_type": "efflux and envelope-export genetics",
                }
            ],
        }
    )
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def patch_tolc_reference() -> None:
    gene = "tolC"
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    refs = doc.setdefault("references", [])
    ref_id = ref_file(gene, "deep-research-asta.md")
    if not any(ref.get("id") == ref_id for ref in refs):
        asta_line = first_line((GENE_ROOT / gene / f"{gene}-deep-research-asta.md").read_text(encoding="utf-8").splitlines(), "- **Protein Description:**")
        refs.append(
            {
                "id": ref_id,
                "title": "Asta retrieval report for tolC (Q88EE6)",
                "findings": [{"supporting_text": asta_line}],
            }
        )
        path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def annoton(info: dict[str, object]) -> dict[str, object]:
    gene = info["gene"]
    cores = core_functions(info)
    entry: dict[str, object] = {
        "id": f"{gene}_efflux_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {info['product']}",
    }
    if cores:
        core = cores[0]
        if "molecular_function" in core:
            entry["function"] = {"preferred_term": core["molecular_function"]["label"], "term": core["molecular_function"]}
        if "contributes_to_molecular_function" in core:
            entry["function"] = {"preferred_term": core["contributes_to_molecular_function"]["label"], "term": core["contributes_to_molecular_function"]}
        if "directly_involved_in" in core:
            entry["processes"] = [{"preferred_term": p["label"], "term": p} for p in core["directly_involved_in"]]
        if "locations" in core:
            entry["locations"] = [{"preferred_term": loc["label"], "term": loc} for loc in core["locations"]]
        if "in_complex" in core:
            entry.setdefault("locations", []).append({"preferred_term": core["in_complex"]["label"], "term": core["in_complex"]})
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
    doc = yaml.safe_load(MODULE_PATH.read_text(encoding="utf-8"))
    doc["description"] = (
        "Boundary module for RND, MFP, OMF, and related efflux/export components in Pseudomonas putida "
        "KT2440. It preserves the existing PP_2064-PP_2065 RND efflux pair and adds the "
        "transport/membrane/efflux split covering Czc metal-efflux loci, Mex/Opr and generic RND "
        "systems, MFS/Emr/EamA efflux side systems, type-I secretion/TolC-like components, PvdR "
        "pyoverdine export context, and FieF CDF metal efflux."
    )
    evidence = doc.setdefault("evidence", [])
    source_id = f"file:{BATCH_PATH.relative_to(ROOT)}"
    if not any(ev.get("source_id") == source_id for ev in evidence):
        evidence.append(
            {
                "source_id": source_id,
                "title": "PSEPK transport/membrane/efflux RND/MFP/OMF batch",
                "statement": "The partition groups 42 RND, MFP, OMF, MFS/Emr/EamA, Czc, PvdR, FieF, and TolC-like components for component-aware efflux/export curation.",
            }
        )
    module = doc["module"]
    existing_concepts = {c["term"]["id"] for c in module.get("concepts", [])}
    for go_id, desc in [
        ("GO:0022857", "Broad transporter activity for MFS/EamA and low-resolution transporter candidates."),
        ("GO:0015267", "Channel activity for TolC/NodT-family outer-membrane factors."),
        ("GO:0030253", "Type-I secretion process context for HlyD/TolC-like components."),
        ("GO:0030256", "Type-I secretion system complex context for HlyD/TolC-like components."),
        ("GO:0008324", "Cation transporter activity for CzcA-like metal-efflux components."),
        ("GO:0098655", "Broad monoatomic cation transport for Czc metal-efflux systems."),
        ("GO:0015891", "Siderophore transport context for PvdR pyoverdine export."),
        ("GO:0015341", "Zinc efflux antiporter activity for FieF/CDF context."),
        ("GO:0071577", "Zinc transmembrane transport for FieF/CDF context."),
    ]:
        if go_id not in existing_concepts:
            module.setdefault("concepts", []).append(concept(go_id, desc))
            existing_concepts.add(go_id)
    context = module.setdefault("context", {}).setdefault("cellular_components", [])
    context_ids = {c["term"]["id"] for c in context}
    for go_id, desc in [
        ("GO:0009279", "Outer-membrane location for OMF/TolC/NodT components."),
        ("GO:0042597", "Periplasmic PvdR adaptor context."),
        ("GO:0030256", "Type-I secretion system complex context."),
    ]:
        if go_id not in context_ids:
            context.append({"preferred_term": TERMS[go_id], "term": term(go_id), "description": desc})
            context_ids.add(go_id)

    by_category: dict[str, list[dict[str, object]]] = {}
    for info in infos:
        by_category.setdefault(info["category"], []).append(info)
    prior_parts = [
        p for p in module.get("parts", []) if p.get("node", {}).get("id") not in {
            "czc_metal_efflux_loci",
            "rnd_mex_generic_efflux_components",
            "mfs_emr_eama_efflux_context",
            "type_i_tolc_like_export_components",
            "pvdR_pyoverdine_export_context",
            "fieF_cdf_metal_efflux_context",
        }
    ]
    new_parts = [
        part(2, "Czc metal-efflux loci", "czc_metal_efflux_loci", "Czc cobalt-zinc-cadmium efflux loci", "Two Czc-like OMF/MFP/RND metal-efflux loci represented at component level.", by_category.get("czc_omf", []) + by_category.get("czc_mfp", []) + by_category.get("czc_rnd", [])),
        part(3, "RND/Mex/generic efflux components", "rnd_mex_generic_efflux_components", "RND, Mex, and generic MFP/OMF efflux components", "MexCD-OprJ, MexF/OprN, generic RND transporters, MFPs, and OMFs with unresolved substrate ranges.", by_category.get("rnd_transporter", []) + by_category.get("mfp", []) + by_category.get("omf", [])),
        part(4, "MFS/Emr/EamA efflux context", "mfs_emr_eama_efflux_context", "MFS, Emr, and EamA efflux context", "MFS-family transporters and associated MFP/OMF components retained as efflux side context.", by_category.get("mfs_transporter", []) + by_category.get("eamA_transporter", [])),
        part(5, "Type-I secretion and TolC-like components", "type_i_tolc_like_export_components", "Type-I secretion and TolC-like export components", "HlyD/TolC-like components that may support type-I secretion or related outer-membrane export.", by_category.get("type_i_mfp", []) + by_category.get("type_i_omf", []) + by_category.get("tolc_anchor", [])),
        part(6, "PvdR pyoverdine export context", "pvdR_pyoverdine_export_context", "PvdR pyoverdine export context", "PvdR is the periplasmic adaptor of the characterized PvdRT-OpmQ pyoverdine export system.", by_category.get("pvdR", [])),
        part(7, "FieF CDF metal efflux context", "fieF_cdf_metal_efflux_context", "FieF CDF metal efflux context", "FieF is a CDF-family cation efflux transporter with zinc/metal homeostasis annotations.", by_category.get("cdf_metal", [])),
    ]
    module["parts"] = prior_parts + new_parts
    doc["notes"] = (
        "First-pass interpretation: component terms are intentionally conservative. MFP and OMF proteins are "
        "not modeled as standalone substrate-translocating transporters; they contribute to pump-level efflux, "
        "channel, type-I secretion, or pyoverdine export context depending on product/domain evidence."
    )
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    infos = [load_info(row) for row in load_rows()]
    for info in infos:
        write_gene(info)
    patch_tolc_reference()
    write_module(infos)
    print(f"Wrote {sum(1 for info in infos if info['gene'] != 'tolC')} gene reviews, patched tolC Asta reference, and extended {MODULE_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
