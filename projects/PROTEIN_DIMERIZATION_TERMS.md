---
title: "Protein Dimerization and Oligomerization Terms"
maturity: SCOPING
tags: [OBSOLETION, PIPELINE]
species: [human, mouse, ARATH, ECOLI]
collections: [GO_TRACKER_BACKLOG]
index_group: GO_TRACKER_BACKLOG
---

# Protein Dimerization and Oligomerization Terms

**Bottom line:** Two GO tracker issues, from 2014 and 2017, ask whether
GO:0042803 *protein homodimerization activity*, GO:0046982 *protein
heterodimerization activity*, GO:0046983 *protein dimerization activity* and
the oligomerization processes should exist. Their critics say these terms
describe subunit composition, not activity. Over 43 comments a rough
consensus formed: retire the dimerization MF terms, keep GO:0042802
*identical protein binding*, and record partners in the WITH or has_input
fields. It was never ratified or implemented, and all the terms are live.
This repo leans on them heavily: 615 rows on 463 reviewed genes for
homodimerization alone. Reviews split between genes almost evenly: 191
genes ACCEPT it, 215 keep it non-core. Some reviews MODIFY the generic
dimerization term into the specific ones GO wants to retire. Before more
reviews entrench the terms, this repo needs a convention, and the evidence
behind one is useful upstream. Scoped, not started.

## Upstream tickets

