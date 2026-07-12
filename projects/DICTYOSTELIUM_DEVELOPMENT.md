---
title: "Dictyostelium Development Project"
maturity: IN_PROGRESS
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
- [x] Resolve dictyBase symbols → UniProt accessions (`fetch-gene DICDI <gene>`)
- [x] Fetch GOA + UniProt + cached publications for all priority genes
- [x] **Review existing GO annotations for all 32 priority genes (P1–P4)** —
  every annotation adjudicated (ACCEPT / KEEP_AS_NON_CORE / MODIFY / REMOVE /
  MARK_AS_OVER_ANNOTATED / UNDECIDED), with `description`, `core_functions`, and
  verbatim-quoted `supported_by` evidence; all pass `ai-gene-review validate`.
- [x] **Reviewed all 32 priority genes (P1–P4)** — every annotation adjudicated
  (ACCEPT / KEEP_AS_NON_CORE / MODIFY / REMOVE / MARK_AS_OVER_ANNOTATED /
  UNDECIDED), with `description`, `core_functions`, and verbatim-quoted
  `supported_by`; all pass `ai-gene-review validate`.
- [x] **Reviewed the 8 direct functional paralogs** (carB/C/D, acgA, acrA, rasG,
  pkaR, statC) — see [families table](#protein-families--paralog-coverage).
- [x] **Closed the remaining module gaps (12 genes)** — second messengers,
  DIF-1 biosynthesis, starvation, GRN, morphogenesis (see below). **All 14
  enumerated modules now have reviewed representatives.**
- [ ] Add per-gene `GENE-notes.md` deep-research journals where missing
- [ ] Expert sign-off / second-pass QA of the reviews
- [ ] Deeper paralog families still open: wider *tgr* locus, other Ras/Rap,
  dhk/grl family members, ecm/cot paralogs, statB/statD, additional atg genes

### Reviewed genes (52, all validated)

| Batch | Genes |
|-------|-------|
| P1 — cAMP relay & chemotaxis | acaA, carA, gpaB, dagA, regA, pdsA, pkaC, rasC, pten, mhcA |
| P2 — adhesion / DIF-1 / patterning | csaA, cadA, tgrB1, tgrC1, dmtA, dimB, cudA |
| P3 — terminal differentiation & culmination | ecmA, ecmB, cotB, spiA, acbA, dhkA, tagC, grlE |
| P4 — TFs / counting / autophagy | gbfA, statA, srfA, smlA, ctnA, atg1, yakA |
| Paralogs (functional sisters) | carB, carC, carD, acgA, acrA, rasG, pkaR, statC |
| Module-completion | gcA, sgcA, gbpC, gbpD, iplA (2nd messengers) · stlB, chlA, dimA (DIF-1 biosynthesis) · pufA, cmfA (starvation) · gtaC (GRN) · tipA (morphogenesis) |

(`mlcD` was already reviewed prior to this project. `tgrC1` = `lagC`/`gp150`.)

### Module coverage (all 14 represented)

| # | Module | Reviewed representatives |
|---|--------|--------------------------|
| 1 | Starvation sensing & initiation | yakA, pufA, cmfA |
| 2 | cAMP relay & oscillator | acaA, acgA, acrA, carA–D, gpaB, dagA, pkaC, pkaR, regA, pdsA |
| 3 | Chemotaxis & actin motility | rasC, rasG, pten, mhcA, mlcD |
| 4 | Adhesion & allorecognition | csaA, cadA, tgrB1, tgrC1 |
| 5 | DIF-1 morphogen biosynthesis | stlB, chlA, dmtA |
| 6 | Prestalk/prespore patterning | ecmA, cudA, dimA, dimB, cotB |
| 7 | Stalk differentiation & death | ecmB, cudA, tagC |
| 8 | Spore differentiation & encapsulation | cotB, spiA, acbA, srfA |
| 9 | Culmination signaling | acbA, tagC, grlE, dhkA |
| 10 | Autophagy | atg1 |
| 11 | Cell counting / group size | smlA, ctnA |
| 12 | Second messengers (cGMP/Ca²⁺) | gcA, sgcA, gbpC, gbpD, iplA |
| 13 | Transcriptional GRN | gbfA, gtaC, statA, statC, srfA, dimA, dimB, cudA |
| 14 | Morphogenesis / tip organizer | tipA |

## Protein families & paralog coverage

Most reviewed genes are **single members of larger *Dictyostelium* paralog
families** — the pipeline caches each gene's PANTHER family at fetch time. The
first pass reviewed one representative per developmental module; the sister
paralogs (which typically perform the same molecular job at a **different
developmental stage**) remain to be curated. These intra-family sisters are
where IBA/IEA propagation *within* a family most often produces
over-annotation, so they are high-value targets.

| Reviewed member | Family (PANTHER) | Sister paralogs not yet reviewed |
|-----------------|------------------|----------------------------------|
| carA (cAR1) | GPCR cAMP receptor (PTHR23112) | **carB (cAR2), carC (cAR3), carD (cAR4)** |
| acaA (ACA) | Adenylate cyclase (PTHR45627) | **acgA (ACG), acrA (ACR/ACB)** |
| rasC | Ras small-GTPase superfamily (PTHR24070) | **rasG**, rasB, rasD, rasS, rapA |
| pdsA + regA | Cyclic-nucleotide PDE (PTHR11347/PTHR28283) | gbpA, gbpB, pdeD, pdeE |
| pkaC | cNMP-dependent kinase (PTHR24353) | **pkaR (regulatory subunit)** |
| statA | STAT (PTHR11801) | **statB, statC, statD** |
| dhkA | Two-component histidine kinase (PTHR43719) | dhkB, dhkC, dhkE … (~15-member family) |
| grlE | GABA-B / Grl GPCR (PTHR10519) | grlA–grlR (~17 family GPCRs) |
| csaA + tgrB1 + tgrC1 | IPT/TIG domain (PTHR31341) | polymorphic *tgr* allorecognition locus (~14 tgrB/tgrC genes) |
| ecmA + ecmB | ECM protein A family (PTHR31797) | ecmC, ecmF, ecmO |
| cotB | spore-coat (no clean PANTHER) | cotA, cotC, cotD, other PsB-complex coat proteins |
| ctnA (countin) | small-aggregate / counting factor (PTHR35884) | cf45-1, cf50, countin-2 |
| mhcA | Myosin (PTHR13140) | myosin-I family (mlcD light chain already reviewed) |

`gbfA`, `cotB`, and `ctnA` map to *Dictyostelium*-specific / novel families with
no paralog set to chase.

**Highest-value paralog batch (direct functional sisters) — ✅ REVIEWED:**
`carB` (cAR2), `carC` (cAR3), `carD` (cAR4), `acgA` (ACG), `acrA` (ACR),
`rasG`, `pkaR`, `statC` — completing the cAMP receptor series (cAR1–4), the
three developmental adenylate cyclases (ACA/ACG/ACR), the two principal
chemotaxis Ras proteins (RasC/RasG), the PKA holoenzyme (C+R), and a second
STAT. All 8 reviewed and validated.

This batch confirmed the predicted **intra-family IBA/IEA over-propagation**:
the aggregation-stage "adenylate cyclase-activating cAMP receptor" role was
mis-transferred onto the later paralogs cAR4 (MARK_AS_OVER_ANNOTATED) and the
purinergic-receptor IEA was removed from cAR2/cAR3/cAR4; ACR's degenerate
histidine-kinase/receiver domains carried phosphorelay/transferase IEAs refuted
by its functional paper (REMOVE); statC carried metazoan JAK-STAT / defense /
proliferation terms corrected to STAT signaling and removed.

**Still open (lower priority):** wider *tgr* allorecognition locus, remaining
Ras/Rap members, dhk/grl family members, ecm/cot paralogs, statB/statD.

## Existing DICDI reviews in the repo

- `genes/DICDI/mlcD` — myosin light chain (Module 3, motility)
- `genes/DICDI/nip7` — ribosome biogenesis (not development-specific)
- `genes/DICDI/tlcd4b` — TLC-domain lipid metabolism (not development-specific)

## Key References (to cite during curation)

Seed the literature at review time; canonical entry points include the
*Dictyostelium* developmental cell-signaling reviews and dictyBase gene pages.
Record provenance per gene as `[PMID:xxxx "supporting text"]` in the gene notes.
