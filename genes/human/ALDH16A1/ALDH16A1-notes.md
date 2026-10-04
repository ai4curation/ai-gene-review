# ALDH16A1 (Q8IZ83) review notes

## 2026-10-04: PAINT/affinage review

ALDH16A1 is a pseudoenzyme of the ALDH superfamily.
- **Direct assay:** [PMID:30529746 "In contrast, human ALDH16A1 apparently lacks measurable aldehyde oxidation activity, suggesting that it is a pseudoenzyme, consistent with the absence of the catalytic Cys in its sequence."]
- **Independent confirmation:** [PMID:40897711 "Surprisingly, ALDH16A1 lacks ALDH enzymatic activity, but binds to the anti-ferroptotic oxidoreductase thioredoxin (TXN), facilitating its translocation to the lysosome and subsequent degradation."]

Decisions:
- **IBA GO:0004029 aldehyde dehydrogenase (NAD+) activity** (deep node PTN000192666): REMOVE. This is target-specific loss inside the clade, recorded in propagation_review as PROPAGATION_BAD / PSEUDO_OR_SUBACTIVITY_LOSS.
- **IEA GO:0016491 oxidoreductase activity:** REMOVE.
- **Five generic protein-binding rows** (HuRI, BioPlex, OpenCell, with partners DERA, DLGAP4 and NOTCH2NLC): REMOVE.
- **Membrane HDA:** MARK_AS_OVER_ANNOTATED.
- **TXN inhibition** (single 2025 study): recorded as an MF_DARK knowledge gap and not added as NEW. core_functions is empty, following the dark-gene convention.
