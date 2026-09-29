# SWI1 curation notes

## 2026-09-29 - IBA source alignment

- Rechecked the four SWI1 IBA rows against the current `PTHR13964` PAINT snapshot.
  `PTN000359478` still carries `GO:0006357` regulation of transcription by RNA polymerase
  II and `GO:0005634` nucleus, and the transfers remain valid for S. cerevisiae Swi1.
- Preserved the existing `REMOVE` decision for `GO:0000976` transcription cis-regulatory
  region binding. The PAINT row is seeded by human ARID1A/ARID1B evidence at the root
  ARID/SWI1-family node, whereas yeast Swi1's ARID is weak and nonspecific and Swi1 is
  better captured as a SWI/SNF scaffold that contributes to nucleosome engagement.
- `PTN002303792` still carries `GO:0016514` SWI/SNF complex on the fungal Swi1 node with
  Candida, S. pombe, and S. cerevisiae descendant evidence, so the complex-membership IBA
  was kept as core.
- Converted the legacy `GO:0005515` protein binding IPI rows to `REMOVE`. These
  interactions are biologically real but are represented more informatively as SWI/SNF
  complex membership, RNA polymerase II-specific DNA-binding transcription factor binding,
  and nucleosome binding.
- Searched 2025+ PubMed for `SWI1`, `YPL016W`, `ADR6`, and `GAM3` with
  `Saccharomyces cerevisiae`. The only exact hits were PMID:40004101, a yeast-prion paper
  touching Swi1's N-terminal prion-forming region, and PMID:40768430, a Colletotrichum
  CgSwi1 virulence paper; neither changes the propagated SWI/SNF annotation calls.
