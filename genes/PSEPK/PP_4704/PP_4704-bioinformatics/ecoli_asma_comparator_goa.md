# GOA comparator check: E. coli TamB, YhdP, YdbH

Source: QuickGO annotation search, fetched 2026-10-31 (BERIL run
20261031T012805Z-comparator-goa-tamb-yhdp-ydbh). Full rows in
`ecoli_asma_comparator_goa.tsv`.

Question (PR #5755 review): do the E. coli proteins whose proposed
intermembrane lipid-transport role the PP_4704 GO:0120010 ISS row relied on
carry GO:0120010 themselves?

| Protein | UniProt | GO:0120010 intermembrane phospholipid transfer | GO:0015914 phospholipid transport |
|---|---|---|---|
| TamB | P39321 | absent | absent |
| YhdP | P46474 | absent | EXP (PMID:33046656), IBA |
| YdbH | P52645 | absent | IGI (PMID:34781743) |

None of TamB, YhdP or YdbH carries GO:0120010 in GOA. TamB's process annotations are protein secretion and protein localization to outer membrane.
