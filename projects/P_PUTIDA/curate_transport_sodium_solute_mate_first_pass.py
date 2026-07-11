#!/usr/bin/env python3
"""First-pass curation for sodium-solute symporters, ArcD/ActP carriers, and MATE efflux proteins."""

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
    "module_transport_membrane_efflux_ion_metal_sodium_solute_symporters_and_mate_efflux.tsv"
)
MODULE_PATH = ROOT / "modules/sodium_solute_symporter_mate_boundary.yaml"

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
    "GO:0003333": "amino acid transmembrane transport",
    "GO:0005298": "proline:sodium symporter activity",
    "GO:0005283": "amino acid:sodium symporter activity",
    "GO:0005886": "plasma membrane",
    "GO:0006527": "L-arginine catabolic process",
    "GO:0006814": "sodium ion transport",
    "GO:0006847": "plasma membrane acetate transport",
    "GO:0006865": "amino acid transport",
    "GO:0015104": "antimonite transmembrane transporter activity",
    "GO:0015105": "arsenite transmembrane transporter activity",
    "GO:0015123": "acetate transmembrane transporter activity",
    "GO:0015184": "L-cystine transmembrane transporter activity",
    "GO:0015193": "L-proline transmembrane transporter activity",
    "GO:0015293": "symporter activity",
    "GO:0015297": "antiporter activity",
    "GO:0015501": "glutamate:sodium symporter activity",
    "GO:0015699": "antimonite transmembrane transport",
    "GO:0015700": "arsenite transport",
    "GO:0015811": "L-cystine transport",
    "GO:0015813": "L-glutamate transmembrane transport",
    "GO:0015824": "proline transport",
    "GO:0016020": "membrane",
    "GO:0022857": "transmembrane transporter activity",
    "GO:0031402": "sodium ion binding",
    "GO:0035524": "proline transmembrane transport",
    "GO:0035725": "sodium ion transmembrane transport",
    "GO:0042908": "xenobiotic transport",
    "GO:0042910": "xenobiotic transmembrane transporter activity",
    "GO:0043858": "arginine:ornithine antiporter activity",
    "GO:0046942": "carboxylic acid transport",
    "GO:0055085": "transmembrane transport",
    "GO:1903826": "L-arginine transmembrane transport",
    "GO:1905039": "carboxylic acid transmembrane transport",
}

