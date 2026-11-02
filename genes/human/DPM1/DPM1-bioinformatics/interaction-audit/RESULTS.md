# Executed DPM1 interaction audit

The saved query contains 101 records incident to O60762. Selecting the seven historical binding-source PMIDs gives ten records: one from PMID:16280320 and three each from PMID:25416956, PMID:25910212 and PMID:32296183. These are repeated assay/source records, not ten independent partners.

| Source | Physical lines | Selected participant and scope |
|---|---|---|
| 16280320 | 5 | Human DPM1 O60762 with hamster DPM3 Q4LDX8; anti-tag co-immunoprecipitation in a CHO host. Participant fields, rather than a reversed accession statement in a source comment, determine this identity. |
| 25416956 | 61, 63, 64 | Human TDO2 P48775; pooled, array and validated two-hybrid contexts. |
| 25910212 | 46, 47, 49 | Human TDO2 P48775; repeat assay contexts with DPM1 residue features retained in the full output. |
| 32296183 | 43, 50, 51 | MEOX2 clone Q6FHY5; pooled, array and validated two-hybrid contexts. |

The target, TDO2 and assayed MEOX2 clone reference sequences reproduce the recorded ROGIDs. Q6FHY5 has 303 residues versus 304 in canonical P50222. The difference is one glutamine within a repeated stretch: deletion at any canonical position 81–84 produces the same clone sequence. A uniquely localized deletion is therefore not inferred. The difference lies outside the annotated homeobox at residues 187–246 of P50222.

Official TDO2 function establishes an enzyme partner, and MEOX2 has experimentally curated DNA-dependent transcription-factor activity. These facts support binding-class refinements without assigning the partner's catalytic or transcriptional function to DPM1. Neither the positive binary measurements nor the reference-sequence match establishes a native DPM1 metabolic or transcriptional pathway. DPM3 association remains a separate complex-assembly observation; the free-DPM1/CHIP finding is supported by its primary abstract, not by silently treating the hamster DPM3 record as a STUB1 interaction.

All ten selected records have a non-negative interaction flag. The three original DPM3 association sources PMID:10835346, PMID:10944123 and PMID:23856421 have no matching record in this particular query snapshot; their experimentally documented co-immunoprecipitations remain independent evidence. Original platform Methods distinguish the 2014 three-of-four retest criterion from HuRI's separately reported quadruplicate retesting and sequence confirmation. Dataset-level orthogonal testing is not claimed for each DPM1 pair.

`python3 replay.py --check` reproduces both output files. The alternative target P48775 returns six incident and six selected records from the two TDO2 sources. Full raw fields, computed identities and provenance are available alongside this report.
