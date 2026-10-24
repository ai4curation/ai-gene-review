# Gene Review Notes: Salmonella phage P22 `abc2` (`P11191`, Anti-RecBCD protein 2)

## Overview
- **Gene symbol**: `abc2`
- **UniProt ID**: `P11191` (`ABC2_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Protein length**: 97 amino acids (11.6 kDa)
- **Operon / genomic context**: Encoded in the early left ($P_L$) recombination operon immediately downstream of `abc1` and `erf` ([PMID:3660589](https://pubmed.ncbi.nlm.nih.gov/3660589/), [PMID:2738922](https://pubmed.ncbi.nlm.nih.gov/2738922/), [PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/)).

## Function and Structural Architecture
- **Primary anti-RecBCD modulator (Abc2)**:
  - Murphy et al. (1987) [PMID:3660589] identified `abc2` (encoding the 11.6-kDa polypeptide) as the primary determinant of phage P22 anti-RecBCD (`Abc`) activity required for efficient phage growth and DNA replication/recombination in wild-type (`recB+`), but not `recB-`, *Salmonella* hosts:
    - `"Previous studies (A. C. Fenton and A. R. Poteete, 1984, Virology 134, 148-160) have shown that this region encodes a function that is required for efficient growth of P22 in wild-type, but not in recB- Salmonella. The gene or genes encoding this function were designated abc (anti-recBCD)."`
    - `"The phenotypes of the deletion mutants, and the results of plasmid-phage complementation tests, indicate that Abc activity depends primarily on sequences that encode the 11.6-kDa polypeptide; the 10.9-kDa polypeptide-encoding sequence makes a minor contribution to Abc activity as well. These sequences have been designated abc2 and abc1, respectively."`
  - Unlike lambda Gam (which acts as a DNA mimic blocking DNA binding by RecBCD entirely), P22 Abc2 binds directly to the RecC subunit of the host RecBCD complex (resolved by cryo-EM in `PDB:8B1T` and `PDB:8B1U`, `file:genes/BPP22/abc2/abc2-uniprot.txt`) and modulates RecBCD enzymatic activity, inhibiting its destructive double-stranded DNA exonuclease activity (`GO:0030234` `enzyme regulator activity`) so that linear phage dsDNA is protected and converted into recombination intermediates for Erf-mediated homologous recombination (`GO:0006310` `DNA recombination`).
  - Domain architecture in `abc2-uniprot.txt`: Founding member of `InterPro:IPR020500` (`Phage_P22_anti-RecBCD_p2`) and `Pfam:PF11043` (`Anti-RecBCD_p2`); cryo-EM structures `PDB:8B1T` (3.40 A) and `PDB:8B1U` (3.80 A) cover residues 1–97 (`A=1-97`).

## Review of Existing GO Annotations
- **Existing GOA annotations**: None (`abc2-goa.tsv` is empty).
- **Proposed `NEW` annotations**:
  - `GO:0030234` (`enzyme regulator activity`, `enables`): Directly binds and modulates the enzymatic activity of the host RecBCD helicase-nuclease complex ([PMID:3660589](https://pubmed.ncbi.nlm.nih.gov/3660589/), `file:genes/BPP22/abc2/abc2-uniprot.txt`).
  - `GO:0006310` (`DNA recombination`, `involved_in`): Protects linear viral dsDNA from RecBCD exonucleolytic degradation and channels RecBCD into promoting phage homologous recombination ([PMID:3660589](https://pubmed.ncbi.nlm.nih.gov/3660589/), `file:genes/BPP22/abc2/abc2-uniprot.txt`).
  - `GO:0030430` (`host cell cytoplasm`, `located_in`): Acts on the cytoplasmic host RecBCD complex in the infected *Salmonella* host cell ([PMID:3660589](https://pubmed.ncbi.nlm.nih.gov/3660589/)).
