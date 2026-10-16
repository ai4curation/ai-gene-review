---
title: "Inferred from Sequence Orthology (ISO) Evidence Code Review"
collections: [HOMOLOGY_PROPAGATION]
maturity: IN_PROGRESS
tags: [PIPELINE, EVALUATION]
species: [human, mouse, rat]
manifest:
  slides:
    - href: ISO/slides/ISO-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/GC5QNPTZrY1hotMEPdr3ME
      title: Project brief
---
# Inferred from Sequence Orthology (ISO) Evidence Code Review

**Bottom line:** ISO transfers a GO annotation from a gene to its ortholog in another species, so an ISO row can fail because the source annotation is weak or because the term should not cross that orthology edge. We read the ISO rows in existing gene reviews, worked through three contrasting cases in depth (mouse Calm3, Ghr and Ang2), and built a failure taxonomy that separates source defects from propagation defects, now recorded in the structured `review.propagation_review` field. We did this so that reviewers stop treating ISO as either trustworthy or garbage and instead say where each defect lives. As of 2026-09-26 the repo holds 4,345 reviewed ISO rows in 201 gene reviews (3,258 mouse, 962 rat, and 125 in human, fission yeast and bacterial reviews): 1,456 ACCEPT, 2,073 KEEP_AS_NON_CORE, 435 MARK_AS_OVER_ANNOTATED, 179 REMOVE, 111 MODIFY, 35 UNDECIDED, plus 56 NEW. The usual problem is a cloud of true but contextual transfers; outright failures cluster in cases like Ang2, a divergent angiogenin paralog where 41 of 46 ISO rows were removed. The corpus snapshot below (2026-06-29) predates these counts.

Of the 304 ISO rows that already carry a structured `propagation_review`, the commonest root causes are `PROPAGATION_BAD` (119) and `TERM_SCOPING_PROBLEM` (101), and the commonest subtype is `CONTEXT_OR_TISSUE_MISMATCH` (113). One action item remains: a reusable donor-trace script.

Part of [Propagation by Homology](HOMOLOGY_PROPAGATION.md).
**[Browse ISO rows](../app/propagation/index.html?evidence=ISO)** ·
[Current statistics](HOMOLOGY_PROPAGATION/propagation-stats.md)

## What an ISO annotation asserts

ISO (Inferred from Sequence Orthology, ECO:0000266) says: *gene product X has
this function because its ortholog Y was shown experimentally to have it.* Every
ISO row therefore names three things, and a review should name them too:

| Part | Where it is in the GAF | Example (mouse Calm3, calcium channel regulator activity) |
|---|---|---|
| **Source** — the donor annotation | `WITH/FROM` gene product, plus that gene's own experimental annotation to the same term | human CALM3 (`UniProtKB:P0DP25`), IDA |
| **Relation** — why the donor counts | The `REFERENCE` GO_REF names the pipeline and its orthology set | GO_REF:0000119, Alliance human→mouse orthology |
| **Target** — the annotated gene | `GENE PRODUCT ID` | mouse Calm3 (`UniProtKB:P0DP28`) |

