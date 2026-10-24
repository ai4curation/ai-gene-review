# Gene Review Notes: Salmonella phage P22 `ninG` (`Q38667`, Protein ninG)

## Overview
- **Gene symbol**: `ninG`
- **UniProt ID**: `Q38667` (`NING_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Protein length**: 203 amino acids (23.7 kDa)
- **Operon / genomic context**: Encoded in the early right ($P_R$) `nin` region between `ninF` and `ninY`/`ninH` ([PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/), [PMID:12562822](https://pubmed.ncbi.nlm.nih.gov/12562822/)).

## Function and Structural Architecture
- **Crossover junction / Holliday junction endodeoxyribonuclease NinG (Rap ortholog)**:
  - Vander Byl & Kropinski (2000) [PMID:11053393] demonstrated that `ninG` is one of the three genes sharing the highest sequence identity (>85% DNA identity, verified at the amino acid level) between Salmonella phage P22 and Escherichia phage lambda:
    - `"Using the BLAST2 algorithm of Tatusova and Madden, we identified five >300-bp regions in lambda DNA which shared >85% sequence identity with the P22 sequence ( 66 ). These are indicated in Fig. 1 . The regions of greatest DNA sequence similarity correspond to genes ninB , ninG , and 23 . This is also verified at the amino acid level."`
  - Domain architecture in `ninG-uniprot.txt`: Member of the lambdoid NinG / Rap Holliday junction resolvase family (`InterPro:IPR008713` `Phage_lambda_NinG`, `Pfam:PF05766` `NinG`, `"CC   -!- SIMILARITY: Belongs to the ninG family. {ECO:0000305}."`).
  - Biochemical characterization of the >85% identical lambdoid NinG (Rap) protein by Sharples et al. (1998) [PMID:9811830] and Sharples et al. (2004) [PMID:15223317]:
    - `"In the presence of manganese ions, Rap acts as an endonuclease that cleaves at the branch point of Holliday and D-loop substrates."` ([PMID:9811830](https://pubmed.ncbi.nlm.nih.gov/9811830/)).
    - `"Here, we demonstrate that Rap can mediate symmetrical resolution of 50 bp and chi Holliday structures containing larger homologous cores."` ([PMID:15223317](https://pubmed.ncbi.nlm.nih.gov/15223317/)).
  - Thus, P22 NinG is a structure-specific crossover junction endodeoxyribonuclease (`GO:0008821`) that resolves branched DNA recombination intermediates during homologous recombination (`GO:0006310`) in the host cell cytoplasm (`GO:0030430`).

## Review of Existing GO Annotations
- **Existing GOA annotations**: None (`ninG-goa.tsv` is empty).
- **Proposed `NEW` annotations**:
  - `GO:0008821` (`crossover junction DNA endonuclease activity`, `enables`, `ISS` from lambda NinG/Rap): Supported by >85% sequence identity to phage lambda NinG/Rap ([PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/)), conserved `InterPro:IPR008713` / `Pfam:PF05766` domain, and biochemical proof of Holliday/D-loop branch-point endonuclease activity ([PMID:9811830](https://pubmed.ncbi.nlm.nih.gov/9811830/), [PMID:15223317](https://pubmed.ncbi.nlm.nih.gov/15223317/)).
  - `GO:0006310` (`DNA recombination`, `involved_in`, `ISS` from lambda NinG/Rap): Resolves Holliday junction and D-loop intermediates during phage homologous recombination ([PMID:9811830](https://pubmed.ncbi.nlm.nih.gov/9811830/), [PMID:15223317](https://pubmed.ncbi.nlm.nih.gov/15223317/)).
  - `GO:0030430` (`host cell cytoplasm`, `located_in`, `ISS`): Functions in the cytoplasm of the infected *Salmonella* host cell ([PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/), [PMID:9811830](https://pubmed.ncbi.nlm.nih.gov/9811830/)).
