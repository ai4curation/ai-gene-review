---
title: "Calcitriol Biosynthesis from Calciol — Obsoletion & Replacement"
maturity: SCOPING
tags: [OBSOLETION]
species:
  - human
  - mouse
  - rat
genes:
  - CYP27B1
  - CYP2R1
  - CYP24A1
  - CYP27A1
  - CYP3A4
---

# Calcitriol Biosynthesis from Calciol — Obsoletion & Replacement

## Overview

A GO obsoletion proposal will obsolete the biological-process term
`GO:0036378 calcitriol biosynthetic process from calciol` and **replace** it
with the sibling term `GO:1901755 vitamin D3 biosynthetic process`. The
upstream rationale is that the two enzymatic steps captured by `GO:0036378`
(25-hydroxylation in liver + 1α-hydroxylation in kidney) are the only two
enzymatic steps in the broader MetaCyc vitamin D3 biosynthesis pathway
(MetaCyc:PWY-6076), so the narrower term is redundant once `GO:1901755` is
re-defined to have **calcitriol** (CHEBI:17823, the active hormone) as its
`has_primary_output` rather than calciol. With that re-definition,
`GO:1901755` subsumes the content of `GO:0036378` exactly, and a clean
`replaced_by` is appropriate.

This is a small, well-scoped curation hygiene job: 24 experimental
annotations on 5 cytochrome P450 genes, none of which currently has an
`*-ai-review.yaml` here. Both groups listed upstream (`BHF-UCL`, `UniProt`)
have already marked their portions done in the tracking spreadsheet.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6449](https://github.com/geneontology/go-annotation/issues/6449)
- Ontology ticket (re-definition + obsoletion):
  [geneontology/go-ontology#32077](https://github.com/geneontology/go-ontology/issues/32077)
- Affected-annotation spreadsheet (upstream-curated):
  https://docs.google.com/spreadsheets/d/1L1ymnLg1_t4fNK9psd211WUGOCHBpSd7ny0e1tC9JKo/edit

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| calcitriol biosynthetic process from calciol (BP) | `GO:0036378` | `GO:1901755 vitamin D3 biosynthetic process` (re-defined to output calcitriol) |

Term metadata confirmed in OLS on 2026-06-20:

- `GO:0036378` (`calcitriol biosynthetic process from calciol`) — live, slated
  for obsoletion. Synonyms include "vitamin D3 activation" and
  "1alpha,25-dihydroxyvitamin D3 biosynthesis".
- `GO:1901755` (`vitamin D3 biosynthetic process`) — live; the proposed
  replacement target. The upstream ontology ticket records the first two
  proposals (add `MetaCyc:PWY-6076` xref; change `has_primary_output` from
  CHEBI:28940 calciol → CHEBI:17823 calcitriol) as already done; the third
  (obsolete `GO:0036378`, `replaced_by` `GO:1901755`) is still pending.

## Affected experimental / curated annotations (24)

Retrieved from the QuickGO annotation API on 2026-06-20
(`goId=GO:0036378`, manual / experimental evidence codes only). Matches the
upstream group counts after accounting for ZFIN, MGI and RGD assertions that
the upstream tally rolls into "other groups":

| # | Source | Accession | Symbol | Organism | Evidence | Reference |
|---|---|---|---|---|---|---|
| 1 | BHF-UCL | UniProtKB:O15528 | CYP27B1 | Human | IDA | PMID:15795327 |
| 2 | BHF-UCL | UniProtKB:O15528 | CYP27B1 | Human | IDA | PMID:16549446 |
| 3 | BHF-UCL | UniProtKB:O15528 | CYP27B1 | Human | IDA | PMID:17023519 |
| 4 | BHF-UCL | UniProtKB:O15528 | CYP27B1 | Human | IDA | PMID:9415400 |
| 5 | BHF-UCL | UniProtKB:P08684 | CYP3A4 | Human | IDA | PMID:15546903 |
| 6 | BHF-UCL | UniProtKB:O35084 | Cyp27b1 | Mouse | IDA | PMID:9295274 |
| 7 | BHF-UCL | UniProtKB:O35132 | Cyp27b1 | Rat | IDA | PMID:9333115 |
| 8 | UniProt | UniProtKB:O15528 | CYP27B1 | Human | EXP | PMID:10518789 |
| 9 | UniProt | UniProtKB:O15528 | CYP27B1 | Human | EXP | PMID:10566658 |
| 10 | UniProt | UniProtKB:O15528 | CYP27B1 | Human | EXP | PMID:12050193 |
| 11 | UniProt | UniProtKB:O15528 | CYP27B1 | Human | EXP | PMID:9486994 |
| 12 | UniProt | UniProtKB:O15528 | CYP27B1 | Human | IDA | PMID:22862690 |
| 13 | UniProt | UniProtKB:O35084 | Cyp27b1 | Mouse | EXP | PMID:10092858 |
| 14 | UniProt | UniProtKB:O35084 | Cyp27b1 | Mouse | IDA | PMID:15972816 |
| 15 | UniProt | UniProtKB:Q02318 | CYP27A1 | Human | IDA | PMID:15465040 |
| 16 | UniProt | UniProtKB:Q6VVX0 | CYP2R1 | Human | EXP | PMID:12867411 |
| 17 | UniProt | UniProtKB:Q6VVX0 | CYP2R1 | Human | IDA | PMID:15465040 |
| 18 | UniProt | UniProtKB:Q6VVX0 | CYP2R1 | Human | IDA | PMID:18511070 |
| 19 | UniProt | UniProtKB:Q07973 | CYP24A1 | Human | IDA | PMID:25727742 |
| 20 | UniProt | UniProtKB:Q09128 | Cyp24a1 | Rat | IDA | PMID:25727742 |
| 21 | MGI | UniProtKB:Q6VVW9 | Cyp2r1 | Mouse | IDA | PMID:12867411 |
| 22 | RGD | UniProtKB:O35132 | Cyp27b1 | Rat | IDA | PMID:9371776 |
| 23 | RGD | UniProtKB:P17178 | Cyp27a1 | Rat | IDA | PMID:2175615 |
| 24 | ZFIN | UniProtKB:A0A097HUX0 | cyp27b1 | Zebrafish | IDA | PMID:25290078 |

On top of these 24 curated records, GO:0036378 currently has **~2,048 total
annotations** (QuickGO, 2026-06-20). The non-experimental tail is small for
this term (the first 100 results contained only one IBA + IDA + ~98 IEA),
which is consistent with a tightly-scoped catalytic BP rather than a
broadly-propagated complex/localization term.

## Why a clean `replaced_by` is appropriate here

Unlike `GO:0030943 mitochondrion targeting sequence binding`
([[MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION]]), where the affected
annotations span biologically distinct mechanism classes, **all 24 affected
annotations are on enzymes catalyzing one of the two hydroxylation steps in
the vitamin D3 → calcitriol pathway**, and the re-defined `GO:1901755`
(`has_primary_output` = calcitriol) literally subsumes the old `GO:0036378`
content. The four annotated CYP roles are:

- **CYP2R1 / CYP3A4 / CYP27A1** — vitamin D 25-hydroxylase activity
  (calciol → 25-hydroxycalciferol / calcidiol). CYP2R1 is the principal
  hepatic 25-hydroxylase; CYP3A4 and CYP27A1 contribute secondary
  25-hydroxylation routes.
- **CYP27B1** — 25-hydroxyvitamin D3 1α-hydroxylase
  (calcidiol → calcitriol, in kidney). This is the activating step that the
  obsoleted term explicitly named.
- **CYP24A1** — 24-hydroxylase that inactivates 25-hydroxyvitamin D3 and
  1,25-(OH)₂D3 (calcitriol). The IDA annotations for CYP24A1 to `GO:0036378`
  in PMID:25727742 are arguably **borderline**: CYP24A1's primary catalytic
  output is the 24-hydroxylated, inactivation-pathway metabolite, not
  calcitriol itself. Reviewers should flag whether `GO:1901755` is the right
  successor, or whether a vitamin D **catabolic** term
  (e.g. `GO:0042369 vitamin D catabolic process`) is more appropriate.
  This is the one case where mechanical `replaced_by` may not be the right
  outcome.

## Impact on this repo

**None of the five affected genes currently has an `*-ai-review.yaml`** under
`genes/` (verified 2026-06-20 across `genes/human/`, `genes/mouse/`,
`genes/rat/`, `genes/zebrafish/`). There are also no other reviews here that
cite `GO:0036378` (`grep -r "GO:0036378" genes/` returned no hits). So this
obsoletion does **not** invalidate any existing AI Gene Review content.

That said, vitamin D biosynthesis is a small, well-characterized,
high-textbook-coverage pathway, and CYP27B1 in particular is medically
important (loss-of-function causes vitamin D-dependent rickets type 1A). It
is a natural candidate for a small, focused gene-family review project, with
this obsoletion as a clean entry point.

## Scope

- **GO branch:** Biological Process (single term obsoletion + `replaced_by`).
- **Organisms:** Human, mouse, rat (curated experimental set); zebrafish
  (one IDA). No yeast / plant / fly annotations.
- **Gene set:** 5 cytochrome P450 enzymes — CYP27B1 (1α-hydroxylase),
  CYP2R1 (principal 25-hydroxylase), CYP27A1 (secondary 25-hydroxylase),
  CYP3A4 (alternative 25-hydroxylase), CYP24A1 (24-hydroxylase / inactivator,
  the edge case).
- **Type of fix:** Curation hygiene + small family review. The biology is
  uncontroversial; the only real curation decision is the CYP24A1 case.

## Candidate genes for initial review

Listed in priority order. The first three would directly exercise the
re-defined `GO:1901755` once the obsoletion lands.

1. **CYP27B1 (human, O15528)** — 1α-hydroxylase; the canonical
   "vitamin D activation" enzyme; 9 of the 24 affected annotations. Highest
   priority and best positive control.
2. **CYP2R1 (human, Q6VVX0)** — principal hepatic 25-hydroxylase; 3 of the
   24 annotations. The other half of the activation route.
3. **CYP27A1 (human, Q02318)** — secondary 25-hydroxylase / sterol
   27-hydroxylase; pleiotropic (also acts on bile-acid precursors).
4. **CYP3A4 (human, P08684)** — drug-metabolizing CYP; vitamin D
   25-hydroxylation is a minor, non-core activity. Good test case for
   `MARK_AS_OVER_ANNOTATED` vs. `KEEP_AS_NON_CORE`.
5. **CYP24A1 (human, Q07973)** — 24-hydroxylase / vitamin D inactivator. The
   edge case: decide whether `GO:1901755` is the right successor or whether
   a catabolic vitamin D term should be used instead. Coordinate with the
   upstream ontology ticket.

The rodent orthologs (`Cyp27b1` mouse/rat, `Cyp2r1` mouse, `Cyp24a1` rat,
`Cyp27a1` rat, `cyp27b1` zebrafish) are not initial-priority for individual
review here — the human reviews will pull their orthologs in via IBA, and
curators in MGI/RGD/ZFIN have already marked or can mirror the upstream
remapping.

## Proposed approach

1. **Wait for the upstream `replaced_by` to land.** The first two ontology
   proposals (xref + `has_primary_output`) are marked done; the obsoletion
   + `replaced_by` step is still pending in go-ontology#32077. Once it
   merges, all 24 annotations migrate automatically.
2. **Open a CYP27B1 review first** (`just fetch-gene human CYP27B1`) as the
   highest-value, lowest-risk case. Use it to validate that the re-defined
   `GO:1901755` is the right `molecular_function` / `involved_in` BP for the
   1α-hydroxylation step.
3. **Add CYP2R1 and CYP27A1** next; these establish the 25-hydroxylase
   half of the pathway and will also need a vitamin D **metabolic / sterol
   hydroxylase** MF.
4. **Handle CYP3A4 and CYP24A1 as edge cases.** For CYP3A4, the vitamin D
   25-hydroxylation is a non-core, low-affinity activity and may warrant
   `KEEP_AS_NON_CORE` or `MARK_AS_OVER_ANNOTATED` rather than `ACCEPT`. For
   CYP24A1, the right successor is plausibly a **catabolic** vitamin D term,
   not `GO:1901755`; flag this back to the upstream tracker if confirmed.
5. **No InterPro2GO / UniRule / UniProt-Keyword cleanup needed.** The
   upstream issue explicitly notes "No Mappings" for `GO:0036378`. The
   downstream-mapping triage that the larger obsoletion projects need
   (e.g. [[NLS_BINDING_OBSOLETION]], [[VESICLE_DOCKING_OBSOLETION]]) does not
   apply here.

## Priority

Low–Medium. Only 24 curated annotations on a five-gene set with no current
reviews here, no mapping fallout, and both upstream curator groups already
marking their work done. The value of opening this is twofold: (a) a clean
test of the `replaced_by` flow on a small, well-defined pathway; and (b) a
natural anchor for a focused vitamin D / cytochrome P450 mini-review of
CYP27B1 (medically important; vitamin D-dependent rickets type 1A) and its
hydroxylase partners. Skip if higher-priority obsoletions are still open.

## Status

- 2026-06-20 — Project file created. Tracking go-annotation#6449 (opened
  2026-06-08, both BHF-UCL and UniProt marked done) and the open
  go-ontology#32077 (third proposal — `replaced_by` `GO:1901755` — still
  pending). The 24 affected curated annotations were retrieved from QuickGO
  (`goId=GO:0036378`, experimental evidence) and reconciled against the
  upstream group tally. Both `GO:0036378` and `GO:1901755` confirmed live in
  OLS. No existing AI Gene Review files reference `GO:0036378`; none of the
  five affected CYP genes (CYP27B1, CYP2R1, CYP27A1, CYP3A4, CYP24A1) has a
  review here yet. CYP24A1 flagged as the one annotation whose successor
  term needs confirmation (catabolic vs biosynthetic vitamin D).
