# Gene Review Notes: Salmonella phage P22 `arf` (`P14112`, Accessory recombination function protein Arf)

## Overview
- **Gene symbol**: `arf`
- **UniProt ID**: `P14112` (`VARF_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Protein length**: 47 amino acids (5.5 kDa)
- **Operon / genomic context**: Encoded in the early left ($P_L$) operon immediately upstream of `erf` and downstream of `kil` ([PMID:2738922](https://pubmed.ncbi.nlm.nih.gov/2738922/), [PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/)).

## Function and Domain Architecture
- **Accessory recombination function protein (Arf)**:
  - Identified and genetically characterized by Semerjian et al. (1989) [PMID:2738922]:
    - `"Gene arf (accessory recombination function) is located just upstream from erf; it is essential for P22 growth in the absence of kil or other genes upstream in PL. The growth defect of P22 bearing a deletion that removes arf is complemented by expression of either arf or the lambda red genes from plasmids."`
    - `"Measurement of recombination focus formation following infection by P22 deletion mutants provides further support for the assignment of recombination-related functions to the products of genes arf and kil."`
  - Domain architecture in `arf-uniprot.txt`: Member of the bacteriophage Arf family (`InterPro:IPR020293` `Arf`, `Pfam:PF17585` `Phage_Arf`).
  - While genetic complementation by lambda `red` (`exo`-`bet`) and recombination assays establish that Arf participates in phage homologous recombination (`GO:0006310` `DNA recombination`) in the host cell cytoplasm (`GO:0030430`), the precise molecular mechanism or biochemical activity of this small 47-residue polypeptide has not yet been biochemically determined.

## Review of Existing GO Annotations
- **Existing GOA annotations**: None (`arf-goa.tsv` is empty).
- **Proposed `NEW` annotations**:
  - `GO:0006310` (`DNA recombination`, `involved_in`): Supported by genetic deletion and lambda `red` complementation experiments demonstrating that Arf provides an accessory recombination function during P22 infection ([PMID:2738922](https://pubmed.ncbi.nlm.nih.gov/2738922/)).
  - `GO:0030430` (`host cell cytoplasm`, `located_in`): Acts during phage recombination in the cytoplasm of the infected *Salmonella* host cell ([PMID:2738922](https://pubmed.ncbi.nlm.nih.gov/2738922/)).
