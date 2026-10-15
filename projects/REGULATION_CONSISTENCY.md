---
title: "Regulation of X: Consistency and Meaning"
maturity: SCOPING
tags: [PIPELINE, EVALUATION]
species: [human]
---

# Regulation of X: Consistency and Meaning

**Bottom line:** a third of GO biological-process terms and 31% of human BP
annotation rows are "regulation of X". This project audits how consistently
they are used. The first pass covers GOA human and the 7,168 existing reviews.
It finds three recurring patterns that are worth triaging:

- a gene annotated both to X and to regulation of X (5,167 gene–process pairs);
- a gene annotated to both positive and negative regulation of the same X
  (1,242 pairs);
- unsigned "regulation of X" sitting alongside a signed term for the same X
  (2,220 pairs).

Can we work out after the fact what a "regulation of X" row means? Partly.
Reviewers' MODIFY replacements tell us directly in about 1,000 cases. Simple
rules flag likely misfiled participants: rows the rules put in the
misfiled-participant bucket were modified to the participant term 7.9% of
the time, against at most 0.5% for rows with no participant co-annotation. Most rows
are still kept as they are, so the rules can rank a review queue but cannot
rewrite annotations automatically. The companion enrichment eval in
`monarch-initiative/genesets`
([`evals/regulation_closure`](https://github.com/monarch-initiative/genesets/tree/main/evals/regulation_closure))
asks what the same choices cost in enrichment analysis.

## Why regulation terms are noisy

GO separates participating in X from regulating X. Real annotation does not
always keep them apart:

- **Participant misfiled as regulator.** A core component of a pathway is
  annotated to *positive regulation of* that pathway because knocking it down
  lowers the output. Necessity evidence cannot tell a component from an
  upstream activator (see "Do not add what curators deliberately declined to
  add" in `CLAUDE.md`).
- **Readout-driven sign.** IMP/IGI rows record the sign of a phenotype
  readout, which depends on cell type, dose and the assay window. Both signs for
  the same X often mean two papers measured different contexts, not that the
  gene has two activities. The Drosophila LKB1–AMPK reviews contain the
  reverse case: *positive regulation of TORC1 signaling* (IMP) corrected to
  *negative* by the reviewer.
- **Indirect, via gene expression.** A transcription factor gets "regulation of
  X" for every X its targets affect.
- **Ontology structure.** GO places *signal transduction*, and so every
  signaling pathway, `is_a` *regulation of cellular process*. Tools that treat
  `is_a regulation` as "is a regulation term" will count all signaling as
  regulation. The script below avoids this by keying on explicit `regulates`
  edges.

## Method

[`regulation_triage.py`](REGULATION_CONSISTENCY/regulation_triage.py) is
deterministic. It takes the full `go.obo` (go-basic lacks the regulates
relations), a GAF and the `genes/` tree:

```bash
uv run python projects/REGULATION_CONSISTENCY/regulation_triage.py \
  --obo go.obo --gaf goa_human.gaf.gz --genes-dir genes \
  --out-dir projects/REGULATION_CONSISTENCY/results
```

1. **GOA triage.** For each gene and each process X targeted by a
   `regulates` / `positively_regulates` / `negatively_regulates` edge, the
   script records the signs annotated, whether the gene also participates in X
   (X itself, or a non-regulation is_a/part_of descendant), and the evidence.
   For broad grouping targets (more than 500 descendants, e.g.
   *biological_process*) only a direct annotation to X counts as
   participation.
2. **Meaning heuristics.** Each regulation row gets an ordered rule-based
   guess: `participant_misfiled_as_regulator` (co-annotated participant, + or
   unsigned, no regulator MF), `participant_with_feedback_or_modulation`,
   `indirect_via_gene_expression` (TF, X not transcription),
   `perturbation_readout` (IMP/IGI/IEP only), `direct_regulator_candidate`
   (regulator-type MF), `propagated_unclassified`, `unclassified`. The GAF
   qualifier is deliberately ignored (see "The `acts_upstream_of*` qualifier
   is noise" below).
3. **Review mine.** For every review, the script tallies the action on each
   regulation row. Each MODIFY is classified by where its replacement points:
   the participant term, the opposite sign, a signed child of an unsigned term,
   a more specific X with the same sign, a broader term, or something else.
4. **Calibration.** Reviewer decisions on human rows are cross-tabulated
   against the heuristic bucket of the same (gene, term) row.

Outputs in [`results/`](REGULATION_CONSISTENCY/results/):
`summary.yaml` (all counts), `triage_queue.tsv` (the 7,630 flagged
gene–process pairs), `review_regulation_modifications.tsv` (972 reviewer
MODIFY replacements on regulation terms) and
`review_participant_and_regulator_pairs.tsv`. The full per-row tables
(`goa_pairs.tsv`, `goa_regulation_rows.tsv`) are regenerated, not committed.

## Findings (GO 2026-07-26, goa_human 2026-05-21)

### The scale

| | count |
|---|---|
| BP terms / of which regulation terms | 23,974 / 8,342 (35%) |
| human BP annotation rows / regulation rows | 204,224 / 62,719 (31%) |
| genes with any regulation annotation | 12,280 |
| gene–process (X) pairs with a regulation annotation | 41,708 |
| … also annotated as participant in X | 5,167 |
| … both + and − regulation of X | 1,242 |
| … unsigned alongside signed | 2,220 |
| regulation rows carrying an `acts_upstream_of*` qualifier | about 4% |

The sign conflicts are concentrated in a few targets. Most are biologically
expected and only a minority are noise. *Transcription by RNA polymerase II*
(336 genes), *DNA-templated transcription* (187) and *gene expression* (127)
are dual-function transcription regulators. *Apoptotic process* (46) and
*cell population proliferation* (45) are mostly context-dependent readouts.
The genes with the most sign-conflicted targets are pleiotropic signaling
hubs: APOE (9), TGFB1 (8), SFRP1 (7), TNF (6), and miRNAs.

### What reviewers do with regulation terms

Across all reviews, reviewers treat regulation rows differently from other BP
rows. They rarely remove them; they demote them:

| action | regulation rows (21,233) | other BP rows (56,372) |
|---|---|---|
| ACCEPT | 35.6% | 47.5% |
| KEEP_AS_NON_CORE | 46.7% | 32.9% |
| MARK_AS_OVER_ANNOTATED | 6.9% | 6.8% |
| MODIFY | 4.4% | 5.5% |
| REMOVE | 1.1% | 2.1% |

Where a reviewer changed a regulation term, the replacement records what they
decided the row meant:

| replacement points to | MODIFYs |
|---|---|
| same sign, more specific X | 242 |
| signed child of an unsigned term | 239 |
| **the participant term X** (row meant participation) | 205 |
| a non-regulation process other than X | 104 |
| a different regulation term | 102 |
| **opposite sign** | 37 |
| broader term | 33 |

Examples of participant re-filing: BAK1 *positive regulation of apoptotic
process* → *mitochondrial outer membrane permeabilization*; RBX1 *positive
regulation of protein catabolic process* → *proteasome-mediated
ubiquitin-dependent protein catabolic process*; AP2S1 *regulation of
endocytosis* → *clathrin-dependent endocytosis*; ZSWIM8 *positive regulation
of miRNA catabolic process* → *target-directed miRNA degradation*.

### Can the meaning be recovered after the fact?

The calibration below covers 8,802 human rows that have both a GOA record and a
reviewer decision:

| heuristic bucket | n | ACCEPT | NON_CORE | OVER_ANN | MODIFY→participant |
|---|---|---|---|---|---|
| participant_misfiled_as_regulator | 595 | 43% | 35% | 5% | **7.9%** |
| participant_with_feedback_or_modulation | 908 | 42% | 43% | 4% | 2.0% |
| direct_regulator_candidate | 2,266 | 33% | 48% | 9% | 0% |
| unclassified | 1,161 | 28% | 56% | 7% | 0.3% |
| propagated_unclassified | 1,315 | 18% | 57% | **14%** | 0.1% |
| indirect_via_gene_expression | 1,016 | 20% | **62%** | 9% | 0% |
| perturbation_readout | 1,541 | 22% | **62%** | 9% | 0.1% |

1. **The buckets carry signal.** Co-annotation as a participant is the
   strongest predictor of a participant re-filing: 7.9% in the misfiled bucket,
   2% for other co-annotated rows, and at most 0.5% elsewhere. Perturbation-only and indirect-via-TF rows are the most often
   demoted to non-core. Propagated rows are the most often marked
   over-annotated.
2. **The signal is not strong enough to automate.** Even in the
   participant-misfiled bucket, 78% of rows were accepted or kept. In many
   cases both readings hold: a component that also limits flux through its
   pathway. Use the buckets to order work, not to rewrite annotations.
3. **The GAF qualifier does not help.** `involved_in` versus
   `acts_upstream_of*` reflects each group's annotation policy, not the
   biology (below), so the heuristics ignore it.

## Deep dive: genes annotated to both X and regulation of X

[`x_and_rox.py`](REGULATION_CONSISTENCY/x_and_rox.py) dissects the 5,167
human gene–process pairs (3,044 genes) where a gene has a participant
annotation to X, or to a part or subtype of X, and a regulation-of-X
annotation. The pairs are in
[`results/x_and_rox_pairs.tsv`](REGULATION_CONSISTENCY/results/x_and_rox_pairs.tsv)
and the counts in
[`results/x_and_rox_summary.yaml`](REGULATION_CONSISTENCY/results/x_and_rox_summary.yaml).

**Shape of the problem.** 55% of pairs annotate X itself; the rest reach X
through a part or subtype. Signs: 40% positive only, 35% unsigned only, 14%
negative only, and the remainder mixed. The largest targets are
*transcription by RNA polymerase II* (215), *apoptotic process* (203),
*DNA-templated transcription* (199) and *cell migration* (166). For the
transcription targets, many pairs are general transcription machinery (TAFs,
Mediator, preinitiation-complex factors). These are annotated to initiation or
PIC assembly, which are part of transcription, and also to *regulation of
transcription by RNA polymerase II*. That is partly an ontology question:
whether core machinery "regulates" the process it executes.

**Patterns** (ordered rules, first match wins):

| pattern | pairs | rule |
|---|---|---|
| own_activity_is_step_of_x | 707 | the gene's own MF reaches X via is_a/part_of, or it is an enzyme and X is a metabolic/modification process (PTGS2 → *positive regulation of prostaglandin biosynthesis*; STUB1 → *positive regulation of protein ubiquitination*) |
| same_paper_both_readings | 609 | one reference supports both rows; the curator asserted both readings at once |
| inhibitor_also_participant | 690 | only negative regulation of X, plus participation in X (CLU, a complement inhibitor, also annotated to *complement activation*) |
| mixed_sources | 1,325 | one side is phylogenetic or electronic and the other is not |
| activator_with_regulator_activity | 999 | gene has a regulator-type MF (enzyme regulator, TF, …) |
| component_as_activator | 837 | the rest: a participant also annotated as a positive or unsigned regulator |

**What reviewers did.** 1,288 pairs have reviewer decisions on both sides.
Reviewers kept both readings in about 74% of them. These pairs are mostly
not contradictions: a gene can be part of X and also limit or tune its rate.
The disagreements are informative, though:

| | kept participant only | kept regulation only |
|---|---|---|
| GO-CAM places the gene's activity *part of* X (134 reviewed) | **37** | **1** |
| inhibitor_also_participant (188) | 15 | **40** |
| own_activity_is_step_of_x (148) | **27** | 16 |
| all other patterns | 107 | 83 |

- **GO-CAM is the best arbiter.** When a curated model places the gene's
  activity in X, reviewers essentially never keep the regulation reading
  alone. GO-CAM covers only 425 of the 5,167 pairs (311 part of X, 92
  regulates X, 22 both), so it settles about 8%.
- **For negative-only pairs, the participant claim is the weak one.** An
  inhibitor annotated as taking part in the process it inhibits is the
  mirror image of the "component misfiled as activator" case, and it is
  dropped more often.
- **When the gene's own activity is a step of X, the regulation claim is the
  weak one.** An enzyme "positively regulating" its own pathway restates
  that it catalyses a step, unless the paper shows it is rate-limiting.
- **The same paper behind both rows (721 pairs; 609 not explained by own
  activity) is a curation-practice
  issue.** Reviewers usually keep both, so this alone does not mark either
  row as wrong.

**Proposed rules for the triage queue** (draft):

1. GO-CAM places the activity part of X → keep X; the regulation row becomes
   `KEEP_AS_NON_CORE`, or `MODIFY` to X when it is redundant.
2. Negative-only regulation plus participation, no GO-CAM support for
   participation → check the participant row first, since it is the one
   reviewers drop.
3. Gene's own activity is a step of X → keep X as core; the
   positive/unsigned regulation row is `KEEP_AS_NON_CORE` unless a
   rate-limiting role is shown.
4. Transcription machinery on *regulation of transcription* → raise as an
   ontology question rather than triaging gene by gene.

## Regulation terms versus extensions, across annotation sources

Could a "regulation of X" annotation instead be a more precise statement
about *which gene* is regulated? GO already supports that through annotation
extensions. For a TF, the precise form is DNA-binding TF activity
`has_input(target gene)`, or a regulation term with a gene-product extension.
[`regulation_by_species.py`](REGULATION_CONSISTENCY/regulation_by_species.py)
compares human GOA with six MOD GAFs from the same GO release
([`results/regulation_by_species.yaml`](REGULATION_CONSISTENCY/results/regulation_by_species.yaml)):

| | human | pombe | yeast | mouse | fly | worm | Arabidopsis |
|---|---|---|---|---|---|---|---|
| regulation share of BP rows | 31% | **12%** | 14% | 31% | 18% | 21% | 15% |
| … of which transcriptional | 29% | 45% | 50% | 26% | 35% | 35% | 50% |
| … perturbation-only evidence | 18% | 41% | 55% | 21% | 56% | 55% | 36% |
| … with a gene-product extension | 5% | 5% | 7% | 3% | 1% | 7% | 0% |
| TF rows on a *non*-transcriptional regulation term | 2,922 | **45** | 219 | 5,212 | 585 | 420 | 1,036 |
| … with a gene-product extension | 1% | 2% | 0% | 0% | 0% | 1% | 0% |
| TF activity (MF) rows naming a target gene | 5% | **75%** | 9% | 5% | 3% | 1% | 0% |

**Pombe uses regulation terms sparingly, and models TF targets on the MF.**
Regulation terms make up 12% of PomBase BP rows, against 31% for human and
mouse. Half of PomBase's regulation rows are transcriptional, and almost none
put a TF on regulation of a downstream process (45 rows). Instead, 75% of
PomBase's DNA-binding TF activity rows name the target gene with `has_input`.
Human GOA does that for 5% of TF activity rows. Its 2,922 rows placing TFs on
"regulation of" a non-transcriptional process carry a target gene in 1% of
cases.

**So in human, a TF on "regulation of X" is usually a weaker, higher-level
stand-in for "this TF controls gene(s) Y that act in X".** The target gene is
almost never recorded. These rows correspond to the
`indirect_via_gene_expression` bucket above, which reviewers most often demote
to non-core. Converting them to the pombe pattern would mean finding the
targets in the source papers, which is a curation task rather than a
relabelling.

**For enrichment, though, TFs are not where the valid regulation signal
comes from.** In the genesets recuration, 145 of the 149 regulation terms
judged core or supporting regulate non-transcriptional processes:
proliferation, cell death, immune activation, the MAPK cascade, muscle
contraction. Only 8% of the contributing genes are TFs, the same rate as in
rejected regulation terms. Most of that signal comes from signaling components
and effectors. GO-CAM would express it as causal links between activities,
and a GAF can express it only with `causally_upstream_of` or
`has_regulation_target` extensions. Those are rare everywhere: under 0.5% of
human regulation rows.

Two other contrasts to follow up:

- **Pombe and yeast lean on perturbation evidence for regulation** (41% and
  55% of rows, against 18% for human). So a low regulation share does not
  mean PomBase has stricter evidence standards for these rows.
### The `acts_upstream_of*` qualifier is noise

The qualifier was meant to separate genes that take part in a process from
genes whose perturbation merely affects it, which is close to flagging
over-annotation. Each group had to choose how to apply it to phenotype-driven
annotations. MGI and TAIR default to the weaker reading; human GOA and PomBase
default to `involved_in`. The same evidence code gets a different qualifier
depending only on who made the annotation. Share of BP rows marked
`acts_upstream*`, by evidence code:

| evidence | MGI | TAIR | human GOA |
|---|---|---|---|
| IMP | 63% | 69% | 5% |
| IGI | 88% | 88% | 19% |
| IDA | 51% | 56% | 5% |
| ISO / ISS | 10% / 2% | — | — / 3% |

PomBase uses it on no regulation rows at all. The signed forms
(`_positive_effect` / `_negative_effect`) are under 0.2% of human regulation
rows. MGI also curates some human genes, and it applies the same default
there: MGI-assigned rows are about half (2,171 of 4,161) of the `acts_upstream*`
BP rows in the human file. Even within one species, the qualifier varies by
curating group.

The annotations underneath are fine. Reviewers mark `acts_upstream*` rows
over-annotated *less* often than `involved_in` rows (3.2% vs 4.3% with
perturbation evidence, 5.2% vs 8.3% otherwise; 4,482 such rows across all
reviews). In enrichment, dropping the 2,438 human gene–term pairs supported
only by `acts_upstream*` rows slightly lowers recall against the recurated
genesets gold (0.549 → 0.543). So the qualifier should be ignored in both
directions: it is not a reason to filter an annotation out, and not evidence of
what kind of role the gene plays. Whether a row is direct participation,
upstream regulation or a phenotype readout has to come from the evidence, the
gene's own activity and GO-CAM, as in the heuristics above.

## Proposed triage rules

These are draft rules for review practice. They are not yet enforced.

| pattern | default action |
|---|---|
| X and positive/unsigned regulation of X, gene is a pathway component (no regulator MF) | review: likely `MODIFY` → X, or `KEEP_AS_NON_CORE` if a flux-limiting role is documented |
| unsigned regulation of X alongside signed regulation of X | the unsigned row is entailed: `TOO_GENERAL` only if the signed row is kept in the same review |
| + and − regulation of X | check each source; keep both only if the papers show context-specific opposite effects, otherwise sign-check (37 reviewer sign flips so far) |
| perturbation-only regulation of a broad readout (proliferation, apoptosis, migration) | `KEEP_AS_NON_CORE` unless the mechanism is shown |
| TF annotated to regulation of a non-transcription process | `KEEP_AS_NON_CORE`; core function is the transcription regulator activity |

## Enrichment consequences (genesets)

The genesets benchmark was first scored as it stood (126 sets, 394 CORE
terms). On that gold, dropping regulation terms looked free, because it lost
only the gold's own regulation terms. That gold had rarely been offered
regulation-only hits, so the contested region was recurated. Candidates were
pooled symmetrically from all four variants (884 terms) and judged blind to
which variant proposed them:

| variant | recall, recurated gold (481 CORE) | precision on judged contested hits |
|---|---|---|
| current is_a/part_of | 0.549 | 0.458 |
| drop regulation terms | 0.459 | 0.356 |
| regulates closure | **0.653** | **0.462** |
| collapse regulation onto X | 0.555 | 0.400 |

- **Regulation terms are not the noise for enrichment.** Judges called 50% of
  contested regulation-term hits core or supporting, against 40% of
  participant-term hits.
- **Regulates closure gives the best recall** at unchanged precision. Collapse
  is the compact option: it matches closure on participant recall with 27%
  less output.
- This sits alongside the annotation-level noise documented above. GOA's
  regulation rows are internally inconsistent, but in aggregate they still
  carry real signal about what a gene set does. Regulates closure also
  propagates the inconsistent rows triaged here, so cleaning them should
  improve it further.

## Next steps

1. Work the `triage_queue.tsv` participant-and-regulator pairs for genes that
   already have reviews, starting with signaling-pathway targets.
2. Add GO-CAM evidence (`gocams/index.tsv`): when a model places the gene as
   an activity *part of* X, that should settle the participant reading. When it
   places the gene *causally upstream of* X, the regulation reading stands.
3. Extend to the MOD GAFs (mouse, fly, worm, yeast, Arabidopsis), where many
   of the sign flips above came from.
4. Write the triage rules into the review guidelines, and possibly into
   `action_consistency.yaml` for the unsigned/signed redundancy case.
