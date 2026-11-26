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
  are left undecided because the abstract reports a family-wide DUSP analysis
  but does not mention DUSP18.

## KISS1R/SRC GO-CAM context

- The KISS1/KISS1R osteoclast GO-CAM uses human DUSP18 as a protein tyrosine
  phosphatase that directly negatively regulates SRC. That is consistent with
  this gene review: GO:0004725 is an accepted activity, Dusp18 dephosphorylates
  Src Tyr416 in the 2024 mouse osteoclast paper [PMID:38346942 "GPR54
  activation by its natural ligand Kisspeptin-10 (Kp-10) causes Dusp18 to
  dephosphorylate Src at Tyr 416"], and Dusp18 loss in mice supports negative
  regulation of bone resorption [PMID:38346942 "Dusp18 knockout mice all
  exhibit osteoclast hyperactivation and bone loss"].
- The 2024 study assayed purified His-DUSP18 and the C104S catalytic mutant
  against His-Src, so the phosphatase edge is biochemically direct
  [PMID:38346942 "His-DUSP18 and His-DUSP18 (C104S) were incubated with His-Src
  in 1x phosphatase buffer"].

## Peripheral rows

- Nuclear and cytoplasmic location were retained from the original COS-cell
  transfection assay, but the nucleus was marked non-core because the direct Src
  dephosphorylation mechanism is receptor-proximal.
- Mitochondrial inner membrane rows were retained as non-core orthology-based
  annotations from mouse Dusp18.
- The INSR and JPH3 interaction rows are bare GO:0005515 protein-binding rows
  from large interactome screens and were removed under the repository
  protein-binding policy.
