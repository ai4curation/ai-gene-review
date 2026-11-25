# hsp98 review notes

## 2026-10-05 fungal PAINT-family review

- `NEUCR/hsp98` was reviewed as the filamentous-fungal representative of the
  `PTHR11638` Hsp104 subfamily. The local PANTHER member table places P31540 in
  `PTHR11638:SF18`, the same subfamily as S. cerevisiae HSP104, S. pombe
  hsp104, and C. albicans HSP104.

- Deep-research providers were unavailable in this shell, so the review used a
  live literature search plus the cached 1992 hsp98 primary paper. The 1992
  record is abstract-only; it verifies that Hsp98 is a major N. crassa
  heat-shock protein with homology to E. coli ClpB and S. cerevisiae Hsp104
  [PMID:1472534, "It also has 71% homology to hsp104 of Saccharomyces
  cerevisiae."], but it does not give detailed Hsp98 mutant phenotypes.

- The IBA rows to cytoplasm, ATP hydrolysis, protein refolding, protein
  unfolding, cytosol, protein-folding chaperone binding, and cellular heat
  acclimation are all accepted from the fungal Hsp104 PAINT nodes. The
  `WITH/FROM` source list has only a few MOD descendants because these are PAINT
  node placements, not pairwise transfers; the short donor list is not weak
  evidence.

- The UniProtKB-SubCell nuclear row was left `UNDECIDED`. Nuclear localization
  is plausible by comparison to S. cerevisiae and S. pombe Hsp104, but the
  cached Neurospora paper reports a microsomal/polyribosomal distribution after
  heat shock and does not test nuclear entry.
