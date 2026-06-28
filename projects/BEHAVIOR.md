---
title: "Behaviour Annotation Project"
maturity: IN_PROGRESS
tags: [PIPELINE, FLAGSHIP]
---

# Behaviour Annotation Project

**When a knockout changes how an animal behaves, the gene gets annotated to
`behavior` (GO:0007610) — even when its molecular function lives many causal
steps upstream. This is a textbook over-annotation scenario, and this project
characterises it across the review corpus.**

## Motivation

The Gene Ontology `behavior` branch (GO:0007610) sits at the extreme
*organismal* end of the biological-process hierarchy. A behaviour is an
integrated, whole-animal output — locomotion, feeding, mating, grooming,
circadian rhythm, a fear response. Almost any perturbation that reaches the
nervous system, or that compromises development, metabolism, or basic
cell biology, can shift one of these readouts.

The annotation chain that produces a behaviour term is the same convergent,
distal pattern flagged in [ASSAY_TO_FUNCTION](ASSAY_TO_FUNCTION.md) and
[OVER_ANNOTATION_PATTERNS](OVER_ANNOTATION_PATTERNS.md):

> perturb gene **G** → animal behaves differently → annotate **G** to behaviour **B**

The evidence codes that dominate behaviour annotations (IMP from a mutant,
IGI from a genetic interaction) record that the phenotype is *real and
reproducible* — but they say nothing about how **proximal** the gene is to the
behaviour. A tubulin, a lysosomal peptidase, an angiotensin receptor, and a
ciliary scaffold can all earn a `locomotory behavior` annotation from a
phenotype assay, yet none of them is a "behaviour gene" in any mechanistic
sense. The behaviour is a downstream readout of a much more specific molecular
defect.

So the goal here is **not** to delete behaviour annotations wholesale. A
behaviour phenotype is legitimate evidence, and for a handful of genes
(neurotransmitter receptors, neuropeptides, circadian clock components) a
behaviour term genuinely is close to the core function. The goal is to
**separate the core from the consequence**: keep well-supported behaviour
annotations as **non-core** context, flag the distal ones as
over-annotations, and reserve `REMOVE` for the cases that are actually
*contradicted* (wrong paralog, wrong gene) rather than merely distal.

## What the corpus already shows

Mined with [`BEHAVIOR/mine_behavior.py`](BEHAVIOR/mine_behavior.py) over every
`*-goa.tsv` (source annotations) and every `*-ai-review.yaml` (reviewer
decisions). The full tables regenerate into
[`BEHAVIOR/reports/REPORT.md`](BEHAVIOR/reports/REPORT.md).

**Source surface.** Behaviour terms in the corpus GOA files are overwhelmingly
phenotype-driven: **IMP + IGI account for the large majority** of behaviour
annotations, with only a few IDA (direct assay) annotations. The most common
terms are the broad ones — `locomotory behavior` (GO:0007626) by a wide margin,
followed by `behavioral response to pain`, `mating behavior`, `social
behavior`, `circadian behavior`, and `adult locomotory behavior`.

**Reviewer decisions.** Of the behaviour annotations that reviewers have already
adjudicated, **~76% were downgraded** — kept as non-core, marked as
over-annotated, or removed — and only a minority were `ACCEPT`ed as a core
function:

| Action | Meaning for a behaviour term | Share |
|---|---|---|
| `KEEP_AS_NON_CORE` | Real phenotype, distal to molecular function | dominant (~60%) |
| `ACCEPT` | Behaviour genuinely near the core (e.g. receptors, clock genes) | minority |
| `MARK_AS_OVER_ANNOTATED` | Too broad / too distal to be useful | small |
| `REMOVE` | Contradicted — wrong gene/paralog or not supported | small |

This is exactly the signature of a benign-but-pervasive over-annotation
pattern: the annotations are mostly *not wrong*, but they are mostly *not core*.

## Exemplars from completed reviews

These are real decisions already in the corpus — concrete illustrations of the
"keep as non-core, it's a downstream readout" call:

