#!/usr/bin/env python3
"""First-pass curation for protein export/secretion/outer-membrane assembly split."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes/PSEPK"
BATCH_PATH = (
    ROOT
    / "projects/P_PUTIDA/batches/module_transport_membrane_efflux_protein_export_secretion_outer_membrane_assembly.tsv"
)
MODULE_PATH = ROOT / "modules/protein_export_secretion_outer_membrane_assembly_boundary.yaml"

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
}

TERMS = {
    "GO:0004190": "aspartic-type endopeptidase activity",
    "GO:0005886": "plasma membrane",
    "GO:0008320": "protein transmembrane transporter activity",
    "GO:0009279": "cell outer membrane",
    "GO:0015031": "protein transport",
    "GO:0015562": "efflux transmembrane transporter activity",
    "GO:0015627": "type II protein secretion system complex",
    "GO:0015628": "protein secretion by the type II secretion system",
    "GO:0016020": "membrane",
    "GO:0019867": "outer membrane",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0030288": "outer membrane-bounded periplasmic space",
    "GO:0030313": "cell envelope",
    "GO:0030674": "protein-macromolecule adaptor activity",
    "GO:0042597": "periplasmic space",
    "GO:0042953": "lipoprotein transport",
    "GO:0043165": "Gram-negative-bacterium-type cell outer membrane assembly",
    "GO:0043952": "protein transport by the Sec complex",
    "GO:0044874": "lipoprotein localization to outer membrane",
    "GO:0044877": "protein-containing complex binding",
    "GO:0046819": "protein secretion by the type V secretion system",
    "GO:0051205": "protein insertion into membrane",
    "GO:0055085": "transmembrane transport",
    "GO:0071709": "membrane assembly",
    "GO:0098046": "type V protein secretion system complex",
    "GO:1990063": "Bam protein complex",
    "GO:1990281": "efflux pump complex",
}


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
    lower = product.lower()
    if gene.startswith("bamA__") or "bama" in lower:
        return "bam"
    if gene in {"bamB", "bamD", "bamE"}:
        return "bam"
    if "bame domain" in lower:
        return "bam_like"
    if gene in {"lolA", "lolB"}:
        return "lol"
    if "type ii secretion system protein h" in lower:
        return "type_ii"
    if "shlb" in lower or "fhac" in lower or "tps_om_transporter" in uniprot_text:
        return "type_v"
    if "prepilin" in lower:
        return "prepilin_peptidase"
    if "secyeg" in lower:
        return "sec_accessory"
    if "hlyd family secretion protein" in lower:
        return "mfp_candidate"
    return "other"


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
        "location_outer": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell outer membrane", optional=True),
        "location_inner": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell inner membrane", optional=True),
        "location_cell": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell membrane", optional=True),
        "location_membrane": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Membrane", optional=True),
        "location_periplasm": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Periplasm", optional=True),
        "location_envelope": first_line(uniprot_lines, "SUBCELLULAR LOCATION: Cell envelope", optional=True),
        "function": first_line(uniprot_lines, "CC   -!- FUNCTION:", optional=True),
        "family": first_line(uniprot_lines, "CC   -!- SIMILARITY:", optional=True),
        "bamA_domain": first_line(uniprot_lines, "DR   InterPro; IPR023707; OM_assembly_BamA.", optional=True),
        "bamB_domain": first_line(uniprot_lines, "DR   InterPro; IPR017687; BamB.", optional=True),
        "bamD_domain": first_line(uniprot_lines, "DR   InterPro; IPR017689; BamD.", optional=True),
        "bamE_domain": first_line(uniprot_lines, "DR   InterPro; IPR007450; BamE_dom.", optional=True),
        "lolA_domain": first_line(uniprot_lines, "DR   InterPro; IPR004564; OM_lipoprot_carrier_LolA-like.", optional=True),
        "lolB_domain": first_line(uniprot_lines, "DR   InterPro; IPR004565; OM_lipoprot_LolB.", optional=True),
        "t2ss_domain": first_line(uniprot_lines, "DR   InterPro; IPR022346; T2SS_GspH.", optional=True),
        "tps_domain": first_line(uniprot_lines, "DR   InterPro; IPR051544; TPS_OM_transporter.", optional=True),
        "prepilin_domain": first_line(uniprot_lines, "DR   InterPro; IPR000045; Prepilin_IV_endopep_pep.", optional=True),
        "sec_domain": first_line(uniprot_lines, "DR   InterPro; IPR018704; SecYEG/CpoB_TPR.", optional=True),
        "mfp_domain": first_line(uniprot_lines, "DR   InterPro; IPR050739; MFP.", optional=True),
        "rnd_mfp_domain": first_line(uniprot_lines, "DR   InterPro; IPR006143; RND_pump_MFP.", optional=True),
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
    requested = [lines.get(key) for key in keys] if keys else [lines["de"], lines.get("family")]
    requested.append(lines["asta"])
    refs: list[dict[str, str]] = []
    for line in dedupe(requested):
        refs.append(support(asta_ref if line == lines["asta"] else uniprot_ref, line))
    return refs


def core_keys(info: dict[str, object]) -> tuple[str, ...]:
    category = info["category"]
    if category == "bam":
        return ("de", "function", "bamA_domain", "bamB_domain", "bamD_domain", "bamE_domain")
    if category == "bam_like":
        return ("de", "bamE_domain")
    if category == "lol":
        return ("de", "function", "lolA_domain", "lolB_domain")
    if category == "type_ii":
        return ("de", "family", "t2ss_domain")
    if category == "type_v":
        return ("de", "tps_domain")
    if category == "prepilin_peptidase":
        return ("de", "prepilin_domain")
    if category == "sec_accessory":
        return ("de", "family", "sec_domain")
    if category == "mfp_candidate":
        return ("de", "family", "mfp_domain", "rnd_mfp_domain")
    return ("de", "family")


def description(info: dict[str, object]) -> str:
    gene = info["gene"]
    product = info["product"]
    category = info["category"]
    if category == "bam":
        return f"{gene} encodes {product}, a component of the beta-barrel assembly machinery that contributes to insertion and assembly of outer-membrane proteins in the Gram-negative outer membrane."
    if category == "bam_like":
        return f"{gene} encodes a BamE-domain outer-membrane protein assembly factor candidate. The lightweight evidence supports an outer-membrane BamE-like envelope role, but not a fully resolved BAM-complex subunit assignment."
    if category == "lol":
        return f"{gene} encodes {product}, a Lol-pathway factor involved in localization of mature bacterial lipoproteins to the outer membrane."
    if category == "type_ii":
        return f"{gene} encodes type II secretion system protein H, a pilin-like GspH-family component of the type II secretion apparatus."
    if category == "type_v":
        return f"{gene} encodes a ShlB/FhaC/HecB-family two-partner/type V secretion outer-membrane transporter candidate with POTRA/ShlB/TPS transporter domains."
    if category == "prepilin_peptidase":
        return f"{gene} encodes a membrane prepilin/type IV endopeptidase-domain peptidase candidate that likely processes pilin or pseudopilin substrates."
    if category == "sec_accessory":
        return f"{gene} encodes an ancillary SecYEG translocon subunit candidate in the YfgM/SecYEG accessory family."
    if category == "mfp_candidate":
        return f"{gene} encodes an HlyD-family membrane-fusion-protein candidate. The available metadata support a secretion or efflux-envelope component, but do not identify its cognate transporter, outer-membrane channel, or substrate."
    return f"{gene} encodes {product}."


def review_for_annotation(info: dict[str, object], go_id: str, label: str) -> dict[str, object]:
    category = info["category"]
    if go_id in {"GO:0009279", "GO:0019867", "GO:0016020", "GO:0005886", "GO:0030288", "GO:0042597", "GO:0030313"}:
        if go_id == "GO:0019867" and category == "bam":
            action = "KEEP_AS_NON_CORE"
            summary = "Outer membrane localization is correct but less specific than the bacterial cell outer membrane term where that is also present."
        elif go_id == "GO:0019867" and category == "bam_like":
            action = "ACCEPT"
            summary = "Outer membrane localization is the best available cellular-component context for this BamE-domain candidate."
        elif go_id == "GO:0016020" and category in {"mfp_candidate", "prepilin_peptidase"}:
            action = "ACCEPT"
            summary = "Membrane localization is consistent with the protein family and available UniProt localization."
        else:
            action = "ACCEPT"
            summary = "The cellular-component annotation matches the predicted location of this envelope export, secretion, or assembly factor."
        return {
            "summary": summary,
            "action": action,
            "reason": "The UniProt and Asta metadata support the envelope or membrane localization for this protein.",
            "supported_by": support_lines(
                info,
                "de",
                "location_outer",
                "location_inner",
                "location_cell",
                "location_membrane",
                "location_periplasm",
                "location_envelope",
            ),
        }
    if go_id in {"GO:0043165", "GO:0051205", "GO:1990063"}:
        return {
            "summary": "This captures the core BAM/outer-membrane protein assembly role.",
            "action": "ACCEPT",
            "reason": "The protein is a Bam-family outer-membrane assembly factor and the product/domain evidence supports participation in outer-membrane protein assembly and insertion.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0071709":
        return {
            "summary": "Membrane assembly is true but broader than the BAM-specific outer-membrane assembly process.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "Bam-family evidence supports the more specific Gram-negative cell outer membrane assembly and protein insertion terms.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0030674":
        return {
            "summary": "Adaptor activity is plausible for BamE but is less informative than BAM complex and outer-membrane assembly context.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "BamE is an accessory BAM component; this broad adapter term is retained as non-core family context.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0042953", "GO:0044874", "GO:0015031"}:
        return {
            "summary": "The lipoprotein localization/transport annotation matches the Lol-pathway role.",
            "action": "ACCEPT" if go_id != "GO:0015031" else "KEEP_AS_NON_CORE",
            "reason": "LolA/LolB metadata support outer-membrane lipoprotein localization; broad protein transport is true but less specific.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0015627", "GO:0015628"}:
        return {
            "summary": "The type-II secretion annotation matches the GspH/type-II secretion-system component role.",
            "action": "ACCEPT",
            "reason": "The product name, GSP H family line, and T2SS_GspH domain support type-II secretion-system component context.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0008320", "GO:0046819", "GO:0098046"}:
        return {
            "summary": "The type-V/two-partner secretion annotation matches the ShlB/FhaC/TPS transporter-family role.",
            "action": "ACCEPT",
            "reason": "The protein has a two-partner secretion outer-membrane transporter domain profile and TreeGrafter assigns type V secretion terms.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0004190":
        return {
            "summary": "Aspartic-type endopeptidase activity is consistent with the prepilin/type IV endopeptidase peptidase domain.",
            "action": "ACCEPT",
            "reason": "The InterPro/Pfam peptidase A24 domain supports a prepilin-processing peptidase activity, though specific substrate context is unresolved.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id == "GO:0044877":
        return {
            "summary": "Protein-containing complex binding is plausible but not the most informative description of an ancillary SecYEG translocon subunit.",
            "action": "KEEP_AS_NON_CORE",
            "reason": "The product/domain evidence supports Sec-translocon accessory context; complex binding is retained as non-core molecular-function context.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:0015562", "GO:0022857"}:
        return {
            "summary": "Direct efflux/transporter activity is likely over-specific for a membrane-fusion protein component.",
            "action": "MARK_AS_OVER_ANNOTATED",
            "reason": "HlyD-family membrane-fusion proteins bridge tripartite secretion/efflux assemblies but are not by themselves the substrate-translocating membrane transporter.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    if go_id in {"GO:1990281", "GO:0055085"}:
        return {
            "summary": "Efflux-pump complex or broad transport context is consistent with the HlyD/MFP family, but substrate and partner components remain unresolved.",
            "action": "ACCEPT",
            "reason": "The protein is best treated as a candidate membrane-fusion component in broad transport or efflux-complex context until its cognate transporter/channel system is identified.",
            "supported_by": support_lines(info, *core_keys(info)),
        }
    raise ValueError(f"Unhandled annotation {info['gene']} {go_id} {label}")


def new_annotation(info: dict[str, object], go_id: str, qualifier: str) -> dict[str, object]:
    return {
        "term": term(go_id),
        "evidence_type": "IEA",
        "original_reference_id": ref_file(info["gene"], "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": f"Adds {TERMS[go_id]} as a conservative core term absent from the fetched GOA rows.",
            "action": "NEW",
            "reason": "The product and domain metadata support this boundary-level function/process assignment in the first-pass review.",
            "supported_by": support_lines(info, *core_keys(info)),
        },
    }


def add_missing_new_annotations(info: dict[str, object], annotations: list[dict[str, object]]) -> None:
    present = {ann["term"]["id"] for ann in annotations}
    if info["category"] == "bam" and info["gene"] == "bamB" and "GO:1990063" not in present:
        annotations.append(new_annotation(info, "GO:1990063", "part_of"))
    if info["category"] == "sec_accessory" and "GO:0043952" not in present:
        annotations.append(new_annotation(info, "GO:0043952", "involved_in"))
    if info["category"] == "bam_like" and "GO:0043165" not in present:
        annotations.append(new_annotation(info, "GO:0043165", "involved_in"))
    if info["category"] == "mfp_candidate":
        if "GO:0016020" not in present and "GO:0030313" not in present:
            annotations.append(new_annotation(info, "GO:0016020", "located_in"))
            present.add("GO:0016020")
        if "GO:0055085" not in present:
            annotations.append(new_annotation(info, "GO:0055085", "involved_in"))
            present.add("GO:0055085")
        if "GO:1990281" not in present:
            annotations.append(new_annotation(info, "GO:1990281", "part_of"))


def core_functions(info: dict[str, object], annotations: list[dict[str, object]]) -> list[dict[str, object]]:
    category = info["category"]
    base = {"description": "", "supported_by": support_lines(info, *core_keys(info))}
    if category == "bam":
        cf = {
            **base,
            "description": "Bam-family outer-membrane assembly factor contributing to beta-barrel outer-membrane protein assembly and insertion.",
            "directly_involved_in": [term("GO:0043165"), term("GO:0051205")],
            "locations": [term("GO:0009279")],
            "in_complex": term("GO:1990063"),
        }
        return [cf]
    if category == "bam_like":
        return [
            {
                **base,
                "description": "BamE-domain outer-membrane protein assembly factor candidate.",
                "directly_involved_in": [term("GO:0043165")],
                "locations": [term("GO:0019867")],
            }
        ]
    if category == "lol":
        loc = "GO:0030288" if info["gene"] == "lolA" else "GO:0009279"
        return [
            {
                **base,
                "description": "Lol-pathway factor for localization of mature lipoproteins to the outer membrane.",
                "directly_involved_in": [term("GO:0044874")],
                "locations": [term(loc)],
            }
        ]
    if category == "type_ii":
        return [
            {
                **base,
                "description": "GspH-family type-II secretion-system component.",
                "directly_involved_in": [term("GO:0015628")],
                "locations": [term("GO:0005886")],
                "in_complex": term("GO:0015627"),
            }
        ]
    if category == "type_v":
        return [
            {
                **base,
                "description": "Two-partner/type V secretion outer-membrane transporter candidate.",
                "molecular_function": term("GO:0008320"),
                "directly_involved_in": [term("GO:0046819")],
                "in_complex": term("GO:0098046"),
            }
        ]
    if category == "prepilin_peptidase":
        return [
            {
                **base,
                "description": "Membrane prepilin/type IV endopeptidase-domain peptidase candidate.",
                "molecular_function": term("GO:0004190"),
                "locations": [term("GO:0016020")],
            }
        ]
    if category == "sec_accessory":
        return [
            {
                **base,
                "description": "Ancillary SecYEG translocon subunit candidate contributing to Sec-dependent protein transport.",
                "directly_involved_in": [term("GO:0043952")],
                "locations": [term("GO:0005886")],
            }
        ]
    if category == "mfp_candidate":
        loc_id = "GO:0030313" if "GO:0030313" in info.get("go_ids", []) else "GO:0016020"
        return [
            {
                **base,
                "description": "HlyD-family membrane-fusion protein candidate associated with an unresolved efflux or secretion pump complex.",
                "directly_involved_in": [term("GO:0055085")],
                "locations": [term(loc_id)],
                "in_complex": term("GO:1990281"),
            }
        ]
    return []


def references_for(info: dict[str, object], annotations: list[dict[str, object]]) -> list[dict[str, object]]:
    refs: list[dict[str, object]] = []
    for ref_id in sorted({ann.get("original_reference_id") for ann in annotations if ann.get("original_reference_id")}):
        if ref_id.startswith("file:"):
            continue
        refs.append({"id": ref_id, "title": GO_REF_TITLES.get(ref_id, ref_id), "findings": []})
    lines = info["line_by_key"]
    uniprot_lines = [
        lines["de"],
        lines.get("location_outer"),
        lines.get("location_inner"),
        lines.get("location_cell"),
        lines.get("location_membrane"),
        lines.get("location_periplasm"),
        lines.get("location_envelope"),
        lines.get("function"),
        lines.get("family"),
        lines.get("bamA_domain"),
        lines.get("bamB_domain"),
        lines.get("bamD_domain"),
        lines.get("bamE_domain"),
        lines.get("lolA_domain"),
        lines.get("lolB_domain"),
        lines.get("t2ss_domain"),
        lines.get("tps_domain"),
        lines.get("prepilin_domain"),
        lines.get("sec_domain"),
        lines.get("mfp_domain"),
        lines.get("rnd_mfp_domain"),
    ]
    refs.append(
        {
            "id": ref_file(info["gene"], "uniprot.txt"),
            "title": f"UniProtKB entry for {info['gene']}",
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
        ann["review"] = review_for_annotation(info, ann["term"]["id"], ann["term"]["label"])
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
            "core_functions": core_functions(info, annotations),
            "proposed_new_terms": [],
            "suggested_questions": [
                {
                    "question": "What are the cognate partner proteins and substrates for this envelope export, secretion, or assembly factor in KT2440?"
                }
            ],
            "suggested_experiments": [
                {
                    "description": "Combine deletion or depletion with envelope-protein, lipoprotein-localization, secretion, or efflux assays matched to the predicted system context.",
                    "experiment_type": "envelope transport genetics",
                }
            ],
        }
    )
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def annoton(info: dict[str, object]) -> dict[str, object]:
    gene = info["gene"]
    cores = core_functions(info, [])
    entry: dict[str, object] = {
        "id": f"{gene}_export_secretion_assembly_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {info['product']}",
    }
    if cores:
        core = cores[0]
        if "molecular_function" in core:
            entry["function"] = {"preferred_term": core["molecular_function"]["label"], "term": core["molecular_function"]}
        if "directly_involved_in" in core:
            entry["processes"] = [{"preferred_term": p["label"], "term": p} for p in core["directly_involved_in"]]
        if "locations" in core:
            entry["locations"] = [{"preferred_term": loc["label"], "term": loc} for loc in core["locations"]]
    elif info["category"] == "mfp_candidate":
        entry["processes"] = [{"preferred_term": "transmembrane transport", "term": term("GO:0055085")}]
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
        "id": "MODULE:protein_export_secretion_outer_membrane_assembly_boundary",
        "title": "Protein export, secretion, and outer-membrane assembly boundary",
        "description": (
            "Boundary module for the transport/membrane/efflux split covering BAM outer-membrane protein assembly, "
            "LolA/LolB lipoprotein localization, type-II/type-V secretion side components, an ancillary SecYEG "
            "translocon subunit, prepilin peptidase context, and unresolved HlyD-family membrane-fusion proteins."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK transport/membrane/efflux protein export/secretion/outer-membrane assembly batch",
                "statement": "The partition groups 15 envelope export, secretion, BAM, Lol, SecYEG-accessory, and HlyD-family candidates that should not be forced into generic membrane-protein spillovers.",
            }
        ],
        "module": {
            "id": "protein_export_secretion_outer_membrane_assembly_boundary",
            "label": "Protein export, secretion, and outer-membrane assembly boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                concept("GO:0043165", "Outer-membrane protein assembly by Gram-negative BAM-associated proteins."),
                concept("GO:0051205", "Protein insertion into membranes, especially beta-barrel outer-membrane proteins."),
                concept("GO:1990063", "Bam protein complex context for BamA/B/D/E factors."),
                concept("GO:0044874", "Lol-mediated localization of mature lipoproteins to the outer membrane."),
                concept("GO:0042953", "Lipoprotein transport through the Lol pathway."),
                concept("GO:0043952", "Sec-complex protein transport context for ancillary SecYEG-associated proteins."),
                concept("GO:0015628", "Type-II secretion process for GspH-like pseudopilin components."),
                concept("GO:0015627", "Type-II secretion system complex context."),
                concept("GO:0046819", "Type-V/two-partner secretion process."),
                concept("GO:0098046", "Type-V protein secretion system complex context."),
                concept("GO:0004190", "Prepilin/type IV endopeptidase-domain peptidase activity."),
                concept("GO:1990281", "Efflux pump complex context for HlyD/MFP candidates."),
                concept("GO:0055085", "Broad transport process retained for unresolved HlyD/MFP candidates."),
            ],
            "context": {
                "cellular_components": [
                    {"preferred_term": "cell outer membrane", "term": term("GO:0009279"), "description": "Bam, LolB, and type-V outer-membrane transporter context."},
                    {"preferred_term": "plasma membrane", "term": term("GO:0005886"), "description": "Bacterial inner-membrane Sec and type-II secretion component context."},
                    {"preferred_term": "outer membrane-bounded periplasmic space", "term": term("GO:0030288"), "description": "Periplasmic LolA lipoprotein-carrier context."},
                    {"preferred_term": "cell envelope", "term": term("GO:0030313"), "description": "Broad envelope context for HlyD-family membrane-fusion proteins."},
                ]
            },
            "parts": [
                part(1, "BAM outer-membrane protein assembly", "bam_outer_membrane_assembly", "BAM outer-membrane protein assembly factors", "BamA/B/D/E-family proteins and BamE-domain candidate context.", by_category.get("bam", []) + by_category.get("bam_like", [])),
                part(2, "LolA/LolB lipoprotein localization", "lola_lolb_lipoprotein_localization", "LolA/LolB lipoprotein localization", "Periplasmic LolA carrier and outer-membrane LolB acceptor context.", by_category.get("lol", [])),
                part(3, "Sec/type-II/type-V/prepilin export and secretion side components", "protein_export_secretion_side_components", "Protein export and secretion side components", "Ancillary SecYEG, GspH, ShlB/TpsB, and prepilin-peptidase candidates.", by_category.get("sec_accessory", []) + by_category.get("type_ii", []) + by_category.get("type_v", []) + by_category.get("prepilin_peptidase", [])),
                part(4, "HlyD-family membrane-fusion candidates", "hlyd_mfp_candidate_context", "HlyD-family membrane-fusion candidates", "MFP/HlyD-family candidates with unresolved transporter partners and substrates.", by_category.get("mfp_candidate", [])),
            ],
        },
        "notes": (
            "The module is intentionally a boundary/spillover module. It preserves compact system context for BAM, Lol, "
            "Sec/type-II/type-V secretion, and HlyD/MFP candidates while leaving cognate partners and substrates unresolved."
        ),
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
