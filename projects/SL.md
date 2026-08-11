---
title: "UniProt Subcellular Locations (SL) Unique Terms Project"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human, mouse, yeast, SCHPO, worm, DICDI]
---

# UniProt Subcellular Locations (SL) Unique Terms Project

## Overview

The localization counterpart to [SPKW](SPKW.md). Where SPKW reviewed GO annotations derived
solely from UniProt **keywords** (`GO_REF:0000043`), this project reviews annotations derived
solely from UniProt **subcellular locations** (`GO_REF:0000044`) — SL-xxxx identifiers mapped
to GO cellular-component terms, with no corroborating experimental, phylogenetic, or curator
evidence behind them.

Two things make this worth a project of its own rather than a subproject of SPKW.

**It is still running.** GOA retired the SPKW pipeline for cellular organisms around April
2026, which closed that problem at the source. `GO_REF:0000044` is live and is one of the
largest single sources of CC annotation in GOA.

**The source identifier is in the data.** SPKW's methodology had to reverse-map GO terms to
their originating keywords through the external2go `keyword2go` file, because the GAF records
only the GO term. The SL pipeline writes `UniProtKB-SubCell:SL-xxxx` straight into the
WITH/FROM column. The location-level view that took SPKW a separate mapping step is available
for free, per annotation.

## Key finding: the failure is granularity, not truth

Across 1,297 reviewed SL-unique annotations in this corpus (986 gene folders), **41% were
downgraded or worse** and **10% carry a hard issue** (`REMOVE` / `MARK_AS_OVER_ANNOTATED` /
`MODIFY`). But the issue rate is not spread evenly, and the pattern is sharp:

| SL location | Reviewed | Issue rate | | SL location | Reviewed | Issue rate |
|---|---|---|---|---|---|---|
| SL-0171 Mitochondrion membrane | 13 | **31%** | | SL-0097 ER membrane | 36 | **0%** |
| SL-0066 Cilium | 12 | **25%** | | SL-0134 Golgi apparatus membrane | 21 | **0%** |
| SL-0162 Membrane | 61 | **28%** | | SL-0151 Late endosome membrane | 18 | **0%** |
| SL-0147 Endomembrane system | 10 | **20%** | | SL-0071 Clathrin-coated vesicle membrane | 18 | **0%** |
| SL-0090 Cytoskeleton | 59 | **27%** | | SL-0091 Cytosol | 13 | **0%** |
| SL-0132 Golgi apparatus | 23 | **17%** | | SL-0158 Lysosome | 10 | **0%** |
| SL-0243 Secreted | 89 | **15%** | | SL-0182 Nucleus membrane | 10 | **0%** |

The cleanest demonstration is within a single organelle:

| SL location | Reviewed | Issue rate |
|---|---|---|
| SL-0171 Mitochondrion **membrane** | 13 | 31% |
| SL-0168 Mitochondrion **inner** membrane | 19 | 11% |
| SL-0170 Mitochondrion **matrix** | 14 | 7% |

(The SL-0162 and SL-0090 rates include the batches reviewed under their own subprojects; the
pre-batch figures were 23% and 17%.)

Same organelle, same pipeline, same curators. The under-specified location is three to four
times worse. The pattern repeats for Golgi apparatus (17%) versus Golgi apparatus membrane
(0%), endoplasmic reticulum (10%) versus ER membrane (0%), and bare Membrane (28%) versus
every specific membrane in the table (0%).

**This is a different failure mode from SPKW.** SPKW's problems were semantic — process
conflation, regulatory conflation, expression mistaken for function. The gene was in the wrong
place in a pathway. SL's problem is that an under-specified location maps to a GO term that is
*true but uninformative*, and reviewers then have to adjudicate whether "true but
uninformative" counts as over-annotation. Hence the unusually high `KEEP_AS_NON_CORE` share
(406 of 1,297, 31%) alongside a modest hard-issue rate.

## The redundancy hypothesis, tested and refuted