Almost all ISO in the corpus comes from three automated pipelines, which move
only experimental annotations (IDA, IMP, IPI, IGI, EXP) from the donor
([GO_REF definitions](https://github.com/geneontology/go-site/blob/master/metadata/gorefs.yaml)):

| GO_REF | Donor → target | Orthology source |
|---|---|---|
| GO_REF:0000119 | human → mouse | Alliance of Genome Resources |
| GO_REF:0000096 | mouse ↔ rat | Alliance of Genome Resources |
| GO_REF:0000121 | other mammals (human, mouse, pig, dog, …) → rat | RGD, from HCOP and Alliance calls |

The validity of an ISO row is then three separate questions:

1. **Is the source sound?** Does the donor *still* carry the term, with
   experimental evidence, from a paper about that gene? A donor that has since
   lost the term leaves a stale transfer; a donor whose own support is inferred
   makes the ISO a transfer of a transfer.
2. **Is the relation the right one?** Is the donor the target's one-to-one
   ortholog, or a paralog, or one member of a one-to-many call?
3. **Is the term safe to move?** Conserved biochemistry usually is; tissue,
   developmental, compartment, and regulatory context often is not.

The [propagation browser](../app/propagation/index.html?evidence=ISO) shows all
three for every ISO row: the donor resolved to symbol and species, whether the
donor currently carries the term (`Donor support`), whether the donor is the
target's namesake (`Donor vs target symbol`), and the review verdict.

## Worked examples

### Calmodulin: an orthology pipeline that also transfers across paralogs

Target: mouse Calm3. It receives ISO from four donors:

| Donor | Relation to mouse Calm3 | Pipeline |
|---|---|---|
| human CALM3 (`UniProtKB:P0DP25`) | ortholog | GO_REF:0000119 |
| rat Calm3 (`RGD:2259`) | ortholog | GO_REF:0000096 |
| rat Calm1 (`RGD:2257`) | paralog | GO_REF:0000096 |
| rat Calm2 (`RGD:2258`) | paralog | GO_REF:0000096 |

So yes — part of the Calm3 ISO set is paralogy transfer. The two pipelines
behave differently: human→mouse (GO_REF:0000119) pairs namesakes (CALM1→Calm1,
CALM2→Calm2, CALM3→Calm3), while mouse↔rat (GO_REF:0000096) donates from all
three rat loci to each mouse locus, so rat Calm3 also donates to mouse Calm1 and
Calm2 ([browse](../app/propagation/index.html?evidence=ISO&symbol_match=DIFFERENT_SYMBOL&q=calm)).
Five Calm3 terms, including chromatin, are donated by rat Calm1 alone. Here it
is harmless for protein-level terms: Calm1, Calm2, and Calm3 encode identical
proteins in mouse, rat, and human, and differ only at the locus level (UTR
regulation and tissue expression).
The donors all still carry their terms experimentally. What does not transfer
is locus-level biology — Calm3's Stau2-dependent dendritic mRNA localization is
Calm3-specific — so synaptic, cardiac, spindle, and sarcomere rows are kept as
non-core rather than read as Calm3-defining. (An earlier version of the Calm3
review named the human donor as CALM1; `P0DP25` is CALM3, and the review has
been corrected.)

### Ang2: the right source, the wrong target

Target: mouse Ang2 (Angrp). Every ISO row comes from human ANG
(`UniProtKB:P03950`) via GO_REF:0000119. The donor is well characterised and
most of its terms are still experimentally supported, but mouse Ang2 is a
divergent member of the expanded mouse angiogenin family, not ANG's namesake
ortholog: direct mouse
evidence supports RNase/tRNA cleavage but not angiogenesis, receptor binding,
signaling, nuclear trafficking, or immune-effector roles. Most rows were
removed as `PROPAGATION_BAD` + `WRONG_ORTHOLOG_OR_PARALOG` +
`FUNCTIONAL_DIVERGENCE`. The donor check also finds rows whose human ANG term
has since gone or was itself only inferred, so source and propagation defects
compound. The manual trace is in
`genes/mouse/Ang2/Ang2-bioinformatics/RESULTS.md`;
[browse the rows](../app/propagation/index.html?evidence=ISO&q=Ang2).

### Ghr: sound orthologs, stale sources

Target: mouse Ghr. Donors are its orthologs, human GHR (`UniProtKB:P10912`,
GO_REF:0000119) and rat Ghr (`RGD:2687`, GO_REF:0000096), so the relation is
not the problem. Receptor activity, hormone binding, membrane localization and
JAK-STAT signaling transfer cleanly. The problems are on the source side:
several transferred terms (growth factor binding, receptor internalization,
response to estradiol, response to cycloheximide) are no longer on the human
donor, and one (cytosol) is supported on the donor only by IBA. A stale source
is not automatically a wrong term — the JAK-STAT rows are also stale on the
donor but were kept because the biology is well established for mouse Ghr. The manual trace is
`genes/mouse/Ghr/Ghr-iso-donor-trace.md`; the browser's `Donor support = ABSENT`
filter now finds the same pattern automatically
([browse](../app/propagation/index.html?evidence=ISO&donor_support=ABSENT)).
Ghr also shows an isoform trap: extracellular-space rows fit the GH-binding
protein, signaling rows fit the full-length receptor.

## What ISO adds on top of IBA

For each ISO row the browser records the closest IBA on the same target, using
the GO is_a/part_of closure
([statistics](HOMOLOGY_PROPAGATION/propagation-stats.md#what-does-iso-add-on-top-of-iba)):

- **IBA to the same or a more specific term** — the ISO row is already implied
  by PAINT. Same-term rows are rarely rejected; ISO here is corroboration, not
  new information.
- **IBA only to a more general term** — ISO adds specificity below a PAINT
  term.
- **No related IBA** — ISO adds a new assertion. This is the majority of ISO
  rows, and mostly biological process: the tissue, pathway and physiological
  context that experimental work in human or rat establishes and PAINT does
  not propagate. It is also where most of the non-core, over-annotated and
  removed ISO rows sit.

So ISO's value beyond IBA is mainly mammal-specific process and context
annotation carried from the best-studied species, with conserved core
functions largely duplicated by PAINT. The review burden follows the same line:
the rows ISO uniquely contributes are the ones that most need checking.
[Browse ISO rows with no related IBA](../app/propagation/index.html?evidence=ISO&iba_on_target=NONE).

## Where ISO fails

The failure patterns seen so far, in rough order of how often they change the
verdict:

- **Context, not function.** Most ISO rows are true but contextual — the
  common outcome is `KEEP_AS_NON_CORE`, not `REMOVE`. The risk is that a cloud
  of true-but-contextual rows hides the few real defects.
- **Donor is not the namesake.** ISO annotations whose donors all have a
  different gene symbol from the target (paralogs, expanded families) are
  rejected or reduced about three times as often as annotations with a
  namesake donor (see statistics).
- **Stale source.** The donor no longer carries the term. The row outlives the
  evidence that justified it.
- **Transfer of a transfer.** The donor's own support is inferred.

## Failure Taxonomy

Use two labels when reviewing IBA or ISO propagation:

1. A **root-cause class**: where the defect lives.
2. A **biological subtype**: what kind of transfer mistake it is.

Record these in `review.propagation_review`. Keep the narrative rationale in
`review.reason`; the structured object should stay mechanical.

Example:

```yaml
review:
  action: REMOVE
  reason: Mouse Ang2/Angrp retains RNase activity but lacks the angiogenic function of human ANG.
  propagation_review:
    root_cause: PROPAGATION_BAD
    failure_modes:
      - WRONG_ORTHOLOG_OR_PARALOG
      - FUNCTIONAL_DIVERGENCE
    source_entities:
      - source_id: UniProtKB:P03950
        source_label: ANG
        source_status: SUPPORTS_SOURCE_BUT_NOT_TARGET
        comment: Human ANG supports angiogenesis; mouse Ang2/Angrp is non-angiogenic.
```

### Root-cause classes

| Code | Meaning | Fix target |
|---|---|---|
| `NO_FAILURE_CORE` | Transfer is correct and core for the target. | Keep annotation. |
| `NO_FAILURE_NON_CORE` | Transfer is biologically defensible but contextual or secondary. | Keep as non-core. |
| `SOURCE_BAD` | Source annotation is wrong, miscited, homonym-confused, or contradicted. | Fix source annotation before judging transfer. |
| `SOURCE_STALE_OR_MISSING` | Transferred term no longer appears on the current source record, or donor trace cannot recover it. | Remove or re-source the transfer. |
| `SOURCE_WEAK_OR_INFERRED` | Source exists but is only inferred, statement-level, or otherwise weak for transfer. | Downgrade confidence; require target/family corroboration. |
| `EVIDENCE_CIRCULAR_OR_REDUNDANT` | ISO chain transfers from another transfer, or target already has stronger direct evidence. | Do not treat ISO edge as independent support. |
| `PROPAGATION_BAD` | Source annotation is sound, but the term should not propagate to this target. | Fix orthology/family/node propagation. |
| `TERM_SCOPING_PROBLEM` | Biology is related, but the GO term is too broad, too specific, or wrong in role/qualifier. | `MODIFY` or mark over-annotated. |
| `UNRESOLVED` | Propagation issue was investigated but cannot yet be classified confidently. | Use `UNDECIDED` or defer until source/target evidence is resolved. |

### Biological subtypes

| Code | Applies to | Typical signal |
|---|---|---|
| `WRONG_ORTHOLOG_OR_PARALOG` | ISO and IBA | Donor/source is a paralog, expanded family member, or wrong subfamily. |
| `FUNCTIONAL_DIVERGENCE` | ISO and IBA | Target retained fold/orthology but changed substrate, product, activity, or pathway role. |
| `PSEUDO_OR_SUBACTIVITY_LOSS` | Mostly IBA, sometimes ISO | Catalytic residues or a specific sub-activity are lost even though the domain remains. |
| `CONTEXT_OR_TISSUE_MISMATCH` | ISO and IBA | Donor evidence is tissue, developmental, organismal, or disease-context specific. |
| `LINEAGE_OR_TAXON_MISMATCH` | Mostly IBA | Process does not occur in the target lineage or organelle system. |
| `COMPARTMENT_OR_COMPLEX_MISMATCH` | ISO and IBA | Localization, complex membership, or pathway compartment does not transfer. |
| `REGULATORY_SIGN_INVERSION` | ISO and IBA | Family contains activators and inhibitors; positive/negative term leaks across members. |
| `ROLE_CONFLATION` | ISO and IBA | Substrate, regulator, effector, or specificity subunit is annotated as the agent/core machinery. |
| `GRANULARITY_MISMATCH` | ISO and IBA | Parent term is true but uninformative, or child term overstates specificity. |
| `SOURCE_MISCITATION` | ISO and IBA | Source evidence points to the wrong gene, organism, publication, or homonym. |
| `SOURCE_EVIDENCE_WEAK` | ISO and IBA | Source evidence is inferred, statement-level, stale, or otherwise too weak for confident propagation. |
| `CIRCULAR_PROPAGATION` | Mostly ISO, sometimes IBA | Propagation chain depends on another propagated annotation rather than independent source evidence. |

Examples:

- Ang2 human ANG-to-mouse Ang2 angiogenesis rows:
  `PROPAGATION_BAD` + `WRONG_ORTHOLOG_OR_PARALOG` + `FUNCTIONAL_DIVERGENCE`.
- Ghr receptor internalization:
  `SOURCE_STALE_OR_MISSING` + `EVIDENCE_CIRCULAR_OR_REDUNDANT`.
- Ghr hormone-mediated signaling:
  `TERM_SCOPING_PROBLEM` + `GRANULARITY_MISMATCH`.
- Calm3 calcium ion binding:
  `NO_FAILURE_CORE`.
- Calm3 spindle/centrosome contexts:
  `NO_FAILURE_NON_CORE` + `CONTEXT_OR_TISSUE_MISMATCH`.

## Reviewer Checklist

Use this checklist before making a strong `REMOVE` call on ISO or IBA.

### Source annotation checked

- Record the target row: gene, species, GO term, qualifier, aspect, evidence code,
  reference, `WITH/FROM`, and assigned-by source.
- Verify the GO term definition, not just the label.
- Resolve the source gene/product(s) named by `WITH/FROM`.
- Check whether the current source record still carries the same GO term.
- Record the source evidence code and original source reference.
- If the source evidence is experimental, verify that the cited paper supports
  the source gene and term. If only abstract text is cached, avoid claiming a
  curator misread full text.
- Check for source-side `NOT` annotations or contradictory direct evidence.

### Propagation checked

- For ISO, confirm whether the donor-target relation is one-to-one orthology,
  one-to-many, in-paralog, identical protein sequence, or broader family
  similarity.
- For IBA, inspect the PANTHER family/node, seed genes, `WITH/FROM` proteins, and
  whether seeds map to the same functional subfamily as the target.
- Ask whether the exact term should transfer, not only whether the broad family
  function is conserved.
- Check active-site residues, key domains, isoforms, compartment targeting,
  lineage constraints, and target-species direct evidence when relevant.
- Distinguish source defects from propagation defects. Do not hide a bad source
  annotation under "orthology failure," and do not blame a source annotation when
  the real problem is target-specific divergence.

### Disposition recorded

- Assign `propagation_review.root_cause` and any relevant
  `propagation_review.failure_modes`.
- Add `propagation_review.source_entities` entries for donor genes, seed
  proteins, PANTHER nodes, family nodes, or other source entities that were
  checked.
- State whether the recommended fix is source-side, propagation-side, term
  replacement, or non-core retention.
- Prefer `UNDECIDED` when the source full text or family-node evidence cannot be
  checked.

## Action Items

- [x] Review mouse Calm3 ISO annotations as the initial positive-control case.
- [x] Summarize existing ISO reviews across the repository.
- [x] Add an ISO/IBA failure taxonomy that distinguishes source defects from
      propagation defects.
- [x] Add a source/family annotation checklist for future ISO and IBA reviews.
- [x] Add structured `review.propagation_review` schema fields for the taxonomy
      and per-source entity comments.
- [x] Add a reusable donor trace: `just refresh-propagation-sources` resolves every
      ISO/ISS/ISA/Compara donor and records whether it still carries the term;
      surfaced in the [propagation browser](../app/propagation/index.html).
- [x] Regenerated statistics (species pairs, donor support, ISO vs IBA) in
      [propagation-stats](HOMOLOGY_PROPAGATION/propagation-stats.md) instead of
      hand-maintained counts.
- [ ] Map automated donor support onto `propagation_review.source_entities[].source_status`
      suggestions for reviewers (e.g. `ABSENT` → `SOURCE_STALE_OR_MISSING`).
- [ ] Distinguish one-to-one from one-to-many orthology calls in the browser
      (needs Alliance/HCOP orthology type, not yet cached).
