# Nitrogen Cycle Metabolic Process — do_not_annotate / Regulation Term Obsoletion

## Overview

A GO obsoletion proposal will:

- Mark **GO:0071941 nitrogen cycle metabolic process** as `do_not_annotate`
  (term remains, but new direct annotations are forbidden — existing
  annotations must move to a descendant pathway term such as denitrification,
  nitrogen fixation, nitrification, or mineralization).
- Obsolete the three regulation terms outright:
  - GO:1903314 regulation of nitrogen cycle metabolic process
  - GO:1903315 negative regulation of nitrogen cycle metabolic process
  - GO:1903316 positive regulation of nitrogen cycle metabolic process

The motivation (per upstream) is that "nitrogen cycle metabolic process" is an
ecosystem-level grouping term: real biology happens in its children
(denitrification, nitrification, nitrogen fixation, mineralization). Direct
annotation to the parent erases mechanistic detail and — more importantly — has
attracted over-annotations of mammalian genes that have nothing to do with the
ecological nitrogen cycle.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6411](https://github.com/geneontology/go-annotation/issues/6411)
- Ontology ticket: [geneontology/go-ontology#27220](https://github.com/geneontology/go-ontology/issues/27220)

## Obsoletion / do_not_annotate plan (per upstream)

| Term | ID | Action | Replacement strategy |
|---|---|---|---|
| nitrogen cycle metabolic process | GO:0071941 | `do_not_annotate` (stays as grouping term) | Re-route to a descendant: e.g. GO:0019333 denitrification pathway, GO:0009399 nitrogen fixation, GO:0008152 / a nitrification or mineralization child as appropriate |
| regulation of nitrogen cycle metabolic process | GO:1903314 | obsolete | No replacement currently slated — only relevant if a child regulation term exists for the specific pathway |
| negative regulation of nitrogen cycle metabolic process | GO:1903315 | obsolete | Same |
| positive regulation of nitrogen cycle metabolic process | GO:1903316 | obsolete | Same |

Term labels verified in OLS on 2026-05-13. All four terms are still live.
The replacement term GO:0019333 (denitrification pathway) was also verified.

## Affected experimental annotations

The upstream issue cites 5 MGI + 1 CACAO experimental annotations.
QuickGO (exact-term query against GO:0071941, evidence codes IDA / IMP / IGI /
IPI / IEP) on 2026-05-13 returns 6 direct experimental annotations — matching
the upstream count:

| # | Gene | Accession | Taxon | Qualifier | Evidence | PMID | Assigned by | Replacement plan |
|---|---|---|---|---|---|---|---|---|
| 1 | Prkcsh | UniProtKB:O08795 | Mus musculus (10090) | acts_upstream_of_or_within | IGI | PMID:21685914 | MGI | **REMOVE** — Prkcsh is glucosidase II β / Pkd-network polycystic-liver gene; no nitrogen-cycle role |
| 2 | Pkd1 | UniProtKB:O08852 | Mus musculus (10090) | acts_upstream_of_or_within | IGI | PMID:21685914 | MGI | **REMOVE** — Polycystin-1, cystogenic Ca²⁺ signalling; no nitrogen-cycle role |
| 3 | Pkd1 (dup) | UniProtKB:O08852 | Mus musculus (10090) | acts_upstream_of_or_within | IGI | PMID:21685914 | MGI | **REMOVE** — Duplicate row; flag both annotations |
| 4 | Apc | UniProtKB:Q61315 | Mus musculus (10090) | acts_upstream_of_or_within | IMP | PMID:16740478 | MGI | **REMOVE** — Adenomatous polyposis coli (Wnt pathway / liver zonation); no nitrogen-cycle role |
| 5 | Sec63 | UniProtKB:Q8VHE0 | Mus musculus (10090) | acts_upstream_of_or_within | IGI | PMID:21685914 | MGI | **REMOVE** — Sec63 translocon component; no nitrogen-cycle role |
| 6 | napA | UniProtKB:O88111 | Cereibacter sphaeroides f. sp. denitrificans (39723) | involved_in | IMP | PMID:10227138 | CACAO | **MODIFY → GO:0019333 denitrification pathway** — Periplasmic nitrate reductase; legitimate denitrification gene |

Five of the six annotations look like classic over-annotation of mammalian
kidney/liver genes (PKD1, PRKCSH, SEC63 are the canonical autosomal dominant
polycystic kidney/liver disease genes; APC drives a liver-zonation phenotype).
The 1999 paper supporting napA (PMID:10227138, Bisci. Biotechnol. Biochem.) is
explicitly about denitrification in Rhodobacter (Cereibacter) sphaeroides, so
the bacterial annotation is biologically sound but should be moved to the
specific child term GO:0019333 (denitrification pathway), not stranded on the
parent.

The three regulation children (GO:1903314 / 1903315 / 1903316) currently have
**zero experimental annotations** in QuickGO (verified 2026-05-13), so their
obsoletion is uncontested from an annotation-impact standpoint.

## Impact on this repo

None of the affected genes (mouse Prkcsh / Pkd1 / Apc / Sec63 or
Cereibacter napA) currently have an `*-ai-review.yaml` in this repo
(verified by `find genes -iname '*Prkcsh*' -o -iname '*Pkd1*' -o -iname
'*Apc*' -o -iname '*Sec63*' -o -iname '*napA*'` and a directory scan of
`genes/mouse`, `genes/human` on 2026-05-13). The project is therefore a
queueing exercise plus a clear documentation of the over-annotation pattern
this term has accumulated.

## Scope

- **Organisms involved:** mouse (Mus musculus, 4 of the 5 MGI annotations
  collapse to 4 distinct genes after the Pkd1 duplicate) and Cereibacter
  sphaeroides f. sp. denitrificans (1 CACAO annotation).
- **GO branch:** biological process — nitrogen metabolism / microbial
  nitrogen-cycle pathways and their mammalian over-annotations.
- **Type of fix:**
  - Five mammalian annotations are scientifically incorrect (these genes do
    not act in the nitrogen cycle as defined by the term) and should be
    **removed**, not relabelled. The annotation pattern suggests automatic
    propagation from a kidney/liver phenotype to "nitrogen handling" without
    discriminating ecological nitrogen cycle (microbial) from mammalian
    nitrogen excretion biology.
  - One bacterial annotation is correct in spirit but should be **modified**
    to a specific child term (GO:0019333 denitrification pathway).

## Candidate genes for initial review

Listed in priority order. Each should be set up with
`just fetch-gene <organism> <gene>` before review begins. Mouse genes are
written with the MGI symbol casing; substitute the species code as appropriate
for the `fetch-gene` invocation (e.g. `mouse` for MGI orthologs, or pull the
human ortholog if better-characterised).

1. **PKD1 (mouse Pkd1, UniProtKB:O08852; human PKD1)** — Polycystin-1. The
   IGI annotation to GO:0071941 from PMID:21685914 is a clear over-annotation
   and a useful case study: a kidney-disease genetic-interaction paper has
   propagated an ecological-nitrogen-cycle term onto a mammalian
   mechanotransduction gene. The human PKD1 review would carry the most
   downstream value because PKD1 is heavily studied; flag the mouse-MGI
   annotation in the existing-annotations review.
2. **PRKCSH (mouse Prkcsh, UniProtKB:O08795; human PRKCSH)** —
   Protein kinase C substrate 80K-H / glucosidase II β subunit. Same paper
   (PMID:21685914), same critique. PRKCSH's actual core function is N-linked
   glycoprotein quality control in the ER (glucosidase II regulatory
   subunit); reviewing it would let us cleanly remove the nitrogen-cycle
   over-annotation in the same pass.
3. **SEC63 (mouse Sec63, UniProtKB:Q8VHE0; human SEC63)** —
   Translocon subunit, ER protein translocation. Same paper, same critique.
   Human SEC63 is the canonical autosomal dominant polycystic liver disease
   gene and a clean target for a focused over-annotation removal.
4. **APC (mouse Apc, UniProtKB:Q61315; human APC)** —
   Adenomatous polyposis coli, β-catenin destruction complex scaffold. The
   IMP annotation from PMID:16740478 (Apc as "zonation-keeper" of mouse
   liver) does not support a nitrogen-cycle role; the paper's phenotype is
   metabolic zonation in hepatocytes, which involves urea-cycle and
   ammonia-handling enzymes downstream — not a nitrogen-cycle role for APC
   itself. Recommend REMOVE of the GO:0071941 annotation in the APC review.
5. **napA (Cereibacter sphaeroides f. sp. denitrificans, UniProtKB:O88111)** —
   Periplasmic nitrate reductase. Biologically the cleanest case: the
   PMID:10227138 IMP evidence supports involvement in denitrification, so
   the GO:0071941 annotation should be **modified** to GO:0019333
   denitrification pathway. Use the species code corresponding to taxon
   39723 (Cereibacter sphaeroides f. sp. denitrificans). This is a
   non-canonical organism for the repo and may not have an obvious species
   subdirectory yet; check before invoking `just fetch-gene`.

## Proposed approach

1. **Pattern-document the mammalian over-annotation first.** Add a short
   section to `projects/OVER_ANNOTATION_PATTERNS.md` (or a new entry there)
   noting that GO:0071941 has attracted polycystic kidney/liver genes via
   IGI/IMP propagation from PMID:21685914 and PMID:16740478. This is a
   reusable insight even if the obsoletion is delayed.
2. **Prioritise the human orthologs over the mouse MGI entries.** Human
   PKD1, PRKCSH, SEC63, APC are well-studied and likely to attract more
   downstream consumers of any review we publish. The mouse-MGI annotation
   can be cited within those reviews under `existing_annotations` (or under
   `references` with a brief note).
3. **Move napA last.** It is biologically correct and only needs a term
   refinement (MODIFY); it does not have the diagnostic value of the
   mammalian cluster. If the Cereibacter species directory does not yet
   exist, this is a small enough single-annotation case to defer.
4. **Wait for the do_not_annotate decision before bulk-rewriting.** GO
   ontology ticket #27220 may still be in discussion. The action codes
   (REMOVE vs MODIFY) in any reviews started now are not affected by
   the eventual ontology decision; do not block on the upstream timing.

## Priority

Medium-low. The total annotation set is tiny (6 rows), but the over-annotation
pattern is illustrative — five out of six annotations on a microbial-ecology
term are on mammalian kidney/liver genes. Reviewing PKD1 / PRKCSH / SEC63
fits the repo's existing emphasis on cleaning up over-annotations of pleiotropic
genes (see `projects/OVER_ANNOTATION_PATTERNS.md`).

## Status

- 2026-05-13 — Project file created. Tracking upstream issue #6411 (opened
  prior; last upstream activity 2026-05-12). Term labels and the proposed
  replacement (GO:0019333) verified in OLS. Affected annotation set
  cross-checked via the QuickGO REST API (6 hits, matching the upstream
  count). No reviews started; none of the 5 distinct affected genes are in
  the repo yet.
