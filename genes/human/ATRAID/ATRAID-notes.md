# ATRAID notes

## 2026-10-05 review (PAINT, affinage)

- Lysosomal ATRAID-SLC37A3 complex [PMID:29745899 "SLC37A3 and ATRAID localize to lysosomes and are required for releasing N-BP molecules that have trafficked to lysosomes through fluid-phase endocytosis into the cytosol."]; [PMID:29745899 "Additionally, consistent with the observation that ATRAID is required for the stable expression of SLC37A3, ATRAIDKO cells phenocopied SLC37A3KO cells in these uptake assays."].
- Xenobiotic transporter activity (IDA and IEA) is marked over-annotated in its 'enables' form. ATRAID is the stabilizing partner, and the paper does not show it translocating; core_functions uses contributes_to. Xenobiotic transport (BP) and lysosomal membrane are accepted.
- The NELL-1/osteoblast rows (PMID:21723284, Saos2 overexpression) and the nuclear envelope, perinuclear and plasma membrane rows are kept as non-core. Regulation of gene expression is over-annotated. Negative regulation of protein catabolic process is UNDECIDED: the cached full text only speculates about Runx2 stabilization.
- Three IPIs (SNX9, NELL1, SLC37A3; four GOA rows, as the stub collapses duplicates) removed under policy.

## 2026-10-05 revision (reviewer round 1)

- Plasma membrane rows (EXP, IEA) are now over-annotated. PMID:29745899 shows both ATRAID isoforms on lysosomes but not on the plasma membrane at near-endogenous expression, and attributes the surface signal to overexpression.
- The GO:0042910 reason now states that ATRAID and SLC37A3 are mutually dependent for stability and that SLC37A3 is epistatic to ATRAID.
- The perinuclear row has its own quote (NELL-1-EGFP perinuclear condensation with APR3).
- The IBA propagation_review now lists Q6UW56 as a source. The UNDECIDED reason now names the missing supplementary data. There is no GO CC term for the SLC37A3-ATRAID complex, so no in_complex is given.
