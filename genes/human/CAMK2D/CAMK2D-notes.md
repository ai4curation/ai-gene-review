# CAMK2D review notes

## Literature search (manual; no deep-research provider available)

Sources checked, 2026-11-04:

- UniProt Q13557 record (`CAMK2D-uniprot.txt`): FUNCTION, ACTIVITY REGULATION, SUBUNIT,
  SUBCELLULAR LOCATION, TISSUE SPECIFICITY, PTM.
- All GOA publications cached with `just fetch-gene-pmids human CAMK2D` (23 papers); most
  cardiac papers are abstract-only in the cache.
- Additional papers fetched: PMID:14722083 (isoform comparison), PMID:16690701 (skeletal muscle
  exercise), PMID:11972023 (CaMKII gamma/delta and STAT1 Ser727).
- Context only: the `genes/human/CAMK2A` and `genes/human/CAMK2B` reviews, and the STAT1 module
  and GO-CAM review proposed in ai4curation/ai-gene-review#5904 (not used as evidence here).

## Findings

### Catalysis, structure and holoenzyme
- CaMKII delta is a Ca2+/calmodulin-activated Ser/Thr kinase; the CaMKIIdelta/Ca2+/CaM crystal
  structure shows how CaM binding releases the regulatory segment and how Thr287 is presented to
  a neighbouring kinase domain [PMID:20668654 "Transphosphorylation of T287 (T286 in CaMKIIα) by a
  catalytic domain present in the same holoenzyme has been described as the molecular switch that
  leads to constitutive and Ca2+/CaM-independent CaMKII activity"].
- All four isoforms are dodecamers [PMID:14722083 "all four isoforms were dodecamers with similar
  but highly unusual architecture"]. Delta is the predominant cardiac CaMKII
  [PMID:12676813 "Ca2+/calmodulin-dependent protein kinase II (CaMKII) delta is the predominant
  cardiac isoform, and the deltaC splice variant is cytoplasmic"].

### Cardiac excitation-contraction coupling
- deltaC phosphorylates RyR2 and phospholamban in vivo [PMID:12676814 "These findings are the
  first to demonstrate that CaMKIIdeltaC can mediate phosphorylation of Ca2+ regulatory proteins
  in vivo"]; overexpression increases SR Ca2+ leak/sparks and reduces SR load
  [PMID:12676813 "Acute CaMKII inhibition normalized Ca2+ spark frequency and ICa, consistent with
  direct CaMKII activation of ryanodine receptors (and ICa) in TG"].
- deltaC binds and phosphorylates Nav1.5 at Ser516/Thr594, shifting gating toward loss of
  function [PMID:22514276 "A stable interaction between δ(C)-CaMKII and the intracellular loop
  between domains 1 and 2 of Na(V)1.5 was observed"].
- beta-IV-spectrin targets CaMKII to excitable membranes and Nav channels (mouse)
  [PMID:20877009 "we identified a regulatory mechanism for Na(+) channels, via direct
  phosphorylation by β(IV)-spectrin-targeted calcium/calmodulin-dependent kinase II (CaMKII)"].
- CaMKII phosphorylates titin PEVK and N2B elements and lowers passive force; delta/gamma DKO and
  deltaC transgenic hearts were used [PMID:23283722 "CaMKII phosphorylates the titin springs at
  conserved serines/threonines, thereby lowering F(passive)"].

### Nuclear deltaB and hypertrophy
- deltaB is nuclear and phosphorylates HDAC4 Ser210, derepressing MEF2; knockdown blunts
  hypertrophic responses [PMID:17179159 "RNA interference knockdown of CaMKIIdeltaB prevents the
  effects of hypertrophic stimuli"].

### Over-reaching rows
- Electrical-coupling and heart-rate-by-conduction rows (IC/ISS) extrapolate from Nav1.5 gating
  and AP prolongation; no gap-junction or conduction data for CAMK2D were found.
- "regulation of cell growth" (NAS, PMID:9060999) rests on a speculative sentence in a variant
  cloning paper.
- LTP rows are an alpha/beta neuronal property; no delta-specific LTP evidence was found.

### STAT1 (module context)
- PMID:11972023 identifies the ubiquitous gamma/delta isoforms as the STAT1 TAD-interacting
  kinases [PMID:11972023 "These results indicate that there is a specific interaction between
  Stat1 and the ubiquitous members of the CaMKII family, i.e., CaMKIIγ/δ."]. The antibodies and
  purification did not separate gamma from delta, so no delta-specific NEW annotation is
  proposed; recorded as a suggested question.

## Revision after PR review (ai4curation/ai-gene-review#5945)

- Added a second core function for the nuclear deltaB branch: deltaB phosphorylates HDAC4 Ser210
  and promotes its nuclear export, relieving MEF2 repression in cardiomyocytes [PMID:17179159
  "These results demonstrate that CaMKIIdeltaB preferentially targets HDAC4, and this involves
  serine 210."]. Process term is GO:0046827 positive regulation of protein export from nucleus,
  the MODIFY replacement for the GO:0060341 row; location nucleus.