- **Tuba1a** (mouse, α-tubulin) — annotated to `locomotory behavior`, `motor
  behavior`, `locomotory exploration behavior`, `adult locomotory behavior`,
  and `adult behavior`, all IMP. All five kept as **non-core**: *"Behavioral
  phenotypes are distal consequences of brain malformation caused by Tuba1a
  mutation. Not a direct function."* The molecular function is microtubule
  structure; the behaviour is the bottom of a long causal chain.

- **tpp1** (zebrafish, lysosomal tripeptidyl-peptidase) — `locomotory behavior`
  (IMP) kept **non-core**: *"The direct conserved role is lysosomal
  tripeptidyl-peptidase / proteolysis; neurodevelopmental and locomotor defects
  are downstream phenotypes."*

- **Ciliary genes** (BBS2, BBS4, MKKS, osm-5, nphp-1/4, che-2/3) — behaviour
  and chemosensory-behaviour annotations arising because cilia defects disrupt
  sensory behaviour. Adjudicated as **non-core** organismal phenotypes, e.g.
  BBS2 `adult behavior`: *"Downstream organismal phenotype, not a direct
  molecular function."*

- **Agtr1a** (mouse, angiotensin II receptor type 1a) — a `REMOVE`, not a
  downgrade: direct central-angiotensin experiments assign **drinking
  behaviour** to the paralog **AT1B**, so the AT1A annotation is *contradicted*,
  not merely distal. This is the boundary case where `REMOVE` is the right call.

The contrast between Tuba1a/tpp1 (distal → non-core) and Agtr1a (wrong paralog →
remove) is the core curation distinction this project sharpens.

## Curation guidance (working rubric)

For a `behavior` (GO:0007610-descendant) annotation, ask:

1. **Is it contradicted?** Wrong gene, wrong paralog, or the cited evidence
   actually attributes the behaviour elsewhere → **`REMOVE`**. (Verify the
   paralog/organism before claiming this — see CLAUDE.md; do not `REMOVE` an
   experimental annotation just because the cached abstract foregrounds another
   gene.)
2. **Is the gene proximal to the behaviour?** Neurotransmitter receptor,
   neuropeptide/hormone, ion channel, or circadian-clock component acting
   directly in the relevant circuit → behaviour may be near-core → **`ACCEPT`**
   or capture a more specific behaviour term.
3. **Is it a real but distal phenotype?** (the common case — structural,
   metabolic, developmental, or ciliary gene whose knockout perturbs behaviour
   indirectly) → **`KEEP_AS_NON_CORE`**, with `reason` naming the proximal
   molecular defect the behaviour is downstream of.
4. **Is the term uselessly broad** (`adult behavior`, `behavior`) **or the
   phenotype barely connected?** → **`MARK_AS_OVER_ANNOTATED`**.

The default for a phenotype-driven behaviour annotation on a
molecular/structural gene is **`KEEP_AS_NON_CORE`**, not `REMOVE`: the phenotype
is genuine data about the gene, just not its core function.

## Reproducing the analysis

```bash
uv run python projects/BEHAVIOR/mine_behavior.py \
    --genes-dir genes --out-dir projects/BEHAVIOR/reports
```

Outputs (regenerated, not hand-edited):

- `BEHAVIOR/reports/REPORT.md` — summary tables (evidence-code mix, top terms,
  reviewer-action distribution).
- `BEHAVIOR/reports/behavior_source_annotations.csv` — every behaviour
  annotation in the GOA files.
- `BEHAVIOR/reports/behavior_review_actions.csv` — every behaviour annotation a
  reviewer has adjudicated, with the action and rationale.

## Spot-check of the `ACCEPT`ed annotations

Applying the rubric to every behaviour annotation that a reviewer had `ACCEPT`ed
as a core function sorts them cleanly into genuinely-proximal cases and missed
downgrades.

**Genuinely proximal — `ACCEPT` upheld:**

- **CRY** (Drosophila) — `circadian behavior`: cryptochrome is a bona fide
  circadian-clock photoreceptor; the behaviour is the clock's direct output.
- **lov-1 / pkd-2** (C. elegans) — `male mating behavior` / `mating behavior`:
  the polycystin-1/2 sensory channels that *constitute* the male-mating sensory
  circuit; an ion channel acting directly in the relevant neurons (rubric step 2).
