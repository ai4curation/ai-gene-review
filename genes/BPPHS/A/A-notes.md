# Gene Review Notes: Enterobacteria phage phiX174 gene A (P03631)

## Overview
- **Gene symbol**: `A`
- **UniProt ID**: `P03631` (`REPA_BPPHS`)
- **Organism**: Enterobacteria phage phiX174 isolate Sanger (`NCBITaxon:1217068`)
- **Product**: Replication-associated protein A (gpA, 513 aa, 58.7 kDa) and in-frame alternative translation initiation product protein A* (gpA*, residues 173-513, 341 aa)
- **Phage lifecycle module**: `phage_dna_replication.yaml` (Rolling-circle single-stranded viral DNA replication) and `phage_packaging_headful_cos.yaml` (Coupled rolling-circle packaging at the procapsid)

## Biological Function & Mechanism
1. **Stage II and Stage III Rolling-Circle DNA Replication (gpA)**:
   - Protein A (gpA) is the HUH/Y2-family rolling-circle replication initiator endonuclease of bacteriophage phiX174 (`file:BPPHS/A/A-uniprot.txt`, `PMID:2972712`).
   - It recognizes and binds the 30-bp viral origin of replication on supercoiled double-stranded replicative form I (RFI) DNA and introduces a site-specific nick in the viral (+) strand (`PMID:2972712`, `file:BPPHS/A/A-uniprot.txt`).
   - Cleavage proceeds via transesterification that forms a covalent `O-(5'-phospho-DNA)-tyrosine` bond with one of two active-site tyrosines (`Tyr-343` and `Tyr-347`), generating open circular RFII DNA with a free 3'-OH terminus (`file:BPPHS/A/A-uniprot.txt`).
   - Host Rep helicase and DNA polymerase III holoenzyme extend the 3'-OH terminus to synthesize a new viral (+) strand while displacing the parental (+) strand (`PMID:2972712`, `file:BPPHS/A/A-uniprot.txt`).
   - After a complete round of rolling-circle synthesis, the second catalytic tyrosine cleaves the regenerated origin and joins the 5' and 3' ends of the displaced strand via a second transesterification reaction to release a closed circular single-stranded viral genome (`file:BPPHS/A/A-uniprot.txt`).
2. **Isoform A* (gpA*, P03631-2)**:
   - Synthesized from an internal in-frame start codon at residue 173 (`VSP_018674`), protein A* retains the C-terminal catalytic domain (`Tyr-343`/`Tyr-347`) and binds double-stranded DNA, protecting it from nuclease hydrolysis and inhibiting host/viral semiconservative DNA replication during the transition to late single-stranded DNA synthesis (`file:BPPHS/A/A-uniprot.txt`).

## GO Annotation Review Summary
- **Accepted core terms**:
  - `GO:0039684` (`rolling circle single-stranded viral DNA replication`, IDA from `PMID:2972712`)
  - `GO:0004519` (`endonuclease activity`, IEA)
  - `GO:0003677` (`DNA binding`, IEA)
- **Removed erroneous EC 6.5.1.1 mappings**:
  - `GO:0003910` (`DNA ligase (ATP) activity`), `GO:0005524` (`ATP binding`), and `GO:0000166` (`nucleotide binding`): UniProt cross-references `EC:6.5.1.1` (ATP-dependent DNA ligase) because gpA circularizes the displaced ssDNA strand. However, biochemically gpA is an energy-conserving HUH/Y2 relaxase/endonuclease that ligates DNA via a covalent 5'-phosphotyrosine intermediate (`Tyr-343`/`Tyr-347`) without ATP binding or hydrolysis.
- **Broad ancestor terms marked `TOO_GENERAL`**:
  - `GO:0004518` (`nuclease activity`), `GO:0016787` (`hydrolase activity`), `GO:0006260` (`DNA replication`), `GO:0039693` (`viral DNA genome replication`), `GO:0046872` (`metal ion binding`).
- **Non-core terms (`KEEP_AS_NON_CORE`)**:
  - `GO:0008270` (`zinc ion binding`, predicted zinc-finger region 246-268) and `GO:0016874` (`ligase activity`, general strand-joining activity during termination of rolling-circle replication).
