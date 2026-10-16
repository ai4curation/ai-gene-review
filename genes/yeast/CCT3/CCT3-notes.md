## 2026-10-01 current-GOA refresh

- Ran `just fetch-gene yeast CCT3 --force`: current GOA has 13 rows and 12
  exact source signatures because the `PMID:16762366` protein-folding IDA row
  is now emitted by both SGD and ComplexPortal with the same term/evidence/source
  signature. The refresh added InterPro `GO:0005524` ATP binding and
  ComplexPortal/PMID:21701561 `GO:0005832` CCT-complex membership rows, removed
  the old `GO:0051082` IBA/IEA/IDA assertions, removed the UniProt keyword
  nucleotide-binding row, and retired two generic Cct3-Eft2 protein-binding
  rows that are no longer live.
- The current PTHR11353 PAINT snapshot keeps `PTN004253040` for inherited
  CCT/TRiC protein folding and `PTN000143681` for gamma-subunit CCT complex
  membership; no current PAINT row carries obsolete `GO:0051082`.
- PubMed/Web searches for exact CCT3/Cct3/YJL014W mentions in 2025-2026 did not
  find a new direct *S. cerevisiae* CCT3 functional paper beyond database
  refreshes and broad yeast studies where CCT3 was not assayed as the primary
  functional subject.
