# ARHGEF3 (XPLN) notes

## Biology
- XPLN is a GEF for RhoA/RhoB, not RhoC (RhoC I43 confers the selectivity), RhoG, Rac1 or Cdc42; it drives ROCK-dependent stress fibres [PMID:12221096].
- An endogenous mTORC2 inhibitor [PMID:24043828]:
  - Purified XPLN inhibits mTORC2 kinase toward Akt; the N-terminal 125 aa are necessary and sufficient; the effect is GEF-independent.
  - XPLN restrains myoblast differentiation.
  - DEPTOR is the comparator and carries GO:0004860 IDA and GO:1903940.
- Transferrin uptake in erythroid cells [PMID:21715309].
- Knockout mice: muscle regeneration via autophagy, GEF-dependent [PMID:33406419].

## GOA calls
- **Protein binding (15 rows, all Y2H screens) → REMOVE.** Partners: TRIM27, TRIM23, CEP70, HSF2BP, TERF1, DDIT4L, PBX4, PICK1.
- **ACCEPT:** GEF activity; positive regulation of Rho signal transduction (IBA, PTN000517811 seeded by fly RhoGEF64C); cytosol.
- **Non-core:** Rho signal transduction (TAS), general signalling parents, cytoplasm.
- **NEW:** protein kinase inhibitor activity (IDA) and negative regulation of TORC2 signaling (IDA), both from PMID:24043828.
- Review round (PR #4167):
  - NEW kinase-inhibitor term changed to GO:0030291 (Ser/Thr kinase inhibitor). Comparator: DEPTOR (Q8TB45) carries GO:0030291 by IDA and IBA (QuickGO, 2026-10-04).
  - Cytosol and cytoplasm changed to KEEP_AS_NON_CORE. UniProt's cytoplasm is by similarity only, and U937 cells show mainly nuclear ARHGEF3 that moves to the cytoplasm on HDACi [PMID:25494542].
  - RHOA and RHOB are recorded as substrates in core_functions. A NEW IDA GO:0005085 row could not be added, because validation rejects NEW for a term already present in GOA.
  - Declined, not annotated:
    - Muscle regeneration/autophagy [PMID:33406419]: a knockout phenotype downstream of RhoA; erratum not checked.
    - Transferrin uptake [PMID:21715309]: zebrafish and K562 knockdown, an indirect phenotype.
    - ACLY stabilization [PMID:36241648]: single study, GEF-independent.
