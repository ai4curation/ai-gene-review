# ybbO (STM0505, Q7CR11) — Salmonella Typhimurium LT2 — curation notes

## 2026-10-30 session

- Deep research: `just deep-research-falcon SALTY ybbO --fallback perplexity-lite` failed
  (neither falcon nor perplexity providers are configured in this environment). Literature
  search was done manually (PubMed eutils, QuickGO).
- No Salmonella-specific literature on STM0505 was found. All functional evidence comes
  from the E. coli orthologue YbbO (P0AFP4), 90.6% identical
  (file:SALTY/ybbO/ybbO-bioinformatics/RESULTS.md).
- E. coli YbbO evidence:
  - [PMID:25108218 "YbbO showed broad substrate activity toward all the C2–C10 aldehydes
    with the highest activity toward hexanal and octanal"]; NADPH-dependent, about 10-fold
    lower activity than DkgA and YahK.
  - [PMID:27134112 "deletion of ybbO gene, which encodes NADP(+) dependent aldehyde
    reductase, led to >90% reduction in long chain fatty alcohol production"] and
    "YbbO has wide substrate specificity ranging from C6 to C18 aldehyde".
  - EcoCyc annotates P0AFP4 with GO:0008106 alcohol dehydrogenase (NADP+) activity (IDA)
    from both papers.
- Both studies are metabolic-engineering screens with non-physiological aldehyde loads;
  the natural substrate and physiological role (detoxification of endogenous aldehydes?)
  are unknown.
- PANTHER: PTHR43313 (SDR family 9C), subfamily SF1. The IBA node PTN000672121 is seeded
  by the vertebrate 17beta-HSD / retinol dehydrogenase SDR9C members plus E. coli YbbO, so
  the shared claim is only generic oxidoreductase activity; substrate specificity differs
  across the clade.
- Fitness data could not be fetched (no FEBA source reachable).

## Decision

- GO:0016491 oxidoreductase activity (IBA): correct but general; MODIFY to GO:0008106
  alcohol dehydrogenase (NADP+) activity, supported by orthology to E. coli YbbO.
