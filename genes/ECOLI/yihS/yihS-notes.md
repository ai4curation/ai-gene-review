# yihS (P32140) notes

## Session 2026-11-10

Deep research: `just deep-research ECOLI yihQ --provider perplexity` failed in this
environment (deep-research-client dependency unresolvable offline, "All providers
failed"); not retried per gene. Built from UniProt and cached literature:
PMID:24463506 (abstract), PMID:18328504 (abstract), PMID:33791429 (full text),
PMID:41676062 (review, full text).

### Function
- SQ isomerase, first sulfo-EMP step [PMID:24463506 "SQ is catabolised through four
  newly discovered reactions that we established using purified, heterologously
  expressed enzymes: SQ isomerase, ..."].
- kcat/KM for SQ is 4.17 x 10^4 M-1 s-1; 178-fold better than mannose; no activity on
  G6P [PMID:33791429 "SQ is 178-fold better as a substrate for EcYihS (in terms of
  kcat/KM)"].
- Prefers beta-SQ; also forms sulforhamnose (SR), a CsqR derepressor [PMID:33791429].
- Before its physiological substrate was known, YihS was characterised as a
  cofactor-independent aldose-ketose isomerase on mannose/fructose/glucose and
  lyxose/xylulose (KM 108 mM for mannose) [PMID:18328504].
- Homohexamer (crystallographic dimer of trimers; SEC-MALS hexamer of SeYihS)
  [PMID:33791429].
- AGE (N-acylglucosamine 2-epimerase) fold, but no AGE activity [PMID:18328504 "Both
  proteins were found to show no AGE activity"]. PAINT places an IRD (NOT GO:0050121)
  at PTN001431668 (taxon:1224), consistent with this.

### Decisions
- GO:0061593 x4 ACCEPT (core).
- GO:0016853 isomerase activity -> MODIFY GO:0061593.
- GO:0005975 carbohydrate metabolic process -> MODIFY GO:0061722 sulphoglycolysis.
- GO:1902777 (UniRule IEA, IMP) -> MODIFY GO:0061722 sulphoglycolysis (is_a GO:1902777),
  matching the module's process for this annoton. The GO:0061722 definition ends in DHAP
  and pyruvate; YihS catalyses the committing step of the route that yields DHAP.
- GO:0050089 mannose isomerase: real in vitro activity (KM 108 mM) of unclear
  relevance -> MARK_AS_OVER_ANNOTATED (promiscuous-activity tier 2).
- GO:0042802, GO:0034214: hexamer, KEEP_AS_NON_CORE.
