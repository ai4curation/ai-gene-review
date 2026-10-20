# Gene Review Notes: Salmonella phage P22 `ninB` (`Q38662`, Protein ninB)

## Overview
- **Gene symbol**: `ninB`
- **UniProt ID**: `Q38662` (`NINB_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Protein length**: 145 amino acids (16.5 kDa)
- **Operon / genomic context**: First gene of the early right ($P_R$) `nin` (N-independent) region located between the replication gene `12` and the late antiterminator gene `23` ([PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/)).

## Function and Structural Architecture
- **Recombination mediator protein NinB (lambda Orf ortholog)**:
  - Vander Byl & Kropinski (2000) [PMID:11053393] demonstrated that `ninB` is one of the three regions of highest sequence conservation (>85% DNA identity, verified at the amino acid level) between Salmonella phage P22 and Escherichia phage lambda:
    - `"Using the BLAST2 algorithm of Tatusova and Madden, we identified five >300-bp regions in lambda DNA which shared >85% sequence identity with the P22 sequence ( 66 ). These are indicated in Fig. 1 . The regions of greatest DNA sequence similarity correspond to genes ninB , ninG , and 23 . This is also verified at the amino acid level."`
  - Domain architecture in `ninB-uniprot.txt`: Member of the NinB recombination mediator family (`InterPro:IPR008711` `Recombinase_NinB`, `InterPro:IPR036619` `NinB_sf`, `Pfam:PF05772` `NinB`, `Gene3D:1.10.3790.10` `NinB`, `SUPFAM:SSF103370` `NinB`).
  - Functional characterization of the closely conserved (>85% identical) lambdoid NinB/Orf protein ([PMID:16076958](https://pubmed.ncbi.nlm.nih.gov/16076958/)):
    - Acts as a homodimeric recombination mediator functionally analogous to the host RecFOR complex during the early stages of homologous recombination (`GO:0006310` `DNA recombination`).
    - Directly binds single-stranded DNA (`GO:0003697` `single-stranded DNA binding`) and interacts with host single-stranded DNA-binding protein (SSB) in the host cell cytoplasm (`GO:0030430`) to facilitate loading of recombinases onto SSB-coated ssDNA.

## Review of Existing GO Annotations
- **Existing GOA annotations**: None (`ninB-goa.tsv` is empty).
- **Proposed `NEW` annotations**:
  - `GO:0003697` (`single-stranded DNA binding`, `enables`, `ISS` from lambda NinB/Orf): Supported by >85% sequence identity to phage lambda NinB/Orf ([PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/)), conserved NinB recombinase domain (`InterPro:IPR008711`, `Pfam:PF05772`), and experimental demonstration of ssDNA binding by NinB/Orf ([PMID:16076958](https://pubmed.ncbi.nlm.nih.gov/16076958/)).
  - `GO:0006310` (`DNA recombination`, `involved_in`, `ISS` from lambda NinB/Orf): Functions as a RecFOR-like recombination mediator during phage homologous recombination ([PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/), [PMID:16076958](https://pubmed.ncbi.nlm.nih.gov/16076958/)).
  - `GO:0030430` (`host cell cytoplasm`, `located_in`, `ISS`): Acts in the cytoplasm of the infected *Salmonella* host cell ([PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/), [PMID:16076958](https://pubmed.ncbi.nlm.nih.gov/16076958/)).
