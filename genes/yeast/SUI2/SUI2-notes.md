# SUI2 IBA re-review notes

## 2026-09-29

- Rebasing from `origin/main` was a no-op on `codex/yeast-sui2-iba-rereview`.
- Re-read the cached SUI2/eIF2alpha publications that support the reviewed rows, including
  the original SUI2 identification paper (PMID:2649894), ternary-complex biochemistry
  (PMID:14698289, PMID:16565414), Pi-release/start-site selection work
  (PMID:16246727), the reconstituted yeast initiation system paper (PMID:12008673),
  the eIF5 GDI paper (PMID:20485439), and eIF2 assembly work through Cdc123
  (PMID:23775072, PMID:26211610).
- Checked the PTHR10602 PAINT snapshot against GOA's five IBA rows. Current PAINT still
  has the conserved `PTN000063907` IBD rows for `GO:0003743`, `GO:0043022`, and
  `GO:0006413`, plus the eukaryote-restricted `PTN000063908` IBD rows for
  `GO:0005850` and `GO:0033290`. SUI2 itself appears among the descendant seeds for all
  but the ribosome-binding row; that is valid target support, not circular evidence.
- Preserved all five IBA calls as `ACCEPT` and added `propagation_review` blocks
  with the relevant PANTHER PTN source nodes. Kept the `GO:0043022 ribosome binding`
  IBA because R53 directly contacts 18S rRNA helix 23 in the yeast PIC; the
  translation-initiation-factor and methionyl-initiator-tRNA-binding rows are already
  present and do not replace that 40S contact.
- Converted the legacy generic `GO:0005515 protein binding` rows from
  `MARK_AS_OVER_ANNOTATED` to `REMOVE`. The underlying interactions are not being
  disputed; `GO:0005515` is simply too low-information when eIF2 complex membership,
  multi-eIF complex membership, and translation-initiation factor activity are already
  available.
- Searched for 2025+ literature with the exact PubMed query
  `((SUI2 OR YJR007W OR eIF2alpha OR eIF2-alpha OR "eIF2 alpha") AND "Saccharomyces cerevisiae") AND 2025:3000[pdat]`.
  The result set was dominated by Gcn2-regulation or stress-readout papers
  (PMIDs:39992511, 40198700, 40440025, 40862493, 42394718, 42527248, 42543787) and one
  Cryptococcus eIF3 preprint (PMID:41648462); these do not change the direct Sui2
  functional calls. A web search for 2025-2026 SUI2/eIF2alpha papers likewise did not
  reveal a new SUI2-specific paper that needed to be added to the review.

## 2026-10-01 current-GOA refresh

- Refreshed UniProt/GOA for SUI2. The live GOA snapshot has 36 rows. The current
  `PTHR10602` PAINT cache still carries five SUI2 IBA rows on `PTN000063907` and
  `PTN000063908`; no IBA row needed a changed action.
- Preserved six vanished rows as retired: old GO_REF:0000120 IEA rows for RNA binding
  and translation initiation factor activity, keyword IEAs for broad translation and
  translational initiation, and no-longer-live protein-binding rows from PMID:16554755
  and PMID:27107014.
- Reviewed five newly seeded current rows. The InterPro `GO:0003723` row and two
  `TIF5` protein-binding rows were removed as generic, the InterPro `GO:0003743`
  row was accepted as redundant but correct, and the ComplexPortal PMID:8947054
  `GO:0005850` eIF2-complex row was accepted.

## 2026-10-05 reviewer follow-up

- Resolved PR review blockers by fetching Thakur et al. 2020 as PMID:32955564
  and using it as the primary support for `GO:0043022 ribosome binding` and the
  R53/R55/R57 start-codon-fidelity claims; by changing the broad PMID:12008673
  `GO:0005840` ribosome row to `KEEP_AS_NON_CORE` because `GO:0033290` captures
  the 48S preinitiation complex more precisely; and by replacing the duplicated
  `core_functions` entries with contributions to the eIF2 complex's Met-tRNAi
  and GTP binding plus Sui2's direct 40S contact.
