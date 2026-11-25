# Bacteriophage lambda gene ea59 (Putative AAA+ ATPase / antiviral defense-associated protein Ea59; UniProt P03754)

## Overview
Gene `ea59` of *Escherichia phage lambda* (`NCBITaxon:2681611`) encodes a 525-amino-acid (59.5 kDa) protein (Ea59) located in the nonessential *b2* region of the phage genome adjacent to `ea31` and `ea47` [file:LAMBD/ea59/ea59-uniprot.txt]. Identified originally as a ~59 kDa polypeptide expressed from the *b2* region, `ea59` is nonessential for lytic growth or lysogeny in standard *Escherichia coli* K-12 laboratory strains.

## Bioinformatics and Domain Architecture
1. **AAA+ ATPase Core Domain**: Sequence classification in UniProt and InterPro places Ea59 in the P-loop containing nucleoside triphosphate hydrolase superfamily (`InterPro:IPR027417`), with a conserved AAA+ ATPase core domain (`InterPro:IPR003959` ATPase_AAA_core; `Pfam:PF13304` AAA_21) [file:LAMBD/ea59/ea59-uniprot.txt].
2. **Antiviral Defense / Excinuclease ATPase Homology**: Ea59 is classified in `InterPro:IPR051396` (`Bact_Antivir_Def_Nuclease`, Bacterial antiviral defense nuclease) and `PANTHER:PTHR43581:SF2` (`EXCINUCLEASE ATPASE SUBUNIT`), homologous to ABC/AAA+ ATPase subunits of OLD-like and GajA/septu-like bacterial and prophage antiviral defense nucleases [file:LAMBD/ea59/ea59-uniprot.txt]. Notably, in the lambda *b2* locus, `ea59` lies immediately upstream of `ea31`, which encodes an HNH endonuclease domain-containing protein (`InterPro:IPR003615`), consistent with an ATPase-nuclease gene pair architecture.

## GO Annotation Review Summary
- **Accepted Core Terms**:
  - `GO:0005524` (`ATP binding`, IEA `GO_REF:0000002` from `InterPro:IPR003959`): Supported by the conserved P-loop NTPase / AAA+ ATPase core domain (`IPR003959`, `PF13304`).
  - `GO:0016887` (`ATP hydrolysis activity`, IEA `GO_REF:0000002` from `InterPro:IPR003959`): Core predicted enzymatic activity of the AAA+ ATPase domain (`IPR003959`).
