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

## Round 1 (PR #3976 review)

- **Residue claims added.** `ALDH16A1-bioinformatics/catalytic_site_msa.py` runs MAFFT L-INS-i over ALDH2, ALDH1A1, ALDH3A1 and the frog, zebrafish and mouse ALDH16 orthologs.
  - At the ALDH2 Cys319 column, human ALDH16A1 has a gap.
  - At the Glu285 column it has Ala272, but the ELGGK motif is absent.
  - Frog retains both residues (Cys309, Glu275).
  - Both are recorded as LOST against `PANTHER:PTHR11699#aldh_nucleophile`, with no target position, matching the family review's refusal to assert one.
  - gene_residue_claims: 4 pass, 2 unresolved (target intentionally omitted).
- **TXN active-site occlusion.** It comes from an AlphaFold2 model in PMID:40897711, and the description now says so.
- **PMID:40897711 inactivity.** Its test is a whole-lysate total-ALDH kit, now described as consistent with the recombinant assay rather than as independent confirmation.
- **New negatives from PMID:30529746.** No esterase activity and no NAD(H) binding for the human protein are now cited.
