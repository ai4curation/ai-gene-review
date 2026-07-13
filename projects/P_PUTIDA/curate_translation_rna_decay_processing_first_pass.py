#!/usr/bin/env python3
"""First-pass curation for RNase/RNA-decay/helicase boundary genes."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "rna_decay_processing_boundary.yaml"
BATCH_TSV = (
    "projects/P_PUTIDA/batches/"
    "module_translation_rna_processing_ribonuclease_rna_decay_processing_helicases.tsv"
)


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


def term(go_id: str, label: str) -> dict[str, str]:
    return {"id": go_id, "label": label}


TERM = {
    "GO:0000049": term("GO:0000049", "tRNA binding"),
    "GO:0000166": term("GO:0000166", "nucleotide binding"),
    "GO:0000175": term("GO:0000175", "3'-5'-RNA exonuclease activity"),
    "GO:0000287": term("GO:0000287", "magnesium ion binding"),
    "GO:0001682": term("GO:0001682", "tRNA 5'-leader removal"),
    "GO:0003676": term("GO:0003676", "nucleic acid binding"),
    "GO:0003723": term("GO:0003723", "RNA binding"),
    "GO:0003724": term("GO:0003724", "RNA helicase activity"),
    "GO:0004526": term("GO:0004526", "ribonuclease P activity"),
    "GO:0004527": term("GO:0004527", "exonuclease activity"),
    "GO:0004540": term("GO:0004540", "RNA nuclease activity"),
    "GO:0005524": term("GO:0005524", "ATP binding"),
    "GO:0005737": term("GO:0005737", "cytoplasm"),
    "GO:0005829": term("GO:0005829", "cytosol"),
    "GO:0006364": term("GO:0006364", "rRNA processing"),
    "GO:0006396": term("GO:0006396", "RNA processing"),
    "GO:0008033": term("GO:0008033", "tRNA processing"),
    "GO:0008270": term("GO:0008270", "zinc ion binding"),
    "GO:0008408": term("GO:0008408", "3'-5' exonuclease activity"),
    "GO:0008428": term("GO:0008428", "ribonuclease inhibitor activity"),
    "GO:0008948": term("GO:0008948", "oxaloacetate decarboxylase activity"),
    "GO:0009022": term("GO:0009022", "tRNA nucleotidyltransferase activity"),
    "GO:0016075": term("GO:0016075", "rRNA catabolic process"),
    "GO:0016787": term("GO:0016787", "hydrolase activity"),
    "GO:0016891": term(
        "GO:0016891",
        "RNA endonuclease activity producing 5'-phosphomonoesters, hydrolytic mechanism",
    ),
    "GO:0016896": term("GO:0016896", "RNA exonuclease activity, producing 5'-phosphomonoesters"),
    "GO:0030677": term("GO:0030677", "ribonuclease P complex"),
    "GO:0031125": term("GO:0031125", "rRNA 3'-end processing"),
    "GO:0033890": term("GO:0033890", "ribonuclease D activity"),
    "GO:0042780": term("GO:0042780", "tRNA 3'-end processing"),
    "GO:0042781": term("GO:0042781", "3'-tRNA processing endoribonuclease activity"),
    "GO:0045004": term("GO:0045004", "DNA replication proofreading"),
    "GO:0046872": term("GO:0046872", "metal ion binding"),
    "GO:0047443": term("GO:0047443", "4-hydroxy-4-methyl-2-oxoglutarate aldolase activity"),
    "GO:0051252": term("GO:0051252", "regulation of RNA metabolic process"),
}

GENES = [
    "rnpA",
    "rng",
    "rnt",
    "PP_1840",
    "PP_2084",
    "rnz",
    "PP_4462",
    "srmB",
    "rnd",
    "PP_4720",
    "dbpA",
    "rph",
]

SIDE_NODE_GENES = {"PP_1840", "PP_2084", "PP_4462", "PP_4720"}

DESCRIPTIONS = {
    "rnpA": (
        "rnpA encodes the protein component of bacterial RNase P in Pseudomonas putida KT2440. The RNase P "
        "ribonucleoprotein removes 5' leader sequences from precursor tRNAs; the protein subunit binds pre-tRNA "
        "leader/substrate context and broadens or stabilizes ribozyme activity in vivo."
    ),
    "rng": (
        "rng encodes RNase G, an RNase E/G-family S1-domain endoribonuclease in Pseudomonas putida KT2440. Its "
        "supported first-pass role is cytoplasmic RNA nuclease activity tied to rRNA/RNA processing rather than a "
        "fully resolved organism-specific RNA-decay pathway."
    ),
    "rnt": (
        "rnt encodes RNase T, a magnesium-dependent 3'-5' exoribonuclease that trims short 3' overhangs on RNA "
        "substrates and participates in tRNA end-turnover and tRNA biosynthesis. The DNA proofreading annotation "
        "appears to be a family-transfer artifact rather than this enzyme's biological role."
    ),
    "PP_1840": (
        "PP_1840 encodes a low-information RraB-domain regulator-of-ribonuclease-activity candidate. It has no GOA "
        "rows, so the first-pass review retains it as an unresolved RNase-regulator side node rather than asserting "
        "a specific nuclease, helicase, or RNA-processing function."
    ),
    "PP_2084": (
        "PP_2084 encodes a class II aldolase/RraA-like protein annotated as 4-hydroxy-4-methyl-2-oxoglutarate "
        "aldolase and oxaloacetate decarboxylase, with secondary RraA-like ribonuclease-regulator annotations. Its "
        "better-supported function is metabolic lyase chemistry, while RNA-metabolism regulation remains side context."
    ),
    "rnz": (
        "rnz encodes RNase Z, a zinc-dependent metallo-beta-lactamase-family endoribonuclease that performs tRNA "
        "3'-end maturation by removing 3' trailers from precursor tRNAs. Its generic RNA endonuclease and metal-binding "
        "annotations are secondary to the specific tRNA-processing endoribonuclease role."
    ),
    "PP_4462": (
        "PP_4462 encodes an RraA-like/class II aldolase-family candidate with product-name support for HMG-aldolase "
        "or regulator-of-ribonuclease-activity context but no GOA rows. The first-pass review leaves it unresolved "
        "pending stronger evidence for either metabolic lyase activity or RNase regulation."
    ),
    "srmB": (
        "srmB encodes a DEAD-box ATP-dependent RNA helicase related to SrmB/RhlE-like bacterial RNA helicases. It is "
        "best retained as a cytosolic RNA helicase candidate associated with ribosomal RNA/ribosome-biogenesis context, "
        "while generic nucleotide-binding and hydrolase annotations are less informative."
    ),
    "rnd": (
        "rnd encodes RNase D, a cytoplasmic 3'-5' exoribonuclease involved in 3' processing of precursor tRNAs. It "
        "initiates hydrolysis at RNA 3' termini and releases 5' mononucleotides, with the specific RNase D and tRNA "
        "3'-end-processing terms capturing the core role."
    ),
    "PP_4720": (
        "PP_4720 encodes a YhbY/CRM-domain RNA-binding protein candidate in Pseudomonas putida KT2440. Current evidence "
        "supports RNA binding, but not a specific RNase, helicase, or RNA-processing reaction."
    ),
    "dbpA": (
        "dbpA encodes a DEAD-box ATP-dependent RNA helicase with a DbpA/CsdA-like RNA-binding domain and predicted "
        "23S-rRNA specificity. It is best retained as a cytosolic RNA helicase/ribosome-assembly boundary factor rather "
        "than a generic hydrolase."
    ),
    "rph": (
        "rph encodes RNase PH, a phosphorolytic 3'-5' exoribonuclease that contributes to tRNA 3'-end maturation and "
        "can participate in starvation-associated rRNA degradation. The tRNA phosphorolysis/exonuclease role is the "
        "primary first-pass function; rRNA catabolism is kept as secondary context."
    ),
}

CORE = {
    "rnpA": [
        {
            "description": "Protein component of the RNase P ribonucleoprotein contributing to tRNA 5'-leader removal.",
            "contributes_to_molecular_function": "GO:0004526",
            "directly_involved_in": ["GO:0001682"],
            "in_complex": "GO:0030677",
        }
    ],
    "rng": [
        {
            "description": "RNase E/G-family RNA endoribonuclease activity in cytoplasmic rRNA/RNA processing.",
            "molecular_function": "GO:0004540",
            "directly_involved_in": ["GO:0006364"],
            "locations": ["GO:0005737"],
        }
    ],
    "rnt": [
        {
            "description": "Magnesium-dependent RNase T 3'-5' RNA exonuclease activity in tRNA/RNA end processing.",
            "molecular_function": "GO:0016896",
            "directly_involved_in": ["GO:0008033"],
            "locations": ["GO:0005829"],
        }
    ],
    "PP_1840": [
        {
            "description": "RraB-domain RNase-regulator candidate with unresolved target and no defensible GO-level activity in this first pass.",
        }
    ],
    "PP_2084": [
        {
            "description": "Class II aldolase activity converting 4-hydroxy-4-methyl-2-oxoglutarate to pyruvate.",
            "molecular_function": "GO:0047443",
        },
        {
            "description": "Secondary oxaloacetate decarboxylase activity assigned to the RraA-like aldolase fold.",
            "molecular_function": "GO:0008948",
        },
    ],
    "rnz": [
        {
            "description": "RNase Z tRNA 3'-trailer endoribonuclease activity in precursor-tRNA maturation.",
            "molecular_function": "GO:0042781",
            "directly_involved_in": ["GO:0042780"],
        }
    ],
    "PP_4462": [
        {
            "description": "RraA-like/class II aldolase-family candidate with unresolved metabolic versus RNase-regulator role.",
        }
    ],
    "srmB": [
        {
            "description": "DEAD-box ATP-dependent RNA helicase candidate associated with large-subunit/rRNA maturation context.",
            "molecular_function": "GO:0003724",
            "locations": ["GO:0005829"],
        }
    ],
    "rnd": [
        {
            "description": "RNase D 3'-5' exonuclease activity that removes extra residues from precursor tRNA 3' ends.",
            "molecular_function": "GO:0033890",
            "directly_involved_in": ["GO:0042780"],
            "locations": ["GO:0005737"],
        }
    ],
    "PP_4720": [
        {
            "description": "YhbY/CRM-domain RNA-binding protein candidate with no resolved processing reaction.",
            "molecular_function": "GO:0003723",
        }
    ],
    "dbpA": [
        {
            "description": "DbpA-family ATP-dependent RNA helicase with predicted 23S-rRNA specificity.",
            "molecular_function": "GO:0003724",
            "locations": ["GO:0005829"],
        }
    ],
    "rph": [
        {
            "description": "RNase PH phosphorolytic 3'-5' exoribonuclease/nucleotidyltransferase activity in tRNA 3'-end maturation.",
            "molecular_function": "GO:0009022",
            "directly_involved_in": ["GO:0008033"],
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
        "CC   -!- COFACTOR:",
        "CC   -!- SUBCELLULAR LOCATION:",
        "CC   -!- SIMILARITY:",
        "DR   GO;",
        "DR   InterPro;",
        "DR   Pfam;",
        "DR   PANTHER;",
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
        "rnpA": {
            "GO:0000049": review(
                "tRNA binding is appropriate substrate-binding context for the RNase P protein component.",
                "KEEP_AS_NON_CORE",
                "RnpA binds pre-tRNA leader/substrate context as part of RNase P, but the informative function is contribution to RNase P-mediated 5'-leader removal.",
                gene,
                term_id,
            ),
            "GO:0001682": review(
                "tRNA 5'-leader removal is the correct RNase P biological process.",
                "ACCEPT",
                "UniProt/HAMAP states that RNase P removes the 5'-leader sequence from pre-tRNA, which matches this process annotation.",
                gene,
                term_id,
            ),
            "GO:0004526": review(
                "Ribonuclease P activity is the correct complex-level molecular function for RnpA.",
                "ACCEPT",
                "The protein component does not act alone, but it contributes to the RNase P ribonucleoprotein activity captured by this GOA row.",
                gene,
                term_id,
            ),
            "GO:0008033": review(
                "Generic tRNA processing is true but less specific than tRNA 5'-leader removal for RNase P.",
                "MARK_AS_OVER_ANNOTATED",
                "The specific RNase P step is captured by GO:0001682; the parent tRNA-processing term is too broad for the core review.",
                gene,
                term_id,
            ),
            "GO:0030677": review(
                "Ribonuclease P complex membership is appropriate for RnpA.",
                "ACCEPT",
                "RnpA is the protein component of the RNase P ribonucleoprotein complex.",
                gene,
                term_id,
            ),
            "GO:0042780": review(
                "tRNA 3'-end processing is an electronic carryover inconsistent with RNase P protein function.",
                "MODIFY",
                "RNase P removes 5' leaders from precursor tRNAs, whereas 3'-end processing is better assigned to RNase Z/D/PH-family enzymes in this split.",
                gene,
                term_id,
                ["GO:0001682"],
            ),
            "GO:0042781": review(
                "3'-tRNA processing endoribonuclease activity is not the correct specific RNase P activity.",
                "MODIFY",
                "The correct complex-level activity is ribonuclease P activity, an endonucleolytic 5'-leader-removal reaction.",
                gene,
                term_id,
                ["GO:0004526"],
            ),
        },
        "rng": {
            "GO:0003676": review(
                "Nucleic acid binding is true but non-specific for an RNase E/G-family nuclease.",
                "KEEP_AS_NON_CORE",
                "The more informative activity is RNA nuclease activity.",
                gene,
                term_id,
            ),
            "GO:0003723": review(
                "RNA binding is substrate context for RNase G.",
                "KEEP_AS_NON_CORE",
                "The S1/RNase E/G domain supports RNA binding, but binding alone is less informative than RNA nuclease activity.",
                gene,
                term_id,
            ),
            "GO:0004540": review(
                "RNA nuclease activity is the supported RNase G molecular function.",
                "ACCEPT",
                "The protein is named endoribonuclease G and carries RNase E/G and S1 RNA-binding domains.",
                gene,
                term_id,
            ),
            "GO:0005737": review(
                "Cytoplasm is plausible location context for RNase G.",
                "ACCEPT",
                "The TreeGrafter GOA row places the protein in the bacterial cytoplasm.",
                gene,
                term_id,
            ),
            "GO:0006364": review(
                "rRNA processing is appropriate process context for the RNase G-family assignment.",
                "ACCEPT",
                "The PANTHER/TreeGrafter row supports rRNA processing and the protein belongs to the RNase E/G family.",
                gene,
                term_id,
            ),
            "GO:0006396": review(
                "Generic RNA processing is true but broader than the rRNA-processing row.",
                "MARK_AS_OVER_ANNOTATED",
                "The more specific supported process in this first pass is rRNA processing.",
                gene,
                term_id,
                ["GO:0006364"],
            ),
        },
        "rnt": {
            "GO:0000287": review(
                "Magnesium ion binding is valid cofactor context for RNase T.",
                "KEEP_AS_NON_CORE",
                "The catalytic active site uses magnesium, but metal binding is not the core RNA-processing function.",
                gene,
                term_id,
            ),
            "GO:0003676": review(
                "Nucleic acid binding is broad substrate context.",
                "KEEP_AS_NON_CORE",
                "RNase T is better captured by its 3'-5' RNA exonuclease activity.",
                gene,
                term_id,
            ),
            "GO:0004527": review(
                "Generic exonuclease activity is true but less informative than the RNA exonuclease terms.",
                "MARK_AS_OVER_ANNOTATED",
                "The record already has the RNA-specific 3'-5' exonuclease annotations that capture the core function more precisely.",
                gene,
                term_id,
                ["GO:0016896"],
            ),
            "GO:0004540": review(
                "RNA nuclease activity is correct but too broad for RNase T.",
                "MARK_AS_OVER_ANNOTATED",
                "RNase T is specifically a magnesium-dependent 3'-5' RNA exonuclease.",
                gene,
                term_id,
                ["GO:0016896"],
            ),
            "GO:0005829": review(
                "Cytosol is appropriate bacterial location context for RNase T.",
                "ACCEPT",
                "The TreeGrafter GOA row supports cytosol localization.",
                gene,
                term_id,
            ),
            "GO:0006396": review(
                "RNA processing is a broad but acceptable process parent for RNase T.",
                "KEEP_AS_NON_CORE",
                "UniProt describes trimming short 3' overhangs and tRNA end-turnover; tRNA processing is the more informative context.",
                gene,
                term_id,
            ),
            "GO:0008408": review(
                "3'-5' exonuclease activity is a supported RNase T molecular function.",
                "ACCEPT",
                "The RNase T family assignment and UniProt function support 3'-5' exonucleolytic trimming of RNA substrates.",
                gene,
                term_id,
            ),
            "GO:0016896": review(
                "RNA exonuclease activity producing 5'-phosphomonoesters is a core RNase T activity.",
                "ACCEPT",
                "UniProt/HAMAP describes RNase T trimming RNA 3' overhangs and the GOA row captures the RNA exonuclease reaction.",
                gene,
                term_id,
            ),
            "GO:0045004": review(
                "DNA replication proofreading is not supported for this bacterial RNase T record.",
                "REMOVE",
                "The protein is a ribonuclease T/exoribonuclease; the DNA proofreading row appears to be PANTHER carryover from polymerase exonuclease relatives.",
                gene,
                term_id,
            ),
        },
        "PP_2084": {
            "GO:0008428": review(
                "Ribonuclease inhibitor activity is plausible RraA-like side context but not the best-supported core function.",
                "KEEP_AS_NON_CORE",
                "The InterPro RraA assignment supports RNase-regulator context, while UniProt/Rhea provide more direct support for HMG aldolase and oxaloacetate decarboxylase chemistry.",
                gene,
                term_id,
            ),
            "GO:0008948": review(
                "Oxaloacetate decarboxylase activity is supported as a secondary activity of this aldolase fold.",
                "ACCEPT",
                "UniProt lists oxaloacetate decarboxylase activity with Rhea and EC support.",
                gene,
                term_id,
            ),
            "GO:0047443": review(
                "4-hydroxy-4-methyl-2-oxoglutarate aldolase activity is the strongest first-pass activity for PP_2084.",
                "ACCEPT",
                "UniProt describes catalysis of HMG cleavage into pyruvate and records EC 4.1.3.17/Rhea support.",
                gene,
                term_id,
            ),
            "GO:0051252": review(
                "Regulation of RNA metabolic process is RraA-like side context.",
                "KEEP_AS_NON_CORE",
                "The RraA domain explains why this gene entered the RNA-decay split, but the specific KT2440 RNA target and in vivo regulator role are not resolved.",
                gene,
                term_id,
            ),
        },
        "rnz": {
            "GO:0008033": review(
                "tRNA processing is true but less specific than RNase Z tRNA 3'-end processing.",
                "MARK_AS_OVER_ANNOTATED",
                "The specific RNase Z process is removal of 3' trailers from precursor tRNAs.",
                gene,
                term_id,
                ["GO:0042780"],
            ),
            "GO:0008270": review(
                "Zinc ion binding is valid cofactor context for RNase Z.",
                "KEEP_AS_NON_CORE",
                "RNase Z is a zinc-dependent phosphodiesterase, but the core function is tRNA 3'-processing endoribonuclease activity.",
                gene,
                term_id,
            ),
            "GO:0016891": review(
                "The generic RNA endonuclease term is true but less specific than the tRNA 3'-processing child term.",
                "MARK_AS_OVER_ANNOTATED",
                "GO:0042781 captures the tRNA substrate and 3'-trailer-removal context more precisely.",
                gene,
                term_id,
                ["GO:0042781"],
            ),
            "GO:0042780": review(
                "tRNA 3'-end processing is the correct RNase Z biological process.",
                "ACCEPT",
                "UniProt/HAMAP states that RNase Z removes 3' trailers from precursor tRNAs.",
                gene,
                term_id,
            ),
            "GO:0042781": review(
                "3'-tRNA processing endoribonuclease activity is the core RNase Z molecular function.",
                "ACCEPT",
                "The reviewed UniProt record assigns EC 3.1.26.11 and describes endonucleolytic removal of extra 3' nucleotides from tRNA precursors.",
                gene,
                term_id,
            ),
        },
        "srmB": {
            "GO:0000166": review(
                "Nucleotide binding is expected for a DEAD-box ATPase but not informative as a core function.",
                "MARK_AS_OVER_ANNOTATED",
                "RNA helicase activity is the more specific molecular function.",
                gene,
                term_id,
            ),
            "GO:0003676": review(
                "Nucleic acid binding is broad substrate context for SrmB.",
                "KEEP_AS_NON_CORE",
                "The DEAD-box helicase domains and GOA row support RNA helicase activity more specifically.",
                gene,
                term_id,
            ),
            "GO:0003724": review(
                "RNA helicase activity is the core SrmB molecular function.",
                "ACCEPT",
                "The record has DEAD/DEAH helicase domains and is named an ATP-dependent DEAD-box RNA helicase.",
                gene,
                term_id,
            ),
            "GO:0005524": review(
                "ATP binding is valid cofactor/substrate context for a DEAD-box RNA helicase.",
                "KEEP_AS_NON_CORE",
                "ATP binding supports helicase activity but is less informative than the RNA helicase term.",
                gene,
                term_id,
            ),
            "GO:0005829": review(
                "Cytosol is appropriate location context for this soluble bacterial RNA helicase.",
                "ACCEPT",
                "The TreeGrafter GOA row supports cytosol localization.",
                gene,
                term_id,
            ),
            "GO:0016787": review(
                "Generic hydrolase activity should be narrowed to RNA helicase activity.",
                "MODIFY",
                "DEAD-box helicases are ATP-dependent RNA remodeling enzymes; the generic hydrolase label hides the RNA-helicase function.",
                gene,
                term_id,
                ["GO:0003724"],
            ),
        },
        "rnd": {
            "GO:0000166": review(
                "Nucleotide binding is broad domain context for RNase D.",
                "KEEP_AS_NON_CORE",
                "The core function is 3'-5' exonucleolytic processing of RNA/tRNA substrates.",
                gene,
                term_id,
            ),
            "GO:0003676": review(
                "Nucleic acid binding is broad substrate context.",
                "KEEP_AS_NON_CORE",
                "RNase D is more specifically annotated by ribonuclease D and 3'-5' exonuclease activity terms.",
                gene,
                term_id,
            ),
            "GO:0005737": review(
                "Cytoplasm is the supported location for RNase D.",
                "ACCEPT",
                "UniProt/HAMAP places RNase D in the cytoplasm.",
                gene,
                term_id,
            ),
            "GO:0008033": review(
                "tRNA processing is true but less specific than tRNA 3'-end processing.",
                "MARK_AS_OVER_ANNOTATED",
                "The RNase D role is specifically precursor-tRNA 3'-end processing.",
                gene,
                term_id,
                ["GO:0042780"],
            ),
            "GO:0008408": review(
                "3'-5' exonuclease activity is a supported RNase D molecular function.",
                "ACCEPT",
                "The RNase D domains and UniProt function support hydrolysis from RNA 3' termini.",
                gene,
                term_id,
            ),
            "GO:0033890": review(
                "Ribonuclease D activity is the best specific molecular function for rnd.",
                "ACCEPT",
                "UniProt/HAMAP assigns EC 3.1.13.5 and describes removal of extra residues from tRNA 3' termini.",
                gene,
                term_id,
            ),
            "GO:0042780": review(
                "tRNA 3'-end processing is the core RNase D biological process.",
                "ACCEPT",
                "UniProt/HAMAP describes RNase D as involved in 3' processing of precursor tRNAs.",
                gene,
                term_id,
            ),
        },
        "PP_4720": {
            "GO:0003723": review(
                "RNA binding is the only supported function for the YhbY/CRM-domain PP_4720 protein.",
                "ACCEPT",
                "UniProt and GOA support an RNA-binding/YhbY-like domain, but no specific RNA-processing reaction is yet resolved.",
                gene,
                term_id,
            ),
        },
        "dbpA": {
            "GO:0000166": review(
                "Nucleotide binding is expected for a DEAD-box ATPase but too general.",
                "MARK_AS_OVER_ANNOTATED",
                "RNA helicase activity is the more informative molecular function.",
                gene,
                term_id,
            ),
            "GO:0003676": review(
                "Nucleic acid binding is broad substrate context for DbpA.",
                "KEEP_AS_NON_CORE",
                "The DbpA/CsdA and DEAD-box domains support a more specific RNA helicase function.",
                gene,
                term_id,
            ),
            "GO:0003724": review(
                "RNA helicase activity is the core DbpA molecular function.",
                "ACCEPT",
                "The protein is named an ATP-dependent RNA helicase specific for 23S rRNA and carries DEAD-box helicase domains.",
                gene,
                term_id,
            ),
            "GO:0005524": review(
                "ATP binding is valid substrate context for DbpA.",
                "KEEP_AS_NON_CORE",
                "ATP binding supports the helicase cycle but is less informative than RNA helicase activity.",
                gene,
                term_id,
            ),
            "GO:0005829": review(
                "Cytosol is appropriate location context for DbpA.",
                "ACCEPT",
                "The TreeGrafter GOA row supports cytosol localization.",
                gene,
                term_id,
            ),
            "GO:0016787": review(
                "Generic hydrolase activity should be narrowed to RNA helicase activity.",
                "MODIFY",
                "The ATP hydrolysis is coupled to RNA helicase/remodeling activity.",
                gene,
                term_id,
                ["GO:0003724"],
            ),
        },
        "rph": {
            "GO:0000049": review(
                "tRNA binding is substrate context for RNase PH.",
                "KEEP_AS_NON_CORE",
                "The core activity is phosphorolytic 3'-5' exonucleolytic processing of tRNA ends.",
                gene,
                term_id,
            ),
            "GO:0000175": review(
                "3'-5'-RNA exonuclease activity is a core RNase PH function.",
                "ACCEPT",
                "UniProt/HAMAP describes RNase PH as a phosphorolytic 3'-5' exoribonuclease.",
                gene,
                term_id,
            ),
            "GO:0003723": review(
                "RNA binding is substrate context for RNase PH.",
                "KEEP_AS_NON_CORE",
                "RNA binding is expected for this enzyme but less informative than exonuclease/nucleotidyltransferase activity.",
                gene,
                term_id,
            ),
            "GO:0008033": review(
                "tRNA processing is the main biological process for RNase PH.",
                "ACCEPT",
                "UniProt/HAMAP states that RNase PH plays an important role in tRNA 3'-end maturation.",
                gene,
                term_id,
            ),
            "GO:0009022": review(
                "tRNA nucleotidyltransferase activity is the phosphorolytic RNase PH reaction captured by EC 2.7.7.56.",
                "ACCEPT",
                "UniProt and Rhea support the reversible tRNA nucleotidyltransferase/phosphorolysis chemistry.",
                gene,
                term_id,
            ),
            "GO:0016075": review(
                "rRNA catabolic process is supported as secondary starvation-associated context.",
                "KEEP_AS_NON_CORE",
                "UniProt says RNase PH probably contributes to initiation of 16S rRNA degradation during starvation, but tRNA maturation is the primary first-pass role.",
                gene,
                term_id,
            ),
            "GO:0031125": review(
                "rRNA 3'-end processing is a weak ARBA-level process call for RNase PH.",
                "MODIFY",
                "The better-supported rRNA-related process from UniProt/HAMAP is starvation-associated rRNA catabolism rather than a specific rRNA 3'-end maturation role.",
                gene,
                term_id,
                ["GO:0016075"],
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
    if spec.get("contributes_to_molecular_function"):
        mf = spec["contributes_to_molecular_function"]
        out["contributes_to_molecular_function"] = t(mf)
        support_items.extend(evidence_for(gene, mf))
    if spec.get("directly_involved_in"):
        out["directly_involved_in"] = [t(x) for x in spec["directly_involved_in"]]
        for process_id in spec["directly_involved_in"]:
            add_support(support_items, support(file_id(gene, "goa.tsv"), goa_line(gene, process_id)))
    if spec.get("locations"):
        out["locations"] = [t(x) for x in spec["locations"]]
        for location_id in spec["locations"]:
            add_support(support_items, support(file_id(gene, "goa.tsv"), goa_line(gene, location_id)))
    if spec.get("in_complex"):
        out["in_complex"] = t(spec["in_complex"])
        add_support(support_items, support(file_id(gene, "goa.tsv"), goa_line(gene, spec["in_complex"])))
    out["supported_by"] = support_items
    return out


def suggested_question(gene: str) -> list[dict[str, str]]:
    if gene in {"PP_1840", "PP_4462"}:
        return [
            {
                "question": f"Does {gene} regulate a specific P. putida RNase, or is the RraA/RraB-like product name an unsupported family transfer?"
            }
        ]
    if gene == "PP_2084":
        return [
            {
                "question": "Is PP_2084 primarily a metabolic class II aldolase in KT2440, or does it also regulate RNase E/G-family RNA turnover in vivo?"
            }
        ]
    if gene == "PP_4720":
        return [
            {
                "question": "What RNA species are bound by PP_4720/YhbY, and does this binding alter ribosome maturation or RNA turnover?"
            }
        ]
    return [
        {
            "question": f"What are the direct RNA substrates and stress-condition phenotypes for {gene} in P. putida KT2440?"
        }
    ]


def suggested_experiment(gene: str) -> list[dict[str, str]]:
    if gene in SIDE_NODE_GENES:
        return [
            {
                "description": f"Combine affinity pulldown/RNA co-purification with {gene} deletion or depletion to identify RNA or RNase partners before assigning a specific RNA-processing pathway role.",
                "experiment_type": "RNA/protein interaction and perturbation assay",
            }
        ]
    return [
        {
            "description": f"Compare wild-type and {gene} perturbation strains by RNA end-mapping or RNA-seq under exponential, stationary-phase, and stress conditions to identify direct processing defects.",
            "experiment_type": "RNA end-mapping and stress RNA-seq assay",
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
        f"# {gene} RNase/RNA-decay boundary first-pass notes",
        "",
        "- First-pass curation date: 2026-07-10.",
        f"- Batch: `{BATCH_TSV}`.",
        f"- Asta retrieval report: `{file_id(gene, 'deep-research-asta.md')}`. The report is retained as provenance; annotation decisions are supported by local UniProt and GOA rows.",
        f"- Main conclusion: {CORE[gene][0]['description']}",
    ]
    gene_file(gene, "notes.md").write_text("\n".join(notes) + "\n", encoding="utf-8")


def clean_id(text: str) -> str:
    out = re.sub(r"[^A-Za-z0-9_]+", "_", text.lower())
    out = re.sub(r"_+", "_", out).strip("_")
    return out


def annoton(
    gene: str,
    label: str,
    role: str,
    function_id: str | None = None,
    processes: list[str] | None = None,
    locations: list[str] | None = None,
) -> dict:
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


def write_module() -> None:
    module = {
        "id": "MODULE:rna_decay_processing_boundary",
        "title": "RNase, RNA-decay, and RNA-processing boundary",
        "description": (
            "Boundary module for PSEPK translation/RNA-processing genes covering RNase P/G/T/Z/D/PH activities, "
            "DEAD-box RNA helicase context, and RraA/RraB/YhbY-like side nodes. The module separates catalytic "
            "nuclease or helicase roles from generic RNA-binding, broad hydrolase, and low-information RNase-regulator "
            "family transfers."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_TSV}",
                "title": "PSEPK translation/RNA RNase and RNA-decay-processing split",
                "statement": "The batch records RNase P/G/T/Z/D/PH proteins, DEAD-box RNA helicases, and RraA/RraB/YhbY-like side nodes.",
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
            "id": "rna_decay_processing_boundary",
            "label": "RNase, RNA-decay, and RNA-processing boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {"preferred_term": TERM[x]["label"], "term": t(x)}
                for x in [
                    "GO:0004526",
                    "GO:0001682",
                    "GO:0042781",
                    "GO:0042780",
                    "GO:0033890",
                    "GO:0009022",
                    "GO:0003724",
                    "GO:0006364",
                ]
            ],
            "parts": [
                {
                    "order": 1,
                    "role": "tRNA-processing ribonucleases",
                    "node": {
                        "id": "trna_processing_ribonucleases",
                        "label": "tRNA-processing ribonucleases",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "RNase P/Z/D/PH and RNase T activities involved in bacterial tRNA end processing or turnover.",
                        "annotons": [
                            annoton(
                                "rnpA",
                                "RNase P protein component",
                                CORE["rnpA"][0]["description"],
                                "GO:0004526",
                                ["GO:0001682"],
                            ),
                            annoton(
                                "rnz",
                                "RNase Z tRNA 3-prime endonuclease",
                                CORE["rnz"][0]["description"],
                                "GO:0042781",
                                ["GO:0042780"],
                            ),
                            annoton(
                                "rnd",
                                "RNase D tRNA 3-prime exonuclease",
                                CORE["rnd"][0]["description"],
                                "GO:0033890",
                                ["GO:0042780"],
                                ["GO:0005737"],
                            ),
                            annoton(
                                "rnt",
                                "RNase T RNA exonuclease",
                                CORE["rnt"][0]["description"],
                                "GO:0016896",
                                ["GO:0008033"],
                                ["GO:0005829"],
                            ),
                            annoton(
                                "rph",
                                "RNase PH phosphorolytic tRNA-processing enzyme",
                                CORE["rph"][0]["description"],
                                "GO:0009022",
                                ["GO:0008033"],
                            ),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "rRNA/RNA processing nucleases and helicases",
                    "node": {
                        "id": "rrna_rna_processing_nucleases_helicases",
                        "label": "rRNA/RNA processing nucleases and helicases",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "RNase G and DEAD-box helicases with first-pass support for RNA/rRNA processing and remodeling.",
                        "annotons": [
                            annoton(
                                "rng",
                                "RNase G RNA nuclease",
                                CORE["rng"][0]["description"],
                                "GO:0004540",
                                ["GO:0006364"],
                                ["GO:0005737"],
                            ),
                            annoton(
                                "srmB",
                                "SrmB DEAD-box RNA helicase",
                                CORE["srmB"][0]["description"],
                                "GO:0003724",
                                None,
                                ["GO:0005829"],
                            ),
                            annoton(
                                "dbpA",
                                "DbpA 23S-rRNA RNA helicase",
                                CORE["dbpA"][0]["description"],
                                "GO:0003724",
                                None,
                                ["GO:0005829"],
                            ),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "RNase-regulator and RNA-binding side nodes",
                    "node": {
                        "id": "rnase_regulator_rna_binding_side_nodes",
                        "label": "RNase-regulator and RNA-binding side nodes",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "RraA/RraB-like and YhbY/CRM-domain entries that entered the split by RNase-regulator or RNA-binding context but are not yet resolved as catalytic RNA-processing factors.",
                        "annotons": [
                            annoton(
                                "PP_1840",
                                "unresolved RraB-domain RNase-regulator candidate",
                                CORE["PP_1840"][0]["description"],
                            ),
                            annoton(
                                "PP_2084",
                                "RraA-like HMG aldolase side node",
                                CORE["PP_2084"][0]["description"],
                                "GO:0047443",
                            ),
                            annoton(
                                "PP_4462",
                                "unresolved RraA-like side node",
                                CORE["PP_4462"][0]["description"],
                            ),
                            annoton(
                                "PP_4720",
                                "YhbY CRM-domain RNA-binding candidate",
                                CORE["PP_4720"][0]["description"],
                                "GO:0003723",
                            ),
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
