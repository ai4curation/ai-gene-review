# Rtl8c notes

Mouse Rtl8c: 112-aa capsid-only, ~70% identity to Rtl8a/8b, unique leucine zipper; cytoplasmic (vs nuclear Rtl8a/8b) [PMID:39875098 "the former in the nuclei (nucleoli) and the latter in the cytoplasm"]. Single Rtl8c KO no behavioural abnormality. Murine CXX1B (RTL8 ortholog, closest to RTL8C) is a UBQLN2 interactor [PMID:33277362].
Calls: ND MF MODIFY->protein-macromolecule adaptor activity; ND BP MODIFY->positive regulation of protein catabolic process; NEW cytoplasm (IDA).

## Deep research integration (OpenScientist, 2026-10-24)

Report read as leads; checked against cached sources.

- Contradiction (report vs review): the report calls Rtl8c "constitutively nucleolar". That is human RTL8 data [PMID:35247097 "Under endogenous and overexpressed conditions, RTL8 localizes to nucleoli."], which does not resolve the mouse paralogs. In mouse, "mRTL8A/8B with the N-terminal NLS-like signal is accumulated in the nuclei of NIH3T3 cells while mRTL8C without it is located in the cytoplasm" [PMID:39875098]. The review's cytoplasm call stands; the NLS quote was added to it.
- Correction to the review itself: the description said "A single Rtl8c knockout shows no behavioural abnormality". The cached full text of PMID:39875098 does not say this. It reports generating Rtl8c flox mice, says "In this work, mouse Rtl8a and Rtl8b were knocked out; however, Rtl8c still remained active", and calls for a future comparison of "Rtl8c KO, Rtl8a and Rtl8b DKO and Rtl8a, Rtl8b and Rtl8c TKO mice". The report also found no Rtl8c KO phenotype. Sentence removed and replaced by what the paper does show; reference_review note corrected.
- Verified and added: no Cys or His in F6TUF7 (checked on the UniProt sequence; 112 aa, C-terminus ...KEEFGWEEDEDF), so no CCHC knuckle; tissue expression "Rtl8a-c mRNAs exhibit higher expression in the cerebrum and cerebellum, but are ubiquitously expressed in all other tissues and organs, with the exception of no Rtl8c expression in the liver" [PMID:39875098]; mouse brain RTL8-UBQLN2 interaction [PMID:35247097], added to the adaptor MODIFY row.
- Placental expression of the Cxx1/Mart8 cluster [PMID:25888968] is cluster-level with confusing paralog naming (Cxx1c/Mart8a etc.); not used.
- LDOC1 paralog analogies and UBQLN2 biology papers (26637328, 31889386, 27764577, 34750982, 37501540, 26521126) are context only.

No action changes. Cross-species: if the Rtl8a review or a human RTL8 review repeats the single-Rtl8c-KO claim, it should be dropped there too (Rtl8a's review does not carry it).
