# ruvA (E. coli K-12, P0A809) curation notes

Reviewed by Claude (AI-assisted) as the E. coli exemplar of the RuvA step of `modules/bacterial_ruvabc_holliday_junction_processing.yaml`.

- Provider deep research was not run for this gene (no provider API keys in this session); the review rests on the UniProt record and the cached publications.
- RuvA confers junction specificity and loads RuvB [PMID:1617728, "RuvA protein provides specificity by binding to the Holliday junction, thereby reducing the requirement for RuvB by 50-fold"]; the motor is RuvB [PMID:1617728, "the RuvB ATPase provides the motor force for branch migration"].
- GO:0009378 four-way junction helicase activity is accepted on all three rows (IDA, PAINT IBA at PTN008659601, IEA) because RuvA is an essential subunit of the RuvAB helicase; the core function records it as `contributes_to`, with GO:0000400 as the RuvA activity.
- ATP binding (InterPro2GO from IPR013849/IPR011114) is removed and filed as an InterPro source defect: RuvA is not an ATPase.
- SOS response rows (IBA, IEA, IEP, RCA) are kept as non-core: ruvAB is a LexA-repressed SOS operon [PMID:2842314, "the transcription from both sites was repressed by the LexA repressor"].
- Not added: replication fork reversal. UniProt states RuvAB acts in fork reversal, but no GOA row exists and the cached abstract (PMID:9814711) does not itself state reversal by RuvAB; left for a future curator with full text.
