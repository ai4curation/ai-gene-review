# yihU (P0A9V8) notes

## Session 2026-11-10

Deep research via `just deep-research` failed in this environment (deep-research-client
dependency unresolvable offline); review built from UniProt and cached literature:
PMID:24463506 (abstract), PMID:19372223 (abstract; PMC2713508 full text not retrievable,
publisher restricts XML), PMID:41676062 (review, full text). The YihU structure and
kinetics paper (Sharma et al. 2020, ACS Catal, DOI 10.1021/acscatal.9b04427) has no PMID;
its results are used only through UniProt's curated text (Ref.6, ECO:0000269).

- SLA reductase is the fourth sulfo-EMP reaction [PMID:24463506].
- kcat 332 s-1, KM 0.3 mM for SLA [PMID:41676062 "exhibits high catalytic proficiency
  (kcat = 332 ± 9 s−1, KM = 0.3 ± 0.038 mM, kcat/KM = 1,090 ± 120 mM−1 s−1) for SLA
  reduction (Sharma et al., 2020)"].
- NADH-dependent SSA -> GHB reduction in vitro; deletion reduces tolerance to exogenous
  SSA [PMID:19372223]. UniProt (Ref.6): 42,000-fold greater efficiency for SLA than SSA.
- Homotetramer, dimer of dimers [UniProt SUBUNIT, PubMed:19372223, Ref.6].

PAINT: PTN000541321 (PTHR22981 root-level node, taxon blank) IBD GO:0016616 with 8
seeds including UniProtKB:P0A9V8. It grounds only the generic CH-OH/NAD(P)
oxidoreductase parent of GO:0061596, not the SLA-specific activity.

Decisions:
- GO:0061596 x2 ACCEPT (core).
- GO:0016491, GO:0016616 (IBA, ARBA IEA) MODIFY -> GO:0061596.
- GO:0047577 (IDA, IEA) KEEP_AS_NON_CORE: genuine but minor secondary activity with a
  deletion phenotype under SSA stress (tier 1 of the promiscuity tiers).
- GO:0009407 toxin catabolic process MODIFY -> GO:0110095 cellular detoxification of
  aldehyde: SSA is a cytotoxic metabolite aldehyde, not a toxin in GO's sense.
- GO:0051287 NAD binding KEEP_AS_NON_CORE; GO:0050661 NADP binding
  MARK_AS_OVER_ANNOTATED (characterized cofactor is NADH).
- GO:0042802, GO:0051289, GO:0032991 KEEP_AS_NON_CORE (homotetramer).
- GO:1902777 (IEA, IEP) ACCEPT: the SLA -> DHPS step is part of SQ catabolism in
  E. coli; following the module, not refined to GO:0061722, whose definition ends in DHAP
  and pyruvate formation, which this step does not contribute to.
