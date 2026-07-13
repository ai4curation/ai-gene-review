#!/usr/bin/env python3
"""First-pass curation for the ppu02010 C22 Gts glucose ABC importer."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
PMID_GLUCOSE = "PMID:17483213"
PMID_GLUCOSE_TITLE = (
    "Convergent peripheral pathways catalyze initial glucose catabolism in Pseudomonas putida: genomic and flux analysis."
)
PMID_GLUCOSE_TEXT = (
    "Glucose is transported to the cytoplasm in a \n"
    "process mediated by an ABC uptake system encoded by open reading frames PP1015 \n"
    "to PP1018 and is then phosphorylated by glucokinase"
)


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


def support_pubmed() -> dict:
    return {"reference_id": PMID_GLUCOSE, "supporting_text": PMID_GLUCOSE_TEXT}


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


D_GLUCOSE_BINDING = {"id": "GO:0005536", "label": "D-glucose binding"}
D_GLUCOSE_TRANSMEMBRANE_TRANSPORT = {
    "id": "GO:1904659",
    "label": "D-glucose transmembrane transport",
}
ABC_MONOSACCHARIDE_TRANSPORTER = {
    "id": "GO:0015407",
    "label": "ABC-type monosaccharide transporter activity",
}
ABC_TRANSPORTER_ACTIVITY = {"id": "GO:0140359", "label": "ABC-type transporter activity"}
CARBOHYDRATE_TRANSPORT = {"id": "GO:0008643", "label": "carbohydrate transport"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
CELL_ENVELOPE = {"id": "GO:0030313", "label": "cell envelope"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}


CONFIG = {
    "gtsA": {
        "symbol": "gtsA",
        "description": (
            "gtsA (PP_1015) encodes the solute-binding component of the PP_1015-PP_1018 "
            "Gts glucose ABC uptake system in Pseudomonas putida KT2440. The product is "
            "annotated as a mannose/glucose ABC transporter glucose-binding periplasmic "
            "protein, and a P. putida glucose-catabolism study identifies PP1015-PP1018 "
            "as the ABC uptake system that transports glucose to the cytoplasm."
        ),
        "uniprot_text": "Full=Mannose/glucose ABC transporter, glucose-binding periplasmic protein",
        "asta_text": "Protein Description:** SubName: Full=Mannose/glucose ABC transporter, glucose-binding periplasmic protein",
        "reviews": {
            "GO:0030313": (
                "Cell envelope localization is acceptable for this periplasmic/cell-envelope solute-binding component.",
                "ACCEPT",
                "UniProt names GtsA as a glucose-binding periplasmic protein, and GOA maps the subcellular-location vocabulary to cell envelope.",
                "glucose-binding periplasmic protein",
            ),
        },
        "new": [
            new_annotation(
                D_GLUCOSE_BINDING,
                "enables",
                "gtsA",
                "GtsA should be represented with D-glucose binding as the solute-binding component of the Gts importer.",
                "The product name identifies a glucose-binding periplasmic protein, and the P. putida glucose-catabolism paper assigns PP1015-PP1018 to glucose ABC uptake.",
                [
                    support_uniprot("gtsA", "Full=Mannose/glucose ABC transporter, glucose-binding periplasmic protein"),
                    support_pubmed(),
                ],
            ),
            new_annotation(
                D_GLUCOSE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "gtsA",
                "GtsA participates in D-glucose transmembrane transport as the solute-binding component.",
                "The PP1015-PP1018 locus is reported as the ABC uptake system transporting glucose to the cytoplasm.",
                [support_pubmed()],
            ),
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                "gtsA",
                "GtsA should be represented as part of the Gts ABC transporter complex.",
                "GtsA is the binding component of the PP1015-PP1018 ABC uptake system.",
                [
                    support_uniprot("gtsA", "Full=Mannose/glucose ABC transporter, glucose-binding periplasmic protein"),
                    support_pubmed(),
                ],
            ),
        ],
        "core": {
            "description": "Glucose-binding solute-binding component of the PP_1015-PP_1018 Gts glucose ABC importer.",
            "molecular_function": D_GLUCOSE_BINDING,
            "directly_involved_in": [D_GLUCOSE_TRANSMEMBRANE_TRANSPORT],
            "locations": [CELL_ENVELOPE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("gtsA", "Full=Mannose/glucose ABC transporter, glucose-binding periplasmic protein"),
                support_pubmed(),
                support_asta("gtsA", "Protein Description:** SubName: Full=Mannose/glucose ABC transporter, glucose-binding periplasmic protein"),
            ],
        },
    },
    "gtsB": {
        "symbol": "gtsB",
        "description": (
            "gtsB (PP_1016) encodes a multi-pass membrane permease component of the "
            "PP_1015-PP_1018 Gts glucose ABC uptake system. It is annotated as a "
            "mannose/glucose ABC transporter permease and belongs to the "
            "binding-protein-dependent transport-system permease family."
        ),
        "uniprot_text": "Full=Mannose/glucose ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Mannose/glucose ABC transporter, permease protein",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial ABC permease.",
                "ACCEPT",
                "UniProt predicts GtsB as a cell-membrane multi-pass membrane protein.",
                "Cell membrane",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell membrane",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for GtsB.",
                "ACCEPT",
                "GtsB is a binding-protein-dependent transport-system permease in the PP1015-PP1018 glucose ABC uptake system.",
                "Belongs to the binding-protein-dependent transport system",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to D-glucose transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and P. putida glucose-catabolism paper support glucose-specific transport for the PP1015-PP1018 system.",
                "Full=Mannose/glucose ABC transporter, permease protein",
            ),
        },
        "new": [
            new_annotation(
                D_GLUCOSE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "gtsB",
                "GtsB should be represented with D-glucose transmembrane transport.",
                "The PP1015-PP1018 locus is reported as the ABC uptake system transporting glucose to the cytoplasm.",
                [support_pubmed(), support_uniprot("gtsB", "Full=Mannose/glucose ABC transporter, permease protein")],
            ),
            new_annotation(
                ABC_MONOSACCHARIDE_TRANSPORTER,
                "contributes_to",
                "gtsB",
                "GtsB contributes the membrane-channel component of ABC-type monosaccharide transporter activity.",
                "GtsB is a mannose/glucose ABC permease in the PP1015-PP1018 glucose uptake system.",
                [support_uniprot("gtsB", "Full=Mannose/glucose ABC transporter, permease protein"), support_pubmed()],
            ),
        ],
        "core": {
            "description": "Multi-pass membrane permease component of the PP_1015-PP_1018 Gts glucose ABC importer.",
            "contributes_to_molecular_function": ABC_MONOSACCHARIDE_TRANSPORTER,
            "directly_involved_in": [D_GLUCOSE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("gtsB", "Full=Mannose/glucose ABC transporter, permease protein"),
                support_uniprot("gtsB", "Belongs to the binding-protein-dependent transport system"),
                support_pubmed(),
            ],
        },
    },
    "gtsC": {
        "symbol": "gtsC",
        "description": (
            "gtsC (PP_1017) encodes the second multi-pass membrane permease component of "
            "the PP_1015-PP_1018 Gts glucose ABC uptake system. Its product name and "
            "binding-protein-dependent transport-system permease family assignment support "
            "a channel role in glucose import."
        ),
        "uniprot_text": "Full=Mannose/glucose ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Mannose/glucose ABC transporter, permease protein",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass bacterial ABC permease.",
                "ACCEPT",
                "UniProt predicts GtsC as a cell-membrane multi-pass membrane protein.",
                "Cell membrane",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than plasma membrane for this bacterial permease.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma membrane annotation is the more informative retained location.",
                "Cell membrane",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for GtsC.",
                "ACCEPT",
                "GtsC is a binding-protein-dependent transport-system permease in the PP1015-PP1018 glucose ABC uptake system.",
                "Belongs to the binding-protein-dependent transport system",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to D-glucose transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The product name and P. putida glucose-catabolism paper support glucose-specific transport for the PP1015-PP1018 system.",
                "Full=Mannose/glucose ABC transporter, permease protein",
            ),
        },
        "new": [
            new_annotation(
                D_GLUCOSE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "gtsC",
                "GtsC should be represented with D-glucose transmembrane transport.",
                "The PP1015-PP1018 locus is reported as the ABC uptake system transporting glucose to the cytoplasm.",
                [support_pubmed(), support_uniprot("gtsC", "Full=Mannose/glucose ABC transporter, permease protein")],
            ),
            new_annotation(
                ABC_MONOSACCHARIDE_TRANSPORTER,
                "contributes_to",
                "gtsC",
                "GtsC contributes the second membrane-channel component of ABC-type monosaccharide transporter activity.",
                "GtsC is a mannose/glucose ABC permease in the PP1015-PP1018 glucose uptake system.",
                [support_uniprot("gtsC", "Full=Mannose/glucose ABC transporter, permease protein"), support_pubmed()],
            ),
        ],
        "core": {
            "description": "Second multi-pass membrane permease component of the PP_1015-PP_1018 Gts glucose ABC importer.",
            "contributes_to_molecular_function": ABC_MONOSACCHARIDE_TRANSPORTER,
            "directly_involved_in": [D_GLUCOSE_TRANSMEMBRANE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_uniprot("gtsC", "Full=Mannose/glucose ABC transporter, permease protein"),
                support_uniprot("gtsC", "Belongs to the binding-protein-dependent transport system"),
                support_pubmed(),
            ],
        },
    },
    "gtsD": {
        "symbol": "gtsD",
        "description": (
            "gtsD (PP_1018) encodes the ATP-binding energy-coupling subunit of the "
            "PP_1015-PP_1018 Gts glucose ABC uptake system. Although automated family "
            "annotation labels the protein as MalK/YcjV-like and assigns maltose transport, "
            "P. putida-specific evidence identifies PP1015-PP1018 as the ABC uptake system "
            "transporting glucose to the cytoplasm."
        ),
        "uniprot_text": "Full=Maltose import ATP-binding protein YcjV",
        "asta_text": "Protein Description:** RecName: Full=Maltose import ATP-binding protein YcjV",
        "reviews": {
            "GO:0000166": (
                "Nucleotide binding is correct but too broad for this ABC ATP-binding subunit.",
                "MARK_AS_OVER_ANNOTATED",
                "ATP binding and ABC-type monosaccharide transporter activity are more informative descriptions of the GtsD core function.",
                "ATP-binding",
            ),
            "GO:0005524": (
                "ATP binding is appropriate for this ABC ATP-binding subunit.",
                "ACCEPT",
                "GtsD belongs to the ABC transporter ATP-binding superfamily.",
                "ATP-binding",
            ),
            "GO:0008643": (
                "Carbohydrate transport is correct process context for the GtsD ATPase, but D-glucose transmembrane transport is more specific for PP1015-PP1018.",
                "MARK_AS_OVER_ANNOTATED",
                "The P. putida glucose-catabolism paper identifies PP1015-PP1018 as the glucose ABC uptake system.",
                "carbohydrate transport",
            ),
            "GO:0015423": (
                "ABC-type maltose transporter activity appears to be a MalK/YcjV-family over-propagation for this P. putida glucose uptake ATPase.",
                "REMOVE",
                "The organism-specific glucose-catabolism evidence assigns PP1015-PP1018 to glucose uptake, while only automated family annotation supports maltose transport.",
                "Reaction=D-maltose(out) + ATP + H2O = D-maltose(in) + ADP + phosphate +",
            ),
            "GO:0016887": (
                "ATP hydrolysis is correct mechanistic chemistry, but the transporter activity is the core MF for this ATPase subunit.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers the ABC transporter, while GO:0015407 captures ATP-dependent monosaccharide import.",
                "ATP",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for GtsD.",
                "ACCEPT",
                "GtsD is the ATP-binding component of the PP1015-PP1018 ABC uptake system.",
                "ABC transporter",
            ),
            "GO:0055052": (
                "Substrate-binding subunit-containing ABC transporter complex is appropriate for this importer.",
                "ACCEPT",
                "The PP1015-PP1018 glucose uptake system includes the GtsA solute-binding component together with GtsB/GtsC permeases and GtsD ATPase.",
                "The complex is composed of two ATP-binding proteins (YcjV)",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to D-glucose transmembrane transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The P. putida glucose-catabolism paper identifies PP1015-PP1018 as the glucose ABC uptake system.",
                "transmembrane transport",
            ),
            "GO:0140359": (
                "ABC-type transporter activity is correct but less specific than ABC-type monosaccharide transporter activity for the GtsD ATPase.",
                "MODIFY",
                "The local PP1015-PP1018 system transports glucose, a monosaccharide; GO:0015407 is the more specific ABC transporter activity.",
                "ABC-type transporter activity",
            ),
            "GO:1904981": (
                "Maltose transmembrane transport appears to be an automated consequence of the maltose-transporter activity annotation and is not supported as the P. putida locus function.",
                "REMOVE",
                "The organism-specific glucose-catabolism evidence assigns PP1015-PP1018 to glucose uptake rather than maltose transport.",
                "maltose transmembrane transport",
            ),
        },
        "proposed": {"GO:0140359": [ABC_MONOSACCHARIDE_TRANSPORTER]},
        "new": [
            new_annotation(
                ABC_MONOSACCHARIDE_TRANSPORTER,
                "enables",
                "gtsD",
                "GtsD should be represented with ABC-type monosaccharide transporter activity.",
                "The PP1015-PP1018 locus is reported as an ABC uptake system for glucose, and GtsD is the ATP-binding component.",
                [
                    support_pubmed(),
                    support_uniprot("gtsD", "ABC transporter"),
                    support_asta("gtsD", "Protein Description:** RecName: Full=Maltose import ATP-binding protein YcjV"),
                ],
            ),
            new_annotation(
                D_GLUCOSE_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "gtsD",
                "GtsD should be represented with D-glucose transmembrane transport.",
                "The PP1015-PP1018 locus is reported as the ABC uptake system transporting glucose to the cytoplasm.",
                [support_pubmed()],
            ),
        ],
        "core": {
            "description": "ATP-binding energy-coupling subunit of the PP_1015-PP_1018 Gts glucose ABC importer.",
            "molecular_function": ABC_MONOSACCHARIDE_TRANSPORTER,
            "directly_involved_in": [D_GLUCOSE_TRANSMEMBRANE_TRANSPORT],
            "in_complex": ABC_COMPLEX,
            "support": [
                support_pubmed(),
                support_goa("gtsD", "GO:0140359", "ABC-type transporter activity"),
                support_uniprot("gtsD", "ABC transporter"),
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
    ensure_reference(doc, PMID_GLUCOSE, PMID_GLUCOSE_TITLE, PMID_GLUCOSE_TEXT)

    doc["existing_annotations"] = [
        ann for ann in doc.get("existing_annotations", []) if ann.get("review", {}).get("action") != "NEW"
    ]

    proposed_by_term = cfg.get("proposed", {})
    for ann in doc.get("existing_annotations", []):
        term_id = ann["term"]["id"]
        if term_id not in cfg["reviews"]:
            raise ValueError(f"No review configured for {gene} {term_id}")
        summary, action, reason, uniprot_text = cfg["reviews"][term_id]
        extra_support = [support_pubmed()] if term_id in {"GO:0008643", "GO:0015423", "GO:0055085", "GO:0140359", "GO:1904981"} else None
        ann["review"] = review(
            gene,
            term_id,
            ann["term"]["label"],
            summary,
            action,
            reason,
            uniprot_text=uniprot_text,
            asta_text=cfg["asta_text"] if action == "ACCEPT" else None,
            proposed=proposed_by_term.get(term_id),
            extra_support=extra_support,
        )

    doc["existing_annotations"].extend(cfg.get("new", []))

    core = dict(cfg["core"])
    support = core.pop("support")
    core["supported_by"] = support
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "What are the exact substrate range and affinities of the PP_1015-PP_1018 Gts ABC importer for D-glucose, D-mannose, and related hexoses in KT2440?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Measure uptake and growth on glucose, mannose, maltose, and related sugars in single-subunit and whole-locus PP_1015-PP_1018 mutants, with complementation of the Gts importer.",
            "experiment_type": "targeted sugar uptake and carbon-source growth assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
