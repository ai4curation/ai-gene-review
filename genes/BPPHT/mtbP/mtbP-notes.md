# mtbP (Bacillus phage phi3T) — Curation Notes

## Overview
- **Gene symbol**: `mtbP`
- **UniProt ID**: `P68586` (`MTBP_BPPHT`)
- **Organism**: *Bacillus* phage phi3T (`NCBITaxon:10736`)
- **Product**: Modification methylase Phi3TI (`M.Phi3TI`; 443 aa, ~50.5 kDa; EC `2.1.1.37`)

## Biological Function and Mechanism
- **Multispecific C5-cytosine DNA methyltransferase**: `mtbP` encodes the orphan multispecific DNA (cytosine-5-)-methyltransferase `M.Phi3TI`, which is identical in amino acid sequence (443 aa, `Mr` 50,507) to the *Bacillus subtilis* phage SPbeta methyltransferase `M.SPbetaI` (`mtbS`) except for its upstream promoter region [PMID:3087819; PMID:2989588].
- **Sequence specificity and TRD organization**: `M.Phi3TI` catalyzes the S-adenosyl-L-methionine-dependent methylation of the C5 atom of the first (internal) cytosine (`C-1`) within both `5'-GGCC-3'` and `5'-GCNGC-3'` recognition sequences [PMID:3142766; file:BPPHT/mtbP/mtbP-uniprot.txt]. Chimeric domain-swapping and point-mutation analyses demonstrated that recognition of `5'-GCNGC-3'` and `5'-GGCC-3'` is mediated by two distinct, contiguous ~50-amino-acid target-recognizing domains (TRDs) arranged in tandem without overlap inside the variable region between conserved C5-Mtase motifs VIII and IX [PMID:3142766].
- **Evasion of host restriction**: By methylating phage DNA at `5'-GGCC-3'` (the `BsuRI` recognition site) and `5'-GCNGC-3'` (the `Fnu4HI` recognition site), `M.Phi3TI` protects phage phi3T DNA against cleavage by host *Bacillus subtilis* restriction endonucleases [PMID:2989588; PMID:3087819; file:BPPHT/mtbP/mtbP-uniprot.txt].

## Curation Decisions
- **Existing annotations**:
  - `GO:0003886` (`DNA (cytosine-5-)-methyltransferase activity`, IEA): `ACCEPT`. Core catalytic activity (`EC:2.1.1.37`).
  - `GO:0003677` (`DNA binding`, IEA): `ACCEPT`. `M.Phi3TI` contains two tandem sequence-specific DNA target-recognizing domains (TRDs) that bind `5'-GGCC-3'` and `5'-GCNGC-3'` DNA duplexes.
  - `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`, IEA): `ACCEPT`. Core biological role of this phage orphan methyltransferase.
  - `GO:0008168` (`methyltransferase activity`, IEA) and `GO:0016740` (`transferase activity`, IEA): `TOO_GENERAL` (entailed by `GO:0003886`).
  - `GO:0052031` (`symbiont-mediated perturbation of host defense response`, IEA) and `GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA): `TOO_GENERAL` (entailed by `GO:0099018`).
