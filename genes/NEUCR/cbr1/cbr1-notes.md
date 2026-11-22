# NEUCR cbr1 Notes

## 2026-10-10

- Seeded `NEUCR/cbr1` from GOA and reviewed 16 current rows against the
  `PTHR19370` PAINT cache.
- The N. crassa protein `Q7RXL1`, ORF `NCU00216`, is in
  `PTHR19370:SF184`, the CBR1-like NADH-cytochrome b5 reductase subfamily.
- GOA currently has one IBA row: the very broad `GO:0016491 oxidoreductase
  activity` propagated from `PANTHER:PTN001833551`. The ancestral node is
  biologically sound for cbr1 and deliberately broad because the family root
  spans animal CYB5R enzymes, fungal MCR1/PGA3/CYC2 branches, and plant nitrate
  reductases; it was retained as a non-core parent while the exact
  NADH-specific activity is supplied by the Rhea/EC rows.
- The `GO:0003954 NADH dehydrogenase activity` and `GO:0004128
  cytochrome-b5 reductase activity, acting on NAD(P)H` transfers from
  S. cerevisiae CBR1 are all correct at the family level but too broad, so they
  were also redirected to `GO:0090524`.
- The `GO:0002098 tRNA wobble uridine modification` row is a true ancestor but
  duplicates the more specific `GO:0002926 tRNA wobble base
  5-methoxycarbonylmethyl-2-thiouridinylation` rows, so only the specific term
  was retained as core.
- `GO:0090560 2-(3-amino-3-carboxypropyl)histidine synthase activity` is the
  Dph1-Dph2 radical-SAM activity, not CBR1's reductase activity. CBR1 supplies
  electrons to Dph3, and Dph3 feeds Dph1-Dph2; the row is therefore modified to
  a proposed `NADH-dependent Dph3 reductase activity` term for `RHEA:71231`
  while noting that cbr1 can be a reductase component of the synthase complex.
- The 2016 S. cerevisiae CBR1 paper is a full-text cached paper and supports the
  Dph3 reductase and mcm5s2U wobble-uridine process inferences. The paper's
  in-vivo diphthamide result is conditional: cbr1 deletion did not produce
  diphtheria-toxin resistance at endogenous eEF2 levels, while Cbr1 supported
  Dph1-Dph2 in vitro and became important for diphthamide formation when eEF2
  overexpression raised electron demand. It also reports that S. cerevisiae
  Cbr1 is embedded in ER and mitochondrial outer membranes with a cytosolic
  catalytic domain, supporting the homology-based outer-membrane rows and
  leaving the ER location as a Neurospora question.
- `just deep-research-falcon NEUCR cbr1 --fallback perplexity-lite` could not
  run to completion because no deep-research provider API keys were available.
  Manual web searches for `Q7RXL1`, `NCU00216`, and Neurospora cbr1 found only
  product records plus a 2015 Xanthophyllomyces CBR phylogeny that includes
  N. crassa CBR1 and CBR2; no newer Neurospora-specific paper was found that
  would change the GOA review.