The obvious mechanical explanation, and the fix this project first proposed: SL-unique
annotations get flagged because the gene *already carries a more specific term from another
source*, so the broad SL term is pure duplication. If that were right, GOA could suppress an
SL-derived CC annotation whenever a descendant is present from any other reference, and most
of the problem would disappear.

It was tested directly (`projects/SL/scripts/sl_redundancy.py`, committed). For every
SL-unique annotation, the script asks whether any other CC term on that gene is a proper
descendant under `is_a`/`part_of`, and cross-tabulates against the reviewer's verdict.

**The hypothesis fails.** Measured before this project's own review batches:

| Group | n | Issue rate | `KEEP_AS_NON_CORE` |
|---|---|---|---|
| Redundant — more specific term already present | 445 | **10%** | 31% |
| Not redundant — the SL term is the most specific the gene has | 852 | **8%** | 32% |

Two percentage points. And the split barely moves inside individual locations either
(SL-0162: 26% vs 19%; SL-0090: 17% vs 17%; SL-0171: 33% vs 25%). Redundancy is also not
tracking breadth in the way the story needs: spindle is 88% redundant with an 8% issue rate,
chromosome 83% redundant with 6%.

The reviewer quotes explain why. Genes were flagged for *vagueness*, not duplication —
"marked over-annotated for lack of specificity rather than for lack of membrane association"
(human ABHD14A), "not wrong, but 'membrane' is the uninformative parent" (yeast DCV1). A gene
whose only annotation is `membrane` is as uninformatively annotated as one with `membrane`
plus five specific terms, arguably worse. Deduplication fixes the second case and misses the
first.

**So there is no cheap structural fix.** This is an evidential judgment about whether a
location says anything, and it has to be made per annotation.

*Caveat on re-running the numbers:* the table above is the pre-intervention measurement.
Re-running the script now returns 12% vs 8%, because the [SL-0162](SL/SL-0162-MEMBRANE.md) and
[SL-0090](SL/SL-0090-CYTOSKELETON.md) batches deliberately selected redundant cases to
re-review. That is a self-fulfilling measurement and should not be quoted as a result.

## Failure-mode patterns

Four patterns, established across the subprojects. The first is the SL pipeline's own; the
others have SPKW analogues.

| Pattern | Description | Examples | SPKW analogue |
|---|---|---|---|
| **A. Under-specification** | Term is true and adds no information over the gene's topology or existing annotations | `membrane` for a known ER protein; `cytoskeleton` for a microtubule protein; `mitochondrial membrane` for an inner-membrane protein | none — this is SL's own |
| **B. Association ≠ residence** | Protein binds or anchors to the structure but is not located in it | SGCA, SGCE (sarcolemmal proteins linked to cytoskeleton via the DGC) | regulatory conflation |
| **C. Family-rule propagation** | A location true of some family members is attached to all by a HAMAP/UniRule rule or a sequence feature | PSEPK and METEA enolase (`Secreted` from pathogen moonlighting); yeast THI22 (signal-peptide prediction); human PGRMC1 | subclade divergence |
| **D. Transit annotated as destination** | Protein passes through a compartment to reach a tethered, injected or embedded destination | SALTY slrP (T3SS effector); STAAU lytN (cross-wall); ACET2 SdbA (SLH-tethered) | toxin vs effector |

### Sweep: do any flagged cases need terms that do not exist?

After the [GO:0034045 audit](CONDENSATES/GO_0034045-annotation-audit.md) found three genes
wrongly parked at `ACCEPT` because their destination did not exist, the whole SL flagged set
was swept for the same mistake. The test: a flagged SL-unique annotation with no
`proposed_replacement_terms` and no more-specific CC term anywhere on the gene — "stranded".

42 annotations are stranded, but **almost none are missing-term cases.** They are stranded
because the protein is *not in the compartment at all*, which `REMOVE` and
`MARK_AS_OVER_ANNOTATED` express correctly — human PGRMC1 has no extracellular pool, METEA and
PSEPK enolase are not secreted, yeast THI22 is a signal-peptide prediction. There is no
destination because there is nothing to relocate.

