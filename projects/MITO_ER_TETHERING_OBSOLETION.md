# Mitochondrion–ER Membrane Tethering — Obsoletion & Replacement (GO:1990456)

## Overview

A GO obsoletion proposal will retire **GO:1990456 mitochondrion-endoplasmic
reticulum membrane tethering** (a BP term). The rationale matches the parallel
ER–PM and peroxisome–chloroplast tether obsoletions: the activity is more
appropriately captured at the molecular function level by the existing
**GO:0140474 mitochondrion-endoplasmic reticulum membrane tether activity**.

This project tracks the impact on AI Gene Review and queues the canonical
mitochondrion–ER tether proteins for review.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6397](https://github.com/geneontology/go-annotation/issues/6397)
- Ontology ticket: [geneontology/go-ontology#31875](https://github.com/geneontology/go-ontology/issues/31875)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| mitochondrion-endoplasmic reticulum membrane tethering | GO:1990456 | MF: GO:0140474 mitochondrion-endoplasmic reticulum membrane tether activity |

### Affected upstream groups (from issue body)

| Group | Annotations | Status |
|---|---:|---|
| CACAO | 1 | pending |
| ComplexPortal | 9 | pending |
| FlyBase | 1 | DONE |
| MGI | 1 | pending |
| SGD | 6 | DONE |
| UniProt | 7 | DONE |
| dictyBase | 5 | pending |

### Mappings to be reviewed

| Source | Mapping |
|---|---|
| InterPro2GO | InterPro:IPR039275 (PDZ domain-containing protein 8) → GO:1990456 |
| HAMAP2GO | HAMAP:MF_03102 (MDM10 family — ERMES component) → GO:1990456 |
| UniRule2GO | UniRule:UR000106107 → GO:1990456 |

## Impact on this repo

The obsoletion intersects existing reviews in the following way:

| Gene | Organism | Existing action on GO:1990456 |
|---|---|---|
| VMP1 | human | annotated with GO:1990456 in `genes/human/VMP1/VMP1-ai-review.yaml` |
| CALM1 | human | GO:1990456 row currently `ACCEPT` |
| CALM2 | human | GO:1990456 row present |
| CALM3 | human | GO:1990456 row present |
| Calm1 | mouse | GO:1990456 row present |
| Calm2 | mouse | GO:1990456 row present |
| Calm3 | mouse | GO:1990456 row present |

These reviews will need a refresh once the obsoletion lands — for VMP1 and the
calmodulin family the GO:1990456 annotation should be reassessed against
GO:0140474 (or, for calmodulins, likely **REMOVED** as a downstream Reactome
pathway over-annotation that was not based on a tether-activity assay).

No canonical mito–ER tether genes (ERMES components, PDZD8, MFN2,
VAPB/PTPIP51) are currently reviewed in this repository.

## Scope

- **Organisms**: human (PDZD8, MFN2, VAPB, PTPIP51), S. cerevisiae (ERMES
  components: MMM1, MDM10, MDM12, MDM34), Dictyostelium (5 dictyBase
  annotations still pending), mouse (1 MGI annotation pending).
- **GO branches**: BP (the obsoleted term itself) and MF GO:0140474. Both
  belong to the membrane contact site (MCS) branch.
- **Type of fix**: terminological in GO; biology is well established. Reviews
  should evaluate whether the MF replacement (`tether activity`) is the better
  core-function term and add it where the underlying assay supports it.

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` before starting; do not
add files without confirming the UniProt accession from the UniProt API.

### Mammalian mito–ER tethers

1. **PDZD8** (human) — PDZ domain-containing protein 8. Direct target of the
   InterPro2GO mapping (IPR039275). Vertebrate functional analog of yeast
   Mmm1; established mito–ER tether (Hirabayashi et al. 2017, Science).
2. **MFN2** (human) — Mitofusin-2. Long-debated mito–ER tether at MAMs
   (de Brito & Scorrano 2008, Nature).
3. **VAPB** (human) — VAMP-associated protein B/C. Forms a tether with
   PTPIP51 at MAMs (Stoica et al. 2014, Nat Commun).
4. **PTPIP51** / **RMDN3** (human) — partner of VAPB at MAMs.

### Yeast ERMES complex (S. cerevisiae)

5. **MMM1** — ER-anchored ERMES SMP-domain subunit (HAMAP MF_03102 family
   member is *MDM10*; MMM1 is a sister subunit).
6. **MDM10** — outer mitochondrial membrane β-barrel; ERMES + TOM-assembly
   bridge. Direct target of HAMAP MF_03102.
7. **MDM12** — cytosolic SMP-domain subunit bridging Mmm1 and Mdm34.
8. **MDM34** — outer mitochondrial membrane SMP-domain subunit.

Yeast SGD has already migrated its annotations upstream; review here would
serve to capture the canonical tether MF for these reference proteins rather
than to fix outstanding GOA rows.

### Other organisms

9. The 5 dictyBase pending annotations are likely to be the *Dictyostelium*
   ERMES homologs — review opportunistically once the gene set is confirmed.

## Proposed approach and priority

1. **Refresh existing affected reviews** (VMP1, CALM1/2/3 in human + mouse)
   to revisit GO:1990456 rows once the obsoletion lands. Most of these are
   likely Reactome-pathway over-annotations that should be **REMOVED** rather
   than rerouted.
2. **Anchor new reviews** on **PDZD8** + **MFN2** as the highest-impact
   mammalian tethers, and on **MMM1** + **MDM12** for the yeast ERMES anchor
   pair.
3. Once GO:0140474 is the canonical MF term, audit other genes in this
   repository whose `core_functions` could legitimately gain it (e.g. through
   the `proposed_replacement_terms` mechanism).

## Status

- Upstream FlyBase, SGD, and UniProt updates are done; CACAO (1),
  ComplexPortal (9), MGI (1), and dictyBase (5) experimental annotations are
  still pending.
- Mappings (InterPro2GO IPR039275, HAMAP MF_03102, UniRule UR000106107) all
  need to be re-pointed to GO:0140474.
- No reviews in this repo are blocked by the obsoletion; the impact is a
  refresh queue (VMP1 + CALM1/2/3) and a forward-looking review queue (PDZD8,
  MFN2, VAPB, PTPIP51, ERMES components).
- Recommend starting with **PDZD8** as the anchor review, since it is both
  the InterPro2GO mapping target and the most recently mechanistically
  characterized mammalian mito–ER tether.