PROFILE = {
    "PP_0496": {
        "class": "agcs",
        "group": "AGCS sodium-amino-acid symporters",
        "primary": "GO:0005283",
        "processes": ["GO:0003333", "GO:0035725"],
        "locations": ["GO:0005886"],
        "description": "PP_0496 encodes an AGCS-family membrane sodium/amino-acid symporter, curated at first pass as an amino acid:sodium symporter candidate.",
    },
    "PP_0569": {
        "class": "mate",
        "group": "MATE xenobiotic efflux antiporters",
        "primary": "GO:0042910",
        "processes": ["GO:0042908"],
        "locations": ["GO:0005886"],
        "description": "PP_0569 encodes a MATE-family membrane efflux protein, curated as a xenobiotic transmembrane transporter candidate with antiporter context.",
    },
    "PP_0670": {
        "class": "acr3",
        "group": "ACR3 arsenite/antimonite efflux outlier",
        "primary": "GO:0015105",
        "processes": ["GO:0015700", "GO:0015699"],
        "locations": ["GO:0005886"],
        "description": "PP_0670 encodes an ACR3-family arsenical-resistance membrane transporter; despite an older bile-acid/Na+ product string, family and GOA evidence support arsenite/antimonite transport.",
    },
    "gltS": {
        "class": "glts",
        "group": "Sodium-amino-acid symporters",
        "primary": "GO:0015501",
        "processes": ["GO:0015813"],
        "locations": ["GO:0005886"],
        "description": "gltS encodes a GltS/ESS-family sodium-dependent glutamate symporter in the bacterial inner membrane.",
    },
    "arcD-I": {
        "class": "arcd",
        "group": "ArcD arginine-ornithine antiporters",
        "primary": "GO:0043858",
        "processes": ["GO:1903826"],
        "locations": ["GO:0005886"],
        "description": "arcD-I encodes an APC-family arginine-ornithine antiporter associated with arginine transport and arginine-catabolism context.",
    },
    "arcD-II": {
        "class": "arcd",
        "group": "ArcD arginine-ornithine antiporters",
        "primary": "GO:0043858",
        "processes": ["GO:1903826"],
        "locations": ["GO:0005886"],
        "description": "arcD-II encodes an APC-family arginine-ornithine antiporter associated with arginine transport and arginine-catabolism context.",
    },
    "actP-I": {
        "class": "actp",
        "group": "ActP acetate symporters",
        "primary": "GO:0015123",
        "processes": ["GO:0006847"],
        "locations": ["GO:0005886"],
        "description": "actP-I encodes an SSF-family ActP cation/acetate symporter, curated as an acetate transmembrane transporter.",
    },
    "actP-II": {
        "class": "actp",
        "group": "ActP acetate symporters",
        "primary": "GO:0015123",
        "processes": ["GO:0006847"],
        "locations": ["GO:0005886"],
        "description": "actP-II encodes an SSF-family ActP cation/acetate symporter, curated as an acetate transmembrane transporter.",
    },
    "actP-III": {
        "class": "actp",
        "group": "ActP acetate symporters",
        "primary": "GO:0015123",
        "processes": ["GO:0006847"],
        "locations": ["GO:0005886"],
        "description": "actP-III encodes an SSF-family ActP cation/acetate symporter, curated as an acetate transmembrane transporter.",
    },
    "PP_3331": {
        "class": "low_proline",
        "group": "Low-confidence sodium-solute symporter candidates",
        "primary": "GO:0015293",
        "processes": [],
        "locations": ["GO:0016020"],
        "description": "PP_3331 encodes a PepSY-associated transmembrane protein with a low-confidence sodium:proline-symporter product line; first-pass curation keeps it as a membrane symporter candidate rather than a specific PutP ortholog.",
    },
    "PP_4524": {
        "class": "ssf_broad",
        "group": "Low-resolution sodium-solute symporters",
        "primary": "GO:0015293",
        "processes": ["GO:0055085"],
        "locations": ["GO:0005886"],
        "description": "PP_4524 encodes an SSF-family sodium-solute symporter candidate with unresolved transported solute.",
    },
    "putP": {
        "class": "putp",
        "group": "PutP sodium-proline symporter",
        "primary": "GO:0005298",
        "processes": ["GO:0035524"],
        "locations": ["GO:0005886"],
        "description": "putP encodes the SSF-family sodium/proline symporter PutP, a bacterial inner-membrane L-proline uptake system.",
    },
    "tcyP": {
        "class": "tcyp",
        "group": "TcyP cystine symporter",
        "primary": "GO:0015184",
        "processes": ["GO:0015811"],
        "locations": ["GO:0005886"],
        "description": "tcyP encodes a sodium-cystine symporter-family membrane protein, curated as an L-cystine transmembrane transporter candidate.",
    },
    "norM": {
        "class": "mate",
        "group": "MATE xenobiotic efflux antiporters",
        "primary": "GO:0042910",
        "processes": ["GO:0042908"],
        "locations": ["GO:0005886"],
        "description": "norM encodes the reviewed MATE-family multidrug efflux transporter NorM, an inner-membrane xenobiotic efflux system.",
    },
}

DOMAIN_NEEDLES = {
    "PP_0496": ["Sodium/alanine symporter", "alanine or glycine:cation symporter", "Na/Ala_symport"],
    "PP_0569": ["MATE efflux family protein", "multi antimicrobial extrusion", "MATE_fam"],
    "PP_0670": ["Transporter, bile acid/Na+ symporter family", "arsenical resistance-3", "Arsenical-R_Acr3"],
    "gltS": ["Sodium/glutamate symporter", "Catalyzes the sodium-dependent transport of glutamate", "GltS"],
    "arcD-I": ["Arginine-ornithine antiporter", "Arg/Orn_antiprt_ArcD"],
    "arcD-II": ["Arginine-ornithine antiporter", "Arg/Orn_antiprt_ArcD"],
    "actP-I": ["Cation/acetate symporter ActP", "Na/solute_symporter", "Sodium:Solute_Symporter"],
    "actP-II": ["Cation/acetate symporter ActP", "Na/solute_symporter", "Sodium:Solute_Symporter"],
    "actP-III": ["Cation/acetate symporter ActP", "Na/solute_symporter", "Sodium:Solute_Symporter"],
    "PP_3331": ["Sodium:proline symporter", "PepSY-ass_TM", "KW   Membrane"],
    "PP_4524": ["Sodium-solute symporter", "Na/solute_symporter", "Sodium:Solute_Symporter"],
    "putP": ["Sodium/proline symporter", "Catalyzes the sodium-dependent uptake", "Na/Pro_symporter"],
    "tcyP": ["Sodium-cystine symporter", "Na-dicarboxylate_symporter"],
    "norM": ["Probable multidrug resistance protein NorM", "Multidrug efflux pump", "MATE_MdtK"],
}


