---
title: "GO Tracker Backlog: Old Open Ontology Issues That Gene Review Can Move"
maturity: SCOPING
tags: [PIPELINE]
collections: [GO_TRACKER_BACKLOG]
---

# GO Tracker Backlog: Old Open Ontology Issues That Gene Review Can Move

**Bottom line:** The GO ontology tracker (geneontology/go-ontology) had 625
open issues on 2026-11-16, and 323 of them were opened before 2023. After
dropping build, QC, mapping, relation and documentation issues, 242 concern
the meaning or structure of terms. Of these, 125 name a GO term that at
least one gene reviewed in this repo carries. We read 24 of them in full and
grouped them into eleven projects. Each one stalled on a question about what
annotated gene products actually do, which gene review can answer:

- is this a molecular function or a process?
- is this row a phenotype?
- which specific complex does each annotation belong in?

Every project is scoped only. None has started curation. The full
catalogue, with each issue's terms and their footprint in this repo, is
[`backlog.yaml`](GO_TRACKER_BACKLOG/backlog.yaml). It is rebuilt by a
script. Nothing has been posted, labelled or otherwise changed on the
tracker.

## Projects

| Project | Tracker issues (opened) | What stalled it | Footprint here |
|---|---|---|---|
| [ACTIN_DYNAMICS_MF_REFACTORING](ACTIN_DYNAMICS_MF_REFACTORING.md) | [18437](https://github.com/geneontology/go-ontology/issues/18437) (2019), [18555](https://github.com/geneontology/go-ontology/issues/18555), [18609](https://github.com/geneontology/go-ontology/issues/18609), [19185](https://github.com/geneontology/go-ontology/issues/19185) (2020), [22594](https://github.com/geneontology/go-ontology/issues/22594) (2021) | severing and cross-linking MFs exist, but the process terms were never migrated; nucleator and polymerase MFs await design decisions | 94 rows, 50 genes |
| [DETECTION_OF_STIMULUS_MF](DETECTION_OF_STIMULUS_MF.md) | [18097](https://github.com/geneontology/go-ontology/issues/18097), [18098](https://github.com/geneontology/go-ontology/issues/18098) (2019), [20133](https://github.com/geneontology/go-ontology/issues/20133) (2020), [23137](https://github.com/geneontology/go-ontology/issues/23137) (2022) | sensor activity or multi-gene process? still disputed in 2026 | 307 rows, 159 genes |
| [PROTEIN_DIMERIZATION_TERMS](PROTEIN_DIMERIZATION_TERMS.md) | [11094](https://github.com/geneontology/go-ontology/issues/11094) (2014), [13036](https://github.com/geneontology/go-ontology/issues/13036) (2017) | rough consensus to retire the terms, never ratified | 615 rows, 463 genes (homodimerization) |
| [FATTY_ACID_ELONGATION_TERMS](FATTY_ACID_ELONGATION_TERMS.md) | [10773](https://github.com/geneontology/go-ontology/issues/10773) (2013) | biosynthesis versus elongation axes never reconciled | 534 rows, 132 genes |
| [CELL_PERIPHERY_DEFINITIONS](CELL_PERIPHERY_DEFINITIONS.md) | [14909](https://github.com/geneontology/go-ontology/issues/14909) (2018), [23429](https://github.com/geneontology/go-ontology/issues/23429) (2022) | definitions of cell surface and cell cortex | 523 rows, 289 genes (surface); 168 rows, 119 genes (cortex) |
| [PROTEIN_STABILITY_TERMS](PROTEIN_STABILITY_TERMS.md) | [20833](https://github.com/geneontology/go-ontology/issues/20833), [16360](https://github.com/geneontology/go-ontology/issues/16360) (2018) | is "protein stabilization" a process or a phenotype? usage guidelines never written | 231 rows, 155 genes (stabilization) |
| [PROTEIN_BINDING_SUBTYPE_TERMS](PROTEIN_BINDING_SUBTYPE_TERMS.md) | [14601](https://github.com/geneontology/go-ontology/issues/14601) (2017), [16186](https://github.com/geneontology/go-ontology/issues/16186) (2018), [20873](https://github.com/geneontology/go-ontology/issues/20873) (2021) | 2019 decision to remove family and partner binding terms, only partly done | 172 rows, 109 genes |
| [CYTOLYSIS_TERMS](CYTOLYSIS_TERMS.md) | [13041](https://github.com/geneontology/go-ontology/issues/13041) (2017) | 2017 plan half done; "Can we go ahead with this?" unanswered since 2020 | 104 rows, 51 genes |
| [UPR_RIDD_AND_ER_QC](UPR_RIDD_AND_ER_QC.md) | [14380](https://github.com/geneontology/go-ontology/issues/14380) (2017), [20914](https://github.com/geneontology/go-ontology/issues/20914) (2021) | no RIDD term; UPR still classed as signaling | 88 rows, 49 genes (ER UPR) |
| [CHROMATIN_SILENCING_COMPLEX_OBSOLETION](CHROMATIN_SILENCING_COMPLEX_OBSOLETION.md) | [19574](https://github.com/geneontology/go-ontology/issues/19574) (2020) | obsolete, merge or rename? | 24 rows, 17 genes |
| [RNAP_II_HOLOENZYME_OBSOLETION](RNAP_II_HOLOENZYME_OBSOLETION.md) | [10556](https://github.com/geneontology/go-ontology/issues/10556) (2013) | the consider-term dispute and the GO:0005665 logical definition | 1 row; 28 on the subcomplexes |

Two more old issues are already covered by an existing project:
[go-ontology#14275](https://github.com/geneontology/go-ontology/issues/14275)
(receptor ligand agonist/antagonist activity) and
[go-ontology#15477](https://github.com/geneontology/go-ontology/issues/15477)
(interferon-gamma signaling start and end), both in
[LIGANDS_IN_SIGNALING](LIGANDS_IN_SIGNALING.md).

"Footprint" is the number of `existing_annotations` rows, and of reviews,
on the issue's main terms. It was computed on 2026-11-16 with
[`term_actions.py`](GO_TRACKER_BACKLOG/term_actions.py). Each project page
has the full per-term table, broken down by review action.

## How the backlog was built

1. **Issues.** Every open issue created before 2023-01-01, fetched read-only
   from the GitHub search API on 2026-11-16. The command is in
   [`build_backlog.py`](GO_TRACKER_BACKLOG/build_backlog.py)'s docstring.
   The raw payload is not committed.
2. **Scope.** Issues with any of these labels were marked NON_CONTENT:
   Infrastructure, QC, documentation, enhancement, relations, xref &
   mappings, subsets, go2rhea, ontology alignment. That left 242 CONTENT
   issues.
3. **Terms.** GO ids written in each title or body were resolved against
   go-edit.obo (checkout of 2026-11-12), with alt_ids merged. Each was tagged
   CURRENT, OBSOLETE or MISSING.
4. **Footprint.** For each term, and for the term with its is_a/part_of
   descendants: how many genes under `genes/` have a GOA row for it, and how
   many of those are reviewed.
5. **Coverage.** Which project pages under `projects/` link to the issue.
   This is how the catalogue knows which issues have a project.

Regenerate with:

```bash
python projects/GO_TRACKER_BACKLOG/build_backlog.py \
  --issues issues.jsonl --obo ../go-ontology/src/ontology/go-edit.obo \
  --out projects/GO_TRACKER_BACKLOG/backlog.yaml
```

### The old content backlog in numbers

| Opened | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Content issues still open | 2 | 1 | 2 | 5 | 20 | 39 | 28 | 50 | 46 | 49 |

- 125 of the 242 name a term on at least one reviewed gene, 75 on at least
  ten, and 22 on at least a hundred.
- The most common labels are PomBase (41), obsoletion (40), multi-species
  process (36), New term request (28) and targeting and transport (22).
  MF_in_BP, the label for process terms that describe a single activity,
  has 18.
- 149 show no update since 2022. GitHub's "updated" date also moves on label
  changes, so this undercounts how many have had no discussion.

## How projects were chosen

The footprint number alone is a poor guide. An issue that mentions
`plasma membrane` in passing (#20359, spore membrane) or `mitochondrion`
(#16785, spatial relations) scores in the thousands but has nothing for gene
review to settle. Projects were made where reading the thread showed all
three of these:

1. **The blocker is about gene products.** Is the activity done by one
   protein? Is the row a phenotype? Which complex is it?
2. **The answer is already partly in this repo,** in reviews that carry the
   terms, often applied inconsistently. That makes the first step an audit,
   not new curation.
3. **The issue is not already resolved in go-edit.obo.** Where part of it
   was resolved, as with severing activity or the ERAD consolidation, the
   project is scoped to what remains.

Related issues were grouped when they share the same blocker.

## Next candidates (not yet read in full)

These scored well on footprint and look tractable from their title, labels
and opening text. Each needs its thread read before it becomes a project.

| Issue | Opened | Topic | Why it may fit |
|---|---|---|---|
| [15238](https://github.com/geneontology/go-ontology/issues/15238) | 2018 | NTR telomerase complex assembly (45 comments) | assembly factors are gene-specific evidence |
| [23997](https://github.com/geneontology/go-ontology/issues/23997) | 2022 | merge protection from NHEJ at telomere into telomere capping (labelled ready) | 14 reviewed genes carry the terms |
| [15821](https://github.com/geneontology/go-ontology/issues/15821) | 2018 | CDK/cyclin complex terms | 29 reviewed genes carry the complex terms |
| [21053](https://github.com/geneontology/go-ontology/issues/21053) | 2021 | tail-anchored protein insertion vs post-translational ER targeting | 18 reviewed genes |
| [19963](https://github.com/geneontology/go-ontology/issues/19963) | 2020 | NTR ATPase coupled to Fe-S cluster translocation (Needed for GO-CAM) | fits [IRON_SULFUR_CLUSTER_BIOGENESIS](IRON_SULFUR_CLUSTER_BIOGENESIS.md) |
| [16565](https://github.com/geneontology/go-ontology/issues/16565) | 2018 | obsolete cellular response to methyl methanesulfonate | DNA damage response genes; PomBase |
| [21284](https://github.com/geneontology/go-ontology/issues/21284) | 2021 | obsolete cellular response to oxygen-glucose deprivation (labelled ready) | 5 reviewed genes; small |
| [23300](https://github.com/geneontology/go-ontology/issues/23300) | 2022 | obsolete glycoside metabolic process branch (labelled ready) | 5 reviewed genes; small |
| [18072](https://github.com/geneontology/go-ontology/issues/18072), [19347](https://github.com/geneontology/go-ontology/issues/19347) | 2019-2020 | response to fungus and oomycete terms | 80 and 52 reviewed genes; overlaps [PLANT_FUNGAL_INTERACTIONS](PLANT_FUNGAL_INTERACTIONS.md) |
| [21283](https://github.com/geneontology/go-ontology/issues/21283), [22996](https://github.com/geneontology/go-ontology/issues/22996) | 2021-2022 | nutrient and starvation response terms (PomBase) | 76 and 41 reviewed genes |
| [15826](https://github.com/geneontology/go-ontology/issues/15826) | 2018 | NTR N-hydroxypipecolic acid biosynthesis (31 comments) | plant immunity enzymes |
| [22455](https://github.com/geneontology/go-ontology/issues/22455), [22274](https://github.com/geneontology/go-ontology/issues/22274), [23596](https://github.com/geneontology/go-ontology/issues/23596) | 2021-2022 | MF_in_BP: regulation of molecular function, proteolysis, Golgi retention | same pattern as the actin and detection projects |

## Working conventions for these projects

- **Read-only on the tracker.** No comments, labels, reactions or
  assignments on the issues. Whether and when to share a project's findings
  with an issue's owners is the project lead's decision.
- **No backlinks by accident.** GitHub adds a timeline entry to an issue
  when a commit message, PR description or PR comment mentions it. Links
  inside committed files do not. Keep go-ontology issue numbers and URLs out
  of commit messages and PR text for this work.
- **Thread summaries are dated.** Each page states the date its summary was
  read (2026-11-16) and the go-edit.obo checkout it was checked against
  (2026-11-12). Re-read the thread before acting on a page that is more than
  a few weeks old.
- **Evidence, not resolution.** Each page separates what gene review can
  settle from what remains an editor decision.

## STATUS

- 2026-11-16: catalogue built (323 issues, 242 content). Eleven projects
  scoped, covering 24 issues, all read in full. Two more old issues were
  already covered by LIGANDS_IN_SIGNALING. No curation started.

## NOTES

### 2026-11-16

- The 24 threads were read by AI agents working read-only, who also checked
  term states in go-edit.obo. Their reported states were re-checked against
  the edit file. The quotations used on the project pages were checked by
  exact-phrase tracker search.
- #14601 (kinase binding parentage) on its own needs no gene review. It is
  attached to PROTEIN_BINDING_SUBTYPE_TERMS as the record of the 2019
  decision.
- #20133 is effectively a duplicate of #18097. It is listed with the
  detection project for completeness.
