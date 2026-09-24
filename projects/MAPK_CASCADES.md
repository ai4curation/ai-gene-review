---
title: "MAPK Cascades: Module and Gene Review Coverage"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human, mouse, rat, yeast, SCHPO, worm, DROME]
---

# MAPK Cascades: Module and Gene Review Coverage

## Overview

The generic three-tier MAP kinase relay (MAP3K -> MAP2K -> MAPK) is captured as
the abstract module [mapk_relay](../modules/mapk_relay.html). Six concrete cascade
modules conform to it:

| Module | Cascade | Relay (MAP3K -> MAP2K -> MAPK) |
|---|---|---|
| `erk_cascade` | Ras-RAF-MEK-ERK1/2 | RAF -> MEK1/2 -> ERK1/2 |
| `p38_cascade` | p38 (stress) | ASK1/TAK1/MLK -> MKK3/6 -> p38 |
| `jnk_cascade` | JNK (stress) | MEKK1/ASK1/MLK -> MKK4/7 -> JNK1-3 |
| `erk5_cascade` | ERK5 | MEKK2/3 -> MEK5 -> ERK5 |
| `scer_hog1_cascade` | S. cerevisiae HOG (Sln1 branch) | Ssk2/Ssk22 -> Pbs2 -> Hog1 |
| `scer_mating_fus3_cascade` | S. cerevisiae pheromone | Ste11 -> Ste7 -> Fus3/Kss1 |

This project tracks (1) PANTHER grounding of the module family descriptors and
(2) gene review coverage of the proteins that fill each tier, in human and in
representative model organisms.

## PANTHER grounding of family descriptors

Family descriptors now carry family-level PANTHER ids, each checked against the
local membership index (`interpro/panther/panther-members.tsv`) or the family
entries file:

| Tier | PANTHER family | Used by |
|---|---|---|
| MAPK | PTHR24055 (MITOGEN-ACTIVATED PROTEIN KINASE) | ERK1/2, p38, JNK, ERK5, Fus3/Kss1 |
| MAP2K | PTHR48013 (...KINASE KINASE 5-RELATED) | MEK1/2, MKK3/6, MKK4/7, MEK5 (also contains Pbs2, Ste7, worm SEK-1) |
| MAP3K, MEKK group | PTHR24361 (MITOGEN-ACTIVATED KINASE KINASE KINASE) | MEKK2/MEKK3 |
| MAP3K, RAF | PTHR44329 (TNNI3K-RELATED; contains BRAF, RAF1, ARAF) | RAF kinases |
| MAP3K, yeast osmostress | PTHR48016 (SSK2-RELATED-RELATED) | Ssk2/Ssk22 |
| Ras switch | PTHR24070, PTHR23113, PTHR10194 | Ras, SOS, RasGAP |

Deliberately left without an id: the stress MAP3K descriptors of the p38 and JNK
modules (ASK1, TAK1, MLK and MEKK1 sit in unrelated PANTHER families), the
GRB2/SHC adaptor descriptor, and the DUSP/MKP phosphatase descriptors.

PANTHER subfamilies were not used. The validator suggests them where all listed
members share one, but they are not clean paralog groups for these kinases:
`PTHR48013:SF9` is named for MEK5 but also contains yeast Ste7 and plant MKKs.

### PAINT ancestral nodes

Family descriptors also carry PAINT IBD nodes from the local
`interpro/panther/*/*-paint.tsv` slices, each seeded by the descriptor's own
representative members:

| Descriptor | PAINT node | Propagated terms |
|---|---|---|
| Ras GTPases | PTN000631348, PTN008604616 | GTPase activity; Ras protein signal transduction |
| RasGAPs | PTN008939999 | GTPase activator activity |
| SOS | PTN000560991 | guanyl-nucleotide exchange factor activity |
| RAF | PTN001147804 | MAP kinase kinase kinase activity; MAPK cascade |
| ASK-subgroup MAP3Ks (p38) | PTN000684847 | MAP kinase kinase kinase activity |
| MEK1/2, MKK3/6, MKK4/7 | PTN000684494 | MAP kinase kinase activity; MAPK cascade |
| JNK | PTN001171982, PTN000622075 | JUN kinase activity; JNK cascade; plus the MAPK-wide node |
| ERK1/2, p38, ERK5 | PTN000622075 | MAPK-wide node (Ser/Thr kinase, intracellular signal transduction, nucleus, cytoplasm) |

