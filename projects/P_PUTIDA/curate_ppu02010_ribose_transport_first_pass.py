#!/usr/bin/env python3
"""First-pass curation for the ppu02010 C33 Rbs ribose block."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"


def goa_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-goa.tsv"


def uniprot_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-uniprot.txt"


def asta_ref(gene: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"


def support_goa(gene: str, term_id: str, label: str) -> dict:
    return {"reference_id": goa_ref(gene), "supporting_text": f"{term_id}\t{label}"}


def support_uniprot(gene: str, text: str) -> dict:
    return {"reference_id": uniprot_ref(gene), "supporting_text": text}


def support_asta(gene: str, text: str) -> dict:
    return {"reference_id": asta_ref(gene), "supporting_text": text}


def ensure_reference(doc: dict, ref_id: str, title: str, supporting_text: str | None = None) -> None:
    refs = doc.setdefault("references", [])
    for ref in refs:
        if ref.get("id") == ref_id:
            if supporting_text and not ref.get("findings"):
                ref["findings"] = [{"supporting_text": supporting_text}]
            return
    ref = {"id": ref_id, "title": title, "findings": []}
    if supporting_text:
        ref["findings"].append({"supporting_text": supporting_text})
    refs.append(ref)


def review(
    gene: str,
    term_id: str,
    label: str,
    summary: str,
    action: str,
    reason: str,
    *,
    uniprot_text: str | None = None,
    asta_text: str | None = None,
    proposed: list[dict] | None = None,
    extra_support: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if uniprot_text:
        supported_by.append(support_uniprot(gene, uniprot_text))
    if asta_text:
        supported_by.append(support_asta(gene, asta_text))
    if extra_support:
        supported_by.extend(extra_support)
    result = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        result["proposed_replacement_terms"] = proposed
    return result


def new_annotation(
    term: dict,
    qualifier: str,
    gene: str,
    summary: str,
    reason: str,
    supported_by: list[dict],
) -> dict:
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": uniprot_ref(gene),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": supported_by,
        },
    }


CARBOHYDRATE_BINDING = {"id": "GO:0030246", "label": "carbohydrate binding"}
D_RIBOSE_TRANSMEMBRANE_TRANSPORT = {"id": "GO:0015752", "label": "D-ribose transmembrane transport"}
ABC_D_RIBOSE_TRANSPORTER = {"id": "GO:0015611", "label": "ABC-type D-ribose transporter activity"}
D_RIBOSE_TRANSPORTER = {"id": "GO:0015591", "label": "D-ribose transmembrane transporter activity"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
CELL_ENVELOPE = {"id": "GO:0030313", "label": "cell envelope"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
D_RIBOSE_PYRANASE = {"id": "GO:0062193", "label": "D-ribose pyranase activity"}
D_RIBOSE_CATABOLIC_PROCESS = {"id": "GO:0019303", "label": "D-ribose catabolic process"}
CYTOSOL = {"id": "GO:0005829", "label": "cytosol"}


CONFIG = {
    "rbsB": {
        "symbol": "rbsB",
        "description": (
            "rbsB (PP_2454) encodes the periplasmic ribose-binding solute-binding component "
            "of a predicted Rbs ABC D-ribose importer. The product name and periplasmic "
            "binding-protein family support ribose capture for delivery to the RbsC permease "
            "and RbsA-I ATP-binding component."
        ),
        "uniprot_text": "Full=Ribose ABC transporter, periplasmic ribose-binding subunit",
        "asta_text": "Protein Description:** SubName: Full=Ribose ABC transporter, periplasmic ribose-binding subunit",
        "reviews": {
            "GO:0030246": (
                "Carbohydrate binding is appropriate but broad for this ribose-binding solute-binding component.",
                "ACCEPT",
                "UniProt names RbsB as a periplasmic ribose-binding subunit of a ribose ABC transporter.",
                "periplasmic ribose-binding subunit",
            ),
            "GO:0030313": (
                "Cell envelope localization is acceptable for this bacterial periplasmic binding component.",
                "ACCEPT",
                "UniProt places RbsB in the cell envelope and names it as a periplasmic ribose-binding subunit.",
                "Cell envelope",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct but too broad relative to D-ribose transmembrane transport for this Rbs importer component.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name supports D-ribose-specific ABC transport context.",
                "Full=Ribose ABC transporter, periplasmic ribose-binding subunit",
            ),
        },
        "new": [
            new_annotation(
                D_RIBOSE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "rbsB",
                "RbsB should be represented with D-ribose transmembrane transport.",
                "RbsB is the periplasmic ribose-binding component of the local Rbs ABC importer.",
                [
                    support_uniprot("rbsB", "Full=Ribose ABC transporter, periplasmic ribose-binding subunit"),
                    support_asta("rbsB", "Protein Description:** SubName: Full=Ribose ABC transporter, periplasmic ribose-binding subunit"),
                ],
            ),
            new_annotation(
                ABC_D_RIBOSE_TRANSPORTER,
                "contributes_to",
                "rbsB",
                "RbsB contributes the substrate-binding component of ABC-type D-ribose transporter activity.",
                "The local rbsB/rbsA-I/rbsC locus encodes a D-ribose ABC importer.",
                [
                    support_uniprot("rbsB", "Full=Ribose ABC transporter, periplasmic ribose-binding subunit"),
                    support_uniprot("rbsB", "Periplasmic binding protein"),
                ],
            ),
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "rbsB",
                "RbsB should be represented as part of the ribose ABC transporter complex.",
                "RbsB is the solute-binding component paired with RbsA-I and RbsC in the local ribose ABC importer.",
                [support_uniprot("rbsB", "Full=Ribose ABC transporter, periplasmic ribose-binding subunit")],
            ),
        ],
        "core": {
            "description": "Periplasmic ribose-binding component of the PP_2454-PP_2456 Rbs D-ribose ABC importer.",
            "molecular_function": CARBOHYDRATE_BINDING,
            "directly_involved_in": [D_RIBOSE_TRANSMEMBRANE_TRANSPORT],
            "locations": [CELL_ENVELOPE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_goa("rbsB", "GO:0030246", "carbohydrate binding"),
                support_uniprot("rbsB", "Full=Ribose ABC transporter, periplasmic ribose-binding subunit"),
                support_asta("rbsB", "Protein Description:** SubName: Full=Ribose ABC transporter, periplasmic ribose-binding subunit"),
            ],
        },
    },
    "rbsA-I": {
        "symbol": "rbsA-I",
        "description": (
            "rbsA-I (PP_2455) encodes the ATP-binding energy-coupling subunit of the "
            "PP_2454-PP_2456 Rbs D-ribose ABC importer. Its ABC-carbohydrate-import "
            "ATPase domains, ATP-binding annotation, and local rbsB/rbsC context support "
            "ATP-dependent D-ribose uptake."
        ),
        "uniprot_text": "Full=Ribose ABC transporter-ATP-binding subunit",
        "asta_text": "Protein Description:** SubName: Full=Ribose ABC transporter-ATP-binding subunit",
        "reviews": {
            "GO:0000166": (
                "Nucleotide binding is correct but broad for this ABC ATP-binding subunit.",
                "MARK_AS_OVER_ANNOTATED",
                "ATP binding and ABC-type D-ribose transporter activity are more informative for RbsA-I.",
                "ATP-binding",
            ),
            "GO:0005524": (
                "ATP binding is appropriate for this ABC ATP-binding subunit.",
                "ACCEPT",
                "RbsA-I contains ABC transporter ATP-binding domains and ATP-binding sequence features.",
                "ATP-binding",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for the membrane-associated ATPase component of the importer.",
                "ACCEPT",
                "UniProt places RbsA-I at the cell inner membrane/cell membrane as a peripheral membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0015749": (
                "Monosaccharide transmembrane transport is correct but less specific than D-ribose transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and Rbs locus context support D-ribose-specific transport.",
                "Full=Ribose ABC transporter-ATP-binding subunit",
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic chemistry, but the substrate-specific ABC transporter activity is the core MF.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers ABC transport, while GO:0015611 captures ATP-dependent D-ribose import.",
                "ATP",
            ),
        },
        "new": [
            new_annotation(
                ABC_D_RIBOSE_TRANSPORTER,
                "enables",
                "rbsA-I",
                "RbsA-I should be represented with ABC-type D-ribose transporter activity.",
                "RbsA-I is the ATP-binding subunit of the local D-ribose ABC importer.",
                [
                    support_uniprot("rbsA-I", "Full=Ribose ABC transporter-ATP-binding subunit"),
                    support_uniprot("rbsA-I", "Ribose import ATP-binding protein RbsA"),
                    support_asta("rbsA-I", "Protein Description:** SubName: Full=Ribose ABC transporter-ATP-binding subunit"),
                ],
            ),
            new_annotation(
                D_RIBOSE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "rbsA-I",
                "RbsA-I should be represented with D-ribose transmembrane transport.",
                "The local rbsB/rbsA-I/rbsC locus encodes a D-ribose ABC importer.",
                [support_uniprot("rbsA-I", "Full=Ribose ABC transporter-ATP-binding subunit")],
            ),
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "rbsA-I",
                "RbsA-I should be represented as the ATP-binding subunit of the ribose ABC transporter complex.",
                "The Rbs importer pairs RbsA-I with the RbsB solute-binding component and RbsC permease.",
                [support_uniprot("rbsA-I", "Full=Ribose ABC transporter-ATP-binding subunit")],
            ),
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit of the PP_2454-PP_2456 Rbs D-ribose ABC importer.",
            "molecular_function": ABC_D_RIBOSE_TRANSPORTER,
            "directly_involved_in": [D_RIBOSE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("rbsA-I", "Full=Ribose ABC transporter-ATP-binding subunit"),
                support_uniprot("rbsA-I", "Ribose import ATP-binding protein RbsA"),
                support_asta("rbsA-I", "Protein Description:** SubName: Full=Ribose ABC transporter-ATP-binding subunit"),
            ],
        },
    },
    "rbsC": {
        "symbol": "rbsC",
        "description": (
            "rbsC (PP_2456) encodes the membrane permease component of the PP_2454-PP_2456 "
            "Rbs D-ribose ABC importer. UniProt names it as a D-ribose ABC transporter "
            "permease and places it in the AraH/RbsC subfamily of binding-protein-dependent "
            "transport-system permeases."
        ),
        "uniprot_text": "Full=D-ribose ABC transporter-permease subunit",
        "asta_text": "Protein Description:** SubName: Full=D-ribose ABC transporter-permease subunit",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial permease.",
                "ACCEPT",
                "UniProt places RbsC at the cell inner membrane and predicts a multi-pass membrane protein.",
                "Cell inner membrane",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial inner-membrane permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell inner membrane",
            ),
            "GO:0022857": (
                "Transmembrane transporter activity is correct but too broad for this D-ribose ABC permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and AraH/RbsC permease-family assignment support D-ribose transporter activity.",
                "Full=D-ribose ABC transporter-permease subunit",
            ),
            "GO:0055085": (
                "Transmembrane transport is correct but too broad relative to D-ribose transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and Rbs locus context support D-ribose-specific transmembrane transport.",
                "Full=D-ribose ABC transporter-permease subunit",
            ),
        },
        "new": [
            new_annotation(
                D_RIBOSE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "rbsC",
                "RbsC should be represented with D-ribose transmembrane transport.",
                "RbsC is the permease subunit of the local D-ribose ABC importer.",
                [
                    support_uniprot("rbsC", "Full=D-ribose ABC transporter-permease subunit"),
                    support_asta("rbsC", "Protein Description:** SubName: Full=D-ribose ABC transporter-permease subunit"),
                ],
            ),
            new_annotation(
                ABC_D_RIBOSE_TRANSPORTER,
                "contributes_to",
                "rbsC",
                "RbsC contributes the membrane-channel component of ABC-type D-ribose transporter activity.",
                "RbsC is the D-ribose ABC transporter permease paired with RbsB and RbsA-I.",
                [
                    support_uniprot("rbsC", "Full=D-ribose ABC transporter-permease subunit"),
                    support_uniprot("rbsC", "AraH/RbsC subfamily"),
                ],
            ),
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "rbsC",
                "RbsC should be represented as part of the ribose ABC transporter complex.",
                "RbsC is the permease component of the local Rbs ABC importer.",
                [support_uniprot("rbsC", "Full=D-ribose ABC transporter-permease subunit")],
            ),
        ],
        "core": {
            "description": "Membrane permease component of the PP_2454-PP_2456 Rbs D-ribose ABC importer.",
            "contributes_to_molecular_function": ABC_D_RIBOSE_TRANSPORTER,
            "directly_involved_in": [D_RIBOSE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("rbsC", "Full=D-ribose ABC transporter-permease subunit"),
                support_uniprot("rbsC", "AraH/RbsC subfamily"),
                support_asta("rbsC", "Protein Description:** SubName: Full=D-ribose ABC transporter-permease subunit"),
            ],
        },
    },
    "rbsD": {
        "symbol": "rbsD",
        "description": (
            "rbsD (PP_2459) encodes a reviewed cytosolic D-ribose pyranase associated with "
            "D-ribose utilization. It catalyzes interconversion of beta-pyran and beta-furan "
            "forms of D-ribose as the first step of the UniPathway D-ribose degradation route, "
            "and is best modeled as a ribose-catabolic accessory enzyme near the Rbs importer."
        ),
        "uniprot_text": "Full=D-ribose pyranase",
        "asta_text": "Protein Description:** RecName: Full=D-ribose pyranase",
        "reviews": {
            "GO:0005737": (
                "Cytoplasm localization is appropriate for this soluble ribose-catabolic enzyme.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation places RbsD in the cytoplasm.",
                "Cytoplasm",
            ),
            "GO:0005829": (
                "Cytosol localization is appropriate for this soluble RbsD enzyme.",
                "ACCEPT",
                "GOA includes a cytosol annotation and UniProt/HAMAP places RbsD in the cytoplasm.",
                "Cytoplasm",
            ),
            "GO:0005996": (
                "Monosaccharide metabolic process is correct but broad relative to D-ribose catabolic process.",
                "MARK_AS_OVER_ANNOTATED",
                "Reviewed UniProt/HAMAP annotation places RbsD in D-ribose degradation.",
                "D-ribose degradation",
            ),
            "GO:0016853": (
                "Isomerase activity is correct but too broad for RbsD.",
                "MARK_AS_OVER_ANNOTATED",
                "D-ribose pyranase activity captures the specific interconversion of beta-pyran and beta-furan forms of D-ribose.",
                "Catalyzes the interconversion of beta-pyran and beta-furan",
            ),
            "GO:0016866": (
                "Intramolecular transferase activity is a broad parent-level annotation for the specific RbsD pyranase activity.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0062193 captures the specific D-ribose pyranase function.",
                "Full=D-ribose pyranase",
            ),
            "GO:0016872": (
                "Intramolecular lyase activity is correct but less specific than D-ribose pyranase activity.",
                "MARK_AS_OVER_ANNOTATED",
                "UniProt records the Rhea reaction and EC 5.4.99.62 for D-ribose pyranase.",
                "Reaction=beta-D-ribopyranose = beta-D-ribofuranose;",
            ),
            "GO:0019303": (
                "D-ribose catabolic process is appropriate process context for RbsD.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP pathway annotation places RbsD in D-ribose degradation.",
                "D-ribose degradation",
            ),
            "GO:0048029": (
                "Monosaccharide binding is correct substrate-binding context but non-core relative to the catalytic pyranase activity.",
                "KEEP_AS_NON_CORE",
                "RbsD binds a monosaccharide substrate while catalyzing D-ribose pyranose/furanose interconversion.",
                "forms of D-ribose",
            ),
            "GO:0062193": (
                "D-ribose pyranase activity is the specific molecular function for RbsD.",
                "ACCEPT",
                "Reviewed UniProt/HAMAP annotation records the D-ribose pyranase reaction and EC 5.4.99.62.",
                "Full=D-ribose pyranase",
            ),
        },
        "core": {
            "description": "Cytosolic D-ribose pyranase accessory enzyme for D-ribose utilization.",
            "molecular_function": D_RIBOSE_PYRANASE,
            "directly_involved_in": [D_RIBOSE_CATABOLIC_PROCESS],
            "locations": [CYTOSOL],
            "support": [
                support_goa("rbsD", "GO:0062193", "D-ribose pyranase activity"),
                support_uniprot("rbsD", "Catalyzes the interconversion of beta-pyran and beta-furan"),
                support_uniprot("rbsD", "Reaction=beta-D-ribopyranose = beta-D-ribofuranose;"),
                support_asta("rbsD", "Protein Description:** RecName: Full=D-ribose pyranase"),
            ],
        },
    },
}


def curate_gene(gene: str, cfg: dict) -> None:
    path = Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["gene_symbol"] = cfg["symbol"]
    doc["status"] = "COMPLETE"
    doc["description"] = cfg["description"]

    ensure_reference(doc, goa_ref(gene), f"QuickGO GOA annotations for {gene}")
    ensure_reference(doc, uniprot_ref(gene), f"UniProtKB entry for {gene} ({doc['id']})", cfg["uniprot_text"])
    ensure_reference(doc, asta_ref(gene), f"Asta retrieval report for {gene} ({doc['id']})", cfg["asta_text"])

    doc["existing_annotations"] = [
        ann for ann in doc.get("existing_annotations", []) if ann.get("review", {}).get("action") != "NEW"
    ]

    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        if term_id not in cfg["reviews"]:
            raise ValueError(f"No review configured for {gene} {term_id}")
        summary, action, reason, uniprot_text = cfg["reviews"][term_id]
        ann["review"] = review(
            gene,
            term_id,
            ann["term"]["label"],
            summary,
            action,
            reason,
            uniprot_text=uniprot_text,
            asta_text=cfg["asta_text"] if action == "ACCEPT" else None,
        )

    doc["existing_annotations"].extend(cfg.get("new", []))

    core = dict(cfg["core"])
    support = core.pop("support")
    core["supported_by"] = support
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "Are the PP_2454-PP_2456 and PP_2757-PP_2761 ribose-like loci functionally redundant, differentially regulated, or specialized for distinct pentose substrates in KT2440?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure D-ribose uptake and growth on ribose in PP_2454-PP_2456 transporter mutants, rbsD mutants, and paired mutants with the PP_2757-PP_2761 ribose-like locus.",
            "experiment_type": "targeted ribose transporter and pyranase mutant uptake/growth assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
