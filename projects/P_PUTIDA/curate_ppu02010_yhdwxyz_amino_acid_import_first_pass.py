#!/usr/bin/env python3
"""First-pass curation for the ppu02010 PP_1297-PP_1300 YhdWXYZ importer."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml


SPECIES = "PSEPK"
MODULE_PATH = Path("modules/yhdwxyz_amino_acid_abc_import_boundary.yaml")


AMINO_ACID_TRANSPORT = {"id": "GO:0006865", "label": "amino acid transport"}
AMINO_ACID_TRANSMEMBRANE_TRANSPORT = {
    "id": "GO:0003333",
    "label": "amino acid transmembrane transport",
}
ABC_AMINO_ACID = {"id": "GO:0015424", "label": "ABC-type amino acid transporter activity"}
AMINO_ACID_BINDING = {"id": "GO:0016597", "label": "amino acid binding"}
ATP_BINDING = {"id": "GO:0005524", "label": "ATP binding"}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
NUCLEOTIDE_BINDING = {"id": "GO:0000166", "label": "nucleotide binding"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}


CONFIG = {
    "yhdW": {
        "accession": "Q88NB5",
        "locus": "PP_1297",
        "role": "amino-acid ABC importer solute-binding component",
        "kind": "binding",
        "uniprot_text": "Full=Amino-acid ABC transporter-binding protein YhdW",
        "asta_text": "Protein Description:** SubName: Full=Amino-acid ABC transporter-binding protein YhdW",
        "family_text": "Belongs to the bacterial solute-binding protein 3 family.",
        "domain_text": "InterPro; IPR051455; Bact_solute-bind_prot3.",
        "panther_text": "AMINO-ACID ABC TRANSPORTER-BINDING PROTEIN YHDW-RELATED",
        "description": (
            "yhdW (PP_1297) encodes the predicted solute-binding component of the adjacent "
            "PP_1297-PP_1300 YhdWXYZ amino-acid ABC importer. Its product name, bacterial "
            "solute-binding protein 3 family assignment, signal peptide, and adjacency to the "
            "YhdX/YhdY permeases and YhdZ ABC ATPase support a substrate-recognition role in "
            "amino-acid uptake, while the exact transported amino acid remains unresolved."
        ),
    },
    "yhdX": {
        "accession": "Q88NB4",
        "locus": "PP_1298",
        "role": "amino-acid ABC importer permease",
        "kind": "permease",
        "uniprot_text": "Full=Amino acid ABC transporter-permease subunit",
        "asta_text": "Protein Description:** SubName: Full=Amino acid ABC transporter-permease subunit",
        "location_text": "Cell inner membrane",
        "family_text": "Belongs to the binding-protein-dependent transport system",
        "domain_text": "InterPro; IPR010065; AA_ABC_transptr_permease_3TM.",
        "panther_text": "MEMBRANE COMPONENT OF AMINO ACID ABC TRANSPORTER",
        "description": (
            "yhdX (PP_1298) encodes a predicted multi-pass inner-membrane permease subunit of "
            "the PP_1297-PP_1300 YhdWXYZ amino-acid ABC importer. UniProt and Asta identify it "
            "as a binding-protein-dependent amino-acid ABC transporter permease with MetI-like "
            "transporter features, supporting a membrane-channel role in ATP-driven amino-acid uptake."
        ),
    },
    "yhdY": {
        "accession": "Q88NB3",
        "locus": "PP_1299",
        "role": "amino-acid ABC importer permease",
        "kind": "permease",
        "uniprot_text": "Full=Amino acid ABC transporter-membrane subunit",
        "asta_text": "Protein Description:** SubName: Full=Amino acid ABC transporter-membrane subunit",
        "location_text": "Cell inner membrane",
        "family_text": "Belongs to the binding-protein-dependent transport system",
        "domain_text": "InterPro; IPR010065; AA_ABC_transptr_permease_3TM.",
        "panther_text": "MEMBRANE COMPONENT OF AMINO ACID ABC TRANSPORTER",
        "description": (
            "yhdY (PP_1299) encodes the second predicted multi-pass inner-membrane permease "
            "subunit of the PP_1297-PP_1300 YhdWXYZ amino-acid ABC importer. Its binding-"
            "protein-dependent transporter family assignment, amino-acid ABC transporter "
            "product name, and adjacency to yhdW, yhdX, and yhdZ support a membrane-channel "
            "role in the same unresolved-substrate amino-acid uptake system."
        ),
    },
    "yhdZ": {
        "accession": "Q88NB2",
        "locus": "PP_1300",
        "role": "amino-acid ABC importer ATP-binding subunit",
        "kind": "atpase",
        "uniprot_text": "Full=Amino acid ABC transporter-ATP-binding subunit",
        "asta_text": "Protein Description:** SubName: Full=Amino acid ABC transporter-ATP-binding subunit",
        "location_text": "Cell inner membrane",
        "family_text": "Belongs to the ABC transporter superfamily.",
        "domain_text": "InterPro; IPR030679; ABC_ATPase_HisP-typ.",
        "panther_text": "AMINO ACID IMPORT ATP-BINDING PROTEIN",
        "description": (
            "yhdZ (PP_1300) encodes the ATP-binding energy-coupling subunit of the adjacent "
            "PP_1297-PP_1300 YhdWXYZ amino-acid ABC importer. Its ABC ATPase domains, ATP "
            "binding and ATP hydrolysis annotations, amino-acid-import ATP-binding protein "
            "family assignment, and local pairing with YhdW/YhdX/YhdY support ATP-driven "
            "amino-acid transmembrane uptake."
        ),
    },
}


def go_term(term: dict) -> dict:
    return {"id": term["id"], "label": term["label"]}


def review_path(gene: str) -> Path:
    return Path("genes") / SPECIES / gene / f"{gene}-ai-review.yaml"


def ref(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def support_goa(gene: str, term_id: str, label: str) -> dict:
    return {"reference_id": ref(gene, "goa.tsv"), "supporting_text": f"{term_id}\t{label}"}


def support_uniprot(gene: str, text: str) -> dict:
    return {"reference_id": ref(gene, "uniprot.txt"), "supporting_text": text}


def support_asta(gene: str, text: str) -> dict:
    return {"reference_id": ref(gene, "deep-research-asta.md"), "supporting_text": text}


def ensure_reference(doc: dict, ref_id: str, title: str, supporting_text: str | None = None) -> None:
    refs = doc.setdefault("references", [])
    for entry in refs:
        if entry.get("id") == ref_id:
            if supporting_text and not entry.get("findings"):
                entry["findings"] = [{"supporting_text": supporting_text}]
            return
    entry = {"id": ref_id, "title": title, "findings": []}
    if supporting_text:
        entry["findings"].append({"supporting_text": supporting_text})
    refs.append(entry)


def review(
    gene: str,
    term_id: str,
    label: str,
    summary: str,
    action: str,
    reason: str,
    *,
    proposed: list[dict] | None = None,
    extra_support: list[dict] | None = None,
) -> dict:
    supported_by = [support_goa(gene, term_id, label)]
    if extra_support:
        supported_by.extend(extra_support)
    result = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        result["proposed_replacement_terms"] = deepcopy(proposed)
    return result


def new_annotation(
    gene: str,
    term: dict,
    qualifier: str,
    summary: str,
    reason: str,
    supporting_texts: list[str],
) -> dict:
    return {
        "term": go_term(term),
        "evidence_type": "IEA",
        "original_reference_id": ref(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": [
                *(support_uniprot(gene, text) for text in supporting_texts),
                support_asta(gene, CONFIG[gene]["asta_text"]),
            ],
        },
    }


def binding_reviews(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    if term_id == "GO:0006865":
        return review(
            gene,
            term_id,
            label,
            "Amino acid transport is appropriate for this predicted YhdWXYZ substrate-binding component, but the transporter context is more specifically transmembrane import.",
            "MODIFY",
            "YhdW is named as an amino-acid ABC transporter binding protein and has bacterial solute-binding protein domains; the adjacent YhdX/YhdY/YhdZ components support amino acid transmembrane transport as the better process term for the importer.",
            proposed=[go_term(AMINO_ACID_TRANSMEMBRANE_TRANSPORT)],
            extra_support=[
                support_uniprot(gene, cfg["uniprot_text"]),
                support_uniprot(gene, cfg["family_text"]),
                support_uniprot(gene, cfg["domain_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        )
    raise ValueError(f"Unhandled binding annotation for {gene}: {term_id} {label}")


def permease_reviews(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["uniprot_text"])
    asta = support_asta(gene, cfg["asta_text"])
    if term_id == "GO:0005886":
        return review(
            gene,
            term_id,
            label,
            "Plasma membrane localization is appropriate for this predicted inner-membrane amino-acid ABC permease.",
            "ACCEPT",
            "UniProt places this binding-protein-dependent transporter permease at the bacterial cell inner membrane.",
            extra_support=[support_uniprot(gene, cfg["location_text"]), product, asta],
        )
    if term_id == "GO:0006865":
        return review(
            gene,
            term_id,
            label,
            "Amino acid transport is correct but broad for this membrane permease.",
            "MODIFY",
            "The product name, inner-membrane localization, and amino-acid ABC transporter family context support amino acid transmembrane transport as the more specific process.",
            proposed=[go_term(AMINO_ACID_TRANSMEMBRANE_TRANSPORT)],
            extra_support=[product, support_uniprot(gene, cfg["panther_text"]), asta],
        )
    if term_id == "GO:0016020":
        return review(
            gene,
            term_id,
            label,
            "Membrane localization is correct but less informative than plasma membrane for this bacterial inner-membrane permease.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also has a plasma-membrane annotation and UniProt resolves this permease to the cell inner membrane.",
            extra_support=[support_uniprot(gene, cfg["location_text"]), product],
        )
    if term_id == "GO:0022857":
        return review(
            gene,
            term_id,
            label,
            "Generic transmembrane transporter activity is too broad for this ABC-transporter permease component.",
            "MODIFY",
            "The YhdX/YhdY proteins are binding-protein-dependent transporter permeases in an amino-acid ABC importer, so ABC-type amino-acid transporter activity is the better complex-level activity.",
            proposed=[go_term(ABC_AMINO_ACID)],
            extra_support=[product, support_uniprot(gene, cfg["domain_text"]), support_uniprot(gene, cfg["panther_text"]), asta],
        )
    if term_id == "GO:0043190":
        return review(
            gene,
            term_id,
            label,
            "ABC transporter complex membership is appropriate for this YhdWXYZ permease.",
            "ACCEPT",
            "The product name, binding-protein-dependent transporter family, and local PP_1297-PP_1300 locus support an ABC-importer permease role.",
            extra_support=[product, support_uniprot(gene, cfg["family_text"]), support_uniprot(gene, cfg["domain_text"]), asta],
        )
    if term_id == "GO:0055085":
        return review(
            gene,
            term_id,
            label,
            "Transmembrane transport is true but broad relative to amino-acid transmembrane transport.",
            "MODIFY",
            "The amino-acid ABC transporter product and family annotations support amino acid transmembrane transport as the more informative biological-process term.",
            proposed=[go_term(AMINO_ACID_TRANSMEMBRANE_TRANSPORT)],
            extra_support=[product, support_uniprot(gene, cfg["panther_text"]), asta],
        )
    raise ValueError(f"Unhandled permease annotation for {gene}: {term_id} {label}")


def atpase_reviews(gene: str, cfg: dict, term_id: str, label: str) -> dict:
    product = support_uniprot(gene, cfg["uniprot_text"])
    asta = support_asta(gene, cfg["asta_text"])
    if term_id == "GO:0000166":
        return review(
            gene,
            term_id,
            label,
            "Generic nucleotide binding is over-broad for this ABC ATP-binding subunit.",
            "MARK_AS_OVER_ANNOTATED",
            "The review retains the more specific ATP binding and ATP hydrolysis annotations for the YhdZ ABC ATPase.",
            extra_support=[product, support_uniprot(gene, cfg["domain_text"]), asta],
        )
    if term_id == "GO:0003333":
        return review(
            gene,
            term_id,
            label,
            "Amino acid transmembrane transport is appropriate process context for the YhdZ ATP-binding component.",
            "ACCEPT",
            "UniProt and Asta identify YhdZ as an amino-acid ABC transporter ATP-binding subunit, consistent with ATP-coupled amino-acid uptake by the PP_1297-PP_1300 locus.",
            extra_support=[product, support_uniprot(gene, cfg["panther_text"]), asta],
        )
    if term_id == "GO:0005524":
        return review(
            gene,
            term_id,
            label,
            "ATP binding is appropriate for this ABC ATPase but is not the most informative core activity.",
            "KEEP_AS_NON_CORE",
            "YhdZ is the ATP-binding energy-coupling component of the predicted YhdWXYZ importer; ATP hydrolysis captures the mechanistic activity more directly.",
            extra_support=[product, support_uniprot(gene, cfg["domain_text"]), asta],
        )
    if term_id == "GO:0005886":
        return review(
            gene,
            term_id,
            label,
            "Plasma membrane localization is appropriate for this inner-membrane-associated ABC ATPase.",
            "ACCEPT",
            "UniProt places YhdZ at the cell inner membrane.",
            extra_support=[support_uniprot(gene, cfg["location_text"]), product, asta],
        )
    if term_id == "GO:0015424":
        return review(
            gene,
            term_id,
            label,
            "ABC-type amino acid transporter activity is appropriate as the complex-level activity to which YhdZ contributes.",
            "ACCEPT",
            "YhdZ is named as an amino-acid ABC transporter ATP-binding subunit and carries an amino-acid import ATP-binding protein family assignment.",
            extra_support=[product, support_uniprot(gene, cfg["panther_text"]), asta],
        )
    if term_id == "GO:0016887":
        return review(
            gene,
            term_id,
            label,
            "ATP hydrolysis activity is appropriate for this ABC ATP-binding energy-coupling subunit.",
            "ACCEPT",
            "YhdZ has ABC transporter ATPase domains and is the predicted energy-coupling subunit of the YhdWXYZ amino-acid importer.",
            extra_support=[product, support_uniprot(gene, cfg["family_text"]), support_uniprot(gene, cfg["domain_text"]), asta],
        )
    raise ValueError(f"Unhandled ATPase annotation for {gene}: {term_id} {label}")


def extra_annotations(gene: str, cfg: dict) -> list[dict]:
    if cfg["kind"] == "binding":
        return [
            new_annotation(
                gene,
                AMINO_ACID_BINDING,
                "enables",
                "Amino acid binding captures the expected substrate-recognition role of YhdW.",
                "YhdW is named as an amino-acid ABC transporter binding protein and belongs to bacterial solute-binding protein family 3.",
                [cfg["uniprot_text"], cfg["family_text"], cfg["domain_text"], cfg["panther_text"]],
            ),
            new_annotation(
                gene,
                AMINO_ACID_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                "Amino acid transmembrane transport is a useful process annotation for the YhdWXYZ binding component.",
                "YhdW is the predicted solute-binding protein in the adjacent YhdWXYZ amino-acid ABC importer locus.",
                [cfg["uniprot_text"], cfg["panther_text"]],
            ),
            new_annotation(
                gene,
                ABC_AMINO_ACID,
                "contributes_to",
                "YhdW should be recorded as contributing substrate recognition to ABC-type amino acid transporter activity.",
                "The solute-binding component supplies substrate capture rather than independently catalyzing membrane transport.",
                [cfg["uniprot_text"], cfg["panther_text"]],
            ),
            new_annotation(
                gene,
                ABC_COMPLEX,
                "part_of",
                "ABC transporter complex membership is appropriate for the YhdW substrate-binding component.",
                "The product name and local YhdWXYZ locus identify YhdW as the binding component of an amino-acid ABC importer.",
                [cfg["uniprot_text"], cfg["family_text"]],
            ),
        ]
    if cfg["kind"] == "permease":
        return [
            new_annotation(
                gene,
                AMINO_ACID_TRANSMEMBRANE_TRANSPORT,
                "involved_in",
                f"Amino acid transmembrane transport is a useful missing process annotation for {gene}.",
                f"{gene} is an inner-membrane permease of a predicted amino-acid ABC importer.",
                [cfg["uniprot_text"], cfg["location_text"], cfg["panther_text"]],
            ),
            new_annotation(
                gene,
                ABC_AMINO_ACID,
                "contributes_to",
                f"{gene} should be recorded as contributing to ABC-type amino acid transporter activity.",
                "As a permease subunit, the protein contributes to the transporter complex rather than functioning as a complete transporter alone.",
                [cfg["uniprot_text"], cfg["domain_text"], cfg["panther_text"]],
            ),
        ]
    return [
        new_annotation(
            gene,
            ABC_COMPLEX,
            "part_of",
            "ABC transporter complex membership is appropriate for the YhdZ ATP-binding component.",
            "YhdZ is the ATP-binding subunit of the adjacent predicted YhdWXYZ amino-acid ABC importer.",
            [cfg["uniprot_text"], cfg["panther_text"]],
        )
    ]


def core_function(gene: str, cfg: dict) -> dict:
    common_support = [support_uniprot(gene, cfg["uniprot_text"]), support_asta(gene, cfg["asta_text"])]
    if cfg["kind"] == "binding":
        return {
            "description": "Substrate-binding component contributing amino-acid recognition to the predicted YhdWXYZ ABC uptake system.",
            "molecular_function": go_term(AMINO_ACID_BINDING),
            "contributes_to_molecular_function": go_term(ABC_AMINO_ACID),
            "directly_involved_in": [go_term(AMINO_ACID_TRANSMEMBRANE_TRANSPORT)],
            "in_complex": go_term(ABC_COMPLEX),
            "supported_by": [
                support_uniprot(gene, cfg["uniprot_text"]),
                support_uniprot(gene, cfg["family_text"]),
                support_uniprot(gene, cfg["panther_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    if cfg["kind"] == "permease":
        return {
            "description": "Multi-pass permease component contributing to the predicted YhdWXYZ amino-acid ABC uptake system.",
            "contributes_to_molecular_function": go_term(ABC_AMINO_ACID),
            "directly_involved_in": [go_term(AMINO_ACID_TRANSMEMBRANE_TRANSPORT)],
            "locations": [go_term(PLASMA_MEMBRANE)],
            "in_complex": go_term(ABC_COMPLEX),
            "supported_by": [
                support_goa(gene, "GO:0043190", ABC_COMPLEX["label"]),
                support_uniprot(gene, cfg["uniprot_text"]),
                support_uniprot(gene, cfg["location_text"]),
                support_asta(gene, cfg["asta_text"]),
            ],
        }
    return {
        "description": "ATP-binding energy-coupling subunit of the predicted YhdWXYZ amino-acid ABC uptake system.",
        "molecular_function": go_term(ATP_HYDROLYSIS),
        "contributes_to_molecular_function": go_term(ABC_AMINO_ACID),
        "directly_involved_in": [go_term(AMINO_ACID_TRANSMEMBRANE_TRANSPORT)],
        "locations": [go_term(PLASMA_MEMBRANE)],
        "in_complex": go_term(ABC_COMPLEX),
        "supported_by": [
            support_goa(gene, "GO:0016887", ATP_HYDROLYSIS["label"]),
            support_goa(gene, "GO:0015424", ABC_AMINO_ACID["label"]),
            *common_support,
            support_uniprot(gene, cfg["domain_text"]),
        ],
    }


def curate_gene(gene: str, cfg: dict) -> None:
    path = review_path(gene)
    doc = yaml.safe_load(path.read_text())
    doc["status"] = "COMPLETE"
    doc["gene_symbol"] = gene
    doc["description"] = cfg["description"]

    for annotation in doc.get("existing_annotations", []):
        term = annotation["term"]
        term_id = term["id"]
        label = term["label"]
        if cfg["kind"] == "binding":
            annotation["review"] = binding_reviews(gene, cfg, term_id, label)
        elif cfg["kind"] == "permease":
            annotation["review"] = permease_reviews(gene, cfg, term_id, label)
        elif cfg["kind"] == "atpase":
            annotation["review"] = atpase_reviews(gene, cfg, term_id, label)
        else:
            raise ValueError(f"Unhandled gene kind for {gene}: {cfg['kind']}")

    existing_term_ids = {annotation["term"]["id"] for annotation in doc.get("existing_annotations", [])}
    for annotation in extra_annotations(gene, cfg):
        term_id = annotation["term"]["id"]
        if term_id not in existing_term_ids:
            doc.setdefault("existing_annotations", []).append(annotation)
            existing_term_ids.add(term_id)

    ensure_reference(doc, ref(gene, "goa.tsv"), f"QuickGO GOA annotations for {gene}")
    ensure_reference(
        doc,
        ref(gene, "uniprot.txt"),
        f"UniProtKB entry for {gene} ({cfg['accession']})",
        cfg["uniprot_text"],
    )
    ensure_reference(
        doc,
        ref(gene, "deep-research-asta.md"),
        f"Asta retrieval report for {gene} ({cfg['accession']})",
        cfg["asta_text"],
    )

    doc["core_functions"] = [core_function(gene, cfg)]
    doc["proposed_new_terms"] = []
    doc["suggested_questions"] = [
        {
            "question": (
                "What is the exact substrate specificity of the PP_1297-PP_1300 YhdWXYZ ABC importer, and does it "
                "prefer one amino acid or a broader class of amino acids?"
            )
        }
    ]
    doc["suggested_experiments"] = [
        {
            "description": (
                f"Measure amino-acid uptake and growth phenotypes for a {gene} deletion or depletion strain across a "
                "panel of individual amino acids, then compare with complementation by the intact PP_1297-PP_1300 locus."
            ),
            "experiment_type": "targeted ABC-importer mutant substrate-uptake and growth assay",
        }
    ]

    path.write_text(yaml.safe_dump(doc, sort_keys=False, width=120))
    print(f"curated {path}")


def preferred(term: dict, preferred_term: str | None = None, description: str | None = None) -> dict:
    entry = {"preferred_term": preferred_term or term["label"], "term": go_term(term)}
    if description:
        entry["description"] = description
    return entry


def annoton(gene: str, cfg: dict) -> dict:
    base = {
        "id": f"{gene}_yhdwxyz_amino_acid_import_annoton",
        "label": f"{gene}: {cfg['role']}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "processes": [preferred(AMINO_ACID_TRANSMEMBRANE_TRANSPORT)],
        "role_description": cfg["role"].capitalize() + ".",
    }
    if cfg["kind"] == "binding":
        base["function"] = preferred(AMINO_ACID_BINDING)
    elif cfg["kind"] == "permease":
        base["function"] = preferred(ABC_AMINO_ACID, "contributes to ABC-type amino acid transporter activity")
        base["locations"] = [preferred(PLASMA_MEMBRANE)]
    else:
        base["function"] = preferred(ATP_HYDROLYSIS)
        base["locations"] = [preferred(PLASMA_MEMBRANE)]
    return base


def module_evidence() -> list[dict]:
    evidence = [
        {
            "source_id": "KEGG:ppu02010",
            "title": "ABC transporters - Pseudomonas putida KT2440",
            "statement": (
                "KEGG ppu02010 contributes PP_1297-PP_1300 as a coherent amino-acid ABC-transporter "
                "sub-batch within the broad ABC-transporter umbrella map."
            ),
        },
        {
            "source_id": "file:projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv",
            "title": "PSEPK ppu02010 ABC-transporter partition batch",
            "statement": (
                "The ppu02010 partition batch records cluster C26 as yhdW, yhdX, yhdY, and yhdZ after "
                "first-pass curation."
            ),
        },
    ]
    for gene, cfg in CONFIG.items():
        evidence.append(
            {
                "source_id": f"UniProtKB:{cfg['accession']}",
                "title": f"{gene} {cfg['role']}",
                "statement": (
                    f"UniProt records {gene} ({cfg['locus']}) as {cfg['uniprot_text'].removeprefix('Full=')}."
                ),
            }
        )
    return evidence


def curate_module() -> None:
    doc = {
        "id": "MODULE:yhdwxyz_amino_acid_abc_import_boundary",
        "title": "YhdWXYZ amino-acid ABC import boundary",
        "description": (
            "Boundary module for the Pseudomonas putida KT2440 PP_1297-PP_1300 YhdWXYZ amino-acid ABC "
            "importer pulled from the KEGG ppu02010 ABC-transporter umbrella map. YhdW is the predicted "
            "solute-binding component, YhdX and YhdY are inner-membrane permeases, and YhdZ is the ABC "
            "ATP-binding energy-coupling subunit. The module records a coherent predicted amino-acid uptake "
            "system while leaving the exact amino-acid substrate unresolved."
        ),
        "status": "DRAFT",
        "evidence": module_evidence(),
        "module": {
            "id": "yhdwxyz_amino_acid_abc_import_boundary",
            "label": "YhdWXYZ amino-acid ABC import boundary",
            "module_type": "TRANSPORT_STEP",
            "concepts": [
                preferred(
                    AMINO_ACID_TRANSMEMBRANE_TRANSPORT,
                    description="ATP-dependent uptake of an unresolved amino-acid substrate across the bacterial inner membrane.",
                ),
                preferred(AMINO_ACID_TRANSPORT, description="General amino-acid transport context for the solute-binding component."),
                preferred(AMINO_ACID_BINDING, description="Substrate recognition by the YhdW solute-binding component."),
                preferred(ABC_AMINO_ACID, description="Complex-level ABC-type amino acid transporter activity."),
                preferred(ATP_HYDROLYSIS, description="ATP hydrolysis by the YhdZ energy-coupling subunit."),
                preferred(ABC_COMPLEX, description="Multi-component ABC transporter complex containing binding, permease, and ATPase subunits."),
            ],
            "context": {
                "cellular_components": [
                    preferred(
                        PLASMA_MEMBRANE,
                        "bacterial plasma membrane",
                        "YhdX and YhdY are predicted inner-membrane permeases and YhdZ is inner-membrane-associated.",
                    )
                ]
            },
            "parts": [
                {
                    "order": 1,
                    "role": "YhdWXYZ amino-acid ABC import",
                    "node": {
                        "id": "yhdwxyz_amino_acid_abc_import",
                        "label": "PP_1297-PP_1300 YhdWXYZ amino-acid ABC import",
                        "module_type": "TRANSPORT_STEP",
                        "description": (
                            "The PP_1297-PP_1300 locus encodes a predicted amino-acid ABC importer. YhdW is the "
                            "solute-binding component, YhdX and YhdY are membrane permeases, and YhdZ supplies "
                            "ATP-dependent energy coupling. Current UniProt, GOA, and Asta evidence supports "
                            "amino-acid import but does not resolve the exact substrate."
                        ),
                        "concepts": [
                            preferred(AMINO_ACID_TRANSMEMBRANE_TRANSPORT),
                            preferred(ABC_AMINO_ACID),
                            preferred(AMINO_ACID_BINDING),
                        ],
                        "annotons": [annoton(gene, CONFIG[gene]) for gene in ["yhdW", "yhdX", "yhdY", "yhdZ"]],
                    },
                }
            ],
        },
        "notes": (
            "This boundary module records ppu02010 cluster C26 as a complete predicted amino-acid ABC importer. "
            "It is kept separate from the glutamate/aspartate, branched-chain amino-acid, arginine/ornithine, "
            "His/ArgT, methionine, and cystine/sulfur-compound importer modules because the exact YhdWXYZ substrate "
            "specificity is unresolved in the first-pass evidence."
        ),
    }
    MODULE_PATH.write_text(yaml.safe_dump(doc, sort_keys=False, width=120))
    print(f"updated {MODULE_PATH}")


def main() -> None:
    for gene, cfg in CONFIG.items():
        curate_gene(gene, cfg)
    curate_module()


if __name__ == "__main__":
    main()
