# ARL14EP (ARF7EP / C11orf46) notes

## Two roles
1. ARL14 effector linking ARL14 to myosin 1E on MHC-II vesicles in human dendritic cells [PMID:21458045] (abstract-only).
2. Nuclear SETDB1-complex member:
   - Co-IP with SETDB1/MCAF1 (ATF7IP) from human cortex and HeLa; required for transcallosal connectivity in mouse [PMID:31511512].
   - SETDB2 MBD-C11orf46 crystal structure [PMID:38159574].
   - Worm ARLE-14 promotes MET-2 chromatin association [PMID:30140741] and monoallelic expression control [PMID:41315265].

## GOA calls
- **Protein binding:**
  - ARL14 → small GTPase binding.
  - MYO1E → myosin binding.
  - SETDB2 (Q96T68; 5 screen rows) → histone methyltransferase binding. Note: these rows are SETDB2, not SETDB1 (the SETDB1 association comes from co-IP, PMID:31511512).
  - ATF7IP and KANK2 → REMOVE.
- **Cytosol/cytoplasm → non-core.**
- **NEW:** nucleus (IDA, PMID:31511512).

## Review round 1 (PR #4176)
- Corrected partner identity: Q96T68 is SETDB2; summaries now lead with the SETDB2 MBD/CRD crystal structure (PMID:38159574).
- NEW histone binding (IDA, PMID:31511512): recombinant C11orf46 recognizes modified H3 tails on a peptide array and binds H3 independently of its CRD.
- NEW adaptor activity (IMP, PMID:21458045) for the ARL14-to-myosin 1E bridge.
- Nucleus row now quotes the immunohistochemistry result.
