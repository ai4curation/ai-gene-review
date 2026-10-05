# HST2 review notes

## 2026-10 IBA/current-GOA refresh

- Refreshed HST2 against current GOA. The three live IBA rows still trace to
  current PTHR11085 nodes:
  - `GO:0005634 nucleus`: `PANTHER:PTN008492176`
  - `GO:0017136 histone deacetylase activity, NAD-dependent`:
    `PANTHER:PTN008718612`
  - `GO:0000183 rDNA heterochromatin formation`: `PANTHER:PTN000119247`
- The nuclear-localization and histone-deacetylase IBAs are core for Hst2.
  Hst2 shuttles between the nucleus and cytoplasm and has direct yeast support
  for NAD-dependent histone deacetylase activity [PMID:10811920;
  PMID:11226170; PMID:17110954].
- The rDNA-heterochromatin IBA is defensible but non-core. The PAINT node is
  seeded by Hst2 itself plus fission-yeast Hst4, and Hst2 promotes rDNA
  stability, but the best-resolved catalytic role is H4K16 deacetylation during
  Bmh1-dependent short-range chromosome compaction rather than rDNA
  heterochromatin formation [PMID:16051752; PMID:33187982].
- Three old UniProt keyword rows are no longer live in the current GOA export
  and were retained as `retired: true` history:
  - `GO:0006351 DNA-templated transcription`
  - `GO:0016740 transferase activity`
  - `GO:0046872 metal ion binding`
- The stale generic metal-binding row now resolves to `REMOVE`; the retained
  `GO:0008270 zinc ion binding` row captures the zinc cofactor claim more
  precisely.
- Added a conservative `NEW` recommendation for `GO:0030261 chromosome
  condensation`, supported by the 2021 yeast Bmh1/Hst2 paper. The broader term
  fits Hst2-dependent short-range compaction without implying the full mitotic
  chromosome-segregation context of `GO:0007076 mitotic chromosome
  condensation`.
- The current refresh split the previous combined `GO:0045950 negative
  regulation of mitotic recombination` IGI review into separate exact rows for
  the SIR2 (`SGD:S000002200`) and FOB1 (`SGD:S000002517`) genetic partners.
  The PMID:16051752 cached record is abstract-only, so both IGI rows remain
  `UNDECIDED` pending full-text confirmation of the interaction assays.
- A 2026-10 PubMed/web refresh found the primary 2021 yeast Bmh1/Hst2 paper
  for short-range chromosome compaction and no newer HST2-specific *S.
  cerevisiae* paper that changes the core deacetylase, nuclear/cytoplasmic
  shuttling, rDNA, or mitotic-recombination assessment.
