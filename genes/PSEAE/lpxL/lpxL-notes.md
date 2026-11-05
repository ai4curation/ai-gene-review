# lpxL (PA3242, HtrB2, Q9HYZ8) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HYZ8 --alias lpxL`; accession matches the worklist. No
deep-research provider used. PMID:26223882 is abstract-only (PubMed MCP returned no body; Europe
PMC full text unavailable for PMC4626592).

### Literature

- [PMID:26223882 "In this study, we were able to show that each gene identified is responsible for site-specific modification of lipid A."]
  PA0011 = htrB1, PA3242 = htrB2. Deletions alter antibiotic and peptide resistance and increase
  membrane permeability.
- UniProt: HAMAP MF_01942, LpxL/LpxM/LpxP family, cell inner membrane.

### Annotation decisions

- ACCEPT: GO:0008913 (IDA, IEA), GO:0009245 (IBA, IDA, IEA), GO:0036104, GO:0009103, GO:0005886.
- TOO_GENERAL: GO:0016746 (IBA, IEA), GO:0016740, GO:0009247, GO:0016020 (IBA, IEA).
- Action counts: ACCEPT 8, TOO_GENERAL 6. No source defects.

## PseudoCAP IBA-seed assessment

Shared node PTN004745460 with PA0011 (same paper, same verdict; no node-level defect needed).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004745460 | GO:0016746 acyltransferase activity | 6 | 36 (22 taxa) | GO:0008913, IDA, PMID:26223882 (PseudoCAP) | SOUND | Abstract states HtrB2 is responsible for site-specific lipid A acylation; supports the generic node term. Assay type not checked (abstract only). | E. coli LpxL P0ACV0, LpxM P24205, LpxP P0ACV2, M. tuberculosis PatA P9WMB5, PA0011 Q9I7B5 | Yes |
| PTN004745460 | GO:0009247 glycolipid biosynthetic process | 6 | 23 (21 taxa) | GO:0009245, IDA, PMID:26223882 (PseudoCAP) | SOUND | Lipid A is a glycolipid; node term is generic enough to cover PIM acylation by PatA. | as above | Yes |
| PTN000770079 | GO:0009245 lipid A biosynthetic process | 2 | not listed separately | GO:0009245, IDA, PMID:26223882 (PseudoCAP) | SOUND | As above. | E. coli LpxL P0ACV0 | Yes |
