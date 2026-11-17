---
title: "Cytolysis: Phenotype, Self-Lysis or Killing Another Cell?"
maturity: SCOPING
tags: [OBSOLETION, BIOLOGY_DOMAIN]
species: [human, DROME, LAMBD, BPT4, BPT7, BPP2]
collections: [GO_TRACKER_BACKLOG]
---

# Cytolysis: Phenotype, Self-Lysis or Killing Another Cell?

**Bottom line:** A 2017 GO tracker issue asks whether GO:0019835
*cytolysis* (the rupture of a cell's membranes) is a process at all or a
phenotype, and how its annotations should be split between self-lysis,
killing of cells of the same organism, and killing of cells of another
organism. A 2017 plan was agreed: make GO:0019835 a do-not-annotate
grouping term and obsolete the "in other organism" regulation terms. Part of
it was done. The regulation terms and the do-not-annotate tag were not, and
PomBase's 2020 "Can we go ahead with this?" got no reply. In this repo the
picture is clear. 22 of 37 rows on GO:0031640 *killing of cells of another
organism* are phage lysis proteins, and reviews already MODIFY those to
GO:0044659 *viral release from host cell by cytolysis*. The only direct
GO:0019835 rows are NINJ1 and its fly orthologue, a case the thread never
considered. Scoped, not started.

## Upstream ticket

| Issue | Opened | Last substantive comment | Checklist last edited |
|---|---|---|---|
| [go-ontology#13041](https://github.com/geneontology/go-ontology/issues/13041) | 2017-02-22 | 2020-02-03 | 2026-02-10 |

Thread summary as of 2026-11-16, and term states from a go-ontology checkout
of 2026-11-12. Nothing has been posted to the issue.

## Where the thread stands

- **The original objection** (2017-02-22) was that if cytolysis is just the
  observed outcome of membrane rupture, "then it’s a phenotype rather than a
  process, and it shouldn’t be in GO." The three E. coli annotations then on
  the term looked like autolysis or same-species killing.
- **The 2017-12-21 plan:** "Keep GO:0019835 cytolysis as a grouping term (+
  tag 'do not annotate')", obsolete GO:0051715 and the regulation-in-other-
  organism terms, and move annotations to the symbiont terms.
- **Done:** GO:0051710, GO:0051713, GO:0051714, GO:0051801 to GO:0051804,
  GO:0051838 to GO:0051841 and GO:0001898 are obsolete.
- **Not done:**
  - GO:0042268 *regulation of cytolysis* and its positive and negative
    children are live.
  - GO:0019835 has no do-not-annotate subset and keeps related synonyms such
    as "holin" and "necrosis".
  - GO:0051715 was renamed *cytolysis in another organism* and now has
    children (GO:0001897 symbiont-mediated cytolysis of host cell, GO:0044179
    hemolysis in another organism) rather than being obsoleted.

## What this repo already has

All non-obsolete is_a/part_of descendants of GO:0019835 and GO:0031640
with at least one row, computed 2026-11-16 with
[`term_actions.py`](GO_TRACKER_BACKLOG/term_actions.py).

| Term | Rows | Genes | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED | Other | Core in |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| GO:0019835 cytolysis | 6 | 2 | 6 | 0 | 0 | 0 | 0 | 0 |  | 2 |
| GO:0031640 killing of cells of another organism | 37 | 37 | 2 | 2 | 22 | 1 | 3 | 0 | NEW 3, TOO_GENERAL 4 | 4 |
| GO:0044659 viral release from host cell by cytolysis | 30 | 24 | 20 | 0 | 1 | 1 | 0 | 0 | NEW 6, TOO_GENERAL 2 | 22 |
| GO:0001897 symbiont-mediated cytolysis of host cell | 3 | 1 | 3 | 0 | 0 | 0 | 0 | 0 |  | 1 |
| GO:0001907 symbiont-mediated killing of host cell | 2 | 1 | 2 | 0 | 0 | 0 | 0 | 0 |  | 1 |
| GO:0019836 symbiont-mediated hemolysis of host erythrocyte | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | NEW 1 | 1 |
| GO:0044179 hemolysis in another organism | 2 | 1 | 2 | 0 | 0 | 0 | 0 | 0 |  | 1 |
| GO:0039640 viral release via suppression of host peptidoglycan biosynthetic process | 3 | 2 | 3 | 0 | 0 | 0 | 0 | 0 |  | 2 |
| GO:0044660 viral release via pore formation in host cell membrane | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  | 1 |
| GO:0090680 viral release via disruption of host outer membrane | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |  | 2 |
| GO:0044696 killing by virus of host cell by post-segregational killing | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  | 1 |
| GO:0052151 symbiont-mediated activation of host apoptosis | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  | 1 |
| GO:0070943 neutrophil-mediated killing of symbiont cell | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | TOO_GENERAL 2 | 0 |
| GO:0070944 neutrophil-mediated killing of bacterium | 5 | 3 | 3 | 1 | 0 | 0 | 1 | 0 |  | 1 |
| GO:0070945 neutrophil-mediated killing of gram-negative bacterium | 2 | 2 | 0 | 2 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0070947 neutrophil-mediated killing of fungus | 5 | 3 | 3 | 1 | 0 | 0 | 0 | 1 |  | 1 |

Total: 104 rows on 51 reviewed genes. Of the regulation terms the 2017 plan
left alive, only GO:0045918 *negative regulation of cytolysis* is used: one
ACCEPT row on LAMBD/S, for the S-107 antiholin that delays holin hole
formation. No review carries GO:0042268, GO:0045919 or GO:0051715 itself.

What stands out:

- **Phage lysis is the dominant real use, and it already has a home.**
  - The 22 MODIFY rows on GO:0031640 are holins, endolysins and spanins from
    lambda (S, R, Rz, Rz1), T4, T7, P2, phi6, MS2 and Qbeta. Nearly all were
    moved to GO:0044659 or one of its mechanism-specific children.
  - Four more are marked TOO_GENERAL for the same reason.
  - The thread's "holin" synonym on GO:0019835 points the same way.
- **NINJ1 is a self-lysis case the thread did not foresee.** human/NINJ1 and
  DROME/NijA carry GO:0019835 (all ACCEPT, 6 rows). NINJ1 oligomerizes to
  rupture the plasma membrane of the cell that expresses it, during lytic
  cell death. That is the cell's own lysis. It argues for keeping a
  self-lysis concept (or GO:0019835 as it stands) rather than tagging the
  term do-not-annotate.
- **Killing by immune cells is a separate axis.** The neutrophil-mediated
  killing rows concern immune killing of microbes, which the thread does not
  discuss.

## What gene review can and cannot settle

- **Can settle, per row:**
  - self-lysis (NINJ1, autolysins);
  - lysis of a host by a symbiont, phage or pathogen (already the
    GO:0044659/GO:0001897 branches);
  - killing of another organism's cells by a toxin or immune effector;
  - phenotype only.
- **Can provide:** the evidence that GO:0019835 has live, non-phenotypic
  annotations (NINJ1), which bears on the do-not-annotate plan.
- **Cannot settle:** whether GO:0051715 should still be obsoleted now that it
  has children, or what replaces the regulation-of-cytolysis terms. These are
  editor decisions.

## Plan

- [ ] Confirm the GO:0031640 MODIFY rows all target the GO:0044659 subtree,
      and check the 3 REMOVE (ARATH LCR1, T4 gene 5, T7 gene 16) and 4
      TOO_GENERAL rows.
- [ ] New reviews for the thread's own example classes:
  - [ ] one E. coli autolysis or same-species killing gene with a GO:0019835
        row in GOA;
  - [ ] one antimicrobial peptide with a "cytolysis in another organism" row;
  - [ ] human PRF1 (perforin) as the immune-effector case.
- [ ] Find which genes carry GO:0042268, GO:0045918 or GO:0045919 in GOA
      across the repo's organisms, and review a sample. These are the
      un-actioned rows. The lambda antiholin row shows that at least some
      are phage lysis timing, which belongs with GO:0044659.
- [ ] Write a short note for the issue owners on NINJ1 and the phage
      evidence. Posting it is the project lead's decision.

## STATUS

- 2026-11-16: project scoped from the GO tracker backlog. No reviews started.

## NOTES

### 2026-11-16

- Created from the [GO tracker backlog](GO_TRACKER_BACKLOG.md). Thread read
  in full, including the edited checklist.
- GO:0019835 still carries the KW-0204 (UniProt keyword "Cytolysis")
  definition source. The UniProt keyword mapping may be what keeps feeding
  annotations to the term.
