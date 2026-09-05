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

## 2026-09-05 Update (review follow-up)

Follow-up to PR review feedback on the GO:0006303 entry: the previous `reason`
attributed the NHEJ requirement to SIR3's "telomere/chromatin maintenance role",
which was an unevidenced mechanism swapped in for another. Looked up the actual
literature (PMIDs resolved via `ai-gene-review fetch-pmid`, not guessed) and the
established mechanism is silencing-dependent control of *NEJ1* expression:

- Deleting *SIR* genes derepresses the silent mating-type cassettes, and it is
  that derepression — not a Sir role at the break — that accounts for the NHEJ
  defect [PMID:10421582 "the effect of deleting SIR genes is largely
  attributable to derepression of silent mating-type genes, although Sir
  proteins do play a minor role in end-joining"]. In haploids that retain their
  mating type, *sir* deletions left plasmid end-joining unaffected and reduced
  chromosomal NHEJ only two- to threefold.
- The downstream target is *NEJ1*, a haploid-specific NHEJ factor whose promoter
  carries an a1/α2 repressor site: "transcription of NEJ1 was completely
  repressed in a/alpha diploid and sir haploid strains. The NEJ1 promoter
  contained a consensus binding site for the a1/alpha2 repressor" [PMID:11676923].
- Decisive test: restoring Nej1p bypasses the Sir requirement entirely
  [PMID:11676923 "Expression of Nej1p from a constitutive promoter in a/alpha
  diploid and sir mutant strains completely rescued the defect in NHEJ, thus
  showing that Sir proteins per se were dispensable for NHEJ"].

Given the rescue result, SIR3 is not a participant in end-joining; it acts
upstream, silencing HML/HMR so that *NEJ1* stays expressed. Changed the action
from `KEEP_AS_NON_CORE` to `MODIFY`, proposing GO:2001032 (regulation of
double-strand break repair via nonhomologous end joining; id verified via OLS,
already used elsewhere in this repo). Chose the general regulation term over the
directional GO:2001034 because SIR3's contribution is permissive — maintaining
*NEJ1* expression — rather than active modulation of the repair reaction itself.

Also addressed two smaller review points:

- The `UNDECIDED` GO:0070481 entry's `supported_by` quoted only the paper title,
  which reads as support for a claim that PR showed cannot be supported. Swapped
  in the recoverable methods sentence [PMID:17660569 "for 15 genes that were
  initially identified in our screen, the his3 -nonstop suppression phenotype
  was indeed linked to their deletion mutants"] and added a breadcrumb naming
  Table 2 of that paper (or the SGD annotation detail) as the concrete unblocker.
- Flagged, without editing out of scope: the identical GO:0006303 / IMP /
  PMID:9501103 annotation — from one experiment assaying SIR2, SIR3 and SIR4
  together — is currently adjudicated three different ways across the repo
  (SIR2 `REMOVE`, SIR3 this entry, SIR4 `MARK_AS_OVER_ANNOTATED`). Those sibling
  entries should be reconciled with the NEJ1 rationale above in a separate pass;
  a note to that effect is now in the SIR3 `reason`.
