# shc1 (Schizosaccharomyces japonicus) notes

## 2026-10-01 re-review (GOA refresh)

- Three IEA rows are no longer present in the current GOA snapshot and were marked
  `retired: true` (reviews retained): GO:0008610 lipid biosynthetic process (GO_REF:0000117),
  GO:0016829 lyase activity (GO_REF:0000043), GO:0016853 isomerase activity (GO_REF:0000043).
- New ARBA row GO:0006629 lipid metabolic process (GO_REF:0000117) reviewed: MODIFY ->
  GO:0019746 hopanoid biosynthetic process (consistent with the EXP row for the same term).
- Lyase activity judgment corrected REMOVE -> KEEP_AS_NON_CORE: the earlier reasoning that SHC
  performs no lyase chemistry was wrong; UniProt assigns EC 4.2.1.129 (squalene + H2O =
  hopan-22-ol) as well as EC 5.4.99.17, and diplopterol (hopan-22-ol) is the major hopanoid.
- Dropped NEW GO:0071454 cellular response to anoxia (and from core_functions): the evidence is
  that shc1 deletion prevents anaerobic growth (necessity), while hopanoids are made at high levels
  even under oxygen, so Shc1 is not a participant in an anoxia response per se.
- Added supporting evidence to the NEW GO:0019746 hopanoid biosynthetic process row (previously
  empty) and replaced a placeholder deep-research quote with verbatim text.
