# ytm1 notes

## 2026-10-17

- Deep research did not complete: the Falcon wrapper fell back to the lightweight
  provider but the fresh provider environment had no `agentapi` credentials on
  `PATH`. I therefore used cached primary literature and manual PubMed follow-up.
- Neurospora `ytm1` is in the same `PTHR19855:SF11` fungal WDR12/Ytm1 clade as
  budding-yeast YTM1, fission-yeast `ytm1`, and Candida YTM1. The three IBA
  rows should be reviewed against `PANTHER:PTN000458086`, not as pairwise
  SGD-to-Neurospora transfers.
- The SGD seed is well grounded. Ytm1 "binds directly to Erb1 and is present in
  a heterotrimeric subcomplex together with Erb1 and Nop7, both within
  preribosomes and independently of preribosomes" [PMID:16287855], and WD40
  mutants "delay pre-rRNA processing and nuclear export of preribosomes"
  [PMID:16287855].
- Independent fission-yeast structural work observes the orthologous complex in
  the nascent 60S pathway: "the biogenesis complex Ytm1-Erb1-Ppp1
  (Ytm1-Erb1-Nop7 in S. cerevisiae) is incorporated" [PMID:36423630].
- The EnsemblFungi `GO:0110136 protein-RNA complex remodeling` row is a
  reasonable orthology transfer: the Neurospora HAMAP record specifically
  predicts that the Ytm1 UBL domain interacts with rbg-35/mdn1 via the Mdn1
  VWFA/MIDAS domain, matching the conserved Rea1/Mdn1 release-handle mechanism
  seen in budding yeast [PMID:20542003].
- I marked the EnsemblFungi `GO:0051276 chromosome organization` row
  over-annotated because the conserved PTHR19855:SF11 function is pre-60S
  assembly, not direct execution of chromosome organization.
