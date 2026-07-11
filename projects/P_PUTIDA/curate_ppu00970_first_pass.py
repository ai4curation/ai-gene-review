#!/usr/bin/env python3
"""First-pass curation for the PSEPK ppu00970 aminoacyl-tRNA batch."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml


BATCH = Path("projects/P_PUTIDA/batches/ppu00970_aminoacyl_trna_biosynthesis.tsv")


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


CONFIG: dict[str, dict] = {
    "glyS": {
        "description": "glyS encodes the beta subunit of heterotetrameric glycyl-tRNA synthetase, the class II aminoacyl-tRNA ligase that charges tRNA(Gly) with glycine for protein translation.",
        "accept": {"GO:0004820", "GO:0006426"},
        "non_core": {"GO:0000166", "GO:0005524", "GO:0005737", "GO:0005829"},
        "remove": {"GO:0004814", "GO:0006420"},
        "core": [
            {
                "description": "Glycyl-tRNA synthetase beta-subunit contribution to glycine charging of tRNA(Gly).",
                "molecular_function": term("GO:0004820", "glycine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006426", "glycyl-tRNA aminoacylation")],
            }
        ],
    },
    "glyQ": {
        "description": "glyQ encodes the alpha subunit of heterotetrameric glycyl-tRNA synthetase, the class II aminoacyl-tRNA ligase that charges tRNA(Gly) with glycine for protein translation.",
        "accept": {"GO:0004820", "GO:0006426"},
        "non_core": {"GO:0000166", "GO:0005524", "GO:0005737", "GO:0005829"},
        "core": [
            {
                "description": "Glycyl-tRNA synthetase alpha-subunit contribution to glycine charging of tRNA(Gly).",
                "molecular_function": term("GO:0004820", "glycine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006426", "glycyl-tRNA aminoacylation")],
            }
        ],
    },
    "tyrS": {
        "description": "tyrS encodes tyrosyl-tRNA synthetase, a class I aminoacyl-tRNA ligase that charges tRNA(Tyr) with tyrosine for protein translation.",
        "accept": {"GO:0004831", "GO:0006437"},
        "non_core": {"GO:0000166", "GO:0003723", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0005829", "GO:0006418", "GO:0043039"},
        "core": [
            {
                "description": "Tyrosine charging of tRNA(Tyr) for translation.",
                "molecular_function": term("GO:0004831", "tyrosine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006437", "tyrosyl-tRNA aminoacylation")],
            }
        ],
    },
    "ileS": {
        "description": "ileS encodes isoleucyl-tRNA synthetase, a class I aminoacyl-tRNA ligase with editing activity that charges tRNA(Ile) and hydrolyzes mischarged aminoacyl-tRNAs to maintain translational fidelity.",
        "accept": {"GO:0002161", "GO:0004822", "GO:0006428", "GO:0106074"},
        "non_core": {"GO:0000049", "GO:0000166", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0005829", "GO:0006418", "GO:0008270"},
        "core": [
            {
                "description": "Isoleucine charging of tRNA(Ile) for translation.",
                "molecular_function": term("GO:0004822", "isoleucine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006428", "isoleucyl-tRNA aminoacylation")],
            },
            {
                "description": "Aminoacyl-tRNA editing/deacylation supporting translational fidelity.",
                "molecular_function": term("GO:0002161", "aminoacyl-tRNA deacylase activity"),
                "directly_involved_in": [term("GO:0106074", "aminoacyl-tRNA metabolism involved in translational fidelity")],
            },
        ],
    },
    "PP_0613": {
        "description": "PP_0613 encodes a predicted amidase-family protein included by KEGG ppu00970, but the fetched GOA table only supports generic catalytic activity and does not establish an aminoacyl-tRNA biosynthesis role.",
        "over": {"GO:0003824"},
        "core": [
            {
                "description": "Predicted amidase-family enzyme with unresolved substrate; not yet a satisfiable aminoacyl-tRNA pathway step.",
            }
        ],
        "questions": [
            "Does PP_0613 participate in tRNA-dependent transamidation or is it an unrelated amidase-family side node in the KEGG ppu00970 bucket?"
        ],
    },
    "hisS": {
        "description": "hisS encodes histidyl-tRNA synthetase, the class II aminoacyl-tRNA ligase that charges tRNA(His) with histidine for protein translation.",
        "accept": {"GO:0004821", "GO:0006427"},
        "non_core": {"GO:0005524", "GO:0005737", "GO:0006418"},
        "core": [
            {
                "description": "Histidine charging of tRNA(His) for translation.",
                "molecular_function": term("GO:0004821", "histidine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006427", "histidyl-tRNA aminoacylation")],
            }
        ],
    },
    "gatB": {
        "description": "gatB encodes subunit B of the bacterial GatCAB Asp/Glu-tRNA amidotransferase, a transamidation enzyme complex that converts misacylated Glu-tRNA(Gln) and/or Asp-tRNA(Asn) into correctly amidated Gln-tRNA(Gln) and Asn-tRNA(Asn).",
        "accept": {"GO:0050566", "GO:0050567", "GO:0070681"},
        "non_core": {"GO:0006412"},
        "over": {"GO:0003824", "GO:0016874", "GO:0016879", "GO:0016884"},
        "core": [
            {
                "description": "GatCAB transamidation activity for glutaminyl-tRNA(Gln) formation.",
                "molecular_function": term("GO:0050567", "glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity"),
                "directly_involved_in": [term("GO:0070681", "glutaminyl-tRNAGln biosynthesis via transamidation")],
            },
            {
                "description": "GatCAB transamidation activity for asparaginyl-tRNA(Asn) formation.",
                "molecular_function": term("GO:0050566", "asparaginyl-tRNA synthase (glutamine-hydrolyzing) activity"),
            },
        ],
    },
    "gatA": {
        "description": "gatA encodes the amidase/glutaminase subunit of GatCAB glutamyl-tRNA(Gln) amidotransferase, supplying the amide nitrogen for tRNA-dependent glutamine formation.",
        "accept": {"GO:0004359", "GO:0030956", "GO:0050567"},
        "non_core": {"GO:0005737", "GO:0006412"},
        "over": {"GO:0003824"},
        "core": [
            {
                "description": "Glutamine-hydrolyzing amidotransferase subunit activity in GatCAB-mediated Gln-tRNA(Gln) formation.",
                "molecular_function": term("GO:0050567", "glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity"),
            },
            {
                "description": "Glutaminase activity supplying amide nitrogen for GatCAB transamidation.",
                "molecular_function": term("GO:0004359", "glutaminase activity"),
            },
        ],
    },
    "gatC": {
        "description": "gatC encodes the small subunit of GatCAB Asp/Glu-tRNA amidotransferase, supporting tRNA-dependent amidation of misacylated Glu-tRNA(Gln) and Asp-tRNA(Asn).",
        "accept": {"GO:0050566", "GO:0050567", "GO:0070681"},
        "non_core": {"GO:0006412", "GO:0006450"},
        "core": [
            {
                "description": "GatCAB subunit contribution to glutaminyl-tRNA(Gln) formation by transamidation.",
                "molecular_function": term("GO:0050567", "glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity"),
                "directly_involved_in": [term("GO:0070681", "glutaminyl-tRNAGln biosynthesis via transamidation")],
            },
            {
                "description": "GatCAB subunit contribution to asparaginyl-tRNA(Asn) formation by transamidation.",
                "molecular_function": term("GO:0050566", "asparaginyl-tRNA synthase (glutamine-hydrolyzing) activity"),
            },
        ],
    },
    "valS": {
        "description": "valS encodes valyl-tRNA synthetase, a class I aminoacyl-tRNA ligase with editing activity that charges tRNA(Val) and helps maintain translational fidelity.",
        "accept": {"GO:0002161", "GO:0004832", "GO:0006438", "GO:0106074"},
        "non_core": {"GO:0000166", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0005829", "GO:0006418"},
        "core": [
            {
                "description": "Valine charging of tRNA(Val) for translation.",
                "molecular_function": term("GO:0004832", "valine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006438", "valyl-tRNA aminoacylation")],
            },
            {
                "description": "Aminoacyl-tRNA editing/deacylation supporting translational fidelity.",
                "molecular_function": term("GO:0002161", "aminoacyl-tRNA deacylase activity"),
                "directly_involved_in": [term("GO:0106074", "aminoacyl-tRNA metabolism involved in translational fidelity")],
            },
        ],
    },
    "proS": {
        "description": "proS encodes prolyl-tRNA synthetase, a class II aminoacyl-tRNA ligase with editing activity that charges tRNA(Pro) and helps maintain translational fidelity.",
        "accept": {"GO:0002161", "GO:0004827", "GO:0006433", "GO:0106074"},
        "non_core": {"GO:0000166", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0005829", "GO:0006418"},
        "core": [
            {
                "description": "Proline charging of tRNA(Pro) for translation.",
                "molecular_function": term("GO:0004827", "proline-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006433", "prolyl-tRNA aminoacylation")],
            },
            {
                "description": "Aminoacyl-tRNA editing/deacylation supporting translational fidelity.",
                "molecular_function": term("GO:0002161", "aminoacyl-tRNA deacylase activity"),
                "directly_involved_in": [term("GO:0106074", "aminoacyl-tRNA metabolism involved in translational fidelity")],
            },
        ],
    },
    "aspS": {
        "description": "aspS encodes a non-discriminating aspartyl-tRNA synthetase that charges tRNA(Asp) and tRNA(Asn) with aspartate, feeding direct aspartyl-tRNA formation and indirect Asn-tRNA synthesis through GatCAB transamidation.",
        "accept": {"GO:0004815", "GO:0006422", "GO:0050560"},
        "non_core": {"GO:0000166", "GO:0003676", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0006418", "GO:0016874"},
        "core": [
            {
                "description": "Aspartate charging of tRNA(Asp) for translation.",
                "molecular_function": term("GO:0004815", "aspartate-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006422", "aspartyl-tRNA aminoacylation")],
            },
            {
                "description": "Non-discriminating aspartate charging of tRNA(Asn), supplying substrate for transamidation.",
                "molecular_function": term("GO:0050560", "aspartate-tRNA(Asn) ligase activity"),
            },
        ],
    },
    "trpS": {
        "description": "trpS encodes tryptophanyl-tRNA synthetase, the class I aminoacyl-tRNA ligase that charges tRNA(Trp) with tryptophan for protein translation.",
        "accept": {"GO:0004830", "GO:0006436"},
        "non_core": {"GO:0000166", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0005829", "GO:0006418"},
        "core": [
            {
                "description": "Tryptophan charging of tRNA(Trp) for translation.",
                "molecular_function": term("GO:0004830", "tryptophan-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006436", "tryptophanyl-tRNA aminoacylation")],
            }
        ],
    },
    "lysS": {
        "description": "lysS encodes lysyl-tRNA synthetase, the class II aminoacyl-tRNA ligase that charges tRNA(Lys) with lysine for protein translation.",
        "accept": {"GO:0004824", "GO:0006430"},
        "non_core": {"GO:0000049", "GO:0000166", "GO:0000287", "GO:0003676", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0005829", "GO:0006418", "GO:0042803"},
        "core": [
            {
                "description": "Lysine charging of tRNA(Lys) for translation.",
                "molecular_function": term("GO:0004824", "lysine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006430", "lysyl-tRNA aminoacylation")],
            }
        ],
    },
    "thrS": {
        "description": "thrS encodes threonyl-tRNA synthetase, the class II aminoacyl-tRNA ligase that charges tRNA(Thr) with threonine for protein translation.",
        "accept": {"GO:0004829", "GO:0006435"},
        "non_core": {"GO:0000166", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0005829", "GO:0006418", "GO:0043039"},
        "core": [
            {
                "description": "Threonine charging of tRNA(Thr) for translation.",
                "molecular_function": term("GO:0004829", "threonine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006435", "threonyl-tRNA aminoacylation")],
            }
        ],
    },
    "pheS": {
        "description": "pheS encodes the alpha subunit of phenylalanyl-tRNA synthetase, the class II aminoacyl-tRNA ligase complex that charges tRNA(Phe) with phenylalanine for protein translation.",
        "accept": {"GO:0004826", "GO:0006432"},
        "non_core": {"GO:0000049", "GO:0000166", "GO:0000287", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0043039"},
        "core": [
            {
                "description": "Phenylalanine charging of tRNA(Phe) by the PheRS alpha/beta complex.",
                "molecular_function": term("GO:0004826", "phenylalanine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006432", "phenylalanyl-tRNA aminoacylation")],
            }
        ],
    },
    "pheT": {
        "description": "pheT encodes the beta subunit of phenylalanyl-tRNA synthetase, the class II aminoacyl-tRNA ligase complex that charges tRNA(Phe) with phenylalanine for protein translation.",
        "accept": {"GO:0004826", "GO:0006432"},
        "non_core": {"GO:0000049", "GO:0000287", "GO:0003723", "GO:0005524", "GO:0005737", "GO:0009328"},
        "core": [
            {
                "description": "Phenylalanine charging of tRNA(Phe) by the PheRS alpha/beta complex.",
                "molecular_function": term("GO:0004826", "phenylalanine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006432", "phenylalanyl-tRNA aminoacylation")],
            }
        ],
    },
    "glnS": {
        "description": "glnS encodes glutaminyl-tRNA synthetase, the class I aminoacyl-tRNA ligase that charges tRNA(Gln) with glutamine for protein translation.",
        "accept": {"GO:0004819", "GO:0006425"},
        "non_core": {"GO:0000166", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0005829", "GO:0006412", "GO:0006418", "GO:0043039"},
        "remove": {"GO:0006424"},
        "core": [
            {
                "description": "Glutamine charging of tRNA(Gln) for translation.",
                "molecular_function": term("GO:0004819", "glutamine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006425", "glutaminyl-tRNA aminoacylation")],
            }
        ],
    },
    "cysS": {
        "description": "cysS encodes cysteinyl-tRNA synthetase, the class I aminoacyl-tRNA ligase that charges tRNA(Cys) with cysteine for protein translation.",
        "accept": {"GO:0004817", "GO:0006423"},
        "non_core": {"GO:0000166", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0005829", "GO:0006418", "GO:0008270"},
        "core": [
            {
                "description": "Cysteine charging of tRNA(Cys) for translation.",
                "molecular_function": term("GO:0004817", "cysteine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006423", "cysteinyl-tRNA aminoacylation")],
            }
        ],
    },
    "serS": {
        "description": "serS encodes seryl-tRNA synthetase, the class II aminoacyl-tRNA ligase that charges tRNA(Ser) and tRNA(Sec) with serine for protein translation and selenocysteine precursor formation.",
        "accept": {"GO:0004828", "GO:0006434", "GO:0016260"},
        "non_core": {"GO:0000166", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0006418"},
        "core": [
            {
                "description": "Serine charging of tRNA(Ser) and tRNA(Sec).",
                "molecular_function": term("GO:0004828", "serine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006434", "seryl-tRNA aminoacylation")],
            }
        ],
    },
    "alaS": {
        "description": "alaS encodes alanyl-tRNA synthetase, a class II aminoacyl-tRNA ligase with editing activity that charges tRNA(Ala) and helps maintain translational fidelity.",
        "accept": {"GO:0002161", "GO:0004813", "GO:0006419", "GO:0106074"},
        "non_core": {"GO:0000166", "GO:0003676", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0005829", "GO:0008270", "GO:0043039", "GO:0045892"},
        "core": [
            {
                "description": "Alanine charging of tRNA(Ala) for translation.",
                "molecular_function": term("GO:0004813", "alanine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006419", "alanyl-tRNA aminoacylation")],
            },
            {
                "description": "Aminoacyl-tRNA editing/deacylation supporting translational fidelity.",
                "molecular_function": term("GO:0002161", "aminoacyl-tRNA deacylase activity"),
                "directly_involved_in": [term("GO:0106074", "aminoacyl-tRNA metabolism involved in translational fidelity")],
            },
        ],
    },
    "leuS": {
        "description": "leuS encodes leucyl-tRNA synthetase, a class I aminoacyl-tRNA ligase with editing activity that charges tRNA(Leu) and helps maintain translational fidelity.",
        "accept": {"GO:0002161", "GO:0004823", "GO:0006429", "GO:0106074"},
        "non_core": {"GO:0000166", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0005829", "GO:0006418"},
        "core": [
            {
                "description": "Leucine charging of tRNA(Leu) for translation.",
                "molecular_function": term("GO:0004823", "leucine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006429", "leucyl-tRNA aminoacylation")],
            },
            {
                "description": "Aminoacyl-tRNA editing/deacylation supporting translational fidelity.",
                "molecular_function": term("GO:0002161", "aminoacyl-tRNA deacylase activity"),
                "directly_involved_in": [term("GO:0106074", "aminoacyl-tRNA metabolism involved in translational fidelity")],
            },
        ],
    },
    "argS": {
        "description": "argS encodes arginyl-tRNA synthetase, the class I aminoacyl-tRNA ligase that charges tRNA(Arg) with arginine for protein translation.",
        "accept": {"GO:0004814", "GO:0006420"},
        "non_core": {"GO:0000166", "GO:0004812", "GO:0005524", "GO:0005737", "GO:0006418"},
        "core": [
            {
                "description": "Arginine charging of tRNA(Arg) for translation.",
                "molecular_function": term("GO:0004814", "arginine-tRNA ligase activity"),
                "directly_involved_in": [term("GO:0006420", "arginyl-tRNA aminoacylation")],
            }
        ],
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


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
                    "title": f"UniProt entry for {gene}",
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
                    "title": f"QuickGO GOA annotations for {gene}",
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
                    "title": f"Asta retrieval report for {gene}",
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
        "REMOVE": "Removed",
    }[action]


def classify(annotation: dict[str, str], cfg: dict) -> str:
    go_id = annotation["GO TERM"]
    if go_id in cfg.get("accept", set()):
        return "ACCEPT"
    if go_id in cfg.get("non_core", set()):
        return "KEEP_AS_NON_CORE"
    if go_id in cfg.get("over", set()):
        return "MARK_AS_OVER_ANNOTATED"
    if go_id in cfg.get("remove", set()):
        return "REMOVE"
    name = annotation["GO NAME"]
    if annotation["GO ASPECT"] == "cellular_component" or "binding" in name:
        return "KEEP_AS_NON_CORE"
    if name in {
        "aminoacyl-tRNA ligase activity",
        "tRNA aminoacylation for protein translation",
        "tRNA aminoacylation",
        "translation",
    }:
        return "KEEP_AS_NON_CORE"
    if name in {"catalytic activity", "ligase activity", "ligase activity, forming carbon-nitrogen bonds"}:
        return "MARK_AS_OVER_ANNOTATED"
    return "KEEP_AS_NON_CORE"


def reason_for(action: str, annotation: dict[str, str]) -> str:
    label = annotation["GO NAME"]
    if action == "ACCEPT":
        return (
            f"{label} matches the fetched GOA/UniProt identity for this ppu00970 first-pass review "
            "and captures a specific aminoacylation, editing, or tRNA-dependent transamidation role."
        )
    if action == "KEEP_AS_NON_CORE":
        return (
            f"{label} is plausible context, but it is a location, cofactor, binding, complex, "
            "or broader translation/aminoacylation parent term rather than the most informative core function."
        )
    if action == "MARK_AS_OVER_ANNOTATED":
        return (
            f"{label} is compatible with enzyme function but broader than the specific aminoacyl-tRNA ligase, "
            "GatCAB transamidase, or pathway role supported by UniProt/GOA."
        )
    if action == "REMOVE":
        return (
            f"{label} conflicts with the fetched UniProt identity for this protein and appears to be an "
            "electronic transfer from the wrong aminoacyl-tRNA ligase specificity."
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
    action = classify(goa_row or {"GO TERM": go_id, "GO NAME": label, "GO ASPECT": ""}, cfg)
    review = {
        "summary": f"{action_label(action)}: {label} for {gene} in the ppu00970 aminoacyl-tRNA first-pass review.",
        "action": action,
        "reason": reason_for(action, goa_row or {"GO NAME": label}),
    }
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
    if "molecular_function" in core:
        term_ids.add(core["molecular_function"]["id"])
    for item in core.get("directly_involved_in", []) or []:
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
    data["suggested_questions"] = [{"question": q} for q in cfg.get("questions", [])]
    data["suggested_experiments"] = []
    review_path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False), encoding="utf-8")


def main() -> None:
    for row in read_tsv(BATCH):
        curate(row)


if __name__ == "__main__":
    main()
