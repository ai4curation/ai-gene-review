# YciO vs TsaC (YrdC) comparative analysis

## Goal
Test, independently of any single publication, whether *E. coli* YciO (P0AFR4) is a
bona fide L-threonylcarbamoyl-AMP (TC-AMP) synthase like its paralog TsaC/YrdC
(P45748), the dedicated enzyme of the t6A tRNA-modification pathway. This bears
directly on the DeepECTF EC:2.7.7.87 prediction for YciO.

## Method (reproducible)
```bash
# Sequences: YciO from genes/ECOLI/yciO/yciO-uniprot.txt; TsaC fetched from UniProt
curl -s https://rest.uniprot.org/uniprotkb/P45748.fasta -o tsaC.fasta
cat yciO.fasta tsaC.fasta > yciO_vs_tsaC.fasta
mafft --auto yciO_vs_tsaC.fasta > yciO_vs_tsaC.aln
```
Inputs/outputs are in this folder (`yciO_vs_tsaC.fasta`, `yciO_vs_tsaC.aln`).

## Results
- **Homology, but deep divergence.** YciO (206 aa) and TsaC/YrdC (190 aa) align over a
  single YrdC/Sua5 (PF01300) domain at **~29% identity** (48/164 aligned columns).
  This is the expected signal for ancient paralogs that share the fold but are not
  necessarily isofunctional.
- **Degenerate active-site motif.** At the conserved Sua5/TsaC catalytic motif TsaC
  reads `...PLV-STSANL-SGL...`; the structurally/mechanistically important Asn (the
  "S-x-N" catalytic signature) and the following Ser-Gly are present. In YciO the
  homologous segment reads `...PML-STSLML-PGS...` — the **conserved catalytic Asn is
  replaced by Met** (SAN → SLM) and the SG is lost. YciO therefore lacks part of the
  canonical TC-AMP-synthase catalytic apparatus.

## Interpretation
YciO is a degenerate paralog of TsaC. The fold is conserved (consistent with the YciO
crystal structures 1K7J/1KK9) but the catalytic motif is not. This is consistent with:
1. TsaC/YrdC, not YciO, being the dedicated, essential TC-AMP synthase in *E. coli*
   (t6A is essential; *tsaC*/*yrdC* is essential despite the presence of YciO,
   i.e. YciO does not provide redundant TC-AMP-synthase function in vivo); and
2. the weak in-vitro activity reported for purified YciO (0.0705 U/mg in Kim et al.
   2023) reflecting residual/promiscuous family chemistry of a degenerate paralog
   (note UniProt also records YciO "ATP hydrolysis activity in vitro, producing AMP")
   rather than the protein's dedicated biological function.

The DeepECTF EC:2.7.7.87 prediction for YciO is thus best read as a **paralog
over-annotation**: the dedicated TC-AMP-synthase function belongs to the TsaC
subfamily, and YciO's true in-vivo role remains unresolved.
