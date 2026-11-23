# SMIM10 (Q96HG1) review notes

## 2026-10-03 Tier 2 microprotein review

### Identity
- UniProt Q96HG1 SIM10_HUMAN, 83 aa, PE1; alias CXorf69 (X chromosome). Single predicted helical
  TM segment at the extreme C terminus (64-82), so the predicted topology is tail-anchored-like with
  a soluble N-terminal 63 residues (Gly/Ala/Arg-rich first ~35 residues). Membrane / single-pass is
  sequence-based (ECO:0000255).
- Family: Pfam PF15118 DUF4560, InterPro IPR029367 SMIM10, PANTHER PTHR34446. Human paralogs
  SMIM10L1, SMIM10L2A, SMIM10L2B. One SMIM10L1 paper (PMID:35290761, adipose progenitor
  differentiation) and one SMIM10L2B mention (PMID:37235655, microglial macrosome proteome, said to
  inhibit Abeta aggregation) exist; neither concerns SMIM10 itself and function is not transferred.
- Expression: HPA "Tissue enhanced (blood)" (UniProt DR line); HPA JSON (fetched 2026-10-03) lists
  blood vessel nTPM 48.5. No HPA subcellular location.

### Literature search
- PubMed `SMIM10[tiab] OR CXorf69[tiab]` -> 2 hits; `"small integral membrane protein 10"` -> 3
  (two about paralogs, one irrelevant).
- PMID:30237439 (Oncogene 2019; abstract only cached). A yeast functional screen for human cDNAs that
  rescue BRAF-V600E toxicity recovered SMIM10. [PMID:30237439 "we identify
  SMIM10, a mitochondrial protein that in melanoma cells selectively downregulates
  BRAFV600E RNA and protein levels, by acting indirectly at the
  post-transcriptional level."] Overexpression caused [PMID:30237439 "disrupted mitochondrial
  structure/function and undergo senescence"]. The effect is indirect and overexpression-based.
  Mitochondrial localization is stated but the method is not visible in the abstract. Not used for a NEW CC
  annotation: abstract-only, overexpression, and SMIM10 has no independent mitochondrial proteomics
  support in GOA. Recorded as a suggested question instead.
- PMID:37965330 (keratoconus single-cell; SMIM10 as a prognostic/immune-associated gene) - list
  mention only, not cached.

### GOA rows
- membrane (IEA) -> ACCEPT.

### Conclusion
No established function. Overexpression phenotype in BRAF-mutant melanoma cells is indirect and
does not support an MF or BP term. No NEW.
