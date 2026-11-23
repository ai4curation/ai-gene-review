# P14 (P14_BPPH6, Q38563) — Curation Notes

## Overview
- **Organism:** *Pseudomonas* phage phi6 (`NCBITaxon:2928686`, *Cystovirus phi6*)
- **Gene / Protein:** `P14` / Protein P14 (`UniProtKB:Q38563`, 62 AA)
- **Genomic Segment:** Encoded near the 5' end of the large (L) dsRNA segment.

## Biological Role in the Cystovirus Lifecycle
1. **Small Nonstructural Accessory Protein (`GO:0003674`, `GO:0030430`):**
   - P14 is a 62-residue (6.9 kDa), low-abundance nonstructural protein encoded by a small open reading frame on the large (L) dsRNA segment upstream of genes 7, 2, 4, and 1 [file:BPPH6/P14/P14-uniprot.txt].
   - Characterization of a gene 14 nonsense mutant demonstrated that P14 is not strictly essential for plaque formation on standard hosts, but is needed for optimal phage development [file:BPPH6/P14/P14-uniprot.txt].
   - Its specific molecular biochemical activity and host or viral binding partners remain unknown.

## Curation Decisions
- **Existing GOA Annotations:** None (`P14-goa.tsv` is empty).
- **New Annotations (`action: NEW`):**
  - `GO:0003674` (`molecular_function`, `enables`, `ND` from `file:BPPH6/P14/P14-uniprot.txt`): The specific biochemical activity of P14 is unknown despite genetic characterization showing it contributes to optimal phage development.
  - `GO:0030430` (`host cell cytoplasm`, `located_in`, `IC` from `file:BPPH6/P14/P14-uniprot.txt`): P14 is a low-abundance nonstructural viral protein expressed inside the infected bacterial cell.
