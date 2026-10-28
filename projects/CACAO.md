---
title: "CACAO community annotations review"
maturity: SCOPING
tags: [EVALUATION]
species: [STRP1, EBOZM, yeast, RVFVZ, BUNYW, BPPRD, PSEAE, BPP22, SHIFL, ECOLI, BPPH2, BACSU, BPT4, LAMBD, human, mouse, rat, ARATH, DROME]
genes: [pppL, VP35, VP40, GP, WHI3, NSS, N, XV, fabY, sieA, ipaH4.5, clpX, "6"]
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

**Microbes first.** Microbial proteins (bacteria, archaea, viruses and phages,
fungi and protists) carry 2,166 CACAO rows on 1,617 gene products, half the
corpus, but only 116 of them are reviewed, against 151 of 1,107 animal
proteins. They are also where the judged rows fail hardest: 8 of the 9
CACAO removals so far are on microbial genes, out of 199 microbial rows
judged (137 accepted, 20 non-core, 21 modified, 4 over-annotated, 8 removed,
2 undecided, 2 too general, 5 missing). For many of these proteins, notably
phage and virus proteins, the CACAO row is the only experimental GO
annotation, so an error there is not diluted by other curation. The review
order is therefore microbes first, ranked by CACAO row count; the animal and
plant genes follow.

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

## Project files

- [`CACAO/data/cacao-quickgo-2026-10-28.tsv`](CACAO/data/cacao-quickgo-2026-10-28.tsv):
  QuickGO download of every annotation with `assignedBy=CACAO`.
- [`CACAO/data/taxon-groups.yaml`](CACAO/data/taxon-groups.yaml): each of the
  658 taxa assigned to a broad group (Bacteria, Archaea, Viruses, Fungi,
  Metazoa, Viridiplantae, Other eukaryote) from its UniProt taxonomy lineage.
  Regenerate with `uv run python projects/CACAO/scripts/fetch_taxon_groups.py`.
- [`CACAO/cacao-inventory.yaml`](CACAO/cacao-inventory.yaml): per gene review,
  the action given to each CACAO row, matched on term, evidence code and
  reference; counts by group; and the top 100 unreviewed microbial gene
  products by CACAO row count. Regenerate with
  `uv run python projects/CACAO/scripts/cacao_inventory.py`.

## Coverage

| Group | CACAO rows | Gene products | Reviewed |
|-------|-----------:|--------------:|---------:|
| Metazoa | 1,847 | 1,107 | 151 |
| Bacteria | 1,238 | 975 | 34 |
| Viruses (incl. phages) | 612 | 409 | 54 |
| Viridiplantae | 360 | 263 | 14 |
| Fungi | 236 | 170 | 28 |
| Other eukaryotes (protists) | 56 | 42 | 0 |
| Archaea | 24 | 21 | 0 |

Top taxa:

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

1. Review microbial genes first, those with the most CACAO rows at the top,
   so each review judges several student annotations at once. Batch 1 is
   every unreviewed microbial gene product with at least five CACAO rows.
   Most microbial proteins carry only one or two CACAO rows (1,174 of the
   1,501 unreviewed have one), so later batches should group them by
   organism or by cited paper rather than by row count. Animal and plant
   genes come after.
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

Snapshot 2026-10-28: 281/2,987 CACAO gene products reviewed; 503/4,373 rows
judged. Microbial: 116/1,617 reviewed.

## Batch 1: microbes, at least five CACAO rows

Organism codes are UniProt mnemonics, for `just fetch-gene <CODE> <gene>`.

- [ ] STRP1 pppL (Q99YM9), *Streptococcus pyogenes* M1, 8 CACAO rows
- [ ] EBOZM VP35 (Q05127), Zaire ebolavirus, 8
- [ ] EBOZM VP40 (Q05128), Zaire ebolavirus, 6
- [ ] yeast WHI3 (P34761), 6
- [ ] RVFVZ NSS (P21698), Rift Valley fever virus, 6
- [ ] BUNYW N (P16494, entry NSS_BUNYW), Bunyamwera virus, 6
- [ ] BPPRD XV (P13559), phage PRD1 endolysin, 6
- [ ] PSEAE fabY (Q9HU15), *Pseudomonas aeruginosa* PAO1, 5
- [ ] BPP22 sieA (Q38674), phage P22 superinfection exclusion, 5
- [ ] EBOZM GP (Q05320), Zaire ebolavirus glycoprotein, 5
- [ ] SHIFL ipaH4.5 (P18009), *Shigella flexneri*, 5
- [ ] ECOLI clpX (P0A6H1), 5
- [ ] BPPH2 6 (P03685), phage phi29 nucleoid protein p6, 5

## Batch 2: microbes, four CACAO rows (from `cacao-inventory.yaml`)

cha (*T. cruzi*), STM3697 (*Salmonella* LT2), gag (simian foamy virus),
ORF30/ORF32 (phage K), VPS74 and APN1 (yeast), doc (phage P1), K3 and K5
(KSHV), P/V/C (Sendai virus), 5.4 (phage T4), acs and ybjN (ECOLI), D15
(phage T5), 3 (phage phi29), P03316 (Sindbis virus), SWP7 (*Nosema
bombycis*), D4276_028 (*Streptococcus* phage D4276).

## Later: animals and plants (top by CACAO row count)

mouse Reln (20), Shank3 (18), Sirt6 (14), Nlgn3 (13), Wnt5a (11), Pafah1b1
(9), Zbtb20 (8); rat Nlgn1 (9); human GOLPH3 (6), PLAUR (6).

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

Later the same day, at the user's request, the review order was switched to
microbes first. Added `fetch_taxon_groups.py`, which assigns every taxon to a
broad group from its UniProt lineage, and extended the inventory with
per-group counts and a ranked list of unreviewed microbial gene products.
Batch 1 is now the 13 microbial proteins with five or more CACAO rows; the
animal batch moved to the end of the queue.
