# APELA notes

## Biology
- ELABELA/Toddler is a secreted 32-aa peptide hormone and APLNR agonist.
  - Zebrafish: heart and endoderm [PMID:24316148]; gastrulation motogen [PMID:24407481].
  - Human APJ signalling (cAMP, ERK, internalization, HUVEC angiogenesis) [PMID:25639753].
  - Human heart binding, an endogenous agonist [PMID:28137936].
  - Kd 0.51 nM and Gi signalling; rat fluid homeostasis [PMID:25995451].
  - Rat heart inotropy [PMID:26611206].
  - Mouse knockout cardiovascular defects [PMID:28854362].
  - Placental ELA and preeclampsia [PMID:28663440].
  - Cryo-EM of APJ-G protein with ELA bound [PMID:35817871].

## GOA calls
- **Core, ACCEPT:** hormone activity, apelin receptor binding, apelin receptor signaling pathway, extracellular region, heart development.
- **GPCR signaling (IDA, cryo-EM) → MODIFY** to apelin receptor signaling pathway.
- **Adult heart development (ISS) → REMOVE.** The GOA WITH/FROM is Q9WV08, mouse Aplnr: the receptor, not an APELA homolog.
- **Non-core:**
  - Zebrafish gastrulation and endoderm ISS rows.
  - Mouse vascular ISS rows.
  - Placenta vessels.
  - Trophoblast migration (IMP); angiogenesis (IMP); GPCR internalization (IMP).
  - Rat heart contraction and ERK (ISS).
- No IBA rows; no NEW rows.
- Review round (PR #4156):
  - Coronary vasculature now cites PMID:28890073 (Ela/Apj coronary migration defect).
  - GO:1903589 (sprouting-angiogenesis EC proliferation) → MARK_AS_OVER_ANNOTATED. The donor paper reports a migration defect, and "proliferation" appears only twice in its text, both in background statements.
  - Each mouse ISS row is adjudicated on its own donor evidence (found via QuickGO on P0DMC4).
  - All 17 ISS rows carry propagation_review. The Q9WV08 row is PROPAGATION_BAD: the receptor's own adult heart IMP comes from PMID:28663440.
