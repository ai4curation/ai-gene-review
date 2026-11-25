# Trpc7 (rat) review notes

## 2026-10-28 session

- Task asked for UniProt A0A8I6GIE6. `just fetch-gene rat Trpc7` resolved F1LQF7 instead. Both
  are unreviewed TrEMBL entries for the same gene: same symbol Trpc7, same RGD:628820 and same
  Ensembl gene ENSRNOG00000012727 (A0A8I6GIE6 also carries GeneID 282822). The GOA file
  (17 rows, including the RGD IDA/TAS/ISO and PAINT IBA rows) is keyed to F1LQF7; QuickGO has
  only 5 IEA rows for A0A8I6GIE6. Reviewed F1LQF7.
- No deep research API; manual synthesis in `Trpc7-deep-research-manual.md`.
- Key points:
  - Core: receptor-operated, DAG-activated Ca2+-permeable nonselective cation channel at the
    plasma membrane [PMID:10488066 "the TRP7 channel is a new member of diacylglycerol-activated
    cation channels"]; [PMID:16741513 "opens Ca(2+)-permeable TRPC7 channels"].
  - Store-operated gating only in stable HEK expression [PMID:15342342]; not seen for mouse TRPC7
    [PMID:10488066 "TRP7 expression did not affect capacitative Ca(2+) entry induced by
    thapsigargin"]. IBA store-operated row marked over-annotated.
  - IP3 binding IBA: no direct binding evidence for TRPC7; IP3 effect is IP3R-independent
    modulation [PMID:18158870]. Over-annotated.
  - Single fertilization IBA: seeded from mouse Trpc2 and a worm TRP gene; no TRPC7 evidence.
  - Endogenous rat TRPC7 in GH4C1 cells is in a perinuclear Golgi region co-localising with
    mannosidase II [PMID:18452405]; added Golgi apparatus as NEW IDA beside the perinuclear row.
  - Overexpression enhances constitutive secretion [PMID:18452405]; overexpression phenotype only,
    no NEW process term (necessity/sufficiency of overexpression is not participation evidence).
  - Mn2+ transport ISO: Mn2+ quench is an assay surrogate for divalent entry; over-annotated.
- Nomenclature trap: PMID:9806837 "TRPC7" on chr21 is TRPM2.
