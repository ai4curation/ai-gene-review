---
title: "Entner-Doudoroff Sub-pathway Obsoletion (GO:0009255, GO:0061679, GO:0061680, GO:0061681)"
maturity: IN_PROGRESS
tags: [OBSOLETION]
species: [PSEPK]
genes: [edd, eda, glk]
manifest:
  slides:
    - href: ENTNER_DOUDOROFF_OBSOLETION/slides/ENTNER_DOUDOROFF_OBSOLETION-slides.html
  artifacts:
    - href: https://claude.ai/artifact/5RhmT3CyKNu5wKp3pXvmaG
      title: Project brief
---

# Entner-Doudoroff Sub-pathway Obsoletion (GO:0009255, GO:0061679, GO:0061680, GO:0061681)

**Bottom line:** GO has retired four Entner-Doudoroff (ED) sub-pathway
terms, GO:0009255, GO:0061679, GO:0061680 and GO:0061681, and folded them
into the parent GO:0061678 *Entner-Doudoroff pathway*, because MetaCyc-style
pathway variants are better captured in GO-CAMs than as nested terms. We
tracked the upstream tickets, the external mappings that fed the old terms,
and every review in this repo that uses them. Only two reviews do: *P.
putida* KT2440 *edd* (an accepted IEA row) and *eda* (a proposed NEW row),
both on GO:0009255 and both in `core_functions`. The obsoletion has now
landed (OLS lists GO:0009255 as obsolete, pointing to GO:0061678), so the
"not yet merged" status below is out of date. Both reviews are fixed in
#3232: *edd*'s IEA row changes from ACCEPT to MODIFY → GO:0061678,
*eda*'s NEW row now proposes GO:0061678, and both `core_functions` point to
GO:0061678. The biology does not change. The repo's
`modules/entner_doudoroff_and_gluconeogenesis.yaml` already records the
obsoletion (GO release 2026-07-26) and grounds itself in GO:0061678. One
related term outside this page's four, GO:0061688 *glycolytic process via
Entner-Doudoroff Pathway* (obsoleted in the same release, replaced by
GO:0006096), was proposed by the *P. putida* *glk* review; #3232
drops that MODIFY target, ACCEPTs glk's GOA GO:0006096 *glycolytic process*
row, and moves its `core_functions` to GO:0006096, because Glk
phosphorylates glucose upstream and performs no ED step.

## Overview

A GO obsoletion proposal will retire four sub-variant terms under the
Entner-Doudoroff pathway and consolidate annotations to the parent term
**GO:0061678 Entner-Doudoroff pathway**:

- GO:0009255 Entner-Doudoroff pathway through 6-phosphogluconate
- GO:0061679 Entner-Doudoroff pathway through gluconate
- GO:0061680 Entner-Doudoroff pathway through gluconate to D-glyceraldehyde
- GO:0061681 Entner-Doudoroff pathway through gluconate to D-glyceraldehyde-3-phosphate

The intent is to flatten the over-specified sub-pathway hierarchy and let
biology be captured by the single parent ED-pathway term plus the relevant
enzyme MFs. This project tracks impact on the AI Gene Review repo and queues
follow-up edits to existing reviews and candidate gene reviews for the canonical
ED enzymes.

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

### Affected upstream groups (from issue body)

| Group | Annotations | Status |
|---|---:|---|
| EcoCyc | 1 | pending |
| UniProt | 3 | pending |

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

The obsoletion **directly affects** existing reviews. Two PSEPK gene reviews
already use GO:0009255 in their `existing_annotations` and `core_functions`:

| Gene | File | Current usage |
|---|---|---|
| PSEPK edd | `genes/PSEPK/edd/edd-ai-review.yaml` | IEA from `GO_REF:0000120`, was accepted; also referenced under `core_functions[].directly_involved_in`. Fixed in #3232: row ACCEPT → **MODIFY → GO:0061678**, `core_functions` → GO:0061678 |
| PSEPK eda | `genes/PSEPK/eda/eda-ai-review.yaml` | `action: NEW` annotation proposal (not in GOA) keyed off the UniProt pathway statement; also referenced under `core_functions[].directly_involved_in`. Fixed in #3232: NEW row and `core_functions` → **GO:0061678** |

