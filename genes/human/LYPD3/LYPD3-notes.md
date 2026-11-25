# LYPD3 (C4.4A) curation notes

Deep research (`just deep-research-falcon human LYPD3 --fallback perplexity-lite`) failed in this
environment (falcon/perplexity providers unavailable), so these notes are from direct reading of
the UniProt record (O95274) and cached publications.

## Identity and topology
- LYPD3 = C4.4A, a uPAR (PLAUR) homologue with two Ly6/uPAR (LU) domains, a C-terminal Ser/Thr/Pro-rich
  O-glycosylated region, signal peptide 1-30, and a C-terminal propeptide (327-346) replaced by a
  GPI anchor at Cys326 (UniProt FT, ECO:0000255). UniProt: "Cell membrane; Lipid-anchor, GPI-anchor."
- [PMID:11179665 "both molecules have a glycolipid anchor site"]
- [PMID:15012588 "By immunohistochemistry we observed a pronounced surface staining for C4.4A in suprabasal keratinocytes of chronic human wounds"]
- [PMID:15012588 "MCF 7 cells, which express significant amounts of GPI-anchored C4.4A"]; no uPA binding,
  so not a functional uPAR paralog.
- Soluble/shed forms: GPLD1 hydrolysis (Reactome R-HSA-8940388); detected in colostrum proteomics
  (PMID:16502470). Shedding of GPI-anchored ectodomain explains extracellular region annotations.

## Localization conclusion
Plasma membrane, outer leaflet (GPI-anchored), with entire mature polypeptide (both LU domains and the
mucin-like stalk) extracellular and accessible at the cell surface. Also released into the
extracellular space by GPI-anchor cleavage.

## Function
- Partners: AGR2 and AGR3 (yeast two-hybrid; PMID:12592373) and AGR2 by ERMIT in ER (PMID:31040128),
  LGALS3 and laminin-1/-5 by similarity to rat C4.4A (UniProt ECO:0000250). Laminin binding is from rat;
  no human primary paper cached.
- Phenotypes: supports keratinocyte migration during wound re-epithelialization (expression
  correlate, PMID:15012588), cancer progression/metastasis marker; miRNA-target studies (PMID:32151690,
  VSMC apoptosis) are indirect.
- No catalytic activity; molecular function essentially unknown beyond adhesion-related binding.
