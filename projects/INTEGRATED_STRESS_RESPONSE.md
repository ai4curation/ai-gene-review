---
title: "Integrated Stress Response (ISR) Project"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human]
manifest:
  slides:
    - href: INTEGRATED_STRESS_RESPONSE/slides/INTEGRATED_STRESS_RESPONSE-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/Lfky9QLttPtNhYWCDnYQyx
      title: Project brief
---

# Integrated Stress Response (ISR) Project

**Bottom line:** in the integrated stress response, four kinases (HRI, PKR,
PERK and GCN2) each sense a different stress and phosphorylate eIF2α, which
blocks the eIF2B exchange factor, dampens global translation and lets ATF4 be
translated. The pathway is now modelled as
[`modules/integrated_stress_response.yaml`](https://github.com/ai4curation/ai-gene-review/blob/main/modules/integrated_stress_response.yaml)
(DRAFT): five required parts plus an optional secondary-bZIP arm, with the
OMA1-DELE1 mitochondrial relay taken by reference from the mitochondrial UPR
module rather than re-authored. Gene coverage is most of the way there.
Fifteen of the ~18 candidates have reviews from this and other work — EIF2AK1,
EIF2AK3, EIF2AK4, DELE1, OMA1, ATF4, ATF3, GCN1, EIF2B3 and ASNS COMPLETE;
EIF2B1, EIF2B2, EIF2B4, EIF2B5 and EIF2S3 DRAFT. Six module participants still
have no review: the hub EIF2S1 (eIF2α), EIF2AK2 (PKR), DDIT3 (CHOP), PPP1R15A
(GADD34), PPP1R15B (CReP) and EIF2S2 — all but EIF2S2 have an open pull
request.

We scoped this because the ISR is a drug target (ISRIB), eIF2B mutations cause
vanishing white matter disease, and the DELE1-HRI branch was only described in
2020, so current GO annotation may not reflect it.

## Overview

The Integrated Stress Response (ISR) is a conserved signaling pathway that responds to diverse cellular stresses by phosphorylating eIF2α, leading to global translation attenuation and selective translation of stress-response genes like ATF4. Recent discoveries include the DELE1-HRI mitochondrial stress pathway.

## Model Species

**Primary: Homo sapiens (human)**
- Therapeutic target (ISRIB and related compounds)
- Disease relevance across multiple conditions

## Core Pathway Architecture

### 1. eIF2α Kinases (Stress Sensors)
Four kinases sense different stresses:
- **EIF2AK1** (HRI) - Heme deficiency, mitochondrial stress
- **EIF2AK2** (PKR) - Viral dsRNA
- **EIF2AK3** (PERK) - ER stress
- **EIF2AK4** (GCN2) - Amino acid starvation

### 2. Mitochondrial Stress Signaling (New!)
- **DELE1** - Mitochondrial stress sensor, activates HRI
- **OMA1** - Protease that cleaves DELE1

### 3. Core Pathway
- **EIF2S1** (eIF2α) - Translation initiation factor, phosphorylation target
- **EIF2B1-5** - eIF2B complex, guanine nucleotide exchange factor
- **PPP1R15A** (GADD34) - Phosphatase regulatory subunit, negative feedback
- **PPP1R15B** (CReP) - Constitutive phosphatase

### 4. Transcriptional Response
- **ATF4** - Master ISR transcription factor
- **DDIT3** (CHOP) - Pro-apoptotic TF
- **ATF3** - Stress-responsive TF
- **ASNS** - ATF4 target gene (asparagine synthetase)

## Candidate Genes (~18)

| Gene | UniProt | Function |
|------|---------|----------|
| EIF2AK1 | Q9BQI3 | HRI kinase |
| EIF2AK2 | P19525 | PKR kinase |
| EIF2AK3 | Q9NZJ5 | PERK kinase |
| EIF2AK4 | Q9P2K8 | GCN2 kinase |
| EIF2S1 | P05198 | eIF2α |
| DELE1 | Q14154 | Mitochondrial sensor |
| OMA1 | Q96E52 | DELE1 protease |
| ATF4 | P18848 | Master TF |
| DDIT3 | P35638 | CHOP |
| PPP1R15A | O75807 | GADD34 |
| PPP1R15B | Q5SWA1 | CReP |
| EIF2B1-5 | various | eIF2B complex |

## Key Recent Discoveries (2020+)

- DELE1-HRI pathway for mitochondrial stress (2020)
- ISRIB mechanism of action
- ISR in aging and neurodegeneration
- COVID-19 and ISR activation

## Disease Relevance

- Vanishing white matter disease (EIF2B mutations)
- Neurodegeneration
- Cancer (stress adaptation)
- Metabolic disease

## Module

`modules/integrated_stress_response.yaml` (DRAFT, scope CONCRETE, context
Mammalia) models the relay itself and leaves the induced effector genes out as
downstream biology:

1. **eIF2α kinase activation** — a `ROUTE` variant set over the four kinases
   with `ONE_OR_MORE` selection, because co-occurring stresses engage more than
   one. The HRI branch takes `mitochondrial_upr#oma1_dele1_cleavage` and
   `mitochondrial_upr#dele1_hri_activation` by `module_ref`, both optional
   (heme limitation and cytosolic misfolding activate HRI without DELE1). The
   GCN2 branch includes GCN1 as the ribosome-bound activator.
2. **The eIF2 hub** — the heterotrimer as a complex participant with EIF2S1,
   EIF2S2 and EIF2S3 as active units, so the Ser51-bearing subunit stays visible.
3. **eIF2B inhibition** — the decamer as a complex participant with the catalytic
   ε subunit and the regulatory α/β/δ subcomplex as active units.
4. **ATF4 translational and transcriptional output.**
5. *(optional)* **Secondary bZIP arm** — CHOP and ATF3.
6. **Feedback dephosphorylation** — PPP1CA plus a `REALIZER` variant set over the
   GADD34 and CReP targeting subunits.

Two things the module records rather than hides. GO has no molecular-function
term for the activity of phosphorylated eIF2 toward eIF2B — the mechanistic core
of the pathway — so the hub annoton carries eIF2's ordinary GO:0003743 and the
inhibition is stated on the connection; this is an ontology gap, best raised when
EIF2S1 is reviewed. And the PERK branch deliberately avoids a `module_ref` to
`er_unfolded_protein_response#perk_arm`, which would duplicate this module's
parts 2 and 4. See `modules/integrated_stress_response-notes.md` for the full
build record, including the accession checks and a citation trap (PMID:12882984
is not the CReP paper; PMID:14638860 is).

Six production GO-CAMs cover parts of the relay and are linked on the matching
annotons: `gomodel:6606056e00000903` (the complete HRI branch),
`gomodel:66b5638000000624` (PERK), `gomodel:63d320cd00001779` and
`gomodel:62f58d8800000037` (GCN2 activation by GCN1 and by ZAKα),
`gomodel:61e0e55600000407` (GADD34/CReP targeting PPP1CA) and
`gomodel:6494e2e900001856` (SIFI shut-off of the HRI branch).

## Project Status

- [x] Gene folders set up for 15 of the ~18 candidates
- [x] ISR module built, including the OMA1-DELE1 mitochondrial branch
- [ ] EIF2S1, EIF2AK2, DDIT3, PPP1R15A, PPP1R15B reviews (open PRs)
- [ ] EIF2S2 review (no PR; the one module participant with neither a review nor
      a PR)
- [ ] Promote the module from DRAFT once the hub and feedback reviews land and
      the annoton `notes:` disclaimers can be replaced by `file:` evidence
- EIF2AK3 (PERK): the review does not add GO:0140467 *integrated stress
  response signaling*. [PR #3219](https://github.com/ai4curation/ai-gene-review/pull/3219)
  removed that proposed `NEW` row: GO:0140467 is an ancestor of the
  already-accepted GO:0036499 *PERK-mediated unfolded protein response*, and
  the cited 1999 cloning paper (PMID:9930704) does not show ISR signalling.
  With #3219 merged, EIF2AK3 has 95 annotation rows, down from 96.
