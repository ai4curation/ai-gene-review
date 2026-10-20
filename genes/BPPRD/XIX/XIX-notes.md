# Gene XIX (Single-stranded DNA-binding protein P19) - Curation Notes

## Overview
- **UniProt ID**: P17638 (`VP19_BPPRD`)
- **Gene symbol**: `XIX` (Protein P19)
- **Organism**: Enterobacteria phage PRD1 (`NCBITaxon:10658`)
- **Function**: Nonstructural single-stranded DNA-binding protein that associates with unpackaged viral DNA in the host cytoplasm and is removed during genome packaging [PMID:17202207, file:BPPRD/XIX/XIX-uniprot.txt].

## Curation Decisions
- **REMOVE**: `GO:0000166` (nucleotide binding, IEA from KW-0547) — false positive keyword mapping; P19 binds ssDNA, not free nucleotides.
- **MODIFY**: `GO:0003677` (DNA binding) -> `GO:0003697` (single-stranded DNA binding) based on [PMID:17202207, file:BPPRD/XIX/XIX-uniprot.txt].
- **NEW**: `GO:0030430` (host cell cytoplasm).
