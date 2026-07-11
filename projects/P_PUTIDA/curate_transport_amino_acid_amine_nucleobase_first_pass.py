#!/usr/bin/env python3
"""First-pass curation for non-ABC amino-acid, amine, and nucleobase transporters."""

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
    "module_transport_membrane_efflux_amino_acid_quaternary_amine_nucleobase_transporters.tsv"
)
MODULE_PATH = ROOT / "modules/amino_acid_amine_nucleobase_transport_boundary.yaml"

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on inter-ontology links",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERMS = {
    "GO:0015220": "choline transmembrane transporter activity",
    "GO:0015847": "putrescine transport",
    "GO:0015871": "choline transport",
    "GO:0034228": "ethanolamine transmembrane transporter activity",
    "GO:0034229": "ethanolamine transport",
    "GO:0070778": "L-aspartate transmembrane transport",
}

PROFILES = {
    "gltP": ("GltP acidic-amino-acid proton symporter", "GO:0005280", ["GO:0003333", "GO:0006835", "GO:1902600"], ["GO:0005886"]),
    "PP_0198": ("Rht/LysE homoserine exporter candidates", "GO:0042970", ["GO:0042968"], ["GO:0005886"]),
    "betT-II": ("BCCT choline/betaine/carnitine transporters", "GO:0015220", ["GO:0015871"], ["GO:0005886"]),
    "gabP-I": ("GabP-family GABA permeases", "GO:0015185", ["GO:0015812"], ["GO:0016020"]),
    "PP_0544": ("Ethanolamine APC-family transporter", "GO:0034228", ["GO:0034229"], ["GO:0005886"]),
    "mmuP": ("APC amino-acid and amine permease candidates", "GO:0015171", ["GO:0006865"], ["GO:0016020"]),
    "PP_0699": ("Broad LysE/Rht-family amino-acid exporters", "GO:0015171", ["GO:0003333"], ["GO:0005886"]),
    "uraA": ("NCS nucleobase permeases", "GO:0015205", ["GO:0015851"], ["GO:0005886"]),
    "PP_0916": ("Broad LysE/Rht-family amino-acid exporters", "GO:0015171", ["GO:0003333"], ["GO:0005886"]),
    "aroP-I": ("APC amino-acid and amine permease candidates", "GO:0015171", ["GO:0006865"], ["GO:0005886"]),
    "PP_1060": ("Transport-bucket enzyme side nodes", "GO:0015930", ["GO:0097054"], []),
    "puuP": ("APC amino-acid and amine permease candidates", "GO:0022857", ["GO:0015847"], ["GO:0016020"]),
    "PP_1248": ("Rht/LysE substrate-specific amino-acid exporters", "GO:0015190", ["GO:0015820", "GO:1902475"], ["GO:0005886"]),
    "yveA": ("Aspartate-proton and AGT-like symporters", "GO:0005280", ["GO:0070778"], ["GO:0016020"]),
    "PP_2106": ("Ammonium and urea channel transporters", "GO:0008519", ["GO:0072488", "GO:0097272"], ["GO:0016020"]),
    "PP_2171": ("Broad LysE/Rht-family amino-acid exporters", "GO:0015171", ["GO:0003333"], ["GO:0005886"]),
    "azlC": ("Branched-chain amino-acid transporters", "GO:0015658", ["GO:1903785"], ["GO:0005886"]),
    "PP_2388": ("Broad LysE/Rht-family amino-acid exporters", "GO:0015171", ["GO:0003333"], ["GO:0005886"]),
    "PP_2429": ("Broad LysE/Rht-family amino-acid exporters", "GO:0015171", ["GO:0006865"], ["GO:0005886"]),
    "sstT": ("SstT serine/threonine sodium symporter", "GO:0005295", ["GO:0032329", "GO:0015826"], ["GO:0005886"]),
    "gabP-II": ("GabP-family GABA permeases", "GO:0015185", ["GO:0015812"], ["GO:0016020"]),
    "PP_2586": ("APC amino-acid and amine permease candidates", "GO:0015171", ["GO:0006865"], ["GO:0016020"]),
    "PP_2692": ("BCCT choline/betaine/carnitine transporters", "GO:0015220", ["GO:0015871"], ["GO:0005886"]),
    "PP_2721": ("Low-confidence transporter-name-only records", None, [], []),
    "PP_2802": ("APC amino-acid and amine permease candidates", "GO:0015171", ["GO:0006865"], ["GO:0016020"]),
    "gabP-III": ("GabP-family GABA permeases", "GO:0015185", ["GO:0015812"], ["GO:0016020"]),
    "PP_3021": ("Broad LysE/Rht-family amino-acid exporters", "GO:0015171", ["GO:0003333"], ["GO:0005886"]),
    "PP_3025": ("Broad LysE/Rht-family amino-acid exporters", "GO:0015171", ["GO:0003333"], ["GO:0005886"]),
    "PP_3405": ("Broad LysE/Rht-family amino-acid exporters", "GO:0015171", ["GO:0006865"], ["GO:0005886"]),
    "PP_3438": ("Broad LysE/Rht-family amino-acid exporters", "GO:0015171", ["GO:0006865"], ["GO:0005886"]),
    "PP_3565": ("Rht/LysE homoserine exporter candidates", "GO:0042970", ["GO:0042968"], ["GO:0005886"]),
    "PP_3625": ("Rht/LysE homoserine exporter candidates", "GO:0042970", ["GO:0042968"], ["GO:0005886"]),
    "PP_3628": ("BCCT choline/betaine/carnitine transporters", "GO:0015220", ["GO:0015871"], ["GO:0005886"]),
    "PP_3652": ("Broad LysE/Rht-family amino-acid exporters", "GO:0015171", ["GO:0003333"], ["GO:0005886"]),
    "PP_3653": ("Broad LysE/Rht-family amino-acid exporters", "GO:0015171", ["GO:0003333"], ["GO:0005886"]),
    "rocE": ("APC amino-acid and amine permease candidates", "GO:0015171", ["GO:0006865"], ["GO:0016020"]),
    "betT-III": ("BCCT choline/betaine/carnitine transporters", "GO:0015220", ["GO:0015871"], ["GO:0005886"]),
    "xanP": ("NCS xanthine/uracil-family permeases", "GO:0042907", ["GO:0042906"], ["GO:0005886"]),
    "gabP-IV": ("GabP-family GABA permeases", "GO:0015185", ["GO:0015812"], ["GO:0016020"]),
    "brnQ": ("Branched-chain amino-acid transporters", "GO:0015658", ["GO:0015803"], ["GO:0005886"]),
    "PP_4226": ("Transport-bucket enzyme side nodes", None, [], []),
    "PP_4284": ("NCS adenine/purine permeases", "GO:0015207", ["GO:0015853", "GO:1904823"], ["GO:0005886"]),
    "uacT": ("NCS nucleobase permeases", "GO:0015205", ["GO:0015851"], ["GO:0005886"]),
    "PP_4302": ("Ammonium and urea channel transporters", "GO:0015204", ["GO:0071918"], ["GO:0005886"]),
    "PP_4407": ("GabP-family GABA permeases", "GO:0015185", ["GO:0015812"], ["GO:0016020"]),
    "aroP-II": ("APC amino-acid and amine permease candidates", "GO:0015171", ["GO:0006865"], ["GO:0005886"]),
    "PP_4643": ("NCS xanthine/uracil-family permeases", "GO:0042907", ["GO:0042906"], ["GO:0005886"]),
    "purP": ("NCS adenine/purine permeases", "GO:0015207", ["GO:0015853", "GO:1904823"], ["GO:0005886"]),
    "gabP-V": ("GabP-family GABA permeases", "GO:0015185", ["GO:0015812"], ["GO:0016020"]),
    "cycA": ("APC amino-acid and amine permease candidates", "GO:0015171", ["GO:0006865"], ["GO:0005886"]),
    "hutT": ("HutT histidine transporter", "GO:0005291", ["GO:1902024"], ["GO:0005886"]),
    "betT-I": ("BCCT choline/betaine/carnitine transporters", "GO:0015220", ["GO:0015871"], ["GO:0005886"]),
    "amtB": ("Ammonium and urea channel transporters", "GO:0008519", ["GO:0072488"], ["GO:0005886"]),
    "PP_5297": ("APC amino-acid and amine permease candidates", "GO:0015171", ["GO:0006865"], ["GO:0005886"]),
    "PP_5374": ("BCCT choline/betaine/carnitine transporters", "GO:0015220", ["GO:0015871"], ["GO:0005886"]),
}

