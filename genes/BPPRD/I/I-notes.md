# Gene I (DNA-directed DNA polymerase P1) - Curation Notes

## Overview
- **UniProt ID**: P10479 (`DPOL_BPPRD`)
- **Gene symbol**: `I` (Protein P1)
- **Organism**: Enterobacteria phage PRD1 (`NCBITaxon:10658`)
- **Function**: Protein-primed family B DNA-directed DNA polymerase (EC 2.7.7.7) with an N-terminal 3'-5' proofreading exonuclease domain and a C-terminal DNA polymerase domain. Replicates the linear dsDNA genome of phage PRD1 from the terminal protein P8 primer in the host cell cytoplasm [PMID:1655759, file:BPPRD/I/I-uniprot.txt].

## Key Literature & Evidence
- [PMID:1655759] Savilahti et al. (1991) cloned and purified PRD1 DNA polymerase P1 to homogeneity, demonstrating that DNA polymerase (GO:0003887), single-strand-specific 3'-5' exonuclease (GO:0008408), and P8-dGMP replication initiation complex formation activities co-sediment with the 65 kDa P1 protein, and reconstituted full-length in vitro PRD1 DNA replication (GO:0039693).
- [file:BPPRD/I/I-uniprot.txt] Documents the N-terminal 3'-5' proofreading exonuclease domain and C-terminal type-B DNA polymerase domain.

## Curation Decisions
- **ACCEPT**: `GO:0003887` (DNA-directed DNA polymerase activity, IDA from PMID:1655759 and IEA), `GO:0003677` (DNA binding, IEA), `GO:0039693` (viral DNA genome replication, IEA).
- **MODIFY**: `GO:0004527` (exonuclease activity) -> `GO:0008408` (3'-5' exonuclease activity) and `GO:0006260` (DNA replication) -> `GO:0039693` (viral DNA genome replication), supported by biochemical characterization in [PMID:1655759].
- **TOO_GENERAL**: Broad parent terms (`GO:0000166`, `GO:0003676`, `GO:0003824`, `GO:0004518`, `GO:0016740`, `GO:0016779`, `GO:0016787`, `GO:0034061`, `GO:0071897`, `GO:0140640`).
- **NEW**: `GO:0030430` (host cell cytoplasm) as the site of viral DNA replication in the Gram-negative bacterial host.
