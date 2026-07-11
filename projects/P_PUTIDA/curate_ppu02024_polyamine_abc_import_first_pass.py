#!/usr/bin/env python3
"""First-pass curation for ppu02024 polyamine ABC import genes."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
SPECIES = "PSEPK"
GENE_ROOT = ROOT / "genes" / SPECIES
MODULE_PATH = ROOT / "modules" / "polyamine_transport_boundary.yaml"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


GO_REF_TITLES = {
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000044": "Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary mapping, accompanied by conservative changes to GO terms applied by UniProt",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on on inter-ontology links.",
    "GO_REF:0000117": "Electronic Gene Ontology annotations created by ARBA machine learning models",
    "GO_REF:0000118": "TreeGrafter-generated GO annotations",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}

POLYAMINE_TRANSPORT = {"id": "GO:0015846", "label": "polyamine transport"}
POLYAMINE_TRANSMEMBRANE_TRANSPORT = {
    "id": "GO:1902047",
    "label": "polyamine transmembrane transport",
}
PUTRESCINE_TRANSPORT = {"id": "GO:0015847", "label": "putrescine transport"}
POLYAMINE_BINDING = {"id": "GO:0019808", "label": "polyamine binding"}
ABC_POLYAMINE_TRANSPORTER = {
    "id": "GO:0015417",
    "label": "ABC-type polyamine transporter activity",
}
ABC_PUTRESCINE_TRANSPORTER = {
    "id": "GO:0015594",
    "label": "ABC-type putrescine transporter activity",
}
ATP_HYDROLYSIS = {"id": "GO:0016887", "label": "ATP hydrolysis activity"}
ABC_TRANSPORTER = {"id": "GO:0140359", "label": "ABC-type transporter activity"}
TRANSMEMBRANE_TRANSPORTER = {"id": "GO:0022857", "label": "transmembrane transporter activity"}
TRANSMEMBRANE_TRANSPORT = {"id": "GO:0055085", "label": "transmembrane transport"}
ABC_COMPLEX = {
    "id": "GO:0043190",
    "label": "ATP-binding cassette (ABC) transporter complex",
}
PLASMA_MEMBRANE = {"id": "GO:0005886", "label": "plasma membrane"}
MEMBRANE = {"id": "GO:0016020", "label": "membrane"}
PERIPLASM = {"id": "GO:0042597", "label": "periplasmic space"}
GRAM_NEG_PERIPLASM = {"id": "GO:0030288", "label": "outer membrane-bounded periplasmic space"}


GENES = {
    "potA": {
        "accession": "Q88QS7",
        "locus": "PP_0411",
        "kind": "atpase",
        "operon": "PP_0411-PP_0414",
        "role": "spermidine/putrescine ABC import ATP-binding subunit",
        "product_text": "Full=Spermidine/putrescine import ATP-binding protein PotA",
        "asta_text": "Protein Description:** RecName: Full=Spermidine/putrescine import ATP-binding protein PotA",
        "domain_text": "PotA-like.",
        "atp_domain_text": "ABC_transporter-like_ATP-bd.",
        "description": (
            "potA (PP_0411) encodes the ATP-binding energy-coupling subunit of the PP_0411-PP_0414 "
            "polyamine ABC import locus in Pseudomonas putida KT2440. UniProt names it as PotA, assigns "
            "EC 7.6.2.11, and records PotA-like ABC transporter domains, supporting ATP-driven "
            "spermidine/putrescine uptake rather than a quorum-sensing-specific role."
        ),
    },
    "PP_0412": {
        "accession": "Q88QS6",
        "locus": "PP_0412",
        "kind": "binding",
        "operon": "PP_0411-PP_0414",
        "role": "polyamine ABC import periplasmic binding subunit",
        "product_text": "Full=Polyamine ABC transporter, periplasmic polyamine-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Polyamine ABC transporter, periplasmic polyamine-binding protein",
        "domain_text": "SPERMIDINE/PUTRESCINE-BINDING PERIPLASMIC PROTEIN",
        "signal_text": "FT   SIGNAL          1..22",
        "description": (
            "PP_0412 encodes a predicted signal-peptide-bearing periplasmic substrate-binding component of "
            "the PP_0411-PP_0414 polyamine ABC import locus in Pseudomonas putida KT2440. Although GOA has "
            "no current annotations for this protein, UniProt product naming, SBP_bac_8/PANTHER family "
            "context, and adjacency to potA plus two permeases support a polyamine-binding importer role."
        ),
    },
    "PP_0413": {
        "accession": "Q88QS5",
        "locus": "PP_0413",
        "kind": "permease",
        "operon": "PP_0411-PP_0414",
        "role": "polyamine ABC import permease",
        "product_text": "Full=Polyamine ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Polyamine ABC transporter, permease protein",
        "domain_text": "MetI-like.",
        "location_text": "Cell membrane",
        "tm_text": "FT   TRANSMEM        33..54",
        "description": (
            "PP_0413 encodes a multi-pass inner-membrane permease subunit of the PP_0411-PP_0414 "
            "polyamine ABC import locus in Pseudomonas putida KT2440. Product naming, MetI-like "
            "binding-protein-dependent transporter features, and membrane topology support a channel-subunit "
            "role in polyamine uptake."
        ),
    },
    "PP_0414": {
        "accession": "Q88QS4",
        "locus": "PP_0414",
        "kind": "permease",
        "operon": "PP_0411-PP_0414",
        "role": "polyamine ABC import permease",
        "product_text": "Full=Polyamine ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Polyamine ABC transporter, permease protein",
        "domain_text": "MetI-like.",
        "location_text": "Cell inner membrane",
        "tm_text": "FT   TRANSMEM        12..40",
        "description": (
            "PP_0414 encodes a second multi-pass inner-membrane permease subunit of the PP_0411-PP_0414 "
            "polyamine ABC import locus in Pseudomonas putida KT2440. Its product name, MetI-like "
            "permease domains, and predicted transmembrane helices support a paired membrane-channel role "
            "with PP_0413."
        ),
    },
    "ydcV": {
        "accession": "Q88MT6",
        "locus": "PP_1482",
        "kind": "permease",
        "operon": "ydcVUTS",
        "role": "polyamine ABC import permease",
        "product_text": "Full=Polyamine ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Polyamine ABC transporter, permease protein",
        "domain_text": "Bact_Polyamine_Transport.",
        "location_text": "Cell membrane",
        "tm_text": "FT   TRANSMEM        12..33",
        "description": (
            "ydcV (PP_1482) encodes a multi-pass membrane permease subunit of a predicted YdcVUTS "
            "polyamine ABC import locus in Pseudomonas putida KT2440. Its bacterial polyamine transport "
            "and MetI-like permease signatures support a substrate-class assignment to polyamine uptake."
        ),
    },
    "ydcU": {
        "accession": "Q88MT5",
        "locus": "PP_1483",
        "kind": "permease",
        "operon": "ydcVUTS",
        "role": "polyamine ABC import permease",
        "product_text": "Full=Polyamine ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Polyamine ABC transporter, permease protein",
        "domain_text": "MetI-like.",
        "location_text": "Cell membrane",
        "tm_text": "FT   TRANSMEM        21..43",
        "description": (
            "ydcU (PP_1483) encodes a second multi-pass membrane permease subunit of the predicted YdcVUTS "
            "polyamine ABC import locus in Pseudomonas putida KT2440. Product naming, MetI-like transporter "
            "features, and local ydcV/ydcT/ydcS context support a role in polyamine transmembrane import."
        ),
    },
    "ydcT": {
        "accession": "Q88MT4",
        "locus": "PP_1484",
        "kind": "atpase",
        "operon": "ydcVUTS",
        "role": "polyamine ABC import ATP-binding subunit",
        "product_text": "Full=Predicted polyamine ABC transporter, ATP-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Predicted polyamine ABC transporter, ATP-binding protein",
        "domain_text": "SPERMIDINE/PUTRESCINE IMPORT ATP-BINDING PROTEIN POTA",
        "atp_domain_text": "ABC_transporter-like_ATP-bd.",
        "description": (
            "ydcT (PP_1484) encodes the ATP-binding energy-coupling subunit of the predicted YdcVUTS "
            "polyamine ABC import locus in Pseudomonas putida KT2440. Its product name, ABC ATP-binding "
            "domains, and local ydcV/ydcU permease plus ydcS binding-protein context support ATP-driven "
            "putrescine/polyamine uptake."
        ),
    },
    "ydcS": {
        "accession": "Q88MT2",
        "locus": "PP_1486",
        "kind": "binding",
        "operon": "ydcVUTS",
        "role": "polyamine ABC import periplasmic binding subunit",
        "product_text": "Full=Polyamine ABC transporter, periplasmic polyamine-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Polyamine ABC transporter, periplasmic polyamine-binding protein",
        "domain_text": "Sperm_putr-bd.",
        "signal_text": "FT   SIGNAL          1..22",
        "location_text": "Periplasm",
        "description": (
            "ydcS (PP_1486) encodes a periplasmic substrate-binding component of the predicted YdcVUTS "
            "polyamine ABC import locus in Pseudomonas putida KT2440. UniProt/GOA support polyamine binding, "
            "polyamine transport, and periplasmic localization for this solute-capture subunit."
        ),
    },
    "PP_2870": {
        "accession": "Q88IX9",
        "locus": "PP_2870",
        "kind": "binding",
        "operon": "singleton",
        "role": "spermidine/putrescine-binding periplasmic component",
        "product_text": "Full=Spermidine/putrescine-binding periplasmic protein",
        "asta_text": "Protein Description:** SubName: Full=Spermidine/putrescine-binding periplasmic protein",
        "domain_text": "SPERMIDINE/PUTRESCINE-BINDING PERIPLASMIC PROTEIN",
        "signal_text": "FT   SIGNAL          1..24",
        "description": (
            "PP_2870 encodes a predicted signal-peptide-bearing spermidine/putrescine-binding periplasmic "
            "protein in Pseudomonas putida KT2440. The protein is best curated as a polyamine-binding "
            "substrate-capture component, while its cognate membrane permease and ATP-binding partners remain "
            "unresolved in this first-pass pathway partition."
        ),
    },
    "PP_3814": {
        "accession": "Q88GB0",
        "locus": "PP_3814",
        "kind": "binding",
        "operon": "PP_3814-PP_3817",
        "role": "polyamine ABC import periplasmic binding subunit",
        "product_text": "Full=Polyamine ABC transporter, periplasmic polyamine-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Polyamine ABC transporter, periplasmic polyamine-binding protein",
        "domain_text": "SBP_bac_8",
        "signal_text": "FT   SIGNAL          1..25",
        "location_text": "Periplasm",
        "description": (
            "PP_3814 encodes a predicted signal-peptide-bearing periplasmic substrate-binding component of "
            "the PP_3814-PP_3817 polyamine ABC import locus in Pseudomonas putida KT2440. UniProt names it "
            "as a polyamine ABC transporter binding protein; TreeGrafter thiamine-binding annotations are "
            "therefore treated as over-propagated relative to the local polyamine importer context."
        ),
    },
    "PP_3815": {
        "accession": "Q88GA9",
        "locus": "PP_3815",
        "kind": "permease",
        "operon": "PP_3814-PP_3817",
        "role": "polyamine ABC import permease",
        "product_text": "Full=Polyamine ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Polyamine ABC transporter, permease protein",
        "domain_text": "MetI-like.",
        "location_text": "Cell membrane",
        "tm_text": "FT   TRANSMEM        40..64",
        "description": (
            "PP_3815 encodes a multi-pass membrane permease subunit of the PP_3814-PP_3817 polyamine ABC "
            "import locus in Pseudomonas putida KT2440. Product naming, MetI-like transporter signatures, "
            "and local binding/permease/ATPase context support polyamine transmembrane import."
        ),
    },
    "PP_3816": {
        "accession": "Q88GA8",
        "locus": "PP_3816",
        "kind": "permease",
        "operon": "PP_3814-PP_3817",
        "role": "polyamine ABC import permease",
        "product_text": "Full=Polyamine ABC transporter, permease protein",
        "asta_text": "Protein Description:** SubName: Full=Polyamine ABC transporter, permease protein",
        "domain_text": "MetI-like.",
        "location_text": "Cell inner membrane",
        "tm_text": "FT   TRANSMEM        16..39",
        "description": (
            "PP_3816 encodes a second multi-pass inner-membrane permease subunit of the PP_3814-PP_3817 "
            "polyamine ABC import locus in Pseudomonas putida KT2440. It is best modeled as contributing "
            "to the membrane channel of a predicted polyamine importer."
        ),
    },
    "PP_3817": {
        "accession": "Q88GA7",
        "locus": "PP_3817",
        "kind": "atpase",
        "operon": "PP_3814-PP_3817",
        "role": "polyamine ABC import ATP-binding subunit",
        "product_text": "Full=Polyamine ABC transporter, ATP-binding protein",
        "asta_text": "Protein Description:** SubName: Full=Polyamine ABC transporter, ATP-binding protein",
        "domain_text": "SPERMIDINE/PUTRESCINE IMPORT ATP-BINDING PROTEIN POTA",
        "atp_domain_text": "ABC_transporter-like_ATP-bd.",
        "description": (
            "PP_3817 encodes the ATP-binding energy-coupling subunit of the PP_3814-PP_3817 polyamine "
            "ABC import locus in Pseudomonas putida KT2440. Its product name, PotA-family assignment, and "
            "local PP_3814/PP_3815/PP_3816 importer context support ATP-driven polyamine uptake."
        ),
    },
}


def go_term(term: dict[str, str]) -> dict[str, str]:
    return {"id": term["id"], "label": term["label"]}


def file_ref(gene: str, suffix: str) -> str:
    return f"file:{SPECIES}/{gene}/{gene}-{suffix}"


def support(reference_id: str, supporting_text: str) -> dict[str, str]:
    return {"reference_id": reference_id, "supporting_text": supporting_text}


def support_uniprot(gene: str, text: str) -> dict[str, str]:
    return support(file_ref(gene, "uniprot.txt"), text)


def support_asta(gene: str, text: str) -> dict[str, str]:
    return support(file_ref(gene, "deep-research-asta.md"), text)


def goa_rows(gene: str) -> dict[str, dict[str, str]]:
    with (GENE_ROOT / gene / f"{gene}-goa.tsv").open(encoding="utf-8") as handle:
        return {row["GO TERM"]: row for row in csv.DictReader(handle, delimiter="\t")}


def goa_quote(row: dict[str, str]) -> str:
    return f"{row['GO TERM']}\t{row['GO NAME']}"


def support_goa(gene: str, rows: dict[str, dict[str, str]], term_id: str) -> dict[str, str]:
    return support(file_ref(gene, "goa.tsv"), goa_quote(rows[term_id]))


def review(
    summary: str,
    action: str,
    reason: str,
    supported_by: list[dict[str, str]],
    proposed: list[dict[str, str]] | None = None,
) -> dict:
    result = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": supported_by,
    }
    if proposed:
        result["proposed_replacement_terms"] = proposed
    return result


def basic_support(gene: str, cfg: dict, rows: dict[str, dict[str, str]], term_id: str) -> list[dict[str, str]]:
    evidence = [
        support_goa(gene, rows, term_id),
        support_uniprot(gene, cfg["product_text"]),
        support_asta(gene, cfg["asta_text"]),
    ]
    if cfg["kind"] == "atpase":
        evidence.extend([support_uniprot(gene, cfg["atp_domain_text"]), support_uniprot(gene, cfg["domain_text"])])
    elif cfg["kind"] == "permease":
        evidence.extend([support_uniprot(gene, cfg["domain_text"]), support_uniprot(gene, cfg["tm_text"])])
    else:
        evidence.extend([support_uniprot(gene, cfg["domain_text"]), support_uniprot(gene, cfg["signal_text"])])
    return evidence


def ensure_references(data: dict, gene: str, cfg: dict) -> None:
    refs = {entry["id"]: entry for entry in data.get("references", [])}
    for ref_id, title in GO_REF_TITLES.items():
        refs.setdefault(ref_id, {"id": ref_id, "title": title, "findings": []})

    findings = [
        {
            "statement": "UniProt product naming supports the first-pass polyamine transporter component assignment.",
            "supporting_text": cfg["product_text"],
        },
    ]
    if cfg["kind"] == "atpase":
        findings.extend(
            [
                {
                    "statement": "ABC ATP-binding domains support an energy-coupling role.",
                    "supporting_text": cfg["atp_domain_text"],
                },
                {
                    "statement": "PotA-family assignment supports putrescine/polyamine importer context.",
                    "supporting_text": cfg["domain_text"],
                },
            ]
        )
    elif cfg["kind"] == "permease":
        findings.extend(
            [
                {
                    "statement": "MetI-like or bacterial polyamine transporter features support a permease role.",
                    "supporting_text": cfg["domain_text"],
                },
                {
                    "statement": "Predicted transmembrane helices support an inner-membrane channel subunit role.",
                    "supporting_text": cfg["tm_text"],
                },
            ]
        )
    else:
        findings.extend(
            [
                {
                    "statement": "Solute-binding protein family context supports a periplasmic substrate-binding role.",
                    "supporting_text": cfg["domain_text"],
                },
                {
                    "statement": "The signal peptide supports extracytoplasmic/periplasmic localization.",
                    "supporting_text": cfg["signal_text"],
                },
            ]
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
                "supporting_text": cfg["asta_text"],
            }
        ],
    }
    data["references"] = list(refs.values())


def atpase_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], term_id: str) -> dict:
    if term_id == "GO:0000166":
        return review(
            "Generic nucleotide binding is true but over-broad for this ABC ATP-binding transporter subunit.",
            "MARK_AS_OVER_ANNOTATED",
            "ATP binding and ATP hydrolysis in a polyamine ABC importer are more informative than generic nucleotide binding.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0005524":
        return review(
            "ATP binding is correct mechanistic context for this PotA-family ABC energy-coupling subunit.",
            "KEEP_AS_NON_CORE",
            "ATP binding is required for the ABC ATPase, but the transporter role is better captured by ATP hydrolysis coupled to polyamine import.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0015417":
        return review(
            "ABC-type polyamine transporter activity is appropriate for the PotA-family importer ATP-binding subunit.",
            "ACCEPT",
            "The product, PotA-family assignment, and local permease/binding-protein context support polyamine ABC importer activity.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0015594":
        return review(
            "ABC-type putrescine transporter activity is appropriate for this PotA-family importer ATP-binding subunit.",
            "ACCEPT",
            "Putrescine is a named substrate within the spermidine/putrescine/polyamine importer context, so this substrate-specific activity is retained.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0015846":
        return review(
            "Polyamine transport is appropriate process context for this PotA-family importer subunit.",
            "ACCEPT",
            "The product and local ABC import locus support ATP-driven polyamine uptake.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0015847":
        return review(
            "Putrescine transport is supported for this predicted spermidine/putrescine/polyamine importer subunit.",
            "ACCEPT",
            "Putrescine transport is consistent with PotA/PotABCD-like importer context and is not a quorum-sensing-specific assertion.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0016020":
        return review(
            "Generic membrane association is plausible but less informative than transporter-complex and process annotations.",
            "MARK_AS_OVER_ANNOTATED",
            "PotA-family ATP-binding subunits are energy-coupling components of membrane transporter complexes, but generic membrane localization should not be the core function.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0016887":
        return review(
            "ATP hydrolysis activity is appropriate for this ABC transporter ATP-binding subunit.",
            "ACCEPT",
            "The ABC ATP-binding domain and PotA-family importer context support ATP hydrolysis as the catalytic energy-coupling activity.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0022857":
        return review(
            "Generic transmembrane transporter activity is correct only as broad complex context.",
            "MODIFY",
            "The local product and operon context support the more specific ABC-type polyamine transporter activity.",
            basic_support(gene, cfg, rows, term_id),
            [go_term(ABC_POLYAMINE_TRANSPORTER)],
        )
    if term_id == "GO:0043190":
        return review(
            "ABC transporter complex membership is appropriate for this polyamine import ATP-binding subunit.",
            "ACCEPT",
            "The product, ABC ATP-binding domains, and local permease/binding-protein partners support complex membership.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0055085":
        return review(
            "Transmembrane transport is true but too broad for this polyamine ABC importer subunit.",
            "MODIFY",
            "The product and local locus context support polyamine transmembrane transport as the more informative process term.",
            basic_support(gene, cfg, rows, term_id),
            [go_term(POLYAMINE_TRANSMEMBRANE_TRANSPORT)],
        )
    if term_id == "GO:0140359":
        return review(
            "ABC-type transporter activity is correct but less specific than polyamine/putrescine ABC transporter activity.",
            "MODIFY",
            "PotA-family and local locus context support a substrate-class-specific ABC-type polyamine transporter term.",
            basic_support(gene, cfg, rows, term_id),
            [go_term(ABC_POLYAMINE_TRANSPORTER)],
        )
    if term_id == "GO:1902047":
        return review(
            "Polyamine transmembrane transport is appropriate process context for this PotA-family importer subunit.",
            "ACCEPT",
            "The product and local ABC import locus support ATP-driven polyamine movement across the membrane.",
            basic_support(gene, cfg, rows, term_id),
        )
    raise KeyError(f"Unhandled ATPase term {term_id} for {gene}")


def permease_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], term_id: str) -> dict:
    if term_id == "GO:0005886":
        return review(
            "Plasma membrane localization is appropriate for this predicted inner-membrane polyamine-import permease.",
            "ACCEPT",
            "UniProt subcellular-location and transmembrane-segment predictions support bacterial membrane localization.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0016020":
        return review(
            "Generic membrane localization is supported but less informative than plasma membrane and transporter-complex context.",
            "MARK_AS_OVER_ANNOTATED",
            "The record also carries plasma membrane localization, and the protein is a multi-pass permease subunit of an ABC importer.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0043190":
        return review(
            "ABC transporter complex membership is appropriate for this permease subunit.",
            "ACCEPT",
            "MetI-like transporter domains, membrane topology, and local ATPase/binding-protein partners support complex membership.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0055085":
        return review(
            "Transmembrane transport is correct but too broad for this polyamine ABC importer permease.",
            "MODIFY",
            "The UniProt product name and local locus context support polyamine transmembrane transport rather than unspecified transport.",
            basic_support(gene, cfg, rows, term_id),
            [go_term(POLYAMINE_TRANSMEMBRANE_TRANSPORT)],
        )
    raise KeyError(f"Unhandled permease term {term_id} for {gene}")


def binding_review(gene: str, cfg: dict, rows: dict[str, dict[str, str]], term_id: str) -> dict:
    if term_id == "GO:0015846":
        return review(
            "Polyamine transport is appropriate process context for this periplasmic substrate-binding component.",
            "ACCEPT",
            "The product and family context support substrate capture for a polyamine ABC import system.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0019808":
        return review(
            "Polyamine binding is appropriate for this predicted periplasmic polyamine-binding protein.",
            "ACCEPT",
            "Product naming, solute-binding protein features, and Asta retrieval support polyamine substrate binding.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0015888":
        return review(
            "The transporter-process idea is plausible, but thiamine specificity is unsupported in this polyamine-import locus.",
            "MODIFY",
            "PP_3814 is named as a polyamine ABC transporter periplasmic binding protein and sits next to polyamine transporter permease and ATP-binding genes; the TreeGrafter thiamine transport call is better replaced by polyamine transport.",
            basic_support(gene, cfg, rows, term_id),
            [go_term(POLYAMINE_TRANSPORT)],
        )
    if term_id in {"GO:0030288", "GO:0042597"}:
        return review(
            "Periplasmic localization is appropriate for this signal-peptide-bearing solute-binding protein.",
            "ACCEPT",
            "The signal peptide, product description, and UniProt periplasmic context support extracytoplasmic/periplasmic localization.",
            basic_support(gene, cfg, rows, term_id),
        )
    if term_id == "GO:0030975":
        return review(
            "Thiamine binding is not supported by the local polyamine ABC-import context.",
            "MODIFY",
            "The product name and adjacent PP_3815/PP_3816/PP_3817 transporter subunits support polyamine binding as the better molecular-function term.",
            basic_support(gene, cfg, rows, term_id),
            [go_term(POLYAMINE_BINDING)],
        )
    if term_id == "GO:0030976":
        return review(
            "Thiamine pyrophosphate binding is likely an over-propagated solute-binding-family annotation for this periplasmic transporter component.",
            "REMOVE",
            "PP_3814 is a signal-peptide-bearing polyamine ABC transporter binding protein, not a cytosolic thiamine-pyrophosphate enzyme or cofactor-binding protein, and the local transporter locus does not support TPP binding.",
            basic_support(gene, cfg, rows, term_id),
        )
    raise KeyError(f"Unhandled binding term {term_id} for {gene}")


def new_annotation(
    term: dict[str, str],
    qualifier: str,
    gene: str,
    cfg: dict,
    summary: str,
    reason: str,
    extra_support: list[dict[str, str]] | None = None,
) -> dict:
    supported_by = [
        support_uniprot(gene, cfg["product_text"]),
        support_asta(gene, cfg["asta_text"]),
    ]
    if cfg["kind"] == "atpase":
        supported_by.extend([support_uniprot(gene, cfg["atp_domain_text"]), support_uniprot(gene, cfg["domain_text"])])
    elif cfg["kind"] == "permease":
        supported_by.extend([support_uniprot(gene, cfg["domain_text"]), support_uniprot(gene, cfg["tm_text"])])
    else:
        supported_by.extend([support_uniprot(gene, cfg["domain_text"]), support_uniprot(gene, cfg["signal_text"])])
    if extra_support:
        supported_by.extend(extra_support)
    return {
        "term": go_term(term),
        "evidence_type": "IEA",
        "original_reference_id": file_ref(gene, "uniprot.txt"),
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": supported_by,
        },
    }


def maybe_new_annotations(data: dict, gene: str, cfg: dict) -> None:
    existing_ids = {ann["term"]["id"] for ann in data.get("existing_annotations", [])}
    additions: list[dict] = []
    if cfg["kind"] == "atpase":
        if ABC_POLYAMINE_TRANSPORTER["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    ABC_POLYAMINE_TRANSPORTER,
                    "contributes_to",
                    gene,
                    cfg,
                    "ABC-type polyamine transporter activity is a missing substrate-class activity annotation for this ATP-binding importer subunit.",
                    "The product name, PotA-family assignment, and local permease/binding-protein partners support polyamine ABC importer activity.",
                )
            )
        if POLYAMINE_TRANSMEMBRANE_TRANSPORT["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    POLYAMINE_TRANSMEMBRANE_TRANSPORT,
                    "involved_in",
                    gene,
                    cfg,
                    "Polyamine transmembrane transport is a missing substrate-class process annotation for this ATP-binding importer subunit.",
                    "The local ABC import locus supports ATP-driven movement of polyamines across the bacterial membrane.",
                )
            )
    elif cfg["kind"] == "permease":
        if ABC_POLYAMINE_TRANSPORTER["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    ABC_POLYAMINE_TRANSPORTER,
                    "contributes_to",
                    gene,
                    cfg,
                    "ABC-type polyamine transporter activity is a missing component-level activity annotation for this permease.",
                    "The permease does not transport alone, but contributes to the predicted polyamine ABC importer complex.",
                )
            )
        if POLYAMINE_TRANSMEMBRANE_TRANSPORT["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    POLYAMINE_TRANSMEMBRANE_TRANSPORT,
                    "involved_in",
                    gene,
                    cfg,
                    "Polyamine transmembrane transport is a missing substrate-class process annotation for this permease.",
                    "The product name and local ABC import locus support polyamine uptake across the membrane.",
                )
            )
    else:
        if POLYAMINE_BINDING["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    POLYAMINE_BINDING,
                    "enables",
                    gene,
                    cfg,
                    "Polyamine binding is a missing molecular-function annotation for this periplasmic binding protein.",
                    "Product naming, solute-binding protein family context, and signal peptide support a polyamine substrate-capture role.",
                )
            )
        if POLYAMINE_TRANSPORT["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    POLYAMINE_TRANSPORT,
                    "involved_in",
                    gene,
                    cfg,
                    "Polyamine transport is a missing process annotation for this solute-binding component.",
                    "The protein is predicted to capture polyamine substrate for an ABC importer.",
                )
            )
        if PERIPLASM["id"] not in existing_ids:
            additions.append(
                new_annotation(
                    PERIPLASM,
                    "located_in",
                    gene,
                    cfg,
                    "Periplasmic space is a missing cellular-component annotation for this signal-peptide-bearing binding protein.",
                    "The signal peptide and periplasmic binding-protein product context support Gram-negative periplasmic localization.",
                )
            )
    if cfg["operon"] != "singleton" and ABC_COMPLEX["id"] not in existing_ids:
        additions.append(
            new_annotation(
                ABC_COMPLEX,
                "part_of",
                gene,
                cfg,
                "ABC transporter complex membership is a missing annotation for this polyamine importer component.",
                "The protein belongs to an operon-like ATPase/permease/binding-protein polyamine ABC import locus.",
            )
        )
    data.setdefault("existing_annotations", []).extend(additions)


def core_functions(gene: str, cfg: dict, rows: dict[str, dict[str, str]]) -> list[dict]:
    supported_by = [
        support_uniprot(gene, cfg["product_text"]),
        support_asta(gene, cfg["asta_text"]),
    ]
    if cfg["kind"] == "atpase":
        return [
            {
                "description": f"ATP-binding energy-coupling subunit of the {cfg['operon']} polyamine ABC importer.",
                "molecular_function": go_term(ATP_HYDROLYSIS),
                "contributes_to_molecular_function": go_term(ABC_POLYAMINE_TRANSPORTER),
                "directly_involved_in": [go_term(POLYAMINE_TRANSMEMBRANE_TRANSPORT), go_term(PUTRESCINE_TRANSPORT)],
                "in_complex": go_term(ABC_COMPLEX),
                "supported_by": supported_by
                + [
                    support_uniprot(gene, cfg["atp_domain_text"]),
                    support_uniprot(gene, cfg["domain_text"]),
                ],
            }
        ]
    if cfg["kind"] == "permease":
        return [
            {
                "description": f"Multi-pass membrane permease subunit contributing to {cfg['operon']} polyamine ABC import.",
                "contributes_to_molecular_function": go_term(ABC_POLYAMINE_TRANSPORTER),
                "directly_involved_in": [go_term(POLYAMINE_TRANSMEMBRANE_TRANSPORT)],
                "locations": [go_term(PLASMA_MEMBRANE)],
                "in_complex": go_term(ABC_COMPLEX),
                "supported_by": supported_by
                + [
                    support_uniprot(gene, cfg["domain_text"]),
                    support_uniprot(gene, cfg["tm_text"]),
                ],
            }
        ]
    core = {
        "description": (
            "Periplasmic polyamine-binding substrate-capture component"
            if cfg["operon"] == "singleton"
            else f"Periplasmic substrate-binding component of the {cfg['operon']} polyamine ABC importer."
        ),
        "molecular_function": go_term(POLYAMINE_BINDING),
        "directly_involved_in": [go_term(POLYAMINE_TRANSPORT)],
        "locations": [go_term(PERIPLASM)],
        "supported_by": supported_by
        + [
            support_uniprot(gene, cfg["domain_text"]),
            support_uniprot(gene, cfg["signal_text"]),
        ],
    }
    if cfg["operon"] != "singleton":
        core["in_complex"] = go_term(ABC_COMPLEX)
    return [core]


def suggested_questions(gene: str, cfg: dict) -> list[dict[str, str]]:
    if cfg["operon"] == "singleton":
        question = (
            f"Which membrane permease and ATP-binding partners pair with {gene}, and what is its ligand preference "
            "among putrescine, spermidine, norspermidine, and related polyamines?"
        )
    else:
        question = (
            f"What substrate range is transported by the {cfg['operon']} importer containing {gene}, and how does "
            "it divide uptake of putrescine, spermidine, norspermidine, and related polyamines from other P. putida polyamine systems?"
        )
    return [{"question": question}]


def suggested_experiments(gene: str, cfg: dict) -> list[dict[str, str]]:
    if cfg["kind"] == "binding":
        description = (
            f"Measure purified {gene} ligand binding and compare deletion/complementation phenotypes for uptake or growth "
            "responses to putrescine, spermidine, norspermidine, and related polyamines."
        )
        experiment_type = "targeted polyamine-binding and uptake assay"
    else:
        description = (
            f"Measure uptake and growth phenotypes for a {gene} deletion or depletion strain with putrescine, spermidine, "
            f"norspermidine, and related polyamines, and compare with complementation by the intact {cfg['operon']} locus."
        )
        experiment_type = "targeted polyamine ABC-import mutant uptake/growth assay"
    return [{"description": description, "experiment_type": experiment_type}]


def curate_gene(gene: str, cfg: dict) -> None:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    data = yaml.safe_load(path.read_text())
    rows = goa_rows(gene)

    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_references(data, gene, cfg)

    for ann in data.get("existing_annotations", []):
        if ann.get("review", {}).get("action") == "NEW":
            continue
        term_id = ann["term"]["id"]
        if cfg["kind"] == "atpase":
            ann["review"] = atpase_review(gene, cfg, rows, term_id)
        elif cfg["kind"] == "permease":
            ann["review"] = permease_review(gene, cfg, rows, term_id)
        else:
            ann["review"] = binding_review(gene, cfg, rows, term_id)

    maybe_new_annotations(data, gene, cfg)
    data["core_functions"] = core_functions(gene, cfg, rows)
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions(gene, cfg)
    data["suggested_experiments"] = suggested_experiments(gene, cfg)

    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=1000))
    print(f"curated {path}")


def preferred(term: dict[str, str], preferred_term: str | None = None, description: str | None = None) -> dict:
    entry = {"preferred_term": preferred_term or term["label"], "term": go_term(term)}
    if description:
        entry["description"] = description
    return entry


def annoton(gene: str, cfg: dict) -> dict:
    safe = gene.replace("-", "_")
    participant = {"selector_type": "GENE", "gene": {"preferred_term": gene}}
    if cfg["kind"] == "atpase":
        return {
            "id": f"{safe}_polyamine_import_atpase",
            "label": f"{gene}: {cfg['role']}",
            "participant": participant,
            "function": preferred(ATP_HYDROLYSIS),
            "processes": [preferred(POLYAMINE_TRANSMEMBRANE_TRANSPORT), preferred(PUTRESCINE_TRANSPORT)],
            "role_description": "ATP-binding energy-coupling subunit of a predicted polyamine ABC importer.",
        }
    if cfg["kind"] == "permease":
        return {
            "id": f"{safe}_polyamine_import_permease",
            "label": f"{gene}: {cfg['role']}",
            "participant": participant,
            "function": preferred(ABC_POLYAMINE_TRANSPORTER, "contributes to ABC-type polyamine transporter activity"),
            "processes": [preferred(POLYAMINE_TRANSMEMBRANE_TRANSPORT)],
            "locations": [preferred(PLASMA_MEMBRANE, "plasma membrane")],
            "role_description": "Multi-pass membrane permease subunit of a predicted polyamine ABC importer.",
        }
    entry = {
        "id": f"{safe}_polyamine_binding_component",
        "label": f"{gene}: {cfg['role']}",
        "participant": participant,
        "function": preferred(POLYAMINE_BINDING),
        "processes": [preferred(POLYAMINE_TRANSPORT)],
        "locations": [preferred(PERIPLASM)],
        "role_description": (
            "Periplasmic polyamine-binding component with unresolved transporter partners."
            if cfg["operon"] == "singleton"
            else "Periplasmic substrate-binding component of a predicted polyamine ABC importer."
        ),
    }
    return entry


def update_module() -> None:
    module_doc = yaml.safe_load(MODULE_PATH.read_text())
    evidence = {item["source_id"]: item for item in module_doc.get("evidence", [])}
    evidence["KEGG:ppu02024"] = {
        "source_id": "KEGG:ppu02024",
        "title": "Quorum sensing - Pseudomonas putida KT2440",
        "statement": (
            "KEGG ppu02024 includes several polyamine ABC import components, but these are best curated as "
            "transport systems rather than as direct quorum-sensing genes."
        ),
    }
    for gene, cfg in GENES.items():
        evidence[f"UniProtKB:{cfg['accession']}"] = {
            "source_id": f"UniProtKB:{cfg['accession']}",
            "title": f"{gene} {cfg['role']}",
            "statement": f"UniProt records {gene} ({cfg['locus']}) as {cfg['product_text'].replace('Full=', '')}.",
        }
    module_doc["evidence"] = list(evidence.values())

    module = module_doc["module"]
    concept_ids = {item["term"]["id"] for item in module.get("concepts", [])}
    for term, desc in [
        (POLYAMINE_TRANSMEMBRANE_TRANSPORT, "Membrane import of putrescine, spermidine, norspermidine, or related polyamines."),
        (ABC_PUTRESCINE_TRANSPORTER, "Putrescine-specific ABC transporter activity retained where PotA/PotI context supports it."),
    ]:
        if term["id"] not in concept_ids:
            module.setdefault("concepts", []).append(preferred(term, description=desc))

    parts = [part for part in module.get("parts", []) if part.get("node", {}).get("id") != "ppu02024_polyamine_abc_import_candidates"]
    parts.append(
        {
            "order": max(part.get("order", 0) for part in parts) + 1 if parts else 1,
            "role": "ppu02024 polyamine ABC import candidates",
            "node": {
                "id": "ppu02024_polyamine_abc_import_candidates",
                "label": "ppu02024 polyamine ABC import candidates",
                "module_type": "TRANSPORT_STEP",
                "description": (
                    "The ppu02024-derived polyamine bucket contains the PP_0411-PP_0414 PotA-like locus, "
                    "the ydcV/ydcU/ydcT/ydcS locus, the singleton PP_2870 spermidine/putrescine-binding "
                    "protein, and the PP_3814-PP_3817 locus. These are curated as polyamine transport "
                    "boundaries, not as a single quorum-sensing module."
                ),
                "concepts": [
                    preferred(POLYAMINE_TRANSMEMBRANE_TRANSPORT),
                    preferred(POLYAMINE_TRANSPORT),
                    preferred(POLYAMINE_BINDING),
                    preferred(ABC_POLYAMINE_TRANSPORTER),
                    preferred(ATP_HYDROLYSIS),
                    preferred(ABC_COMPLEX),
                ],
                "annotons": [annoton(gene, cfg) for gene, cfg in GENES.items()],
            },
        }
    )
    module["parts"] = parts
    module_doc["description"] = (
        "Boundary module for Pseudomonas putida KT2440 polyamine transport components encountered during "
        "ppu02010 and ppu02024 ABC-transporter/quorum-sensing-map partitioning. The module separates complete "
        "or near-complete Pot/Spu/Ydc-like polyamine ABC import loci from singleton PotF-like or binding-protein "
        "boundary components whose cognate partners remain unresolved."
    )
    module_doc["notes"] = (
        "This boundary module was seeded from ppu02010 PotF-like and Spu/Pot checkpoints and extended with "
        "ppu02024 polyamine ABC import candidates. The ppu02024 bucket should be treated as transporter "
        "context within a broad KEGG umbrella map, not as evidence for direct LuxI/LuxR-type quorum sensing."
    )
    MODULE_PATH.write_text(yaml.dump(module_doc, Dumper=NoAliasDumper, sort_keys=False, width=1000))
    print(f"updated {MODULE_PATH}")


def main() -> None:
    for gene, cfg in GENES.items():
        curate_gene(gene, cfg)
    update_module()


if __name__ == "__main__":
    main()
