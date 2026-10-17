# YTM1 notes

## 2026-10-17

- Deep research did not complete: the Falcon wrapper fell back to the lightweight
  provider but the fresh provider environment had no `agentapi` credentials on
  `PATH`. I therefore used cached primary literature and manual PubMed follow-up.
- Candida YTM1 is a `PTHR19855:SF11` fungal WDR12/Ytm1 member. The PAINT IBA
  rows for large-subunit preribosome, PeBoW complex, and ribosomal large
  subunit biogenesis all trace to `PANTHER:PTN000458086`, the right fungal
  ancestor.
- Budding-yeast Ytm1 provides the main mechanistic anchor: "Ytm1 binds directly
  to Erb1 and is present in a heterotrimeric subcomplex together with Erb1 and
  Nop7, both within preribosomes and independently of preribosomes"
  [PMID:16287855], and the S. pombe ortholog is found in the state-3 nascent
  60S complex where "the biogenesis complex Ytm1-Erb1-Ppp1 (Ytm1-Erb1-Nop7 in
  S. cerevisiae) is incorporated" [PMID:36423630].
- The Rea1/Mdn1-remodeling row from EnsemblFungi is plausible because Ytm1 is
  the conserved MIDAS ligand whose interaction is needed for ATP-dependent
  subcomplex release: "Rea1 induces the release of the Ytm1-Erb1-Nop7
  subcomplex from the nascent 60S subunit and consequently enables this early
  pre-60S intermediate to exit from the nucleolus" [PMID:20542003].
- The direct CGD filamentation rows come from the Uhl et al. haploinsufficiency
  screen, which used "haploinsufficiency and transposon mutagenesis to perform
  large-scale loss-of-function genetic screen in this organism" [PMID:12773383].
  I kept the Spider-medium and serum-induced descendants as non-core Candida
  perturbation phenotypes and marked their shared `GO:0030447 filamentous
  growth` ancestor for replacement by those more specific terms.
- I marked the EnsemblFungi `GO:0051276 chromosome organization` row
  over-annotated because it derives from a budding-yeast dosage phenotype, not
  from conserved Ytm1 execution of chromosome organization.
