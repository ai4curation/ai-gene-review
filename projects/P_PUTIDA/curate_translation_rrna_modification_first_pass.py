#!/usr/bin/env python3
"""First-pass curation for rRNA modification methyltransferase/pseudouridine genes."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "rrna_modification_ribosome_maturation_boundary.yaml"
BATCH_TSV = (
    "projects/P_PUTIDA/batches/"
    "module_translation_rna_processing_rrna_modification_methyltransferase_pseudouridine.tsv"
)

PRESERVE_EXISTING_REVIEWS = {"rsmG", "rsmJ", "rlmE", "rlmH"}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERM = {
    "GO:0000049": term("GO:0000049", "tRNA binding"),
    "GO:0000154": term("GO:0000154", "rRNA modification"),
    "GO:0000179": term("GO:0000179", "rRNA (adenine-N6,N6-)-dimethyltransferase activity"),
    "GO:0000451": term("GO:0000451", "rRNA 2'-O-methylation"),
    "GO:0000455": term("GO:0000455", "enzyme-directed rRNA pseudouridine synthesis"),
    "GO:0001522": term("GO:0001522", "pseudouridine synthesis"),
    "GO:0002935": term("GO:0002935", "tRNA (adenine(37)-C2)-methyltransferase activity"),
    "GO:0003676": term("GO:0003676", "nucleic acid binding"),
    "GO:0003723": term("GO:0003723", "RNA binding"),
    "GO:0003824": term("GO:0003824", "catalytic activity"),
    "GO:0005506": term("GO:0005506", "iron ion binding"),
    "GO:0005737": term("GO:0005737", "cytoplasm"),
    "GO:0005829": term("GO:0005829", "cytosol"),
    "GO:0006355": term("GO:0006355", "regulation of DNA-templated transcription"),
    "GO:0006364": term("GO:0006364", "rRNA processing"),
    "GO:0006396": term("GO:0006396", "RNA processing"),
    "GO:0008168": term("GO:0008168", "methyltransferase activity"),
    "GO:0008173": term("GO:0008173", "RNA methyltransferase activity"),
    "GO:0008649": term("GO:0008649", "rRNA methyltransferase activity"),
    "GO:0008650": term("GO:0008650", "rRNA (uridine-2'-O-ribose)-methyltransferase activity"),
    "GO:0008757": term("GO:0008757", "S-adenosylmethionine-dependent methyltransferase activity"),
    "GO:0008988": term("GO:0008988", "rRNA (adenine-N6-)-methyltransferase activity"),
    "GO:0008990": term("GO:0008990", "rRNA (guanine-N2-)-methyltransferase activity"),
    "GO:0009383": term("GO:0009383", "rRNA (cytosine-C5-)-methyltransferase activity"),
    "GO:0009451": term("GO:0009451", "RNA modification"),
    "GO:0009982": term("GO:0009982", "pseudouridine synthase activity"),
    "GO:0016433": term("GO:0016433", "rRNA (adenine) methyltransferase activity"),
    "GO:0016866": term("GO:0016866", "intramolecular transferase activity"),
    "GO:0019843": term("GO:0019843", "rRNA binding"),
    "GO:0030488": term("GO:0030488", "tRNA methylation"),
    "GO:0031167": term("GO:0031167", "rRNA methylation"),
    "GO:0032259": term("GO:0032259", "methylation"),
    "GO:0036307": term("GO:0036307", "23S rRNA (adenine(2030)-N(6))-methyltransferase activity"),
    "GO:0036308": term("GO:0036308", "16S rRNA (guanine(1516)-N(2))-methyltransferase activity"),
    "GO:0046872": term("GO:0046872", "metal ion binding"),
    "GO:0051536": term("GO:0051536", "iron-sulfur cluster binding"),
    "GO:0051539": term("GO:0051539", "4 iron, 4 sulfur cluster binding"),
    "GO:0052907": term("GO:0052907", "23S rRNA (adenine(1618)-N(6))-methyltransferase activity"),
    "GO:0052908": term(
        "GO:0052908",
        "16S rRNA (adenine(1518)-N(6)/adenine(1519)-N(6))-dimethyltransferase activity",
    ),
    "GO:0052911": term("GO:0052911", "23S rRNA (guanine(745)-N(1))-methyltransferase activity"),
    "GO:0052913": term("GO:0052913", "16S rRNA (guanine(966)-N(2))-methyltransferase activity"),
    "GO:0052914": term("GO:0052914", "16S rRNA (guanine(1207)-N(2))-methyltransferase activity"),
    "GO:0052915": term("GO:0052915", "23S rRNA (guanine(2445)-N(2))-methyltransferase activity"),
    "GO:0052916": term("GO:0052916", "23S rRNA (guanine(1835)-N(2))-methyltransferase activity"),
    "GO:0062105": term("GO:0062105", "RNA 2'-O-methyltransferase activity"),
    "GO:0070038": term("GO:0070038", "rRNA (pseudouridine-N3-)-methyltransferase activity"),
    "GO:0070039": term("GO:0070039", "rRNA (guanosine-2'-O-ribose)-methyltransferase activity"),
    "GO:0070040": term("GO:0070040", "rRNA (adenine(2503)-C2-)-methyltransferase activity"),
    "GO:0070041": term("GO:0070041", "rRNA (uridine-C5-)-methyltransferase activity"),
    "GO:0070042": term("GO:0070042", "rRNA (uridine-N3-)-methyltransferase activity"),
    "GO:0070043": term("GO:0070043", "rRNA (guanine-N7-)-methyltransferase activity"),
    "GO:0070475": term("GO:0070475", "rRNA base methylation"),
    "GO:0070476": term("GO:0070476", "rRNA (guanine-N7)-methylation"),
    "GO:0070677": term("GO:0070677", "rRNA (cytosine-2'-O-ribose)-methyltransferase activity"),
    "GO:0071424": term("GO:0071424", "rRNA (cytosine-N4-)-methyltransferase activity"),
    "GO:0120159": term("GO:0120159", "rRNA pseudouridine synthase activity"),
    "GO:0140098": term("GO:0140098", "catalytic activity, acting on RNA"),
    "GO:0160136": term("GO:0160136", "16S rRNA pseudouridine(516) synthase activity"),
    "GO:0160138": term("GO:0160138", "23S rRNA pseudouridine(2604) synthase activity"),
    "GO:0160139": term("GO:0160139", "23S rRNA pseudouridine(2605) synthase activity"),
    "GO:0160140": term("GO:0160140", "23S rRNA pseudouridine(1911/1915/1917) synthase activity"),
    "GO:0160141": term("GO:0160141", "23S rRNA pseudouridine(955/2504/2580) synthase activity"),
}

GENES = [
    "rsmG",
    "rsmB",
    "rsmA",
    "rluD",
    "rsmC",
    "rlmN",
    "rlmF",
    "PP_1191",
    "rsmI",
    "rsmH",
    "rsuA",
    "rsmJ",
    "rlmAA",
    "rlmD",
    "rluC",
    "rlmL",
    "PP_2110",
    "rlmM",
    "PP_4306",
    "rluB",
    "rlmG",
    "rlmE",
    "rlmH",
    "rlmB",
    "rlmJ",
    "rsmE",
    "PP_5019",
    "PP_5114",
    "rlmI",
]

SPEC = {
    "rsmG": {
        "description": "rsmG encodes the cytoplasmic 16S rRNA guanine-527 N7 methyltransferase RsmG/GidB, which installs the m7G527 modification during bacterial small-subunit maturation.",
        "core": [
            {
                "description": "16S rRNA guanine-527 N7 methyltransferase activity.",
                "molecular_function": "GO:0070043",
                "directly_involved_in": ["GO:0070476"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rsmB": {
        "description": "rsmB encodes cytoplasmic 16S rRNA cytosine-967 C5 methyltransferase RsmB, a conserved SUN/RsmB-family enzyme that installs m5C967 in small-subunit rRNA.",
        "core": [
            {
                "description": "16S rRNA cytosine-967 C5 methyltransferase activity.",
                "molecular_function": "GO:0009383",
                "directly_involved_in": ["GO:0070475"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rsmA": {
        "description": "rsmA encodes KsgA/RsmA, a cytoplasmic 16S rRNA adenine dimethyltransferase that dimethylates adjacent A1518/A1519 residues near the 3' end of 16S rRNA during 30S biogenesis.",
        "core": [
            {
                "description": "16S rRNA A1518/A1519 N6,N6 dimethyltransferase activity.",
                "molecular_function": "GO:0052908",
                "directly_involved_in": ["GO:0031167"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rluD": {
        "description": "rluD encodes an RluA-family 23S rRNA pseudouridine synthase that converts uridines 1911, 1915, and 1917 in 23S rRNA to pseudouridines.",
        "core": [
            {
                "description": "23S rRNA pseudouridine(1911/1915/1917) synthase activity.",
                "molecular_function": "GO:0160140",
                "directly_involved_in": ["GO:0000455"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rsmC": {
        "description": "rsmC encodes cytoplasmic 16S rRNA guanine-1207 N2 methyltransferase RsmC, which methylates G1207 in the 30S particle.",
        "core": [
            {
                "description": "16S rRNA guanine-1207 N2 methyltransferase activity.",
                "molecular_function": "GO:0052914",
                "directly_involved_in": ["GO:0031167"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rlmN": {
        "description": "rlmN encodes a radical-SAM dual-specificity RNA methyltransferase that C2-methylates A2503 in 23S rRNA and A37 in tRNAs using an iron-sulfur cluster-dependent mechanism.",
        "core": [
            {
                "description": "23S rRNA adenine-2503 C2 methyltransferase activity.",
                "molecular_function": "GO:0070040",
                "directly_involved_in": ["GO:0070475"],
                "locations": ["GO:0005737"],
            },
            {
                "description": "tRNA adenine-37 C2 methyltransferase activity.",
                "molecular_function": "GO:0002935",
                "directly_involved_in": ["GO:0030488"],
                "locations": ["GO:0005737"],
            },
        ],
    },
    "rlmF": {
        "description": "rlmF encodes cytoplasmic 23S rRNA adenine-1618 N6 methyltransferase RlmF, a SAM-dependent large-subunit rRNA methyltransferase.",
        "core": [
            {
                "description": "23S rRNA adenine-1618 N6 methyltransferase activity.",
                "molecular_function": "GO:0052907",
                "directly_involved_in": ["GO:0070475"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "PP_1191": {
        "description": "PP_1191 encodes a dual-specificity RluF-like RNA pseudouridine synthase with a supported 23S rRNA pseudouridine-2604 synthase role and possible tRNA(Tyr) pseudouridylation context.",
        "core": [
            {
                "description": "23S rRNA pseudouridine(2604) synthase activity.",
                "molecular_function": "GO:0160138",
                "directly_involved_in": ["GO:0001522"],
            }
        ],
    },
    "rsmI": {
        "description": "rsmI encodes cytoplasmic 16S rRNA cytidine-1402 2'-O-ribose methyltransferase RsmI.",
        "core": [
            {
                "description": "16S rRNA cytidine-1402 2'-O-ribose methyltransferase activity.",
                "molecular_function": "GO:0070677",
                "directly_involved_in": ["GO:0031167"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rsmH": {
        "description": "rsmH encodes cytoplasmic 16S rRNA cytosine-1402 N4 methyltransferase RsmH/MraW.",
        "core": [
            {
                "description": "16S rRNA cytosine N4 methyltransferase activity at C1402.",
                "molecular_function": "GO:0071424",
                "directly_involved_in": ["GO:0070475"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rsuA": {
        "description": "rsuA encodes RsuA, a 16S rRNA pseudouridine synthase that forms pseudouridine at position 516 in small-subunit rRNA.",
        "core": [
            {
                "description": "16S rRNA pseudouridine(516) synthase activity.",
                "molecular_function": "GO:0160136",
                "directly_involved_in": ["GO:0000455"],
            }
        ],
    },
    "rsmJ": {
        "description": "rsmJ encodes cytoplasmic 16S rRNA guanine-1516 N2 methyltransferase RsmJ.",
        "core": [
            {
                "description": "16S rRNA guanine-1516 N2 methyltransferase activity.",
                "molecular_function": "GO:0036308",
                "directly_involved_in": ["GO:0031167"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rlmAA": {
        "description": "rlmAA encodes 23S rRNA guanine-745 N1 methyltransferase RlmA-like activity.",
        "core": [
            {
                "description": "23S rRNA guanine-745 N1 methyltransferase activity.",
                "molecular_function": "GO:0052911",
            }
        ],
    },
    "rlmD": {
        "description": "rlmD encodes 23S rRNA uridine-1939 C5 methyltransferase RlmD/RumA, an RNA methyltransferase with auxiliary RNA-binding and iron/iron-sulfur context.",
        "core": [
            {
                "description": "23S rRNA uridine-C5 methyltransferase activity.",
                "molecular_function": "GO:0070041",
                "directly_involved_in": ["GO:0031167"],
            }
        ],
    },
    "rluC": {
        "description": "rluC encodes an RluA-family 23S rRNA pseudouridine synthase that modifies uridines 955, 2504, and 2580 in large-subunit rRNA.",
        "core": [
            {
                "description": "23S rRNA pseudouridine(955/2504/2580) synthase activity.",
                "molecular_function": "GO:0160141",
                "directly_involved_in": ["GO:0000455"],
            }
        ],
    },
    "rlmL": {
        "description": "rlmL encodes bifunctional RlmK/RlmL, a large-subunit rRNA methyltransferase with 23S rRNA G2445 N2 and G2069 N7 methyltransferase activities.",
        "core": [
            {
                "description": "23S rRNA guanine-2445 N2 methyltransferase activity.",
                "molecular_function": "GO:0052915",
                "directly_involved_in": ["GO:0031167"],
                "locations": ["GO:0005737"],
            },
            {
                "description": "23S rRNA guanine-2069 N7 methyltransferase activity.",
                "molecular_function": "GO:0070043",
                "directly_involved_in": ["GO:0070476"],
                "locations": ["GO:0005737"],
            },
        ],
    },
    "PP_2110": {
        "description": "PP_2110 encodes a ribosomal large-subunit pseudouridine synthase candidate in the RluA-like family.",
        "core": [
            {
                "description": "Candidate rRNA pseudouridine synthase activity.",
                "molecular_function": "GO:0009982",
                "directly_involved_in": ["GO:0000455"],
            }
        ],
    },
    "rlmM": {
        "description": "rlmM encodes cytoplasmic 23S rRNA cytidine-2498 2'-O-ribose methyltransferase RlmM.",
        "core": [
            {
                "description": "23S rRNA 2'-O-ribose methyltransferase activity.",
                "molecular_function": "GO:0062105",
                "directly_involved_in": ["GO:0006364"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "PP_4306": {
        "description": "PP_4306 encodes a SAM-dependent methyltransferase-domain protein with weak rRNA-methyltransferase family context but no resolved target site.",
        "core": [
            {
                "description": "Candidate SAM-dependent methyltransferase activity with unresolved RNA substrate.",
                "molecular_function": "GO:0008168",
            }
        ],
    },
    "rluB": {
        "description": "rluB encodes 23S rRNA pseudouridine-2605 synthase RluB, an RsuA/RluB-family RNA pseudouridine synthase.",
        "core": [
            {
                "description": "23S rRNA pseudouridine(2605) synthase activity.",
                "molecular_function": "GO:0160139",
                "directly_involved_in": ["GO:0000455"],
                "locations": ["GO:0005829"],
            }
        ],
    },
    "rlmG": {
        "description": "rlmG encodes cytoplasmic 23S rRNA guanine-1835 N2 methyltransferase RlmG.",
        "core": [
            {
                "description": "23S rRNA guanine-1835 N2 methyltransferase activity.",
                "molecular_function": "GO:0052916",
                "directly_involved_in": ["GO:0031167"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rlmE": {
        "description": "rlmE encodes cytoplasmic 23S rRNA uridine-2552 2'-O-ribose methyltransferase RlmE/FtsJ.",
        "core": [
            {
                "description": "23S rRNA uridine-2552 2'-O-ribose methyltransferase activity.",
                "molecular_function": "GO:0008650",
                "directly_involved_in": ["GO:0000451"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rlmH": {
        "description": "rlmH encodes 23S rRNA pseudouridine-1915 N3 methyltransferase RlmH, a SPOUT-family enzyme that methylates a pre-existing pseudouridine in helix 69.",
        "core": [
            {
                "description": "23S rRNA pseudouridine-N3 methyltransferase activity.",
                "molecular_function": "GO:0070038",
                "directly_involved_in": ["GO:0031167"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rlmB": {
        "description": "rlmB encodes 23S rRNA guanosine-2251 2'-O-ribose methyltransferase RlmB.",
        "core": [
            {
                "description": "23S rRNA guanosine-2251 2'-O-ribose methyltransferase activity.",
                "molecular_function": "GO:0070039",
                "directly_involved_in": ["GO:0000451"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "rlmJ": {
        "description": "rlmJ encodes 23S rRNA adenine-2030 N6 methyltransferase RlmJ.",
        "core": [
            {
                "description": "23S rRNA adenine-2030 N6 methyltransferase activity.",
                "molecular_function": "GO:0036307",
                "directly_involved_in": ["GO:0070475"],
                "locations": ["GO:0005829"],
            }
        ],
    },
    "rsmE": {
        "description": "rsmE encodes cytoplasmic 16S rRNA uridine-1498 N3 methyltransferase RsmE.",
        "core": [
            {
                "description": "16S rRNA uridine-1498 N3 methyltransferase activity.",
                "molecular_function": "GO:0070042",
                "directly_involved_in": ["GO:0070475"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "PP_5019": {
        "description": "PP_5019 encodes a second RsmE-family 16S rRNA uridine-1498 N3 methyltransferase candidate.",
        "core": [
            {
                "description": "RsmE-family 16S rRNA uridine-N3 methyltransferase activity.",
                "molecular_function": "GO:0070042",
                "directly_involved_in": ["GO:0070475"],
                "locations": ["GO:0005737"],
            }
        ],
    },
    "PP_5114": {
        "description": "PP_5114 encodes 16S rRNA guanine-966 N2 methyltransferase RsmD-like activity.",
        "core": [
            {
                "description": "16S rRNA guanine-966 N2 methyltransferase activity.",
                "molecular_function": "GO:0052913",
                "directly_involved_in": ["GO:0031167"],
            }
        ],
    },
    "rlmI": {
        "description": "rlmI encodes an RlmI-family SAM-dependent large-subunit rRNA methyltransferase candidate with an unresolved target site in this first pass.",
        "core": [
            {
                "description": "Candidate RlmI-family SAM-dependent rRNA methyltransferase activity with unresolved target site.",
                "molecular_function": "GO:0008168",
            }
        ],
    },
}

REMOVE_TERMS = {"rsmB": {"GO:0006355"}}
COFACTOR_TERMS = {"GO:0051536", "GO:0051539", "GO:0046872", "GO:0005506", "GO:0005737", "GO:0005829"}
BINDING_TERMS = {"GO:0000049", "GO:0003676", "GO:0003723", "GO:0019843"}
BROAD_ACTIVITY_TERMS = {
    "GO:0000179",
    "GO:0003824",
    "GO:0008168",
    "GO:0008173",
    "GO:0008649",
    "GO:0008757",
    "GO:0008988",
    "GO:0008990",
    "GO:0009982",
    "GO:0016433",
    "GO:0016866",
    "GO:0062105",
    "GO:0120159",
    "GO:0140098",
}
BROAD_PROCESS_TERMS = {
    "GO:0000154",
    "GO:0000455",
    "GO:0001522",
    "GO:0006364",
    "GO:0006396",
    "GO:0009451",
    "GO:0031167",
    "GO:0032259",
    "GO:0070475",
}


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


def t(go_id: str) -> dict[str, str]:
    return TERM[go_id]


def line_containing(path: Path, *needles: str) -> str | None:
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8").splitlines():
        if all(needle in line for needle in needles):
            return line
    return None


def support(reference_id: str, text: str | None) -> dict[str, str] | None:
    if not text:
        return None
    return {"reference_id": reference_id, "supporting_text": text}


def add_support(items: list[dict[str, str]], item: dict[str, str] | None) -> None:
    if item and item not in items:
        items.append(item)


def goa_line(gene: str, term_id: str) -> str | None:
    return line_containing(gene_file(gene, "goa.tsv"), term_id)


def evidence_for(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if term_id:
        add_support(items, support(file_id(gene, "goa.tsv"), goa_line(gene, term_id)))
    uniprot = gene_file(gene, "uniprot.txt")
    for marker in (
        "DE   ",
        "CC   -!- FUNCTION:",
        "CC   -!- CATALYTIC ACTIVITY:",
        "CC   -!- COFACTOR:",
        "CC   -!- SUBCELLULAR LOCATION:",
        "CC   -!- SIMILARITY:",
        "DR   GO;",
        "DR   InterPro;",
        "DR   Pfam;",
        "DR   PANTHER;",
        "KW   ",
    ):
        add_support(items, support(file_id(gene, "uniprot.txt"), line_containing(uniprot, marker)))
    return items


def preferred_mfs(gene: str) -> list[str]:
    return [entry["molecular_function"] for entry in SPEC[gene]["core"] if entry.get("molecular_function")]


def preferred_processes(gene: str) -> set[str]:
    out: set[str] = set()
    for entry in SPEC[gene]["core"]:
        out.update(entry.get("directly_involved_in", []))
    return out


def preferred_locations(gene: str) -> set[str]:
    out: set[str] = set()
    for entry in SPEC[gene]["core"]:
        out.update(entry.get("locations", []))
    return out


def make_review(
    summary: str,
    action: str,
    reason: str,
    gene: str,
    term_id: str,
    replacements: list[str] | None = None,
) -> dict:
    out = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": evidence_for(gene, term_id),
    }
    if replacements:
        out["proposed_replacement_terms"] = [t(x) for x in replacements]
    return out


def review_for(gene: str, term_id: str) -> dict:
    term_label = TERM.get(term_id, {"label": term_id})["label"]
    mfs = preferred_mfs(gene)
    processes = preferred_processes(gene)
    locations = preferred_locations(gene)

    if term_id in REMOVE_TERMS.get(gene, set()):
        return make_review(
            f"{term_label} is not supported as a core function for {gene}.",
            "REMOVE",
            "This row is an electronic transfer from a domain that is not the biological role of this conserved rRNA-modification enzyme.",
            gene,
            term_id,
        )

    if term_id in mfs:
        return make_review(
            f"{term_label} is the core molecular function for {gene}.",
            "ACCEPT",
            "The UniProt product name, catalytic-activity/Rhea or family support, and GOA row all match the site or reaction-specific rRNA/RNA modification activity.",
            gene,
            term_id,
        )

    if term_id in processes:
        return make_review(
            f"{term_label} is appropriate biological-process context for {gene}.",
            "ACCEPT",
            "The process captures the rRNA/RNA modification context for the supported catalytic activity.",
            gene,
            term_id,
        )

    if term_id in locations:
        return make_review(
            f"{term_label} is appropriate location context for {gene}.",
            "ACCEPT",
            "The enzyme is a soluble bacterial RNA-modification protein acting in the cytoplasm/cytosol.",
            gene,
            term_id,
        )

    if term_id in COFACTOR_TERMS:
        return make_review(
            f"{term_label} is valid cofactor or compartment context for {gene}.",
            "KEEP_AS_NON_CORE",
            "This annotation is compatible with the enzyme family, but the core function is the RNA-modification reaction rather than localization or cofactor binding.",
            gene,
            term_id,
        )

    if term_id in BINDING_TERMS:
        return make_review(
            f"{term_label} is substrate-binding context for {gene}.",
            "KEEP_AS_NON_CORE",
            "RNA or nucleic-acid binding is expected for this rRNA/RNA modification enzyme, but binding alone is less informative than the catalytic modification activity.",
            gene,
            term_id,
        )

    if term_id in BROAD_ACTIVITY_TERMS:
        replacements = [mfs[0]] if mfs and term_id != mfs[0] else None
        action = "MODIFY" if replacements else "ACCEPT"
        reason = (
            "The row is chemically compatible but broad. The site or reaction-specific rRNA/RNA modification term is the preferred molecular-function representation."
            if replacements
            else "This is the best available molecular-function term for the unresolved candidate in the current first pass."
        )
        return make_review(
            f"{term_label} is broad relative to the best-supported activity for {gene}.",
            action,
            reason,
            gene,
            term_id,
            replacements,
        )

    if term_id in BROAD_PROCESS_TERMS:
        if processes:
            return make_review(
                f"{term_label} is true but broad for {gene}.",
                "KEEP_AS_NON_CORE",
                "The term is consistent with an rRNA/RNA modification enzyme, but the most informative process is the specific methylation or pseudouridylation context recorded in core functions.",
                gene,
                term_id,
            )
        return make_review(
            f"{term_label} is plausible context for {gene}.",
            "KEEP_AS_NON_CORE",
            "The record supports a candidate RNA-modification role, but the target site is unresolved in this first pass.",
            gene,
            term_id,
        )

    return make_review(
        f"{term_label} is retained conservatively for {gene}.",
        "KEEP_AS_NON_CORE",
        "The annotation is not the most specific representation of the gene product's role but is compatible with the available UniProt/GOA evidence.",
        gene,
        term_id,
    )


def references_for(gene: str, data: dict) -> list[dict]:
    seen = set()
    refs: list[dict] = []
    for ref in data.get("references", []):
        if ref.get("id") not in seen:
            refs.append(ref)
            seen.add(ref.get("id"))
    for suffix, title in [
        ("uniprot.txt", f"{gene} UniProt flat-file record"),
        ("goa.tsv", f"{gene} GOA/QuickGO annotation rows"),
        ("deep-research-asta.md", f"{gene} Asta gene-level retrieval report"),
    ]:
        ref_id = file_id(gene, suffix)
        if ref_id not in seen and gene_file(gene, suffix).exists():
            ref = {"id": ref_id, "title": title, "findings": []}
            if suffix == "deep-research-asta.md":
                accession = line_containing(gene_file(gene, suffix), "uniprot_accession:")
                if accession:
                    ref["findings"].append(
                        {
                            "statement": "Asta retrieval was generated for this first-pass review and retained as lightweight identity context.",
                            "supporting_text": accession.strip(),
                        }
                    )
            refs.append(ref)
            seen.add(ref_id)
    return refs


def core_function(gene: str, spec: dict) -> dict:
    out = {"description": spec["description"]}
    support_items: list[dict[str, str]] = []
    if spec.get("molecular_function"):
        mf = spec["molecular_function"]
        out["molecular_function"] = t(mf)
        support_items.extend(evidence_for(gene, mf))
    else:
        support_items.extend(evidence_for(gene))
    if spec.get("directly_involved_in"):
        out["directly_involved_in"] = [t(x) for x in spec["directly_involved_in"]]
        for process_id in spec["directly_involved_in"]:
            add_support(support_items, support(file_id(gene, "goa.tsv"), goa_line(gene, process_id)))
    if spec.get("locations"):
        out["locations"] = [t(x) for x in spec["locations"]]
        for location_id in spec["locations"]:
            add_support(support_items, support(file_id(gene, "goa.tsv"), goa_line(gene, location_id)))
    out["supported_by"] = support_items
    return out


def suggested_question(gene: str) -> list[dict[str, str]]:
    if gene in {"PP_4306", "rlmI"}:
        return [
            {
                "question": f"What is the direct RNA substrate and methylated nucleotide target of {gene} in P. putida KT2440?"
            }
        ]
    if gene in {"rsmE", "PP_5019"}:
        return [
            {
                "question": "Do both RsmE-family paralogs modify 16S rRNA U1498 in KT2440, or are their expression/stress-condition roles specialized?"
            }
        ]
    return [
        {
            "question": f"Under which growth or stress conditions does loss of {gene} measurably affect ribosome assembly, translation fidelity, or fitness in P. putida KT2440?"
        }
    ]


def suggested_experiment(gene: str) -> list[dict[str, str]]:
    return [
        {
            "description": f"Compare wild-type and {gene} perturbation strains by rRNA modification mapping and ribosome-subunit profiling to confirm the predicted target modification and ribosome-maturation phenotype.",
            "experiment_type": "rRNA modification mapping and ribosome profiling",
        }
    ]


def curate_gene(gene: str) -> None:
    path = gene_file(gene, "ai-review.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    if gene not in PRESERVE_EXISTING_REVIEWS:
        data["description"] = SPEC[gene]["description"]
        for ann in data.get("existing_annotations", []):
            go_id = ann["term"]["id"]
            ann["review"] = review_for(gene, go_id)
        data["core_functions"] = [core_function(gene, spec) for spec in SPEC[gene]["core"]]
        data["proposed_new_terms"] = []
        data["suggested_questions"] = suggested_question(gene)
        data["suggested_experiments"] = suggested_experiment(gene)
    data["references"] = references_for(gene, data)
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=True),
        encoding="utf-8",
    )

    notes = [
        f"# {gene} rRNA-modification first-pass notes",
        "",
        "- First-pass curation date: 2026-07-10.",
        f"- Batch: `{BATCH_TSV}`.",
        f"- Asta retrieval report: `{file_id(gene, 'deep-research-asta.md')}`. The report is retained as provenance; annotation decisions are supported primarily by local UniProt and GOA rows.",
        f"- Main conclusion: {SPEC[gene]['core'][0]['description']}",
    ]
    if gene in PRESERVE_EXISTING_REVIEWS:
        notes.append("- Existing Falcon-backed review decisions were preserved; this pass added Asta coverage and batch/module bookkeeping.")
    gene_file(gene, "notes.md").write_text("\n".join(notes) + "\n", encoding="utf-8")


def clean_id(text: str) -> str:
    out = re.sub(r"[^A-Za-z0-9_]+", "_", text.lower())
    out = re.sub(r"_+", "_", out).strip("_")
    return out


def annoton(gene: str, label: str, role: str, function_id: str | None, processes: list[str] | None = None, locations: list[str] | None = None) -> dict:
    out = {
        "id": f"{clean_id(gene)}_{clean_id(label)}",
        "label": f"{gene}: {label}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "role_description": role,
    }
    if function_id:
        out["function"] = {"preferred_term": TERM[function_id]["label"], "term": t(function_id)}
    if processes:
        out["processes"] = [{"preferred_term": TERM[x]["label"], "term": t(x)} for x in processes]
    if locations:
        out["locations"] = [{"preferred_term": TERM[x]["label"], "term": t(x)} for x in locations]
    return out


def annotons_for(genes: list[str]) -> list[dict]:
    out = []
    for gene in genes:
        for index, core in enumerate(SPEC[gene]["core"], start=1):
            label = core["description"]
            if len(SPEC[gene]["core"]) > 1:
                label = f"{label} ({index})"
            out.append(
                annoton(
                    gene,
                    label,
                    core["description"],
                    core.get("molecular_function"),
                    core.get("directly_involved_in"),
                    core.get("locations"),
                )
            )
    return out


def write_module() -> None:
    module = {
        "id": "MODULE:rrna_modification_ribosome_maturation_boundary",
        "title": "rRNA modification and ribosome maturation boundary",
        "description": (
            "Boundary module for PSEPK rRNA methyltransferases and pseudouridine synthases from the translation/RNA-processing "
            "umbrella. The module keeps site-specific 16S/23S rRNA methylation and pseudouridylation reactions distinct from "
            "generic RNA binding, broad methyltransferase, and unresolved methyltransferase-domain side nodes."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_TSV}",
                "title": "PSEPK translation/RNA rRNA modification split",
                "statement": "The batch records Rsm/Rlm/Rlu/Rsu-family rRNA methyltransferases and pseudouridine synthases, including dual rRNA/tRNA enzymes and unresolved methyltransferase-domain side nodes.",
            }
        ]
        + [
            {
                "source_id": file_id(gene, "ai-review.yaml"),
                "title": f"Curated {gene} review",
                "statement": SPEC[gene]["description"],
            }
            for gene in GENES
        ],
        "module": {
            "id": "rrna_modification_ribosome_maturation_boundary",
            "label": "rRNA modification and ribosome maturation boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {"preferred_term": TERM[x]["label"], "term": t(x)}
                for x in [
                    "GO:0031167",
                    "GO:0070475",
                    "GO:0000455",
                    "GO:0070476",
                    "GO:0000451",
                    "GO:0009982",
                    "GO:0008168",
                ]
            ],
            "parts": [
                {
                    "order": 1,
                    "role": "16S rRNA methyltransferases",
                    "node": {
                        "id": "small_subunit_rrna_methyltransferases",
                        "label": "16S rRNA methyltransferases",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "Small-subunit Rsm-family enzymes installing site-specific methyl marks in 16S rRNA.",
                        "annotons": annotons_for(["rsmG", "rsmB", "rsmA", "rsmC", "rsmI", "rsmH", "rsmJ", "rsmE", "PP_5019", "PP_5114"]),
                    },
                },
                {
                    "order": 2,
                    "role": "23S rRNA methyltransferases and dual RNA methyltransferases",
                    "node": {
                        "id": "large_subunit_rrna_methyltransferases",
                        "label": "23S rRNA methyltransferases",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "Large-subunit Rlm-family enzymes and dual RNA methyltransferases acting on 23S rRNA and, for RlmN, tRNA.",
                        "annotons": annotons_for(["rlmN", "rlmF", "rlmAA", "rlmD", "rlmL", "rlmM", "PP_4306", "rlmG", "rlmE", "rlmH", "rlmB", "rlmJ", "rlmI"]),
                    },
                },
                {
                    "order": 3,
                    "role": "rRNA pseudouridine synthases",
                    "node": {
                        "id": "rrna_pseudouridine_synthases",
                        "label": "rRNA pseudouridine synthases",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "Rlu/Rsu-family enzymes that isomerize specific uridines in 16S or 23S rRNA to pseudouridines.",
                        "annotons": annotons_for(["rluD", "PP_1191", "rsuA", "rluC", "PP_2110", "rluB"]),
                    },
                },
            ],
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, width=120, allow_unicode=True),
        encoding="utf-8",
    )


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
    write_module()


if __name__ == "__main__":
    main()
