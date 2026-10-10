# SCHPO/mst2 notes

## 2026-10-10

- Seeded `SCHPO/mst2` with `just fetch-gene SCHPO mst2 --force` and cached
  the five GOA PMIDs that the seed references. The default Falcon deep-research
  run failed because no provider credentials or agent API were available in this
  environment, so this file records the manual review.
- Read the cached Mst2 papers behind the seeded rows. `PMID:21289066`
  establishes Mst2 as the catalytic MYST-family subunit of the fission-yeast
  H3K14 acetyltransferase complex and shows loss of Mst2 bypasses the RNAi
  pathway for pericentric heterochromatin maintenance rather than establishment.
  `PMID:25774602` and `PMID:39094565` place Mst2 with Epe1 as redundant
  antagonists of H3K9me heterochromatin spreading and adaptive
  heterochromatin-state changes. `PMID:39096900` supports the direct negative
  regulation row by targeting an Mst2 HAT fusion to H3K9me-coated domains,
  increasing H3K14ac and destabilizing heterochromatin through SWI/SNF
  remodelers.
- Searched PubMed and broader web results for newer `mst2` papers. The main
  new paper found was `PMID:41786738`, a 2026 Nature Communications article
  that places Mst2-mediated H3K14 acetylation opposite Clr3-mediated
  deacetylation in an H3K14ub/H3K9me3 feedback circuit that governs
  heterochromatin spreading and inheritance.
- Checked the local `PTHR10615` PAINT cache. Broad chromatin, nucleus,
  chromatin-binding, transcription-coregulator, and histone-acetyltransferase
  IBA rows all come from the deep eukaryotic MYST-family node
  `PANTHER:PTN004172926` and fit Mst2. The `GO:1990467` NuA3a row comes from
  fungal `PANTHER:PTN008308138`; that node is seeded by budding-yeast `SAS3`
  and is appropriate for Sas3 itself, but the term names a budding-yeast NuA3a
  complex rather than the PomBase Mst2 histone acetyltransferase complex.
- Retained the ORFeome cytosol and UniProt cytoplasm localizations as non-core:
  they are compatible with UniProt's dual cytoplasm/nucleus statement but do not
  describe the core H3K14 acetyltransferase activity on nuclear chromatin.
- Followed up on PR review by fetching full text for the two UniProt FUNCTION
  papers that were missing from the first pass. `PMID:16199868` established
  nuclear chromatin localization and Mst2's negative regulation of telomeric
  silencing. `PMID:22184112` biochemically defined the Mst2 complex as a
  nucleosomal H3K14 acetyltransferase and showed that Mst2 and Gcn5-dependent
  H3K14ac supports activation of the DNA damage checkpoint. The
  GO-Central-facing `GO:1990467` to `GO:0036410` complex replacement remains a
  curation action for the PAINT row rather than an expert-facing biology
  question.
