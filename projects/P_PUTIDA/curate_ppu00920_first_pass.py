#!/usr/bin/env python3
"""First-pass curation for the PSEPK ppu00920 sulfur-metabolism batch."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


BATCH = Path("projects/P_PUTIDA/batches/ppu00920_sulfur_metabolism_boundary.tsv")


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


CONFIG: dict[str, dict] = {
    "PP_0053": {
        "description": "PP_0053 encodes a predicted sulfide:quinone oxidoreductase, a membrane-associated flavoprotein-type sulfur redox enzyme that transfers electrons from sulfide to quinone or a related acceptor.",
        "accept": {"GO:0016672", "GO:0070224"},
        "non_core": {"GO:0005737", "GO:0071949"},
        "over": {"GO:0016491"},
        "core": [
            {
                "description": "Predicted sulfide:quinone oxidoreductase activity in sulfur redox metabolism.",
                "molecular_function": term("GO:0070224", "sulfide:quinone oxidoreductase activity"),
            }
        ],
    },
    "PP_0170": {
        "description": "PP_0170 encodes an ABC-transporter periplasmic binding protein in a sulfur-metabolism KEGG neighborhood, but the fetched GOA table has no GO annotations and the transported substrate remains unresolved in this first pass.",
        "core": [
            {
                "description": "Predicted ABC-transporter solute-binding component with unresolved sulfur/nitrogen substrate specificity.",
            }
        ],
        "questions": [
            "What substrate does the PP_0170/PP_0171/PP_0172/PP_0208 ABC-transporter neighborhood import in KT2440?"
        ],
    },
    "PP_0171": {
        "description": "PP_0171 encodes a predicted ABC-transporter ATP-binding protein in the ppu00920 boundary set; current annotations support generic ABC ATPase features but not a resolved transported sulfur compound.",
        "non_core": {"GO:0000166", "GO:0005524", "GO:0016887"},
        "core": [
            {
                "description": "Predicted ABC-transporter ATPase component; transported substrate remains unresolved.",
            }
        ],
        "questions": [
            "Is PP_0171 the ATPase for a sulfonate/taurine transporter, a nitrate-related transporter, or another import system?"
        ],
    },
    "PP_0172": {
        "description": "PP_0172 encodes a predicted ABC-transporter permease in the ppu00920 boundary set. Existing GOA terms support membrane/ABC-transporter context but do not resolve the imported substrate.",
        "non_core": {"GO:0005886", "GO:0016020", "GO:0043190", "GO:0055085"},
        "core": [
            {
                "description": "Predicted ABC-transporter permease component with unresolved sulfur/nitrogen substrate specificity.",
            }
        ],
    },
    "PP_0207": {
        "description": "PP_0207 encodes a putative aliphatic-sulfonate-binding protein, suggesting a periplasmic solute-binding role in organosulfur uptake, but the fetched GOA table has no GO annotations.",
        "core": [
            {
                "description": "Predicted aliphatic-sulfonate-binding component of an organosulfur import system.",
            }
        ],
        "questions": [
            "Which aliphatic sulfonate or related organosulfur substrates are bound by PP_0207 in KT2440?"
        ],
    },
    "PP_0208": {
        "description": "PP_0208 encodes a predicted ABC-transporter permease whose UniProt product name says nitrate ABC transporter, while GOA places it in alkanesulfonate transport. It is retained as an unresolved transporter boundary candidate.",
        "undecided": {"GO:0042918"},
        "non_core": {"GO:0005886", "GO:0016020", "GO:0043190", "GO:0055085"},
        "core": [
            {
                "description": "Predicted ABC-transporter permease with unresolved nitrate-versus-alkanesulfonate substrate specificity.",
            }
        ],
        "questions": [
            "Does PP_0208 import alkanesulfonates, nitrate, or another solute in KT2440?"
        ],
    },
    "tauB-I": {
        "description": "tauB-I encodes an ATP-binding taurine-transporter subunit, likely supplying ATP hydrolysis for a taurine or related organosulfonate ABC import system.",
        "accept": {"GO:0016887"},
        "non_core": {"GO:0000166", "GO:0005524"},
        "core": [
            {
                "description": "ATP hydrolysis by a predicted taurine/organosulfonate ABC-transporter ATP-binding subunit.",
                "molecular_function": term("GO:0016887", "ATP hydrolysis activity"),
            }
        ],
    },
    "tauC": {
        "description": "tauC encodes a taurine ABC-transporter permease subunit, a membrane component of organosulfonate/taurine import used during sulfur-source acquisition.",
        "accept": {"GO:0042918"},
        "non_core": {"GO:0005886", "GO:0010438", "GO:0016020", "GO:0043190", "GO:0055085"},
        "core": [
            {
                "description": "Predicted membrane permease component for alkanesulfonate/taurine import.",
                "directly_involved_in": [term("GO:0042918", "alkanesulfonate transmembrane transport")],
            }
        ],
    },
    "tauB": {
        "description": "tauB encodes the ATP-binding subunit of a taurine ABC importer, supporting taurine and related alkanesulfonate uptake for sulfur acquisition.",
        "accept": {"GO:0015411", "GO:0015734", "GO:0042918"},
        "non_core": {"GO:0005524", "GO:0005886", "GO:0016887"},
        "core": [
            {
                "description": "ATP-dependent taurine ABC-transporter activity for taurine/organosulfonate uptake.",
                "molecular_function": term("GO:0015411", "ABC-type taurine transporter transporter activity"),
                "directly_involved_in": [term("GO:0015734", "taurine transmembrane transport")],
            }
        ],
    },
    "tauA": {
        "description": "tauA encodes the periplasmic binding subunit of a taurine/alkanesulfonate ABC transporter, linking organosulfonate recognition to import.",
        "accept": {"GO:0042918"},
        "non_core": {"GO:0042597"},
        "core": [
            {
                "description": "Periplasmic binding component of a predicted alkanesulfonate/taurine import system.",
                "directly_involved_in": [term("GO:0042918", "alkanesulfonate transmembrane transport")],
            }
        ],
    },
    "ssuA": {
        "description": "ssuA encodes a putative aliphatic-sulfonate-binding component of the SsuABC organosulfur import system.",
        "non_core": {"GO:0016020", "GO:0042597", "GO:0042626", "GO:0055085"},
        "core": [
            {
                "description": "Predicted aliphatic-sulfonate-binding component of the SsuABC importer.",
            }
        ],
        "questions": [
            "What aliphatic sulfonate substrate range does KT2440 SsuA recognize?"
        ],
    },
    "ssuC": {
        "description": "ssuC encodes the permease subunit of an aliphatic-sulfonate ABC transporter, likely partnering with SsuA/SsuB for organosulfur import.",
        "accept": {"GO:0042918"},
        "non_core": {"GO:0005886", "GO:0016020", "GO:0043190", "GO:0055085"},
        "core": [
            {
                "description": "Aliphatic-sulfonate ABC-transporter permease role in organosulfur uptake.",
                "directly_involved_in": [term("GO:0042918", "alkanesulfonate transmembrane transport")],
            }
        ],
    },
    "ssuB": {
        "description": "ssuB encodes the ATP-binding protein of an aliphatic-sulfonate import ABC transporter, supplying ATP-dependent transport energy for organosulfur uptake.",
        "accept": {"GO:0042918"},
        "non_core": {"GO:0005524", "GO:0005886", "GO:0016887"},
        "core": [
            {
                "description": "ATP-binding component of the SsuABC alkanesulfonate import system.",
                "directly_involved_in": [term("GO:0042918", "alkanesulfonate transmembrane transport")],
            }
        ],
    },
    "cysQ": {
        "description": "cysQ encodes 3'(2'),5'-bisphosphate nucleotidase/PAP phosphatase, recycling phosphorylated nucleotide intermediates associated with PAPS/APS use during sulfate assimilation.",
        "accept": {"GO:0000103", "GO:0008441", "GO:0050427"},
        "non_core": {"GO:0000287", "GO:0005886", "GO:0006790"},
        "core": [
            {
                "description": "3'(2'),5'-bisphosphate nucleotidase activity supporting sulfate assimilation and PAPS/PAP metabolism.",
                "molecular_function": term("GO:0008441", "3'(2'),5'-bisphosphate nucleotidase activity"),
                "directly_involved_in": [term("GO:0050427", "3'-phosphoadenosine 5'-phosphosulfate metabolic process")],
            }
        ],
    },
    "glpE": {
        "description": "glpE encodes a rhodanese-like thiosulfate sulfurtransferase, supporting sulfur-transfer chemistry in the sulfur-metabolism boundary set.",
        "accept": {"GO:0004792", "GO:0103041"},
        "non_core": {"GO:0005737"},
        "core": [
            {
                "description": "Thiosulfate sulfurtransferase activity by a rhodanese-like GlpE protein.",
                "molecular_function": term("GO:0004792", "thiosulfate-cyanide sulfurtransferase activity"),
            },
            {
                "description": "Thiosulfate-thioredoxin sulfurtransferase activity predicted for GlpE.",
                "molecular_function": term("GO:0103041", "thiosulfate-thioredoxin sulfurtransferase activity"),
            },
        ],
    },
    "PP_0860": {
        "description": "PP_0860 encodes a predicted sulfite-reductase flavoprotein component, providing flavin-dependent electron-transfer capacity in assimilatory sulfite reduction.",
        "accept": {"GO:0016655"},
        "non_core": {"GO:0010181"},
        "over": {"GO:0016491"},
        "core": [
            {
                "description": "Flavin-dependent oxidoreductase component associated with sulfite reduction.",
                "molecular_function": term("GO:0016655", "oxidoreductase activity, acting on NAD(P)H, quinone or similar compound as acceptor"),
            }
        ],
    },
    "PP_1703": {
        "description": "PP_1703 encodes an assimilatory nitrate-reductase/sulfite-reductase family enzyme with predicted sulfite reductase and nitrate reductase activities, placing it at the sulfur/nitrogen redox boundary.",
        "accept": {"GO:0004783", "GO:0050140"},
        "non_core": {"GO:0010181", "GO:0016020", "GO:0043546", "GO:0045333", "GO:0051539"},
        "over": {"GO:0016491", "GO:0016655"},
        "core": [
            {
                "description": "Predicted assimilatory sulfite reductase activity.",
                "molecular_function": term("GO:0004783", "sulfite reductase (NADPH) activity"),
            },
            {
                "description": "Predicted nitrate reductase activity retained as nitrogen-metabolism overlap for this sulfur-boundary enzyme.",
                "molecular_function": term("GO:0050140", "nitrate reductase (cytochrome) activity"),
            },
        ],
    },
    "PP_2048": {
        "description": "PP_2048 encodes a predicted 3-methylmercaptopropionyl-CoA dehydrogenase, an acyl-CoA dehydrogenase-family enzyme connected to organosulfur CoA-thioester metabolism.",
        "accept": {"GO:0016627"},
        "non_core": {"GO:0050660"},
        "core": [
            {
                "description": "Predicted 3-methylmercaptopropionyl-CoA dehydrogenase activity in organosulfur CoA-thioester metabolism.",
                "molecular_function": term("GO:0016627", "oxidoreductase activity, acting on the CH-CH group of donors"),
            }
        ],
    },
    "cysH": {
        "description": "cysH encodes thioredoxin-dependent adenylyl-sulfate reductase/APS reductase, reducing activated sulfate intermediates during assimilatory sulfate reduction toward cysteine biosynthesis.",
        "accept": {"GO:0004604", "GO:0019344", "GO:0043866", "GO:0070814"},
        "non_core": {"GO:0005737", "GO:0051539"},
        "over": {"GO:0003824"},
        "core": [
            {
                "description": "Thioredoxin-dependent adenylyl-sulfate reductase step in assimilatory sulfate reduction.",
                "molecular_function": term("GO:0043866", "adenylyl-sulfate reductase (thioredoxin) activity"),
                "directly_involved_in": [term("GO:0019344", "L-cysteine biosynthetic process")],
            }
        ],
    },
    "cysI": {
        "description": "cysI encodes a sulfite-reductase hemoprotein/beta subunit, a heme and iron-sulfur component of assimilatory sulfite reduction.",
        "non_core": {"GO:0020037", "GO:0051536"},
        "over": {"GO:0016491"},
        "core": [
            {
                "description": "Hemoprotein subunit of assimilatory sulfite reductase; current GOA lacks a specific sulfite-reductase subunit molecular-function term.",
            }
        ],
        "questions": [
            "Which GO molecular-function term best represents the CysI hemoprotein subunit of KT2440 sulfite reductase?"
        ],
    },
    "PP_2677": {
        "description": "PP_2677 encodes a quinoprotein-dehydrogenase-associated SoxYZ-like carrier, suggesting a sulfur-carrier or sulfur-oxidation boundary role, but the fetched GOA table has no GO annotations.",
        "core": [
            {
                "description": "Predicted SoxYZ-like sulfur-carrier protein with unresolved exact role in KT2440 sulfur redox metabolism.",
            }
        ],
        "questions": [
            "Does PP_2677 function as a SoxYZ-like sulfur carrier in KT2440, and what reaction partners use it?"
        ],
    },
    "PP_2765": {
        "description": "PP_2765 encodes a predicted MsuD/SsuD-family alkanesulfonate monooxygenase for oxidative desulfonation of organosulfur compounds.",
        "accept": {"GO:0008726", "GO:0046306"},
        "over": {"GO:0016705"},
        "core": [
            {
                "description": "Predicted alkanesulfonate monooxygenase activity during alkanesulfonate catabolism.",
                "molecular_function": term("GO:0008726", "alkanesulfonate monooxygenase activity"),
                "directly_involved_in": [term("GO:0046306", "alkanesulfonate catabolic process")],
            }
        ],
    },
    "PP_2795": {
        "description": "PP_2795 encodes an ATP-dependent AMP-binding enzyme-family protein in the sulfur-metabolism boundary set; no GOA rows currently resolve its substrate or reaction.",
        "core": [
            {
                "description": "Predicted AMP-binding enzyme-family protein with unresolved organosulfur CoA/AMP-linked role.",
            }
        ],
        "questions": [
            "What substrate is activated by PP_2795, and is it part of methanethiol, methylmercaptopropionate, or another organosulfur branch?"
        ],
    },
    "PP_3217": {
        "description": "PP_3217 encodes a putative aliphatic-sulfonate-binding protein, likely a periplasmic solute-binding component for organosulfur import.",
        "non_core": {"GO:0016020", "GO:0042597", "GO:0042626", "GO:0055085"},
        "core": [
            {
                "description": "Predicted aliphatic-sulfonate-binding component of an organosulfur uptake system.",
            }
        ],
    },
    "PP_3219": {
        "description": "PP_3219 encodes a predicted alkanesulfonate monooxygenase, likely catalyzing oxidative desulfonation in an organosulfur catabolic cluster.",
        "accept": {"GO:0008726", "GO:0046306"},
        "over": {"GO:0016705"},
        "core": [
            {
                "description": "Predicted alkanesulfonate monooxygenase activity during alkanesulfonate catabolism.",
                "molecular_function": term("GO:0008726", "alkanesulfonate monooxygenase activity"),
                "directly_involved_in": [term("GO:0046306", "alkanesulfonate catabolic process")],
            }
        ],
    },
    "PP_3228": {
        "description": "PP_3228 encodes a putative aliphatic-sulfonate-binding protein, likely a periplasmic solute-binding component for organosulfur import.",
        "non_core": {"GO:0016020", "GO:0042626", "GO:0055085"},
        "core": [
            {
                "description": "Predicted aliphatic-sulfonate-binding component of an organosulfur uptake system.",
            }
        ],
    },
    "PP_3229": {
        "description": "PP_3229 encodes a putative aliphatic-sulfonate-binding protein, likely a periplasmic solute-binding component for organosulfur import.",
        "non_core": {"GO:0016020", "GO:0042597", "GO:0042626", "GO:0055085"},
        "core": [
            {
                "description": "Predicted aliphatic-sulfonate-binding component of an organosulfur uptake system.",
            }
        ],
    },
    "PP_3528": {
        "description": "PP_3528 encodes a putative aliphatic-sulfonate-binding protein, likely a periplasmic solute-binding component for organosulfur import.",
        "non_core": {"GO:0016020", "GO:0042597", "GO:0042626", "GO:0055085"},
        "core": [
            {
                "description": "Predicted aliphatic-sulfonate-binding component of an organosulfur uptake system.",
            }
        ],
    },
    "PP_3553": {
        "description": "PP_3553 encodes an ATP-dependent AMP-binding enzyme-family protein adjacent to organosulfur CoA-thioester candidates, but the fetched GOA table has no GO annotations resolving its reaction.",
        "core": [
            {
                "description": "Predicted AMP-binding enzyme-family protein with unresolved organosulfur CoA/AMP-linked role.",
            }
        ],
        "questions": [
            "What substrate is activated by PP_3553, and does it pair functionally with PP_3554?"
        ],
    },
    "PP_3554": {
        "description": "PP_3554 encodes a predicted 3-methylmercaptopropionyl-CoA dehydrogenase, an acyl-CoA dehydrogenase-family enzyme connected to organosulfur CoA-thioester metabolism.",
        "accept": {"GO:0016627"},
        "non_core": {"GO:0050660"},
        "core": [
            {
                "description": "Predicted 3-methylmercaptopropionyl-CoA dehydrogenase activity in organosulfur CoA-thioester metabolism.",
                "molecular_function": term("GO:0016627", "oxidoreductase activity, acting on the CH-CH group of donors"),
            }
        ],
    },
    "PP_3822": {
        "description": "PP_3822 encodes a cytochrome c-family protein, likely serving as an electron-transfer component in a sulfur redox or dehydrogenase-associated boundary system.",
        "accept": {"GO:0009055"},
        "non_core": {"GO:0020037"},
        "core": [
            {
                "description": "Cytochrome c-family electron-transfer activity in a sulfur-redox boundary context.",
                "molecular_function": term("GO:0009055", "electron transfer activity"),
            }
        ],
    },
    "sbp-I": {
        "description": "sbp-I encodes a sulfate ABC-transporter periplasmic binding component, supporting sulfate uptake for assimilatory sulfur metabolism.",
        "accept": {"GO:0140104", "GO:1902358"},
        "non_core": {"GO:0042597"},
        "core": [
            {
                "description": "Sulfate transporter carrier/binding component supporting sulfate transmembrane transport.",
                "molecular_function": term("GO:0140104", "molecular carrier activity"),
                "directly_involved_in": [term("GO:1902358", "sulfate transmembrane transport")],
            }
        ],
    },
    "cysA": {
        "description": "cysA encodes the ATP-binding component of the sulfate/thiosulfate ABC importer, coupling ATP hydrolysis to sulfate and thiosulfate uptake.",
        "accept": {"GO:0015419", "GO:0015709", "GO:0102025", "GO:1902358"},
        "non_core": {"GO:0005524", "GO:0005886", "GO:0016020", "GO:0016887", "GO:0043190"},
        "core": [
            {
                "description": "ABC-type sulfate/thiosulfate transporter ATP-binding component.",
                "molecular_function": term("GO:0015419", "ABC-type sulfate transporter activity"),
                "directly_involved_in": [term("GO:1902358", "sulfate transmembrane transport")],
            },
            {
                "description": "ABC-type thiosulfate transporter activity associated with the CysAWU/Sbp import system.",
                "molecular_function": term("GO:0102025", "ABC-type thiosulfate transporter activity"),
                "directly_involved_in": [term("GO:0015709", "thiosulfate transport")],
            },
        ],
    },
    "cysW": {
        "description": "cysW encodes a membrane permease of the sulfate ABC transporter, supporting sulfate uptake during sulfur assimilation.",
        "accept": {"GO:0015419", "GO:1902358"},
        "non_core": {"GO:0005886", "GO:0016020", "GO:0043190", "GO:0055085"},
        "core": [
            {
                "description": "Sulfate ABC-transporter permease activity in sulfate uptake.",
                "molecular_function": term("GO:0015419", "ABC-type sulfate transporter activity"),
                "directly_involved_in": [term("GO:1902358", "sulfate transmembrane transport")],
            }
        ],
    },
    "cysU": {
        "description": "cysU encodes the second membrane permease of the sulfate ABC transporter, partnering with CysW/CysA and sulfate-binding proteins for sulfate uptake.",
        "accept": {"GO:0015419", "GO:1902358"},
        "non_core": {"GO:0005886", "GO:0016020", "GO:0043190", "GO:0055085"},
        "core": [
            {
                "description": "Sulfate ABC-transporter permease activity in sulfate uptake.",
                "molecular_function": term("GO:0015419", "ABC-type sulfate transporter activity"),
                "directly_involved_in": [term("GO:1902358", "sulfate transmembrane transport")],
            }
        ],
    },
    "sbp-II": {
        "description": "sbp-II encodes a second sulfate ABC-transporter binding protein with sulfur-compound-binding annotation, supporting sulfate uptake for assimilatory sulfur metabolism.",
        "accept": {"GO:1901681", "GO:1902358"},
        "non_core": {"GO:0042597", "GO:0140104"},
        "core": [
            {
                "description": "Sulfur-compound binding by a sulfate-transporter binding protein during sulfate uptake.",
                "molecular_function": term("GO:1901681", "sulfur compound binding"),
                "directly_involved_in": [term("GO:1902358", "sulfate transmembrane transport")],
            }
        ],
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def file_title(kind: str, gene: str) -> str:
    if kind == "uniprot":
        return f"UniProt entry for {gene}"
    if kind == "goa":
        return f"QuickGO GOA annotations for {gene}"
    if kind == "asta":
        return f"Asta retrieval report for {gene}"
    raise ValueError(kind)


def uniprot_snippet(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if "Full=" in line:
            return line.strip()
    match = re.search(r"AC\s+([A-Z0-9]+);", text)
    if match:
        return f"AC   {match.group(1)};"
    return text.splitlines()[0]


def goa_snippet(annotation: dict[str, str]) -> str:
    return f"{annotation['GO TERM']}\t{annotation['GO NAME']}"


def ensure_file_references(data: dict, gene: str, accession: str, gene_dir: Path) -> None:
    references = list(data.get("references") or [])
    by_id = {ref.get("id"): ref for ref in references}
    additions: list[dict] = []

    uniprot = gene_dir / f"{gene}-uniprot.txt"
    if uniprot.exists():
        ref_id = f"file:PSEPK/{gene}/{gene}-uniprot.txt"
        if ref_id not in by_id:
            additions.append(
                {
                    "id": ref_id,
                    "title": file_title("uniprot", gene),
                    "findings": [
                        {
                            "statement": "UniProt provides the protein identity and first-pass functional context used for this review.",
                            "supporting_text": uniprot_snippet(uniprot),
                        }
                    ],
                }
            )

    goa = gene_dir / f"{gene}-goa.tsv"
    if goa.exists():
        ref_id = f"file:PSEPK/{gene}/{gene}-goa.tsv"
        if ref_id not in by_id:
            additions.append(
                {
                    "id": ref_id,
                    "title": file_title("goa", gene),
                    "findings": [
                        {
                            "statement": "The fetched GOA table contains the annotations reviewed for this gene.",
                        }
                    ],
                }
            )

    asta = gene_dir / f"{gene}-deep-research-asta.md"
    if asta.exists():
        ref_id = f"file:PSEPK/{gene}/{gene}-deep-research-asta.md"
        if ref_id not in by_id:
            additions.append(
                {
                    "id": ref_id,
                    "title": file_title("asta", gene),
                    "findings": [
                        {
                            "statement": "Asta retrieval was generated for this first-pass review and used as lightweight identity/literature context.",
                            "supporting_text": f"uniprot_accession: {accession}",
                        }
                    ],
                }
            )

    data["references"] = references + additions


def action_label(action: str) -> str:
    return {
        "ACCEPT": "Accepted",
        "KEEP_AS_NON_CORE": "Retained as non-core",
        "MARK_AS_OVER_ANNOTATED": "Marked as over-annotated",
        "MODIFY": "Modified",
        "REMOVE": "Removed",
        "UNDECIDED": "Left undecided",
    }[action]


def classify(annotation: dict[str, str], cfg: dict) -> tuple[str, dict | None]:
    go_id = annotation["GO TERM"]
    if go_id in cfg.get("accept", set()):
        return "ACCEPT", None
    if go_id in cfg.get("non_core", set()):
        return "KEEP_AS_NON_CORE", None
    if go_id in cfg.get("over", set()):
        return "MARK_AS_OVER_ANNOTATED", None
    if go_id in cfg.get("undecided", set()):
        return "UNDECIDED", None
    if go_id in cfg.get("modify", {}):
        return "MODIFY", cfg["modify"][go_id]
    if annotation["GO ASPECT"] == "cellular_component":
        return "KEEP_AS_NON_CORE", None
    name = annotation["GO NAME"]
    if "binding" in name or name in {"molecular carrier activity", "ATP hydrolysis activity"}:
        return "KEEP_AS_NON_CORE", None
    if name in {
        "catalytic activity",
        "oxidoreductase activity",
        "oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen",
        "oxidoreductase activity, acting on NAD(P)H, quinone or similar compound as acceptor",
        "ATPase-coupled transmembrane transporter activity",
        "transmembrane transport",
    }:
        return "MARK_AS_OVER_ANNOTATED", None
    return "KEEP_AS_NON_CORE", None


def reason_for(action: str, annotation: dict[str, str], replacement: dict | None) -> str:
    label = annotation["GO NAME"]
    if action == "ACCEPT":
        return (
            f"{label} matches the fetched GOA/UniProt identity for this ppu00920 first-pass review "
            "and is consistent with the sulfur-metabolism boundary role recorded for this gene."
        )
    if action == "KEEP_AS_NON_CORE":
        return (
            f"{label} is plausible supporting context for this protein, but it is a location, cofactor, "
            "generic transporter/ATPase feature, or broad side-process annotation rather than the most informative core role."
        )
    if action == "MARK_AS_OVER_ANNOTATED":
        return (
            f"{label} is compatible with the protein family but broader than the specific sulfur transporter, "
            "sulfur redox, desulfonation, or assimilation role supported by UniProt/GOA in this batch."
        )
    if action == "MODIFY" and replacement:
        return (
            f"The annotation captures the right general area but should be represented by the more specific "
            f"{replacement['label']} term for this protein."
        )
    if action == "REMOVE":
        return "This annotation is inconsistent with the fetched protein identity and pathway context."
    if action == "UNDECIDED":
        return (
            f"{label} is plausible in the KEGG sulfur bucket, but the UniProt product name and electronic GOA context "
            "do not yet resolve this protein's substrate specificity. This needs targeted transporter evidence."
        )
    raise AssertionError(action)


def review_annotation(
    gene: str,
    annotation: dict,
    goa_by_id_label: dict[tuple[str, str], dict[str, str]],
    cfg: dict,
) -> None:
    term_data = annotation["term"]
    go_id = term_data["id"]
    label = term_data["label"]
    goa_row = goa_by_id_label.get((go_id, label))
    if goa_row is None:
        goa_row = next((row for (gid, _), row in goa_by_id_label.items() if gid == go_id), None)
    action, replacement = classify(goa_row or {"GO TERM": go_id, "GO NAME": label, "GO ASPECT": ""}, cfg)
    review = {
        "summary": f"{action_label(action)}: {label} for {gene} in the ppu00920 sulfur-metabolism first-pass review.",
        "action": action,
        "reason": reason_for(action, goa_row or {"GO NAME": label}, replacement),
    }
    if replacement is not None:
        review["proposed_replacement_terms"] = [replacement]
    if goa_row is not None:
        review["supported_by"] = [
            {
                "reference_id": f"file:PSEPK/{gene}/{gene}-goa.tsv",
                "supporting_text": goa_snippet(goa_row),
            }
        ]
    annotation["review"] = review


def support_for_core(gene: str, core: dict, goa_rows: list[dict[str, str]], uniprot: Path) -> list[dict[str, str]]:
    support: list[dict[str, str]] = []
    term_ids: set[str] = set()
    for slot in ("molecular_function", "contributes_to_molecular_function"):
        if slot in core:
            term_ids.add(core[slot]["id"])
    for item in core.get("directly_involved_in", []) or []:
        term_ids.add(item["id"])
    for item in core.get("locations", []) or []:
        term_ids.add(item["id"])
    for row in goa_rows:
        if row["GO TERM"] in term_ids:
            support.append(
                {
                    "reference_id": f"file:PSEPK/{gene}/{gene}-goa.tsv",
                    "supporting_text": goa_snippet(row),
                }
            )
    if uniprot.exists():
        support.append(
            {
                "reference_id": f"file:PSEPK/{gene}/{gene}-uniprot.txt",
                "supporting_text": uniprot_snippet(uniprot),
            }
        )
    return support


def suggested_questions(cfg: dict) -> list[dict[str, str]]:
    return [{"question": question} for question in cfg.get("questions", [])]


def curate(row: dict[str, str]) -> None:
    gene = row["suggested_review_name"]
    if gene not in CONFIG:
        return
    cfg = CONFIG[gene]
    review_path = Path(row["review_file"])
    gene_dir = review_path.parent
    goa_path = gene_dir / f"{gene}-goa.tsv"
    uniprot_path = gene_dir / f"{gene}-uniprot.txt"
    data = yaml.safe_load(review_path.read_text(encoding="utf-8")) or {}
    goa_rows = read_tsv(goa_path) if goa_path.exists() else []
    goa_by_id_label = {(row["GO TERM"], row["GO NAME"]): row for row in goa_rows}

    data["gene_symbol"] = gene
    data["status"] = "DRAFT"
    data["description"] = cfg["description"]
    ensure_file_references(data, gene, row["uniprot_accession"], gene_dir)

    for annotation in data.get("existing_annotations") or []:
        review_annotation(gene, annotation, goa_by_id_label, cfg)

    core_functions: list[dict] = []
    for core in cfg.get("core", []):
        core_entry = dict(core)
        core_entry["supported_by"] = support_for_core(gene, core_entry, goa_rows, uniprot_path)
        core_functions.append(core_entry)
    data["core_functions"] = core_functions
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_questions(cfg)
    data["suggested_experiments"] = []

    review_path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False), encoding="utf-8")


def main() -> None:
    rows = read_tsv(BATCH)
    for row in rows:
        curate(row)


if __name__ == "__main__":
    main()
