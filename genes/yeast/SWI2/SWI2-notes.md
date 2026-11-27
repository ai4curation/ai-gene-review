# SWI2 curation notes

## 2026-09-29 - IBA source alignment

- Rechecked the seven SNF2/SWI2 IBA rows against the current `PTHR10799` PAINT
  snapshot. `PTN001649185` carries the current chromatin and nucleus rows, and
  `PTN004198564` carries DNA binding, chromatin binding, nucleosome array spacer
  activity, heterochromatin formation, and positive regulation of Pol II transcription.
- Kept chromatin, nucleus, and Pol II activation as valid for the core nuclear
  chromatin-remodeling activity, kept broad DNA binding as valid but non-core, and added
  `propagation_review` blocks pointing at the current PAINT nodes.
- Removed `GO:0140750` nucleosome array spacer activity because the source activity
  belongs to ISWI/CHD-like nucleosome-spacing remodelers rather than to the SWI/SNF Snf2
  motor branch.
- Removed `GO:0031507` heterochromatin formation because the cited S. cerevisiae SWI/SNF
  evidence shows Snf2 overcoming Sir-mediated heterochromatin repression during
  recombinational repair, not creating heterochromatin.
- Converted most legacy `GO:0005515` protein binding IPI rows to `REMOVE`. The generic
  interactome edges are better represented by SWI/SNF complex membership, transcription-factor
  binding, histone binding, and chromatin binding; the two cryo-EM Snf2/SWI-SNF nucleosome
  rows were instead changed to `MODIFY` with GO:0031491 `nucleosome binding`.
- Searched 2025+ PubMed for `SWI2`, `SNF2`, `YOR290C`, and `SWI/SNF` with
  `Saccharomyces cerevisiae`. The hits included new SWI/SNF target-gene studies in
  2025-2026 and several papers on other SNF2-family remodelers such as Fun30, Rad5, and
  Mot1, but none changed the core Snf2/Swi2 PAINT calls above.
