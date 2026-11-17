# alp13 curation notes

## 2026-11-06

- Fetched `SCHPO/alp13` from GOA/UniProt. The seed contains 24 rows covering the
  fission-yeast Clr6S/Rpd3S complex, the NuA4 histone acetyltransferase
  complex, three broad MRG-domain IEAs, two generic `protein binding` rows for
  Pst2, and three PANTHER/PAINT rows from PTHR10880.
- Deep research was not available for this gene, so the review was based on the
  cached GOA publications plus a manual literature pass. Searches for newer
  `alp13`, `eaf3`, `Clr6S`, and `Rpd3S` papers found two direct 2023 S. pombe
  structural papers already present in the fetched GOA set: PMID:37076472 and
  PMID:37459529. No newer post-2023 Alp13-specific paper changed the core
  curation.
- `PTN000853816` is the clean fungal PAINT node for `GO:0032221 Rpd3S complex`;
  it is seeded by PomBase alp13 and SGD EAF3, which is appropriate target
  self-seeding rather than circularity.
- `PTN000093963` carries three IBD assertions at the broad MRG-family root. The
  `GO:0035267 NuA4 histone acetyltransferase complex` and `GO:0006357
  regulation of transcription by RNA polymerase II` rows are defensible for
  fission yeast. The `GO:1990841 promoter-specific chromatin binding` row is
  seeded only by Arabidopsis MRG1/MRG2 and over-propagates a plant-specific
  promoter-binding assertion to fungal Eaf3/Alp13 proteins that are supported
  as H3K36me-linked Rpd3S/NuA4 subunits.
- Removed the two `GO:0005515 protein binding` rows because Pst2 interactions
  are uninformative as standalone molecular-function annotations and are better
  represented by Rpd3S complex membership. This is not a claim that the curated
  IntAct/PomBase interactions are false.
