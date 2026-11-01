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
reference proteomes, which receive PAINT IBA instead.
[`reference_proteome_check.py`](donkey40/reference_proteome_check.py) counts
both kinds of row on the first 200 ProtNLM2 records (sorted) of each species
([`reference_proteome_check.tsv`](donkey40/reference_proteome_check.tsv),
2026-10-16):

| Species | Records checked | With IBA | With TreeGrafter |
|---|---:|---:|---:|
| horse | 200 | 40 | 0 |
| chimpanzee | 200 | 70 | 0 |
| rhesus macaque | 200 | 74 | 0 |
| pig | 200 | 80 | 0 |
| donkey | 200 | 0 | 127 |
| crab-eating macaque | 200 | 0 | 119 |
| marmoset | 200 | 0 | 125 |

No record has both. Reference status belongs to a proteome version, not a
species: a horse entry outside PANTHER's horse proteome (for example HORSE40's
MTMR9, A0A9L0T3C1) has no IBA rows, which the same script checks.

**Why not the 577 TreeGrafter proteins already reviewed.** ProtNLM2 output
exists only for the accessions on its published list, and only 15 of the
577 reviewed TreeGrafter proteins are on it (10 of them already have a
prediction review), so a larger overlap needs a new cohort chosen from the
list.

## Selection

[`select_donkey40.py`](donkey40/select_donkey40.py) builds
[`selection.yaml`](donkey40/selection.yaml) from live services:

1. the 254 donkey records in the official ProtNLM2 accession list;
2. their ProtNLM2 output from the UniProt API: 107 have at least one GO
   prediction;
3. TreeGrafter and IBA row counts per record from QuickGO;
4. a horse partner per gene symbol (the HORSE40 accession when the gene is
   in that cohort, otherwise, among the first 10 horse UniProtKB entries with
   that exact gene name, the one with the most IBA rows);
5. eligibility: donkey GO predictions, donkey TreeGrafter rows and horse IBA
   rows all present; one record per gene; ranked by ProtNLM2 GO count, then
   TreeGrafter rows.

49 records are eligible and the first 40 are selected (selected 2026-10-14).
All three arms are enriched by this ranking (most ProtNLM2 GO terms, most
TreeGrafter rows, horse partner with the most IBA rows), so the cohort is not
a random sample and its 69/165/217 counts are not population ratios.

The horse partner is a same-symbol match, not an orthology call. In 39 of the
40 pairs the donkey and horse entries share a PANTHER family
([`donkey40_pair_panther.tsv`](donkey40/donkey40_pair_panther.tsv)). The
exception is SAT1: the donkey entry is in PTHR10545 and its horse partner
(A0A5F5PNJ9) in PTHR14564, so SAT1's three TreeGrafter rows have no
like-for-like IBA comparison and are among the 15 with no related IBA term.

### Snapshot

- `select_donkey40.py` (2026-10-14) wrote `selection.yaml` from the ProtNLM2
  accession list, the UniProt ProtNLM API and QuickGO; the committed file is
  the record of that run. The script now also writes the list URL, the UniProt
  release and any skipped accessions into the file.
- The ProtNLM2 tables come from the project fetcher:
  `snapshot_donkey40.py --accessions-file accs.txt`, then
  `fetch_protnlm_api.py --accessions accs.txt --out-dir FETCHDIR`, then
  `snapshot_donkey40.py --fetch-dir FETCHDIR`. That writes
  [`donkey40-entries.tsv`](donkey40/donkey40-entries.tsv) (the predicted
  protein names), [`donkey40-predictions.tsv`](donkey40/donkey40-predictions.tsv)
  and [`donkey40-evidence.tsv`](donkey40/donkey40-evidence.tsv), adding only a
  `gene_symbol` column. A re-fetch on 2026-10-16 reproduced the 2026-10-14
  predictions and evidence tables byte for byte.
- The predicted protein names in `donkey40-entries.tsv` are not yet scored.
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

