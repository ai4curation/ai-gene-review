# SCHPO cbr1 Notes

## 2026-10-10

- Seeded `SCHPO/cbr1` from GOA and reviewed all 16 current rows against the
  `PTHR19370` PAINT cache.
- The S. pombe protein `O74557`, ORF `SPCC970.03`, is in
  `PTHR19370:SF184`, the CBR1-like NADH-cytochrome b5 reductase subfamily.
- GOA currently has one IBA row: broad `GO:0016491 oxidoreductase activity`
  propagated from `PANTHER:PTN001833551`. The family-root node is correctly
  generic because `PTHR19370` includes plant nitrate reductases and
  CoQ6/CYC2-like branches as well as CBR1-like reductases; the specific
  `GO:0004128` PAINT nodes are on deeper eukaryotic and Saccharomycetales
  branches that do not propagate the term to S. pombe cbr1. The existing IBA
  was therefore treated as true but non-core/generic and modified to
  `GO:0090524` for this CBR1-like protein.
- The `GO:0003954 NADH dehydrogenase activity`, `GO:0004128
  cytochrome-b5 reductase activity, acting on NAD(P)H`, and `GO:0016653
  oxidoreductase activity, acting on NAD(P)H, heme protein as acceptor`
  transfers are correct at the family level but too broad, so they were also
  redirected to `GO:0090524`.
- The existing `GO:0006696 ergosterol biosynthetic process` ISO row was kept as
  non-core. PMID:10622712 supports an alternative CYP51 electron-transfer cycle
  in vitro with Candida albicans CYP51 and S. cerevisiae b5/b5R proteins rather
  than a direct S. pombe cbr1 sterol-biosynthesis role, so the row remains a
  plausible curator transfer but was not promoted to `core_functions`.
- The Dph3-dependent process rows, `GO:0002926 tRNA wobble base
  5-methoxycarbonylmethyl-2-thiouridinylation` and `GO:0017183 protein
  histidyl modification to diphthamide`, were accepted by orthology to
  S. cerevisiae Cbr1. GO has no molecular-function term for the direct
  NADH-dependent Dph3 reductase reaction `RHEA:71231`, so the review proposes
  an `NADH-dependent Dph3 reductase activity` term.
- `O13809`/`SPAC17H9.12c` is a second S. pombe member of
  `PTHR19370:SF184`. Because S. cerevisiae Dph3 reduction is shared among Cbr1,
  Mcr1, and Ncp1, this uncharacterized same-subfamily paralog should be tested
  before treating fission-yeast cbr1 as the sole physiological Dph3 reductase.
- The RIKEN S. pombe ORFeome/YFP resource records ER localization for
  `SPCC970.03`, matching the ER/mitochondrial-outer-membrane pattern reported
  for S. cerevisiae Cbr1. The ORF-specific table is not in the cached
  PMID:16823372 abstract, so ER was recorded as a suggested question rather
  than a new supported annotation.
- `just deep-research-falcon SCHPO cbr1 --fallback perplexity-lite` could not
  run to completion because no deep-research provider API keys were available.
  Manual web searches for `O74557`, `SPCC970.03`, `cbr1`,
  `Schizosaccharomyces pombe cytochrome b5 reductase`, and
  `Schizosaccharomyces pombe cbr1 Dph3` found product records, the RIKEN clone
  and localization pages, a 2006 anaerobic-expression survey that listed
  `SPCC970.03`, and a 2017 Dph3/Elp3 S. pombe stress paper, but no newer
  direct S. pombe Cbr1 biochemical paper that would override the S. cerevisiae
  orthology-based review.
