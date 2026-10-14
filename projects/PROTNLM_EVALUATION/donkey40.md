---
title: "DONKEY40: ProtNLM2, TreeGrafter and PAINT IBA on the same genes"
tags: [EVALUATION, ML_PREDICTIONS]
autolink_gene_symbols: false
---
# DONKEY40

**Purpose.** Compare three electronic sources of GO annotation on the same
mammalian genes: ProtNLM2 predictions and TreeGrafter (`GO_REF:0000118`) rows
on donkey proteins, and PAINT IBA (`GO_REF:0000033`) rows on their horse
orthologs. [Parent project](../PROTNLM_EVALUATION.md);
companion to the [TreeGrafter evaluation](../TREEGRAFTER.md).

**Why donkey.** TreeGrafter annotates only proteins outside PANTHER's
reference proteomes, which receive PAINT IBA instead. Horse (the HORSE40
cohort), chimpanzee, rhesus macaque and pig are reference proteomes: sampled
ProtNLM2 records from them carry IBA and no TreeGrafter rows. Donkey
(*Equus asinus*, `EQUAS`) is not: its sampled records carry TreeGrafter rows
and no IBA. Reference status belongs to a proteome version, not a species: a
horse entry outside PANTHER's horse proteome (for example HORSE40's MTMR9,
A0A9L0T3C1) has no IBA rows.

## Selection

[`select_donkey40.py`](donkey40/select_donkey40.py) builds
[`selection.yaml`](donkey40/selection.yaml) from live services:

1. the 254 donkey records in the official ProtNLM2 accession list;
2. their ProtNLM2 output from the UniProt API: 107 have at least one GO
   prediction;
3. TreeGrafter and IBA row counts per record from QuickGO;
4. a horse ortholog per gene symbol (the HORSE40 accession when the gene is
   in that cohort, otherwise the horse UniProtKB entry with that exact gene
   name and the most IBA rows);
5. eligibility: donkey GO predictions, donkey TreeGrafter rows and horse IBA
   rows all present; one record per gene; ranked by ProtNLM2 GO count, then
   TreeGrafter rows.

49 records are eligible and the first 40 are selected (selected 2026-10-14).
Together they carry 69 ProtNLM2 GO predictions, 165 donkey TreeGrafter rows and
217 horse IBA rows. None of the 40 genes is in HORSE40.

FLCN, BICDL1, NDEL1, ATG4C, IRF9, APP, FBXL20, HOXA2, NADK2, PARD3B, ENTR1,
STX3, LNPEP, TNFRSF1A, ORC5, FOXJ3, POLD2, ATG3, GPAT2, PIKFYVE, EPS8L2,
SNAP23, CADM1, GPC3, KDM4C, DUSP5, RBM41, MITF, PDIA4, TGFBR3, NUMB, SEC23A,
USP36, SLC27A5, GEMIN7, ALKAL2, RASGEF1A, SLC16A11, LOXL3, SAT1.

## Plan

For each donkey record: a gene review under `genes/EQUAS/` (reviewing the
TreeGrafter rows with the rest of GOA) and a ProtNLM2 prediction review. The
horse ortholog's IBA rows are compared term by term against the donkey
TreeGrafter rows (same term, nested, sibling or absent), and both against the
ProtNLM2 predictions, using the same GO-relation logic as
`TREEGRAFTER/tg_versus_protnlm.py`.

Status: selected; reviews not yet run.
