# DUSP18 review notes

Automated Falcon and Perplexity deep-research providers were unavailable in this
environment, so no provider-named deep-research file was created. These notes
were compiled manually from the GOA rows, cached publications, the UniProt
record, and the 68d5ebd600001504 GO-CAM review.

## Core activity

- DUSP18 was cloned independently as LMW-DSP20 and as DUSP18. The two early
  abstract-only papers both support direct dual-specificity phosphatase
  activity in vitro: Hood et al. reported pNPP dephosphorylation and synthetic
  MAPK phosphopeptide dephosphorylation [PMID:12408986 "Both proteins are able
  to dephosphorylate the phosphotyrosine analog pNPP in vitro"], while Wu et
  al. reported purified GST-DUSP18 activity on pNPP and pThr/pTyr
  oligopeptides [PMID:12591617 "GST-DUSP18 fusion protein showed distinctive
  phosphatase activity toward p-nitrophenyl phosphate (pNPP), as well as
  oligopeptides containing pThr and pTyr"].
- Hood et al. is enough for pTyr and pThr activity but argues against MAPKs as
  physiological substrates under their conditions [PMID:12408986 "the novel
  DSPs exhibited no detectable in vivo activity against MAPKs under our
  conditions"], so the InterPro2GO MAPK phosphatase row is over-specific.
- Jeong et al. is abstract-only in the local cache. The GOA rows from that paper
  to generic dephosphorylation and phosphatase activity are kept as
  TOO_GENERAL, because the accepted dual-specificity activity and
  peptidyl-tyrosine/peptidyl-threonine dephosphorylation rows establish that
  both broad claims are true but imprecise.

## KISS1R/SRC GO-CAM context

- The KISS1/KISS1R osteoclast GO-CAM uses human DUSP18 as a protein tyrosine
  phosphatase that directly negatively regulates SRC. That is consistent with
  this gene review: GO:0004725 is an accepted activity, the direct human
  DUSP18/SRC biochemical evidence supports the new GO:0044387 negative
  regulation of protein kinase activity row, and Dusp18 loss in mice supports
  negative regulation of bone resorption [PMID:38346942 "Dusp18 knockout mice
  all exhibit osteoclast hyperactivation and bone loss"].
- The 2024 study assayed purified human DUSP18 and the C104S catalytic mutant
  against human SRC, using the paper's Src Tyr416 numbering for the activating
  site that corresponds to human SRC Tyr419, so the phosphatase edge is
  biochemically direct [PMID:38346942 "Purified WT-DUSP18 potently reduced the
  phosphorylation of Src (Y416) purified from Sf9 insect cells in vitro, but the
  enzymatically dead DUSP18 (C104S) mutant had no activity"].

## Peripheral rows

- Nuclear and cytoplasmic location were retained from the original COS-cell
  transfection assay, but the nucleus was marked non-core because the direct Src
  dephosphorylation mechanism is receptor-proximal.
- Mitochondrial inner membrane rows were retained as non-core orthology-based
  annotations from mouse Dusp18.
- The INSR and JPH3 interaction rows are bare GO:0005515 protein-binding rows
  from large interactome screens and were removed under the repository
  protein-binding policy.