Two corrections came out of the sweep, both in the other direction — a destination existed and
was not used:

- **rat Tp53** `GO:0005759` mitochondrial matrix. The review's own text named the outer
  mitochondrial membrane, but the verdict was `MARK_AS_OVER_ANNOTATED` with no replacement.
  `GO:0005741` exists and the gene lacks it; upgraded to `MODIFY`.
- **Pattern B** was described on the [cytoskeleton page](SL/SL-0090-CYTOSKELETON.md) as parked
  pending a policy decision about `located_in` semantics. It was not parked: SGCA and SGCE
  were already `MODIFY` to `GO:0016010` and `GO:0042383`. A protein associating with the
  cytoskeleton *through a named complex* can be annotated to the complex. Page corrected.

**So the missing-term situation is specific to SL-0221**, where the target GO term is itself
defective and the replacements (phagophore membrane, phagophore rim, ER-phagophore contact
site) genuinely do not exist and are now proposed on the ATG2A, ATG2B and atg-18 reviews.
Everywhere else in the SL corpus, the destination exists — the question is only whether the
reviewer looked for it.

### Pattern C has a mirror image: the reviewer's family argument over-reaches too

A blinded OpenScientist run on yeast **THI22** (`genes/yeast/THI22/THI22-hypotheses/`,
pre-registered in `THI22-notes.md` before the result) tested the SL-0243 `Secreted` annotation
neutrally. It confirmed the verdict — no evidence places THI22 outside the cell — but refuted
the reasoning behind it, and the refutation generalises.

This review had argued: *THI22's paralogs THI20/THI21 are cytosolic, so secretion is
implausible, so the annotation is over-annotated.* The run reproduced the key sequence fact
blind — the N-terminal extension is unique to THI22 among the three paralogs, hydropathy peak
3.78 vs ~0.5–0.8 — and then read it the **opposite** way: uniqueness is evidence of
neofunctionalization toward the endomembrane system, not evidence that THI22 behaves like its
sisters. SGD's locus record (verified against the SGD API) reports ER and vacuole localization
for SWAT-GFP and mCherry fusions. The prediction's error is the **endpoint, not the signal** —
entering the secretory pathway is not being secreted.

The lesson for this project: *"family members are secreted, so this one is"* (pattern C) and
*"family members are cytosolic, so this one is"* are the same inference pointed in opposite
directions, and a reviewer refuting the first can commit the second. Family context constrains
a localization; it does not determine it, and the case where a protein diverges from its
paralogs is exactly the case worth annotating. Verdicts reached by paralog analogy alone should
say so explicitly, so the reasoning can be checked separately from the conclusion.

Pattern C is the one with a targeted fix: auditing the handful of family rules that attach
`Secreted`/`Cell surface` to housekeeping enzyme families would remove a disproportionate
share of the *wrong* (as opposed to merely vague) annotations. HAMAP MF_00318 on enolase
alone accounts for two of the 13 SL-0243 flags in this small corpus and would account for far
more at GOA scale.

Full tables and the query in [SL-METHODOLOGY.md](SL/SL-METHODOLOGY.md), regenerable from a
committed script.

## Subprojects

| Subproject | SL | Reviewed | Issue rate | Status |
|---|---|---|---|---|
| [Membrane](SL/SL-0162-MEMBRANE.md) | SL-0162 | 61 | 28% | 3 annotations moved; pattern A |
| [Cytoskeleton](SL/SL-0090-CYTOSKELETON.md) | SL-0090 | 59 | 27% | 6 annotations moved; patterns A + B |
| [Secreted](SL/SL-0243-SECRETED.md) | SL-0243 | 89 | 15% | analysis only; patterns C + D |
| [Mitochondrial granularity triple](SL/SL-MITOCHONDRIA.md) | SL-0171/0168/0170 | 46 | 31/11/7% | controlled comparison; analysis only |
| [SL-0221 / phagophore assembly site membrane](CONDENSATES/GO_0034045-annotation-audit.md) | SL-0221 | 29 | — | 18 annotations moved; feeding GO issue #29437 |

