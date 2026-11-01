# aimR (Bacillus phage phi3T) — Curation Notes

## Overview
- **Gene symbol**: `aimR`
- **UniProt ID**: `P0DOE3` (`AIMR_BPPHT`)
- **Organism**: *Bacillus* phage phi3T (`NCBITaxon:10736`)
- **Product**: Transcriptional regulator AimR (378 aa; PDB `5ZVV`, `5ZVW`)

## Biological Function and Mechanism
- **Intracellular receptor of the arbitrium system**: `AimR` is a 378-amino-acid phage-encoded transcriptional activator and intracellular peptide receptor containing an N-terminal helix-turn-helix (HTH) DNA-binding domain and a C-terminal tetratricopeptide repeat (TPR)-like peptide-binding domain (`InterPro:IPR011990`) [PMID:28099413; file:BPPHT/aimR/aimR-uniprot.txt].
- **Activation of `aimX` in the apo state**: In early infections when extracellular concentration of the `AimP`-derived hexapeptide `SAIRGA` is low, apo-`AimR` forms a homodimer that binds a single operator site in the phage phi3T genome directly downstream of `aimP` [PMID:28099413]. DNA-bound dimeric `AimR` activates transcription of the non-coding RNA regulator `aimX`, which inhibits lysogeny and promotes the lytic replication cycle [PMID:28099413].
- **Peptide-induced dimer dissociation**: When imported `SAIRGA` binds the TPR-like pocket of `AimR` (`EC50 = 138 nM`), it induces a conformational change that dissociates the `AimR` homodimer into peptide-bound monomers incapable of binding DNA (`aimX` expression is abolished), thereby shifting the phage into lysogeny [PMID:28099413].
- **Specificity**: `AimR` from phage phi3T responds specifically to its cognate `SAIRGA` peptide and not to the related phage SPbeta peptide `GMPRGA` [PMID:28099413].

## Curation Decisions
- **Existing annotations**:
  - `GO:0098689` (`latency-replication decision`, IDA from PMID:28099413 and IEA): `ACCEPT`. `AimR` directly controls the lysis-lysogeny decision in phage phi3T in response to the arbitrium peptide.
