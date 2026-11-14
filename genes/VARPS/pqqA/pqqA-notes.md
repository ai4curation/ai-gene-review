# Curation Notes for *Variovorax paradoxus* S110 `pqqA` (`C5CPT7`, `PQQA_VARPS`, `Vapar_3057`)

## Overview
- **UniProt Accession:** `C5CPT7` (`PQQA_VARPS`, reviewed Swiss-Prot)
- **Ordered Locus Name:** `Vapar_3057`
- **Gene Symbol:** `pqqA`
- **Organism:** *Variovorax paradoxus* S110 (`NCBITaxon:543728`; [PMID:21183664 Complete genome sequence of the metabolically versatile plant growth-promoting endophyte Variovorax paradoxus S110., "The complete genome sequence of V. paradoxus S110 is composed of 6,754,997 bp with 6,279 predicted protein-coding sequences within two circular chromosomes."])
- **Protein Function:** 24-amino-acid ribosomally synthesized precursor peptide (`MKWETPTATDLRFGFEITMYVSAR`, `HAMAP-Rule:MF_00656`, `InterPro:IPR011725`, `NCBIfam:TIGR02107`) that provides the conserved `Glu16` and `Tyr20` residues (`FT CROSSLNK 16..20`) from which the redox cofactor pyrroloquinoline quinone (PQQ) is constructed (`UniProtKB:C5CPT7`).

## Biochemical Role in the `pqqABCDE` RiPP Pathway
- PQQ is a ribosomally synthesized and post-translationally modified peptide (RiPP) cofactor ([PMID:25817994 PqqD is a novel peptide chaperone that forms a ternary complex with the radical S-adenosylmethionine protein PqqE in the pyrroloquinoline quinone biosynthetic pathway., "Pyrroloquinoline quinone (PQQ) is a product of a ribosomally synthesized and post-translationally modified pathway consisting of five conserved genes, pqqA-E."]).
- PqqA is not a catalytic enzyme; instead, it is the polypeptide substrate whose N-terminal leader region is bound with nanomolar affinity by the peptide chaperone PqqD (`Kd ~ 200 nM`), positioning the conserved core motif `E-I-T-M-Y` (`Glu16` and `Tyr20` in `C5CPT7`) in the active site of the radical SAM enzyme PqqE ([PMID:32731194 Biogenesis of the peptide-derived redox cofactor pyrroloquinoline quinone., "The pqqA is translated into a short peptide that contains the fully conserved residues, glutamate and tyrosine; site-direct mutagenesis identified these two residues on PqqA as the best candidate for the precursor to PQQ (Figure 2A).[31]"]).
- Pathway context is modeled in [`MODULE:pqq_biosynthesis`](../../../modules/pqq_biosynthesis.yaml).

## Review of Existing GOA Annotations
- `GO:0018189` (`pyrroloquinoline quinone biosynthetic process`, IEA via `UniProtKB-UniRule:UR000098299`) -> **ACCEPT** (core biological process; PqqA is the obligate precursor peptide of PQQ biogenesis).

## New Annotations Added
- `GO:0005829` (`cytosol`, `IC`, `located_in`) — PqqA is translated on cytosolic ribosomes as a 24-aa leaderless peptide and modified intracellularly by cytosolic PqqD/PqqE.