DESCRIPTIONS = {
    "PP_2721": "PP_2721 is a low-confidence amino-acid-transporter-name-only membrane candidate without GOA rows or supporting UniProt domains; first-pass curation leaves its molecular function unresolved.",
    "PP_4226": "PP_4226 encodes a Tre1-like/DUF6861 N-terminal-domain protein pulled into the transport bucket by naming or membrane context; it is not curated as a transporter in this first pass.",
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


def goa_term_ids(gene: str) -> set[str]:
    path = GENE_ROOT / gene / f"{gene}-goa.tsv"
    with path.open() as handle:
        return {row["GO TERM"] for row in csv.DictReader(handle, delimiter="\t")}


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
    extra_support: list[dict[str, str]] | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": dedupe((extra_support or []) + base_support(info)),
    }
    if replacement_ids:
        item["proposed_replacement_terms"] = [term(go_id) for go_id in replacement_ids]
    return item


def existing_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]
    primary = info.get("primary")
    processes = set(info["processes"])
    gene = info["gene"]

    if go_id == "GO:0005886":
        return review(info, "Plasma membrane localization is appropriate for this bacterial transporter or membrane enzyme.", "ACCEPT", "The UniProt/GOA membrane context supports plasma/inner membrane localization.")
    if go_id == "GO:0016020":
        if "GO:0005886" in info["go_ids"]:
            return review(info, "Generic membrane localization is true but less informative than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "A more specific plasma-membrane annotation is present.")
        return review(info, "Membrane localization is appropriate for this membrane-associated protein.", "ACCEPT", "UniProt/GOA membrane context supports this localization.")
    if gene == "gltP" and go_id in {"GO:0000976", "GO:0001216", "GO:0032993", "GO:0045893"}:
        return review(
            info,
            f"{label} is a promoter/regulator annotation misassigned to the GltP transporter protein.",
            "REMOVE",
            "The cached abstract attributes promoter binding and transcriptional activation to the AauR response regulator; GltP is listed as an AauR-responsive transporter gene product, not as the DNA-binding protein.",
            extra_support=[
                support("PMID:18310026", "regulator AauR to the aat promoter"),
                support("PMID:18310026", "H(+)/Glu symporter GltP"),
            ],
        )
    if go_id in {"GO:0022857", "GO:0055085"}:
        if primary in {None, "GO:0022857"}:
            return review(info, f"{label} is appropriate broad transport context for this low-resolution transporter candidate.", "ACCEPT", "The product/domain evidence supports a transporter but not a more specific substrate-resolved term.")
        return review(info, f"{label} is true but broad relative to the substrate/family-specific transporter call.", "MARK_AS_OVER_ANNOTATED", "A more informative transporter term is available for the core function.", [primary])
    if go_id in {"GO:0006865", "GO:0003333"}:
        if primary == "GO:0015171":
            return review(info, f"{label} is appropriate broad amino-acid transport context.", "ACCEPT", "The product/domain evidence supports amino-acid permease or exporter context while substrate is unresolved.")
        return review(info, f"{label} is retained as broad context for a more specific transporter.", "KEEP_AS_NON_CORE", "The substrate-specific transporter/process term is the clearer core annotation.")
    if go_id == "GO:0015171":
        if primary == go_id:
            return review(info, "Amino acid transmembrane transporter activity is the appropriate conservative molecular function.", "ACCEPT", "The product/domain evidence supports amino-acid transport while exact substrate is unresolved.")
        return review(info, "Amino acid transmembrane transporter activity is true but broad.", "KEEP_AS_NON_CORE", "A substrate-specific transporter term is available for the core function.", [primary] if primary else None)
    if go_id == "GO:0015293":
        return review(info, "Symporter activity is retained as coupling context.", "KEEP_AS_NON_CORE", "The substrate-specific transporter activity and process are more informative core calls.")
    if go_id == "GO:0005280":
        return review(info, "Amino acid:proton symporter activity is appropriate for this acidic-amino-acid proton symporter.", "ACCEPT", "The GltP/YveA-family product and domains support proton-coupled amino-acid symport.")
    if go_id in {"GO:0006835", "GO:1902600", "GO:0070778"}:
        return review(info, f"{label} is appropriate process context for proton-coupled acidic-amino-acid transport.", "ACCEPT", "The product/domain assignment supports acidic amino acid or proton-coupled transmembrane transport.")
    if go_id in {"GO:0015185", "GO:0015812"}:
        return review(info, f"{label} is appropriate for the GabP-family GABA permease.", "ACCEPT", "The GabP product/domain evidence supports gamma-aminobutyrate transport.")
    if go_id in {"GO:0042968", "GO:0042970"}:
        return review(info, f"{label} is appropriate for the Rht/LysE-family homoserine exporter candidate.", "ACCEPT", "The Rht/LysE-family product and GOA support homoserine transport.")
    if go_id in {"GO:0015190", "GO:0015820", "GO:1902475"}:
        return review(info, f"{label} is appropriate substrate-specific amino-acid transport context.", "ACCEPT", "The LysE/Rht or branched-chain transporter evidence supports this amino-acid transport assignment.")
    if go_id == "GO:0033228":
        return review(info, "L-cysteine export is too substrate-specific for these low-resolution LysE-family records.", "MODIFY", "The products and domains support broad LysE/Rht-family amino-acid export, but not cysteine specificity in this first pass.", ["GO:0015171"])
    if go_id in {"GO:0005295", "GO:0015826", "GO:0032329"}:
        return review(info, f"{label} is appropriate for SstT.", "ACCEPT", "The reviewed/HAMAP SstT serine/threonine sodium-symporter assignment supports this term.")
    if go_id in {"GO:0005291", "GO:1902024"}:
        return review(info, f"{label} is appropriate for HutT.", "ACCEPT", "The UniProt HutT record and cached literature-supported entry identify an L-histidine transporter.")
    if go_id in {"GO:0015205", "GO:0015851"}:
        return review(info, f"{label} is appropriate broad NCS-family nucleobase transport context.", "ACCEPT", "The NCS2/xanthine-uracil/adenine family evidence supports nucleobase transport.")
    if go_id in {"GO:0042906", "GO:0042907"}:
        if gene == "uacT":
            return review(info, f"{label} is plausible family context but more specific than the UacT product line supports.", "MODIFY", "The product says uric acid permease; without a uric-acid-specific GO term in the local cache, broad nucleobase transport is safer.", ["GO:0015205"])
        return review(info, f"{label} is appropriate for xanthine/uracil-family permeases.", "ACCEPT", "The NCS2/UacT-like/xanthine-uracil permease domains support this substrate family.")
    if go_id in {"GO:0005345", "GO:0015207", "GO:0015853", "GO:1904823"}:
        return review(info, f"{label} is appropriate for Azg-like adenine/purine permeases.", "ACCEPT", "The Azg-like/NCS2 domains and adenine:H+ symporter product context support purine/adenine transport.")
    if go_id in {"GO:0005304", "GO:0015188", "GO:0015658", "GO:0015803", "GO:0015818", "GO:0015829", "GO:1903785"}:
        return review(info, f"{label} is appropriate branched-chain amino-acid transport context.", "ACCEPT", "The BrnQ/AzlC product and family/domain evidence support branched-chain amino-acid transport.")
    if go_id in {"GO:0008519", "GO:0072488", "GO:0097272"}:
        return review(info, f"{label} is appropriate ammonium transporter/channel context.", "ACCEPT", "The Amt/Rh family and ammonium-transporter domains support ammonium transport.")
    if go_id in {"GO:0015204", "GO:0071918"}:
        return review(info, f"{label} is appropriate for the urea transporter.", "ACCEPT", "The urea transporter product and UT domain support urea transport.")
    if go_id in {"GO:0034228", "GO:0034229"}:
        return review(info, f"{label} is appropriate for the ethanolamine transporter.", "ACCEPT", "The ethanolamine transporter product and EtNH/APC domains support ethanolamine transport.")
    if go_id in {"GO:0015220", "GO:0015871"}:
        return review(info, f"{label} is appropriate first-pass BCCT transporter context.", "ACCEPT", "The BCCT family and choline/carnitine/betaine product lines support choline-compatible-solute transport context.")
    if go_id == "GO:0015847":
        return review(info, "Putrescine transport is appropriate process context for PuuP.", "ACCEPT", "The PuuP product supports putrescine permease function.")
    if go_id == "GO:0015930":
        return review(info, "Glutamate synthase activity is the core PP_1060 enzyme function.", "ACCEPT", "The GltB/glutamate synthase domains support enzyme rather than transporter function.")
    if go_id == "GO:0016638":
        return review(info, "This oxidoreductase term is retained as broader enzyme context for glutamate synthase.", "KEEP_AS_NON_CORE", "The more specific glutamate synthase activity captures the core function.")
    if go_id == "GO:0097054":
        return review(info, "L-glutamate biosynthetic process is appropriate process context for glutamate synthase.", "ACCEPT", "Glutamate synthase activity directly supports glutamate biosynthesis.")

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
        out.append(new_annotation(info, primary, "enables", f"Adds {TERMS[primary]} for this transporter/enzyme profile.", "Product, domain, and Asta context support this conservative first-pass core term."))
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
    gene = info["gene"]
    if gene in DESCRIPTIONS:
        return DESCRIPTIONS[gene]
    primary = info.get("primary")
    if primary:
        return f"{gene} encodes {info['product']}, curated in the {info['group']} subgroup with core {TERMS[primary]} context."
    return f"{gene} encodes {info['product']}, retained as unresolved side context in the amino-acid/amine/nucleobase transport bucket."


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
    goa_annotations = [
        ann
        for ann in doc.get("existing_annotations", [])
        if ann["term"]["id"] in goa_ids
    ]
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
    doc["suggested_questions"] = [{"question": "What are the exact substrate, direction, and ion coupling mechanism for this transporter in KT2440?"}]
    doc["suggested_experiments"] = [
        {
            "description": "Measure substrate uptake or export in knockout/complement strains and heterologous expression systems, testing candidate amino acids, amines, compatible solutes, nucleobases, ammonium, or urea as appropriate with ion-coupling controls.",
            "experiment_type": "transport genetics and substrate uptake/efflux assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_amino_acid_amine_nucleobase_context",
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
                    "description": f"First-pass amino-acid/amine/nucleobase transport subgroup: {group}.",
                    "annotons": [module_annoton(info) for info in group_infos],
                },
            }
        )
    concept_ids = [
        "GO:0005280",
        "GO:0015171",
        "GO:0015185",
        "GO:0005295",
        "GO:0005291",
        "GO:0015220",
        "GO:0015205",
        "GO:0015207",
        "GO:0042907",
        "GO:0008519",
        "GO:0015204",
        "GO:0015658",
        "GO:0015930",
        "GO:0005886",
        "GO:0016020",
    ]
    doc = {
        "id": "MODULE:amino_acid_amine_nucleobase_transport_boundary",
        "title": "Amino-acid, amine, and nucleobase transport boundary",
        "description": (
            "Boundary module for non-ABC PSEPK amino-acid, amine, compatible-solute, nucleobase, ammonium, and urea "
            "transporters plus enzyme/name-only side nodes pulled into the transport/membrane/efflux split."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK amino-acid/quaternary-amine/nucleobase transporter batch",
                "statement": "The batch table records 55 PSEPK transport-bucket genes assigned to non-ABC amino-acid, amine, compatible-solute, nucleobase, ammonium, and urea transporter context.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_partition.tsv",
                "title": "PSEPK transport/membrane/efflux partition",
                "statement": "The parent transport partition separates this non-ABC nitrogenous-solute transporter panel from ABC transporters, MFS/DMT, ion/metal, redox, and low-information membrane buckets.",
            },
        ],
        "notes": (
            "First-pass interpretation: keep substrate-specific calls where product/family/GOA agree, use broad amino-acid or nucleobase transporter terms for low-resolution paralogs, and keep PP_1060 and PP_4226 as side nodes rather than transporters."
        ),
        "module": {
            "id": "amino_acid_amine_nucleobase_transport_boundary",
            "label": "Amino-acid, amine, and nucleobase transport boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [descriptor(go_id, "Concept used for first-pass amino-acid/amine/nucleobase transporter curation.") for go_id in concept_ids],
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
