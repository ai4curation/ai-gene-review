# ANKRD34B notes

- Mouse DP58 = Ankrd34b. It is a cytosolic phosphoprotein induced within 30 min of bone-marrow commitment to dendritic cells [PMID:15358210], and a 52 kDa nuclear phosphoprotein in neurons [PMID:17485271]. Human ANKRD34B is brain-enriched (HPA). All four papers are cached as abstracts only.
- GOA: cytosol (HPA IDA), cytoplasm (IEA) and nucleus (IEA, by similarity) are ACCEPT.
- The pi-body IBA is REMOVE: it is the same stale PTN001192751 / Asz1 (MGI:1921318) propagation as in ANKRD34A (#4117). The PTHR24156 files are byte-identical to that PR's.
- The knockdown in ES-derived mesoderm [PMID:20184659] changes NF-H, PPARγ and PECAM1. The authors' "might be a positive regulator of neurogenesis" is speculation from marker changes, and no process is assigned.
- PubMed recall: the other "DP58" hits are an unrelated Sphingomonas strain.
- knowledge_gaps: MF_DARK.

## Round 2 (reviewer on ANKRD34A, PR #4117; applied to all three ANKRD34 reviews)

- The pi-body propagation_review root_cause changes from SOURCE_STALE_OR_MISSING to PROPAGATION_BAD. Asz1's own pi-body localization is sound; the node propagated it to the wrong subfamily. failure_modes are [WRONG_ORTHOLOG_OR_PARALOG, CONTEXT_OR_TISSUE_MISMATCH].
- The reason now gives the domain-architecture argument. PTHR24157 is the ankyrin repeat, SAM and bZIP family, and mouse Asz1 has 6 ANK repeats plus a SAM domain; ANKRD34 proteins have 4 ANK repeats plus a disordered tail. PANTHER keeps a PTHR24157:SF0 "ANKYRIN REPEAT DOMAIN-CONTAINING PROTEIN 34A-RELATED" subfamily, which is probably how the stale node once spanned both.
