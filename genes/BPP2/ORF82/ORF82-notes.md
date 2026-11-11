# ORF82 (`Q06424` / `YO82_BPP2` / `orf-82` / `ORF3`) Notes

## Overview
- **Gene / ORF**: `ORF82` (`orf-82`, `ORF3`, Uncharacterized 8.2 kDa protein in gpA 5' region)
- **UniProt ID**: `Q06424` (`YO82_BPP2`, 74 aa, 8.2 kDa)
- **Organism**: Helper Myovirus Escherichia phage P2 (`NCBITaxon:2905681`)
- **Genomic Context**: Encoded in the early right-arm operon upstream (5' region) of the cis-acting replication endonuclease gene `A`, between `orf-81` and `orf-83` [PMID:8510152].

## Literature & Functional Findings
1. **Identification and Host-Lethal Overexpression Phenotype**:
   - Sequencing of the right end of the P2 genome identified five open reading frames (`orf-80`, `orf-81`, `orf-82`, `orf-83`, and `orf-91`) whose products were cloned and identified [PMID:8510152].
   - Overexpression of the `orf-82` gene product (along with `orf-80` and `gpA`) was found to be lethal to the *Escherichia coli* host cell [PMID:8510152].
   - The predicted amino acid sequence of the `orf-82` product shares similarity with an early gene product of the related P2-like coliphage 186 [PMID:8510152].
2. **Conserved DksA/TraR C4-Type Zinc-Finger Domain**:
   - Sequence and domain analysis (`file:BPP2/ORF82/ORF82-uniprot.txt`) reveals a conserved DksA/TraR C4-type zinc-finger domain (`PF01258` / `IPR000962`) spanning residues 35-59 (`PROSITE:PS51194`), supporting zinc ion binding (`GO:0008270`).
   - DksA/TraR-family zinc-finger proteins in bacteriophages and conjugative plasmids bind the secondary channel of bacterial RNA polymerase to modulate host transcription without binding DNA directly, suggesting that ORF82 may act as an early host-takeover or transcriptional modulator that causes host lethality when overproduced.

## Curation Decisions
- **Existing GO Annotations**:
  - `GO:0008270` (`zinc ion binding`, `IEA`, `GO_REF:0000120` from `InterPro:IPR000962` / `UniProtKB-KW:KW-0863`): **ACCEPT**. Directly supported by the conserved C4-type DksA/TraR zinc-finger domain (`IPR000962` / `PF01258`) at residues 35-59.
  - `GO:0046872` (`metal ion binding`, `IEA`, `GO_REF:0000043` from `UniProtKB-KW:KW-0479`): **MODIFY** to `GO:0008270` (`zinc ion binding`), which is more specific and already present in GOA.
- **Core Functions**:
  - `GO:0008270` (`zinc ion binding`): Binds a structural zinc ion via its conserved C4-type DksA/TraR zinc-finger motif (`IPR000962`).
