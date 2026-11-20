# rpoN (PP_0952, P0A171) review notes

- Sources: existing Falcon deep research (`rpoN-deep-research-falcon.md`), UniProt P0A171, cached literature.
- Role in the CbrA/CbrB-Crc/Hfq catabolite control module: sigma-54 is the promoter-specificity subunit at the
  crcZ/crcY promoters activated by CbrB [PMID:27777366 "The crcZ and crcY genes are transcribed from promoters PcrcZ and PcrcY, respectively, a process that relies on the CbrB transcriptional activator and the RpoN σ factor."];
  in P. aeruginosa [PMID:20080802 "The sigma factor RpoN and the CbrA/CbrB two-component system, which is known to maintain a healthy carbon-nitrogen balance, were necessary for crcZ expression."]
- 2026-10-23 completion pass: generic DNA binding changed from MARK_AS_OVER_ANNOTATED to MODIFY ->
  GO:0000976 (correct-but-general rule); GO_REF:0000108 title corrected; crcZ/crcY evidence added to the core
  function; status set to COMPLETE.
- DNA-binding transcription activator activity remains MARK_AS_OVER_ANNOTATED on both rows: activation of
  sigma-54 promoters is performed by bEBPs such as CbrB and NtrC, not by sigma-54 itself.
- 2026-11-02 (Ntr module PR): the clause naming CbrB-activated crcZ/crcY promoters was moved out of the
  core-function description, since sigma-54 serves many enhancer-binding-protein outputs; the crcZ/crcY
  quotes stay in that core function's supported_by as examples of RpoN-dependent promoters, and the Cbr/Crc
  output itself is modelled in MODULE:pseudomonad_cbr_crc_catabolite_control.
