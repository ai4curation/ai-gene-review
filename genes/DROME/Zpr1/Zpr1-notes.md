# Zpr1 (DROME, Q9W379) review notes

## Session 2026-10-28

- `just fetch-gene DROME Zpr1` resolved Q9W379 (ZPR1_DROME); 19 GOA rows.
- Only one Drosophila paper exists (PMID:23029159, full text read). Ortholog papers cached:
  PMID:36630955, PMID:37597513 (yeast chaperone function, full text), PMID:9852145 (eEF1A
  binding, full text), PMID:9763455 (nucleolus, full text), PMID:8650580 and PMID:11283611
  (abstract only). Literature summary in `Zpr1-deep-research-manual.md`.

### Decisions

- Core: eEF1A-dedicated protein folding chaperone (GO:0044183), translation elongation factor
  binding (GO:0061770), protein folding (GO:0006457), cytoplasm. All rest on orthologs
  (yeast experimental, PAINT IBA from root node PTN000093466) [PMID:36630955 "Zpr1 enables eEF1A to achieve a conformational state resistant to protease digestion"].
- GO:0031369 translation initiation factor binding (ISS from human IPI, with P68104 = EEF1A1):
  MODIFY to GO:0061770; source defect recorded (wrong term at the human UniProt row,
  propagated by FlyBase ISS).
- Tracheal phenotype terms (terminal branching IMP, lumen formation IGI): KEEP_AS_NON_CORE;
  direct and rescued mutant phenotype [PMID:23029159 "We find that a single copy of this transgene is able to rescue the lethality associated with 31ZZ, as well as all terminal cell defects (data not shown)."].
- EGFR signaling (IGI): KEEP_AS_NON_CORE. Epistasis plus mammalian ZPR1-EGFR binding
  (PMID:8650580) make it plausible, but no pathway read-out was measured in the fly.
- FGFR signaling (IGI): MARK_AS_OVER_ANNOTATED. Only epistasis to activated Btl
  overexpression; the interaction is untested, and a general requirement for an essential chaperone
  explains the result equally well.
- cellular response to EGF stimulus (ISS), pre-mRNA catabolic process (ISS):
  MARK_AS_OVER_ANNOTATED (mammal-specific observation / unsupported source row).
- system development, animal gross anatomical part developmental process (ARBA IEA): MODIFY
  to the specific tracheal terms the gene already carries.
- No NEW terms proposed (strict NEW bar; phenotype evidence only for fly).
