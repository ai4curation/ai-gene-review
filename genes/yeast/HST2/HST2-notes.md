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

## 2026-10-16: GO:0045950 rows resolved (issue #4027)

The three `GO:0045950 negative regulation of mitotic recombination` rows from
PMID:16051752 (IMP; IGI with SIR2, SGD:S000002200; IGI with FOB1,
SGD:S000002517) were UNDECIDED because the paper is abstract-only. SGD's GO
detail for this reference (`https://www.yeastgenome.org/backend/reference/16051752/go_details`,
retrieved 2026-10-16) confirms the three HST2 rows and the With partners, and
shows the same term was also given to HST1 from this paper. The abstract states
the claim directly [PMID:16051752 "Sir2-independent life-span extension is
mediated by Hst2, a Sir2 homolog that promotes the stability of repetitive
ribosomal DNA"]: instability of the tandem rDNA array is recombination between
repeats, so "promotes rDNA stability" and "negatively regulates mitotic
recombination" are the same claim. GO has no regulation child of
`GO:0045458 recombination within rDNA repeats`, so GO:0045950 is as precise as
the ontology allows.

Decision: all three rows `KEEP_AS_NON_CORE`, matching the sibling
`GO:0000183 rDNA heterochromatin formation` IMP row from the same paper. The
rDNA effect is calorie-restriction-dependent; the core HST2 function remains
NAD-dependent H4K16 deacetylation in mitotic chromatin compaction.