The obsoletion landed in the GO release 2026-07-26 and both reviews were
refreshed in PR #3232 so that the author-supplied `directly_involved_in`
references and review actions point to **GO:0061678** instead of
GO:0009255. GOA-sourced `existing_annotations[].term.id` values are never
rewritten (see CLAUDE.md); the change is carried in `action` plus
`proposed_replacement_terms` instead. The biology is
unchanged — Edd (phosphogluconate dehydratase) and Eda (KDPG aldolase) are
the canonical ED-pathway enzymes in P. putida KT2440.

The pathway modules are already updated.
`modules/entner_doudoroff_and_gluconeogenesis.yaml` (evidence block for
GO:0061678) records that GO:0009255 was obsoleted in GO release 2026-07-26 with
`replaced_by GO:0061678`, and is itself grounded in GO:0061678
(`modules/emp_glycolysis.yaml` cites it too), so the replacement term is in use
at module level and, since #3232, in the edd and eda reviews.

**Sibling term outside this page's scope.** The same modules record that
GO:0061688 *glycolytic process via Entner-Doudoroff Pathway* was obsoleted in
that release (`replaced_by GO:0006096`). `genes/PSEPK/glk/glk-ai-review.yaml`
proposed GO:0061688 as a `MODIFY` replacement and listed it in
`core_functions[].directly_involved_in`. Fixed in #3232: the MODIFY
target is dropped, the GOA GO:0006096 row is now ACCEPT, and
`core_functions` uses GO:0006096. GO:0061678 was rejected for glk because
Glk phosphorylates glucose upstream and performs no ED step.
(`genes/PSEPK/pgi2` mentions GO:0061688 only in prose, to
reject it.)

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

The two existing PSEPK reviews are the immediate work items; a small set of
ortholog reviews would round out coverage of the canonical ED pathway.

### Existing reviews refreshed (done in #3232)

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
add files without confirming the UniProt accession from the UniProt API.

4. **edd (E. coli K-12)** — phosphogluconate dehydratase; the founding
   organism for the ED pathway and likely the EcoCyc-affected entry upstream.
5. **eda (E. coli K-12)** — KDPG aldolase; companion to E. coli edd,
   completes the two-enzyme ED core.
6. **gnd / 6PGD homologs** — the diversion point between ED and the pentose
   phosphate pathway; a clean review here clarifies why annotations should
   sit at GO:0061678 rather than a sub-variant.

## Proposed approach

1. **Done (PR #3232):** the obsoletion is in the GO release 2026-07-26 and
   the two PSEPK reviews were updated in one PR. For **edd** the GOA IEA row
   keeps its GOA term id (never rewrite GOA ids) and moves from `ACCEPT` to
   `MODIFY` with `proposed_replacement_terms` GO:0061678; for **eda** the
   curator-proposed `NEW` row (no GOA row) was repointed to GO:0061678 and
   its summary relabelled. Author-supplied `core_functions` ids were
   repointed in both.
2. **Defer new ortholog reviews** (E. coli edd/eda, gnd) to a follow-up
   batch — the obsoletion does not block them, and they are best done as a
   coherent ED-pathway batch rather than ad hoc.

## Priority

**Low–Medium.** The obsoletion is mechanical and only two existing reviews
are affected; both are updated in a single small PR, #3232, now that
the ontology release has shipped. Higher value is in using the moment to add E. coli ED
reviews, but those are independent of the obsoletion itself.

## Status

- 2026-05-10 — Project file created. Tracking upstream issue #6390 (last
  active 2026-05-01). Obsoletion not yet merged. Two existing PSEPK reviews
  (edd, eda) flagged for term-ID update once the obsoletion ships.
- 2026-09-27 — Obsoletion is in the GO release 2026-07-26. PR #3232
  applied it: edd GOA row `MODIFY` → GO:0061678, eda `NEW` row and both
  `core_functions` repointed to GO:0061678. The related obsolete
  GO:0061688 (glycolytic process via Entner-Doudoroff Pathway, replaced_by
  GO:0006096) was handled on PSEPK glk, which stays `ACCEPT` on GO:0006096.
  The E. coli edd/eda and gnd ortholog reviews remain as optional follow-up.
