# Tpm1 (rat) review notes

- UniProt P04692 (TPM1_RAT), RGD:3898, GeneID 24851; fetch-gene resolved the expected accession.
  51 GOA rows.
- No deep-research API keys; literature synthesis in `Tpm1-deep-research-manual.md`.
- Full text read: PMID:19041430 (recombinant rat Tpm1 isoforms smTM, TM2, TM5a, TM1b9a; actin
  cosedimentation and ATPase regulation) [PMID:19041430 "The four tropomyosin isoforms selected
  for this study were products of the rat α-TM gene (TPM1)"], PMID:22812662 (rat alpha/beta
  skeletal Tm dimers). All other cited PMIDs are abstract-only.

## Decisions

- Core: actin filament binding (GO:0051015); thin-filament regulation of striated/cardiac
  muscle contraction; stabilization of non-muscle actin filaments/stress fibers.
- `actin binding` and `cytoskeletal protein binding` rows -> MODIFY to actin filament binding
  (correct but general).
- `identical protein binding` rows -> MODIFY to protein homodimerization activity (homodimeric
  coiled coil, PMID:7568216, PMID:22812662).
- `cytoplasm`, `cytoskeleton`, `actin cytoskeleton`, `myofibril` -> MODIFY to actin filament /
  stress fiber / striated muscle thin filament as appropriate.
- `muscle contraction` TAS -> MODIFY to striated muscle contraction and cardiac muscle contraction.
- `positive regulation of heart rate by epinephrine` (ISO from mouse) -> MARK_AS_OVER_ANNOTATED:
  tropomyosin regulates contractility in cardiomyocytes, not pacemaker rate; a mutant-mouse
  response phenotype is indirect.
- Cell migration/adhesion/wound healing/ruffle/bleb/VSMC rows -> KEEP_AS_NON_CORE (cell-level
  consequences of actin stabilization; kept consistent with human TPM1 review).
- No NEW terms proposed: the existing set covers the core functions; GO:0005862 (muscle thin
  filament tropomyosin) is used only in core_functions.in_complex.

## 2026-10-28 review-fix pass

- A curated CC:FUNCTION quote ("Plays a central role, in association with the troponin complex...") now cites file:rat/Tpm1/Tpm1-uniprot.txt instead of UniProtKB:P04692, so record_section backfill and the local quote check apply; added that file to references.
- Removed supported_by self-citations of the gene's own -deep-research-manual.md where a primary citation in the same block already supports the row (the reviewer's own conclusion is not independent evidence). The validator now warns that no annotation cites the deep-research file; that warning is accepted deliberately, which sets the status to DRAFT.