Status: reviews done 2026-10-14, re-reviewed 2026-10-23 (#5309) and predictions rescored 2026-10-24 (#5351); comparison below.

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
| same term | 199 | 39 (20%) |
| TreeGrafter shallower | 9 | 4 |
| TreeGrafter deeper | 1 | 1 |
| sibling | 1 | 0 |
| no related IBA term | 15 | 7 |
| **all TreeGrafter rows** | **225** | **51 (22.7%)** |

Down-graded means REMOVE, MARK_AS_OVER_ANNOTATED, MODIFY or TOO_GENERAL;
TOO_GENERAL (12 rows here) counts because, like MODIFY, the review did not keep
the term as it is. Without it the share is 39/225 (17.3%), which is the
definition the TreeGrafter corpus figure uses. Another 13 rows are UNDECIDED.
The actions are those of the donkey gene reviews as re-reviewed on 2026-10-23
(#5309). Per-row data:
[`donkey40_tg_vs_iba.tsv`](donkey40/donkey40_tg_vs_iba.tsv).

On these 40 genes, 88% of TreeGrafter rows (199/225) carry the same term as
horse IBA, and 14 of the 217 IBA terms have no related TreeGrafter row. For a
protein whose closest reference ortholog is one speciation away, the graft
lands in the right subfamily: no donkey review attributes a down-grade to the
placement. TreeGrafter therefore passes PAINT's terms on largely unchanged,
faults included: 39 of the 51 down-graded rows carry exactly the term the
horse ortholog receives as IBA.

A correct graft does not make the rows much more reliable. Under the corpus
definition, 17.3% of donkey rows are down-graded, against 26.9% for the
repo's TreeGrafter corpus (see [TREEGRAFTER](../TREEGRAFTER.md)), which is
mostly bacterial and fungal and has no TOO_GENERAL rows; counting TOO_GENERAL,
the donkey share is 22.7%. The gap is modest and rests on 40 genes: 24 of them
have a down-graded row, and PARD3B and PIKFYVE have six each. It also mixes
taxon with review vintage, since the corpus reviews are older. Both figures
come from the same agentic review process, so they compare the reviews'
judgements, not independent ground truth. About half of the donkey
down-grades keep the biology and ask only for precision (12 TOO_GENERAL, 12
MODIFY to a descendant term); REMOVE and MARK_AS_OVER_ANNOTATED together
account for 23 rows (10.2%), six of them on one PIKFYVE fragment.

The 64 rows that are down-graded (51) or UNDECIDED (13) fall into six groups:

- **The donkey sequence model, not the graft (16 rows on three proteins:
  6 down-graded, 10 UNDECIDED).**
  - The PIKFYVE entry is a short isoform-3 fragment with no kinase domain:
    6 REMOVE, 2 UNDECIDED.
  - The TNFRSF1A model lacks part of the ligand-binding ectodomain:
    4 UNDECIDED.
  - The SNAP23 entry is a 97-residue product with only the first SNARE motif:
    4 UNDECIDED (its two synaptic rows are in the next group).

  TreeGrafter scores the family HMM and does not check that the protein keeps
  the domains the function needs. The PDIA4 entry (a KRAB/zinc-finger fusion)
  shows the same fault, but there the wrong rows come from other pipelines.
- **A PAINT term that over-reaches (13 rows: 12 MARK_AS_OVER_ANNOTATED,
  1 REMOVE).** Each is the same term the horse ortholog receives as IBA, so
  the question is about the IBD node, not the graft:
  - the SNAP25 synaptic terms on SNAP23 (2);
  - mitophagy and piecemeal microautophagy of the nucleus on ATG4C;
  - endoderm formation and cytoplasm on DUSP5;
  - cell adhesion, microtubule cytoskeleton organization, intracellular
    protein localization and epithelial apical/basal polarity on PARD3B;
  - kinesin complex on NDEL1 (REMOVE), detection of stimulus on CADM1, and
    regulation of apoptotic process on USP36.
- **A PAINT term that is right but imprecise (14 MODIFY rows, all the same
  term as horse IBA).** Twelve move to a descendant: the two DUSP5 terms
  (MAP kinase phosphatase activity, ERK1/ERK2 cascade), actin filament binding
  and ruffle membrane on EPS8L2, SMN-Sm protein complex on GEMIN7, type I
  interferon signalling on IRF9, H3K36me2/me3 demethylase activity on KDM4C,
  positive regulation of Pol II transcription on MITF, NADP+ biosynthesis on
  NADK2, bile acid conjugation on SLC27A5, type III TGF-beta receptor activity
  on TGFBR3, and nucleolus on USP36. Two are lateral: ALKAL2 to the
  transmembrane receptor tyrosine kinase activator sibling, and LNPEP
  proteolysis to peptide catabolic process.
- **True but too general (12 TOO_GENERAL rows).** A more specific term in the
  same review entails each: cytoplasm and membrane on LNPEP, apical junction
  complex on PARD3B, endoplasmic reticulum on PDIA4, DNA polymerase complex on
  POLD2, N-acetyltransferase activity on SAT1, plasma membrane and fatty acid
  transmembrane transporter activity on SLC27A5, regulation of Pol II
  transcription on IRF9, and regulation of gene expression, histone
  demethylase activity and histone H3K9 demethylase activity on KDM4C.
- **Not in horse IBA (6 rows).**
  - ATG3 carries `GO:0019776`; horse IBA has its replacement `GO:0141046`.
    This is the same release lag as the stale rows in TREEGRAFTER.
  - Vesicle on EPS8L2, inflammatory response on LOXL3 and establishment of
    centrosome localization on PARD3B (REMOVE): the reviews find each absent
    from the family's current PAINT annotation.
  - Two GPAT2 rows: fatty acid metabolic process has no horse counterpart, and
    mitochondrial membrane is deeper than horse's mitochondrion and is
    refined further to the outer membrane.
- **Not decidable from the available evidence (3 UNDECIDED rows).**
  Positive regulation of TGF-beta receptor signalling on FLCN, whose mouse
  IMP source is not cached; phosphatidylinositol binding on PARD3B; and
  pre-mRNA intronic binding on RBM41, for which no cached literature tests the
  activity.

### ProtNLM2 on the same proteins

The 69 ProtNLM2 GO predictions were judged COR 11, CNN 13, LSP 23, UNC 13,
NPI 9: 68% correct, 13% wrong. Per-row data:
[`donkey40_protnlm_vs.tsv`](donkey40/donkey40_protnlm_vs.tsv). Correctness is judged
for the deposited donkey sequence, so a claim true of the gene but needing a region an
alternative model lacks is NPI. Novelty is judged against GOA for any product of the gene.

Two caveats limit what "68% correct" means. CNN and LSP are judged against the
donkey GOA record, which includes the TreeGrafter rows under evaluation, so 36
of the 47 correct calls (23 of them LSP) are correct relative to TreeGrafter
itself. And the prediction reviews and the gene reviews were written by the
same agentic process. The COR, UNC and NPI calls (33) are the ones judged on
their own evidence.

| Relation to donkey TreeGrafter rows | Predictions | Correct | UNC | Wrong |
|---|---|---|---|---|
| same term | 4 | 4 | 0 | 0 |
| ProtNLM2 shallower | 28 | 24 | 2 | 2 |
| ProtNLM2 deeper | 3 | 2 | 0 | 1 |
| sibling | 3 | 2 | 1 | 0 |
| unrelated | 31 | 15 | 10 | 6 |

Against horse IBA the counts are almost the same (29 shallower, 3 same term),
as expected now that TreeGrafter and IBA agree.

- **Where ProtNLM2 overlaps the tree-based sources, it is shallower.** It
  names an ancestor of a term TreeGrafter already gives in 28 of the 38
  related predictions; 24 of those are correct, most of them LSP.
- **Its new content sits off the tree.** All 11 COR predictions are unrelated
  to any TreeGrafter or IBA term. Examples:
  - protein delipidation on ATG4C;
  - peptidyl-lysine oxidation on LOXL3;
  - protein homodimerization on NADK2;
  - extracellular region on TGFBR3.

  So do 10 of the 13 UNC and 6 of the 9 NPI predictions.
- **The nine wrong predictions fall into four kinds.**
  - **The selected model lacks what the term needs:** membrane on a 97-residue
    SNAP23 product, transporter activity on a SLC16A11 alternative model, and
    double-stranded DNA binding on the PDIA4 fusion gene model.
  - **A phenotype read as participation:** in utero embryonic development and
    cell-cell junction assembly on FLCN, and neuron projection development on
    BICDL1, each resting on loss-of-function or overexpression phenotypes.
  - **Keyword or family default read as an activity:** phosphorylation on
    EPS8L2 (Phosphoprotein keyword) and ubiquitin-dependent catabolism on
    USP36, a nucleolar deubiquitinase.
  - **Activity of an unrelated family:** myosin phosphatase on DUSP5.

**Summary.** On a mammal one speciation from a reference proteome,
TreeGrafter is redundant with IBA: the graft lands correctly and copies the
PAINT terms, but the reviews still down-grade 22.7% of its rows. Those errors
come from the input sequence, are inherited from PAINT, or are terms more
general than the review keeps. ProtNLM2 is shallower where
the two overlap, but supplies most of the correct annotation that neither
tree-based source has.