- **GCG** (human) — `feeding behavior`: proglucagon/GLP-1 is a neuropeptide that
  directly signals satiety to feeding circuits.
- **DpuGr29** (Daphnia) — `chemosensory behavior`: a gustatory chemoreceptor,
  the proximal transducer of the behaviour.

**Missed downgrades — corrected to `KEEP_AS_NON_CORE`:**

- **App** (mouse) — `adult locomotory behavior` / `locomotory behavior` (×5,
  IMP/IGI): "supported by knockout phenotypes" with supporting text describing
  righting difficulty, ataxia and balance deficits — a distal neurological
  readout, exactly the Tuba1a pattern.
- **STAT3** (human) — `regulation of feeding behavior` / `eating behavior` (×3,
  IEA/ISS): electronic annotations on a highly pleiotropic transcription factor;
  distal to its core JAK-STAT signalling role.
- **nphp-1** (C. elegans) — `turning behavior involved in mating` (IGI): a
  **ciliary** gene (named in this project) whose behaviour annotation's own
  reason states it is "part of the … phenotype" — a downstream consequence of
  cilium dysfunction.

This moved 9 annotations from core to non-core, raising the downgrade rate among
reviewed behaviour annotations from ~76% to **82%** (now only 19 `ACCEPT`ed as
core). **Borderline cases left as-is** (documented, not changed): `daf-2`
feeding/eating (the pleiotropic insulin receptor — feeding is one of many
outputs) and `trpm7` swimming (a channel-kinase whose swimming phenotype is
plausibly a distal developmental consequence) — defensible either way and not
clear-cut enough to overturn.

## Cross-link: behaviour is the extreme readout quadrant

[ASSAY_TO_FUNCTION](ASSAY_TO_FUNCTION.md) frames over-annotation risk on two
axes — **proximity** (does the readout measure the gene product's own molecular
activity, or a downstream cellular consequence?) and **convergence** (is the
readout a specific signature of process P, or a hub that many inputs feed into?).
A whole-animal behaviour is the *maximal* phenotypic + high-convergence readout:
it integrates the entire nervous system plus development, metabolism and basic
cell biology, so almost any perturbation can move it. That is exactly why ~82% of
reviewed behaviour annotations are downgraded.

Behaviour has now been added as a first-class readout in that project's catalogue
(`BEHAVIORAL_ASSAY` in
[`readout_catalog.yaml`](ASSAY_TO_FUNCTION/readout_catalog.yaml)), with the test
names — Morris Water Maze, open field, rotarod, fear conditioning, … — as match
patterns. The **Casp3 `swimming behavior`** case above is the emblematic failure
mode: the *assay modality* is mistaken for the gene's function. The Morris Water
Maze is a swimming-based test of *spatial memory*; a gene merely measured in it
(caspase-3, as an apoptosis marker) gets mis-annotated to `swimming behavior`.

### Standardized behavioural-assay resources

There is **no single canonical ontology that maps a behavioural assay to the GO
process it licenses** (which is the gap `readout_catalog.yaml` fills by hand).
The landscape is split across three complementary layers:

