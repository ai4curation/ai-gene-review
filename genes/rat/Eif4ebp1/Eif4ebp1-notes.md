# Eif4ebp1 (rat, Q62622) review notes

## Session 2026-10-28

- `just fetch-gene rat Eif4ebp1` resolved Q62622 (4EBP1_RAT); 45 GOA rows seeded.
- PMIDs cached with `just fetch-gene-pmids`; PMID:20736160 is full text (read). All other
  GOA PMIDs are abstract-only; PMC full text for PMID:11865047 was not returned by the
  PubMed tool.
- No deep-research API available; literature synthesis in Eif4ebp1-deep-research-manual.md.

### Key evidence
- Function: hypophosphorylated 4E-BP1 binds eIF4E, competes with eIF4G, represses cap-dependent
  initiation [PMID:7939721 "Nonphosphorylated PHAS-I bound to initiation factor 4E (eIF-4E) and inhibited protein synthesis."].
- Rat brain IR: hierarchical Thr69 -> Thr36/45 -> Ser64 phosphorylation; Thr36/45 releases eIF4E
  [PMID:20736160 "Our results demonstrate that Thr69 phosphorylation alone allows binding to eIF4E, and subsequent Thr36/Thr45 phosphorylation is sufficient to dissociate 4E-BP1 from eIF4E."].

### Decisions
- Core: translation repressor activity (GO:0030371) via eIF4E binding (GO:0008190); process
  negative regulation of translational initiation (GO:0045947); location cytosol.
- `translation initiation factor binding` IPI (PMID:11865047): WITH = RGD:732833, which resolves
  to human EIF4E, so MODIFY to eIF4E binding.
- `negative regulation of protein-containing complex assembly` IMP: MODIFY to GO:1905536
  negative regulation of eIF4F complex assembly (the complex whose assembly is blocked).
- `negative regulation of translation` -> MODIFY to negative regulation of translational initiation.
- cytoplasm rows -> MODIFY to cytosol; nucleus rows -> MODIFY to nucleoplasm (nucleus is not one of
  the five root organelles in the ORGANELLES policy, so the general "correct but general" rule applies).
- Stress-response IEP/IDA rows (ischemia, hypoxia, amino-acid starvation) kept as non-core: 4E-BP1
  is the effector through which these signals repress initiation.
- Ethanol, lung development (IEP of phosphorylation change), G1/S and positive regulation of
  mitotic cell cycle, IRES-dependent initiation: marked over-annotated. IRES-dependent initiation is
  driven by other factors; 4E-BP1 only sequesters eIF4E, which indirectly favours cap-independent
  translation. A positive role in mitotic cell cycle is the opposite of the repressor's direct action.
- No NEW terms proposed.