Not added: MEK5 and MEKK2/3 (not seeds of
a matching node), and Fus3/Kss1 and Hog1 (the yeast seeds are SGD ids that
cannot be mapped to genes offline). The p38 module previously described
PTN000684847 as a p38 MAPK node; it is an ASK-subgroup MAP3K node (seeds ASK1,
MAP3K6, MAP3K15) and the evidence text was corrected.

`panther-members.tsv` was refreshed on 2026-09-24. The old index had MEK2 in
PTHR47448; the current PANTHER classification puts MEK1 and MEK2 in PTHR48013,
consistent with the PAINT tree (both are seeds of PTN000684494), so the MEK
descriptor now uses PTHR48013. One PAINT/HMM mismatch remains: MEKK1/2/3 are
seeds of PTN004700021 in the PTHR48013 PAINT slice, while the membership index
puts them in PTHR24361.

The yeast HOG and mating modules name their proteins as single gene products,
not family members, so Pbs2, Hog1, Ste11, Ste7 and the Sln1/Ypd1/Ssk1
phosphorelay are not in the membership index.

## Gene review coverage

Status as of 2026-09-23. "Done" means the review exists with all existing
annotations actioned and `core_functions` filled.

### ERK1/2 (`erk_cascade`)

| Tier | Done | To do |
|---|---|---|
| Adaptor | mouse Grb2 | human GRB2, SHC1 |
| Ras GEF | - | human SOS1, SOS2 |
| Ras | human HRAS, KRAS, NRAS; mouse Kras, Hras | finish human HRAS, NRAS (status INITIALIZED); deep research for NRAS |
| RasGAP | human NF1, RASA1 | - |
| RAF (MAP3K) | human BRAF | human RAF1, ARAF |
| MEK (MAP2K) | human MAP2K2, horse MAP2K2 (IN_PROGRESS) | human MAP2K1 |
| ERK (MAPK) | human MAPK1; mouse Mapk1, Mapk3; rat Mapk1 | human MAPK3 |
| Invertebrates | - | fly rl, Dsor1, phl; worm mpk-1, mek-2, lin-45, let-60, sem-5 |

### p38 (`p38_cascade`)

| Tier | Done | To do |
|---|---|---|
| MAP3K | human MAP3K5, MAP3K20; worm nsy-1 | human MAP3K7 |
| MAP2K | worm sek-1; S. pombe wis1 (DRAFT) | human MAP2K3, MAP2K6 |
| MAPK | worm pmk-1; S. pombe sty1 (DRAFT) | human MAPK14, MAPK11, MAPK12, MAPK13 |

### JNK (`jnk_cascade`)

No reviews yet. To do: human MAP3K1, MAP2K4, MAP2K7, MAPK8, MAPK9, MAPK10; fly
bsk, hep; worm jnk-1, kgb-1.

### ERK5 (`erk5_cascade`)

No reviews yet. To do: human MAP3K2, MAP3K3, MAP2K5, MAPK7.

### S. cerevisiae HOG (`scer_hog1_cascade`)

No reviews yet, although the module names these proteins directly. To do: yeast
SLN1, YPD1, SSK1, SSK2, SSK22, PBS2, HOG1.

### S. cerevisiae mating (`scer_mating_fus3_cascade`)

No reviews yet. To do: yeast STE11, STE7, FUS3, KSS1, STE5. Note that
`genes/SCHPO/ste11` is an unrelated HMG-box transcription factor; the
S. pombe relative of budding-yeast STE11 is byr2.

### Phosphatase feedback (DUSP/MKP)

No DUSP reviews in any species. To do: human DUSP1, DUSP4, DUSP6, DUSP10, DUSP16.

## Suggested order

1. Yeast HOG and mating cascades: the modules name specific proteins, so these
   reviews ground them directly.
2. The human p38 tier proteins (MAP2K3, MAP2K6, MAPK14) that are the module's
   own representative members.
3. Human JNK and ERK5 relays.
4. Remaining ERK gaps (MAP2K1, MAPK3, RAF1, GRB2, SOS1), then DUSPs.
5. Invertebrate orthologs.

Gene reviews need `just fetch-gene`, which needs network access to UniProt,
QuickGO and PubMed.
