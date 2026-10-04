# AKR1C8 (Q5T2L2) review notes

## 2026-10-03: PAINT/affinage review

AKR1C8 (formerly the pseudogene AKR1C8P, alias AKR1CL1) is an AKR1C-family aldo-keto reductase, 326 aa long. No human functional study exists. UniProt cites only cDNA and genome sequencing papers.

- **Affinage:** the trust gates clear, but its only functional evidence is from pig. Pig PGFS knockdown reduces PGF2alpha [PMID:25726376 "knock down porcine mPGES-1 and PGFS (also named as AKR1CL1 in GenBank)"]. The second pig paper (PMID:28673084) is a transcriptome screen and was not used.
- **Orthology:** Ensembl REST (homology/symbol/human/AKR1C8, target sus_scrofa) reports a one-to-one ortholog, ENSSSCG00000063387. Whether that gene is the pig PGFS cDNA that the 2014 knockdown study targeted is not established from the abstract, so the PGF synthase role is recorded as a gap and not transferred.
- **Catalytic tetrad:** conserved; see `AKR1C8-bioinformatics/RESULTS.md`. D53, Y58, K87 and H120 align to the AKR1C1 tetrad D50, Y55, K84 and H117, and identity to AKR1C1 is 68%.
- **Decisions:**
  - Generic oxidoreductase activity (InterPro): ACCEPT.
  - Cytoplasm: ACCEPT.
  - ARBA alcohol dehydrogenase (NADP+): KEEP_AS_NON_CORE.
  - ARBA androsterone dehydrogenase and the three ARBA process terms (steroid, monocarboxylic acid and hormone metabolism): MARK_AS_OVER_ANNOTATED. These are substrate claims inherited from rules, and AKR1C substrate preferences diverge between close paralogs.
  - Five protein-binding rows from the neurodegeneration Y2H screen: REMOVE, per policy.
