# C. albicans ERG10 review notes

## 2026-11-23 review

- Reviewed the new CGD-derived C. albicans ERG10 stub against the local UniProt
  flat file, the PTHR18919 PAINT snapshot, the cached PMID:14653518 abstract,
  the newly cached Lin et al. 2022 paper, and the A. fumigatus erg10A/erg10B
  paralog split in the same family.
- PMID:14653518 is abstract-only. The abstract confirms that Song et al. assayed
  expression of the Candida sterol and prenylation pathways under lovastatin
  and fluconazole, but it names only HMG1, ERG20, ERG9, ERG11, RAM1, RAM2, and
  CDC43; it does not directly identify an ERG10 assay.
- PMID:35551233 directly revisited C. albicans ERG10 as the target of bacterial
  polyynes. Lin et al. report that "ERG10 is the first enzyme of the ergosterol
  biosynthesis pathway" and that ERG10 overexpression rescued viability under
  several bacterial polyyne treatments. That is C. albicans-specific support for
  replacing the biological-process no-data row with ergosterol biosynthesis.
- Literature searches for `"Candida albicans" ERG10 acetoacetyl-CoA
  acetyltransferase`, `A0A1D8PH52`, `orf19.1595`, and `CAALFM_CR06080CA` found
  no C. albicans ERG10 microscopy, fractionation, or tagged-protein
  localization study. The CGD cellular-component no-data row therefore remains
  current even though UniProt places the enzyme in the cytosol by similarity to
  Saccharomyces cerevisiae Erg10.
- Searches in the 2024-2026 window found Candida ergosterol-stress studies that
  mention ERG10 as a mevalonate-pathway gene but no newer direct ERG10
  enzymology or localization paper beyond Lin et al. 2022.
