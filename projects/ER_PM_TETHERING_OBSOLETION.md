---
title: "ER–Plasma Membrane Tethering — Obsoletion & Replacement (GO:0061817)"
maturity: SCOPING
last_reviewed: 2026-10-04
tags: [OBSOLETION, FLAGSHIP]
species: [human, yeast, ARATH]
genes: [VAPA]
manifest:
  slides:
    - href: ER_PM_TETHERING_OBSOLETION/slides/ER_PM_TETHERING_OBSOLETION-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/FMq8m8yzvRNQmUs1Jv1YqH
      title: Project brief
---

# ER–Plasma Membrane Tethering — Obsoletion & Replacement (GO:0061817)

**Bottom line:** GO has obsoleted the process term GO:0061817
*endoplasmic reticulum-plasma membrane tethering*, because holding the ER
against the plasma membrane is a molecular function. Annotations move to the
function term GO:0160214 *endoplasmic reticulum-plasma membrane adaptor
activity*, with GO:0051643 *endoplasmic reticulum localization* for any
process aspect. We recorded the upstream outcome, the affected groups (CGD 4,
PomBase 13, TAIR 2, UniProt 2) and the eight InterPro2GO mappings InterPro has
already removed, and checked the repo (`grep -rl` over all files under
`genes/`). No review YAML or GOA file uses either term, and no dedicated ER-PM
tether (extended synaptotagmins, tricalbins, plant SYTs) has been reviewed.
Human VAPA, a broad ER contact-site adaptor, never carried GO:0061817 as a
GO annotation here: the term is absent from its GOA file (in every committed
version) and its review. It appears only as a cross-reference line
(IDA:UniProtKB) in the cached UniProt flat file. VAPA has now been assessed for
GO:0160214 and not annotated ([PR #3220](https://github.com/ai4curation/ai-gene-review/pull/3220)). The term's definition requires the adaptor
itself to bind plasma-membrane lipids, and at VAPA contacts that is done by the
partner's PH domain (e.g. ORP3). Scoped, not yet started for the tethers
proper: the obsoletion has since landed (OLS lists GO:0061817 as obsolete),
which makes this family a timely candidate for new reviews, starting with human
ESYT2 and yeast TCB3.

## Overview

GO has retired **GO:0061817 endoplasmic reticulum–plasma membrane
tethering** as a BP term. The rationale is that the tether itself is better
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

## Upstream obsoletion outcome

| Obsoleted term | ID | Replacement terms |
|---|---|---|
| endoplasmic reticulum–plasma membrane tethering | GO:0061817 | MF: GO:0160214 endoplasmic reticulum–plasma membrane adaptor activity; BP: GO:0051643 endoplasmic reticulum localization |

### Affected upstream groups (from issue body)

| Group | Annotations | Status |
|---|---:|---|
| CGD (Candida Genome Database; *Candida* species not recorded upstream) | 4 | DONE |
| PomBase | 13 | DONE |
| TAIR (Arabidopsis) | 2 | DONE |
| UniProt | 2 | DONE |

### InterPro2GO mappings (per latest upstream comment, term removed by InterPro)

These eight InterPro entries previously mapped to GO:0061817; InterPro has
removed that mapping from the live records.

| InterPro ID | Family | Maps to (organisms) |
|---|---|---|
| IPR017147 | Tricalbin | yeast Tcb1/2/3 |
| IPR037761 | Tricalbin C2A domain | yeast Tcb1/2/3 |
| IPR037765 | Tricalbin C2B domain | yeast Tcb1/2/3 |
| IPR037762 | Tricalbin C2C domain | yeast Tcb1/2/3 |
| IPR037756 | Tricalbin C2D domain | yeast Tcb1/2/3 |
| IPR037733 | Extended synaptotagmin C2A domain | mammalian ESYT1/2/3 and plant SYT1/SYT3/SYT5 |
| IPR037749 | Extended synaptotagmin C2B domain | mammalian ESYT1/2/3 |
| IPR037752 | Extended synaptotagmin C-terminal C2 domain | mammalian ESYT1/2/3 |

## Impact on this repo

No canonical extended-synaptotagmin, tricalbin, or plant-SYT ER-PM tether is
currently reviewed. There are no `genes/human/ESYT1`-`ESYT3`,
`genes/yeast/TCB1`-`TCB3`, or `genes/ARATH/SYT1`/`SYT3`/`SYT5` review
directories; no GOA file contains GO:0061817 or GO:0160214; and the only
review occurrence of GO:0160214 is VAPA's suggested question.

A search across **all** file types (`grep -rl GO:0061817 genes/`) finds one
hit: `genes/human/VAPA/VAPA-uniprot.txt:505`, a DR line in the cached UniProt
flat file (entry version 220, 2026-09-02)
`GO:0061817 endoplasmic reticulum-plasma membrane tethering; IDA:UniProtKB`.
That line is UniProt's own cross-reference, not a GOA row. `VAPA-goa.tsv` has
no GO:0061817 row in any committed version, and the review has never used the
term, so no VAPA annotation needs repair for the obsoletion. The two
statements that VAPA "carries GO:0061817 in its cached UniProt record" and
"carries no GO:0061817 annotation in GOA" (the VAPA notes in [PR #3220](https://github.com/ai4curation/ai-gene-review/pull/3220)) are
both true; they describe different files.

VAPA is an ER-resident FFAT-motif adaptor whose review describes it as
organizing contact sites with endosomes, Golgi and plasma membrane, with core
molecular function GO:0043495 *protein-membrane adaptor activity*. It was the
one repo gene where "does GO:0160214 apply?" was already live, and [PR #3220](https://github.com/ai4curation/ai-gene-review/pull/3220)
answers it: **not annotated**. GO:0160214 is defined as bringing the plasma
membrane and ER membrane together "via membrane lipid binding". At
VAPA-dependent ER-PM contacts the plasma-membrane lipid binding is done by the
FFAT partner (e.g. the ORP3 PH domain binding PI(4,5)P2), while VAPA is the
ER-anchored FFAT receptor, already captured by GO:0043495. PomBase does annotate
the fission-yeast VAP orthologs scs2 and scs22 to GO:0160214, and UniProt
transfers it to human VAPB (ISS), so the review records this as a
`suggested_questions` entry rather than settling it. No other review needs refresh for the obsoletion itself; the
tether family proper is well-characterized in the literature and represents a
coherent candidate set for proactive review.

## Scope

- **Organisms**: human (mammalian E-Syts), S. cerevisiae (tricalbins), and
  Arabidopsis (plant SYTs / TAIR-affected entries). Yeast S. pombe is already
  handled upstream by PomBase.
- **GO branches**: BP (the obsoleted term itself) and the MF replacement
  GO:0160214 — both belong to the membrane contact site (MCS) branch.
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

7. **SYT3** (Arabidopsis, AT5G04220) — TAIR-migrated ER–PM adaptor row; exact
   GO:0160214 IDA annotation from PMID:33944955.
8. **SYT1** (Arabidopsis, AT2G20990) — most-studied plant ER–PM tether;
   Ca²⁺-regulated; involved in stress-induced membrane contact stabilization.
9. **SYT5** (Arabidopsis) — additional plant ER–PM tether; redundant with SYT1.

### Lower priority / verification only

10. **CGD-resolved *Candida* orthologs** — CGD handled the four original
    GO:0061817 annotations upstream; defer local reviews unless the project
    expands to fungal pathogens.

## Proposed approach

1. **Record the upstream outcome.** GO:0061817 is obsolete, GO:0160214 is
   active as the replacement MF, PomBase, UniProt, TAIR, and CGD have all
   updated their affected rows, and InterPro has removed the eight former
   InterPro2GO mappings to GO:0061817.
2. **VAPA: done ([PR #3220](https://github.com/ai4curation/ai-gene-review/pull/3220)).** Assessed for GO:0160214 and not annotated,
   because the PM lipid binding at VAPA contacts is the partner's. Whether
   the term should cover ER-anchored FFAT receptors (the PomBase scs2/scs22
   and UniProt VAPB precedent) is raised as a suggested question.
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
- 2026-09-26 — VAPA assessed for GO:0160214 in [PR #3220](https://github.com/ai4curation/ai-gene-review/pull/3220): not annotated
  (definition requires PM lipid binding by the adaptor; at VAPA contacts the
  partner's PH domain does it). VAPA never had GO:0061817 in GOA or its
  review; the only occurrence is a UniProt DR line in `VAPA-uniprot.txt`.
- 2026-10-04 — Re-audited the project against the current repo state. VAPA
  remains the only local review touching GO:0160214, all upstream groups have
  updated their GO:0061817 rows, no canonical ESYT/TCB/SYT tether has been
  reviewed, and the remaining work is to start anchor reviews for ESYT2 and
  TCB3 now that the obsoletion has landed.
