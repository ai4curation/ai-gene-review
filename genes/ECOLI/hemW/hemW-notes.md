# hemW (P52062, E. coli K-12; formerly yggW) notes

Deep research was unavailable for this gene (falcon returns 403 and asta returned nothing
useful in RADICAL_SAM Phase 1), so these notes are built from cached papers, the PMC full text
of PMID:29282292 (PMC5818191; the cache has only the abstract) and UniProt.

## Function: heme chaperone, not CPDH
- One heme per subunit; the cluster is required for dimerization and transfer but not for binding.
  [PMID:29282292 "intact iron-sulfur cluster was required for HemW dimerization and HemW-catalyzed heme transfer but not for stable heme binding"]
- Transfers heme to heme-depleted NarGHI and restores its activity.
  [PMID:29282292 "heme that was covalently bound to HemW was actively transferred to a heme-depleted, catalytically inactive nitrate reductase"]
- PMC full text: "E. coli pGEX hemW failed to restore anaerobic growth of the mutant" (the delta hemN strain), which shows that HemW does not harbor coproporphyrinogen III dehydrogenase activity.
- PMC full text: HemW binds [14C]SAM. Its SAM cleavage is at the HemN-without-substrate background level. "SAM did not influence the heme transfer reaction."
- PMC full text: the hemW mutant has a "slight, but highly reproducible growth phenotype" under nitrate respiration, which suggests that a second heme-inserting system exists.
- PMC full text: butanone extraction points to covalent heme, but "strong binding of the heme in a tight hydrophobic pocket ... cannot be excluded".
- L. lactis orthologue: [PMID:22142238 "showed that it is devoid of CPDH activity in vivo and in vitro"]
- Review: [PMID:37101575 "heme is inserted into enzymes by the cytoplasmic heme chaperone HemW"]

## GO term search for heme chaperone activity (QuickGO, 2026-10-19)
- No MF term exists for "heme chaperone", "heme transfer", "heme insertion", "heme delivery" or "heme carrier".
- GO:0016530 metallochaperone activity covers metal ions only. GO:0017003 protein-heme linkage is a process for covalent heme attachment (cytochrome c type), and NarI heme b is non-covalent.
- Therefore proposed_new_terms: "heme chaperone activity", parent GO:0140104 molecular carrier activity.
- No NEW BP. GO:0017004 cytochrome complex assembly is possible, but the in vivo phenotype is slight, so it is left as a suggested question.
- No NEW GO:1904047: catalysis is not established (per the Phase 2 brief), even though [14C]SAM binding was shown.

## PAINT / propagation
- The IBA GO:0006779 comes from PTN000358281, the same node as for RSAD1, and reaches hemW. REMOVE, with a propagation_review.
- GO:0051989 sits on PTN000358335 (the HemN clade) and does not reach hemW. This is consistent.
- The ISS GO:0006779 donor Q9CGF7 (L. lactis) has an IDA to GO:0006779 citing PMID:22142238, which reports no CPDH activity. The donor is flagged UNRESOLVED.

## Decisions
- REMOVE GO:0004109 (IEA) and GO:0006779 (IBA, IEA, ISS).
- ACCEPT the cytoplasm rows (3) and GO:0020037 (IDA).
- KEEP_AS_NON_CORE GO:0003824, GO:0042803 and GO:0051539 (4 rows).
- MODIFY GO:0051536 to GO:0051539.
