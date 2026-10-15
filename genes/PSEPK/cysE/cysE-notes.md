# cysE curation notes

## 2026-08-11 first-pass synthesis

- Q88PL0 is the named KT2440 `cysE` product and its exact UniProt record assigns
  the reaction L-serine + acetyl-CoA to O-acetyl-L-serine + CoA
  [UniProtKB:Q88PL0, "Reaction=L-serine + acetyl-CoA = O-acetyl-L-serine + CoA;"].
- GO:0006535 is the live, route-specific process term for cysteine biosynthesis
  from L-serine. The review retains broad GO:0019344 and adds GO:0006535 as the
  more informative authored core process.
- P. putida S-313 has directly measured O-acetylserine sulfhydrylase activity,
  establishing organism-level pathway operation but not the identity of its
  serine acetyltransferase [PMID:10482527, "substantial levels of
  O-acetylserine sulfhydrylase (cysteine synthase) activity."].
- A 2026 study identified PA3816 as the major serine acetyltransferase in
  P. aeruginosa and showed that its deletion causes cysteine auxotrophy
  [PMID:42278617, "PA3816 as the major P. aeruginosa serine acetyltransferase
  (PaCysE), the enzyme"]. This is ortholog-level support, not direct evidence
  for Q88PL0.

## Paralog boundary

PP_0228, PP_1110, and PP_3136 carry electronic serine-acetyltransferase
assignments, but they are not silently treated as equivalent pathway leaves.
Their physiological contribution is retained as a targeted question because
some records have atypical architecture or conflicting process annotations.

## 2026-09-27 correction: GO:0006535 is retired

- The 2026-08-11 entry above calls GO:0006535 (L-cysteine biosynthetic process
  from L-serine) the live route-specific term and says the review adds it as the
  authored core process. That was wrong: GO retired the term (obsolete no later
  than release 2026-03-25, replaced_by GO:0019344). A reviewed label alias in
  conf/oak_config.yaml and stale committed term caches had kept it validating.
  The NEW proposal is removed and the authored core process is GO:0019344; the
  O-acetylserine route is carried by the
  bacterial_cysteine_biosynthesis_via_o_acetylserine module. UniProt's
  `DR GO; GO:0006535` line is a stale cross-reference, not support for a new
  term (PR #3105).
