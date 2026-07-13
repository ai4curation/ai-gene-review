#!/usr/bin/env python3
"""First-pass curation for the ppu02010 sulfur/cystine ABC transporter block."""

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


def goa_text(term_id: str, label: str) -> str:
    return f"{term_id}\t{label}"


def support_goa(gene: str, term_id: str, label: str) -> dict:
    return {"reference_id": goa_ref(gene), "supporting_text": goa_text(term_id, label)}


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
    asta_text: str | None = None,
    proposed: list[dict] | None = None,
    extra_support: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
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
    original_reference_id: str,
    summary: str,
    reason: str,
    supported_by: list[dict],
) -> dict:
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": original_reference_id,
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": supported_by,
        },
    }


ABC_AMINO_ACID = {"id": "GO:0015424", "label": "ABC-type amino acid transporter activity"}
CYSTINE_TRANSPORTER = {"id": "GO:0015184", "label": "L-cystine transmembrane transporter activity"}
CYSTINE_TRANSPORT = {"id": "GO:0015811", "label": "L-cystine transport"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0042597", "label": "periplasmic space"}


CONFIG = {
    "sctC": {
        "symbol": "sctC",
        "description": (
            "sctC (PP_0225) encodes the ATP-binding energy-coupling component of a predicted "
            "cystine/sulfur-compound ABC transporter. Its ABC ATPase domain and adjacency to "
            "sctS and the periplasmic cystine-binding protein fliY support a role in ATP-driven "
            "amino-acid/sulfur-compound uptake rather than an independent metabolic enzyme."
        ),
        "asta_text": "Protein Description:** SubName: Full=Sulfur compound ABC transporter-ATP-binding subunit",
        "uniprot_text": "Full=Sulfur compound ABC transporter-ATP-binding subunit",
        "reviews": {
            "GO:0000166": (
                "Nucleotide binding is true but less informative than ATP binding for this ABC ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "The review retains the more specific ATP-binding and ATP-hydrolysis annotations for the transporter ATPase.",
            ),
            "GO:0003333": (
                "Amino acid transmembrane transport is correct but should be narrowed to the cystine-transport context of the local sctC-sctS-fliY locus.",
                "MODIFY",
                "The neighboring sctS/fliY annotations and product names support an L-cystine/sulfur-compound ABC transporter; L-cystine transport is the better process term for this sub-batch.",
                [CYSTINE_TRANSPORT],
            ),
            "GO:0005524": (
                "ATP binding is correct for the ABC-transporter nucleotide-binding component.",
                "ACCEPT",
                "SctC has ABC transporter ATP-binding domains and is annotated as the ATP-binding subunit of the sulfur-compound transporter.",
            ),
            "GO:0005886": (
                "Plasma membrane localization is appropriate for the inner-membrane-associated ABC transporter ATPase.",
                "ACCEPT",
                "UniProt places this ABC ATPase at the cell inner membrane as a peripheral membrane protein.",
            ),
            "GO:0015424": (
                "ABC-type amino acid transporter activity is appropriate at first pass for the ATP-binding component.",
                "ACCEPT",
                "The local transporter appears to import cystine or a related sulfur-containing amino acid, but the existing ABC-type amino acid transporter term is a reasonable complex-level activity for the ATPase subunit.",
            ),
            "GO:0016887": (
                "ATP hydrolysis activity is correct mechanistic context for the ABC ATPase.",
                "KEEP_AS_NON_CORE",
                "ATP hydrolysis powers transport, while substrate-specific transport is captured in the process and transporter-complex context.",
            ),
        },
        "new_annotations": [
            {
                "term": CYSTINE_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-cystine transport is a useful missing process annotation for the SctC ATP-binding component.",
                "reason": "The adjacent SctS permease has L-cystine transporter and L-cystine transport annotations, and FliY is named as a periplasmic cystine-binding protein, supporting the same cystine-transport sub-batch for SctC.",
                "supporting_text": "Full=Sulfur compound ABC transporter-ATP-binding subunit",
            }
        ],
        "core": {
            "description": "ATP-binding component of a predicted cystine/sulfur-compound ABC uptake system.",
            "molecular_function": ABC_AMINO_ACID,
            "directly_involved_in": [CYSTINE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "support": ("GO:0015424", "ABC-type amino acid transporter activity"),
        },
    },
    "sctS": {
        "symbol": "sctS",
        "description": (
            "sctS (PP_0226) encodes a predicted multi-pass inner-membrane permease of an "
            "ABC-type cystine/sulfur-compound uptake system. TreeGrafter assigns L-cystine "
            "transmembrane transporter activity and L-cystine transport, consistent with its "
            "position next to sctC and fliY."
        ),
        "asta_text": "Protein Description:** SubName: Full=Sulfur compound ABC transporter-permease subunit",
        "uniprot_text": "Full=Sulfur compound ABC transporter-permease subunit",
        "reviews": {
            "GO:0005886": (
                "Plasma membrane localization is appropriate for this multi-pass transporter permease.",
                "ACCEPT",
                "UniProt predicts SctS as a cell inner-membrane multi-pass membrane protein.",
            ),
            "GO:0006865": (
                "Amino acid transport is correct but less specific than L-cystine transport.",
                "MARK_AS_OVER_ANNOTATED",
                "The same TreeGrafter source assigns the more informative L-cystine transport process.",
            ),
            "GO:0015184": (
                "L-cystine transmembrane transporter activity is the best substrate-specific molecular-function term for SctS.",
                "ACCEPT",
                "TreeGrafter assigns L-cystine transmembrane transporter activity, and the local fliY product is a periplasmic cystine-binding protein.",
            ),
            "GO:0015811": (
                "L-cystine transport is the correct biological-process context for SctS.",
                "ACCEPT",
                "This is the substrate-specific process term already assigned by TreeGrafter for the permease.",
            ),
            "GO:0016020": (
                "Membrane localization is correct but less specific than the plasma-membrane annotation.",
                "MARK_AS_OVER_ANNOTATED",
                "The plasma-membrane term is more informative for this bacterial inner-membrane permease.",
            ),
            "GO:0022857": (
                "Generic transmembrane transporter activity is too broad for this cystine transporter permease.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0015184 captures the substrate-specific transporter activity.",
            ),
            "GO:0043190": (
                "ABC transporter complex membership is appropriate for this permease component.",
                "ACCEPT",
                "SctS is a binding-protein-dependent transport-system permease in the local sctC-sctS-fliY ABC transporter locus.",
            ),
            "GO:0055085": (
                "Transmembrane transport is true but broad relative to the existing L-cystine transport annotation.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0015811 already captures the substrate-specific process for this transporter component.",
            ),
        },
        "core": {
            "description": "Multi-pass permease component of a predicted ABC-type L-cystine uptake system.",
            "molecular_function": CYSTINE_TRANSPORTER,
            "directly_involved_in": [CYSTINE_TRANSPORT],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "support": ("GO:0015184", "L-cystine transmembrane transporter activity"),
        },
    },
    "fliY": {
        "symbol": "fliY",
        "description": (
            "fliY (PP_0227) encodes a predicted signal-peptide-bearing periplasmic cystine-binding "
            "protein of the bacterial solute-binding protein family. Despite the fliY symbol, this "
            "KT2440 protein is best treated in this first pass as the solute-binding component of the "
            "adjacent SctC/SctS cystine or sulfur-compound ABC uptake system."
        ),
        "asta_text": "Protein Description:** SubName: Full=Periplasmic cystine-binding protein",
        "uniprot_text": "Full=Periplasmic cystine-binding protein",
        "reviews": {
            "GO:0015276": (
                "The ligand-gated ion-channel annotation is an InterPro2GO spillover and is not appropriate for this bacterial periplasmic solute-binding protein.",
                "REMOVE",
                "FliY has a signal peptide and solute-binding protein family domains, with no evidence that it is a membrane ion channel; the ion-channel term appears to come from the ionotropic-glutamate-receptor-like domain mapping.",
                None,
                [support_uniprot("fliY", "Full=Periplasmic cystine-binding protein")],
            ),
            "GO:0016020": (
                "The membrane annotation is not the best location for a signal-peptide-bearing periplasmic cystine-binding protein.",
                "MODIFY",
                "UniProt predicts a signal peptide and mature chain for a periplasmic cystine-binding protein, so periplasmic space is the better location term.",
                [PERIPLASM],
                [support_uniprot("fliY", "FT   SIGNAL          1..27")],
            ),
            "GO:0034220": (
                "Monoatomic ion transmembrane transport is a downstream inference from the incorrect ion-channel annotation and should be replaced by cystine transport context.",
                "MODIFY",
                "The product name and local sctC-sctS-fliY locus support cystine/sulfur-compound solute binding for ABC transport, not monoatomic ion channel transport.",
                [CYSTINE_TRANSPORT],
                [support_uniprot("fliY", "Full=Periplasmic cystine-binding protein")],
            ),
        },
        "new_annotations": [
            {
                "term": PERIPLASM,
                "qualifier": "located_in",
                "summary": "Periplasmic space is the appropriate location for this predicted cystine-binding component.",
                "reason": "FliY is named as a periplasmic cystine-binding protein and has a predicted N-terminal signal peptide with a mature chain.",
                "supporting_text": "Full=Periplasmic cystine-binding protein",
            },
            {
                "term": CYSTINE_TRANSPORT,
                "qualifier": "involved_in",
                "summary": "L-cystine transport is a useful missing process annotation for this solute-binding component.",
                "reason": "The product name and adjacent SctC/SctS transporter components support a cystine/sulfur-compound ABC uptake role.",
                "supporting_text": "Full=Periplasmic cystine-binding protein",
            },
            {
                "term": CYSTINE_TRANSPORTER,
                "qualifier": "contributes_to",
                "summary": "FliY should be recorded as contributing to the L-cystine transporter activity of the adjacent ABC uptake system.",
                "reason": "As a periplasmic solute-binding protein, FliY likely supplies substrate-recognition capacity for the SctC/SctS transporter rather than catalyzing transport alone.",
                "supporting_text": "Full=Periplasmic cystine-binding protein",
            },
        ],
        "core": {
            "description": "Periplasmic cystine-binding component contributing substrate capture to a predicted ABC-type L-cystine uptake system.",
            "contributes_to_molecular_function": CYSTINE_TRANSPORTER,
            "directly_involved_in": [CYSTINE_TRANSPORT],
            "locations": [PERIPLASM],
            "support": ("GO:0015811", "L-cystine transport"),
            "support_in_goa": False,
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

    for ann in doc.get("existing_annotations", []):
        term = ann["term"]
        term_id = term["id"]
        label = term["label"]
        entry = cfg["reviews"][term_id]
        proposed = entry[3] if len(entry) > 3 else None
        extra_support = entry[4] if len(entry) > 4 else None
        asta_text = cfg["asta_text"] if term_id == cfg["core"]["support"][0] else None
        ann["review"] = review(
            gene,
            term_id,
            label,
            entry[0],
            entry[1],
            entry[2],
            asta_text=asta_text,
            proposed=proposed,
            extra_support=extra_support,
        )

    existing_term_ids = {ann["term"]["id"] for ann in doc.get("existing_annotations", [])}
    for extra in cfg.get("new_annotations", []):
        term = extra["term"]
        if term["id"] in existing_term_ids:
            continue
        doc.setdefault("existing_annotations", []).append(
            new_annotation(
                term,
                extra["qualifier"],
                uniprot_ref(gene),
                extra["summary"],
                extra["reason"],
                [
                    support_uniprot(gene, extra["supporting_text"]),
                    support_asta(gene, cfg["asta_text"]),
                ],
            )
        )

    core = dict(cfg["core"])
    support_term = core.pop("support")
    support_in_goa = core.pop("support_in_goa", True)
    core["supported_by"] = []
    if support_in_goa:
        core["supported_by"].append(support_goa(gene, support_term[0], support_term[1]))
    core["supported_by"].extend(
        [
            support_uniprot(gene, cfg["uniprot_text"]),
            support_asta(gene, cfg["asta_text"]),
        ]
    )
    doc["core_functions"] = [core]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": "Does the PP_0225-PP_0227 transporter import L-cystine specifically in P. putida KT2440, or does it accept additional sulfur-containing amino acids or related sulfur compounds?"
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": "Compare uptake and growth phenotypes of PP_0225-PP_0227 mutants on L-cystine, cysteine, and related sulfur-containing substrates under sulfur limitation.",
            "experiment_type": "targeted transporter mutant substrate-uptake and growth assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
