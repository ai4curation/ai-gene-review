#!/usr/bin/env python3
"""First-pass curation for ppu02024 peptide/opine/glutathione ABC import genes."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
SPECIES = "PSEPK"
GENE_ROOT = ROOT / "genes" / SPECIES


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

DIPEPTIDE_TRANSPORT = {"id": "GO:0042938", "label": "dipeptide transport"}
DIPEPTIDE_TRANSMEMBRANE_TRANSPORT = {"id": "GO:0035442", "label": "dipeptide transmembrane transport"}
DIPEPTIDE_TRANSPORTER = {"id": "GO:0071916", "label": "dipeptide transmembrane transporter activity"}
GLUTATHIONE_TRANSPORT = {"id": "GO:0034635", "label": "glutathione transport"}
GLUTATHIONE_TRANSPORTER = {"id": "GO:0034634", "label": "glutathione transmembrane transporter activity"}
PEPTIDE_TRANSPORT = {"id": "GO:0015833", "label": "peptide transport"}
PEPTIDE_TRANSPORTER = {"id": "GO:1904680", "label": "peptide transmembrane transporter activity"}
TRANSMEMBRANE_TRANSPORT = {"id": "GO:0055085", "label": "transmembrane transport"}
TRANSMEMBRANE_TRANSPORTER = {"id": "GO:0022857", "label": "transmembrane transporter activity"}
ABC_COMPLEX = {"id": "GO:0043190", "label": "ATP-binding cassette (ABC) transporter complex"}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}


GENES = {
    "PP_3220": {
        "accession": "Q88HY3",
        "symbol": "PP_3220",
        "group": "dipeptide",
        "kind": "atpase",
        "description": (
            "PP_3220 encodes the ATP-binding energy-coupling subunit of a predicted "
            "dipeptide ABC import system in Pseudomonas putida KT2440. The reviewed "
            "UniProt product name assigns ABC-type dipeptide transporter activity "
            "(EC 7.4.2.9), and the adjacent PP_3221/PP_3222 permeases plus PP_3223 "
            "periplasmic binding protein support a compact peptide-import locus."
        ),
        "product_quote": "DE   RecName: Full=ABC-type dipeptide transporter",
        "domain_quote": "DR   InterPro; IPR050319; ABC_transp_ATP-bind.",
        "location_quote": "CC   -!- SUBCELLULAR LOCATION: Cell inner membrane",
        "asta_quote": "- **Protein Description:** RecName: Full=ABC-type dipeptide transporter",
    },
    "PP_3221": {
        "accession": "Q88HY2",
        "symbol": "PP_3221",
        "group": "dipeptide",
        "kind": "permease",
        "description": (
            "PP_3221 encodes a multi-pass membrane permease subunit of the predicted "
            "PP_3220-PP_3223 dipeptide ABC importer in Pseudomonas putida KT2440. Its "
            "binding-protein-dependent transporter permease domains and membrane "
            "topology support a channel-subunit role, with dipeptide specificity inferred "
            "from the adjacent PP_3220 ATPase product name."
        ),
        "product_quote": "DE   SubName: Full=ABC transporter, permease protein",
        "domain_quote": "DR   InterPro; IPR050366; BP-dependent_transpt_permease.",
        "location_quote": "CC   -!- SUBCELLULAR LOCATION: Cell membrane",
        "tm_quote": "FT   TRANSMEM        45..65",
        "asta_quote": "- **Protein Description:** SubName: Full=ABC transporter, permease protein",
    },
    "PP_3222": {
        "accession": "Q88HY1",
        "symbol": "PP_3222",
        "group": "dipeptide",
        "kind": "permease",
        "description": (
            "PP_3222 encodes a second multi-pass membrane permease subunit of the predicted "
            "PP_3220-PP_3223 dipeptide ABC importer in Pseudomonas putida KT2440. It has "
            "MetI-like binding-protein-dependent transporter domains and is best curated "
            "as contributing to the membrane transport activity of the local dipeptide "
            "ABC import system."
        ),
        "product_quote": "DE   SubName: Full=ABC transporter, permease protein",
        "domain_quote": "DR   InterPro; IPR045621; BPD_transp_1_N.",
        "location_quote": "CC   -!- SUBCELLULAR LOCATION: Cell membrane",
        "tm_quote": "FT   TRANSMEM        12..30",
        "asta_quote": "- **Protein Description:** SubName: Full=ABC transporter, permease protein",
    },
    "PP_3223": {
        "accession": "Q88HY0",
        "symbol": "PP_3223",
        "group": "dipeptide",
        "kind": "binding",
        "description": (
            "PP_3223 encodes a predicted periplasmic solute-binding component of the "
            "PP_3220-PP_3223 dipeptide ABC importer in Pseudomonas putida KT2440. Its "
            "SBP_5/peptide-binding domains, peptide transport annotations, and local "
            "dipeptide transporter ATPase support a substrate-capture role for a "
            "dipeptide-like ABC import system."
        ),
        "product_quote": "DE   SubName: Full=ABC transporter, periplasmic binding protein",
        "domain_quote": "DR   InterPro; IPR030678; Peptide/Ni-bd.",
        "signal_quote": "KW   Signal {ECO:0000256|ARBA:ARBA00022729};",
        "location_quote": "CC   -!- SUBCELLULAR LOCATION: Cell envelope",
        "asta_quote": "- **Protein Description:** SubName: Full=ABC transporter, periplasmic binding protein",
    },
    "gsiA": {
        "accession": "Q88EK9",
        "symbol": "gsiA",
        "group": "glutathione",
        "kind": "atpase",
        "description": (
            "gsiA encodes the ATP-binding energy-coupling subunit of a predicted "
            "glutathione/opine-like ABC import system in Pseudomonas putida KT2440. "
            "The UniProt product name supports glutathione import ATPase function "
            "(EC 7.4.2.10), although the neighboring locus also contains opine-named "
            "permease and binding-protein components, leaving substrate range unresolved."
        ),
        "product_quote": "DE   RecName: Full=Glutathione import ATP-binding protein GsiA",
        "domain_quote": "DR   InterPro; IPR050319; ABC_transp_ATP-bind.",
        "location_quote": "CC   -!- SUBCELLULAR LOCATION: Cell inner membrane",
        "asta_quote": "- **Protein Description:** RecName: Full=Glutathione import ATP-binding protein GsiA",
    },
    "PP_4454": {
        "accession": "Q88EK8",
        "symbol": "PP_4454",
        "group": "opine_like",
        "kind": "permease",
        "description": (
            "PP_4454 encodes a predicted multi-pass permease subunit of an opine/glutathione-like "
            "ABC import locus in Pseudomonas putida KT2440. UniProt names it as an opine "
            "ABC transporter permease, while adjacent gsiA and gsiC are glutathione-import "
            "subunits; this first pass therefore keeps the exact transported substrate range "
            "as unresolved."
        ),
        "product_quote": "DE   SubName: Full=Opine ABC transporter, permease protein",
        "domain_quote": "DR   InterPro; IPR050366; BP-dependent_transpt_permease.",
        "location_quote": "CC   -!- SUBCELLULAR LOCATION: Cell membrane",
        "tm_quote": "FT   TRANSMEM        24..48",
        "asta_quote": "- **Protein Description:** SubName: Full=Opine ABC transporter, permease protein",
    },
    "gsiC": {
        "accession": "Q88EK7",
        "symbol": "gsiC",
        "group": "glutathione",
        "kind": "permease",
        "description": (
            "gsiC encodes a predicted multi-pass permease subunit of a glutathione ABC import "
            "system in Pseudomonas putida KT2440. Its product name, MetI-like permease "
            "domains, and adjacency to gsiA support a membrane-channel role in a "
            "glutathione/opine-like ABC importer."
        ),
        "product_quote": "DE   SubName: Full=Glutathione ABC transporter permease subunit",
        "domain_quote": "DR   InterPro; IPR045621; BPD_transp_1_N.",
        "location_quote": "CC   -!- SUBCELLULAR LOCATION: Cell membrane",
        "tm_quote": "FT   TRANSMEM        9..30",
        "asta_quote": "- **Protein Description:** SubName: Full=Glutathione ABC transporter permease subunit",
    },
    "PP_4458": {
        "accession": "Q88EK4",
        "symbol": "PP_4458",
        "group": "opine_like",
        "kind": "binding",
        "description": (
            "PP_4458 encodes a predicted signal-peptide-bearing periplasmic binding component "
            "of an opine/glutathione-like ABC import locus in Pseudomonas putida KT2440. "
            "UniProt names it as an opine ABC transporter binding protein and records "
            "SBP_5/peptide-binding domains; the exact ligand range remains unresolved."
        ),
        "product_quote": "DE   SubName: Full=Opine ABC transporter, periplasmic binding protein",
        "domain_quote": "DR   InterPro; IPR030678; Peptide/Ni-bd.",
        "signal_quote": "FT   SIGNAL          1..28",
        "asta_quote": "- **Protein Description:** SubName: Full=Opine ABC transporter, periplasmic binding protein",
    },
}


def file_ref(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def ref(reference_id: str, text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": text}


def review(summary: str, action: str, reason: str, supported_by: list[dict[str, str]], proposed: list[dict] | None = None) -> dict:
    out = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        out["proposed_replacement_terms"] = proposed
    return out


def goa_rows(gene: str) -> dict[str, dict[str, str]]:
    with (GENE_ROOT / gene / f"{gene}-goa.tsv").open(encoding="utf-8") as handle:
        return {row["GO TERM"]: row for row in csv.DictReader(handle, delimiter="\t")}


def goa_quote(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def process_term(cfg: dict) -> dict[str, str]:
    if cfg["group"] == "dipeptide":
        return DIPEPTIDE_TRANSMEMBRANE_TRANSPORT
    if cfg["group"] == "glutathione":
        return GLUTATHIONE_TRANSPORT
    return TRANSMEMBRANE_TRANSPORT


def activity_term(cfg: dict) -> dict[str, str]:
    if cfg["group"] == "dipeptide":
        return DIPEPTIDE_TRANSPORTER
    if cfg["group"] == "glutathione":
        return GLUTATHIONE_TRANSPORTER
    if cfg["kind"] == "binding":
        return PEPTIDE_TRANSPORTER
    return TRANSMEMBRANE_TRANSPORTER


def ensure_references(data: dict, gene: str, cfg: dict) -> None:
    refs = {entry["id"]: entry for entry in data.get("references", [])}
    for ref_id, title in GO_REF_TITLES.items():
        refs.setdefault(ref_id, {"id": ref_id, "title": title, "findings": []})

    findings = [
        {
            "statement": "UniProt product naming supports the first-pass transporter-subunit assignment.",
            "supporting_text": cfg["product_quote"],
        },
        {
            "statement": "Domain annotation supports the ABC importer subunit role.",
            "supporting_text": cfg["domain_quote"],
        },
    ]
    if cfg["kind"] == "atpase":
        findings.append(
            {
                "statement": "Subcellular-location annotation supports association with the inner-membrane transporter complex.",
                "supporting_text": cfg["location_quote"],
            }
        )
    elif cfg["kind"] == "permease":
        findings.extend(
            [
                {
                    "statement": "Subcellular-location annotation supports a membrane permease role.",
                    "supporting_text": cfg["location_quote"],
                },
                {
                    "statement": "Predicted transmembrane helices support a membrane-channel subunit role.",
                    "supporting_text": cfg["tm_quote"],
                },
            ]
        )
    else:
        findings.append(
            {
                "statement": "Signal or envelope localization supports an extracytoplasmic solute-binding component.",
                "supporting_text": cfg["signal_quote"],
            }
        )

    refs[file_ref(gene, "goa.tsv")] = {
        "id": file_ref(gene, "goa.tsv"),
        "title": f"QuickGO/GOA annotation table for {gene} in Pseudomonas putida KT2440",
        "findings": [],
    }
    refs[file_ref(gene, "uniprot.txt")] = {
        "id": file_ref(gene, "uniprot.txt"),
        "title": f"UniProt record {cfg['accession']} for {gene} in Pseudomonas putida KT2440",
        "findings": findings,
    }
    refs[file_ref(gene, "deep-research-asta.md")] = {
        "id": file_ref(gene, "deep-research-asta.md"),
        "title": f"Asta retrieval report for {gene} in Pseudomonas putida KT2440",
        "findings": [
            {
                "statement": "Asta retrieval was checked for this first pass and recapitulates the UniProt product assignment.",
                "supporting_text": cfg["asta_quote"],
            }
        ],
    }
    data["references"] = list(refs.values())


def support(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> list[dict[str, str]]:
    evidence = [
        ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
        ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
        ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
        ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
    ]
    if cfg["kind"] == "atpase":
        evidence.append(ref(file_ref(gene, "uniprot.txt"), cfg["location_quote"]))
    elif cfg["kind"] == "permease":
        evidence.append(ref(file_ref(gene, "uniprot.txt"), cfg["tm_quote"]))
    else:
        evidence.append(ref(file_ref(gene, "uniprot.txt"), cfg["signal_quote"]))
    return evidence


def atpase_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    term = process_term(cfg)
    if go_id == "GO:0000166":
        return review(
            "Nucleotide binding is true but less informative than ATP binding and ABC transporter ATPase context.",
            "MARK_AS_OVER_ANNOTATED",
            "The ABC transporter ATP-binding domains support nucleotide binding, but this generic term should not be treated as the core function.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0005524":
        return review(
            "ATP binding is correct for the ABC ATP-binding subunit.",
            "KEEP_AS_NON_CORE",
            "ATP binding is a necessary mechanistic property, but the transporter substrate/process context is more informative for the core function.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0005886":
        return review(
            "Plasma membrane localization is appropriate for an ATP-binding component associated with a bacterial inner-membrane ABC importer.",
            "ACCEPT",
            "UniProt places the ATP-binding component at the cell inner membrane, consistent with association with the importer complex.",
            [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
                ref(file_ref(gene, "uniprot.txt"), cfg["location_quote"]),
            ],
        )
    if go_id == "GO:0015833":
        return review(
            "Peptide transport is supported but should be made substrate-specific where product naming allows it.",
            "MODIFY",
            "The product and locus context support the more specific transport term for this importer.",
            support(gene, cfg, rows, go_id),
            [term],
        )
    if go_id == "GO:0016887":
        return review(
            "ATP hydrolysis activity is correct for the ABC energy-coupling subunit.",
            "KEEP_AS_NON_CORE",
            "ATP hydrolysis powers import, but the substrate-specific transporter function/process is the core biological role.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0055085":
        return review(
            "Transmembrane transport is correct but too broad for this ABC importer ATPase.",
            "MODIFY",
            "The local product and locus context support a more specific transporter process term.",
            support(gene, cfg, rows, go_id),
            [term],
        )
    raise KeyError(f"Unhandled ATPase term {go_id} for {gene}")


def permease_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    term = process_term(cfg)
    if go_id == "GO:0005886":
        return review(
            "Plasma membrane localization is appropriate for this multi-pass bacterial inner-membrane permease.",
            "ACCEPT",
            "UniProt subcellular-location and transmembrane-segment predictions support membrane localization, represented as plasma membrane for bacteria.",
            [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
                ref(file_ref(gene, "uniprot.txt"), cfg["location_quote"]),
                ref(file_ref(gene, "uniprot.txt"), cfg["tm_quote"]),
            ],
        )
    if go_id == "GO:0016020":
        return review(
            "Generic membrane localization is supported but less informative than plasma membrane.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also contains the more specific plasma membrane annotation for this inner-membrane permease.",
            [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows["GO:0005886"])),
                ref(file_ref(gene, "uniprot.txt"), cfg["location_quote"]),
            ],
        )
    if go_id == "GO:0043190":
        return review(
            "ABC transporter complex membership is appropriate for this permease subunit.",
            "ACCEPT",
            "Binding-protein-dependent transporter permease domains and transmembrane helices support complex membership.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0055085":
        if cfg["group"] == "opine_like":
            return review(
                "Transmembrane transport is appropriate but remains substrate-unspecific for this opine-named permease.",
                "ACCEPT",
                "The protein is a membrane permease in an opine/glutathione-like ABC import locus. Current GO lacks an opine-specific transporter term and the exact substrate range remains unresolved, so the generic transport process is retained as the core first-pass process.",
                support(gene, cfg, rows, go_id),
            )
        return review(
            "Transmembrane transport is correct but too broad for this substrate-class importer permease.",
            "MODIFY",
            "The local product and locus context support a more specific transport process term.",
            support(gene, cfg, rows, go_id),
            [term],
        )
    raise KeyError(f"Unhandled permease term {go_id} for {gene}")


def binding_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], go_id: str) -> dict:
    if go_id == "GO:0015833":
        if cfg["group"] == "dipeptide":
            return review(
                "Peptide transport is supported but should be narrowed to dipeptide transport for this local importer.",
                "MODIFY",
                "The adjacent PP_3220 ATPase is annotated as an ABC-type dipeptide transporter, supporting dipeptide transport as the better process term.",
                support(gene, cfg, rows, go_id),
                [DIPEPTIDE_TRANSPORT],
            )
        return review(
            "Peptide transport is plausible family-level context for this SBP_5 binding component but not the resolved opine/glutathione substrate.",
            "ACCEPT",
            "PP_4458 is named as an opine ABC transporter binding protein, while the locus also contains glutathione-import subunits. Peptide transport is retained as the best available broad transporter-process term pending substrate evidence.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0030288":
        return review(
            "Periplasmic localization is appropriate for this extracytoplasmic ABC solute-binding component.",
            "ACCEPT",
            "The product name, periplasm/envelope localization, and signal or SBP-family features support a Gram-negative periplasmic binding-protein role.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0030313":
        return review(
            "Cell-envelope localization is compatible but less specific than periplasmic space.",
            "KEEP_AS_NON_CORE",
            "The periplasmic-space annotation better captures the expected localization of this ABC solute-binding component.",
            [
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows[go_id])),
                ref(file_ref(gene, "goa.tsv"), goa_quote(rows["GO:0030288"])),
                ref(file_ref(gene, "uniprot.txt"), cfg["location_quote"]),
            ],
        )
    if go_id == "GO:0043190":
        return review(
            "ABC transporter complex membership is appropriate for this solute-binding component.",
            "ACCEPT",
            "Bacterial ABC importers include extracytoplasmic solute-binding proteins, and the product/domain context supports that role.",
            support(gene, cfg, rows, go_id),
        )
    if go_id == "GO:0055085":
        replacement = DIPEPTIDE_TRANSMEMBRANE_TRANSPORT if cfg["group"] == "dipeptide" else PEPTIDE_TRANSPORT
        return review(
            "Transmembrane transport is correct at importer-complex level but broad for a solute-binding component.",
            "MODIFY" if cfg["group"] == "dipeptide" else "KEEP_AS_NON_CORE",
            "The binding protein contributes substrate capture for an ABC importer; the exact ligand range is clearer for the PP_3220 dipeptide locus than for the opine/glutathione-like PP_4453-PP_4458 locus.",
            support(gene, cfg, rows, go_id),
            [replacement] if cfg["group"] == "dipeptide" else None,
        )
    if go_id == "GO:1904680":
        if cfg["group"] == "dipeptide":
            return review(
                "Peptide transmembrane transporter activity is appropriate but can be narrowed to dipeptide transporter activity for this local importer.",
                "MODIFY",
                "The adjacent PP_3220 ATPase product name supports dipeptide transporter activity as the more specific molecular-function term.",
                support(gene, cfg, rows, go_id),
                [DIPEPTIDE_TRANSPORTER],
            )
        return review(
            "Peptide transmembrane transporter activity is plausible but may overstate the unresolved opine/glutathione substrate range.",
            "ACCEPT",
            "PP_4458 is named as an opine ABC transporter binding protein, so the peptide transporter term is retained as the closest available broad molecular-function term pending substrate-specific evidence.",
            support(gene, cfg, rows, go_id),
        )
    raise KeyError(f"Unhandled binding-protein term {go_id} for {gene}")


def new_annotation(term: dict[str, str], qualifier: str, gene: str, cfg: dict, summary: str, reason: str) -> dict:
    return {
        "term": term,
        "evidence_type": "IEA",
        "original_reference_id": file_ref(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": [
                ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
                ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
                ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
            ],
        },
    }


def maybe_new_annotations(data: dict, gene: str, cfg: dict) -> None:
    existing_ids = {ann["term"]["id"] for ann in data.get("existing_annotations", [])}
    if cfg["kind"] == "atpase" and "GO:0043190" not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                gene,
                cfg,
                "ABC transporter complex membership is a useful missing annotation for this ATP-binding importer subunit.",
                "The ATP-binding protein product name and ABC transporter ATP-binding domains support membership in a multi-subunit ABC importer complex.",
            )
        )
    if cfg["group"] == "dipeptide" and "GO:0071916" not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                DIPEPTIDE_TRANSPORTER,
                "contributes_to" if cfg["kind"] != "atpase" else "enables",
                gene,
                cfg,
                "Dipeptide transmembrane transporter activity is the missing substrate-specific molecular-function annotation for this local importer subunit.",
                "The PP_3220 product name and local permease/binding-protein context support a dipeptide ABC import system.",
            )
        )
    if cfg["group"] == "glutathione" and "GO:0034634" not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                GLUTATHIONE_TRANSPORTER,
                "contributes_to" if cfg["kind"] != "atpase" else "enables",
                gene,
                cfg,
                "Glutathione transmembrane transporter activity is the missing substrate-specific molecular-function annotation for this Gsi importer subunit.",
                "The gsiA/gsiC product names support glutathione import activity for the local ABC transporter.",
            )
        )
    if cfg["group"] == "glutathione" and "GO:0034635" not in existing_ids:
        data.setdefault("existing_annotations", []).append(
            new_annotation(
                GLUTATHIONE_TRANSPORT,
                "involved_in",
                gene,
                cfg,
                "Glutathione transport is the missing substrate-specific biological-process annotation for this Gsi importer subunit.",
                "The gsiA/gsiC product names support glutathione import as the substrate-specific process for these subunits.",
            )
        )


def core_functions(gene: str, cfg: dict, rows: dict[str, dict[str, str]]) -> list[dict]:
    common_support = [
        ref(file_ref(gene, "uniprot.txt"), cfg["product_quote"]),
        ref(file_ref(gene, "uniprot.txt"), cfg["domain_quote"]),
        ref(file_ref(gene, "deep-research-asta.md"), cfg["asta_quote"]),
    ]
    if cfg["kind"] == "atpase":
        locs = [PLASMA_MEMBRANE] if "GO:0005886" in rows else []
        return [
            {
                "description": "ATP-binding energy-coupling subunit of a predicted substrate-specific ABC importer.",
                "molecular_function": activity_term(cfg),
                "directly_involved_in": [process_term(cfg)],
                "locations": locs,
                "in_complex": ABC_COMPLEX,
                "supported_by": common_support,
            }
        ]
    if cfg["kind"] == "permease":
        core = {
            "description": "Multi-pass membrane permease subunit of a predicted peptide/opine/glutathione-like ABC importer.",
            "directly_involved_in": [process_term(cfg)],
            "locations": [PLASMA_MEMBRANE],
            "in_complex": ABC_COMPLEX,
            "supported_by": common_support + [ref(file_ref(gene, "uniprot.txt"), cfg["tm_quote"])],
        }
        if cfg["group"] != "opine_like":
            core["contributes_to_molecular_function"] = activity_term(cfg)
        else:
            core["contributes_to_molecular_function"] = TRANSMEMBRANE_TRANSPORTER
        return [core]
    return [
        {
            "description": "Periplasmic solute-binding component predicted to capture substrate for a peptide/opine/glutathione-like ABC importer.",
            "contributes_to_molecular_function": activity_term(cfg),
            "directly_involved_in": [process_term(cfg) if cfg["group"] != "opine_like" else PEPTIDE_TRANSPORT],
            "locations": [PERIPLASM],
            "in_complex": ABC_COMPLEX,
            "supported_by": common_support,
        }
    ]


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text())
    rows = goa_rows(gene)

    data["gene_symbol"] = cfg["symbol"]
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_references(data, gene, cfg)

    for ann in data.get("existing_annotations", []):
        if ann.get("review", {}).get("action") == "NEW":
            continue
        go_id = ann["term"]["id"]
        if cfg["kind"] == "atpase":
            ann["review"] = atpase_review(gene, cfg, rows, go_id)
        elif cfg["kind"] == "permease":
            ann["review"] = permease_review(gene, cfg, rows, go_id)
        else:
            ann["review"] = binding_review(gene, cfg, rows, go_id)

    maybe_new_annotations(data, gene, cfg)
    data["core_functions"] = core_functions(gene, cfg, rows)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = [
        {
            "question": f"What substrate range is transported by the {gene}-containing ABC importer in P. putida KT2440, and how are peptide, glutathione, and opine-like substrates partitioned among related loci?"
        }
    ]
    data["suggested_experiments"] = [
        {
            "description": f"Compare wild type, {gene} deletion, and complemented strains for uptake or growth on candidate dipeptide, glutathione, and opine substrates using LC-MS or radiotracer assays.",
            "experiment_type": "targeted transporter mutant substrate-uptake assay",
        }
    ]

    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=1000))
    print(f"curated {path}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)


if __name__ == "__main__":
    main()
