# SIR4 curation notes

## 2026-09-02 Update

Audited existing_annotations for oversights (this is a companion fix to the same
issue found and fixed in SIR2 and SIR3).

- **GO:0006303 (double-strand break repair via nonhomologous end joining), IMP,
  PMID:9501103**: was marked `MARK_AS_OVER_ANNOTATED` ("SIR4 is not a direct
  participant in the NHEJ catalytic machinery... this is an indirect function...
  overstates SIR4's role"). But the cited paper's abstract reports a direct
  functional assay, not an inference: "using an in vivo plasmid rejoining assay,
  we demonstrate that SIR2, SIR3 and SIR4, three genes shown previously to
  function in TPE, are essential for Ku-dependent DSB repair" [PMID:9501103
  "SIR2, SIR3 and SIR4, three genes shown previously to function in TPE, are
  essential for Ku-dependent DSB repair"]. SIR4 is not core NHEJ catalytic
  machinery, so the function remains secondary/non-core, but `MARK_AS_OVER_ANNOTATED`
  mischaracterizes directly-demonstrated genetic evidence as likely spurious
  over-annotation. Changed action to `KEEP_AS_NON_CORE`, consistent with the same
  fix applied to SIR2 and SIR3 for the identical annotation/reference.
- All other annotations reviewed; no other genuine, evidence-backed oversights
  found.
