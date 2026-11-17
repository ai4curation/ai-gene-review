---
title: "Protein Stabilization and Destabilization: What Do the Terms Mean?"
maturity: SCOPING
tags: [OBSOLETION, BIOLOGY_DOMAIN]
species: [human, mouse, rat, ECOLI, DROME]
collections: [GO_TRACKER_BACKLOG]
---

# Protein Stabilization and Destabilization: What Do the Terms Mean?

**Bottom line:** Two GO tracker issues from 2018 question whether
GO:0050821 *protein stabilization* and GO:0031648 *protein destabilization*
describe processes at all. Curators in both threads say many annotations
record a mutant or knockdown phenotype, the loss of one complex subunit
making its partners unstable, rather than a gene product's job. Obsoletion
of GO:0050821 was favoured in 2018 but never decided, and the usage
guidelines asked for in 2020 were never written. This repo leans the other
way. It holds 231 rows on 155 genes for GO:0050821, about half ACCEPT, and
reviews have added 24 NEW rows. Sorting those rows into chaperones (an MF),
stabilizing partners, true anti-degradation regulators, and phenotypes is
what both issues need. Scoped, not started.

## Upstream tickets

| Issue | Opened | Request | Last substantive comment |
|---|---|---|---|
| [go-ontology#16360](https://github.com/geneontology/go-ontology/issues/16360) | 2018-09-10 | missing parent: should protein stabilization subsume GO:2000059? (became: should the term exist?) | 2021-01-04 |
| [go-ontology#20833](https://github.com/geneontology/go-ontology/issues/20833) | 2018-03-17 | TMEM147 and NOMO2 annotated to protein destabilization from PMID:20538592 | 2024-10-25 |

Thread summaries are as of 2026-11-16 and term states from a go-ontology
checkout of 2026-11-12. Nothing has been posted to either issue.

## Where the threads stand

- **#16360.** The opening question was a parentage one, about GO:2000059
  *negative regulation of ubiquitin-dependent protein catabolic process*.
  It turned into a question about GO:0050821 itself: "Many different types of
  genes have been directly annotated to 'protein stabilization', and some of
  those annotations seem to reflect phenotypes resulting from loss of one
  subunit of a multi-protein complex." (2018-09-12). Obsoletion was favoured,
  and PomBase put the term on its do-not-annotate list. The term went to
  editors' discussion, and the last comment (2021-01-04) asks whether that
  discussion happened. In go-edit.obo GO:0050821 is live, defined as
  positively regulating the characteristic *protein stability*
  (OBA:0000128), and is not linked to GO:2000059.
- **#20833.** The original error was fixed in 2018: the curator found the
  paper showed stabilization, not destabilization, and removed the TMEM147
  and NOMO2 rows. The thread then generalised. A neXtProt editor wrote that
  "an IMP to 'protein stabilization' is unlikely to reflect a real function"
  (2018-03-22), and PomBase asked whether stability is an outcome rather than
  a process. The reporter tried to close the issue in 2020 but an editor kept
  it open, because guidelines are still needed. The last comment (2024-10-25)
  counts 91 experimental annotations to GO:0031648. NCLN (Nicalin) still
  carries GO:0050821 (IMP) and GO:0061635 (IDA) from the same paper.

## What this repo already has

Computed 2026-11-16 with
[`term_actions.py`](GO_TRACKER_BACKLOG/term_actions.py).

| Term | Rows | Genes | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED | Other | Core in |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| GO:0050821 protein stabilization | 231 | 155 | 96 | 92 | 1 | 11 | 2 | 3 | NEW 24, NOT ACCEPT 2 | 53 |
| GO:0031648 protein destabilization | 26 | 22 | 0 | 21 | 0 | 2 | 2 | 0 | NEW 1 | 1 |
| GO:0031647 regulation of protein stability | 78 | 53 | 12 | 46 | 9 | 7 | 1 | 2 | NOT ACCEPT 1 | 3 |
| GO:2000059 negative regulation of ubiquitin-dependent protein catabolic process | 9 | 8 | 6 | 2 | 0 | 1 | 0 | 0 |  | 4 |
| GO:0061635 regulation of protein complex stability | 8 | 6 | 6 | 2 | 0 | 0 | 0 | 0 |  | 1 |

What stands out:

- **The ACCEPT and core rows on GO:0050821 are mostly chaperones and
  holdases**: CRYAA, CRYAB, BAG1-3, CLU, CANAL/CDC37, CALR, DROME Hsp83, E. coli
  Skp and SurA, and NEW rows on E. coli HdeA, HdeB and Spy and on tardigrade
  CAHS3 and MAHS. In #16360 these are the cases a curator called really a
  molecular function. The repo's
  [UNFOLDED_PROTEIN_BINDING](UNFOLDED_PROTEIN_BINDING.md) project already
  deals with the missing holdase MF that may explain why reviewers reach for
  the process term.
- **The KEEP_AS_NON_CORE rows are kinases, transcription factors and
  structural proteins**: AKT2, ATM, CHEK2, CDK7, CREB1, EP300, DSP, FLNA,
  GAPDH. That is the phenotype pattern the thread describes, and reviewers
  kept the rows rather than removing them.
- **Destabilization rows are never core.** 21 of 26 are KEEP_AS_NON_CORE, on
  E3 ligases (CUL3, PRKN, SIAH1, FBXL3), proteases (CAPN3) and signaling
  proteins (SRC, MTOR). A ligase that ubiquitinates a substrate has a
  catalytic MF and a catabolic-process term, so "destabilization" adds
  nothing.
- **Reviews are extending the term.** 24 NEW rows, and 53 reviews naming
  GO:0050821 in `core_functions`, cut against the 2018 lean towards
  obsoletion. The reasons these reviews give are the input the issues need.

## What gene review can and cannot settle

- **Can settle, per row:** which of four classes a GO:0050821 or GO:0031648
  annotation belongs to: (a) chaperone or holdase activity (an MF; record
  it), (b) a complex partner whose loss destabilizes the others (better as
  the complex membership), (c) a regulator that blocks or promotes
  degradation of a named substrate (e.g. a deubiquitinase; better as
  regulation of the catabolic process, the GO:2000059 parentage question),
  (d) a phenotype with no mechanism (remove).
- **Can supply:** worked examples from the experimental rows for the
  guidelines #20833 asks for, starting with NCLN and the 2018 paper.
- **Cannot settle:** whether GO keeps the terms. If the classification shows
  class (d) dominates the experimental rows, that is strong evidence for
  obsoletion.

## Plan

- [ ] Classify every GO:0050821 row in the repo into (a)-(d), starting with
      the 53 core-function uses and the 24 NEW rows.
- [ ] Same for the 26 GO:0031648 rows and the 78 GO:0031647 rows.
- [ ] Check reviews that ACCEPT GO:0050821 alongside a chaperone MF. Is the
      process row adding anything?
- [ ] New review: human NCLN (GO:0050821 IMP, GO:0061635 IDA,
      PMID:20538592), with TMEM147 and NOMO1/NOMO2 as complex partners. This
      is the issue's own case.
- [ ] Draft usage guidance with one example per class, for the issue owners.
      Posting it is the project lead's decision.

## STATUS

- 2026-11-16: project scoped from the GO tracker backlog. No reviews started.

## NOTES

### 2026-11-16

- Created from the [GO tracker backlog](GO_TRACKER_BACKLOG.md). Both
  threads read in full.
- PMID:20538592 is cached as abstract only. A review of NCLN needs the full
  text before judging the IMP row.
