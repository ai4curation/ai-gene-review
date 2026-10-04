# ANAPC13 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- APC13/Swm1 is a small core APC/C subunit [PMID:15060174 "Swm1/Apc13 promotes the stable association with the APC/C of the essential subunits Cdc16 and Cdc27."]. It is needed for full ligase activity, and human APC13 complements yeast swm1Δ (same paper).
- **Meiosis:** biallelic ANAPC13 mutations (p.D2E, p.L24R) arrest human oocytes at metaphase I, and a knock-in mouse reproduces the arrest (PMID:41997520, 2026). On this basis the NAS "regulation of meiotic cell cycle" row is accepted rather than kept as non-core.
- **GOA rows (23):**
  - All APC/C complex, catabolism, chain-type and cell-cycle regulation rows are accepted.
  - The 7 protein-binding IPIs are removed: 6 are proteome-scale CDC23 hits, already captured by the APC/C complex rows, and 1 is a WFS1 hit from a disease interactome.
- **Not used from affinage:** the SF3B1-K700E/Treg paper (PMID:39303038). It concerns ANAPC13 expression levels, not ANAPC13 function.

## 2026-10-04 round 2 (reviewer comments on #4056)

- **Arc Lamp/TPR-lobe framing:** now cited to PMID:25490258.
- **Nucleus row: ACCEPT changed to KEEP_AS_NON_CORE.** UniProt's basis is ECO:0000305. Yeast Swm1p is nuclear (PMID:10022899), but PMID:40238067 found overexpressed wild-type human APC13 "primarily found in the cytoplasm" in HEK293T cells. OpenCell (PMID:35271311) has no ANAPC13-specific localization sentence in the cached text.
- **Meiosis:** added PMID:40238067 as a second infertility cohort. (Corrected in round 3: this family is compound heterozygous for p.D2E and an independent frameshift, p.P39QfsTer25. So p.D2E recurs independently, which strengthens the case.)
- **Other fixes:**
  - The CDC23 REMOVE reasons no longer cite yeast.
  - The affinage reference_review now accounts for every affinage citation; the yeast sporulation and cell-wall roles are explicitly not propagated.
  - Added a question on an adaptor/scaffold MF for TPR-lobe subunits.
  - Fixed a typo.

## 2026-10-04 round 3 (reviewer comments on #4056)

- **Correction:** I had said PMID:40238067 adds "a second family, not an independent allele". In fact its case 3 is compound heterozygous for p.D2E and p.P39QfsTer25. The frameshift is absent from PMID:41997520, the two papers come from unrelated groups, and PMID:40238067 is the earlier report. The meiosis row now quotes the case-3 sentence directly.
- **Nucleus caveat:** the reason now spells out that the cytoplasmic wild-type result is an overexpression readout; the same assay scores the mutant as nuclear.
- **References:** PMID:10022899 raised to MEDIUM relevance, since it is the sole positive citation on the retained nucleus row.
