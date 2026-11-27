# JUNB notes

- **Deep research.** Perplexity deep research was unavailable in this worktree during the JUN-family
  review. Continue the review from UniProt, GOA, the PTHR11462 PAINT table, Reactome caches, and cached
  primary literature.
- **Core AP-1 function.** PTHR11462 PAINT places the conserved AP-1 DNA-binding and transcriptional
  activation calls at the eukaryotic PTN000894784 node. The JunB UniProt record describes a nuclear
  Jun-family transcription factor that binds `5'-TGA[GC]TCA-3'` and heterodimerizes with FOS proteins in
  AP-1 complexes, so broad DNA-binding, transcription-regulator-complex, and transcription-regulation
  rows were refined to the specific AP-1/Pol II terms.
- **Protein-binding policy.** Most JunB `GO:0005515` rows name bZIP AP-1 partners from curated or
  large-scale interaction datasets. FOS, FOSB, FOSL, ATF, BATF, DDIT3 and JDP2 partners were refined to
  `GO:0061629` RNA polymerase II-specific DNA-binding transcription factor binding; HBZ/MDV005 viral
  interactions and non-transcription-factor screen partners were removed as uninformative bare protein
  binding.
- **Contextual outputs.** The metazoan PAINT rows for proliferation, steroid response and cell-cycle
  regulation were retained as non-core outputs. The JunB-specific Th17 row is also retained as a
  cell-type-specific regulatory output rather than promoted to the conserved AP-1 core
  [PMID:29234109, "The AP-1 transcription factor JunB is required for Th17 cell differentiation"].
