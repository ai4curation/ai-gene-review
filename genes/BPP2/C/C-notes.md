# Bacteriophage P2 Gene C (Immunity repressor C; UniProt P04132)

## Overview
Gene **C** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes the 99-amino-acid immunity repressor C (11.1 kDa; `UniProt:P04132`). Repressor C establishes and maintains the lysogenic state by binding as a homodimer to two operator sites (`O1` and `O2`) overlapping the early lytic promoter `Pe`, repressing transcription of the early replication operon (`cox-B-A`), while regulating its own promoter `Pc` (`PMID:6330728`, `PMID:2826134`, `file:BPP2/C/C-uniprot.txt`). Unlike phage lambda CI, P2 repressor C is a small (99-aa), non-inducible by UV/SOS (non-cleavable) Cro/C1-type helix-turn-helix DNA-binding protein (`InterPro:IPR010982`).

## Key Literature & Experimental Evidence
- **PMID:6330728** (*DNA sequences of the repressor gene and operator region of bacteriophage P2.*):
  - Determined the nucleotide sequence of gene `C` and the early operator region: `"The nucleotide sequence of the repressor gene C of the temperate phage P2 has been determined. It codes for a nonbasic polypeptide, 99 amino acids long."`
  - Mapped virulent operator mutations: `"The operator region for the early replication functions was located by sequencing the DNA of three virulent mutants. The sequence indicates that there are two repressor-binding sites."`
- **PMID:2826134** (*The cox protein of bacteriophage P2 inhibits the formation of the repressor protein and autoregulates the early operon.*):
  - Demonstrated mutual antagonism between C and Cox at the `Pc`/`Pe` switch region.

## Curation Decisions
- **Molecular Function**:
  - `GO:0003677` (`DNA binding`, IEA): **MODIFY** to `GO:0001227` (`DNA-binding transcription repressor activity, RNA polymerase II-specific` is eukaryotic; for prokaryotes/general use `GO:0001217` `DNA-binding transcription repressor activity` and/or `GO:0000976` `transcription cis-regulatory region binding`).
  - Add `NEW` for `GO:0001217` (`DNA-binding transcription repressor activity`) and `GO:0000976` (`transcription cis-regulatory region binding`) supported by `PMID:6330728`.
- **Biological Process**:
  - Add `NEW` for `GO:0045892` (`negative regulation of DNA-templated transcription`) and `GO:0019046` (`release from viral latency` / or `GO:0075713` `establishment of integrated proviral latency`? Actually `GO:0045892` `negative regulation of DNA-templated transcription` is directly supported by operator-mediated repression of the early operon in `PMID:6330728`).
- **Cellular Component**:
  - Add `NEW` for `GO:0030430` (`host cell cytoplasm`).
