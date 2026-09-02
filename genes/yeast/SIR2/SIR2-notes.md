# SIR2 curation notes

## 2026-09-02 Update

Audited existing_annotations for oversights.

- **GO:0006303 (double-strand break repair via nonhomologous end joining), IMP,
  PMID:9501103**: was marked `REMOVE` with the reasoning "SIR2 is not a component
  of the NHEJ repair machinery... conflates recombination suppression with NHEJ
  repair." This is contradicted by the cited paper's own abstract, which reports
  a direct functional assay: "using an in vivo plasmid rejoining assay, we
  demonstrate that SIR2, SIR3 and SIR4, three genes shown previously to function
  in TPE, are essential for Ku-dependent DSB repair" [PMID:9501103 "using an in
  vivo plasmid rejoining assay, we demonstrate that SIR2, SIR3 and SIR4, three
  genes shown previously to function in TPE, are essential for Ku-dependent DSB
  repair"]. SIR2 is not part of the core catalytic NHEJ machinery (Ku70/80,
  Lig4/Dnl4), but the IMP evidence directly demonstrates it is genuinely required
  for efficient Ku-dependent end-joining in vivo (most plausibly through its role
  in telomere/chromatin maintenance rather than catalysis). Changed action from
  `REMOVE` to `KEEP_AS_NON_CORE` to reflect this real, experimentally-demonstrated,
  secondary requirement rather than removing a genuine finding.
- All other annotations reviewed; no other genuine, evidence-backed oversights
  found. The rest of the review reflects an extensive prior systematic curation
  pass (see `README-CURATION.md`, `CURATION-REVIEW-FINAL.md`) that remains sound.
