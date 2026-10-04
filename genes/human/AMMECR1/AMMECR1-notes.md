# AMMECR1 (Q9Y4X0) review notes

## 2026-10-04: PAINT/affinage review

AMMECR1 is a nuclear AMME-syndrome gene with no demonstrated molecular activity.
- **Localization:** [PMID:27811305 "Nuclear localisation of AMMECR1 was observed in both wild type and mutant; however, the non-uniform expression pattern of AMMECR1 was only found in cells transfected with mutant AMMECR1."]
- **Dimerization:** [PMID:29193635 "AMMECR1 and AMMECR1L proteins dimerize and localize to the nucleus as suggested by their nucleic acid-binding RAGNYA folds."]

Decisions:
- **Four nucleus/nucleoplasm rows: ACCEPT.** The nucleoplasm row rests on the HPA image (GO_REF:0000052).
- **11 protein-binding rows: REMOVE.** They come from HI-II-14, a splicing ORF screen, a variant screen and an Amer1 paper (rat Axin1 and Xenopus csnk1g1 partners). None involves AMMECR1L.
- **Synthesis:** an MF_DARK top-level gap, plus a location-only core function (nucleus), following the SDD3 pattern.

## Round 1 (PR #4025 review)

- **Retracted the p.G177D mislocalization claim.** My first version said p.G177D mislocalizes AMMECR1, a misreading of the abstract's "aberrant nuclear localisation patterns". The full text says the mutant is still nuclear, only unevenly distributed. Corrected everywhere, and the same overstatement is flagged in the affinage reference_review.
