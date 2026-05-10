# Entner-Doudoroff Sub-pathway Obsoletion (GO:0009255, GO:0061679, GO:0061680, GO:0061681)

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
| PSEPK edd | `genes/PSEPK/edd/edd-ai-review.yaml` | IEA from `GO_REF:0000120`, accepted; also referenced under `core_functions[].directly_involved_in` |
| PSEPK eda | `genes/PSEPK/eda/eda-ai-review.yaml` | `action: NEW` annotation proposal (not in GOA) keyed off the UniProt pathway statement; also referenced under `core_functions[].directly_involved_in` |

Both reviews will need a refresh once the obsoletion lands so that the
`directly_involved_in` references and the `existing_annotations` review
entries point to **GO:0061678** instead of GO:0009255. The biology is
unchanged — Edd (phosphogluconate dehydratase) and Eda (KDPG aldolase) are
the canonical ED-pathway enzymes in P. putida KT2440.

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

### Existing reviews to refresh (post-obsoletion)

1. **edd (PSEPK)** — `genes/PSEPK/edd/edd-ai-review.yaml`. Update
   GO:0009255 → GO:0061678 in both `existing_annotations` and the
   `core_functions[].directly_involved_in` block.
2. **eda (PSEPK)** — `genes/PSEPK/eda/eda-ai-review.yaml`. Same edit pattern
   as edd.

### New ortholog reviews (proactive)

Verify each with `just fetch-gene <organism> <gene>` before starting; do not
add files without confirming the UniProt accession from the UniProt API.

3. **edd (E. coli K-12)** — phosphogluconate dehydratase; the founding
   organism for the ED pathway and likely the EcoCyc-affected entry upstream.
4. **eda (E. coli K-12)** — KDPG aldolase; companion to E. coli edd,
   completes the two-enzyme ED core.
5. **zwf (PSEPK)** — glucose-6-phosphate 1-dehydrogenase, the entry step into
   the ED pathway via 6-phosphogluconate. Already partially covered in the
   PSEPK gene set per `projects/SPKW-PSEPK.md`; verify status before adding.
6. **gnd / 6PGD homologs** — the diversion point between ED and the pentose
   phosphate pathway; a clean review here clarifies why annotations should
   sit at GO:0061678 rather than a sub-variant.

## Proposed approach

1. **Wait for the obsoletion to land** in a public GO release. The
   ontology ticket (#31916) has not yet been merged at the time of writing,
   so refreshing the PSEPK reviews now would need to be redone if labels
   change.
2. **Once the obsoletion is in a release**, update the two PSEPK reviews in
   one PR — the change is mechanical (term ID swap + label update) and the
   `review.summary` text already justifies pathway-level annotation. The
   action differs by gene: for **edd** the existing IEA is `ACCEPT`ed and
   stays `ACCEPT` on the lifted parent term; for **eda** the annotation is
   a curator-proposed `NEW` (no GOA row) and stays `NEW` on the lifted
   parent term. The `review.summary` text in eda also references the old
   label "Entner-Doudoroff pathway through 6-phosphogluconate" and should
   be updated to "Entner-Doudoroff pathway (GO:0061678)" alongside the
   term-ID swap.
3. **Re-run `just validate PSEPK edd` and `just validate PSEPK eda`** after
   the edits to confirm the schema accepts the new term IDs.
4. **Defer new ortholog reviews** (E. coli edd/eda, zwf, gnd) to a follow-up
   batch — the obsoletion does not block them, and they are best done as a
   coherent ED-pathway batch rather than ad hoc.

## Priority

**Low–Medium.** The obsoletion is mechanical and only two existing reviews
are affected; both can be updated in a single small PR once the ontology
release ships. Higher value is in using the moment to add E. coli ED
reviews, but those are independent of the obsoletion itself.

## Status

- 2026-05-10 — Project file created. Tracking upstream issue #6390 (last
  active 2026-05-01). Obsoletion not yet merged. Two existing PSEPK reviews
  (edd, eda) flagged for term-ID update once the obsoletion ships.
