# Mlac1 notes

## Re-review 2026-10-01 (GOA refresh)

- New GOA row reviewed: GO:0009986 cell surface (ISS, GO_REF:0000024, from A. fumigatus
  Abr2 E9RBR0, which has EXP cell-surface evidence) -> ACCEPT (homology-based; consistent
  with conidial pigment role).
- GO:0046872 metal ion binding (IEA, GO_REF:0000043 keyword mapping) vanished from the
  current GOA snapshot -> `retired: true` (REMOVE review kept).
- NEW proposal revised: GO:0030639 polyketide biosynthetic process -> GO:0046148 pigment
  biosynthetic process (ISS). Comparator check via QuickGO (2026-10-01): the characterized
  cluster laccase Abr2 (E9RBR0) carries GO:0046148 pigment biosynthetic process (IMP,
  PMID:10515939) and GO:0042438 melanin biosynthetic process, but not polyketide
  biosynthetic process. Mlac1's step is inferred (UniProt: "Probable") - no Mlac1
  deletion/assay in PMID:29958281. core_functions updated to match; description hedged.
- Added verbatim UniProt supporting text to ACCEPT rows that lacked it.
