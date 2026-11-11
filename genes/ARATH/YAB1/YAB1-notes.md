# YAB1 (FIL) review notes

- 2026-10-28: fetch-gene resolved O22152 (YAB1_ARATH, At2g45190, GeneID 819127). 39 GOA rows.
- Deep-research API unavailable; literature compiled manually in YAB1-deep-research-manual.md.
- Key paper PMID:23133401 (fruit mediolateral patterning; JAG/FIL vs BP/RPL mutual repression) read in full.
  Its evidence is genetic/expression (BP::GUS, qRT-PCR, in situ), supporting the existing fruit development
  rows; not used to add a NEW process term (regulatory/necessity evidence only).
- MF: DNA-binding TF activity is directly supported [PMID:26530088 EMSA + LUC on MYB75 promoter;
  PMID:23025792 transactivation]. Early claim of non-sequence-specific binding [PMID:11812777] is superseded
  in part by FBE-specific binding [PMID:26530088]. FIL is bifunctional (activator and, with LUG/LUH, repressor),
  so GO:0003700 and GO:0006355 are kept at that level rather than refined to activator/repressor.
- 13 bare protein binding rows removed per policy (LUG, LUH, SPL/NZZ, TCPs, KAN1, JAZ3, ERF8, IDD14, ZFP3).
- Cell fate commitment rows (IBA and IMP) refined to abaxial cell fate specification (verified is_a descendant via OAK).
- Many developmental BP rows (flower, inflorescence meristem, fruit, SAM, leaf, organ position) kept as non-core:
  they reflect downstream/non-cell-autonomous consequences of FIL's abaxial TF function.
