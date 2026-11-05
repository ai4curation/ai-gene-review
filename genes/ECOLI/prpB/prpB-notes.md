# prpB (P77541) - Escherichia coli K-12 2-methylisocitrate lyase

## 2026-10-23 - Initial review

### Setup / provenance
- Files fetched with `just fetch-gene ECOLI prpB` (uniprot, goa, stub review).
- Provider deep research could not be run in this session because provider API
  credentials were unavailable. No `-deep-research-*.md` file was created; the review
  is based on the cached publications and the reviewed UniProt entry.
- All three GOA-cited papers are abstract-only in the cache
  (`full_text_available: false`): PMID:11422389, PMID:12706720, PMID:15723538.

### Evidence
- PrpB is the E. coli 2-methylisocitrate lyase of the prp operon
  [PMID:11422389 "2-Methylisocitrate lyase from E. coli corresponds to the PrpB protein of the prp operon involved in propionate oxidation."].
- Substrate is threo-2-methylisocitrate; erythro is inactive, isocitrate is not cleaved
  [PMID:11422389 "The enzymes show no measurable activity with isocitrate."].
- Homotetramer, ~32 kDa subunits [PMID:11422389 "Both 2-methylisocitrate lyases have a native homotetrameric structure as identified by size-exclusion chromatography."].
- Mg2+-dependent; 1.9 A structure with Mg2+, open active-site loop
  [PMID:12706720 "The enzyme, which strictly depends on Mg(2+) for catalysis, belongs to the isocitrate lyase protein family."].
- C123S structures with Mg2+-pyruvate + succinate and with Mg2+-isocitrate (inhibitor);
  alpha-carboxy-carbanion mechanism; stringent specificity verified in solution
  [PMID:15723538 "We propose a catalytic mechanism involving an alpha-carboxy-carbanion intermediate/transition state"].
  The abstract does not name the organism, but UniProt P77541 cites this paper with
  ECO:0000269 for kinetics, binding sites and the C123S mutant (PDB 1XG4).
- UniProt kinetics [file:ECOLI/prpB/prpB-uniprot.txt "KM=19 uM for threo-2-methylisocitrate"].

### Decisions
- GO:0046421 methylisocitrate lyase activity (IDA x2, IBA, IEA): ACCEPT, core MF.
- GO:0019543 propionate catabolic process (IBA, IEA): ACCEPT; PrpB catalyses the last
  step of the 2-methylcitrate cycle (participation, not mere necessity).
- GO:0000287 magnesium ion binding (IDA x2, IEA): KEEP_AS_NON_CORE (catalytic cofactor).
- GO:0003824 catalytic activity (IEA InterPro2GO): MODIFY -> GO:0046421.
- No NEW annotations proposed. No cytosol annotation exists in GOA; none added.
