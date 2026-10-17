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
  reasonable orthology transfer from budding yeast: Ytm1 is the Rea1-recognized
  MIDO/UBL ligand required for ATP-dependent release of the Ytm1-Erb1-Nop7
  subcomplex [PMID:20542003].
- I marked the EnsemblFungi `GO:0051276 chromosome organization` row
  over-annotated because it derives from a budding-yeast dosage phenotype, not
  from conserved Ytm1 execution of chromosome organization.
