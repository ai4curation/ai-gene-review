# Bacteriophage lambda gene ea31 (Uncharacterized HNHc domain-containing protein Ea31; UniProt P03753)

## Overview
Gene `ea31` of *Escherichia phage lambda* (`NCBITaxon:2681611`) encodes a 296-amino-acid (33.5 kDa) early/accessory protein (Ea31) located in the nonessential *b2* region of the phage genome (between `ea47` and `ea59`, transcribed leftward from early/constitutive promoters in the *b2* region) [file:LAMBD/ea31/ea31-uniprot.txt]. The *b2* region is dispensable for standard lytic and lysogenic growth in laboratory *Escherichia coli* K-12 strains (`lambda b2` deletion mutants plaque normally).

## Bioinformatics and Domain Architecture
1. **C-terminal HNH Endonuclease Domain**: Sequence analysis in UniProt and InterPro shows that Ea31 contains a conserved C-terminal HNH endonuclease domain (`CDD:cd00085` HNHc, `SMART:SM00507`, `InterPro:IPR003615` HNH_nuc, `PROSITE:PS50159` HNHC, spanning residues 197–244) [file:LAMBD/ea31/ea31-uniprot.txt].
2. **Genomic Context (`ea47`-`ea31`-`ea59`)**: In phage lambda, `ea31` sits immediately adjacent to `ea59` (which encodes an AAA+ ATPase / OLD-like antiviral defense-associated protein) and `ea47`. The presence of a canonical HNH nuclease motif (`IPR003615`) strongly suggests that Ea31 possesses endonuclease activity (`GO:0004519`), potentially acting as a homing-like endonuclease, a DNA nicking/cleavage factor, or a nuclease effector paired with neighboring *b2* proteins during inter-phage competition or host defense modulation. However, no direct biochemical or genetic characterization of Ea31's nuclease activity in phage lambda has been published.

## GO Annotation Review Summary
- `existing_annotations`: None (`[]`) in GOA.
- `core_functions`: Left empty (`[]`) as Ea31 has no experimentally validated function in GOA, though its C-terminal HNHc domain (`InterPro:IPR003615`, residues 197–244) predicts endonuclease activity.
