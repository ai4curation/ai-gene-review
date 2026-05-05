# ER–Plasma Membrane Tethering — Obsoletion & Replacement (GO:0061817)

## Overview

A GO obsoletion proposal will retire **GO:0061817 endoplasmic reticulum–plasma
membrane tethering** (a BP term). The rationale is that the activity is better
captured at the molecular function level by **GO:0160214 endoplasmic
reticulum–plasma membrane adaptor activity**, with the broader spatial
consequence captured by **GO:0051643 endoplasmic reticulum localization** (BP).

This project tracks the impact on AI Gene Review and queues affected gene
families for review, given that none of the canonical ER–PM tether proteins
(extended synaptotagmins, tricalbins, plant synaptotagmins) have been reviewed
yet in this repository.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6383](https://github.com/geneontology/go-annotation/issues/6383)
- Ontology ticket: [geneontology/go-ontology#31873](https://github.com/geneontology/go-ontology/issues/31873)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement candidates |
|---|---|---|
| endoplasmic reticulum–plasma membrane tethering | GO:0061817 | MF: GO:0160214 endoplasmic reticulum–plasma membrane adaptor activity; BP: GO:0051643 endoplasmic reticulum localization |

### Affected upstream groups (from issue body)

| Group | Annotations | Status |
|---|---:|---|
| CGD (Candida glabrata) | 4 | pending |
| PomBase | 13 | DONE |
| TAIR (Arabidopsis) | 2 | pending |
| UniProt | 2 | per latest comment, "uniprot updated" |

### InterPro2GO mappings (per latest upstream comment, term removed by InterPro)

These eight InterPro entries previously mapped to GO:0061817 and have since had
the mapping removed (will appear in InterPro release 109.0):

| InterPro ID | Family | Maps to (organisms) |
|---|---|---|
| IPR017147 | Tricalbin | yeast Tcb1/2/3 |
| IPR037761 | Tricalbin C2A domain | yeast Tcb1/2/3 |
| IPR037765 | Tricalbin C2B domain | yeast Tcb1/2/3 |
| IPR037762 | Tricalbin C2C domain | yeast Tcb1/2/3 |
| IPR037756 | Tricalbin C2D domain | yeast Tcb1/2/3 |
| IPR037733 | Extended synaptotagmin C2A domain | mammalian ESYT1/2/3 and plant SYT1/SYT5 |
| IPR037749 | Extended synaptotagmin C2B domain | mammalian ESYT1/2/3 |
| IPR037752 | Extended synaptotagmin C-terminal C2 domain | mammalian ESYT1/2/3 |

## Impact on this repo

No genes in the ER–PM tether family are currently reviewed. A search for ESYT,
TCB, tricalbin, or synaptotagmin under `genes/` returned no matches. This means
**no existing reviews need refresh** for the obsoletion itself, but the family
is well-characterized in the literature and represents a coherent candidate set
for proactive review.

## Scope

- **Organisms**: human (mammalian E-Syts), S. cerevisiae (tricalbins), and
  Arabidopsis (plant SYTs / TAIR-affected entries). Yeast S. pombe is already
  handled upstream by PomBase.
- **GO branches**: BP (the obsoleted term itself) and the proposed MF
  replacement GO:0160214 — both belong to the membrane contact site (MCS)
  branch.
- **Type of fix**: terminological in GO; biology is well-established. Reviews
  should evaluate whether the MF replacement (adaptor activity) or BP parent
  (ER localization) is the better core-function term, and propose either as
  appropriate.

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` before starting; do not
add files without confirming the UniProt accession from the UniProt API.

### Mammalian Extended Synaptotagmins (E-Syts)

1. **ESYT1** (human) — extended synaptotagmin-1; major Ca²⁺-regulated ER–PM
   tether; recruited to junctions at elevated cytosolic Ca²⁺ (Ca²⁺-dependent
   MCS expansion).
2. **ESYT2** (human) — extended synaptotagmin-2; constitutive ER–PM tether
   active at resting Ca²⁺.
3. **ESYT3** (human) — extended synaptotagmin-3; constitutive ER–PM tether,
   functionally redundant with ESYT2.

### S. cerevisiae Tricalbins

4. **TCB1** (SGD: YOR086C) — yeast tricalbin-1; cortical ER–PM tether.
5. **TCB2** (SGD: YNL087W) — yeast tricalbin-2; cortical ER–PM tether.
6. **TCB3** (SGD: YML072C) — yeast tricalbin-3; cortical ER–PM tether; the
   triple Δtcb1/2/3 mutant is the canonical loss-of-MCS phenotype.

### Plant Synaptotagmins (TAIR)

7. **SYT1** (Arabidopsis, AT2G20990) — most-studied plant ER–PM tether;
   Ca²⁺-regulated; involved in stress-induced membrane contact stabilization.
   Likely candidate for one of the two TAIR annotations under review upstream.
8. **SYT5** (Arabidopsis) — additional plant ER–PM tether; redundant with SYT1.

### Lower priority / verification only

9. **CGD-affected Candida glabrata orthologs** — 4 annotations upstream; not a
   primary AI Gene Review focus organism. Defer unless the broader project
   expands to fungal pathogens.

## Proposed approach

1. **Wait for the obsoletion decision.** Comment thread on
   geneontology/go-ontology#31873 should be monitored; the InterPro mappings
   have already been removed (per comment from Sara), so the upstream work
   is partly underway.
2. **Once the obsoletion lands**, the replacement MF term GO:0160214 will be
   the natural ACCEPT for core-function annotations of these tethers. Reviews
   should propose this MF and either GO:0051643 (ER localization) or a more
   informative BP child term (membrane contact site organization etc.) for
   process-level annotation.
3. **Begin with ESYT2 + TCB3** as anchor reviews — these are the most
   structurally and biochemically characterized members and have the cleanest
   literature support for the adaptor/tether MF call.
4. **Use the family as a coherent batch** — once one member is reviewed, the
   others can leverage shared references and core-function language.
5. **For TAIR plant SYTs**, defer until ESYT/TCB reviews establish the
   template; plant annotations also require careful handling of stress/drought
   phenotypes vs. core MCS function.

## Priority

**Medium.** The biology is well-established and reviews would be high-quality,
but no existing reviews are blocked by the obsoletion. This is opportunistic —
the family is unreviewed in the repo, the obsoletion makes it timely, and the
membrane contact site (MCS) area has been growing in interest.

## Status

- 2026-05-04 — Project file created. Tracking upstream issue #6383 (last
  active 2026-05-01). Obsoletion not yet applied but InterPro2GO mappings have
  been removed by InterPro per Sara's comment. No gene reviews started yet.
