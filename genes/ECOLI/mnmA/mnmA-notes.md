# mnmA (E. coli K-12) curation notes

## Sources checked

- UniProtKB record (genes/ECOLI/mnmA/mnmA-uniprot.txt) and GOA table.
- Cached publications: PMID:12549933, PMID:16387657, PMID:16871210, PMID:3881393
  (abstract-only); PMID:18304323 and PMID:38466471 (full text).
- No provider deep-research file was generated for this gene.

## Findings

- Activity: in vitro s2U synthesis [PMID:12549933 "The activity requires MnmA,
  Mg-ATP, l-cysteine, and the cysteine desulfurase IscS."]; adenylated
  intermediate [PMID:16871210 "The adenylated RNA intermediate is trapped."].
- Generic sulfurtransferase/transferase rows are MODIFIED to GO:0103016; tRNA
  processing/modification rows to GO:0002143.
- GO:1990228 rows (IBA, IPI) kept as non-core, as for TusE: MnmA associates with
  TusE but is not a TusBCD subunit.
- The boric-acid IMP row (GO:0097532) is a pleiotropic screen phenotype and is
  marked over-annotated.
