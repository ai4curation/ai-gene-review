# PA0011 (HtrB1, Q9I7B5) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I7B5 --alias PA0011`; accession matches the worklist. No
deep-research provider used. PMID:26223882 and PMID:22146126 are abstract-only.

### Literature

- [PMID:26223882 "In this study, we were able to show that each gene identified is responsible for site-specific modification of lipid A."]
- [PMID:22146126 "We found that the PA0011 mutant strain was susceptible to several different antibiotics and environmental stresses."]
  Basis of the heat, antibiotic and osmotic stress IMP rows: an indirect envelope phenotype.

### Annotation decisions

- ACCEPT: GO:0016747 (IDA), GO:0009245 (IDA), GO:0005886 (IEA).
- TOO_GENERAL: GO:0016746 (IBA, IEA), GO:0016740, GO:0009247 (IBA, IEA), GO:0016020 (IBA, IEA).
- MARK_AS_OVER_ANNOTATED: GO:0034605, GO:0071236, GO:0071470 (IMP).
- Action counts: ACCEPT 3, TOO_GENERAL 7, MARK_AS_OVER_ANNOTATED 3. No source defects.

## PseudoCAP IBA-seed assessment

Shares PTN004745460 with lpxL (PA3242); verdicts kept consistent, see lpxL notes. No node-level defect.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004745460 | GO:0016746 acyltransferase activity | 6 | 36 (22 taxa) | GO:0016747, IDA, PMID:26223882 (PseudoCAP) | SOUND | Abstract states HtrB1 is responsible for site-specific lipid A acylation. Assay type not checked (abstract only). | E. coli LpxL P0ACV0, LpxM P24205, LpxP P0ACV2, M. tuberculosis PatA P9WMB5, lpxL Q9HYZ8 | Yes |
| PTN004745460 | GO:0009247 glycolipid biosynthetic process | 6 | 23 (21 taxa) | GO:0009245, IDA, PMID:26223882 (PseudoCAP) | SOUND | Lipid A is a glycolipid. | as above | Yes |
