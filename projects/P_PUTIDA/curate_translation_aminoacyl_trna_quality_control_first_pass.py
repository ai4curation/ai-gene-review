#!/usr/bin/env python3
"""First-pass curation for aminoacyl-tRNA quality-control boundary genes."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "aminoacyl_trna_quality_control_boundary.yaml"
BATCH_TSV = (
    "projects/P_PUTIDA/batches/"
    "module_translation_rna_processing_aminoacyl_trna_charging_editing_quality_control.tsv"
)


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERM = {
    "GO:0000049": term("GO:0000049", "tRNA binding"),
    "GO:0000166": term("GO:0000166", "nucleotide binding"),
    "GO:0002161": term("GO:0002161", "aminoacyl-tRNA deacylase activity"),
    "GO:0004536": term("GO:0004536", "DNA nuclease activity"),
    "GO:0004812": term("GO:0004812", "aminoacyl-tRNA ligase activity"),
    "GO:0004818": term("GO:0004818", "glutamate-tRNA ligase activity"),
    "GO:0005524": term("GO:0005524", "ATP binding"),
    "GO:0005737": term("GO:0005737", "cytoplasm"),
    "GO:0005829": term("GO:0005829", "cytosol"),
    "GO:0006399": term("GO:0006399", "tRNA metabolic process"),
    "GO:0006400": term("GO:0006400", "tRNA modification"),
    "GO:0006424": term("GO:0006424", "glutamyl-tRNA aminoacylation"),
    "GO:0008270": term("GO:0008270", "zinc ion binding"),
    "GO:0008914": term("GO:0008914", "leucyl-tRNA--protein transferase activity"),
    "GO:0016788": term("GO:0016788", "hydrolase activity, acting on ester bonds"),
    "GO:0019478": term("GO:0019478", "D-amino acid catabolic process"),
    "GO:0030163": term("GO:0030163", "protein catabolic process"),
    "GO:0043039": term("GO:0043039", "tRNA aminoacylation"),
    "GO:0043908": term("GO:0043908", "Ser(Gly)-tRNA(Ala) hydrolase activity"),
    "GO:0046872": term("GO:0046872", "metal ion binding"),
    "GO:0051499": term("GO:0051499", "D-aminoacyl-tRNA deacylase activity"),
    "GO:0051500": term("GO:0051500", "D-tyrosyl-tRNA(Tyr) deacylase activity"),
    "GO:0106026": term("GO:0106026", "Gly-tRNA(Ala) deacylase activity"),
    "GO:0106074": term("GO:0106074", "aminoacyl-tRNA metabolism involved in translational fidelity"),
}

GENES = [
    "PP_0201",
    "PP_0782",
    "PP_0784",
    "ybaK",
    "PP_1091",
    "ycfH",
    "aat",
    "PP_4228",
    "gluQ",
    "dtd",
    "PP_5664",
]

GAD_TDI_GENES = {"PP_0782", "PP_0784", "PP_4228", "PP_5664"}

DESCRIPTIONS = {
    "PP_0201": (
        "PP_0201 encodes a predicted YbaK/aminoacyl-tRNA synthetase-associated domain protein in Pseudomonas "
        "putida KT2440. The current first-pass support is domain and IEA evidence for aminoacyl-tRNA deacylase "
        "activity, so it is best treated as a candidate aminoacyl-tRNA editing factor rather than a fully "
        "characterized enzyme."
    ),
    "PP_0782": (
        "PP_0782 encodes a predicted GAD-related/T6SS Tdi1 C-terminal domain protein in Pseudomonas putida "
        "KT2440. Although the current UniProt protein-language-model name says glutamyl-tRNA amidotransferase, "
        "the record lacks GOA, Rhea, HAMAP, or subunit-context support for a GatCAB-like aminoacyl-tRNA role."
    ),
    "PP_0784": (
        "PP_0784 encodes a predicted GAD-related/T6SS Tdi1 C-terminal domain protein in Pseudomonas putida "
        "KT2440. It currently lacks GOA support and should be kept as an unresolved side node rather than a "
        "curated glutamyl-tRNA amidotransferase claim."
    ),
    "ybaK": (
        "ybaK encodes a prolyl-tRNA editing-family YbaK/EbsC protein predicted as a Cys-tRNA(Pro)/Cys-tRNA(Cys) "
        "deacylase. Its supported role is aminoacyl-tRNA editing/deacylation that helps maintain translational "
        "fidelity."
    ),
    "PP_1091": (
        "PP_1091 encodes a 58 amino acid DUF8197/PA3496-like protein in Pseudomonas putida KT2440. The current "
        "protein-language-model name says leucyl-tRNA synthetase, but the record is far too short and lacks "
        "GOA/domain evidence for a canonical LeuRS function."
    ),
    "ycfH": (
        "ycfH encodes a TatD/YcfH-like metal-dependent hydrolase annotated as tRNA D-aminoacylase in Pseudomonas "
        "putida KT2440. The first-pass evidence supports a candidate tRNA/aminoacyl-tRNA deacylase role more "
        "strongly than a generic TatD-family DNA nuclease assertion."
    ),
    "aat": (
        "aat encodes leucyl/phenylalanyl-tRNA--protein transferase, the cytoplasmic L/F-transferase of the "
        "bacterial N-end rule protein-degradation pathway. It transfers Leu or Phe from aminoacyl-tRNAs to "
        "destabilizing N-terminal residues on proteins."
    ),
    "PP_4228": (
        "PP_4228 encodes a predicted GAD-related/T6SS Tdi1 C-terminal domain protein in Pseudomonas putida "
        "KT2440. Its current glutamyl-tRNA amidotransferase name is not supported by GOA rows or a recognizable "
        "GatCAB subunit assignment."
    ),
    "gluQ": (
        "gluQ encodes glutamyl-Q tRNA(Asp) synthetase, a cytosolic class-I aminoacyl-tRNA-synthetase-like enzyme "
        "that activates glutamate and transfers it to the queuosine wobble-base moiety of tRNA(Asp). This is best "
        "curated as tRNA modification context rather than ordinary tRNA(Glu) charging for translation."
    ),
    "dtd": (
        "dtd encodes the cytoplasmic D-aminoacyl-tRNA deacylase DTD. It hydrolyzes mischarged D-aminoacyl-tRNAs "
        "and glycyl-tRNA(Ala), recycling tRNA and supporting translational fidelity and protein L-homochirality."
    ),
    "PP_5664": (
        "PP_5664 encodes a predicted GAD-related/T6SS Tdi1 C-terminal domain protein in Pseudomonas putida "
        "KT2440. It has no GOA rows and should remain an unresolved side node pending direct evidence for any "
        "aminoacyl-tRNA amidotransferase activity."
    ),
}

CORE = {
    "PP_0201": [
        {
            "description": "Candidate YbaK-domain aminoacyl-tRNA deacylase/editing factor.",
            "molecular_function": "GO:0002161",
            "directly_involved_in": ["GO:0106074"],
        }
    ],
    "PP_0782": [
        {
            "description": "Predicted GAD/T6SS Tdi1_C-domain protein with unresolved substrate and no defensible first-pass GO function.",
        }
    ],
    "PP_0784": [
        {
            "description": "Predicted GAD/T6SS Tdi1_C-domain protein with unresolved substrate and no defensible first-pass GO function.",
        }
    ],
    "ybaK": [
        {
            "description": "YbaK-family aminoacyl-tRNA editing/deacylation activity.",
            "molecular_function": "GO:0002161",
            "directly_involved_in": ["GO:0106074"],
        }
    ],
    "PP_1091": [
        {
            "description": "Short DUF8197/PA3496-like protein fragment; not yet a satisfiable leucyl-tRNA synthetase step.",
        }
    ],
    "ycfH": [
        {
            "description": "Candidate TatD/YcfH-family aminoacyl-tRNA deacylase-like hydrolase.",
            "molecular_function": "GO:0002161",
            "locations": ["GO:0005829"],
        }
    ],
    "aat": [
        {
            "description": "Leucyl/phenylalanyl-tRNA--protein transferase in the bacterial N-end rule pathway.",
            "molecular_function": "GO:0008914",
            "directly_involved_in": ["GO:0030163"],
            "locations": ["GO:0005737"],
        }
    ],
    "PP_4228": [
        {
            "description": "Predicted GAD/T6SS Tdi1_C-domain protein with unresolved substrate and no defensible first-pass GO function.",
        }
    ],
    "gluQ": [
        {
            "description": "Glutamyl-Q tRNA(Asp) synthetase activity in tRNA wobble-base modification.",
            "molecular_function": "GO:0004818",
            "directly_involved_in": ["GO:0006400"],
            "locations": ["GO:0005829"],
        }
    ],
    "dtd": [
        {
            "description": "Broad D-aminoacyl-tRNA editing/deacylase activity.",
            "molecular_function": "GO:0051499",
            "directly_involved_in": ["GO:0106074"],
            "locations": ["GO:0005737"],
        },
        {
            "description": "Gly-tRNA(Ala) deacylation that protects against AlaRS mischarging.",
            "molecular_function": "GO:0106026",
            "directly_involved_in": ["GO:0106074"],
            "locations": ["GO:0005737"],
        },
    ],
    "PP_5664": [
        {
            "description": "Predicted GAD/T6SS Tdi1_C-domain protein with unresolved substrate and no defensible first-pass GO function.",
        }
    ],
}


def gene_file(gene: str, suffix: str) -> Path:
    return GENE_ROOT / gene / f"{gene}-{suffix}"


def file_id(gene: str, suffix: str) -> str:
    return f"file:PSEPK/{gene}/{gene}-{suffix}"


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


def evidence_for(gene: str, term_id: str | None = None, extra_markers: tuple[str, ...] = ()) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if term_id:
        add_support(items, support(file_id(gene, "goa.tsv"), goa_line(gene, term_id)))
    uniprot = gene_file(gene, "uniprot.txt")
    for marker in (
        "DE   ",
        "CC   -!- FUNCTION:",
        "CC   -!- CATALYTIC ACTIVITY:",
        "CC   -!- SUBCELLULAR LOCATION:",
        "CC   -!- SIMILARITY:",
        "DR   GO;",
        "DR   InterPro;",
        "DR   Pfam;",
        "DR   PANTHER;",
        "FT   DOMAIN",
        "KW   ",
        *extra_markers,
    ):
        add_support(items, support(file_id(gene, "uniprot.txt"), line_containing(uniprot, marker)))
    return items


def t(go_id: str) -> dict[str, str]:
    return TERM[go_id]


def review(
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
    decisions = {
        "PP_0201": {
            "GO:0002161": review(
                "Aminoacyl-tRNA deacylase activity is supported as a candidate YbaK-domain function.",
                "ACCEPT",
                "The GOA row is electronic/domain-derived rather than experimental, but it matches the YbaK/aminoacyl-tRNA synthetase-associated domain identity.",
                gene,
                term_id,
            ),
            "GO:0106074": review(
                "Aminoacyl-tRNA metabolism involved in translational fidelity follows from the deacylase row.",
                "ACCEPT",
                "This process is logically inferred from the aminoacyl-tRNA deacylase annotation and is appropriate for a YbaK-like editing candidate.",
                gene,
                term_id,
            ),
        },
        "ybaK": {
            "GO:0002161": review(
                "Aminoacyl-tRNA deacylase activity is the core YbaK-family function.",
                "ACCEPT",
                "UniProt names the protein as Cys-tRNA(Pro)/Cys-tRNA(Cys) deacylase and the GOA row is supported by YbaK-domain evidence.",
                gene,
                term_id,
            ),
            "GO:0106074": review(
                "Aminoacyl-tRNA metabolism involved in translational fidelity is appropriate process context.",
                "ACCEPT",
                "YbaK-family deacylation removes mischarged aminoacyl-tRNA species and supports translation fidelity.",
                gene,
                term_id,
            ),
        },
        "ycfH": {
            "GO:0004536": review(
                "DNA nuclease activity is probably a TatD-family over-transfer for this record.",
                "MODIFY",
                "The protein is named tRNA D-aminoacylase, PANTHER places it in a D-aminoacyl-tRNA deacylase family, and a tRNA deacylase term is a better first-pass call than generic TatD DNase activity.",
                gene,
                term_id,
                ["GO:0002161"],
            ),
            "GO:0005829": review(
                "Cytosol is plausible location context for this soluble bacterial hydrolase.",
                "ACCEPT",
                "The TreeGrafter row directly supports cytosol localization.",
                gene,
                term_id,
            ),
            "GO:0016788": review(
                "Generic ester hydrolase activity should be narrowed to aminoacyl-tRNA deacylase activity.",
                "MODIFY",
                "The product name and PANTHER family point to tRNA/aminoacyl-tRNA deacylation, while the GOA hydrolase row is too broad to be the core function.",
                gene,
                term_id,
                ["GO:0002161"],
            ),
        },
        "aat": {
            "GO:0005737": review(
                "Cytoplasm is the supported location for Aat.",
                "ACCEPT",
                "UniProt places the L/F-transferase in the cytoplasm.",
                gene,
                term_id,
            ),
            "GO:0008914": review(
                "Leucyl-tRNA--protein transferase activity is the core molecular function.",
                "ACCEPT",
                "UniProt/HAMAP and the GOA/Rhea/EC mapping support transfer of Leu or Phe from aminoacyl-tRNAs to protein N-termini.",
                gene,
                term_id,
            ),
            "GO:0030163": review(
                "Protein catabolic process is appropriate N-end rule pathway context.",
                "ACCEPT",
                "Aat modifies N-termini to feed bacterial N-end rule protein degradation.",
                gene,
                term_id,
            ),
        },
        "gluQ": {
            "GO:0000166": review(
                "Generic nucleotide binding is over-broad for Glu-Q-RS.",
                "MARK_AS_OVER_ANNOTATED",
                "ATP use is real, but the informative function is glutamate activation/transfer to tRNA(Asp) queuosine.",
                gene,
                term_id,
            ),
            "GO:0004812": review(
                "Broad aminoacyl-tRNA ligase activity should be narrowed to the closest available glutamate-tRNA ligase term.",
                "MODIFY",
                "The enzyme is class-I synthetase-like, but its specific role is Glu-Q tRNA(Asp) modification rather than generic aminoacyl-tRNA ligase activity.",
                gene,
                term_id,
                ["GO:0004818"],
            ),
            "GO:0004818": review(
                "Glutamate-tRNA ligase activity is the closest available GO molecular-function term for Glu-Q-RS.",
                "ACCEPT",
                "The reviewed UniProt record names Glutamyl-Q tRNA(Asp) synthetase and describes glutamate transfer onto tRNA(Asp) queuosine.",
                gene,
                term_id,
            ),
            "GO:0005524": review(
                "ATP binding is valid cofactor context but not the core function.",
                "KEEP_AS_NON_CORE",
                "ATP supports glutamate activation but is less informative than the ligase/modification terms.",
                gene,
                term_id,
            ),
            "GO:0005829": review(
                "Cytosol is appropriate location context for Glu-Q-RS.",
                "ACCEPT",
                "The TreeGrafter row directly supports cytosol localization.",
                gene,
                term_id,
            ),
            "GO:0006400": review(
                "tRNA modification is the core biological process for Glu-Q-RS.",
                "ACCEPT",
                "UniProt describes transfer of glutamate onto the queuosine wobble-base moiety of tRNA(Asp), which is tRNA modification context.",
                gene,
                term_id,
            ),
            "GO:0006424": review(
                "Glutamyl-tRNA aminoacylation is misleading as a canonical translation-charging process for Glu-Q-RS.",
                "MODIFY",
                "The enzyme modifies tRNA(Asp) queuosine rather than producing canonical Glu-tRNA(Glu) for protein translation.",
                gene,
                term_id,
                ["GO:0006400"],
            ),
            "GO:0008270": review(
                "Zinc ion binding is valid cofactor context.",
                "KEEP_AS_NON_CORE",
                "UniProt/HAMAP notes one zinc ion per subunit, but metal binding is not the main biological role.",
                gene,
                term_id,
            ),
            "GO:0043039": review(
                "Generic tRNA aminoacylation should be replaced by tRNA modification for this enzyme.",
                "MODIFY",
                "Glu-Q-RS uses aminoacyl-tRNA-synthetase-like chemistry, but the product is a modified tRNA(Asp) wobble base, not a translation-charged tRNA.",
                gene,
                term_id,
                ["GO:0006400"],
            ),
        },
        "dtd": {
            "GO:0000049": review(
                "tRNA binding is substrate context for DTD.",
                "KEEP_AS_NON_CORE",
                "The core function is aminoacyl-tRNA deacylation rather than binding alone.",
                gene,
                term_id,
            ),
            "GO:0002161": review(
                "Aminoacyl-tRNA deacylase activity is a supported parent function for DTD.",
                "ACCEPT",
                "The reviewed UniProt record describes DTD as an aminoacyl-tRNA editing enzyme.",
                gene,
                term_id,
            ),
            "GO:0005737": review(
                "Cytoplasm is the supported location for DTD.",
                "ACCEPT",
                "UniProt places DTD in the cytoplasm.",
                gene,
                term_id,
            ),
            "GO:0006399": review(
                "tRNA metabolic process is correct but broad.",
                "KEEP_AS_NON_CORE",
                "The more informative process is aminoacyl-tRNA metabolism involved in translational fidelity.",
                gene,
                term_id,
            ),
            "GO:0016788": review(
                "Generic ester hydrolase activity should be narrowed to D-aminoacyl-tRNA deacylase activity.",
                "MODIFY",
                "UniProt/HAMAP and Rhea support specific hydrolysis of mischarged aminoacyl-tRNA substrates.",
                gene,
                term_id,
                ["GO:0051499"],
            ),
            "GO:0019478": review(
                "D-amino acid catabolic process is secondary context.",
                "KEEP_AS_NON_CORE",
                "DTD releases D-amino acids from mischarged tRNAs, but its primary role is tRNA quality control and translational fidelity.",
                gene,
                term_id,
            ),
            "GO:0043908": review(
                "Ser(Gly)-tRNA(Ala) hydrolase activity is supported substrate-specific deacylation.",
                "ACCEPT",
                "The GOA/UniRule row is consistent with the reviewed record's glycyl-tRNA(Ala) deacylase activity.",
                gene,
                term_id,
            ),
            "GO:0051499": review(
                "D-aminoacyl-tRNA deacylase activity is a core DTD function.",
                "ACCEPT",
                "UniProt/HAMAP and Rhea support hydrolysis of D-aminoacyl-tRNAs.",
                gene,
                term_id,
            ),
            "GO:0051500": review(
                "D-tyrosyl-tRNA(Tyr) deacylase activity is consistent DTD-family substrate context.",
                "ACCEPT",
                "The TreeGrafter/PANTHER row is consistent with the D-aminoacyl-tRNA deacylase family assignment.",
                gene,
                term_id,
            ),
            "GO:0106026": review(
                "Gly-tRNA(Ala) deacylase activity is a supported core DTD function.",
                "ACCEPT",
                "The reviewed UniProt record specifically states that DTD deacylates mischarged glycyl-tRNA(Ala).",
                gene,
                term_id,
            ),
            "GO:0106074": review(
                "Aminoacyl-tRNA metabolism involved in translational fidelity is the core process.",
                "ACCEPT",
                "DTD removes toxic or mistranslating aminoacyl-tRNA species and supports protein L-homochirality.",
                gene,
                term_id,
            ),
        },
    }
    return decisions[gene][term_id]


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
    if gene in GAD_TDI_GENES:
        return [
            {
                "question": f"Does {gene} have a T6SS immunity/toxin-adjacent role, or is there direct evidence for aminoacyl-tRNA amidotransferase chemistry?"
            }
        ]
    if gene == "PP_1091":
        return [
            {
                "question": "Is PP_1091 translated as a stable small protein, or is the leucyl-tRNA synthetase-like label an annotation artifact for a short DUF8197/PA3496-like ORF?"
            }
        ]
    if gene == "gluQ":
        return [
            {
                "question": "Should Glu-Q-RS be routed primarily to a queuosine/tRNA-modification module rather than the aminoacyl-tRNA quality-control boundary?"
            }
        ]
    return [
        {
            "question": f"What P. putida KT2440 substrates and stress conditions most strongly reveal the aminoacyl-tRNA quality-control role of {gene}?"
        }
    ]


def suggested_experiment(gene: str) -> list[dict[str, str]]:
    if gene in GAD_TDI_GENES or gene == "PP_1091":
        return [
            {
                "description": f"Test {gene} expression, protein stability, and interaction partners under T6SS-active and translation-stress conditions before assigning a pathway function.",
                "experiment_type": "expression/proteomics and interaction assay",
            }
        ]
    return [
        {
            "description": f"Compare wild-type and {gene} perturbation strains for growth and tRNA charging/editing defects under amino-acid imbalance and translation-stress conditions.",
            "experiment_type": "tRNA charging/editing and stress-fitness assay",
        }
    ]


def curate_gene(gene: str) -> None:
    path = gene_file(gene, "ai-review.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    data["description"] = DESCRIPTIONS[gene]
    for ann in data.get("existing_annotations", []):
        go_id = ann["term"]["id"]
        ann["review"] = review_for(gene, go_id)
    data["references"] = references_for(gene, data)
    data["core_functions"] = [core_function(gene, spec) for spec in CORE[gene]]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_question(gene)
    data["suggested_experiments"] = suggested_experiment(gene)
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120),
        encoding="utf-8",
    )

    notes = [
        f"# {gene} aminoacyl-tRNA quality-control first-pass notes",
        "",
        "- First-pass curation date: 2026-07-10.",
        f"- Batch: `{BATCH_TSV}`.",
        f"- Asta retrieval report: `{file_id(gene, 'deep-research-asta.md')}`. The report is retained as provenance; annotation decisions are supported by local UniProt and GOA rows.",
        f"- Main conclusion: {CORE[gene][0]['description']}",
    ]
    gene_file(gene, "notes.md").write_text("\n".join(notes) + "\n", encoding="utf-8")


def annoton(
    gene: str,
    label: str,
    role: str,
    function_id: str | None = None,
    processes: list[str] | None = None,
    locations: list[str] | None = None,
) -> dict:
    out = {
        "id": f"{gene}_{label.lower().replace(' ', '_').replace('/', '_').replace('-', '_')}",
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


def write_module() -> None:
    module = {
        "id": "MODULE:aminoacyl_trna_quality_control_boundary",
        "title": "Aminoacyl-tRNA quality-control boundary",
        "description": (
            "Boundary module for PSEPK translation/RNA-processing genes that are not canonical aminoacyl-tRNA "
            "synthetases but touch aminoacyl-tRNA editing, tRNA modification, or aminoacyl-tRNA-derived protein "
            "quality-control chemistry. Low-information GAD/T6SS Tdi1_C and short-fragment entries are retained "
            "as unresolved side nodes instead of forced GatCAB or synthetase calls."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_TSV}",
                "title": "PSEPK translation/RNA aminoacyl-tRNA charging/editing split",
                "statement": "The batch records YbaK/Dtd/YcfH deacylases, Aat L/F-transferase, Glu-Q-RS, and several low-information GAD/T6SS or short-fragment side nodes.",
            }
        ]
        + [
            {
                "source_id": file_id(gene, "ai-review.yaml"),
                "title": f"Curated {gene} review",
                "statement": DESCRIPTIONS[gene],
            }
            for gene in GENES
        ],
        "module": {
            "id": "aminoacyl_trna_quality_control_boundary",
            "label": "Aminoacyl-tRNA quality-control boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {"preferred_term": TERM[x]["label"], "term": t(x)}
                for x in ["GO:0002161", "GO:0051499", "GO:0106026", "GO:0106074", "GO:0008914", "GO:0006400"]
            ],
            "parts": [
                {
                    "order": 1,
                    "role": "Aminoacyl-tRNA editing and deacylation",
                    "node": {
                        "id": "aminoacyl_trna_editing_deacylation",
                        "label": "Aminoacyl-tRNA editing and deacylation",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "YbaK-domain and DTD/TatD-like candidates with first-pass support for aminoacyl-tRNA deacylation or editing.",
                        "annotons": [
                            annoton(
                                "PP_0201",
                                "candidate YbaK-domain deacylase",
                                CORE["PP_0201"][0]["description"],
                                "GO:0002161",
                                ["GO:0106074"],
                            ),
                            annoton(
                                "ybaK",
                                "YbaK aminoacyl-tRNA deacylase",
                                CORE["ybaK"][0]["description"],
                                "GO:0002161",
                                ["GO:0106074"],
                            ),
                            annoton(
                                "ycfH",
                                "candidate TatD/YcfH tRNA deacylase",
                                CORE["ycfH"][0]["description"],
                                "GO:0002161",
                                None,
                                ["GO:0005829"],
                            ),
                            annoton(
                                "dtd",
                                "D-aminoacyl-tRNA deacylase",
                                CORE["dtd"][0]["description"],
                                "GO:0051499",
                                ["GO:0106074"],
                                ["GO:0005737"],
                            ),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "Aminoacyl-tRNA-derived protein quality control and tRNA modification",
                    "node": {
                        "id": "aat_gluq_side_chemistry",
                        "label": "Aat and Glu-Q-RS aminoacyl-tRNA side chemistry",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "Aat uses aminoacyl-tRNAs in N-end rule protein degradation, while Glu-Q-RS uses aminoacyl-tRNA-synthetase-like chemistry for tRNA(Asp) queuosine modification.",
                        "annotons": [
                            annoton(
                                "aat",
                                "L/F-transferase N-end rule enzyme",
                                CORE["aat"][0]["description"],
                                "GO:0008914",
                                ["GO:0030163"],
                                ["GO:0005737"],
                            ),
                            annoton(
                                "gluQ",
                                "Glu-Q tRNA(Asp) synthetase",
                                CORE["gluQ"][0]["description"],
                                "GO:0004818",
                                ["GO:0006400"],
                                ["GO:0005829"],
                            ),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "Unresolved GAD/T6SS and short-fragment side nodes",
                    "node": {
                        "id": "unresolved_aminoacyl_trna_boundary_side_nodes",
                        "label": "Unresolved aminoacyl-tRNA boundary side nodes",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "Several entries entered the bucket by protein-language-model names or weak domain labels but currently lack enough evidence for GO-level aminoacyl-tRNA functions.",
                        "annotons": [
                            annoton(gene, "unresolved GAD/T6SS Tdi1_C side node", CORE[gene][0]["description"])
                            for gene in ["PP_0782", "PP_0784", "PP_4228", "PP_5664"]
                        ]
                        + [
                            annoton(
                                "PP_1091",
                                "short DUF8197/PA3496-like side node",
                                CORE["PP_1091"][0]["description"],
                            )
                        ],
                    },
                },
            ],
        },
    }
    MODULE_PATH.write_text(
        yaml.dump(module, Dumper=NoAliasDumper, sort_keys=False, width=120),
        encoding="utf-8",
    )


def main() -> None:
    for gene in GENES:
        curate_gene(gene)
    write_module()


if __name__ == "__main__":
    main()
