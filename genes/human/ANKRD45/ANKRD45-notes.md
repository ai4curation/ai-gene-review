# ANKRD45 notes

- The one functional study is PMID:31208154 (full text; Hep3B and other lines plus zebrafish). ANKRD45 is not detected in interphase, is cytoplasmic at metaphase, sits at the cleavage furrow in anaphase and telophase, and is at the midbody ring during cytokinesis. Knockdown or CRISPR loss causes apoptosis. Zebrafish mutants are viable with normal cilia; liver cysts appear only under KrasG12V.
- Location rows (cytoplasm, cytosol, cleavage furrow, midbody, Flemming body) are all ACCEPT. The midbody IBA node PTN001193669 is seeded only by ANKRD45 itself (NO_FAILURE_CORE).
- Cell population proliferation (IBA and IMP) → KEEP_AS_NON_CORE, because the term is a population-level outcome confounded by the concurrent apoptosis. (Corrected in round 2: the paper does measure proliferation, by CCK-8, BrdU and a G0/G1 delay, and time-lapse shows division defects; zebrafish mutants show no proliferation defect without Kras.) IBA seeds are ANKRD45 and zebrafish ankrd45 (NO_FAILURE_NON_CORE).
- MAGEA2B Y2H → REMOVE. MF ND → ACCEPT.
- PubMed recall: one schizophrenia eQTL study (overexpression inhibits neuronal differentiation; no GO drawn), plus prognostic and methylation lists.
- knowledge_gaps: MF_DARK.

## Round 2 (reviewer, PR #4133)

- My first draft wrongly said the paper measured no proliferation defect. A regex hit on the Methods section stood in for reading the Results, which contain CCK-8, G0/G1 accumulation, BrdU/TUNEL and time-lapse division defects. The reason, description and gap boundary now quote those results.
- The gap now centres on the mismatch between midbody-ring localization and a G0/G1 delay.
- Why the midbody IBA is NO_FAILURE_CORE while core_functions is empty: the localization is ANKRD45's best-established property and the IBA transfers it correctly, but core_functions requires a molecular function or process the gene performs, and none is established.
