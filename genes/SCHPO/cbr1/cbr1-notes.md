# SCHPO cbr1 Notes

## 2026-10-10

- Seeded `SCHPO/cbr1` from GOA and reviewed all 16 current rows against the
  `PTHR19370` PAINT cache.
- The S. pombe protein `O74557`, ORF `SPCC970.03`, is in
  `PTHR19370:SF184`, the CBR1-like NADH-cytochrome b5 reductase subfamily.
- GOA currently has one IBA row: broad `GO:0016491 oxidoreductase activity`
  propagated from `PANTHER:PTN001833551`. The ancestral node is biologically
  sound for cbr1, but the term is less informative than the
  NADH-specific cytochrome-b5 reductase activity on the same protein, so the
  row was modified to `GO:0090524`.
- The `GO:0003954 NADH dehydrogenase activity`, `GO:0004128
  cytochrome-b5 reductase activity, acting on NAD(P)H`, and `GO:0016653
  oxidoreductase activity, acting on NAD(P)H, heme protein as acceptor`
  transfers are correct at the family level but too broad, so they were also
  redirected to `GO:0090524`.
- The existing `GO:0006696 ergosterol biosynthetic process` ISO row was kept:
  CBR1-like NADH-cytochrome b5 reductase activity supplies electrons to
  cytochrome-b5-dependent fungal sterol biosynthetic enzymes.
- The Dph3-dependent process rows, `GO:0002926 tRNA wobble base
  5-methoxycarbonylmethyl-2-thiouridinylation` and `GO:0017183 protein
  histidyl modification to diphthamide`, were accepted by orthology to
  S. cerevisiae Cbr1. GO has no molecular-function term for the direct
  NADH-dependent Dph3 reductase reaction `RHEA:71231`, so the review proposes
  an `NADH-dependent Dph3 reductase activity` term.
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
