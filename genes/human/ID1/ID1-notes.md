# ID1 notes

Automated deep research was attempted for this review with `just deep-research-falcon human ID1 --fallback perplexity-lite`,
but the local Falcon provider was unavailable and the Perplexity fallback was not configured. These notes therefore summarize
the cached primary literature, Reactome summaries, UniProt record, and PANTHER PAINT data used for the manual review.

## Evidence reviewed

- **Conserved ID-family mechanism.** ID1, ID2, ID3 and ID4 are helix-loop-helix transcription-regulator inhibitors:
  they retain the HLH dimerization region but lack the basic DNA-binding region, so they heterodimerize with
  bHLH transcription factors and prevent those partners from binding E-box DNA. The family is `PTHR11723`;
  all four reviewed human ID proteins sit under PAINT node `PTN000919548`, which propagates nucleus,
  transcription corepressor activity, negative regulation of transcription by RNA polymerase II, and neuron
  differentiation, with no IRD or IKR loss on the human ID1 lineage.
- **Direct human ID1 mechanism.** Zheng et al. showed endogenous ID1:E47 interaction in human diploid fibroblasts,
  E47 binding at the p16(INK4a) promoter, and increased p16(INK4a) after ID1 knockdown, supporting the core
  transcription-regulator inhibitor activity through E-protein sequestration [PMID:15138269].
- **CLOCK/BMAL1 binding.** Ward et al. found that ID2 binds CLOCK and BMAL1 directly and reported mammalian
  two-hybrid evidence for ID1 and ID3 binding to both CLOCK and BMAL1 [PMID:20861012].
- **TGF-beta/angiogenesis TAS rows.** The abstract cached for PMID:14522471 is a TGF-beta signaling review and
  does not mention ID1; any ID1-specific author statement was not visible, so the old BHF-UCL TAS rows from that
  review are left undecided unless supported by other rows.
- **2026-11-27 follow-up on ID1 angiogenesis.** The BHF-UCL PMID:14522471 batch is deliberate and aligns with
  primary ID1 vascular literature: Goumans et al. place Id1 downstream of endothelial TGF-beta/ALK1-Smad signaling,
  while Volpert et al. show reduced Id1-null neovascularization and endothelial-migration inhibition through
  thrombospondin-1 derepression. I resolved the TAS rows as supported non-core angiogenesis/TGF-beta outputs rather
  than source defects.
