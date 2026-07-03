---
title: "Inferred from Sequence Orthology (ISO) Evidence Code Review"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human, mouse, rat]
---
# Inferred from Sequence Orthology (ISO) Evidence Code Review

## Overview

ISO (Inferred from Sequence Orthology, ECO:0000266) transfers GO annotations
between orthologous genes. The code is often reliable for conserved molecular
functions, but the current reviewed corpus shows that ISO rows need a different
review question from ordinary evidence rows:

> Is the source annotation itself sound, and is this specific term safe to
> propagate across this orthology relationship?

The answer is not binary. Existing reviews show three common outcomes:

1. The transfer is correct, sometimes even redundant with target-species
   experimental evidence.
2. The source annotation is weak, stale, circular, or miscited.
3. The source annotation is sound, but propagation to the target is unsafe
   because the target is a paralog, a diverged family member, a different
   isoform/compartment context, or a different physiological context.

## Corpus Snapshot

Read-only inventory on 2026-06-29 of reviewed `*-ai-review.yaml` files containing
`evidence_type: ISO`:

| Metric | Count |
|---|---:|
| Reviewed ISO rows | 4,189 |
| Gene review files with ISO rows | 153 |
| Mouse ISO rows | 3,228 |
| Rat ISO rows | 926 |
| Other species ISO rows | 35 |

Disposition across those reviewed ISO rows:

| Review action | Count | Interpretation |
|---|---:|---|
| `ACCEPT` | 1,374 | Conserved enough to keep as core or correct annotation. |
| `KEEP_AS_NON_CORE` | 1,970 | Often true, but contextual, tissue-specific, downstream, or generic localization. |
| `MARK_AS_OVER_ANNOTATED` | 378 | Biology may be related, but the propagated term overstates the direct role. |
| `REMOVE` | 217 | Strong evidence that the annotation should not be retained. |
| `MODIFY` | 114 | The transfer captures the right idea but needs a better GO term. |
| `UNDECIDED` | 127 | Evidence could not be adjudicated confidently. |
| `NEW` | 9 | Orthology-supported new-annotation candidates recorded in review files. |

Most reviewed ISO rows are therefore not catastrophic failures. The main curation
value is discriminating correct/non-core transfers from source or propagation
defects.

## Existing Review Synthesis

### Calmodulin: valid family-wide transfer, with locus-specific caveats

Calm3 is the clean positive control. Mouse `Calm1`, `Calm2`, and `Calm3` encode
the same calmodulin protein, so ISO transfer of core protein functions such as
calcium binding, channel
regulation, calcineurin/CaMKII-related signaling, and cytoplasmic localization is
biochemically sound. The remaining issue is not protein orthology but locus and
context: Calm3 has a distinct 3-UTR/Stau2-dependent dendritic mRNA-localization
mechanism, while many synaptic, cardiac, spindle, centrosome, and sarcomere rows
are best retained as non-core context rather than treated as defining Calm3
function.

### Ghr: direct donor support mixed with circular and stale transfers

Ghr shows why ISO review must trace the donor edge. The manual donor trace
(`genes/mouse/Ghr/Ghr-iso-donor-trace.md`) separates
human and rat donor rows into direct receptor biology, redundant/circular
transfer chains, and stale or context-heavy rows.

Good transfers include growth hormone receptor activity, peptide hormone binding,
plasma membrane/cell surface localization, receptor complex terms, and
growth-hormone/JAK-STAT pathway terms. Problem rows include lipid binding, growth
factor binding, receptor internalization, response to estradiol, response to
cycloheximide, IGF receptor signaling, cytosol, cytoplasmic RNP granule,
proteasome-mediated catabolism, and negative regulation of GHR signaling. Several
are not simply "wrong ortholog" cases; they are transfer-of-transfer artifacts
or donor rows with no current source-side support.

The Ghr review also shows an isoform trap: extracellular-space annotations can
fit the GH-binding protein product, while signaling annotations apply to the
full-length membrane receptor.

### Ang2: source and propagation defects reinforce each other

Ang2 is the strongest ISO negative control. A reproducible source trace
(`genes/mouse/Ang2/Ang2-bioinformatics/RESULTS.md`) found that
all 46 local ISO rows were transferred from human ANG (`UniProtKB:P03950`) via
`GO_REF:0000119`. The trace classified the human source side as:

| Source-side status | Count |
|---|---:|
| Current human ANG term with direct experimental support | 34 |
| Current human ANG term with inferred support only | 4 |
| No current matching human ANG source term | 8 |

Even many directly supported human ANG annotations are unsafe for mouse Ang2,
because mouse Ang2/Angrp is a divergent angiogenin paralog: direct mouse evidence
supports RNase/tRNA-cleavage activity but not canonical angiogenesis, receptor
binding, signaling, stress-response, nuclear-trafficking, or immune-effector
roles. The reviewed Ang2 ISO rows ended up mostly `REMOVE`:

| Action for Ang2 ISO rows | Count |
|---|---:|
| `REMOVE` | 41 |
| `ACCEPT` | 2 |
| `KEEP_AS_NON_CORE` | 2 |
| `MODIFY` | 1 |

Ang2 also exposed source-annotation hygiene problems outside the ISO block:
several experimental GOA rows trace to angiopoietin-2, angiotensin II, or ZNF418
papers rather than to mouse Ang2/Angrp. This is the clearest example where
"source annotation bad" and "propagation bad" both matter.

### Broad mouse and rat ISO: the common pattern is non-core context

The largest reviewed ISO blocks are not dominated by outright removals. Many
mouse and rat signaling genes carry large ISO sets where the core molecular
function is correct but the transferred rows include many tissue, pathway,
phenotype, complex, or localization contexts. Typical review actions are
`KEEP_AS_NON_CORE`, `MARK_AS_OVER_ANNOTATED`, or `MODIFY`, not `REMOVE`.

This matters for reviewer tone: ISO is not mostly garbage. The risk is that a
large cloud of true-but-contextual annotations can obscure the small number of
source defects, stale transfers, and paralog-specific propagation failures.

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
- [ ] Add a reusable ISO donor-trace script that handles multiple source entities
      and writes the same source-status fields used in the Ang2 trace.
