---
title: "Entner-Doudoroff Sub-pathway Obsoletion (GO:0009255, GO:0061679, GO:0061680, GO:0061681)"
maturity: IN_PROGRESS
last_reviewed: 2026-10-04
tags: [OBSOLETION]
species: [PSEPK]
genes: [edd, eda, glk]
manifest:
  slides:
    - href: ENTNER_DOUDOROFF_OBSOLETION/slides/ENTNER_DOUDOROFF_OBSOLETION-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/5RhmT3CyKNu5wKp3pXvmaG
      title: Project brief
---

# Entner-Doudoroff Sub-pathway Obsoletion (GO:0009255, GO:0061679, GO:0061680, GO:0061681)

**Bottom line:** GO retired four Entner-Doudoroff (ED) sub-pathway terms,
GO:0009255, GO:0061679, GO:0061680 and GO:0061681, and replaced them with the
parent GO:0061678 *Entner-Doudoroff pathway* because the alternate gluconate
and 6-phosphogluconate routes are better distinguished by GO-CAM structure
than by nested pathway terms. PR #3232 applied the only direct fixes needed in this
repo: PSEPK <gene species="PSEPK" symbol="edd">edd</gene> now keeps its
GOA-sourced GO:0009255 row but marks it `MODIFY` to GO:0061678, PSEPK
<gene species="PSEPK" symbol="eda">eda</gene> now proposes a `NEW` row on
GO:0061678, and both reviews' `core_functions` point to GO:0061678. The same
PR fixed the related PSEPK <gene species="PSEPK" symbol="glk">glk</gene>
proposal for obsolete GO:0061688 by accepting its existing GO:0006096
*glycolytic process* row instead: Glk phosphorylates glucose upstream of the
ED dehydration and aldol-cleavage reactions, so it should not receive the ED
pathway process term. The remaining repo work is optional new E. coli `edd`,
`eda` and `gnd` coverage, tracked in [#460](https://github.com/ai4curation/ai-gene-review/issues/460).

## Overview

GO retired four sub-variant terms under the Entner-Doudoroff pathway and
consolidated annotations to the parent term
**GO:0061678 Entner-Doudoroff pathway**:

- GO:0009255 Entner-Doudoroff pathway through 6-phosphogluconate
- GO:0061679 Entner-Doudoroff pathway through gluconate
- GO:0061680 Entner-Doudoroff pathway through gluconate to D-glyceraldehyde
- GO:0061681 Entner-Doudoroff pathway through gluconate to D-glyceraldehyde-3-phosphate

This flattened an over-specified sub-pathway hierarchy without changing the
biology: the key direct functions are still phosphogluconate dehydratase for
Edd and KDPG aldolase for Eda. The repo now carries those two ED enzymes on
the parent ED-pathway term, while the module
`modules/entner_doudoroff_and_gluconeogenesis.yaml` records the finer route
structure.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6390](https://github.com/geneontology/go-annotation/issues/6390)
- Ontology ticket: [geneontology/go-ontology#31916](https://github.com/geneontology/go-ontology/issues/31916)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| Entner-Doudoroff pathway through 6-phosphogluconate | GO:0009255 | GO:0061678 Entner-Doudoroff pathway |
| Entner-Doudoroff pathway through gluconate | GO:0061679 | GO:0061678 Entner-Doudoroff pathway |
| Entner-Doudoroff pathway through gluconate to D-glyceraldehyde | GO:0061680 | GO:0061678 Entner-Doudoroff pathway |
| Entner-Doudoroff pathway through gluconate to D-glyceraldehyde-3-phosphate | GO:0061681 | GO:0061678 Entner-Doudoroff pathway |

### Affected upstream groups (original issue snapshot)

| Group | Annotations | Status |
|---|---:|---|
| EcoCyc | 1 | listed as pending in geneontology/go-annotation#6390 |
| UniProt | 3 | listed as pending in geneontology/go-annotation#6390 |

### External mappings flagged for review (per upstream)

| Source | Mapping |
|---|---|
| MetaCyc:PWY-8004 → metacyc2go | GO:0009255 |
| InterPro:IPR004786 (6-phosphogluconate dehydratase) → interpro2go | GO:0009255 |
| HAMAP:MF_02094 → hamap2go | GO:0009255 |
| UniRule:UR000683091 → unirule2go | GO:0009255 |
| UniRule:UR001995752 → unirule2go | GO:0009255 |
| MetaCyc:NPGLUCAT-PWY → metacyc2go | GO:0061680 |
| MetaCyc:PWY-2221 → metacyc2go | GO:0061681 |

## Impact on this repo

The obsoletion affected two PSEPK gene reviews that were already on
GO:0009255:

| Gene | Affected row | Current state |
|---|---|---|
| <gene species="PSEPK" symbol="edd">edd</gene> | GOA IEA row on GO:0009255 from `GO_REF:0000120` | The row remains keyed to the trusted GOA id GO:0009255 and now carries `MODIFY` with `proposed_replacement_terms: GO:0061678`; `core_functions[].directly_involved_in` now uses GO:0061678 |
| <gene species="PSEPK" symbol="eda">eda</gene> | Curator-proposed `NEW` row originally keyed to GO:0009255 | The proposed row and `core_functions[].directly_involved_in` now use GO:0061678 |

The obsoletion was already present in GO release 2026-05-19; PR #3232
refreshed both reviews after the repo ontology cache had rolled to
2026-07-26 so that the author-supplied `directly_involved_in` references
and review actions point to **GO:0061678** instead of GO:0009255.
GOA-sourced `existing_annotations[].term.id` values are never rewritten
(see CLAUDE.md); the change is carried in `action` plus
`proposed_replacement_terms` instead. The biology is
unchanged — Edd (phosphogluconate dehydratase) and Eda (KDPG aldolase) are
the canonical ED-pathway enzymes in P. putida KT2440.

The pathway modules are already updated.
`modules/entner_doudoroff_and_gluconeogenesis.yaml` grounds the committed
6-phosphogluconate branch in GO:0061678 and records the old GO:0009255 and
GO:0061688 variant terms as obsolete. `modules/emp_glycolysis.yaml` also
points readers to GO:0061678 for the Entner-Doudoroff route, keeping ED
separate from the fructose-6-phosphate-centered EMP glycolysis module.

**Sibling term outside this page's scope.** The same modules record that
GO:0061688 *glycolytic process via Entner-Doudoroff Pathway* was obsoleted in
the same obsoletion wave with `replaced_by GO:0006096`. PSEPK
<gene species="PSEPK" symbol="glk">glk</gene> had proposed GO:0061688 as a
`MODIFY` replacement and listed it in `core_functions[].directly_involved_in`.
PR #3232 dropped that target, accepted the GOA GO:0006096 row, and moved
`core_functions` to GO:0006096. GO:0061678 was rejected for Glk because the
enzyme phosphorylates glucose upstream of the ED branch rather than catalyzing
an ED step. PSEPK `pgi2` mentions GO:0061688 only in prose, to reject it.

**Negative control: PSEPK zwf.** `genes/PSEPK/zwf/` is a complete review of
glucose-6-phosphate 1-dehydrogenase, the entry step that feeds
6-phosphogluconate into the ED pathway. `zwf-ai-review.yaml` uses none of
GO:0009255, GO:0061678 or GO:0061688, so it needs no change and confirms that
only the edd and eda reviews (plus glk's proposed target) are affected.

## Scope

- **Organisms**: bacteria (E. coli, Pseudomonas spp., other ED-using
  organisms). The repo's existing PSEPK coverage is the primary in-scope set.
- **GO branch**: BP (carbohydrate catabolism, glycolysis-alternative). The
  obsoletion is purely terminological — no MF terms are affected.
- **Type of fix**: lift annotations one level to the parent term GO:0061678.
  No enzyme-MF changes required.

## Candidate genes for initial review

The two ED-enzyme reviews and the sibling glk fix are the completed PSEPK
check set; a small set of ortholog reviews would round out coverage of the
canonical ED pathway.

### Existing PSEPK reviews checked

1. **edd (PSEPK)** — `genes/PSEPK/edd/edd-ai-review.yaml`. The GOA IEA row
   keeps its GOA term id GO:0009255 and moves from `ACCEPT` to `MODIFY` with
   `proposed_replacement_terms` GO:0061678; `core_functions[].directly_involved_in`
   now uses GO:0061678.
2. **eda (PSEPK)** — `genes/PSEPK/eda/eda-ai-review.yaml`. The curator-proposed
   `NEW` row (no GOA row) and `core_functions` now use GO:0061678.
3. **glk (PSEPK)** — `genes/PSEPK/glk/glk-ai-review.yaml`. Obsolete
   GO:0061688 MODIFY target dropped; GOA GO:0006096 *glycolytic process* row
   now ACCEPT and `core_functions` → GO:0006096. GO:0061678 was considered
   and rejected, since Glk performs no ED step.

### New ortholog reviews (proactive)

Verify each with `just fetch-gene <organism> <gene>` before starting; do not
add files without confirming the UniProt accession from the UniProt API. This
optional follow-up batch is tracked in
[#460](https://github.com/ai4curation/ai-gene-review/issues/460).

4. **`edd` (E. coli K-12)** — phosphogluconate dehydratase; the founding
   organism for the ED pathway and likely the EcoCyc-affected entry upstream.
5. **`eda` (E. coli K-12)** — KDPG aldolase; companion to E. coli `edd`,
   completes the two-enzyme ED core.
6. **gnd / 6PGD homologs** — the diversion point between ED and the pentose
   phosphate pathway; a clean review here clarifies why annotations should
   sit at GO:0061678 rather than a sub-variant.

## Proposed approach

1. **Done in #3232:** PSEPK edd and eda now use GO:0061678 for the
   author-supplied replacement or `NEW` process term and for
   `core_functions[].directly_involved_in`.
2. **Done in #3232:** PSEPK glk now stays on GO:0006096 after obsolete
   GO:0061688 was dropped as an attempted replacement.
3. **Open in #460:** E. coli `edd`, E. coli `eda` and a `gnd`/6PGD boundary
   review remain useful as one coherent ED-pathway follow-up batch, but they
   no longer block this obsoletion cleanup.

## Priority

**Low–Medium.** The obsoletion is mechanical and only two existing reviews
are affected; both are updated in a single small PR, #3232, now that
the ontology release has shipped. Higher value is in using the moment to add E. coli ED
reviews, but those are independent of the obsoletion itself.

## Status

- 2026-05-10 — Project file created. Tracking upstream issue #6390 (last
  active 2026-05-01). Obsoletion not yet merged. Two existing PSEPK reviews
  (edd, eda) flagged for term-ID update once the obsoletion ships.
- 2026-09-27 — PR #3232 applied the obsoletion after the repo ontology cache
  had rolled to 2026-07-26: edd's GOA row became `MODIFY` → GO:0061678,
  eda's `NEW` row now proposes GO:0061678, and both edd and eda
  `core_functions` were repointed to GO:0061678. The related obsolete
  GO:0061688 (glycolytic process via Entner-Doudoroff Pathway, replaced_by
  GO:0006096) was handled on PSEPK glk, which stays `ACCEPT` on GO:0006096.
  The E. coli `edd`/`eda` and `gnd` ortholog reviews remain as optional follow-up.
- 2026-10-04 — Project audit rechecked PSEPK edd, eda, glk, pgi2 and zwf
  against the project summary. No additional PSEPK review edits were needed;
  stale post-obsoletion wording in the project page and deck was collapsed,
  and [#460](https://github.com/ai4curation/ai-gene-review/issues/460) now
  tracks only the optional E. coli `edd`/`eda`/`gnd` follow-up batch.