### SL-0221: a third failure mode

`SL-0221 Preautophagosomal structure membrane` → `GO:0034045` is neither a semantic error nor
a granularity error. **The target GO term is logically defective**: it asserts via
`bounding_layer_of` that a membrane bounds the phagophore assembly site, which is a protein
condensate with no bounding bilayer.

This case is documented in full in the
[GO:0034045 corpus slice audit](CONDENSATES/GO_0034045-annotation-audit.md), shared with the
[CONDENSATES](CONDENSATES.md) project. Its lessons for SL generally:

- **UniProt's own hierarchy is not the problem.** SL-0221 is `partOf` the endomembrane system,
  never `partOf` SL-0220 (the PAS itself). The containment that creates the contradiction is
  GO's addition, not UniProt's.
- **The mapping amplifies whatever it is given.** SL-0221 drives ~801 IEAs under
  `GO_REF:0000044`, plus everything derived from it via Ensembl projection
  (`GO_REF:0000107`), ARBA (`GO_REF:0000117`) and TreeGrafter (`GO_REF:0000118`). This corpus
  holds both ends of one such chain: human RAB7A's annotation is a projection of mouse Rab7a's.
- **SL-unique annotations are where the mapping is unchecked.** Every one of the 23 previously
  reviewed GO:0034045/GO:0097632 assertions in this corpus had been `ACCEPT`ed. Re-reviewed
  against the ontology defect, 18 of 29 moved to `MODIFY`.

## What the subprojects established

- **The granularity signal is real and large** — 28% on `membrane`, 27% on `cytoskeleton`,
  31% on `mitochondrial membrane`, against 0% on every precise membrane term in the corpus.
- **But it is not redundancy**, so it cannot be automated away (above).
- **Precision does not reduce errors; it makes them visible.** The mitochondrial triple's
  precise siblings still fail at 7-11%, but they fail *informatively*: a wrong sub-compartment
  (SCHPO tim10, rat Tp53) or, in one case, a wrong organelle entirely (ARTAN A0A2U1PS28,
  a chloroplastic protein annotated to the mitochondrial inner membrane). Vague terms cannot
  be wrong in that way, which is the problem with them.
- **Two of the four patterns are inherited from SPKW**, which suggests the underlying cause is
  the family-rule and prediction layer shared by both pipelines rather than anything specific
  to keywords or locations.

## Open questions

- Is `KEEP_AS_NON_CORE` the right disposition for a true-but-uninformative location, or should
  the project argue for a distinct verdict? A third of all SL-unique annotations land there.
- ~~Should GOA suppress an SL-derived CC annotation when the gene already carries a more
  specific descendant from any source?~~ **Tested and refuted** (above): it would address
  almost nothing. What *would* help is harder — a judgment about whether a location is
  informative for a given protein, which is not derivable from the annotation graph.
- Should GO's `located_in` be usable at all for peripheral association (pattern B), or does
  that need a different relation? SGCA and SGCE are the test cases.
- How many SL locations map to GO terms whose logical axioms do not hold for the structure the
  location names? SL-0221 was found by accident. There is no systematic check.
- Does the issue rate hold outside this corpus? These 986 genes were selected for review for
  other reasons and are not a random sample of GOA.

## Project status

- **Started**: 2026-08-08
- **Corpus scan**: 1,300 SL-unique annotations, 986 gene folders, 1,297 with reviews
- **Genes reviewed under this project**: 22 — 11 for SL-0221, 5 for SL-0162, 6 for SL-0090
- **Annotations moved**: 29 — 18 under SL-0221, 11 under SL-0162/SL-0090
- **Scripts**: `projects/SL/scripts/scan_sl_unique.py`, `projects/SL/scripts/sl_redundancy.py`
