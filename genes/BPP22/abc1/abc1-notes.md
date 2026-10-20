# Gene Review Notes: Salmonella phage P22 `abc1` (`P11190`, Anti-RecBCD protein 1)

## Overview
- **Gene symbol**: `abc1`
- **UniProt ID**: `P11190` (`ABC1_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Protein length**: 94 amino acids (10.9 kDa)
- **Operon / genomic context**: Encoded in the early left ($P_L$) recombination operon immediately downstream of `erf` and upstream of `abc2` ([PMID:3660589](https://pubmed.ncbi.nlm.nih.gov/3660589/), [PMID:2738922](https://pubmed.ncbi.nlm.nih.gov/2738922/), [PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/)).

## Function and Domain Architecture
- **Anti-RecBCD protein 1 (Abc1)**:
  - Murphy et al. (1987) [PMID:3660589] sequenced the P22 `abc` (anti-RecBCD) locus between `erf` and `c3` and dissected the roles of `abc1` (10.9 kDa) and `abc2` (11.6 kDa) using deletion mutants and plasmid-phage complementation:
    - `"Previous studies (A. C. Fenton and A. R. Poteete, 1984, Virology 134, 148-160) have shown that this region encodes a function that is required for efficient growth of P22 in wild-type, but not in recB- Salmonella. The gene or genes encoding this function were designated abc (anti-recBCD)."`
    - `"The phenotypes of the deletion mutants, and the results of plasmid-phage complementation tests, indicate that Abc activity depends primarily on sequences that encode the 11.6-kDa polypeptide; the 10.9-kDa polypeptide-encoding sequence makes a minor contribution to Abc activity as well. These sequences have been designated abc2 and abc1, respectively."`
  - Domain architecture in `abc1-uniprot.txt`: Contains a winged helix-like DNA-binding domain superfamily fold (`Gene3D:1.10.10.10`, `InterPro:IPR036388` `WH-like_DNA-bd_sf`).
  - Functional role: Together with the major anti-RecBCD subunit Abc2 (`P11191`), Abc1 contributes to modulating the host RecBCD helicase-nuclease complex (`GO:0030234` `enzyme regulator activity`), protecting linear double-stranded phage DNA from exonucleolytic degradation and promoting phage homologous recombination (`GO:0006310` `DNA recombination`) in the host cell cytoplasm (`GO:0030430`).

## Review of Existing GO Annotations
- **Existing GOA annotations**: None (`abc1-goa.tsv` is empty).
- **Proposed `NEW` annotations**:
  - `GO:0030234` (`enzyme regulator activity`, `enables`): Modulates the activity of the host RecBCD nuclease (`file:genes/BPP22/abc1/abc1-uniprot.txt`, [PMID:3660589](https://pubmed.ncbi.nlm.nih.gov/3660589/)).
  - `GO:0006310` (`DNA recombination`, `involved_in`): Modulation of host RecBCD protects linear phage dsDNA and promotes recombination during P22 lytic infection ([PMID:3660589](https://pubmed.ncbi.nlm.nih.gov/3660589/)).
  - `GO:0030430` (`host cell cytoplasm`, `located_in`): Acts in the cytoplasm of the infected *Salmonella* host cell ([PMID:3660589](https://pubmed.ncbi.nlm.nih.gov/3660589/)).
