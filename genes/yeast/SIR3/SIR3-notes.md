# SIR3 curation notes

## 2026-09-02 Update

Audited existing_annotations for oversights.

- **GO:0006303 (double-strand break repair via nonhomologous end joining), IMP,
  PMID:9501103**: was marked `REMOVE` ("SIR3 itself is not a NHEJ component or
  catalyst"). This is contradicted by the cited paper's own abstract, which
  reports a direct in vivo functional assay: "using an in vivo plasmid rejoining
  assay, we demonstrate that SIR2, SIR3 and SIR4, three genes shown previously to
  function in TPE, are essential for Ku-dependent DSB repair" [PMID:9501103
  "using an in vivo plasmid rejoining assay, we demonstrate that SIR2, SIR3 and
  SIR4, three genes shown previously to function in TPE, are essential for
  Ku-dependent DSB repair"]. SIR3 is not core catalytic NHEJ machinery, but the
  IMP evidence directly demonstrates a genuine secondary requirement. Changed
  `REMOVE` to `KEEP_AS_NON_CORE`.
- **GO:0070481 (nuclear-transcribed mRNA catabolic process, non-stop decay), IMP,
  PMID:17660569**: was marked `REMOVE` with a specific mechanistic claim
  ("indirect through secondary effects on gene expression or cell stress
  responses") that isn't supported by anything in the cached source. The abstract
  is not gene-specific; I force-refetched full text (`ai-gene-review fetch-pmid
  17660569 --force`, now cached with `full_text_available: true`), but the body/
  discussion text never names SIR3, and the results table (Table 2, listing all
  15 genes with per-gene phenotype values) is not recoverable from the cached
  page — table rows were not captured by the HTML extraction. Since the specific
  supporting detail for SIR3 cannot be verified, and per project guidance an
  experimental annotation should not be REMOVEd on an unverified assumption,
  changed action to `UNDECIDED`.
- All other annotations reviewed; no other genuine, evidence-backed oversights
  found.
