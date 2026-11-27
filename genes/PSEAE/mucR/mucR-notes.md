# mucR (PA1727, Q9I310) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I310 --alias mucR`; accession matches the worklist.
No deep-research provider used. PMID:23729646 and PMID:16477007 are abstract-only (PubMed MCP
returned no body for PMC3754559); PMID:19088322 and PMID:28186120 have cached full text.

### Literature

- MucR is an inner-membrane MHYT-GGDEF-EAL protein; LacZ/PhoA fusions place the GGDEF/EAL
  C-terminus in the cytosol [PMID:19088322 "Translational reporter enzyme fusions with LacZ and PhoA suggested that MucR is located in the cytoplasmic membrane with a cytosolic C terminus."]
- MucR drives alginate production through a localized c-di-GMP pool near Alg44; deletion of the
  GGDEF domain abolishes function [PMID:19088322 "Deletion of the proposed C-terminal GGDEF domain abolished MucR function."]
- Bifunctional in vitro [PMID:23729646 "In contrast, MucR displayed both diguanylate cyclase and PDE activity in vitro, which seemed regulated in a growth-dependent manner in vivo."]
- Dispersion phenotype in response to NO and glutamate [PMID:23729646 "Inactivation of mucR impaired biofilm dispersion in response to NO and glutamate"]. Unlike NbdA, MucR is not shown to be NO-induced; the NO-response row is a phenotype shared with another cue.
- Crystal structures of the MucR EAL domain with c-di-GMP and Mg2+ [PMID:28186120 "We have studied the EAL signature motif-containing phosphodiesterase domains from the Pseudomonas aeruginosa proteins PA3825 (PA3825EAL) and PA1727 (MucREAL)."]

### Annotation decisions

- ACCEPT: GO:0052621 (IDA x2, IEA), GO:0071111 (IDA, IBA, IEA), GO:0005886 (EXP, IEA).
- KEEP_AS_NON_CORE: GO:0071732 cellular response to nitric oxide (IMP, IEA/ARBA). Kept consistent
  with nbdA, where the same term is ACCEPTED because NbdA is NO-induced and NO-specific.
- Action counts: ACCEPT 8, KEEP_AS_NON_CORE 2. No source defects.

## PseudoCAP IBA-seed assessment

Shares PTN002403463 with PA5017 (DipA, Q9HUF2); same verdict and no node-level defect (see
PA5017 notes, which also record the EAL-less PA4929 leaf as a leaf-level exception). This node
is separate from PTN002105365 (rocR review) and PTN002895351 (wspR review).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002403463 | GO:0071111 cyclic-guanylate-specific phosphodiesterase activity | 3 | 14 (5 taxa) | GO:0071111, IDA, PMID:23729646 (PseudoCAP) | SOUND | Abstract states outright that MucR displayed PDE activity in vitro; the EAL domain binds c-di-GMP/Mg2+ in crystal structures (PMID:28186120). | E. coli PdeR P77334 (IDA PMID:17010156, EXP PMID:23708798), PA5017 Q9HUF2 (IDA PMID:22493016) | Yes |