class GeneInfo(dict[str, Any]):
    gene: str


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


def load_rows() -> list[dict[str, str]]:
    with BATCH_PATH.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_info(row: dict[str, str]) -> GeneInfo:
    gene = row["gene"]
    uniprot_lines = (GENE_ROOT / gene / f"{gene}-uniprot.txt").read_text(encoding="utf-8").splitlines()
    asta_lines = (GENE_ROOT / gene / f"{gene}-deep-research-asta.md").read_text(encoding="utf-8").splitlines()
    review_doc = yaml.safe_load((GENE_ROOT / gene / f"{gene}-ai-review.yaml").read_text(encoding="utf-8"))
    info = GeneInfo(
        gene=gene,
        accession=row["uniprot_accession"],
        product=row["protein_name"],
        profile=PROFILE[gene],
        uniprot_lines=uniprot_lines,
        asta_lines=asta_lines,
        existing_refs={ref["id"]: ref for ref in review_doc.get("references", []) if "id" in ref},
    )
    info["de"] = first_de_line(uniprot_lines)
    info["asta_product"] = first_line(asta_lines, "- **Protein Description:**")
    info["asta_domains"] = first_line(asta_lines, "- **Key Domains:**")
    info["location"] = first_line(uniprot_lines, "SUBCELLULAR LOCATION", optional=True)
    return info


