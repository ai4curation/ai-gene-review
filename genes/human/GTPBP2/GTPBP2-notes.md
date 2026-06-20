# GTPBP2 — research notes

UniProt: Q9BX10. TRAFAC-class translation-factor GTPase, related to eEF1A/eRF3/Hbs1/GTPBP1.

## Core function
GTPBP2 is a translational GTPase that **partners PELO in ribosome rescue**, particularly important
in neurons. The mouse Gtpbp2 / Pelo axis rescues ribosomes stalled at deficient tRNA; loss (with
the n-Tr20 tRNA mutation in the *nmf205* mouse) causes ribosome stalling and neurodegeneration
(Ishimura et al. 2014, Science). In humans, GTPBP2 loss-of-function causes Jaberi-Elahi syndrome
(neurodegeneration with developmental delay, cerebellar atrophy).

- [file:human/GTPBP2/GTPBP2-uniprot.txt "Involved in the rescue of ribosome stalling due to the presence of non-functional tRNA"]
- [file:human/GTPBP2/GTPBP2-uniprot.txt "Interacts with PELO"]
- [file:human/GTPBP2/GTPBP2-uniprot.txt "Has very low GTP-binding activity"]

## Distinct from GTPBP1 (PMID:30108131)
Unlike GTPBP1, GTPBP2 **lacks eEF1A-like elongation activity** and did not stimulate exosomal
degradation; its GTP binding is weak though stimulated by Phe-tRNA.
- [PMID:30108131 "GTPBP2 lacked elongation activity and did not stimulate exosomal degradation, indicating that GTPBP1 and GTPBP2 have"]
- The GOA has a NEGATED IDA annotation GO:0003746 translation elongation factor activity (PMID:30108131) — correct: GTPBP2 does NOT have elongation factor activity.

## Annotations
- IDA (PMID:30108131): negated translation elongation factor activity (correct negation); GTP binding (weak); alpha-aminoacyl-tRNA binding (Phe-tRNA stimulates GTP binding).
- IPI: PMID:23455924 (PRMT interactome Y2H), PMID:32296183 — protein binding / identical protein binding (GTPBP2 self / GTPBP2 homodimer). Keep non-core.
- Reactome platelet alpha granule / extracellular region (R-HSA-481007) — platelet-proteomics localization, non-core.

## Action plan
- Core MF: GO:0005525 GTP binding (weak); the rescue role best as BP GO:0072344 (not currently in GOA — could propose, but stick to existing). Existing has translational elongation IBA — but GTPBP2 lacks elongation activity, so MARK as over-annotated / note negation.
- Negated GO:0003746: ACCEPT (the negation is correct and informative).
