# Gene Review Notes: Salmonella phage P22 `erf` (`P04892`, Essential recombination function protein Erf)

## Overview
- **Gene symbol**: `erf`
- **UniProt ID**: `P04892` (`ERF_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Protein length**: 205 amino acids (22.9 kDa)
- **Operon / genomic context**: Encoded in the early left ($P_L$) operon immediately downstream of `arf` and upstream of `abc1`-`abc2`, at the syntenic position of the lambda `red` (`exo`-`bet`) recombination module ([PMID:6210989](https://pubmed.ncbi.nlm.nih.gov/6210989/), [PMID:2738922](https://pubmed.ncbi.nlm.nih.gov/2738922/), [PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/)).

## Function and Structural Architecture
- **Ring-forming single-stranded DNA-binding / annealing recombinase (Erf)**:
  - Bacteriophage P22 enters the host *Salmonella* cell as a terminally redundant, circularly permuted linear dsDNA molecule. To replicate and package DNA, the linear genome must first circularize via homologous recombination between its terminal repeats ([PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/, "The linear double-stranded viral DNA enters the host cell, and circularization occurs, mediated by the phage-encoded protein Erf and the host proteins RecA and gyrase ( 50 , 67 ).")).
  - Erf ("essential recombination function") promotes homologous recombination and is strictly essential for P22 lytic growth in a `recA`-deficient host (`file:genes/BPP22/erf/erf-uniprot.txt`, `"CC   -!- FUNCTION: Promotes homologous recombination. Essential for P22 growth in a recA, but not a wild-type, host."`).
  - Domain architecture: Founding member of the viral Erf single-stranded DNA annealing recombinase family (`InterPro:IPR007499` `ERF_bacteria_virus`, `Pfam:PF04404` `ERF`).
  - Biochemical and structural characterization by Murphy et al. (1987) [PMID:3612797]:
    - Purified Erf self-assembles into discrete ring-like oligomers with protruding "tooth-like" C-terminal domains and binds single-stranded DNA (`ssDNA`) with high affinity.
    - Limited proteolysis generating N-terminal 149-residue and 130-residue fragments demonstrated that both fragments retain the ring-like oligomeric core, while residues 131–149 (an interdomain segment rich in basic amino acids) form a critical determinant for single-stranded DNA binding: `"Intact Erf and the 149 residue fragment have similar affinities for single-stranded DNA; the affinity of the 130 residue fragment is 40-fold lower in low salt at pH 6.0."` ([PMID:3612797](https://pubmed.ncbi.nlm.nih.gov/3612797/)).

## Review of Existing GO Annotations
- **`GO:0003677` (`DNA binding`, `IEA`, `GO_REF:0000043`)**:
  - **Action**: `MODIFY` -> `GO:0003697` (`single-stranded DNA binding`).
  - **Reasoning**: Direct biochemical assays of purified P22 Erf and its proteolytic fragments demonstrate that Erf specifically binds single-stranded DNA to mediate homologous recombination ([PMID:3612797](https://pubmed.ncbi.nlm.nih.gov/3612797/)). Refining `GO:0003677` (`DNA binding`) to `GO:0003697` (`single-stranded DNA binding`) captures its experimentally established substrate specificity.
- **Proposed `NEW` annotations**:
  - `GO:0006310` (`DNA recombination`, `involved_in`): Captures the primary biological process of Erf in mediating homologous recombination and circularization of the terminally redundant P22 genome ([PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/), `file:genes/BPP22/erf/erf-uniprot.txt`).
  - `GO:0030430` (`host cell cytoplasm`, `located_in`): Erf functions in the cytoplasm of the infected *Salmonella* host cell where phage DNA circularization and recombination occur ([PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/)).
