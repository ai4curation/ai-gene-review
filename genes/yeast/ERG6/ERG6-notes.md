# ERG6 notes (P25087, YML008C)

- Function: SAM:Delta24-sterol C-methyltransferase, zymosterol -> fecosterol, EC 2.1.1.41 [UniProt:P25087]; [PMID:6363386 "Various nystatin-resistant mutants defective in S-adenosylmethionine: delta 24-sterol-C-methyltransferase (EC 2.1.1.41) were shown to possess alleles of the same gene, erg6."].
- Recombinant enzyme / AdoMet site: [PMID:18563465 "The results indicate that one or both of Cys128 and Pro133 are covalently bound to AdoMet."].
- Genetics: erg6 null viable, no C-24 methylation [PMID:2677674 "Although erg6 delta cells are unable to methylate ergosterol precursors at C-24, they exhibit normal vegatative growth"]; pleiotropic membrane phenotypes.
- Location: mainly lipid droplets [PMID:9450962 "sterol Delta24-methyltransferase (Erg6p), an enzyme catalyzing a late step in sterol biosynthesis, was found mainly in lipid particles"]; active in LD preps [PMID:10515935 "This is very likely for Erg6p ( 27 ) and Erg7p ( 4a ), which are enzymatically active in lipid particle preparations."]; LD marker in [PMID:24868093 "Sec61 and Erg6 are negative and positive controls, respectively."]; ER pool enriched in PAM [PMID:11298754].
- Mitochondrial signal: activity found in mito fraction but [PMID:6363386 "The amount of activity in each fraction could be manipulated by assay conditions."]; mito proteomics hits treated as contact-site co-purification -> MARK_AS_OVER_ANNOTATED.
- UniProt SubCell lacks lipid droplet (lists Microsome + Mitochondrion only).
- Self-interaction by split-ubiquitin, Y2H, DHFR-PCA -> identical protein binding KEEP_AS_NON_CORE.
- Decisions: 20 ACCEPT, 7 MODIFY, 6 MARK_AS_OVER_ANNOTATED, 3 KEEP_AS_NON_CORE.
- 2026-11-06 PTHR44068 re-review: refreshed UniProt from entry version 212
  to 213; the only visible drift was interaction/xref metadata (BioGRID count,
  MINT, and OMA). Re-checked the PTN002226525 sterol-SMT and PTN000802684
  fungal Erg6 PAINT nodes against the `PTHR44068` family review; the
  Saccharomyces IBAs for sterol 24-C-methyltransferase activity, ER location,
  and ergosterol biosynthesis remain sound. Web and PubMed searches found a
  2025 sterol-intermediate paper using an `erg6Delta` strain, where
  "expected sterol intermediates were the most abundant sterol in erg6" as
  expected [PMID:40267201], but this biophysical phase-separation study does not
  supersede the direct activity, pathway or lipid-droplet/ER localization
  evidence already cited here.
