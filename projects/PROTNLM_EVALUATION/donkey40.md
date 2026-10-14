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

Status: reviews done (2026-10-14); comparison below.

## Results

[`compare_donkey40.py`](donkey40/compare_donkey40.py) builds both tables from
the reviews; the horse IBA rows come from QuickGO into
[`horse_iba.tsv`](donkey40/horse_iba.tsv) (217 rows). TreeGrafter reaches the
donkey record in two ways: its own `GO_REF:0000118` row (165) or a merged
`GO_REF:0000120` row whose WITH/FROM carries a PANTHER PTN node (60). Each row's
action is the action the reviewer gave it in the donkey gene review.

### TreeGrafter on a non-reference mammal reproduces IBA

| Relation to the horse ortholog's IBA | Rows | Down-graded |
|---|---|---|
| same term | 199 | 18 (9%) |
| TreeGrafter shallower | 9 | 0 |
| TreeGrafter deeper | 1 | 1 |
| sibling | 1 | 0 |
| no related IBA term | 15 | 2 |
| **all TreeGrafter rows** | **225** | **21 (9.3%)** |

Down-graded means REMOVE, MARK_AS_OVER_ANNOTATED or MODIFY. Per-row data:
[`donkey40_tg_vs_iba.tsv`](donkey40/donkey40_tg_vs_iba.tsv).

On these 40 genes, 88% of TreeGrafter rows carry the same term as horse IBA,
and 14 of the 217 IBA terms have no related TreeGrafter row. For a protein
whose closest reference ortholog is one speciation away, the graft lands in
the right subfamily, and TreeGrafter acts as a copy of PAINT. The 9.3%
down-graded share compares with 26.9% for the repo's TreeGrafter corpus, which
is mostly bacterial and fungal (see [TREEGRAFTER](../TREEGRAFTER.md)).

The down-graded and UNDECIDED rows have three causes:


- **The donkey sequence model, not the graft (20 rows on three proteins).**
  - The PIKFYVE entry is a short isoform-3 fragment with no kinase domain;
    its kinase and process rows are REMOVE.
  - The TNFRSF1A model lacks part of the ligand-binding ectodomain.
  - The SNAP23 entry is a 97-residue product with only the first SNARE motif.

  Of the 20 rows, 8 are down-graded and 10 are UNDECIDED. TreeGrafter scores
  the family HMM and does not check that the protein keeps the domains the
  function needs. The PDIA4 entry (a KRAB/zinc-finger fusion) shows the same
  fault, but there the wrong rows come from other pipelines.
- **The PAINT annotation itself (10 rows).** These terms are the same on the
  horse IBA, so the question is about the IBD node, not the graft:
  - the SNAP25 synaptic terms on SNAP23;
  - mitophagy and piecemeal microautophagy of the nucleus on ATG4C;
  - endoderm formation and cytoplasm on DUSP5;
  - cell adhesion on PARD3B, kinesin complex on NDEL1, detection of stimulus
    on CADM1, and regulation of apoptotic process on USP36;
  - two MODIFYs to a more exact term (IRF9, TGFBR3).
- **TreeGrafter only (3 rows).**
  - ATG3 carries `GO:0019776`; horse IBA has its replacement `GO:0141046`.
    This is the same release lag as the stale rows in TREEGRAFTER.
  - Two GPAT2 rows (fatty acid metabolic process, mitochondrial membrane)
    have no counterpart on horse.

### ProtNLM2 on the same proteins

The 69 ProtNLM2 GO predictions were judged COR 16, CNN 15, LSP 24, UNC 10,
NPI 4: 80% correct, 6% wrong. Per-row data:
[`donkey40_protnlm_vs.tsv`](donkey40/donkey40_protnlm_vs.tsv).

| Relation to donkey TreeGrafter rows | Predictions | Correct | UNC | Wrong |
|---|---|---|---|---|
| same term | 4 | 4 | 0 | 0 |
| ProtNLM2 shallower | 27 | 27 | 0 | 0 |
| ProtNLM2 deeper | 3 | 2 | 0 | 1 |
| sibling | 3 | 2 | 1 | 0 |
| unrelated | 32 | 20 | 9 | 3 |

Against horse IBA the counts are almost the same (28 shallower, 3 same term),
as expected now that TreeGrafter and IBA agree.

- **Where ProtNLM2 overlaps the tree-based sources, it is shallower.** It
  names an ancestor of a term TreeGrafter already gives in 27 of the 37
  related predictions; all 27 are correct and most are LSP.
- **Its new content sits off the tree.** All 16 COR predictions are unrelated
  to any TreeGrafter or IBA term. Examples:
  - dynactin binding and centrosome on BICDL1;
  - protein delipidation on ATG4C;
  - peptidyl-lysine oxidation on LOXL3;
  - extracellular region on TGFBR3.

  So do 9 of the 10 UNC and 3 of the 4 NPI predictions.
- **The four wrong predictions show four different faults.**
  - **Keyword read as an activity:** phosphorylation on EPS8L2, from the
    Phosphoprotein keyword.
  - **The fused gene model:** double-stranded DNA binding on the PDIA4 fusion.
  - **Function of the full-length protein:** a PI-phosphate biosynthetic
    process on the PIKFYVE fragment.
  - **Activity of an unrelated family:** myosin phosphatase on DUSP5.

**Summary.** On a mammal one speciation from a reference proteome,
TreeGrafter is reliable and redundant with IBA. Its errors there come from
the input sequence or are inherited from PAINT. ProtNLM2 is shallower where
the two overlap, but supplies most of the correct annotation that neither
tree-based source has.
