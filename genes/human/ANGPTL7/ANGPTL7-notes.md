# ANGPTL7 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANGPTL7/CDT6 is a secreted homotetrameric angiopoietin-like protein (PMID:11682471). Its two documented roles:
  - It keeps the cornea avascular (PMID:25622036; knockdown is rescued by recombinant protein).
  - It remodels trabecular meshwork ECM and disrupts fibronectin fibrils (PMID:21199193).
- **IOP and glaucoma:**
  - Human protective variants lower IOP (PMID:32369491).
  - Angptl7 KO mice resist the dexamethasone IOP rise but have elevated baseline IOP, and blocking antibodies raise outflow (PMID:38497513).
- **Wrong identifier: GO:0006979 TAS (PINC, 2003-09-04).** It cites PMID:8026862, the NK-enhancing factor (peroxiredoxin) cloning paper. Removed, with WRONG_IDENTIFIER. This is the same PINC batch and date as ANAPC4's HLA-paper row (PMID:6180011), which suggests a systematic PMID problem in that PINC load.
  - The only ANGPTL7 oxidative-stress paper (PMID:32525822) has ANGPTL7 mediating oxidative stress, not responding to it.
- **Blood coagulation IEA (fibrinogen/angiopoietin-like domain):** removed.
- **ACTN2 protein-binding IPI:** removed.
- **Kept as non-core** (round 2: the ECM IBA moved to ACCEPT):
  - ECM IBA (is_active_in), since matrix deposition is not shown.
  - Identical protein binding (homotetramer).
- **Knowledge gap:** the receptor is unknown (MF_DARK).

## 2026-10-04 round 2 (reviewer comments on #4063)

- **ECM IBA (is_active_in):** KEEP_AS_NON_CORE changed to ACCEPT. My earlier argument (no matrix incorporation shown) rebutted a located_in claim that the row doesn't make. is_active_in asserts where ANGPTL7 acts, and it acts on the trabecular meshwork matrix (fibronectin fibril assembly). Added to core locations.
- **Affinage reference_review:** now explicitly declines PMID:35136015 (SP1 / RhoA-ROCK cross-linked actin networks), a single study downstream of an unknown receptor.
- **Other fixes:**
  - Core function now cites the hydraulic-conductivity and KO results (PMID:38497513).
  - Replaced the PMID:32369491 fragment quote with the title sentence.
  - The description notes the elevated baseline IOP of the KO mice.
