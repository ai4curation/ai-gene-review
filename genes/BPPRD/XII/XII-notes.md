# Gene XII (Single-stranded DNA-binding protein P12) - Curation Notes

## Overview
- **UniProt ID**: P17637 (`SSB_BPPRD`)
- **Gene symbol**: `XII` (Protein P12)
- **Organism**: Enterobacteria phage PRD1 (`NCBITaxon:10658`)
- **Function**: Essential monomeric/multimeric single-stranded DNA-binding protein (SSB) required for protein-primed viral DNA genome replication in the host cell cytoplasm [file:BPPRD/XII/XII-uniprot.txt].

## Curation Decisions
- **REMOVE**: `GO:0000166` (nucleotide binding, IEA from KW-0547) — false positive keyword mapping; P12 binds ssDNA polymers, not monomeric nucleotides.
- **MODIFY**: `GO:0003677` (DNA binding) -> `GO:0003697` (single-stranded DNA binding) based on [file:BPPRD/XII/XII-uniprot.txt].
- **NEW**: `GO:0039693` (viral DNA genome replication) and `GO:0030430` (host cell cytoplasm).
