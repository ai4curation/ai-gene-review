#!/usr/bin/env python3
"""First-pass curation for outer-membrane porin/channel/autotransporter split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = ROOT / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_outer_membrane_porins_channels_autotransporters.tsv"
MODULE_PATH = ROOT / "modules/transport_envelope_spillover_boundary.yaml"
PRESERVE_GENE_REVIEWS = {"oprE", "oprF", "galP", "nicP", "aqpZ"}

TAXON = {
    "id": "NCBITaxon:160488",
    "label": "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)",
}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on inter-ontology links",
    "GO_REF:0000116": "Automatic transfer of experimentally verified manual GO annotation data to orthologs using Ensembl Compara",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
    "PMID:20931591": "Autotransporter esterase EstP from Pseudomonas putida KT2440: biochemical characterization and functional role",
}

TERMS = {
    "GO:0005886": "plasma membrane",
    "GO:0006629": "lipid metabolic process",
    "GO:0006833": "water transport",
    "GO:0008643": "carbohydrate transport",
    "GO:0009279": "cell outer membrane",
    "GO:0009306": "protein secretion",
    "GO:0015250": "water channel activity",
    "GO:0015254": "glycerol channel activity",
    "GO:0015267": "channel activity",
    "GO:0015288": "porin activity",
    "GO:0015483": "long-chain fatty acid transporting porin activity",
    "GO:0015793": "glycerol transmembrane transport",
    "GO:0015909": "long-chain fatty acid transport",
    "GO:0016020": "membrane",
    "GO:0016298": "lipase activity",
    "GO:0016788": "hydrolase activity, acting on ester bonds",
    "GO:0019867": "outer membrane",
    "GO:0044384": "host outer membrane",
    "GO:0046521": "sphingoid catabolic process",
    "GO:0052816": "long-chain fatty acyl-CoA hydrolase activity",
    "GO:0055085": "transmembrane transport",
    "GO:0097347": "TAM protein secretion complex",
    "GO:0106435": "carboxylesterase activity",
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
    if gene == "estP":
        return "autotransporter_esterase"
    if gene == "PP_2892":
        return "tama"
    if gene == "PP_1689":
        return "fadl_fatty_acid_porin"
    if gene in {"glpF", "aqpZ"}:
        return "aquaporin"
    if "carbohydrate-selective porin" in product or "IPR007049" in interpro:
        return "oprb_carbohydrate_porin"
    if gene in {"oprF", "oprG", "PP_3214"}:
        return "outer_membrane_protein_context"
    if "IPR005318" in interpro:
        return "oprd_family_porin"
    if "porin" in product or "IPR023614" in interpro or "IPR032638" in interpro:
        return "generic_porin"
    return "outer_membrane_protein_context"


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
        "location_outer": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell outer membrane", optional=True),
        "location_inner": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell inner membrane", optional=True),
        "location_membrane": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Membrane", optional=True),
        "kw_outer": first_line(uniprot_lines, "KW   Cell outer membrane", optional=True),
        "kw_membrane": first_line(uniprot_lines, "KW   Membrane", optional=True),
        "kw_porin": first_line(uniprot_lines, "Porin", optional=True),
        "family": first_line(uniprot_lines, "CC   -!- SIMILARITY:", optional=True),
        "oprd_family": first_line(uniprot_lines, "DR   InterPro; IPR005318; OM_porin_bac.", optional=True),
        "porin_domain": first_line(uniprot_lines, "DR   InterPro; IPR023614; Porin_dom_sf.", optional=True),
        "porin_op": first_line(uniprot_lines, "DR   InterPro; IPR010870; Porin_O/P.", optional=True),
        "oprb": first_line(uniprot_lines, "DR   InterPro; IPR007049; Carb-sel_porin_OprB.", optional=True),
        "oprb_porin": first_line(uniprot_lines, "DR   InterPro; IPR052932; OprB_Porin.", optional=True),
        "aquaporin": first_line(uniprot_lines, "DR   InterPro; IPR023271; Aquaporin-like.", optional=True),
        "aquaporin_z": first_line(uniprot_lines, "DR   InterPro; IPR023743; Aquaporin_Z.", optional=True),
        "mip": first_line(uniprot_lines, "DR   InterPro; IPR000425; MIP.", optional=True),
        "fadl": first_line(uniprot_lines, "DR   InterPro; IPR005017; OMPP1/FadL/TodX.", optional=True),
        "autotransporter": first_line(uniprot_lines, "DR   InterPro; IPR005546; Autotransporte_beta.", optional=True),
        "gdsl": first_line(uniprot_lines, "DR   InterPro; IPR001087; GDSL.", optional=True),
        "estp": first_line(uniprot_lines, "DR   InterPro; IPR048099; Esterase_EstP/EstA.", optional=True),
        "ompw": first_line(uniprot_lines, "DR   InterPro; IPR005618; OMPW.", optional=True),
        "opr_f": first_line(uniprot_lines, "DR   InterPro; IPR008722; OprF_membrane_N.", optional=True),
        "tama": first_line(uniprot_lines, "DR   InterPro; IPR035243; TamA_POTRA_Dom_1.", optional=True),
        "tama_potra": first_line(uniprot_lines, "DR   InterPro; IPR010827; BamA/TamA_POTRA.", optional=True),
        "porin5": first_line(uniprot_lines, "DR   InterPro; IPR032638; Porin_5.", optional=True),
        "nucleoside_binding": first_line(uniprot_lines, "DR   InterPro; IPR018013; Nuc_channel-bd.", optional=True),
        "transmem": first_line(uniprot_lines, "FT   TRANSMEM", optional=True),
        "signal": first_line(uniprot_lines, "KW   Signal", optional=True),
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
    if category == "autotransporter_esterase":
        return ("de", "function", "location_outer", "autotransporter", "estp", "gdsl")
    if category == "tama":
        return ("de", "location_outer", "family", "tama", "tama_potra")
    if category == "fadl_fatty_acid_porin":
        return ("de", "location_outer", "family", "fadl")
    if category == "aquaporin":
        return ("de", "function", "location_inner", "location_membrane", "family", "aquaporin", "aquaporin_z", "mip")
    if category == "oprb_carbohydrate_porin":
        return ("de", "family", "oprb", "oprb_porin")
    if category == "oprd_family_porin":
        return ("de", "family", "oprd_family", "porin_domain", "signal")
    if category == "generic_porin":
        return ("de", "porin_domain", "porin_op", "porin5", "signal")
    return ("de", "location_outer", "kw_outer", "kw_membrane", "ompw", "opr_f", "nucleoside_binding", "porin_domain")


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
    if category == "autotransporter_esterase":
        return f"{gene} encodes {product}, an outer-membrane autotransporter GDSL/carboxylesterase enzyme."
    if category == "tama":
        return f"{gene} encodes {product}, an outer-membrane TamA-family autotransporter assembly factor."
    if category == "fadl_fatty_acid_porin":
        return f"{gene} encodes {product}, an OmpP1/FadL-family outer-membrane long-chain fatty-acid transport porin."
    if category == "aquaporin":
        return f"{gene} encodes {product}, a MIP/aquaporin-family channel protein."
    if category == "oprb_carbohydrate_porin":
        return f"{gene} encodes {product}, an OprB-family carbohydrate-selective porin candidate."
    if category == "oprd_family_porin":
        return f"{gene} encodes {product}, an OprD-family outer-membrane porin candidate."
    if category == "generic_porin":
        return f"{gene} encodes {product}, a predicted porin or porin-domain outer-envelope protein with unresolved substrate specificity."
    return f"{gene} encodes {product}, an outer-membrane or envelope protein with unresolved transport or structural role."


def replacement(go_id: str) -> list[dict[str, str]]:
    return [term(go_id)]


def review_for_annotation(info: dict[str, object], ann: dict[str, object]) -> dict[str, object]:
    go_id = ann["term"]["id"]
    category = info["category"]
    if go_id in {"GO:0009279", "GO:0019867", "GO:0016020", "GO:0005886"}:
        action = "ACCEPT"
        if go_id == "GO:0016020" and {"GO:0009279", "GO:0019867", "GO:0005886"} & set(info["go_ids"]):
            action = "KEEP_AS_NON_CORE"
        return {
            "summary": "The membrane or outer-membrane localization matches the predicted channel, porin, autotransporter, or envelope-protein context.",
            "action": action,
            "reason": "The UniProt product, subcellular-location or membrane keyword, signal peptide, and porin/autotransporter/channel family evidence support membrane localization; more specific outer-membrane terms are preferred when directly present.",
            "supported_by": support_lines(info, "de", "location_outer", "location_inner", "location_membrane", "kw_outer", "kw_membrane", *core_keys(info)),
        }
    if go_id == "GO:0044384":
        return {
            "summary": "Host outer membrane is not the appropriate cellular-component context for this bacterial outer-membrane protein.",
            "action": "MODIFY",
            "reason": "The protein is encoded by Pseudomonas putida and the local evidence supports bacterial outer-membrane localization, not localization to a host outer membrane.",
            "proposed_replacement_terms": replacement("GO:0019867"),
            "supported_by": support_lines(info, "de", "ompw", "kw_outer", "kw_membrane"),
        }
    if go_id == "GO:0015288":
        return {
            "summary": "Porin activity is appropriate for the OprD/OprB/generic porin-domain context.",
            "action": "ACCEPT",
            "reason": "The product and porin-family/domain evidence support porin activity while substrate-specific calls remain limited to product-name or family context.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0055085":
        return {
            "summary": "Broad transmembrane transport is appropriate process context for this channel or porin candidate.",
            "action": "ACCEPT",
            "reason": "The product and channel/porin family evidence support a transport process, while exact substrates are left unresolved for generic paralogs.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0008643":
        return {
            "summary": "Carbohydrate transport is appropriate for the OprB-family carbohydrate-selective porin.",
            "action": "ACCEPT",
            "reason": "The product name and OprB carbohydrate-selective porin family evidence support carbohydrate transport at substrate-class resolution.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0015254", "GO:0015793"}:
        return {
            "summary": "Glycerol channel activity and glycerol transport are appropriate for the GlpF aquaglyceroporin.",
            "action": "ACCEPT",
            "reason": "The product and MIP/aquaporin family context support aquaglyceroporin function; the fetched GOA rows already provide the glycerol-specific channel/process terms.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0015250", "GO:0006833"}:
        return {
            "summary": "Water channel activity and water transport are appropriate for the AqpZ aquaporin.",
            "action": "ACCEPT",
            "reason": "The product and Aquaporin Z family evidence support water-channel function.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0015267":
        return {
            "summary": "Broad channel activity is supported but less informative than the aquaporin/aquaglyceroporin-specific activity.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The protein is a channel, but the more specific water or glycerol channel annotation better represents core function.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0015483", "GO:0015909"}:
        return {
            "summary": "Long-chain fatty-acid transport porin context is appropriate for the OmpP1/FadL-family protein.",
            "action": "ACCEPT",
            "reason": "The product name, outer-membrane localization, and OmpP1/FadL family evidence support long-chain fatty-acid transport through an outer-membrane porin.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0106435", "GO:0052816"}:
        return {
            "summary": "The specific esterase/acyl-CoA hydrolase activity is supported for EstP.",
            "action": "ACCEPT",
            "reason": "EstP is annotated as an autotransporter esterase/palmitoyl-CoA hydrolase and has both UniProt family evidence and direct experimental GOA support for these hydrolase activities.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0016298", "GO:0016788"}:
        return {
            "summary": "The broad lipase/ester-bond hydrolase annotation is supported but less informative than the specific EstP carboxylesterase/acyl-CoA hydrolase terms.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The GDSL/autotransporter esterase evidence supports hydrolase activity, but the specific carboxylesterase and long-chain fatty acyl-CoA hydrolase annotations better capture EstP function.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0006629":
        return {
            "summary": "Lipid metabolic process is appropriate broad process context for the EstP lipid/ester hydrolase.",
            "action": "ACCEPT",
            "reason": "The product and hydrolase annotations support lipid/ester metabolism context without requiring a more specific in vivo lipid substrate.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0009306", "GO:0097347"}:
        return {
            "summary": "Protein secretion/TAM complex context is appropriate for the TamA-family outer-membrane assembly factor.",
            "action": "ACCEPT",
            "reason": "The product name and TamA/POTRA family evidence support an outer-membrane TamA autotransporter-assembly role rather than generic porin function.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0046521":
        return {
            "summary": "Sphingoid catabolic process is unsupported for this P. putida porin-like membrane protein.",
            "action": "REMOVE",
            "reason": "The local product and Mpo1-like/membrane evidence support a porin-like membrane protein, not a sphingoid catabolic pathway role in KT2440.",
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
            "reason": "The product, family, and domain metadata support this assignment in the first-pass review.",
            "supported_by": support_lines(info, *core_keys(info)),
        },
    }


def best_location_id(info: dict[str, object]) -> str:
    go_ids = set(info["go_ids"])
    product = str(info["product"]).lower()
    lines = info["line_by_key"]
    if "GO:0009279" in go_ids or lines.get("location_outer") or lines.get("kw_outer") or "outer membrane" in product:
        return "GO:0009279"
    if "GO:0019867" in go_ids:
        return "GO:0019867"
    if "GO:0005886" in go_ids or lines.get("location_inner"):
        return "GO:0005886"
    return "GO:0016020"


def add_missing_new_annotations(info: dict[str, object], annotations: list[dict[str, object]]) -> None:
    present = {ann["term"]["id"] for ann in annotations}

    def add(go_id: str, qualifier: str, summary: str | None = None) -> None:
        if go_id not in present:
            annotations.append(new_annotation(info, go_id, qualifier, summary))
            present.add(go_id)

    if not (present & {"GO:0009279", "GO:0019867", "GO:0016020", "GO:0005886"}):
        add(best_location_id(info), "located_in")
    category = info["category"]
    gene = info["gene"]
    if category in {"oprd_family_porin", "generic_porin"}:
        add("GO:0015288", "enables")
        add("GO:0055085", "involved_in")
    elif category == "oprb_carbohydrate_porin":
        add("GO:0015288", "enables")
        add("GO:0008643", "involved_in")
    elif category == "aquaporin" and gene == "glpF":
        add("GO:0015254", "enables")
        add("GO:0015793", "involved_in")
    elif category == "fadl_fatty_acid_porin":
        add("GO:0015483", "enables")
        add("GO:0015909", "involved_in")
    elif category == "autotransporter_esterase":
        add("GO:0106435", "enables")
        add("GO:0006629", "involved_in")


def core_function_terms(info: dict[str, object]) -> tuple[str | None, list[str], str, str | None]:
    category = info["category"]
    gene = info["gene"]
    if category == "autotransporter_esterase":
        return "GO:0106435", ["GO:0006629"], "Outer-membrane autotransporter carboxylesterase/acyl-CoA hydrolase.", None
    if category == "tama":
        return None, ["GO:0009306"], "Outer-membrane TamA-family autotransporter assembly factor.", "GO:0097347"
    if category == "fadl_fatty_acid_porin":
        return "GO:0015483", ["GO:0015909"], "OmpP1/FadL-family long-chain fatty-acid transporting porin.", None
    if category == "aquaporin" and gene == "aqpZ":
        return "GO:0015250", ["GO:0006833"], "Aquaporin Z water channel.", None
    if category == "aquaporin":
        return "GO:0015254", ["GO:0015793"], "Aquaglyceroporin glycerol channel.", None
    if category == "oprb_carbohydrate_porin":
        return "GO:0015288", ["GO:0008643"], "OprB-family carbohydrate-selective porin candidate.", None
    if category in {"oprd_family_porin", "generic_porin"}:
        return "GO:0015288", ["GO:0055085"], "Outer-envelope porin candidate with unresolved or product-name substrate specificity.", None
    if gene == "oprG":
        return None, ["GO:0055085"], "OprG/OMP W-family outer-membrane protein with unresolved substrate specificity.", None
    return None, [], "Outer-membrane or envelope protein with unresolved molecular function.", None


def core_functions(info: dict[str, object]) -> list[dict[str, object]]:
    mf, processes, desc, complex_id = core_function_terms(info)
    core: dict[str, object] = {
        "description": desc,
        "locations": [term(best_location_id(info))],
        "supported_by": support_lines(info, *core_keys(info)),
    }
    if mf:
        core["molecular_function"] = term(mf)
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
        lines.get("location_outer"),
        lines.get("location_inner"),
        lines.get("location_membrane"),
        lines.get("kw_outer"),
        lines.get("kw_membrane"),
        lines.get("kw_porin"),
        lines.get("family"),
        lines.get("oprd_family"),
        lines.get("porin_domain"),
        lines.get("porin_op"),
        lines.get("oprb"),
        lines.get("oprb_porin"),
        lines.get("aquaporin"),
        lines.get("aquaporin_z"),
        lines.get("mip"),
        lines.get("fadl"),
        lines.get("autotransporter"),
        lines.get("gdsl"),
        lines.get("estp"),
        lines.get("ompw"),
        lines.get("opr_f"),
        lines.get("tama"),
        lines.get("tama_potra"),
        lines.get("porin5"),
        lines.get("nucleoside_binding"),
        lines.get("transmem"),
        lines.get("signal"),
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
                {
                    "question": "What substrate, uptake condition, and physiological role apply to this outer-membrane porin, channel, or envelope protein in KT2440?"
                }
            ],
            "suggested_experiments": [
                {
                    "description": "Measure substrate uptake or permeability in wild-type, deletion, and complemented strains under inducing carbon, nitrogen, aromatic-acid, lipid, or osmotic conditions suggested by product name and gene neighborhood.",
                    "experiment_type": "targeted porin/channel genetics and permeability assay",
                }
            ],
        }
    )
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def annoton(info: dict[str, object]) -> dict[str, object]:
    gene = info["gene"]
    core = core_functions(info)[0]
    entry: dict[str, object] = {
        "id": f"{gene}_outer_membrane_porin_channel_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {info['product']}",
        "locations": [{"preferred_term": loc["label"], "term": loc} for loc in core.get("locations", [])],
    }
    if core.get("molecular_function"):
        entry["function"] = {"preferred_term": core["molecular_function"]["label"], "term": core["molecular_function"]}
    if core.get("directly_involved_in"):
        entry["processes"] = [{"preferred_term": proc["label"], "term": proc} for proc in core["directly_involved_in"]]
    return entry


def concept(go_id: str, description_text: str) -> dict[str, object]:
    return {"preferred_term": TERMS[go_id], "term": term(go_id), "description": description_text}


def ensure_concept(module_doc: dict[str, object], go_id: str, description_text: str) -> None:
    concepts = module_doc["module"].setdefault("concepts", [])
    if not any(item.get("term", {}).get("id") == go_id for item in concepts):
        concepts.append(concept(go_id, description_text))


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
    evidence = doc.setdefault("evidence", [])
    batch_source = f"file:{BATCH_PATH.relative_to(ROOT)}"
    if not any(item.get("source_id") == batch_source for item in evidence):
        evidence.append(
            {
                "source_id": batch_source,
                "title": "PSEPK transport/membrane/efflux outer-membrane porin/channel/autotransporter batch",
                "statement": "The transport partition routes 38 Opr/Opd porins, OprB carbohydrate porins, aquaporins, FadL/EstP/TamA side nodes, and low-resolution porin-domain proteins to this boundary module.",
            }
        )
    note = (
        " The transport-bucket outer-membrane porin/channel extension adds 38 genes: OprD/Opd substrate-selective "
        "porins, OprB carbohydrate porins, GlpF/AqpZ channels, FadL-family fatty-acid porin context, EstP "
        "autotransporter esterase, TamA assembly context, and low-resolution porin or outer-membrane proteins. "
        "Substrate claims are kept broad unless product/family evidence is specific; pcaP sphingoid catabolism and "
        "oprG host-outer-membrane context are treated as over-propagated electronic annotations."
    )
    if "outer-membrane porin/channel extension" not in doc.get("notes", ""):
        doc["notes"] = f"{doc.get('notes', '').rstrip()}{note}"

    for go_id, description_text in {
        "GO:0008643": "Carbohydrate transport context for OprB-family porins.",
        "GO:0015250": "Water channel activity for AqpZ.",
        "GO:0015254": "Glycerol channel activity for GlpF.",
        "GO:0015483": "Long-chain fatty-acid transporting porin activity for FadL/OmpP1-family context.",
        "GO:0015793": "Glycerol transmembrane transport for GlpF.",
        "GO:0015909": "Long-chain fatty-acid transport for FadL/OmpP1-family context.",
        "GO:0106435": "Carboxylesterase activity for EstP.",
        "GO:0006629": "Lipid metabolic process context for EstP.",
        "GO:0009306": "Protein secretion context for TamA/autotransporter assembly.",
        "GO:0097347": "TAM protein secretion complex context for TamA.",
    }.items():
        ensure_concept(doc, go_id, description_text)

    by_category: dict[str, list[dict[str, object]]] = {}
    for info in infos:
        by_category.setdefault(info["category"], []).append(info)
    existing_parts = doc["module"].setdefault("parts", [])
    new_ids = {
        "oprd_family_outer_membrane_porins",
        "oprb_carbohydrate_porins",
        "aquaporin_aquaglyceroporin_channels",
        "fatty_acid_porin_autotransporter_tama_context",
        "low_resolution_outer_membrane_porin_candidates",
    }
    doc["module"]["parts"] = [item for item in existing_parts if item.get("node", {}).get("id") not in new_ids]
    start_order = max((item.get("order", 0) for item in doc["module"]["parts"]), default=0) + 1
    doc["module"]["parts"].extend(
        [
            part(start_order, "OprD/Opd substrate-selective porins", "oprd_family_outer_membrane_porins", "OprD/Opd substrate-selective porins", "OprD-family outer-membrane porins, including named amino-acid, peptide, aromatic-acid, nicotinate, phenylacetate, and generic OprD-like candidates.", by_category.get("oprd_family_porin", [])),
            part(start_order + 1, "OprB carbohydrate-selective porins", "oprb_carbohydrate_porins", "OprB carbohydrate-selective porins", "OprB-family carbohydrate-selective porin paralogs retained at carbohydrate-transport resolution.", by_category.get("oprb_carbohydrate_porin", [])),
            part(start_order + 2, "Aquaporin and aquaglyceroporin channels", "aquaporin_aquaglyceroporin_channels", "Aquaporin and aquaglyceroporin channels", "GlpF glycerol-channel and AqpZ water-channel context.", by_category.get("aquaporin", [])),
            part(start_order + 3, "Fatty-acid porin, autotransporter esterase, and TamA context", "fatty_acid_porin_autotransporter_tama_context", "Fatty-acid porin, autotransporter esterase, and TamA context", "Boundary side nodes for FadL-family fatty-acid uptake, EstP autotransporter esterase activity, and TamA autotransporter assembly.", by_category.get("fadl_fatty_acid_porin", []) + by_category.get("autotransporter_esterase", []) + by_category.get("tama", [])),
            part(start_order + 4, "Low-resolution porin and outer-membrane candidates", "low_resolution_outer_membrane_porin_candidates", "Low-resolution porin and outer-membrane candidates", "Porin-domain, OprF/OprG-like, nucleoside-binding, and other outer-envelope proteins with unresolved substrate or structural roles.", by_category.get("generic_porin", []) + by_category.get("outer_membrane_protein_context", [])),
        ]
    )
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    infos = [load_info(row) for row in load_rows()]
    for info in infos:
        write_gene(info)
    write_module(infos)
    print(
        f"Wrote {sum(1 for info in infos if info['gene'] not in PRESERVE_GENE_REVIEWS)} gene reviews, "
        f"patched {len(PRESERVE_GENE_REVIEWS)} preserved anchors, and updated {MODULE_PATH.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
