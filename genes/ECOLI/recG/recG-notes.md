# recG (E. coli K-12, P24230) curation notes

Reviewed by Claude (AI-assisted) as the E. coli exemplar of the alternative RecG branch-migration step of `modules/bacterial_ruvabc_holliday_junction_processing.yaml`, and as the reference protein of the PTHR47964 family review.

- Provider deep research was not run (no provider API keys in this session).
- RecG and RuvAB are alternative branch-migration activities [PMID:8428576, "We suggest that RecG and RuvAB provide alternative activities than can promote branch migration of Holliday junctions in recombination and DNA repair"].
- Holliday junction helicase complex (IDA, PMID:8428576) is marked over-annotated, not removed: RecG acts as a monomer [PMID:10871364, "These data suggest that RecG functions as a monomer to unwind junction DNA"], but the curator's full-text evidence is not cached.
- PTHR47964:SF1 contains both RecG and Mfd (transcription-repair coupling factor); RecG-specific function is asserted at PAINT node PTN002773745, Mfd function at PTN008553567. See the family review.
- 2026-11-10: added a NEW IDA row and core MF for GO:0009378 four-way junction helicase activity, the junction-specific activity RecG evolved for [PMID:7957087, "These results define RecG as a new class of helicase that has evolved to catalyse the branch migration of Holliday junctions"]. GO:0043138 (3'-5' polarity) is still accepted but would also fit UvrD, PcrA or Rep; GO:0009378 is not RuvAB-restricted (BLM, FANCM, Rqh1 carry it).