- **Process / phenotype vocabularies.** The **Neuro Behavior Ontology (NBO)** is
  the OBO Foundry ontology of behavioural *processes* (it complements and extends
  GO's behaviour branch) and behavioural *phenotypes*; GO's `behavior` terms are
  aligned with it. The **Mammalian Phenotype Ontology (MP)** has a
  `behavior/neurological phenotype` branch (MP:0005386) for the *outcome* of a
  test. These describe the process/phenotype, not the assay.
- **Assay / protocol registries.** **IMPReSS** (the International Mouse
  Phenotyping Resource of Standardised Screens, from the IMPC) is the closest
  thing to a standardized *list of behavioural assays*: versioned SOPs with
  defined parameters for open field, rotarod, etc. — a protocol registry rather
  than an ontology. **OBI** (Ontology for Biomedical Investigations) models
  assays generically (as planned processes) and can type a "behavioural assay".
- **Human cognitive tasks.** The **Cognitive Paradigm Ontology (CogPO)** and the
  **Cognitive Atlas** catalogue human behavioural/cognitive *paradigms*,
  decomposed into stimulus → instruction → response, harmonised with OBI/BFO.

For this project's purposes the practical takeaway is that an assay (IMPReSS/OBI)
reports a phenotype (MP/NBO), which is at best weak, non-core evidence for a GO
*process* (NBO/GO) — and never for a molecular function. Tightening the
behaviour branch's GO↔NBO alignment, and recording *which assay* drove each
behaviour annotation, would let the over-annotation check run automatically.

The **IMPReSS** standardized assay battery is ingested under
[`BEHAVIOR/impress/`](BEHAVIOR/impress/README.md): a reproducible pull across 5
IMPC pipelines (287 procedures → **15 canonical behavioural/neurological assay
types**, including Rotarod, Hole-board, Hot Plate, Tail Suspension, Von Frey and
Sleep-Wake, which the core pipeline omits), plus a hand-curated
[`behavioural_assay_go_map.yaml`](BEHAVIOR/impress/behavioural_assay_go_map.yaml)
mapping each assay to the GO behaviour term it can support as `KEEP_AS_NON_CORE`
(QuickGO-verified ids). That map closes the missing assay→GO link and fences off
the traps — Grip Strength (neuromuscular, no behaviour term), Tail Suspension (no
GO term for depression-like immobility) and Auditory Brain Stem Response
(electrophysiology, a hearing term at most, not `auditory behavior`).

The map is wired into the over-annotation mining two ways: a `BEHAVIORAL_ASSAY`
readout class in [`ASSAY_TO_FUNCTION/readout_catalog.yaml`](ASSAY_TO_FUNCTION/readout_catalog.yaml)
(generic readout↔action cross-tab via `mine_readouts.py`), and a dedicated
[`check_behaviour_assays.py`](BEHAVIOR/impress/check_behaviour_assays.py) that
verifies the *specific* GO term against the *specific* assay named in an
annotation's evidence. The checker independently re-derived the **Casp3 `swimming
behavior`** over-annotation (Morris Water Maze is a spatial-memory test; swimming
is only the modality) — confirming that fix from the assay side.

## Status & next steps

- [x] Mine the source surface and reviewer decisions; confirm the
      over-annotation signature (~76% of reviewed behaviour annotations
      downgraded, rising to 82% after the spot-check below).
- [x] Document exemplars and a working rubric.
- [x] Spot-check the `ACCEPT`ed behaviour annotations — proximal cases upheld
      (CRY, lov-1/pkd-2, GCG, DpuGr29); 9 missed downgrades (App ×5, STAT3 ×3,
      nphp-1 ×1) corrected to `KEEP_AS_NON_CORE`.
- [x] Re-review the un-adjudicated / `PENDING` behaviour annotations: only one
      remained — **Casp3** `swimming behavior` (IEP, PMID:33574912). The cited
      study uses the swimming-based Morris Water Maze to assay **memory**
      (postoperative cognitive dysfunction) and measures caspase-3 only as a
      hippocampal apoptosis marker, so swimming is the assay modality, not a
      caspase-3 function → `MARK_AS_OVER_ANNOTATED`. **Every behaviour annotation
      in the corpus is now adjudicated** (0 PENDING).
- [x] Cross-link with [ASSAY_TO_FUNCTION](ASSAY_TO_FUNCTION.md): behaviour
      readouts are the most distal, most convergent quadrant of that framework;
      added a `BEHAVIORAL_ASSAY` readout class to its catalogue and documented the
      standardized behavioural-assay resources (NBO, MP, IMPReSS, OBI, CogPO).

## Related projects

- [ASSAY_TO_FUNCTION](ASSAY_TO_FUNCTION.md) — the proximity / convergence
  framework that behaviour readouts exemplify.
- [OVER_ANNOTATION_PATTERNS](OVER_ANNOTATION_PATTERNS.md) — the broader catalogue
  of over-annotation patterns (behaviour is pattern "indirect downstream
  process").
- [CONTESTED_FUNCTION](CONTESTED_FUNCTION.md) — for cases where the behaviour
  annotation is genuinely contradicted rather than merely distal.
