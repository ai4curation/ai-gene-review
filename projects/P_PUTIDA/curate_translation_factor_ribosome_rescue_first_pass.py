#!/usr/bin/env python3
"""First-pass curation for translation-factor and ribosome-rescue genes."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
GENE_ROOT = ROOT / "genes" / "PSEPK"
MODULE_PATH = ROOT / "modules" / "translation_factor_ribosome_rescue_boundary.yaml"
BATCH_TSV = (
    "projects/P_PUTIDA/batches/"
    "module_translation_rna_processing_translation_factors_ribosome_rescue.tsv"
)
TAXON_LABEL = "Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # type: ignore[override]
        return True


TERM = {
    "GO:0000049": {"id": "GO:0000049", "label": "tRNA binding"},
    "GO:0000166": {"id": "GO:0000166", "label": "nucleotide binding"},
    "GO:0000287": {"id": "GO:0000287", "label": "magnesium ion binding"},
    "GO:0001514": {"id": "GO:0001514", "label": "selenocysteine incorporation"},
    "GO:0002184": {"id": "GO:0002184", "label": "cytoplasmic translational termination"},
    "GO:0003676": {"id": "GO:0003676", "label": "nucleic acid binding"},
    "GO:0003677": {"id": "GO:0003677", "label": "DNA binding"},
    "GO:0003723": {"id": "GO:0003723", "label": "RNA binding"},
    "GO:0003727": {"id": "GO:0003727", "label": "single-stranded RNA binding"},
    "GO:0003743": {"id": "GO:0003743", "label": "translation initiation factor activity"},
    "GO:0003746": {"id": "GO:0003746", "label": "translation elongation factor activity"},
    "GO:0003747": {"id": "GO:0003747", "label": "translation release factor activity"},
    "GO:0003924": {"id": "GO:0003924", "label": "GTPase activity"},
    "GO:0004045": {"id": "GO:0004045", "label": "peptidyl-tRNA hydrolase activity"},
    "GO:0005524": {"id": "GO:0005524", "label": "ATP binding"},
    "GO:0005525": {"id": "GO:0005525", "label": "GTP binding"},
    "GO:0005737": {"id": "GO:0005737", "label": "cytoplasm"},
    "GO:0005829": {"id": "GO:0005829", "label": "cytosol"},
    "GO:0005886": {"id": "GO:0005886", "label": "plasma membrane"},
    "GO:0006412": {"id": "GO:0006412", "label": "translation"},
    "GO:0006413": {"id": "GO:0006413", "label": "translational initiation"},
    "GO:0006414": {"id": "GO:0006414", "label": "translational elongation"},
    "GO:0006415": {"id": "GO:0006415", "label": "translational termination"},
    "GO:0006417": {"id": "GO:0006417", "label": "regulation of translation"},
    "GO:0006515": {
        "id": "GO:0006515",
        "label": "protein quality control for misfolded or incompletely synthesized proteins",
    },
    "GO:0016887": {"id": "GO:0016887", "label": "ATP hydrolysis activity"},
    "GO:0017111": {
        "id": "GO:0017111",
        "label": "ribonucleoside triphosphate phosphatase activity",
    },
    "GO:0019843": {"id": "GO:0019843", "label": "rRNA binding"},
    "GO:0034605": {"id": "GO:0034605", "label": "cellular response to heat"},
    "GO:0043022": {"id": "GO:0043022", "label": "ribosome binding"},
    "GO:0043023": {"id": "GO:0043023", "label": "ribosomal large subunit binding"},
    "GO:0045727": {"id": "GO:0045727", "label": "positive regulation of translation"},
    "GO:0045900": {"id": "GO:0045900", "label": "negative regulation of translational elongation"},
    "GO:0046872": {"id": "GO:0046872", "label": "metal ion binding"},
    "GO:0070929": {"id": "GO:0070929", "label": "trans-translation"},
    "GO:0070930": {"id": "GO:0070930", "label": "trans-translation-dependent protein tagging"},
    "GO:0072344": {"id": "GO:0072344", "label": "rescue of stalled cytosolic ribosome"},
    "GO:0097216": {"id": "GO:0097216", "label": "guanosine tetraphosphate binding"},
}

GENES = ["hslR", "selB", "ettA", "ychF", "pth", "lepA", "frr", "arfB", "infA", "smpB"]

DESCRIPTIONS = {
    "hslR": (
        "hslR encodes heat shock protein 15, a ribosome-associated S4-domain RNA-binding protein in Pseudomonas "
        "putida KT2440. The supported role is binding RNA and the large ribosomal subunit during heat-stress or "
        "ribosome-associated stress context, not DNA-specific regulation."
    ),
    "selB": (
        "selB encodes the bacterial selenocysteyl-tRNA-specific translation elongation factor. It is a cytoplasmic "
        "GTP-dependent elongation factor that recognizes selenocysteyl-tRNA and supports co-translational "
        "selenocysteine incorporation."
    ),
    "ettA": (
        "ettA encodes an ABCF-family energy-dependent translational throttle. It binds the 70S ribosome and uses "
        "ATP hydrolysis to gate progression from the initiation complex into elongation in response to cellular "
        "energy status."
    ),
    "ychF": (
        "ychF encodes a conserved ribosome-binding ATPase of the OBG-HflX-like/YchF family. It binds the 70S "
        "ribosome and 50S subunit and is best treated here as a ribosome-associated ATPase rather than a generic "
        "GTP-binding protein."
    ),
    "pth": (
        "pth encodes peptidyl-tRNA hydrolase Pth, a cytoplasmic enzyme that hydrolyzes ribosome-free or stalled "
        "peptidyl-tRNAs to recycle tRNA and maintain translation quality control."
    ),
    "lepA": (
        "lepA encodes elongation factor 4, also known as EF-4 or ribosomal back-translocase LepA. It is a "
        "peripheral inner-membrane, ribosome-binding translational GTPase that supports accurate and efficient "
        "protein synthesis under stress."
    ),
    "frr": (
        "frr encodes ribosome-recycling factor, a cytoplasmic protein that releases ribosomes from mRNA after "
        "translation termination and supports reuse of ribosomal subunits for subsequent protein synthesis."
    ),
    "arfB": (
        "arfB encodes alternative ribosome-rescue factor B, a release-factor-family peptidyl-tRNA hydrolase that "
        "binds stalled ribosomes and releases nascent peptidyl-tRNA when canonical termination cannot proceed."
    ),
    "infA": (
        "infA encodes translation initiation factor IF-1, a cytoplasmic ribosome-binding initiation factor that "
        "stabilizes the bacterial 30S pre-initiation complex and helps form the mature 70S initiation complex."
    ),
    "smpB": (
        "smpB encodes SsrA-binding protein SmpB, the protein partner of tmRNA in trans-translation. The SmpB-tmRNA "
        "complex rescues stalled ribosomes and tags incomplete nascent proteins for degradation."
    ),
}


CORE = {
    "hslR": {
        "description": "Ribosomal large-subunit and single-stranded RNA-binding heat-shock protein.",
        "molecular_function": "GO:0043023",
        "directly_involved_in": ["GO:0034605"],
    },
    "selB": {
        "description": "Selenocysteyl-tRNA-specific translation elongation factor.",
        "molecular_function": "GO:0003746",
        "directly_involved_in": ["GO:0001514", "GO:0006414"],
        "locations": ["GO:0005737"],
    },
    "ettA": {
        "description": "ATP-dependent ribosome-bound translational throttle.",
        "molecular_function": "GO:0016887",
        "directly_involved_in": ["GO:0045900"],
        "locations": ["GO:0005737"],
    },
    "ychF": {
        "description": "Ribosome-associated ATPase of the YchF/OLA1 family.",
        "molecular_function": "GO:0016887",
        "locations": ["GO:0005737"],
    },
    "pth": {
        "description": "Peptidyl-tRNA hydrolase for stalled or dropped-off peptidyl-tRNAs.",
        "molecular_function": "GO:0004045",
        "directly_involved_in": ["GO:0072344", "GO:0006515"],
        "locations": ["GO:0005737"],
    },
    "lepA": {
        "description": "Ribosome-binding EF-4 translational GTPase/back-translocase.",
        "molecular_function": "GO:0003746",
        "directly_involved_in": ["GO:0006414"],
        "locations": ["GO:0005886"],
    },
    "frr": {
        "description": "Ribosome-recycling factor for post-termination ribosome release.",
        "molecular_function": "GO:0043023",
        "directly_involved_in": ["GO:0002184", "GO:0006415"],
        "locations": ["GO:0005737"],
    },
    "arfB": {
        "description": "Alternative stalled-ribosome rescue peptidyl-tRNA hydrolase.",
        "molecular_function": "GO:0004045",
        "directly_involved_in": ["GO:0072344"],
        "locations": ["GO:0005737"],
    },
    "infA": {
        "description": "Translation initiation factor IF-1.",
        "molecular_function": "GO:0003743",
        "directly_involved_in": ["GO:0006413"],
        "locations": ["GO:0005737"],
    },
    "smpB": {
        "description": "tmRNA-binding trans-translation and stalled-ribosome rescue factor.",
        "molecular_function": "GO:0003723",
        "directly_involved_in": ["GO:0070929", "GO:0070930"],
        "locations": ["GO:0005737"],
    },
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


def evidence_for(gene: str, term_id: str | None = None) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    if term_id:
        add_support(items, support(file_id(gene, "goa.tsv"), goa_line(gene, term_id)))
    uniprot = gene_file(gene, "uniprot.txt")
    for marker in (
        "DE   ",
        "CC   -!- FUNCTION:",
        "CC   -!- CATALYTIC ACTIVITY:",
        "CC   -!- SUBUNIT:",
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


def term(term_id: str) -> dict[str, str]:
    return TERM[term_id]


def review(summary: str, action: str, reason: str, gene: str, term_id: str, replacements: list[str] | None = None) -> dict:
    out = {
        "summary": summary,
        "action": action,
        "reason": reason,
        "supported_by": evidence_for(gene, term_id),
    }
    if replacements:
        out["proposed_replacement_terms"] = [term(x) for x in replacements]
    return out


def review_for(gene: str, term_id: str) -> dict:
    decisions = {
        "hslR": {
            "GO:0003677": review(
                "Generic DNA binding is not supported as the main role of Hsp15.",
                "MARK_AS_OVER_ANNOTATED",
                "The more informative supported terms are single-stranded RNA binding and ribosomal large-subunit binding.",
                gene,
                term_id,
            ),
            "GO:0003723": review(
                "Generic RNA binding should be narrowed to single-stranded RNA binding.",
                "MODIFY",
                "The same InterPro/HSP15 evidence supports the more specific single-stranded RNA-binding row.",
                gene,
                term_id,
                ["GO:0003727"],
            ),
            "GO:0003727": review(
                "Single-stranded RNA binding is supported for this HSP15/S4-domain protein.",
                "ACCEPT",
                "Hsp15 carries S4/HSP15 RNA-binding domain evidence and a matching GOA row.",
                gene,
                term_id,
            ),
            "GO:0034605": review(
                "Cellular response to heat is appropriate heat-shock context for Hsp15.",
                "ACCEPT",
                "The protein is named heat shock protein 15 and the GOA row is domain-supported.",
                gene,
                term_id,
            ),
            "GO:0043023": review(
                "Ribosomal large-subunit binding is supported and functionally informative.",
                "ACCEPT",
                "Hsp15 is a ribosome-associated RNA-binding protein with InterPro support for this row.",
                gene,
                term_id,
            ),
        },
        "selB": {
            "GO:0001514": review(
                "Selenocysteine incorporation is the specific process for SelB.",
                "ACCEPT",
                "SelB is the selenocysteyl-tRNA-specific elongation factor.",
                gene,
                term_id,
            ),
            "GO:0003723": review(
                "RNA binding is secondary context for SelB.",
                "KEEP_AS_NON_CORE",
                "SelB recognizes RNA/tRNA-related substrates, but the core call is selenocysteyl-tRNA-specific elongation factor activity.",
                gene,
                term_id,
            ),
            "GO:0003746": review(
                "Translation elongation factor activity is the core molecular function.",
                "ACCEPT",
                "The product name and domain evidence identify SelB as a translation elongation factor.",
                gene,
                term_id,
            ),
            "GO:0003924": review(
                "GTPase activity is appropriate for this translational GTPase.",
                "ACCEPT",
                "SelB is a GTP-dependent translation elongation factor.",
                gene,
                term_id,
            ),
            "GO:0005525": review(
                "GTP binding is valid cofactor context but not the core function.",
                "KEEP_AS_NON_CORE",
                "GTP binding supports the elongation-factor role and should not displace the more specific functional terms.",
                gene,
                term_id,
            ),
            "GO:0005737": review(
                "Cytoplasm is the expected location for bacterial translation elongation.",
                "ACCEPT",
                "The UniProt subcellular-location mapping supports cytoplasm.",
                gene,
                term_id,
            ),
            "GO:0006414": review(
                "Translational elongation is appropriate process context for SelB.",
                "ACCEPT",
                "SelB delivers selenocysteyl-tRNA during translation elongation.",
                gene,
                term_id,
            ),
        },
        "ettA": {
            "GO:0000049": review(
                "tRNA binding is real contact context but not the core EttA function.",
                "KEEP_AS_NON_CORE",
                "EttA contacts P-site tRNA while functioning as an ATP-dependent ribosome-bound translational throttle.",
                gene,
                term_id,
            ),
            "GO:0000166": review(
                "Generic nucleotide binding is over-broad for an ABCF ATPase.",
                "MARK_AS_OVER_ANNOTATED",
                "ATP binding and ATP hydrolysis activity are already present and are more informative.",
                gene,
                term_id,
            ),
            "GO:0005524": review(
                "ATP binding is valid cofactor context for EttA.",
                "KEEP_AS_NON_CORE",
                "ATP binding supports the ATP-hydrolysis-dependent throttle role.",
                gene,
                term_id,
            ),
            "GO:0005737": review(
                "Cytoplasm is appropriate for a soluble ribosome-associated translation factor.",
                "ACCEPT",
                "UniProt places EttA in the cytoplasm and notes ribosome/polysome association.",
                gene,
                term_id,
            ),
            "GO:0016887": review(
                "ATP hydrolysis activity is a core molecular function for EttA.",
                "ACCEPT",
                "UniProt/HAMAP describes ATP hydrolysis as part of EttA release from the ribosome.",
                gene,
                term_id,
            ),
            "GO:0019843": review(
                "rRNA binding is ribosome-contact context for EttA.",
                "KEEP_AS_NON_CORE",
                "The core function is ATP-dependent translational throttling rather than rRNA binding alone.",
                gene,
                term_id,
            ),
            "GO:0043022": review(
                "Ribosome binding is supported for EttA.",
                "ACCEPT",
                "UniProt states that EttA binds the 70S ribosome E-site.",
                gene,
                term_id,
            ),
            "GO:0045900": review(
                "Negative regulation of translational elongation captures the throttle process.",
                "ACCEPT",
                "EttA gates progression from initiation into elongation according to ATP/ADP status.",
                gene,
                term_id,
            ),
        },
        "ychF": {
            "GO:0000287": review(
                "Magnesium ion binding is cofactor context for this P-loop NTPase.",
                "KEEP_AS_NON_CORE",
                "The core function is ATP hydrolysis coupled to ribosome binding.",
                gene,
                term_id,
            ),
            "GO:0005524": review(
                "ATP binding is valid but secondary to ATP hydrolysis activity.",
                "KEEP_AS_NON_CORE",
                "UniProt names the protein as a ribosome-binding ATPase.",
                gene,
                term_id,
            ),
            "GO:0005525": review(
                "GTP binding is probably a broad family transfer for YchF.",
                "MARK_AS_OVER_ANNOTATED",
                "The curated product and UniRule evidence in this record emphasize ATPase activity rather than GTP binding as the core call.",
                gene,
                term_id,
            ),
            "GO:0005737": review(
                "Cytoplasm is appropriate for this bacterial ribosome-associated ATPase.",
                "ACCEPT",
                "The TreeGrafter location row supports cytoplasm.",
                gene,
                term_id,
            ),
            "GO:0016887": review(
                "ATP hydrolysis activity is the supported core molecular function.",
                "ACCEPT",
                "UniProt/HAMAP describes YchF as an ATPase that binds 70S ribosomes and 50S subunits.",
                gene,
                term_id,
            ),
            "GO:0017111": review(
                "Generic ribonucleoside triphosphate phosphatase activity should be narrowed to ATP hydrolysis activity.",
                "MODIFY",
                "The record has specific ATP hydrolysis evidence, making the broad ARBA NTPase row unnecessary as a core term.",
                gene,
                term_id,
                ["GO:0016887"],
            ),
            "GO:0043022": review(
                "Generic ribosome binding should be narrowed to the large-subunit row already present.",
                "MODIFY",
                "UniProt describes binding to 70S and 50S ribosomal particles, and the GOA includes ribosomal large subunit binding.",
                gene,
                term_id,
                ["GO:0043023"],
            ),
            "GO:0043023": review(
                "Ribosomal large-subunit binding is supported for YchF.",
                "ACCEPT",
                "UniProt/HAMAP describes 50S ribosomal subunit binding.",
                gene,
                term_id,
            ),
            "GO:0046872": review(
                "Generic metal ion binding is non-core cofactor context.",
                "KEEP_AS_NON_CORE",
                "Magnesium is expected for P-loop NTPases but does not describe YchF's biological role.",
                gene,
                term_id,
            ),
        },
        "pth": {
            "GO:0000049": review(
                "tRNA binding is substrate-context for Pth.",
                "KEEP_AS_NON_CORE",
                "The enzymatic core function is peptidyl-tRNA hydrolase activity.",
                gene,
                term_id,
            ),
            "GO:0004045": review(
                "Peptidyl-tRNA hydrolase activity is the core molecular function.",
                "ACCEPT",
                "UniProt/HAMAP describes hydrolysis of peptidyl-tRNAs and includes EC 3.1.1.29/Rhea support.",
                gene,
                term_id,
            ),
            "GO:0005737": review(
                "Cytoplasm is appropriate for Pth.",
                "ACCEPT",
                "UniProt places Pth in the cytoplasm.",
                gene,
                term_id,
            ),
            "GO:0006515": review(
                "Protein quality control is appropriate process context.",
                "ACCEPT",
                "Pth recycles dropped-off or stalled peptidyl-tRNAs from incomplete translation events.",
                gene,
                term_id,
            ),
            "GO:0072344": review(
                "Rescue of stalled cytosolic ribosome is appropriate for Pth.",
                "ACCEPT",
                "UniProt states that Pth releases premature peptidyl moieties from peptidyl-tRNAs trapped in stalled 50S subunits.",
                gene,
                term_id,
            ),
        },
        "lepA": {
            "GO:0003746": review(
                "Translation elongation factor activity is appropriate for EF-4/LepA.",
                "ACCEPT",
                "UniProt identifies LepA as elongation factor 4 and ribosomal back-translocase.",
                gene,
                term_id,
            ),
            "GO:0003924": review(
                "GTPase activity is a core catalytic property of LepA.",
                "ACCEPT",
                "UniProt/HAMAP gives the GTP hydrolysis reaction for LepA.",
                gene,
                term_id,
            ),
            "GO:0005525": review(
                "GTP binding is valid cofactor context.",
                "KEEP_AS_NON_CORE",
                "GTP binding supports the EF-4 GTPase role but is not the core biological function.",
                gene,
                term_id,
            ),
            "GO:0005886": review(
                "Plasma membrane is appropriate for the peripheral inner-membrane localization.",
                "ACCEPT",
                "UniProt places LepA at the cell inner membrane on the cytoplasmic side.",
                gene,
                term_id,
            ),
            "GO:0006414": review(
                "Translational elongation is appropriate process context.",
                "ACCEPT",
                "EF-4 acts on improperly translocated ribosomes during elongation.",
                gene,
                term_id,
            ),
            "GO:0043022": review(
                "Ribosome binding is supported for LepA.",
                "ACCEPT",
                "UniProt states that LepA binds ribosomes in a GTP-dependent manner.",
                gene,
                term_id,
            ),
            "GO:0045727": review(
                "Positive regulation of translation is broad but acceptable stress/fidelity context.",
                "KEEP_AS_NON_CORE",
                "The more direct process is translational elongation/back-translocation, but the row is directionally consistent.",
                gene,
                term_id,
            ),
            "GO:0097216": review(
                "Guanosine tetraphosphate binding is not supported by the main LepA record.",
                "MARK_AS_OVER_ANNOTATED",
                "This ARBA-derived row is not needed to explain the EF-4 GTPase/ribosome-binding function.",
                gene,
                term_id,
            ),
        },
        "frr": {
            "GO:0002184": review(
                "Cytoplasmic translational termination is appropriate process context.",
                "ACCEPT",
                "RRF acts after termination to release ribosomes from mRNA.",
                gene,
                term_id,
            ),
            "GO:0005737": review(
                "Cytoplasm is appropriate for ribosome recycling factor.",
                "ACCEPT",
                "UniProt places RRF in the cytoplasm.",
                gene,
                term_id,
            ),
            "GO:0005829": review(
                "Cytosol is acceptable cytoplasmic location context.",
                "ACCEPT",
                "The logical cytosol inference follows from cytoplasmic translational termination.",
                gene,
                term_id,
            ),
            "GO:0006412": review(
                "Generic translation is correct but less informative than termination/recycling context.",
                "KEEP_AS_NON_CORE",
                "RRF is not a general translation enzyme; it acts during post-termination ribosome recycling.",
                gene,
                term_id,
            ),
            "GO:0006415": review(
                "Translational termination is appropriate context for ribosome recycling factor.",
                "ACCEPT",
                "RRF releases ribosomes from mRNA at termination of protein biosynthesis.",
                gene,
                term_id,
            ),
            "GO:0043023": review(
                "Ribosomal large-subunit binding is supported.",
                "ACCEPT",
                "The TreeGrafter row and RRF family context support large-subunit binding.",
                gene,
                term_id,
            ),
        },
        "arfB": {
            "GO:0003747": review(
                "Translation release factor activity is appropriate for ArfB.",
                "ACCEPT",
                "ArfB is a release-factor-family protein used in alternative ribosome rescue.",
                gene,
                term_id,
            ),
            "GO:0004045": review(
                "Peptidyl-tRNA hydrolase activity is a core catalytic function for ArfB.",
                "ACCEPT",
                "UniProt/Rhea/EC evidence supports peptidyl-tRNA hydrolase activity.",
                gene,
                term_id,
            ),
            "GO:0005737": review(
                "Cytoplasm is appropriate for a bacterial ribosome rescue factor.",
                "ACCEPT",
                "The UniProt subcellular-location row supports cytoplasm.",
                gene,
                term_id,
            ),
            "GO:0006415": review(
                "Translational termination is too generic for ArfB's rescue role.",
                "MODIFY",
                "ArfB functions in rescue of stalled cytosolic ribosomes rather than canonical stop-codon termination.",
                gene,
                term_id,
                ["GO:0072344"],
            ),
            "GO:0043022": review(
                "Ribosome binding is supported for ArfB.",
                "ACCEPT",
                "ArfB acts on stalled ribosomes and has a TreeGrafter ribosome-binding row.",
                gene,
                term_id,
            ),
            "GO:0072344": review(
                "Rescue of stalled cytosolic ribosome is the correct process for ArfB.",
                "ACCEPT",
                "ArfB is annotated and named as alternative ribosome-rescue factor B.",
                gene,
                term_id,
            ),
        },
        "infA": {
            "GO:0003676": review(
                "Generic nucleic-acid binding is over-broad for IF-1.",
                "MARK_AS_OVER_ANNOTATED",
                "Translation initiation factor activity, ribosome binding, and rRNA binding are more informative.",
                gene,
                term_id,
            ),
            "GO:0003723": review(
                "Generic RNA binding should be treated as non-core context.",
                "KEEP_AS_NON_CORE",
                "IF-1 is best described as a translation initiation factor; RNA/rRNA contacts are supporting context.",
                gene,
                term_id,
            ),
            "GO:0003743": review(
                "Translation initiation factor activity is the core function.",
                "ACCEPT",
                "UniProt/HAMAP identifies IF-1 as an essential initiation factor.",
                gene,
                term_id,
            ),
            "GO:0005737": review(
                "Cytoplasm is appropriate for IF-1.",
                "ACCEPT",
                "UniProt places IF-1 in the cytoplasm.",
                gene,
                term_id,
            ),
            "GO:0005829": review(
                "Cytosol is acceptable cytoplasmic location context.",
                "ACCEPT",
                "The TreeGrafter location row supports cytosol.",
                gene,
                term_id,
            ),
            "GO:0006413": review(
                "Translational initiation is the correct process.",
                "ACCEPT",
                "IF-1 participates in bacterial 30S and 70S initiation-complex formation.",
                gene,
                term_id,
            ),
            "GO:0019843": review(
                "rRNA binding is valid mechanistic context but not the core function.",
                "KEEP_AS_NON_CORE",
                "The core role is translation initiation factor activity.",
                gene,
                term_id,
            ),
            "GO:0043022": review(
                "Ribosome binding is supported for IF-1.",
                "ACCEPT",
                "UniProt describes IF-1 action on the 30S pre-initiation complex and mature 70S initiation complex.",
                gene,
                term_id,
            ),
        },
        "smpB": {
            "GO:0003723": review(
                "RNA binding is the supported molecular function for SmpB.",
                "ACCEPT",
                "SmpB binds tmRNA and stabilizes tmRNA association with stalled ribosomes.",
                gene,
                term_id,
            ),
            "GO:0005737": review(
                "Cytoplasm is appropriate for SmpB.",
                "ACCEPT",
                "UniProt places SmpB in the cytoplasm.",
                gene,
                term_id,
            ),
            "GO:0005829": review(
                "Cytosol is acceptable cytoplasmic context.",
                "ACCEPT",
                "The TreeGrafter location row supports cytosol.",
                gene,
                term_id,
            ),
            "GO:0070929": review(
                "Trans-translation is the core process for SmpB.",
                "ACCEPT",
                "UniProt/HAMAP describes SmpB as required for tmRNA-mediated stalled-ribosome rescue.",
                gene,
                term_id,
            ),
            "GO:0070930": review(
                "Trans-translation-dependent protein tagging is appropriate for SmpB.",
                "ACCEPT",
                "The SmpB-tmRNA system appends a tag peptide to incomplete nascent proteins for degradation.",
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
            refs.append({"id": ref_id, "title": title, "findings": []})
            seen.add(ref_id)
    return refs


def core_function(gene: str) -> dict:
    spec = CORE[gene]
    out = {
        "description": spec["description"],
        "molecular_function": term(spec["molecular_function"]),
        "supported_by": evidence_for(gene, spec["molecular_function"]),
    }
    if spec.get("directly_involved_in"):
        out["directly_involved_in"] = [term(x) for x in spec["directly_involved_in"]]
    if spec.get("locations"):
        out["locations"] = [term(x) for x in spec["locations"]]
    return out


def suggested_question(gene: str) -> list[dict[str, str]]:
    if gene in {"hslR", "ychF", "ettA", "lepA"}:
        return [{"question": f"What P. putida KT2440 stress or nutrient conditions most strongly require {gene} for translation fitness?"}]
    if gene in {"pth", "arfB", "smpB"}:
        return [{"question": f"What stalled-ribosome substrates or rescue pathway dependencies are most important for {gene} in KT2440?"}]
    return [{"question": f"Are there P. putida-specific regulatory or growth-condition dependencies for {gene} beyond the conserved bacterial translation role?"}]


def suggested_experiment(gene: str) -> list[dict[str, str]]:
    return [
        {
            "description": f"Compare wild-type and {gene} perturbation strains under translation stress, heat stress, and nutrient limitation using ribosome profiling and growth-rescue assays.",
            "experiment_type": "ribosome profiling and stress-fitness assay",
        }
    ]


def curate_gene(gene: str) -> None:
    path = gene_file(gene, "ai-review.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["status"] = "DRAFT"
    data["description"] = DESCRIPTIONS[gene]
    for ann in data["existing_annotations"]:
        go_id = ann["term"]["id"]
        ann["review"] = review_for(gene, go_id)
    data["references"] = references_for(gene, data)
    data["core_functions"] = [core_function(gene)]
    data["proposed_new_terms"] = []
    data["suggested_questions"] = suggested_question(gene)
    data["suggested_experiments"] = suggested_experiment(gene)
    path.write_text(
        yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=120),
        encoding="utf-8",
    )

    notes = [
        f"# {gene} translation factor / ribosome rescue first-pass notes",
        "",
        f"- First-pass curation date: 2026-07-10.",
        f"- Batch: `{BATCH_TSV}`.",
        f"- Asta retrieval report: `{file_id(gene, 'deep-research-asta.md')}`. The report is retained as provenance; annotation decisions are supported by the local UniProt and GOA rows.",
        f"- Main conclusion: {CORE[gene]['description']}",
    ]
    path_notes = gene_file(gene, "notes.md")
    path_notes.write_text("\n".join(notes) + "\n", encoding="utf-8")


def annoton(gene: str, label: str, function_id: str, processes: list[str] | None = None, locations: list[str] | None = None) -> dict:
    out = {
        "id": f"{gene}_{label.lower().replace(' ', '_').replace('/', '_')}",
        "label": f"{gene}: {label}",
        "participant": {"selector_type": "GENE", "gene": {"preferred_term": gene}},
        "function": {"preferred_term": TERM[function_id]["label"], "term": term(function_id)},
        "role_description": CORE[gene]["description"],
    }
    if processes:
        out["processes"] = [{"preferred_term": TERM[x]["label"], "term": term(x)} for x in processes]
    if locations:
        out["locations"] = [{"preferred_term": TERM[x]["label"], "term": term(x)} for x in locations]
    return out


def write_module() -> None:
    module = {
        "id": "MODULE:translation_factor_ribosome_rescue_boundary",
        "title": "Translation factor and ribosome rescue boundary",
        "description": (
            "Boundary module for PSEPK genes in the translation/RNA-processing bucket that encode bacterial "
            "translation initiation, elongation, recycling, throttling, and stalled-ribosome rescue factors rather "
            "than structural ribosomal proteins or RNA-modification enzymes."
        ),
        "status": "DRAFT",
        "evidence": [
            {
                "source_id": f"file:{BATCH_TSV}",
                "title": "PSEPK translation/RNA translation-factor and ribosome-rescue split",
                "statement": "The batch records hslR, selB, ettA, ychF, pth, lepA, frr, arfB, infA, and smpB as translation-factor, ribosome-rescue, or ribosome-associated regulatory genes.",
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
            "id": "translation_factor_ribosome_rescue_boundary",
            "label": "Translation factor and ribosome rescue boundary",
            "module_type": "BIOLOGICAL_PROCESS",
            "concepts": [
                {"preferred_term": TERM[x]["label"], "term": term(x)}
                for x in [
                    "GO:0003743",
                    "GO:0003746",
                    "GO:0016887",
                    "GO:0004045",
                    "GO:0043023",
                    "GO:0070929",
                    "GO:0072344",
                ]
            ],
            "parts": [
                {
                    "order": 1,
                    "role": "Translation initiation, elongation, and throttle factors",
                    "node": {
                        "id": "translation_initiation_elongation_throttle_factors",
                        "label": "Translation initiation, elongation, and throttle factors",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "IF-1, SelB, EF-4/LepA, and EttA represent initiation, specialized elongation, back-translocation, and energy-dependent elongation-throttle context.",
                        "annotons": [
                            annoton("infA", "translation initiation factor", "GO:0003743", ["GO:0006413"], ["GO:0005737"]),
                            annoton("selB", "selenocysteine elongation factor", "GO:0003746", ["GO:0001514", "GO:0006414"], ["GO:0005737"]),
                            annoton("lepA", "EF-4 ribosomal back-translocase", "GO:0003746", ["GO:0006414"], ["GO:0005886"]),
                            annoton("ettA", "ATP-dependent translational throttle", "GO:0016887", ["GO:0045900"], ["GO:0005737"]),
                        ],
                    },
                },
                {
                    "order": 2,
                    "role": "Ribosome recycling, trans-translation, and stalled-ribosome rescue",
                    "node": {
                        "id": "ribosome_recycling_trans_translation_rescue",
                        "label": "Ribosome recycling, trans-translation, and stalled-ribosome rescue",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "Frr, Pth, ArfB, and SmpB support post-termination ribosome recycling, peptidyl-tRNA hydrolysis, and tmRNA-dependent rescue.",
                        "annotons": [
                            annoton("frr", "ribosome recycling factor", "GO:0043023", ["GO:0002184", "GO:0006415"], ["GO:0005737"]),
                            annoton("pth", "peptidyl-tRNA hydrolase", "GO:0004045", ["GO:0072344"], ["GO:0005737"]),
                            annoton("arfB", "alternative rescue peptidyl-tRNA hydrolase", "GO:0004045", ["GO:0072344"], ["GO:0005737"]),
                            annoton("smpB", "tmRNA-binding trans-translation factor", "GO:0003723", ["GO:0070929", "GO:0070930"], ["GO:0005737"]),
                        ],
                    },
                },
                {
                    "order": 3,
                    "role": "Ribosome-associated stress proteins and NTPases",
                    "node": {
                        "id": "ribosome_associated_stress_ntpases",
                        "label": "Ribosome-associated stress proteins and NTPases",
                        "module_type": "BIOLOGICAL_PROCESS",
                        "description": "HslR/Hsp15 and YchF are ribosome-associated stress or NTPase side nodes in the translation bucket.",
                        "annotons": [
                            annoton("hslR", "ribosomal large-subunit heat-shock protein", "GO:0043023", ["GO:0034605"]),
                            annoton("ychF", "ribosome-associated ATPase", "GO:0016887", None, ["GO:0005737"]),
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
