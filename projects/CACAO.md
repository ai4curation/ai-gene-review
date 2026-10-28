---
title: "CACAO community annotations review"
maturity: SCOPING
tags: [EVALUATION]
species: [human, mouse, BACSU, ECOLI, ARATH, rat, yeast, DROME]
genes: [Reln, Shank3, Sirt6, Nlgn3, Wnt5a, Pafah1b1, Zbtb20, Nlgn1, GOLPH3, PLAUR]
---

# CACAO community annotations review

**Bottom line:** CACAO (Community Assessment of Community Annotation with
Ontologies) is the GONUTS/Texas A&M course-based curation programme in which
student teams wrote experimental GO annotations from the literature, refereed
by competing teams and instructors. GOA carries 4,373 annotations with
`assigned_by: CACAO` on 2,987 gene products from 658 taxa (snapshot
2026-10-28). They are almost all experimental (2,268 IDA, 1,952 IMP, 86 IGI)
and mostly biological process (2,438 BP, 1,034 MF, 901 CC). Gene reviews
already exist for 281 of these gene products, covering 503 CACAO rows. Those
reviews accepted 263, kept 150 as non-core, modified 47, marked 20
over-annotated, removed 9, left 7 undecided, and called 2 too general; 5 rows
are absent from the review files, which predate them.

The question for this project is whether CACAO rows fail in a characteristic
way that differs from professional curation, and how often. The 503 rows
already judged suggest they mostly hold (82% kept), with the failures in
three recurring shapes:

- **Phenotype read as process.** An IMP effect several steps downstream of the
  gene's activity, annotated as a regulation term: GO:0031281 *positive
  regulation of cyclase activity* on MAPK3, MAPK8 and MAPK14 from one paper
  (PMID:22027397); `regulation of gene expression` on YAP1, SIRT1 and P2RX7;
  `apoptotic process` on BAX.
- **One paper applied to genes it does not assay.** PMID:25313396 lists the
  minimal FlgM secretion components and omits fliH, fliY and swrD, yet carries
  CACAO rows for all three (see [BACSU](BACSU.md)).
- **Single-assay localization.** A CC from one IDA image (SNAP23 mitochondrion,
  KRT19 plasma membrane) that the rest of the literature does not support.

CACAO annotations are experimental, so the
[curator-deference rule](../CLAUDE.md) applies: the student read the full
text, and a `REMOVE` needs the paper itself, not its abstract. The GONUTS wiki
(`gowiki.tamu.edu`) keeps a page per paper and per protein for CACAO
annotations (the ALDH4A1 review used both), and is the first thing to check
when the cached publication is abstract-only.

## Source data

- [`CACAO/data/cacao-quickgo-2026-10-28.tsv`](CACAO/data/cacao-quickgo-2026-10-28.tsv):
  QuickGO download of every annotation with `assignedBy=CACAO`.
- [`CACAO/cacao-inventory.yaml`](CACAO/cacao-inventory.yaml): per gene review,
  the action given to each CACAO row, matched on term, evidence code and
  reference. Regenerate with
  `uv run python projects/CACAO/scripts/cacao_inventory.py`.

## Coverage

| Taxon | CACAO rows | Gene products without a review |
|-------|-----------:|-------------------------------:|
| *Homo sapiens* (human) | 741 | 346 |
| *Mus musculus* (mouse) | 672 | 320 |
| *Bacillus subtilis* 168 (BACSU) | 160 | 98 |
| *Escherichia coli* K-12 (ECOLI) | 156 | 102 |
| *Arabidopsis thaliana* (ARATH) | 144 | 94 |
| *Rattus norvegicus* (rat) | 107 | 75 |
| *Saccharomyces cerevisiae* (yeast) | 106 | 45 |
| *Drosophila melanogaster* (DROME) | 73 | 37 |
| *Oryza sativa* japonica | 70 | 43 |
| Phage T4 (BPT4) | 48 | 21 |

## Approach

1. Review genes with the most CACAO rows first, so each review judges several
   student annotations at once. Batch 1 is the top ten unreviewed gene
   products by CACAO row count in organisms with a gene folder convention.
2. Use the standard workflow (`just fetch-gene`, deep research, the
   annotation-reviewer agent). In each review, note in the CACAO rows'
   `reason` what the cited paper shows and, where the cache is abstract-only,
   what the GONUTS page records.
3. After each batch, rerun the inventory script and update the counts and
   failure shapes above.
4. Once enough rows are judged, compare the CACAO acceptance rate with that of
   experimental rows from other groups on the same genes.

---
# STATUS

Snapshot 2026-10-28: 281/2,987 CACAO gene products reviewed; 503/4,373 rows judged.

## Batch 1 (top unreviewed by CACAO row count)

- [ ] mouse Reln (Q60841), 20 CACAO rows
- [ ] mouse Shank3 (Q4ACU6), 18
- [ ] mouse Sirt6 (P59941), 14
- [ ] mouse Nlgn3 (Q8BYM5), 13
- [ ] mouse Wnt5a (P22725), 11
- [ ] mouse Pafah1b1 (P63005), 9
- [ ] rat Nlgn1 (Q62765), 9
- [ ] mouse Zbtb20 (Q8K0L9), 8
- [ ] human GOLPH3 (Q9H4A6), 6
- [ ] human PLAUR (Q03405), 6

## Follow-ups on existing reviews

- [ ] Add the 5 CACAO rows missing from existing reviews (phage T4 genes 9,
  11 and 18, lambda stf, phi6 P9); four have no evidence code in GOA.
- [ ] Resolve the 7 `UNDECIDED` CACAO rows (DNM1L, CASK, APC, Gpdh1, Sirt5,
  and fliH x2) using the GONUTS records.

# NOTES

## 2026-10-28

Project started. Downloaded all 4,373 CACAO annotations from QuickGO and
matched them to the 9,353 existing gene reviews by UniProt accession. 281
gene products already reviewed; their CACAO rows were judged in passing,
not as a CACAO-focused audit. Actions on those rows: ACCEPT 263,
KEEP_AS_NON_CORE 150, MODIFY 47, MARK_AS_OVER_ANNOTATED 20, REMOVE 9,
UNDECIDED 7, TOO_GENERAL 2, not in review 5.

The nine removals: swrD, fliY (PMID:25313396), phage T4 E lysozyme GO:0003796,
yeast HAP4 GO:0098803, LRO1 GO:0046027 (ISO), spoVAD GO:0031160, ECOLI traB
GO:0016887, lambda Rz1 GO:0045861, ARATH DELTA-OAT GO:0051646. Each should be
rechecked against its GONUTS record before the failure taxonomy is fixed.
