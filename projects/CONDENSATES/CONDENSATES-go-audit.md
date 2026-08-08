---
title: "Condensates: GO and annotation audit"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human, worm, SCHPO, mouse]
autolink_gene_symbols: false
---

# Condensates: GO and annotation audit

Supporting page for [Biomolecular Condensates](../CONDENSATES.md). Every table below is
generated, not hand-written:

```bash
uv run python projects/CONDENSATES/scripts/scan_condensate_annotations.py
```

Rerun it after corpus changes and replace the tables wholesale. The script takes ~4 minutes
over the full `genes/` tree.

## Scope of the term list

The script scans a **hand-curated** list of condensate-space GO terms. It has to: GO has no
`biomolecular condensate` class to enumerate descendants from. The obvious substitute,
`GO:0043228` membraneless organelle, is too broad — checking hierarchical ancestors via OLS
confirms that both the ribosome (`GO:0005840`) and the cytoskeleton (`GO:0005856`) are
descendants of `GO:0043232` intracellular membraneless organelle. Neither is a
phase-separated condensate.

The same check shows `GO:0000407` phagophore assembly site is **not** a descendant of
`GO:0043228`, despite the PAS being a liquid-like Atg-protein condensate. It is included in
the list on biological grounds, not ontological ones.

Two parent terms (`GO:0043228`, `GO:0043232`) are scanned only to show how rarely they are
used directly.

## Reading the tables

- **GOA coverage** counts *gene folders* whose `*-goa.tsv` mentions the term, not
  annotations — a gene with four nucleolus annotations counts once.
- **Review outcomes** counts *annotations* in `*-ai-review.yaml`, so the totals are larger.
  It includes `NEW` annotations proposed by reviewers, which is why some terms show more
  reviewed annotations than GOA-annotated genes.
- Term labels are as of the scan date; the audit does not resolve them live.

## GOA coverage

| Term | Label | Gene folders |
|---|---|---|
| GO:0005730 | nucleolus | 89 |
| GO:0016607 | nuclear speck | 40 |
| GO:0016604 | nuclear body | 39 |
| GO:0000407 | phagophore assembly site | 23 |
| GO:0016605 | PML body | 22 |
| GO:0043186 | P granule | 20 |
| GO:0010494 | cytoplasmic stress granule | 19 |
| GO:0036464 | cytoplasmic ribonucleoprotein granule | 16 |
| GO:0000932 | P-body | 15 |
| GO:0140693 | molecular condensate scaffold activity (MF) | 9 |
| GO:0035770 | ribonucleoprotein granule | 2 |
| GO:0140694 | membraneless organelle assembly (BP) | 1 |
| GO:0043232 | intracellular membraneless organelle (parent) | 1 |
| GO:0042382 | paraspeckles | 0 |
| GO:0140168 | nuclear ribonucleoprotein granule | 0 |
| GO:0045495 | pole plasm | 0 |
| GO:0043228 | membraneless organelle (parent) | 0 |

## Review outcomes (399 reviewed annotations)

| Term | Label | Actions |
|---|---|---|
| GO:0005730 | nucleolus | ACCEPT 70, KEEP_AS_NON_CORE 45, MARK_AS_OVER_ANNOTATED 9, REMOVE 3, UNDECIDED 2 |
| GO:0016607 | nuclear speck | ACCEPT 22, KEEP_AS_NON_CORE 14, MARK_AS_OVER_ANNOTATED 2, REMOVE 1, NEW 1, UNDECIDED 1 |
| GO:0016604 | nuclear body | KEEP_AS_NON_CORE 18, ACCEPT 16, MARK_AS_OVER_ANNOTATED 1 |
| GO:0000407 | phagophore assembly site | ACCEPT 29, KEEP_AS_NON_CORE 3, UNDECIDED 1 |
| GO:0016605 | PML body | KEEP_AS_NON_CORE 19, ACCEPT 4, REMOVE 2, MODIFY 2 |
| GO:0036464 | cytoplasmic ribonucleoprotein granule | ACCEPT 14, KEEP_AS_NON_CORE 8, MARK_AS_OVER_ANNOTATED 3, NEW 1 |
| GO:0000932 | P-body | ACCEPT 20, KEEP_AS_NON_CORE 4, NEW 1 |
| GO:0010494 | cytoplasmic stress granule | ACCEPT 19, KEEP_AS_NON_CORE 6 |
| GO:0043186 | P granule | ACCEPT 20, REMOVE 2, KEEP_AS_NON_CORE 2, NEW 1 |
| GO:0140693 | molecular condensate scaffold activity (MF) | ACCEPT 13, NEW 5, MARK_AS_OVER_ANNOTATED 2, KEEP_AS_NON_CORE 2 |
| GO:0140694 | membraneless organelle assembly (BP) | ACCEPT 5 |
| GO:0043232 | intracellular membraneless organelle (parent) | ACCEPT 5 |
| GO:0035770 | ribonucleoprotein granule | ACCEPT 1 |

All actions combined: ACCEPT 238, KEEP_AS_NON_CORE 121, MARK_AS_OVER_ANNOTATED 17, NEW 9, REMOVE 8, UNDECIDED 4, MODIFY 2

## GO:0140693 roster (22 annotations)

| Species | Gene | Evidence | Action |
|---|---|---|---|
| EUPSC | Q6WDN4 | ISS | NEW |
| SCHPO | mid1 | IDA | ACCEPT |
| human | LGALS3 | IDA | ACCEPT |
| human | LGALS3 | IDA | ACCEPT |
| human | NFE2L2 | IDA | ACCEPT |
| human | SQSTM1 | IDA | ACCEPT |
| human | SQSTM1 | IDA | ACCEPT |
| human | SQSTM1 | IDA | ACCEPT |
| human | SQSTM1 | IDA | ACCEPT |
| human | SQSTM1 | IDA | ACCEPT |
| human | SQSTM1 | IEA | ACCEPT |
| mouse | Ccnt1 | IEA | ACCEPT |
| mouse | Ccnt1 | ISO | ACCEPT |
| mouse | Ccnt1 | ISS | ACCEPT |
| mouse | Trp53 | IEA | KEEP_AS_NON_CORE |
| mouse | Trp53 | ISS | KEEP_AS_NON_CORE |
| rat | Tp53 | ISO | MARK_AS_OVER_ANNOTATED |
| rat | Tp53 | ISS | MARK_AS_OVER_ANNOTATED |
| worm | meg-2 | IGI | NEW |
| worm | meg-3 | IDA | NEW |
| worm | meg-4 | IDA | NEW |
| worm | pgl-2 | IC | NEW |
