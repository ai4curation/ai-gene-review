# mak-1 re-review notes

## 2026-11-02 PTHR24055 fungal CWI MAPK review

- `mak-1` encodes the terminal MAP kinase of the *Neurospora crassa*
  MIK-1/MEK-1/MAK-1 cell-wall-integrity signaling cascade. Park et al.
  established the pathway order genetically: MAK-1 phosphorylation is lost in
  `mik-1` and `mek-1` deletion backgrounds, and all three deletion mutants have
  reduced basal hyphal growth, severe asexual-conidiation defects, and female
  sterility [PMID:18849472].
- The PTHR24055 root placements at `PANTHER:PTN000622075` are generic MAPK
  assertions. The serine/threonine kinase, cytoplasm, nucleus, and
  intracellular-signal-transduction rows are broad but fit MAK-1 as an active
  fungal MAPK.
- The fungal `PANTHER:PTN001171896` MAP kinase activity placement is the most
  specific PAINT catalytic assertion. It is safe for MAK-1 because it only
  asserts the shared terminal MAPK catalytic class, not a cell-wall- or
  pheromone-specific process.
- Direct *N. crassa* literature supports a CWI/cell-fusion branch upstream of
  MAK-1. WSC-1 and HAM-7 are genetically upstream sensors whose double mutant
  nearly abolishes MAK-1 activity and recapitulates `mak-1` phenotypes,
  separating WSC-dependent canonical cell-wall signaling from HAM-7-dependent
  cell-to-cell fusion and female development [PMID:22879952].
- The 2012 protoperithecial morphogenesis paper directly complemented
  `mak-1`, `mak-2`, and `os-2` MAPK mutants with GFP-tagged MAPKs. A
  functional MAK-1-sGFP restored vegetative hyphal fusion and protoperithecial
  development to `mak-1`, and MAK-1-GFP signal was enriched in the ascogonial
  coil of developing protoperithecia [PMID:22900028].
- The 2016 micafungin paper is abstract-only in the local cache. Its abstract
  reports that `mak-1` deletion is sensitive to micafungin, that MAK-1
  regulates `ncw-1` and `bgt-2` transcription, and that MAK-1 phosphorylation
  is largely abolished in the `mak-2` mutant but can be induced by micafungin
  [PMID:27268441]. This reinforces CWI crosstalk but should not be used for a
  precise quote beyond the cached abstract.
- MAK-1 and MAK-2 crosstalk recurs in newer work. Lan et al. profiled
  `mak-1` and `mak-2` deletion mutants during protoperithecium formation and
  identified 430 genes co-regulated by the CWI and pheromone-response terminal
  MAPKs; VE-1/VE-2 work in 2024 then connected velvet-complex regulation to
  `mak-1` and `mak-2` promoter binding and to total/phosphorylated MAK-1 and
  MAK-2 abundance [PMID:34899653; PMID:39283084]. These are regulatory
  extensions, not new direct molecular functions for MAK-1.
- `just deep-research-falcon NEUCR mak-1 --fallback perplexity-lite` failed in
  this environment because `agentapi` was not in `PATH` and neither the Falcon
  nor Perplexity provider was available. I used this notes file for manual
  triage instead of creating a provider-named deep-research artifact.
