---
title: "Dictyostelium Development Project"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [DICDI]
---

# Dictyostelium Development Project

## Overview

*Dictyostelium discoideum* is the premier model for the transition from
unicellular to multicellular life. On starvation, ~10⁵ solitary amoebae
aggregate by relayed cAMP chemotaxis into a mound, which builds a tip, elongates
into a migrating slug (pseudoplasmodium), and finally culminates into a fruiting
body (sorocarp) — a cellular stalk holding aloft a mass of dormant spores. The
whole program runs ~24 h and is driven by cell–cell signaling, chemotaxis,
allorecognition, and a binary prestalk/prespore cell-fate decision.

This project scopes the **functional modules** that a curation-grade model of
Dictyostelium development must cover, and lists candidate genes (dictyBase
symbols) for review in each. It is a **scoping enumeration** — UniProt accessions
are intentionally omitted here and should be pulled at review time with
`just fetch-gene DICDI <gene>` rather than guessed.

## Model Species

**Dictyostelium discoideum**
- UniProt species code / `genes/` label: **DICDI**
- NCBI taxon: 44689
- Reference database: dictyBase (http://dictybase.org)
- Haploid genome, tractable genetics (KO, REMI, RNAi), synchronous development

## Developmental Stages (context for the modules)

```
growth → starvation → aggregation (streams) → mound → tipped mound
      → first finger / slug (migration, phototaxis) → Mexican hat
      → culmination → fruiting body (stalk + spore mass)
```

## Functional Modules

### 1. Starvation sensing & developmental initiation
Detects nutrient depletion and cell density; commits cells to development.
- **yakA** — DYRK-family kinase, growth→development switch
- **pufA** — Pumilio translational repressor of *pkaC*
- **cmfA** — conditioned medium factor (cell-density sensing)
- **crlA** — cAMP receptor-like GPCR (early)
- (concepts: PSF prestarvation factor, CMF quorum sensing)

### 2. cAMP relay & oscillatory signaling
The core oscillator that produces propagating cAMP waves for aggregation.
- **acaA** — adenylyl cyclase A (aggregation-stage cAMP synthesis)
- **acrA / acgA** — adenylyl cyclases (later/culmination)
- **carA (cAR1)**, **carB/carC/carD** — cAMP receptors (serpentine GPCRs)
- **gpaB (Gα2)**, **gpbA (Gβ)** — heterotrimeric G proteins
- **dagA (CRAC)** — cytosolic regulator of adenylyl cyclase (PH-domain)
- **erkB (ERK2)** — MAP kinase in the relay
- **pkaC / pkaR** — cAMP-dependent protein kinase catalytic/regulatory subunits
- **regA** — intracellular cAMP phosphodiesterase (response regulator)
- **pdsA** — extracellular cAMP phosphodiesterase
- **pdiA** — extracellular PDE inhibitor

### 3. Chemotaxis & cell motility (actin cytoskeleton)
Directed movement up cAMP gradients; shared machinery reused throughout.
- **rasC, rasG** — Ras GTPases (leading-edge signaling)
- **pikA / pikB (PI3K)**, **pten** — PIP3 gradient (front/back polarity)
- **piaA (TorC2/Rip3)** — TORC2 for adenylyl cyclase activation & chemotaxis
- **mhcA** — myosin II heavy chain (rear contraction)
- **mlcE, mlcR** — myosin II essential/regulatory light chains
- **mlcD** — myosin light chain *(existing review in `genes/DICDI/mlcD`)*
- **abpC, corA (coronin), scrA (SCAR/WAVE), arp2/3** — actin regulators

### 4. Cell–cell adhesion & aggregation
Adhesion systems that hold streams and the mound together.
- **csaA (csA / gp80)** — contact sites A, EDTA-resistant adhesion
- **cadA (ddCAD-1 / gp24)** — Ca²⁺-dependent adhesion, early
- **tgrC1 (= lagC / gp150)** — post-aggregation adhesion + allorecognition ligand
- **tgrB1** — allorecognition receptor (TgrB1–TgrC1 self-recognition pair)

> Note: **lagC / gp150 and tgrC1 are the same gene** (UniProt P42523,
> `TGRC1_DICDI`; *lagC1* was renamed *tgrC1*). Curate once, under **tgrC1**.

### 5. DIF-1 morphogen: polyketide biosynthesis & signaling
Chlorinated hexaphenone that induces prestalk fate.
- **stlA, stlB** — steely polyketide synthases (DIF precursor)
- **dmtA** — des-methyl-DIF-1 methyltransferase (final DIF-1 step)
- **chlA** — chlorination for DIF-1
- **dimA, dimB** — bZIP transcription factors mediating DIF response

### 6. Cell-type patterning: prestalk vs prespore decision
The binary fate choice and its positional markers.
- **ecmA, ecmB** — prestalk extracellular-matrix / stalk markers
- **cudA** — nuclear factor for prestalk/culmination
- **cotB, cotC, pspA** — prespore markers
- (concepts: pstA/pstO/pstB zones, prespore zone, tip organizer)

### 7. Stalk differentiation & developmental cell death
Terminal stalk cell vacuolization and death.
- **ecmB**, **cudA**, **stkA (STATa)**
- **tagB, tagC** — ABC-transporter/serine-protease genes for stalk/spore
- autophagy genes (see Module 10) required for stalk cell death

### 8. Spore differentiation, encapsulation & dormancy
Prespore → mature spore; coat assembly; dormancy maintenance.
- **cotA, cotB, cotC** — spore coat proteins
- **spiA** — spore differentiation (late)
- **pspA** — prespore-specific antigen
- **acbA** → **SDF-2** (acyl-CoA-binding protein, spore-encapsulation signal)
- **dhkA, regA** — two-component relay gating encapsulation timing
- (concepts: discadenine germination inhibitor, autoactivation)

### 9. Culmination signaling (SDF / GABA / PKA)
Coordinates the final rise and synchronous sporulation.
- **acbA / SDF-2**, **tagC** (protease releasing SDF-2)
- **grlE** — GABA_B-like receptor; GABA/glutamate signaling in culmination
- **pkaC** activation as master culmination switch
- **dhkA, dhkB, dhkC** — histidine kinases feeding **regA**

### 10. Autophagy (nutrient recycling & stalk death)
Required for multicellular development and terminal differentiation.
- **atg1, atg5, atg6 (beclin), atg7, atg8, atg9** — core autophagy machinery

### 11. Group-size / cell-counting regulation
Sets the number of cells per fruiting body (breaks streams).
- **smlA** — represses counting factor secretion
- **ctnA (countin)**, **cf45-1**, **cf50** — counting-factor complex

### 12. Second messengers for motility (cGMP / Ca²⁺ / IP3)
- **gcA, sgcA** — guanylyl cyclases (cGMP for myosin assembly)
- **gbpA–gbpD** — cGMP/cAMP-binding phosphodiesterases & effectors
- **iplA** — IP3 receptor-like channel; Ca²⁺ signaling

### 13. Transcriptional regulatory network (GRN)
Stage- and cell-type-specific transcription factors.
- **gbfA (GBF)** — G-box binding factor, post-aggregative gene master switch
- **gtaC, gtaG (GATA)** — GATA-family regulators
- **statA (Dd-STATa), statB, statC** — STAT transcription factors
- **srfA (SRF)** — spore/late development
- **mybE, mybC** — Myb regulators (aggregation)
- **dimB, cudA, comH** — cell-type TFs

### 14. Morphogenesis: slug migration, phototaxis, thermotaxis
Behavior of the multicellular slug and tip organizer.
- **tipA** — tip formation
- **countin/tip organizer** interactions; phototaxis/thermotaxis loci
- (many phototaxis genes are still by locus; curate as identified)

## Genes for Review (suggested priority order)

### Priority 1 — Core cAMP relay & chemotaxis (~10 genes)
| Gene | Module | Function |
|------|--------|----------|
| acaA | 2 | Aggregation adenylyl cyclase |
| carA | 2 | cAMP receptor cAR1 |
| gpaB | 2 | Gα2 |
| dagA | 2 | CRAC / adenylyl cyclase activator |
| regA | 2 | Intracellular cAMP PDE |
| pdsA | 2 | Extracellular cAMP PDE |
| pkaC | 2/9 | PKA catalytic subunit |
| rasC | 3 | Ras GTPase (chemotaxis/relay) |
| pten | 3 | PIP3 gradient / polarity |
| mhcA | 3 | Myosin II heavy chain |

### Priority 2 — Adhesion, allorecognition & patterning (~8 genes)
| Gene | Module | Function |
|------|--------|----------|
| csaA | 4 | csA/gp80 adhesion |
| cadA | 4 | ddCAD-1 adhesion |
| tgrC1 | 4 | gp150/lagC post-aggregation adhesion + allorecognition ligand |
| tgrB1 | 4 | Allorecognition receptor |
| dmtA | 5 | DIF-1 biosynthesis |
| dimB | 5/6 | DIF-response bZIP TF |
| cudA | 6/7 | Prestalk/culmination nuclear factor |

### Priority 3 — Terminal differentiation & culmination (~8 genes)
| Gene | Module | Function |
|------|--------|----------|
| ecmA | 6 | Prestalk/stalk ECM marker |
| ecmB | 7 | Stalk marker |
| cotB | 8 | Spore coat protein |
| spiA | 8 | Spore maturation |
| acbA | 8/9 | SDF-2 precursor |
| dhkA | 8/9 | Histidine kinase (encapsulation) |
| tagC | 7/9 | Serine protease / SDF-2 release |
| grlE | 9 | GABA_B receptor (culmination) |

### Priority 4 — Regulators, counting & autophagy (~7 genes)
| Gene | Module | Function |
|------|--------|----------|
| gbfA | 13 | GBF master post-aggregative TF |
| statA | 13 | Dd-STATa |
| srfA | 13 | SRF (late/spore) |
| smlA | 11 | Counting-factor repressor |
| ctnA | 11 | Countin |
| atg1 | 10 | Autophagy initiation |
| yakA | 1 | Growth→development kinase |

## Status & Next Steps

- [x] Enumerate developmental modules and candidate genes (this page)
- [ ] Resolve dictyBase symbols → UniProt accessions (`just fetch-gene DICDI <gene>`)
- [ ] Seed reviews for Priority 1 genes
- [ ] Add deep-research + notes per gene
- [ ] Review existing annotations against GO developmental terms

## Existing DICDI reviews in the repo

- `genes/DICDI/mlcD` — myosin light chain (Module 3, motility)
- `genes/DICDI/nip7` — ribosome biogenesis (not development-specific)
- `genes/DICDI/tlcd4b` — TLC-domain lipid metabolism (not development-specific)

## Key References (to cite during curation)

Seed the literature at review time; canonical entry points include the
*Dictyostelium* developmental cell-signaling reviews and dictyBase gene pages.
Record provenance per gene as `[PMID:xxxx "supporting text"]` in the gene notes.
