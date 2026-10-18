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
  entries should be reconciled with the NEJ1 rationale above in a separate pass.

## 2026-09-29 Update

Aligned SIR3 with the IBA propagation review:

- The `GO:0006270` transfer from the ORC1/CDC6 PAINT family still carries a
  `PROPAGATION_BAD`/`WRONG_ORTHOLOG_OR_PARALOG` propagation review because Sir3
  is an ORC1-derived silent-chromatin scaffold that suppresses, rather than
  initiates, MCM loading at euchromatic origins. The `GO:0003688` transfer is now
  `TERM_SCOPING_PROBLEM`: SIR3 itself is in that seed list via SGD's
  over-scoped origin-binding IDA from PMID:29795547, whose data support Sir3
  binding to origin-adjacent nucleosomes rather than origin DNA itself.
- The `GO:0033314` checkpoint-signaling IBA points to the same PTN in the cached
  GOA row but is no longer present in the local 2026 PTHR10763 PAINT export, so
  it was marked `SOURCE_STALE_OR_MISSING`.
- The five remaining `GO:0005515 protein binding` rows from RAP1/SIR4
  interaction and high-throughput complex papers are now `REMOVE`: the physical
  interactions are not disputed, but no more-specific RAP1- or Sir4-binding MF
  term exists and generic protein binding should not be retained.

The newer full-text SIR3 literature does not reopen the IBA calls. Brothers and
Rine 2022 refine Sir3 recruitment and spread by Sir3-M.EcoGII/Nanopore mapping
but do not support origin-DNA binding or initiation. Bordelet et al. 2022 do
require a correction to the September NHEJ rationale: the original NEJ1
rescue literature still shows an indirect SIR contribution through HML/HMR
silencing, but SIR3 also has a direct Sae2-binding role that limits
MRX-dependent resection and promotes NHEJ [PMID:34817085 "Via physical
interaction with the Sae2 protein, Sir3 impairs Sae2-dependent functions of the
MRX (Mre11-Rad50-Xrs2) complex, thereby limiting Mre11-mediated resection,
delaying MRX removal from DSB ends, and promoting NHEJ"]. The existing
`GO:0006303` action therefore remains `MODIFY`, but the replacement is now the
directional `GO:2001034 positive regulation of double-strand break repair via
nonhomologous end joining`. Because the same paper explicitly describes Sir3 as
"a direct negative regulator of Sae2", the proposed Sae2-directed molecular
function is the direction-preserving `GO:0140678 molecular function inhibitor
activity`.