def base_support(info: GeneInfo) -> list[dict[str, str]]:
    gene = info["gene"]
    out = [
        support(ref_file(gene, "uniprot.txt"), info["de"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_product"]),
        support(ref_file(gene, "deep-research-asta.md"), info["asta_domains"]),
    ]
    if info.get("location"):
        out.append(support(ref_file(gene, "uniprot.txt"), info["location"]))
    for needle in DOMAIN_NEEDLES[gene]:
        line = first_line(info["uniprot_lines"], needle, optional=True)
        if line:
            out.append(support(ref_file(gene, "uniprot.txt"), line))
    return dedupe(out)


def goa_support(info: GeneInfo, go_id: str, label: str) -> dict[str, str]:
    return support(ref_file(info["gene"], "goa.tsv"), f"{go_id}\t{label}")


def review(
    info: GeneInfo,
    summary: str,
    action: str,
    reason: str,
    replacement_ids: list[str] | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": base_support(info),
    }
    if replacement_ids:
        item["proposed_replacement_terms"] = [term(go_id) for go_id in replacement_ids]
    return item


def existing_review(info: GeneInfo, ann: dict[str, Any]) -> dict[str, Any]:
    go_id = ann["term"]["id"]
    label = ann["term"]["label"]
    cls = info["profile"]["class"]
    primary = info["profile"]["primary"]

    if go_id == "GO:0005886":
        return review(info, "Plasma membrane localization is appropriate for this bacterial membrane transporter.", "ACCEPT", "UniProt/GOA subcellular and transmembrane evidence supports inner/plasma membrane localization.")
    if go_id == "GO:0016020":
        if "GO:0005886" in info["go_ids"]:
            return review(info, "Generic membrane localization is true but less informative than plasma membrane.", "MARK_AS_OVER_ANNOTATED", "A more specific plasma-membrane annotation is present.")
        return review(info, "Membrane localization is appropriate for this transmembrane transporter candidate.", "ACCEPT", "UniProt and domain evidence support a membrane protein.")
    if go_id in {"GO:0022857", "GO:0055085", "GO:0006865", "GO:0006814"}:
        if go_id == "GO:0055085" and cls == "ssf_broad":
            return review(info, "Transmembrane transport is appropriate broad process context for the unresolved SSF-family candidate.", "ACCEPT", "The SSF-family product supports transmembrane solute transport while substrate remains unresolved.")
        replacement = [primary] if primary else None
        return review(info, f"{label} is true but broad relative to the supported transporter function.", "MARK_AS_OVER_ANNOTATED", "A more specific substrate-coupled transporter annotation captures the core function.", replacement)
    if go_id in {"GO:0015293", "GO:0015297"}:
        if cls in {"mate", "tcyp", "low_proline", "ssf_broad"}:
            action = "ACCEPT" if go_id == primary else "KEEP_AS_NON_CORE"
            return review(info, f"{label} is retained as transporter-coupling context.", action, "The transporter family supports symport or antiport, but substrate-specific activity is the preferred core term when available.")
        return review(info, f"{label} is broad carrier-family context.", "KEEP_AS_NON_CORE", "The specific substrate transporter term is preferred as the core molecular function.", [primary])
    if go_id in {"GO:0003333", "GO:0035725"}:
        return review(info, f"{label} is appropriate process context for the AGCS sodium/amino-acid symporter candidate.", "ACCEPT", "The AGCS product/family evidence supports sodium-coupled amino-acid transmembrane transport.")
    if go_id == "GO:0005283":
        return review(info, "Amino acid:sodium symporter activity is appropriate for the AGCS sodium/alanine-family symporter.", "ACCEPT", "The product and AGCS domain evidence support sodium-coupled amino-acid symporter activity.")
    if go_id in {"GO:0015104", "GO:0015105"}:
        action = "ACCEPT" if go_id == "GO:0015105" else "KEEP_AS_NON_CORE"
        return review(info, f"{label} is supported by ACR3-family arsenical-resistance context.", action, "The UniProt family and InterPro domains identify PP_0670 as an ACR3 arsenite/antimonite transporter rather than a generic sodium-solute symporter.")
    if go_id in {"GO:0015699", "GO:0015700"}:
        return review(info, f"{label} is appropriate ACR3-family arsenical transport process context.", "ACCEPT", "The ACR3 family supports arsenite/antimonite membrane transport.")
    if go_id == "GO:0015501":
        return review(info, "Glutamate:sodium symporter activity is appropriate for GltS.", "ACCEPT", "UniProt function states sodium-dependent glutamate transport and the GltS/ESS family supports this specific activity.")
    if go_id == "GO:0015813":
        return review(info, "L-glutamate transmembrane transport is appropriate process context for GltS.", "ACCEPT", "The sodium/glutamate symporter activity directly supports L-glutamate transmembrane transport.")
    if go_id == "GO:0043858":
        return review(info, "Arginine:ornithine antiporter activity is appropriate for the ArcD proteins.", "ACCEPT", "The RecName and ArcD-domain evidence identify these as arginine-ornithine antiporters.")
    if go_id == "GO:1903826":
        return review(info, "L-arginine transmembrane transport is appropriate ArcD process context.", "ACCEPT", "Arginine-ornithine antiporter activity directly involves L-arginine movement across the membrane.")
    if go_id == "GO:0006527":
        return review(info, "L-arginine catabolic process is retained as pathway context but not the core molecular role.", "KEEP_AS_NON_CORE", "ArcD supports arginine-catabolism physiology by exchanging arginine and ornithine, while the core function is antiporter activity.")
    if go_id == "GO:0015123":
        return review(info, "Acetate transmembrane transporter activity is appropriate for the ActP proteins.", "ACCEPT", "The ActP product name and SSF-family evidence support acetate transporter activity.")
    if go_id == "GO:0006847":
        return review(info, "Plasma membrane acetate transport is appropriate process context for ActP.", "ACCEPT", "Acetate transmembrane transporter activity supports acetate movement at the bacterial plasma membrane.")
    if go_id in {"GO:0046942", "GO:1905039"}:
        return review(info, f"{label} is true but broad carboxylate-transport context.", "KEEP_AS_NON_CORE", "The substrate-specific acetate or proline transporter annotation is the more informative core term.", [primary])
    if go_id == "GO:0005298":
        return review(info, "Proline:sodium symporter activity is appropriate for PutP.", "ACCEPT", "The PutP product, family, and UniProt function support sodium-dependent proline uptake.")
    if go_id == "GO:0015193":
        return review(info, "L-proline transporter activity is correct but less specific than proline:sodium symporter activity.", "KEEP_AS_NON_CORE", "The sodium-coupled PutP term captures the core molecular function more precisely.", ["GO:0005298"])
    if go_id in {"GO:0015824", "GO:0035524"}:
        action = "ACCEPT" if go_id == "GO:0035524" else "KEEP_AS_NON_CORE"
        return review(info, f"{label} is proline-transport process context for PutP.", action, "The sodium/proline symporter activity supports proline transport; the transmembrane process term is the preferred core process.")
    if go_id == "GO:0031402":
        return review(info, "Sodium ion binding is retained as non-core coupling context for PutP.", "KEEP_AS_NON_CORE", "The core role is sodium/proline symport rather than ion binding alone.")
    if go_id == "GO:0015184":
        return review(info, "L-cystine transmembrane transporter activity is appropriate for TcyP.", "ACCEPT", "The product and dicarboxylate/amino-acid:cation symporter-family context support cystine transport.")
    if go_id == "GO:0015811":
        return review(info, "L-cystine transport is appropriate process context for TcyP.", "ACCEPT", "The supported cystine transporter activity implies L-cystine transport.")
    if go_id in {"GO:0042908", "GO:0042910"}:
        return review(info, f"{label} is appropriate for MATE-family efflux proteins.", "ACCEPT", "MATE-family product and domain evidence support xenobiotic/multidrug transmembrane efflux context.")

    raise ValueError(f"No review rule for {info['gene']} {go_id} {label}")


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
    primary = info["profile"].get("primary")
    if primary and primary not in go_ids:
        out.append(
            new_annotation(
                info,
                primary,
                "enables",
                f"Adds {TERMS[primary]} for this transporter-family candidate.",
                "The UniProt product/domain context and Asta retrieval header support this conservative first-pass transporter assignment.",
            )
        )
    for process in info["profile"].get("processes", []):
        if process not in go_ids:
            out.append(
                new_annotation(
                    info,
                    process,
                    "involved_in",
                    f"Adds {TERMS[process]} process context.",
                    "The supported transporter activity implies this conservative biological-process annotation.",
                )
            )
    for location in info["profile"].get("locations", []):
        if location not in go_ids:
            out.append(
                new_annotation(
                    info,
                    location,
                    "located_in",
                    f"Adds {TERMS[location]} localization context.",
                    "The UniProt record supports membrane or transmembrane localization.",
                )
            )
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


def core_function(info: GeneInfo) -> dict[str, Any]:
    profile = info["profile"]
    core: dict[str, Any] = {
        "description": profile["description"],
        "supported_by": base_support(info),
    }
    primary = profile.get("primary")
    if primary:
        core["molecular_function"] = term(primary)
    if profile.get("processes"):
        core["directly_involved_in"] = [term(go_id) for go_id in profile["processes"]]
    if profile.get("locations"):
        core["locations"] = [term(go_id) for go_id in profile["locations"]]
    return core


def curate_gene(row: dict[str, str]) -> GeneInfo:
    info = load_info(row)
    gene = info["gene"]
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    goa_annotations = [
        ann
        for ann in doc.get("existing_annotations", [])
        if not (
            ann.get("original_reference_id") == ref_file(gene, "uniprot.txt")
            and (ann.get("review") or {}).get("action") == "NEW"
        )
    ]
    info["go_ids"] = [ann["term"]["id"] for ann in goa_annotations]
    for ann in goa_annotations:
        ann["review"] = existing_review(info, ann)
        ann["review"]["supported_by"].insert(0, goa_support(info, ann["term"]["id"], ann["term"]["label"]))
        ann["review"]["supported_by"] = dedupe(ann["review"]["supported_by"])
    doc["existing_annotations"] = goa_annotations + suggested_new_annotations(info)
    doc["description"] = info["profile"]["description"]
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
    doc["suggested_questions"] = [
        {
            "question": "What is the exact transported solute, ion-coupling mechanism, directionality, and physiological condition for this transporter in KT2440?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure substrate-dependent uptake or efflux in transporter knockouts and complements, with sodium/proton dependence and substrate specificity tested for amino acids, acetate, cystine, arsenite/antimonite, and xenobiotics as appropriate.",
            "experiment_type": "transport genetics and substrate-uptake/efflux assay",
        }
    ]
    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")
    return info


def module_annoton(info: GeneInfo) -> dict[str, Any]:
    gene = info["gene"]
    annoton: dict[str, Any] = {
        "id": f"{gene}_sodium_solute_mate_context",
        "label": f"{gene}: {info['product']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": f"{gene}: {info['product']}",
    }
    primary = info["profile"].get("primary")
    if primary:
        annoton["function"] = descriptor(primary)
    if info["profile"].get("processes"):
        annoton["processes"] = [descriptor(go_id) for go_id in info["profile"]["processes"]]
    if info["profile"].get("locations"):
        annoton["locations"] = [descriptor(go_id) for go_id in info["profile"]["locations"]]
    return annoton


def build_module(infos: list[GeneInfo]) -> None:
    grouped: dict[str, list[GeneInfo]] = defaultdict(list)
    for info in infos:
        grouped[info["profile"]["group"]].append(info)
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
                    "description": f"First-pass sodium-solute/MATE transport subgroup: {group}.",
                    "annotons": [module_annoton(info) for info in group_infos],
                },
            }
        )
    concept_ids = [
        "GO:0005283",
        "GO:0015501",
        "GO:0043858",
        "GO:0015123",
        "GO:0005298",
        "GO:0015184",
        "GO:0042910",
        "GO:0015105",
        "GO:0015104",
        "GO:0015293",
        "GO:0015297",
        "GO:0003333",
        "GO:0015813",
        "GO:1903826",
        "GO:0006847",
        "GO:0035524",
        "GO:0015811",
        "GO:0042908",
        "GO:0015700",
        "GO:0015699",
        "GO:0005886",
        "GO:0016020",
    ]
    doc = {
        "id": "MODULE:sodium_solute_symporter_mate_boundary",
        "title": "Sodium-solute symporter and MATE efflux boundary",
        "description": (
            "Boundary module for PSEPK AGCS, GltS, ArcD, ActP, PutP, TcyP, broad SSF, MATE, and ACR3 "
            "transport-family entries from the transport ion/metal split."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_PATH.relative_to(ROOT)}",
                "title": "PSEPK sodium-solute/MATE transporter batch",
                "statement": "The batch table records 14 PSEPK ion/metal-bucket genes assigned to sodium-solute symporters, ArcD/ActP carriers, MATE efflux, and an ACR3 arsenical-resistance outlier.",
            },
            {
                "source_id": "file:projects/P_PUTIDA/batches/module_transport_membrane_efflux_ion_metal_partition.tsv",
                "title": "PSEPK transport ion/metal sub-bucket partition",
                "statement": "The deeper ion/metal partition separates this non-ABC solute transport set from monovalent cation antiporters, P-type ATPases, metal transporters, redox spillovers, and membrane enzyme side nodes.",
            },
        ],
        "notes": (
            "First-pass interpretation: retain substrate-specific transporter calls when product, family, and GOA agree. "
            "PP_0670 is treated as an ACR3 arsenite/antimonite transporter despite the batch's sodium-solute label. "
            "PP_3331 and PP_4524 remain broad symporter candidates until direct substrate evidence is available."
        ),
        "module": {
            "id": "sodium_solute_symporter_mate_boundary",
            "label": "Sodium-solute symporter and MATE efflux boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [descriptor(go_id, "Concept used for first-pass sodium-solute/MATE transport curation.") for go_id in concept_ids],
            "parts": parts,
        },
    }
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120), encoding="utf-8")


def main() -> None:
    infos = [curate_gene(row) for row in load_rows()]
    build_module(infos)
    print(f"Curated {len(infos)} genes")
    print(f"Wrote {MODULE_PATH}")


if __name__ == "__main__":
    main()
