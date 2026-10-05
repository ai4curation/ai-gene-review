# EGD1 curation notes

## 2026-10-01 current-GOA / IBA review

- Refreshed EGD1 from current UniProt/GOA before editing. Current GOA has 17
  live rows after the header; the refresh materialized a ComplexPortal
  `GO:0005854` IPI row from PMID:26618777 and a second SGD
  `GO:0006613` IGI row from PMID:10518932 with `SGD:S000002660` as the
  supporting entity.
- Checked the PAINT export for `PANTHER:PTHR10351`: both EGD1 IBA rows trace
  to `PANTHER:PTN000039173`. The node-level assertions for cytosol and
  nascent-polypeptide-associated-complex membership are consistent with direct
  yeast NAC evidence, so both rows remain `ACCEPT` with `NO_FAILURE_CORE`
  propagation reviews.
- The refreshed GOA no longer emits the broad UniProt keyword
  `GO:0015031 protein transport`, the older IntAct/Xeno interaction
  `GO:0005515 protein binding` rows from PMID:16554755 and PMID:27107014, or
  obsolete `GO:0051082 unfolded protein binding` from PMID:9482879. These rows
  were kept for source preservation and marked `retired: true`.
- Live IntAct `GO:0005515 protein binding` rows from PMID:16926149,
  PMID:18719252, and PMID:37968396 were changed from
  `MARK_AS_OVER_ANNOTATED` to `REMOVE`: generic protein binding is a root-level
  molecular-function assertion, and EGD1's specific molecular role is the NAC
  chaperone activity at cytosolic ribosomes.
- The retired `GO:0051082` annotation had been the review's only explicit
  molecular-function bridge to chaperone activity, so I added a conservative
  `NEW` row for the existing term `GO:0044183 protein folding chaperone`
  supported by direct NAC ribosome/nascent-chain evidence from PMID:10219998
  and PMID:26618777.
- Checked newer NAC literature cached locally. PMID:38177147 supports keeping
  mitophagy as a non-core phenotype for EGD1. PMID:39426497 mainly dissects
  Btt1/Nac-beta2 specialization relative to abundant Egd1/Nac-beta1, and
  PMID:42538864 links NAC/Ssb to mitochondrial-surface misfolded-protein
  control; neither changed the GO action set for EGD1.

## 2026-10-05 PR #3747 reviewer follow-up

- Demoted the retired `GO:0015031 protein transport` keyword row from `ACCEPT`
  to `KEEP_AS_NON_CORE`. The 1998 NAC targeting paper supports a broad
  targeting phenotype, but the stale root transport term is not core when the
  live, more specific `GO:0006613` membrane-targeting rows are already non-core.
- Added direct support to the retained non-core nucleus and macroautophagy rows.
  The `GO:0016236` row comes from the 2009 selective-mitophagy screen in SGD;
  because the cached PMID:19793921 text is abstract-only and does not name EGD1,
  the row remains a conservative non-core retention rather than a mechanistic
  macroautophagy assertion.
- Replaced generic ribosome/nascent-chain quotes for `GO:0044183` and
  `GO:0051083` with PMID:26618777 chaperone and aggregation text, and made the
  three live `GO:0005515 protein binding` removals name the EGD2 partner hit
  they are intentionally collapsing into NAC complex membership.
- Recorded the old GAL4 DNA-binding/transcriptional activity as a suggested
  question instead of a proposed term; the signal is in UniProt and the gene
  name, but there is not enough current evidence in this review to make a new
  nuclear MF or BP assertion.
