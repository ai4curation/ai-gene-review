---
title: "Fatty Acid Biosynthesis versus Elongation"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human, yeast, SCHPO, ARATH, worm, ECOLI]
collections: [GO_TRACKER_BACKLOG]
autolink_exclude: [benD]
---

# Fatty Acid Biosynthesis versus Elongation

**Bottom line:** A 2013 GO tracker issue, the oldest open content question
after the RNA polymerase II holoenzyme ticket, asks how "fatty acid
biosynthetic process" differs from "fatty acid elongation" and its
saturated, unsaturated, monounsaturated and polyunsaturated children. It
also asks when to use GO:0006636 *unsaturated fatty acid biosynthetic
process* rather than GO:0019368 *fatty acid elongation, unsaturated fatty
acid*. An editor's 2013 working rule was: fatty acid synthase goes to
biosynthesis, and the separate ER elongation systems go to elongation. It
was never written into the ontology, and PomBase's 2022 summary called it a
multiple-axis classification problem. This repo has reviewed essentially
every elongase in the main model organisms, and the reviews apply the two
axes inconsistently: the same term is ACCEPTed on one ELOVL, kept non-core
on another, and removed on the yeast ones. A per-enzyme usage table would
turn the 2013 rule into evidence. Scoped, not started.

## Upstream ticket

