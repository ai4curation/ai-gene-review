# FUCA2 Notes

## 2026-11-21

- Seeded the review with `just fetch-gene human FUCA2`; Q9BTY2 has 35 incoming
  GOA rows.
- `just deep-research-falcon human FUCA2 --fallback perplexity-lite` could not
  run because neither requested provider was registered in this workspace. I did
  not create a synthetic provider deep-research file; the evidence synthesis is
  recorded here instead.
- FUCA2 is the only missing human member in the local `PTHR10030`
  alpha-L-fucosidase family. Human FUCA1 is already reviewed in `PTHR10030:SF2`,
  and FUCA2 sits in `PTHR10030:SF45`.
- PANTHER places `GO:0004560`, `GO:0006004`, and `GO:0016139` at the family root
  `PTN000003123`; FUCA2 is itself a seed for all three positive rows, and
  `just paint-losses human FUCA2` found no IRD/IKR on the Q9BTY2 lineage.
- The only local PAINT loss in this family is a Drosophila IRD at
  `PTN000003216`. The existing `projects/IRD_EVIDENCE` audit flags it as a
  one-protein clade with a conflicting FlyBase IDA row, so the family review
  treats the loss as contradicted and irrelevant to human FUCA1/FUCA2.
- [PMID:19666478] is full text in the publication cache. It directly identified
  secreted human FUCA2 from H. pylori/gastric-cell coculture medium by
  fucosidase-inhibitor affinity chromatography and LC-MS/MS, explicitly
  prepared and characterized human FUCA2, and showed by FUCA2 knockdown or
  fucosidase inhibition that the enzyme promotes H. pylori adhesion and Lewis x
  production in bacteria.
- The H. pylori phenotypes are real but narrow: they justify a non-core
  `response to bacterium` row, while `regulation of entry of bacterium into host
  cell` overstates a system measuring extracellular H. pylori adhesion and CagA
  translocation.
- The official BioStudies workbook for [PMID:23533145] lists Q9BTY2/FUCA2 in SI
  Table 2, row 694. The row has one or two unique peptides in each of the four
  duplicate analyses of two pooled clinical groups, supporting EPS-urine exosome
  preparation detection but not vesicle topology or exosome biogenesis.
- Existing `modules/lysosomal_glycoprotein_degradation.yaml` intentionally
  selects `PTHR10030:SF2` and human FUCA1 for core lysosomal glycoprotein
  degradation. Existing `modules/mammalian_l_fucose_degradation.yaml` explicitly
  leaves FUCA1/FUCA2-mediated fucose release upstream of the cytosolic
  degradation pathway, so no FUCA2 module edit was needed.
- No FUCA2 entry appears in `gocams/index.tsv`; no production GO-CAM review was
  needed for this family PR.
