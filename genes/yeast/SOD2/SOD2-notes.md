# SOD2 notes

## 2026-09-29 IBA propagation rereview

- `GO:0005739 mitochondrion` IBA traces through `PANTHER:PTN000150076`. The current
  `interpro/panther/PTHR11404/PTHR11404-paint.tsv` has a matching mitochondrial IBD
  at that node for eukaryotic MnSOD proteins, including SGD:S000001050 as a descendant
  evidence.
- `GO:0004784 superoxide dismutase activity` and `GO:0030145 manganese ion binding`
  both trace through `PANTHER:PTN004256454` in the current PTHR11404 PAINT file.
  Direct yeast evidence from PMID:238997, PMID:15851472, and the native/Fe-substituted
  yeast SOD2 structures in PMID:22102021 supports the catalytic and Mn-binding calls.
- No IBA propagation failure was found. S. cerevisiae SOD2 is assigned to
  `PTHR11404:SF6`, the mitochondrial MnSOD subfamily, and the three propagated terms
  match its experimentally established matrix superoxide dismutase activity.
- Searched 2024-2026 PubMed and web results for SOD2/Sod2p/MnSOD papers in
  Saccharomyces and yeast. Newer SOD2 hits mostly measure oxidative-stress phenotypes
  or use `SOD2` as a panel readout; none changed the core GO decisions.
- Cached PMID:37638880, a 2023 full-text Genetics paper showing that Sod2 suppresses
  paraquat-induced nuclear chromosomal rearrangements. That result is a downstream
  consequence of mitochondrial superoxide detoxification and does not make SOD2 itself
  a DNA-repair or nuclear genome-maintenance factor.