| Issue | Opened | Last substantive comment |
|---|---|---|
| [go-ontology#10773](https://github.com/geneontology/go-ontology/issues/10773) | 2013-12-16 | 2022-11-19 |

Thread summary as of 2026-11-16, and term states from a go-ontology checkout
of 2026-11-12. Nothing has been posted to the issue.

## Where the thread stands

- **The question** (2013-12-16): when would one use GO:0006636 instead of
  GO:0019368?
- **The working rule** (2013-12-17): "annotate fatty acid synthase to
  GO:0006633 fatty acid biosynthetic process, and 'other enzyme systems' as
  above to GO:0030497 fatty acid elongation."
- **Reactome's account:**
  - FAS releases mainly palmitate.
  - Chains beyond C18 are extended by separate ER enzymes.
  - Desaturation is a separate step.
  - Saturated medium- and long-chain synthesis terms, plus elongation and
    desaturation terms, may be enough.
- **The opposing view:** another curator objected to a process per round of
  the elongation cycle.
- **PomBase** (2022-11-19): GO needs to decide whether both axes are
  required, and if so add the missing parentage. No decision has been
  recorded.

In go-edit.obo:

- GO:0030497 is is_a GO:0006633. Its four children are textually defined
  only, with no logical definitions.
- GO:0019368 is not under GO:0006636, and there is no "saturated fatty acid
  biosynthetic process" for GO:0019367 to sit under.
- On the MF side, GO:0009922 *fatty acid elongase activity* is now
  specifically the ER condensation step for C16 and longer chains.
  GO:0102756 *very-long-chain 3-ketoacyl-CoA synthase activity* was obsoleted
  in its favour.

## What this repo already has

Computed 2026-11-16 with
[`term_actions.py`](GO_TRACKER_BACKLOG/term_actions.py).

| Term | Rows | Genes | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED | Other | Core in |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| GO:0006633 fatty acid biosynthetic process | 176 | 108 | 120 | 7 | 24 | 12 | 7 | 1 | NEW 2, TOO_GENERAL 3 | 46 |
| GO:0030497 fatty acid elongation | 36 | 30 | 22 | 3 | 0 | 2 | 5 | 2 | TOO_GENERAL 2 | 6 |
| GO:0019367 fatty acid elongation, saturated fatty acid | 40 | 24 | 25 | 9 | 0 | 4 | 0 | 2 |  | 7 |
| GO:0019368 fatty acid elongation, unsaturated fatty acid | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0034625 fatty acid elongation, monounsaturated fatty acid | 24 | 15 | 13 | 3 | 0 | 6 | 0 | 2 |  | 4 |
| GO:0034626 fatty acid elongation, polyunsaturated fatty acid | 29 | 15 | 13 | 7 | 0 | 3 | 5 | 1 |  | 4 |
| GO:0006636 unsaturated fatty acid biosynthetic process | 32 | 24 | 21 | 5 | 2 | 0 | 0 | 0 | NEW 4 | 13 |
| GO:1903966 monounsaturated fatty acid biosynthetic process | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |  | 2 |
| GO:0051792 medium-chain fatty acid biosynthetic process | 3 | 2 | 2 | 0 | 0 | 0 | 1 | 0 |  | 1 |
| GO:0042759 long-chain fatty acid biosynthetic process | 29 | 13 | 19 | 0 | 4 | 6 | 0 | 0 |  | 6 |
| GO:0042761 very long-chain fatty acid biosynthetic process | 57 | 27 | 47 | 5 | 0 | 3 | 0 | 1 | NEW 1 | 22 |
| GO:0009922 fatty acid elongase activity | 83 | 19 | 81 | 0 | 1 | 0 | 0 | 1 |  | 18 |
| GO:0004312 fatty acid synthase activity | 22 | 12 | 6 | 0 | 15 | 0 | 1 | 0 |  | 2 |

Reviewed here:

- **ER elongation system:** human ELOVL1-7, HACD1, HACD2, HSD17B12 and TECR;
  yeast ELO1-3, IFA38, PHS1 and TSC13; SCHPO elo1, elo2, phs1 and tsc13;
  ARATH FAE1, CUT1, KCR1, PAS2 and ECR; worm elo-5 and elo-6.
- **De novo synthases:** human FASN; yeast FAS1, FAS2 and ACC1; the yeast
  mitochondrial FAS-II genes CEM1, HFA1, MCT1 and OAR1; E. coli fabF and
  fabB.

What stands out:

- **The same term means two things.** GO:0019367 (saturated elongation) is
  ACCEPT on ELOVL1, ELOVL3 and ELOVL4 and on E. coli fabF (IDA), kept non-core
  on ELOVL5, ELOVL7, yeast FAS1, FAS2 and ACC1, and marked over-annotated on
  CEM1, HFA1, MCT1 and OAR1. Reviewers are deciding case by case whether
  de novo FAS cycles count as "elongation", which is the 2013 question.
- **Two axes, chosen per ELOVL.** On GO:0006636 (unsaturated biosynthesis)
  ELOVL2, ELOVL5 and ELOVL6 are ACCEPT while ELOVL1, ELOVL3 and ELOVL7 are
  kept non-core, and ELOVL4 is MODIFY. Meanwhile GO:0019368, the elongation-
  axis term for the same thing, has a single row (yeast ELO1).
- **Taxon sense applied, but not consistently.** GO:0034626 (PUFA elongation)
  is removed on yeast ELO1-3 and SCHPO elo1/2, which have no PUFA substrates,
  marked over-annotated on ELOVL1 and worm elo-5/elo-6, and ACCEPT on
  ELOVL2/4/5.
- **GO:0030497 itself** is TOO_GENERAL on yeast ELO2 and ELO3 (IMP), and
  removed as an electronic mis-mapping on five bacterial benD/ymfI/actI-ORF1
  rows.

## What gene review can and cannot settle

- **Can settle:** a usage table, one row per enzyme family (FAS-I, FAS-II,
  ELOVL/ELO condensing enzyme, KAR, HACD, TECR, desaturases), saying which
  process term each should carry on each axis. All of the families are
  already reviewed, so this is an audit, not new curation.
- **Can test:** whether the 2013 rule (FAS to biosynthesis, ER elongation to
  elongation) can be applied mechanically to every row here, and where it
  fails.
- **Cannot settle:** whether GO keeps both axes, or adds the missing
  parentage. That is an editor decision. The table gives it a concrete basis.

## Plan

- [ ] Build the usage table from the existing reviews (all rows on the 13
      terms above), grouped by enzyme family.
- [ ] Flag inconsistent actions within a family (ELOVL1-7 on GO:0019367,
      GO:0006636, GO:0034625 and GO:0034626; FAS-I and FAS-II on GO:0019367)
      and harmonise them in follow-up review edits, one PR per family.
- [ ] Record the 2013 rule as a project convention for new reviews until GO
      decides, and note it in [FATTY_ACID_BETA_OXIDATION](FATTY_ACID_BETA_OXIDATION.md)
      and [LIPID_DIVIDE](LIPID_DIVIDE.md) if those touch the same genes.
- [ ] Summarise the table for the issue owners. Posting it is the project
      lead's decision.

## STATUS

- 2026-11-16: project scoped from the GO tracker backlog. No edits started.

## NOTES

### 2026-11-16

- Created from the [GO tracker backlog](GO_TRACKER_BACKLOG.md). Thread read
  in full.
- The 15 MODIFY rows on GO:0004312 *fatty acid synthase activity* move
  polyketide synthases and the yeast and fission-yeast FAS1/FAS2 subunits to
  GO:0004321 *fatty-acyl-CoA synthase activity* (10) or GO:0016218
  *polyketide synthase activity* (5). This is a separate but adjacent
  consistency question.
