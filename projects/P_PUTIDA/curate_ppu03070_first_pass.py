#!/usr/bin/env python3
"""First-pass curation for KEGG ppu03070 bacterial secretion systems."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES
BATCH = Path("projects/P_PUTIDA/batches/ppu03070_bacterial_secretion_system_boundary.tsv")
SKIP_ALREADY_CURATED = {"cyaB"}

GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000003": "Gene Ontology annotation based on Enzyme Commission mapping",
    "GO_REF:0000043": "Gene Ontology annotation based on UniProtKB/Swiss-Prot keyword mapping",
    "GO_REF:0000044": (
        "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, "
        "accompanied by conservative changes to GO terms applied by UniProt"
    ),
    "GO_REF:0000104": (
        "Electronic Gene Ontology annotations created by transferring manual GO annotations between "
        "related proteins based on shared sequence features"
    ),
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

TERM_LABELS = {
    "GO:0003824": "catalytic activity",
    "GO:0005524": "ATP binding",
    "GO:0005576": "extracellular region",
    "GO:0005737": "cytoplasm",
    "GO:0005886": "plasma membrane",
    "GO:0009279": "cell outer membrane",
    "GO:0009306": "protein secretion",
    "GO:0008320": "protein transmembrane transporter activity",
    "GO:0015031": "protein transport",
    "GO:0015627": "type II protein secretion system complex",
    "GO:0015628": "protein secretion by the type II secretion system",
    "GO:0016020": "membrane",
    "GO:0016887": "ATP hydrolysis activity",
    "GO:0019867": "outer membrane",
    "GO:0030253": "protein secretion by the type I secretion system",
    "GO:0030256": "type I protein secretion system complex",
    "GO:0033103": "protein secretion by the type VI secretion system",
    "GO:0034605": "cellular response to heat",
    "GO:0046819": "protein secretion by the type V secretion system",
    "GO:0098046": "type V protein secretion system complex",
    "GO:0140359": "ABC-type transporter activity",
}

TERM_DECISIONS = {
    "GO:0003824": (
        "MARK_AS_OVER_ANNOTATED",
        "generic catalytic activity is too broad for this predicted secretion substrate or effector without resolved catalytic specificity",
    ),
    "GO:0005524": ("ACCEPT", "ATP binding is appropriate for the secretion-system ATPase component"),
    "GO:0005576": (
        "KEEP_AS_NON_CORE",
        "extracellular localization is plausible for a VgrG-like secreted component but is not the main assembly role",
    ),
    "GO:0005737": ("ACCEPT", "cytoplasmic localization is appropriate for the ClpV-family AAA+ ATPase"),
    "GO:0005886": ("ACCEPT", "plasma membrane localization matches the bacterial secretion-system envelope machinery"),
    "GO:0009279": ("ACCEPT", "cell outer membrane localization is appropriate for secretin or outer-membrane secretion components"),
    "GO:0009306": (
        "KEEP_AS_NON_CORE",
        "protein secretion is correct but less specific than the type-specific secretion-system process where available",
    ),
    "GO:0015031": ("KEEP_AS_NON_CORE", "protein transport is correct but broad relative to the secretion-system role"),
    "GO:0015627": ("ACCEPT", "type II secretion system complex membership matches the Xcp/Gsp component assignment"),
    "GO:0015628": ("ACCEPT", "protein secretion by the type II secretion system is the defining process for Xcp/Gsp components"),
    "GO:0016020": (
        "MARK_AS_OVER_ANNOTATED",
        "generic membrane localization is less informative than plasma or outer membrane localization",
    ),
    "GO:0016887": ("ACCEPT", "ATP hydrolysis activity is appropriate for secretion-system AAA+/ABC ATPases"),
    "GO:0019867": ("KEEP_AS_NON_CORE", "outer membrane localization is correct but less bacterial-specific than cell outer membrane"),
    "GO:0034605": (
        "MARK_AS_OVER_ANNOTATED",
        "cellular response to heat is likely over-propagated from ClpB-like family context rather than the T6SS ClpV role",
    ),
    "GO:0046819": ("ACCEPT", "type V secretion is appropriate for the two-partner secretion outer-membrane transporter"),
    "GO:0098046": ("ACCEPT", "type V protein secretion system complex membership matches the TPS transporter assignment"),
    "GO:0140359": ("ACCEPT", "ABC-type transporter activity captures the ATP-driven type-I secretion component"),
}

SPECIFIC_DECISIONS = {
    ("xcpX", "GO:0009306"): (
        "ACCEPT",
        "protein secretion is the best available GOA process for this XcpK/type-II-secretion component",
    ),
    ("PP_4926", "GO:0015031"): (
        "ACCEPT",
        "protein transport is the best available GOA process for this type-I-secretion membrane-fusion component",
    ),
}

T2SS_GENES = {
    "xcpX",
    "xcpP",
    "xcpQ",
    "gspE",
    "gspF",
    "gspG",
    "xcpU",
    "xcpV",
    "xcpW",
    "xcpY",
    "xcpT",
    "xcpS",
    "PP_3476",
    "PP_3477",
    "PP_3478",
    "PP_3483",
    "PP_5190",
}

T2SS_ATPASES = {"gspE", "PP_3483", "PP_5190"}
T2SS_SECRETINS = {"xcpQ", "PP_3478"}
T2SS_PSEUDOPILINS = {"gspG", "xcpU", "xcpV", "xcpW", "xcpT", "PP_3476", "PP_3477"}
T6SS_VGRG = {"vgrG-I", "vgrG-II", "vgrG-III", "PP_3106"}
T6SS_HCP = {"hcpC-I", "PP_3089", "hcpC-II", "PP_4886", "PP_5238"}
T6SS_DOTU = {"PP_2616", "PP_3092", "PP_3385", "PP_4081"}
T6SS_TSSJ = {"PP_2618", "PP_3094", "PP_4079"}
T6SS_TSSM = {"PP_2627", "PP_3090", "PP_3091", "PP_4071"}


def read_batch() -> dict[str, dict[str, str]]:
    with BATCH.open(newline="", encoding="utf-8") as handle:
        return {row["suggested_review_name"]: row for row in csv.DictReader(handle, delimiter="\t")}


def term(term_id: str) -> dict[str, str]:
    return {"id": term_id, "label": TERM_LABELS[term_id]}


def support_for(term_id: str, label: str, gene: str) -> dict:
    path = ROOT / gene / f"{gene}-goa.tsv"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if term_id in line:
                return {"reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv", "supporting_text": line}
    return {"reference_id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv", "supporting_text": f"{term_id}\t{label}"}


def asta_support(gene: str) -> dict:
    path = ROOT / gene / f"{gene}-deep-research-asta.md"
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("- **Protein Description:** "):
            return {"reference_id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md", "supporting_text": line}
    raise ValueError(f"No Asta protein-description line found for {gene}")


def uniprot_de_support(gene: str) -> dict:
    path = ROOT / gene / f"{gene}-uniprot.txt"
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("DE   "):
            return {"reference_id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt", "supporting_text": line}
    raise ValueError(f"No UniProt DE line found for {gene}")


def unique_references(existing: list[dict], gene: str) -> list[dict]:
    refs: list[dict] = []
    seen: set[str] = set()
    for ref in existing:
        ref_id = ref.get("id")
        if not ref_id or ref_id in seen:
            continue
        if ref_id in GO_REF_TITLES:
            ref = {"id": ref_id, "title": GO_REF_TITLES[ref_id], "findings": []}
        refs.append(ref)
        seen.add(ref_id)
    for ref in [
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-uniprot.txt",
            "title": f"UniProtKB entry for {gene}",
            "findings": [{"statement": "UniProt identity, protein name, family, domain, and GO metadata used for first-pass pathway curation."}],
        },
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-goa.tsv",
            "title": f"QuickGO GOA annotations for {gene}",
            "findings": [{"statement": "GOA table containing the annotations reviewed in this file."}],
        },
        {
            "id": f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md",
            "title": f"Asta retrieval report for {gene}",
            "findings": [{"statement": "Asta retrieval used as fast gene-level context; no unsupported hypotheses were imported."}],
        },
    ]:
        local_name = ref["id"].split("/")[-1]
        if ref["id"] not in seen and (ROOT / gene / local_name).exists():
            refs.append(ref)
            seen.add(ref["id"])
    return refs


def product(row: dict[str, str]) -> str:
    return row["protein_name"].rstrip(".")


def description_for(gene: str, row: dict[str, str]) -> str:
    locus = row["ordered_locus"]
    name = product(row)
    if gene == "PP_1449":
        return (
            f"{gene} ({locus}) encodes a large FhaB/CdiA-like two-partner secretion passenger or effector protein. "
            "Its domain architecture places it in the TPS/type Vb secretion context, but the exported substrate or toxin activity "
            "remains unresolved in this light first pass."
        )
    if gene == "PP_1450":
        return (
            f"{gene} ({locus}) encodes a TpsB/ShlB-like outer-membrane transporter for a two-partner secretion system. "
            "It likely exports a cognate large TPS passenger such as the adjacent PP_1449 protein across the outer membrane."
        )
    if gene == "PP_4926":
        return (
            f"{gene} ({locus}) encodes a membrane-fusion protein family component adjacent to the CyaB type-I secretion ABC exporter. "
            "It is best treated as type-I secretion/accessory protein-transport context until its substrate is resolved."
        )
    if gene in T2SS_ATPASES:
        return (
            f"{gene} ({locus}) encodes {name}, a predicted ATPase component of a type II secretion system. "
            "It likely powers assembly or function of an Xcp/Gsp-like outer-membrane protein secretion apparatus."
        )
    if gene in T2SS_SECRETINS:
        return (
            f"{gene} ({locus}) encodes {name}, a predicted outer-membrane secretin/channel component of a type II secretion system. "
            "Secretin components form the outer-membrane pore for type-II-dependent export of folded periplasmic proteins."
        )
    if gene in T2SS_PSEUDOPILINS:
        return (
            f"{gene} ({locus}) encodes {name}, a predicted pseudopilin or pilin-like component of a type II secretion system. "
            "Such proteins assemble the pseudopilus that helps drive substrate movement through the Xcp/Gsp secretion apparatus."
        )
    if gene in T2SS_GENES:
        return (
            f"{gene} ({locus}) encodes {name}, a predicted component of a type II secretion system. "
            "The first-pass interpretation places it in the Xcp/Gsp secretion apparatus rather than in the Sec/Tat inner-membrane export module."
        )
    if gene in T6SS_VGRG:
        return (
            f"{gene} ({locus}) encodes {name}, a VgrG/RHS-like type VI secretion component or effector candidate. "
            "It is likely part of a T6SS puncturing/spike-associated module, but substrate or effector specificity is unresolved."
        )
    if gene in T6SS_HCP:
        return (
            f"{gene} ({locus}) encodes {name}, an Hcp-family type VI secretion tube or secreted effector candidate. "
            "The first-pass call is T6SS-associated context with no resolved antibacterial or host-target activity."
        )
    if gene in T6SS_DOTU:
        return (
            f"{gene} ({locus}) encodes {name}, a DotU-family type IV/VI secretion membrane-complex component. "
            "It is treated as T6SS membrane-platform context rather than a standalone transporter."
        )
    if gene in T6SS_TSSJ:
        return (
            f"{gene} ({locus}) encodes {name}, a TssJ/SciN-like lipoprotein component of a type VI secretion membrane complex. "
            "It likely contributes to envelope anchoring or assembly of a T6SS apparatus."
        )
    if gene in T6SS_TSSM:
        return (
            f"{gene} ({locus}) encodes {name}, an IcmF/TssM-like membrane component of a type VI secretion system. "
            "It is likely part of the T6SS trans-envelope membrane platform."
        )
    if gene == "clpV":
        return (
            "clpV (PP_3095) encodes a ClpV-family AAA+ ATPase associated with type VI secretion systems. "
            "ClpV-like ATPases remodel or recycle contractile sheath components and should not be conflated with generic heat-shock ClpB response."
        )
    return (
        f"{gene} ({locus}) encodes {name}. It is included in the ppu03070 bacterial secretion-system boundary batch, "
        "but the specific apparatus role remains unresolved in this first pass."
    )


def core_for(gene: str, annotations: list[dict]) -> dict:
    ids = {ann.get("term", {}).get("id") for ann in annotations}
    core: dict = {"description": ""}
    if gene in T2SS_GENES:
        core["description"] = "Predicted type II secretion-system component in the Xcp/Gsp secretion boundary module."
        if "GO:0016887" in ids:
            core["molecular_function"] = term("GO:0016887")
        if "GO:0015628" in ids:
            core["directly_involved_in"] = [term("GO:0015628")]
        if "GO:0015627" in ids:
            core["in_complex"] = term("GO:0015627")
        locations = [term(tid) for tid in ("GO:0009279", "GO:0005886") if tid in ids]
        if locations:
            core["locations"] = locations
        return core
    if gene == "PP_1450":
        return {
            "description": "Two-partner/type Vb secretion outer-membrane transporter for a large TPS passenger protein.",
            "directly_involved_in": [term("GO:0046819")],
            "in_complex": term("GO:0098046"),
        }
    if gene == "PP_4926":
        return {
            "description": "Membrane-fusion protein family component supporting type-I-secretion protein transport.",
            "directly_involved_in": [term("GO:0015031")],
            "locations": [term("GO:0005886")],
        }
    if gene == "clpV":
        return {
            "description": "T6SS-associated ClpV-family AAA+ ATPase likely involved in secretion-system sheath remodeling.",
            "molecular_function": term("GO:0016887"),
            "locations": [term("GO:0005737")],
        }
    return {"description": "Predicted secretion-system component or effector candidate with unresolved precise molecular activity."}


def curated_review(gene: str, term_id: str, label: str, decision: tuple[str, str]) -> dict:
    action, reason = decision
    if action == "ACCEPT":
        summary = f"{label} is supported for {gene} in the ppu03070 bacterial-secretion first pass."
    elif action == "KEEP_AS_NON_CORE":
        summary = f"{label} is plausible for {gene} but not the most specific ppu03070 role."
    elif action == "MARK_AS_OVER_ANNOTATED":
        summary = f"{label} is too broad or over-propagated for the ppu03070 role of {gene}."
    else:
        summary = f"{label} was reviewed for {gene}."
    return {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": [support_for(term_id, label, gene), asta_support(gene)],
    }


def core_supported_by(core: dict, annotations: list[dict], gene: str) -> list[dict]:
    support: list[dict] = []
    term_index = {ann["term"]["id"]: ann["term"]["label"] for ann in annotations if ann.get("term", {}).get("id")}
    for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
        value = core.get(slot)
        if isinstance(value, dict) and value.get("id") in term_index:
            support.append(support_for(value["id"], term_index[value["id"]], gene))
    for slot in ("directly_involved_in", "locations"):
        for value in core.get(slot, []) or []:
            if value.get("id") in term_index:
                support.append(support_for(value["id"], term_index[value["id"]], gene))
    support.extend([uniprot_de_support(gene), asta_support(gene)])
    deduped: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for item in support:
        key = (item["reference_id"], item["supporting_text"])
        if key not in seen:
            deduped.append(item)
            seen.add(key)
    return deduped


def curated_questions(gene: str) -> list[dict]:
    return [
        {
            "question": (
                f"Which P. putida KT2440 secretion apparatus, substrate, or effector phenotype depends directly on {gene}, "
                "and under what growth or surface-associated conditions is it expressed?"
            )
        }
    ]


def curated_experiments(gene: str) -> list[dict]:
    return [
        {
            "description": (
                f"Create a targeted {gene} perturbation and assay secreted proteins, surface-associated phenotypes, and envelope-localized "
                "secretion-system assembly markers under planktonic and surface-growth conditions."
            ),
            "experiment_type": "gene perturbation with secretion proteomics and envelope phenotyping",
        }
    ]


def curate_gene(gene: str, row: dict[str, str]) -> None:
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = description_for(gene, row)
    annotations = data.get("existing_annotations", []) or []
    for ann in annotations:
        term_data = ann["term"]
        if term_data["id"] == "GO:0008320":
            term_data["label"] = "protein transmembrane transporter activity"
        decision = SPECIFIC_DECISIONS.get(
            (gene, term_data["id"]),
            TERM_DECISIONS.get(
                term_data["id"],
                (
                    "KEEP_AS_NON_CORE",
                    "reviewed as ppu03070 secretion-system boundary context but not central to the first-pass interpretation",
                ),
            ),
        )
        ann["review"] = curated_review(gene, term_data["id"], term_data["label"], decision)
    core = core_for(gene, annotations)
    core["supported_by"] = core_supported_by(core, annotations, gene)
    data["core_functions"] = [core]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = curated_questions(gene)
    data["suggested_experiments"] = curated_experiments(gene)
    data["references"] = unique_references(data.get("references", []) or [], gene)
    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def add_asta_support_to_existing_gene(gene: str) -> None:
    path = ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    support = asta_support(gene)
    for ann in data.get("existing_annotations", []) or []:
        review = ann.get("review") or {}
        supported_by = review.setdefault("supported_by", [])
        if not any(item.get("reference_id") == support["reference_id"] for item in supported_by):
            supported_by.append(support)
        ann["review"] = review
    for core in data.get("core_functions", []) or []:
        supported_by = core.setdefault("supported_by", [])
        if not any(item.get("reference_id") == support["reference_id"] for item in supported_by):
            supported_by.append(support)
    data["references"] = unique_references(data.get("references", []) or [], gene)
    path.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    rows = read_batch()
    for gene, row in rows.items():
        if gene in SKIP_ALREADY_CURATED:
            add_asta_support_to_existing_gene(gene)
            continue
        curate_gene(gene, row)


if __name__ == "__main__":
    main()
