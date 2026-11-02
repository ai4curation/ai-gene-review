# KIAA0040 notes

## 2026-10-08 Tier 4 microprotein review

### Locus
- UniProt Q15053 (K0040_HUMAN), 99 aa, PE1, "Uncharacterized protein KIAA0040". Predicted
  single TM helix 27..47 (ECO:0000255), then a disordered basic tail with a poly-Lys run
  (65..74). UniProt location "Membrane; Single-pass membrane protein" is sequence-inferred.
  Several older cDNA translations flagged "Wrong choice of CDS" (the 1994 KIAA cDNA was
  originally assigned a different ORF).
- PANTHER PTHR40382 (SF1 "RIKEN CDNA 4930523C07 GENE"), InterPro IPR039964 KIAA0040-like:
  conserved in mammals (mouse 4930523C07Rik). HGNC: gene with protein product, alias IAMP.
  Ensembl ENSG00000235750 protein_coding.
- HPA (2026-10-08): RNA "Tissue enhanced (placenta)", 94.4 nTPM in placenta. Antibody IF main
  location "Nucleoplasm" - at odds with the predicted TM helix; antibody-based and not
  validated by a second method.

### Literature (PubMed "KIAA0040", 18 hits, 2026-10-08)
- Mostly GWAS (alcohol dependence, e.g. PMID:21956439), exome studies, and expression
  signatures; none functional at the protein level.
- One functional study: glioma [PMID:38661644, full text] - shRNA knockdown and
  overexpression; "KIAA0040 enhances glioma growth, migration and invasion by activating the
  JAK2/STAT3 pathway." Single lab, cancer cell lines; no mechanism for how a 99-aa
  single-pass protein affects JAK2.
- Immune transcriptomics [PMID:42120540, abstract only]: KIAA0040 "co-expressed with genes
  involved in innate immunity" after pathogen stimulation of primary immune cells.

### Decisions
- membrane IEA (SubCell): ACCEPT; most specific supportable location.
- No NEW: glioma JAK2/STAT3 data is a single-lab cancer-line phenotype, does not meet the
  participation bar for a process term.
