# Enterobacteria Phage P4 Gene Delta (Transcriptional Transactivator gpDelta) — Curation Notes

## Overview
Enterobacteria satellite phage P4 gene *delta* (`P12551`, 166 aa, ~19.1 kDa) is located in the late `sid-delta-psu` operon and encodes the transcriptional transactivator protein gpDelta [PMID:6095206, PMID:3295254, PMID:2193910, PMID:2183201].

## Structural and Biochemical Functions
- **Tandem Ogr/Delta Zinc-Finger Domain Architecture**: gpDelta consists of two tandem repeats of the phage P2 Ogr-like Cys4 zinc-finger domain (`InterPro:IPR007684` `Znf_Ogr/Delta` / `Pfam:PF04606`), making it look like a covalent homodimer of P2 Ogr.
- **Activation of Helper P2 and Satellite P4 Late Transcription via Host RNA Polymerase α-Subunit**: Halling et al. (1990) demonstrated that `org` suppressor mutations in P4 `delta` restore late gene activation in *Escherichia coli* carrying the `rpoA109` mutation in the RNA polymerase α-subunit (`rpoA`), proving that gpDelta positively regulates transcription of both helper phage P2 morphogenetic/lysis genes and P4 late genes (`GO:0050434`, `positive regulation of viral transcription`) by binding upstream promoter DNA (`GO:0003677`, `DNA binding`) and contacting the C-terminal domain of host RNA polymerase α [PMID:2193910, PMID:3295254].

## GO Annotation Review
- **Accept**: `GO:0003677` (`DNA binding`, `IEA` `GO_REF:0000043`).
- **New**: `GO:0050434` (`positive regulation of viral transcription`, `IMP`, `PMID:2193910`).
