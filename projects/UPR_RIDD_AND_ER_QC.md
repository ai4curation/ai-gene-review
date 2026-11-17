---
title: "Unfolded Protein Response: RIDD and the ER Quality Control Branch"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [SCHPO, human, yeast, worm]
collections: [GO_TRACKER_BACKLOG]
index_group: GO_TRACKER_BACKLOG
---

# Unfolded Protein Response: RIDD and the ER Quality Control Branch

**Bottom line:** A 2017 GO tracker issue from PomBase points out that GO
defines the ER unfolded protein response (GO:0030968) and its IRE1 branch
(GO:0036498) as signaling, but in fission yeast Ire1's only output is
regulated IRE1-dependent mRNA decay (RIDD), which is arguably not signaling.
So annotating S. pombe ire1 to the UPR terms breaks the true-path rule. No
RIDD term exists. In 2026 the request moved to a newer ticket with a
four-step plan, none of it implemented. A companion 2021 issue on ERAD terms
is now mostly resolved by the new grouping term GO:0170080 *endoplasmic
reticulum protein quality control*. One item from it is left: whether
GO:0006983 *ER overload response* duplicates the UPR. This repo has the UPR
side well covered (88 rows on 49 genes for GO:0030968). It has no review of
S. pombe ire1 or the RIDD machinery, and human ERN1's review records RIDD only
as a non-core generic RNA catabolic process. Scoped, not started.

## Upstream tickets