| Issue | Opened | Request | Last substantive comment |
|---|---|---|---|
| [go-ontology#11094](https://github.com/geneontology/go-ontology/issues/11094) | 2014-06-04 | obsolete the dimerization MF terms (and protein homooligomerization) | 2021-02-09 |
| [go-ontology#13036](https://github.com/geneontology/go-ontology/issues/13036) | 2017-02-21 | umbrella for dimerization and oligomerization term problems | 2018-09-25 |

Thread summaries are as of 2026-11-16, and term states from a go-ontology
checkout of 2026-11-12. Nothing has been posted to either issue.

## Where the threads stand

- **#11094.** PomBase asked to obsolete GO:0042803, GO:0046982, GO:0046983 and
  GO:0051260 as composition rather than activity, and lists them as
  do-not-annotate locally.
  - An editor first defended homodimerization as a kind of self-binding.
  - A curator defended the terms for nuclear receptors and drug targets.
  - Another editor proposed cellular-component dimer terms instead.
  - A 2017 comment showed the term had been stretched to trimers: "we have
    been encouraged to use this term for trimers".
  - By 2021 the assignee backed plain protein binding with the partner in
    WITH or has_input, and keeping GO:0042802. The pro-retention curator
    objected that this does not propagate to orthologs.
- **#13036.** This collects earlier proposals. In 2018 an editor proposed
  obsoleting the oligomerization processes and moving annotations to
  GO:0032991 *protein-containing complex* or GO:0065003 *protein-containing
  complex assembly*. A curator asked that any surviving definition say
  whether spontaneous self-association counts: the current definition "does
  not indicate that protein association with itself (spontaneous) is either
  intended or excluded" (2018-09-18). A related request for a hexamerization
  term was closed as won't fix in 2020.

In go-edit.obo all four #11094 terms are live, and GO:0046983 still has a
process-style definition ("The formation of a protein dimer..."). The
oligomerization process family is intact. GO:0051259 is now labelled
*protein complex oligomerization* and is_a GO:0065003. No cellular-component
dimer term exists.

## What this repo already has

Computed 2026-11-16 with
[`term_actions.py`](GO_TRACKER_BACKLOG/term_actions.py).

| Term | Rows | Genes | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED | Other | Core in |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| GO:0042803 protein homodimerization activity | 615 | 463 | 286 | 261 | 16 | 17 | 2 | 11 | NEW 18, NOT ACCEPT 3, NOT KEEP_AS_NON_CORE 1 | 42 |
| GO:0046982 protein heterodimerization activity | 158 | 119 | 97 | 38 | 2 | 9 | 5 | 3 | NEW 4 | 49 |
| GO:0046983 protein dimerization activity | 132 | 124 | 54 | 31 | 35 | 1 | 0 | 6 | NEW 2, TOO_GENERAL 3 | 15 |
| GO:0042802 identical protein binding | 2203 | 952 | 925 | 907 | 232 | 73 | 12 | 42 | NEW 4, TOO_GENERAL 8 | 44 |
| GO:0051259 protein complex oligomerization | 25 | 21 | 8 | 10 | 2 | 3 | 0 | 0 | NEW 1, TOO_GENERAL 1 | 4 |
| GO:0051260 protein homooligomerization | 75 | 55 | 48 | 25 | 0 | 0 | 1 | 0 | NEW 1 | 9 |
| GO:0051291 protein heterooligomerization | 12 | 7 | 0 | 11 | 0 | 0 | 0 | 0 | NEW 1 | 0 |
| GO:0051262 protein tetramerization | 18 | 16 | 8 | 8 | 0 | 1 | 1 | 0 |  | 0 |
| GO:0051289 protein homotetramerization | 63 | 45 | 21 | 40 | 1 | 0 | 1 | 0 |  | 1 |
| GO:0051290 protein heterotetramerization | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0070206 protein trimerization | 4 | 4 | 3 | 1 | 0 | 0 | 0 | 0 |  | 0 |
| GO:0070207 protein homotrimerization | 12 | 10 | 5 | 5 | 1 | 0 | 0 | 0 | NEW 1 | 2 |
| GO:0034214 protein hexamerization | 11 | 8 | 5 | 6 | 0 | 0 | 0 | 0 |  | 0 |

What stands out:

- **The ACCEPT/KEEP split is between genes, not within them.** On
  GO:0042803, 191 genes have ACCEPT rows and 215 have KEEP_AS_NON_CORE rows,
  and no gene has both. Each reviewer applied one convention to all of a
  gene's rows, but reviewers did not share one. ACCEPT means "core function",
  so roughly 190 reviews call homodimerization a core function of their gene.
  42 name it in `core_functions`, among them ARATH BRI1, PIN1 and UVR8, human
  IRF3, HMOX1 and ERN1.
- **Reviews refine the generic term into the specific ones.** 31 genes have
  GO:0046983 MODIFY rows. Of the 35 rows, 17 go to homodimerization, 15 to
  heterodimerization and 3 to both. They are mainly MADS-box and bHLH
  transcription factors (ARATH SEP1-4, SOC1, SVP, MUTE; DANRE hes6; DROME
  tgo; HORSE MITF) and bacterial enzymes. That is the opposite direction
  from the 2021 consensus.
- **GO:0042802 is the one to keep, and it is everywhere.** 2203 rows on 952
  genes, split 925 ACCEPT and 907 KEEP_AS_NON_CORE. Any migration from
  homodimerization to identical protein binding lands in a term the repo
  already treats inconsistently.
- **This is a protein-binding-policy gap.** The repo's
  `protein_binding_policy.py` covers bare GO:0005515 only. Nothing in
  `CLAUDE.md` or the validators says how to treat dimerization or
  identical-protein-binding rows.

## What gene review can and cannot settle

- **Can settle, per row:**
  - whether the evidence shows a dimer, a larger oligomer or just
    self-association;
  - whether the oligomeric state is required for the gene's real activity
    (a dimeric enzyme active site, an obligate receptor dimer, a
    dimerization-dependent transcription factor);
  - what the informative MF is.

  This is the migration mapping the 2021 consensus needs. It is also what a
  repo convention needs.
- **Can supply:** a sample of the 42 core-function uses with their
  justification. That is the strongest case anyone has made for keeping the
  terms, and it is the evidence the pro-retention side would want counted.
- **Cannot settle:** obsoletion. That is consortium policy.

## Plan

- [ ] Draft a repo convention, for discussion with the maintainers, before
      changing any review: dimerization MF rows are KEEP_AS_NON_CORE unless
      the oligomeric state is the gene's mechanism, and are never the
      `core_functions` MF when a catalytic or binding MF exists.
- [ ] Sample 40 ACCEPT and 40 KEEP_AS_NON_CORE homodimerization rows. Record
      the stoichiometry evidence and the gene's informative MF. Estimate how
      many ACCEPTs survive the draft convention.
- [ ] Review the 42 `core_functions` uses one by one.
- [ ] Audit the 35 GO:0046983 MODIFY rows. Would plain GO:0046983 (or
      GO:0042802 with a partner) have been more consistent with upstream
      direction?
- [ ] Summarise the sample for the issue owners. Posting it is the project
      lead's decision.

## STATUS

- 2026-11-16: project scoped from the GO tracker backlog. No edits started.

## NOTES

### 2026-11-16

- Created from the [GO tracker backlog](GO_TRACKER_BACKLOG.md). Both
  threads read in full.
- Tagged PIPELINE as well as OBSOLETION, because the first deliverable is a
  repo convention, not gene curation.
