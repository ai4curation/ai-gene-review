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

Rerun it after corpus changes and replace the tables wholesale. The script walks the full
`genes/` tree.

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
| GO:0005730 | nucleolus | 117 |
| GO:0016607 | nuclear speck | 49 |
| GO:0016604 | nuclear body | 45 |
| GO:0010494 | cytoplasmic stress granule | 26 |
| GO:0000407 | phagophore assembly site | 26 |
| GO:0016605 | PML body | 24 |
| GO:0000932 | P-body | 22 |
| GO:0043186 | P granule | 21 |
| GO:0036464 | cytoplasmic ribonucleoprotein granule | 18 |
| GO:0140693 | molecular condensate scaffold activity (MF) | 16 |
| GO:0140694 | membraneless organelle assembly (BP) | 3 |
| GO:0035770 | ribonucleoprotein granule | 2 |
| GO:0043232 | intracellular membraneless organelle (parent) | 1 |
| GO:0042382 | paraspeckles | 0 |
| GO:0140168 | nuclear ribonucleoprotein granule | 0 |
| GO:0045495 | pole plasm | 0 |
| GO:0043228 | membraneless organelle (parent) | 0 |

## Review outcomes (659 reviewed annotations)

| Term | Label | Actions |
|---|---|---|
| GO:0005730 | nucleolus | ACCEPT 124, KEEP_AS_NON_CORE 70, MARK_AS_OVER_ANNOTATED 9, REMOVE 9, UNDECIDED 7, NEW 1 |
| GO:0016607 | nuclear speck | ACCEPT 42, KEEP_AS_NON_CORE 20, MARK_AS_OVER_ANNOTATED 4, REMOVE 3, UNDECIDED 2, NEW 1 |
| GO:0016604 | nuclear body | ACCEPT 27, KEEP_AS_NON_CORE 26, MARK_AS_OVER_ANNOTATED 1, MODIFY 1, REMOVE 1 |
| GO:0000407 | phagophore assembly site | ACCEPT 44, KEEP_AS_NON_CORE 3 |
| GO:0140693 | molecular condensate scaffold activity (MF) | ACCEPT 35, NEW 7, KEEP_AS_NON_CORE 2, MARK_AS_OVER_ANNOTATED 2 |
| GO:0000932 | P-body | ACCEPT 36, KEEP_AS_NON_CORE 5, UNDECIDED 2, NEW 2 |
| GO:0010494 | cytoplasmic stress granule | ACCEPT 25, KEEP_AS_NON_CORE 15, UNDECIDED 1, REMOVE 1, MARK_AS_OVER_ANNOTATED 1 |
| GO:0043186 | P granule | ACCEPT 41, NEW 2 |
| GO:0016605 | PML body | KEEP_AS_NON_CORE 19, ACCEPT 17, REMOVE 4, MODIFY 2 |
| GO:0036464 | cytoplasmic ribonucleoprotein granule | ACCEPT 17, KEEP_AS_NON_CORE 8, MARK_AS_OVER_ANNOTATED 2, NEW 1, MODIFY 1, REMOVE 1 |
| GO:0140694 | membraneless organelle assembly (BP) | ACCEPT 7 |
| GO:0043232 | intracellular membraneless organelle (parent) | ACCEPT 5 |
| GO:0035770 | ribonucleoprotein granule | ACCEPT 2 |
| GO:0042382 | paraspeckles | NEW 1 |

All actions combined: ACCEPT 422, KEEP_AS_NON_CORE 168, REMOVE 19, MARK_AS_OVER_ANNOTATED 19, NEW 15, UNDECIDED 12, MODIFY 4

## GO:0140693 roster (46 annotations)

| Species | Gene | Evidence | Action |
|---|---|---|---|
| EUPSC | Q6WDN4 | ISS | NEW |
| NEUCR | frq | IDA | ACCEPT |
| SCHPO | mid1 | IDA | ACCEPT |
| human | AR | IDA | ACCEPT |
| human | AR | IDA | ACCEPT |
| human | BLNK | IMP | ACCEPT |
| human | CGAS | IDA | ACCEPT |
| human | CGAS | IDA | ACCEPT |
| human | CGAS | IDA | ACCEPT |
| human | CGAS | IDA | ACCEPT |
| human | CGAS | IDA | ACCEPT |
| human | CGAS | IDA | ACCEPT |
| human | CGAS | IEA | ACCEPT |
| human | FLG | IDA | NEW |
| human | HNRNPA2B1 | IDA | ACCEPT |
| human | LGALS3 | IDA | ACCEPT |
| human | LGALS3 | IDA | ACCEPT |
| human | NFE2L2 | IDA | ACCEPT |
| human | NLRP3 | IDA | ACCEPT |
| human | SOS1 | IDA | ACCEPT |
| human | SQSTM1 | IDA | ACCEPT |
| human | SQSTM1 | IDA | ACCEPT |
| human | SQSTM1 | IDA | ACCEPT |
| human | SQSTM1 | IDA | ACCEPT |
| human | SQSTM1 | IDA | ACCEPT |
| human | SQSTM1 | IEA | ACCEPT |
| human | TARDBP | IDA | ACCEPT |
| human | TARDBP | IDA | ACCEPT |
| human | TARDBP | IDA | ACCEPT |
| human | TP53 | IDA | ACCEPT |
| human | TP53 | IDA | ACCEPT |
| human | TP53 | IDA | ACCEPT |
| human | TP53 | IDA | ACCEPT |
| human | TP53 | IDA | ACCEPT |
| mouse | Ccnt1 | IEA | ACCEPT |
| mouse | Ccnt1 | ISO | ACCEPT |
| mouse | Ccnt1 | ISS | ACCEPT |
| mouse | Trp53 | IEA | KEEP_AS_NON_CORE |
| mouse | Trp53 | ISS | KEEP_AS_NON_CORE |
| rat | Tp53 | ISO | MARK_AS_OVER_ANNOTATED |
| rat | Tp53 | ISS | MARK_AS_OVER_ANNOTATED |
| worm | deps-1 | NAS | NEW |
| worm | meg-2 | IGI | NEW |
| worm | meg-3 | IDA | NEW |
| worm | meg-4 | IDA | NEW |
| worm | pgl-2 | IC | NEW |