| Issue | Opened | Request | Last substantive comment |
|---|---|---|---|
| [go-ontology#14380](https://github.com/geneontology/go-ontology/issues/14380) | 2017-10-18 | UPR terms are defined as signaling; S. pombe Ire1 acts only via RIDD | 2017-12-18 (continued in #28057) |
| [go-ontology#20914](https://github.com/geneontology/go-ontology/issues/20914) | 2021-02-17 | ERAD terms that look like the same process, plus related items | 2026-08-21 |

The RIDD request continues in
[go-ontology#28057](https://github.com/geneontology/go-ontology/issues/28057)
(open, last comment 2026-10-12), where PomBase posted a plan on 2026-09-28:
a neutral IRE1 definition, signaling moved down a level, and a new RIDD term.
Thread summaries are as of 2026-11-16, and term states from a go-ontology
checkout of 2026-11-12. Nothing has been posted to these issues.

## Where the threads stand

- **#14380.** PomBase consulted the paper's author, who agreed the RIDD
  output is arguably not signaling. PomBase concluded: "Therefore I think an
  new term for the RIDD pathway without a signalling parent is required."
  (2017-12-18). Nothing was implemented.
  - GO:0036498 is still is_a GO:0030968, which is is_a GO:0035556
    intracellular signal transduction.
  - Its definition still describes HAC1/XBP1 splicing.
  - GO:0030968 is now part_of GO:0170080.
- **#20914.** Largely done by PRs in August 2026. GO:0170080 was created, and
  GO:0036503 was renamed *ERAD quality control pathway* and placed under it.
  Several duplicate ERAD terms were obsoleted into GO:0036503, and the
  protein-catabolism duplicates were merged. Left open: GO:0006983 *ER
  overload response* versus GO:0030968, both live and both part_of
  GO:0170080.

## What this repo already has

Computed 2026-11-16 with
[`term_actions.py`](GO_TRACKER_BACKLOG/term_actions.py).

| Term | Rows | Genes | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED | Other | Core in |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| GO:0030968 endoplasmic reticulum unfolded protein response | 88 | 49 | 65 | 19 | 1 | 2 | 0 | 0 | NEW 1 | 16 |
| GO:0036498 IRE1-mediated unfolded protein response | 38 | 20 | 27 | 8 | 0 | 3 | 0 | 0 |  | 6 |
| GO:0036499 PERK-mediated unfolded protein response | 21 | 8 | 18 | 1 | 0 | 1 | 0 | 0 | NEW 1 | 3 |
| GO:0036500 ATF6-mediated unfolded protein response | 13 | 6 | 11 | 2 | 0 | 0 | 0 | 0 |  | 4 |
| GO:0006983 ER overload response | 11 | 7 | 3 | 5 | 0 | 1 | 0 | 2 |  | 0 |
| GO:0006986 response to unfolded protein | 48 | 37 | 23 | 20 | 1 | 2 | 1 | 0 | NEW 1 | 9 |
| GO:0034976 response to endoplasmic reticulum stress | 118 | 71 | 40 | 57 | 12 | 6 | 0 | 0 | NEW 2, NOT REMOVE 1 | 5 |
| GO:0036503 ERAD quality control pathway | 134 | 63 | 105 | 8 | 7 | 6 | 2 | 1 | NEW 5 | 38 |
| GO:0170080 endoplasmic reticulum protein quality control | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 |

What stands out:

- **IRE1 branch reviews are all metazoan or budding yeast.** ACCEPT rows on
  GO:0036498 are human ERN1, XBP1 and HSPA5, worm ire-1 and xbp-1, yeast
  IRE1, and HYPJE IRE1. All of these are splicing-competent systems. There
  is no SCHPO review of ire1, and the cell that motivates the RIDD term is
  missing.
- **RIDD is invisible in the reviews.** human/ERN1 records RIDD only as
  GO:0006401 *RNA catabolic process* (IEA, KEEP_AS_NON_CORE): "RIDD is a
  recognized secondary output of IRE1 RNase activity". SCHPO/tam14's review
  notes that the S. pombe UPR uses Ire1-dependent RIDD without Hac1/XBP1.
- **ER overload response is a grab bag.** The 7 genes on GO:0006983 are
  human TP53, WFS1 (ACCEPT), GSK3B, EIF2AK3, rat Tp53, Gsk3b and Hspa5. Only
  EIF2AK3 and WFS1 are UPR components. TP53 and GSK3B are the apoptosis side.
  That bears directly on whether GO:0006983 is a duplicate.

## What gene review can and cannot settle

- **Can document:** the S. pombe case, through reviews of SCHPO ire1 and the
  RIDD decay machinery named in the thread (Dom34/Hbs1 no-go decay, the
  Ski complex). This is the evidence that a RIDD process exists outside
  signaling, and it gives the NTR its first annotations.
- **Can settle, per gene:** for the 7 GO:0006983 genes, whether the row
  describes the UPR itself (merge-compatible), ER-stress-induced apoptosis,
  or something else. That is the evidence for the item left on #20914.
- **Cannot settle:** re-parenting the UPR terms away from signal
  transduction. That is the #28057 plan and an editor decision.

## Plan

- [ ] New review: SCHPO ire1. Record RIDD activity and propose the RIDD
      process term as `proposed_new_terms`, matching #28057.
- [ ] New reviews for the decay partners named in #14380: SCHPO dom34,
      hbs1, and one Ski complex subunit.
- [ ] Re-check human/ERN1: should the RIDD row stay at GO:0006401, or be
      flagged for the NTR?
- [ ] Classify the 11 GO:0006983 rows (UPR component, apoptosis, other) as
      evidence for the merge question.
- [ ] Coordinate with [CAEEL_UPR_STRESS](CAEEL_UPR_STRESS.md) and
      [PROTEOSTASIS](PROTEOSTASIS.md), which already cover the metazoan UPR
      and ERAD genes.

## STATUS

- 2026-11-16: project scoped from the GO tracker backlog. No reviews started.

## NOTES

### 2026-11-16

- Created from the [GO tracker backlog](GO_TRACKER_BACKLOG.md). Both
  threads and #28057 read.
- The 2017 thread cites the S. pombe RIDD paper as PMID: 28945192 (written
  with a space). Verify it before citing it in a review.
