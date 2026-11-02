# SMIM10L1 notes

## 2026-10-08 Tier 4 microprotein review

### Locus
- UniProt P0DMW3 (SIML1_HUMAN), 68 aa, PE1. Family: InterPro
  IPR029367 SMIM10, Pfam PF15118 DUF4560, PANTHER PTHR34446:SF5. N-terminal 1-21 disordered
  (Ala/Pro/Ser-rich). UniProt annotates no TRANSMEM feature and no SUBCELLULAR LOCATION,
  despite the "small integral membrane protein" name; the C-terminal half is hydrophobic
  (FCKGLSRTLLAFFELAWQLRMNFPYFYVAGSVILNIRLQVHI).
- HGNC: gene with protein product. Ensembl ENSG00000256537 protein_coding, chr12.
- HPA: RNA low tissue specificity, detected in all tissues; no IF location.
- Paralogues in repo: genes/human/SMIM10 (reviewed in Tier 2).

### Literature (PubMed "SMIM10L1", 2 hits, 2026-10-08)
- PMID:35290761 (abstract only): SMIM10L1 was the most down-regulated gene after PTEN
  knockdown in adipose progenitor cells; "SMIM10L1 downregulation in APCs led to an enhanced
  adipocyte differentiation"; knockdown also lowered PTEN and raised PI3K/AKT/mTOR signalling;
  "We computationally predicted an α-helical structure and membrane association of SMIM10L1."
- PMID:36672800: GWAS/TWAS of childhood caries; incidental.

### GOA row
- GO:0005739 mitochondrion, HTP, PMID:34800366 (MitoCoP). The cached full text does not name
  SMIM10L1 (the assignment is in the supplementary tables), so the per-protein evidence
  cannot be checked here. MitoCoP combines subtractive and spatial proteomics, importomics and
  curation under stringent criteria. ACCEPT, deferring to the curator; this is the only
  location evidence.

### No NEW
- Adipogenesis: knockdown phenotype only (necessity/indirect via PTEN/AKT); fails the
  participation test. Not proposed.
