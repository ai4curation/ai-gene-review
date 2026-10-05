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

## 2026-10-01 - current GOA refresh

- Force-refreshed `SWI2` against current UniProt and GOA. The live GOA snapshot has
  76 rows; all are now represented in the YAML. Nine older exact source assertions
  are no longer live and were preserved with `retired: true`: broad ATP/nucleotide/
  hydrolase or transcription parent IEA rows, four vanished legacy `GO:0005515`
  protein-binding IPI rows, and one vanished ARBA Pol II activation row.
- Resolved nine newly seeded live rows. Kept the InterPro `GO:0005524` ATP-binding
  row as true but non-core, accepted the new ComplexPortal SWI/SNF-complex row,
  accepted the human-SMARCA ISS for `GO:0016887` ATP hydrolysis, accepted paired
  IGI rows for chromatin remodeling and Pol II transcriptional activation, accepted
  the second transcription-activator-binding row, accepted ARBA `GO:0140015`
  H3K14ac reader activity because direct Zhang 2010 evidence already supports it,
  and removed two new IntAct `GO:0005515` rows as generic Snf2/Snf11 protein-binding
  assertions better captured by SWI/SNF complex membership.
- Rechecked current `PTHR10799` PAINT after the refresh. The same seven IBA rows
  still reach yeast Snf2 from `PTN001649185` or `PTN004198564`; their existing
  `source_entities` remain aligned to PTN nodes. The cached family now also carries
  a `GO:0000729` double-strand-break-processing IBD on `PTN000743674`, but that
  assertion does not propagate to the current SWI2 GOA snapshot.
- Searched for newer `Saccharomyces` Snf2/SWI/SNF literature. The 2026 Scientific
  Reports paper with DOI `10.1038/s41598-026-63900-6` reports a meiotic role for
  Snf2 in transcriptional reprogramming and DSB formation; it did not have a cached
  PMID in this review and does not change the existing core chromatin-remodeler,
  Pol-II transcription, or DSB-repair calls.

## 2026-10-05 PR 3714 follow-up

- Changed the PMID:32188938 `GO:0005515 protein binding` row from `MODIFY` to
  `REMOVE`. Its `WITH/FROM` partner is Swi3, so the row records redundant
  intracomplex Snf2-Swi3 binding rather than the Snf2-nucleosome contact that
  remains represented by the separate PMID:28424519 protein-binding row.
