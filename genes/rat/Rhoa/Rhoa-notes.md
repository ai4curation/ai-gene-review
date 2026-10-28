# Rhoa (rat, P61589) review notes

## Session 1 (create review)

- Fetched with `just fetch-gene rat Rhoa`; UniProt id confirmed P61589 (RHOA_RAT).
  GOA has 207 rows, most of them ISO/ISS transfers from human P61586 and mouse
  Q9QUI0 (MGI:1096342), plus a large set of rat pharmacology/pathophysiology papers
  (2002-2018), almost all abstract-only in the cache.
- No deep-research provider available; literature synthesis is in
  `Rhoa-deep-research-manual.md`.
- Sequence identity of RhoA across rat/mouse/human (identical 193-aa chain)
  makes ISO/ISS transfer of molecular function and location low risk; process
  transfers from mouse knockouts (acts_upstream_of_or_within) are the weakest.

## Decisions worth flagging

- PMID:20858895 "microtubule depolymerization" (IMP): full text shows RhoA acts
  downstream of drug-induced MT depolymerisation (GEF-H1 -> RhoA -> ROCK -> CTGF/ERK
  survival) ["MT depolymerization releases GEF-H1 that activates RhoA by inducing
  exchange of GTP for GDP on RhoA"]. RhoA does not depolymerise microtubules, so
  the row was MODIFIED to Rho protein signal transduction.
- PMID:17488779 "positive regulation of cell migration" (IEP): the abstract says Nogo
  "inhibits the migration of OECs via NgR regulation of RhoA" - sign is wrong;
  MODIFIED to negative regulation of cell migration.
- IEP "response to X" rows (ethanol, glucose, hypoxia, glucocorticoid, amino acid,
  xenobiotic, progesterone) only show RhoA expression/activity changing:
  MARK_AS_OVER_ANNOTATED.
- GTP metabolic process (PMID:21440892) is an over-reading of RhoA activity
  measurement: MARK_AS_OVER_ANNOTATED.
- Mouse-knockout developmental transfers (kidney, bone, T cell, cortex) kept as
  non-core; indirect metabolic/transcription transfers (oxidative phosphorylation,
  ROS biosynthesis, RNA pol II transcription, androgen receptor signalling) marked
  as over-annotations.
- No NEW terms proposed. GO:0160124 (guanyl nucleotide exchange factor activator
  activity, for allosteric ECT2 activation) is supported only by similarity in
  UniProt; left as a question.

## Key quotes

- [PMID:20472934 "free RhoA rapidly exchanged its bound nucleotide (GDP) with GTP, and the reaction was saturated after 15 min"]
- [PMID:21423166 "RhoA and Cdc42 were rapidly activated in the stimulated spine"]
- [PMID:17662049 "ICAM-1 cross-linking induces a strong activation of RhoA in RBE4 cells"]
