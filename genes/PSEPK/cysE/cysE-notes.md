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

## 2026-11-03 completion pass (cysteine biosynthesis module promotion)

- Generic parent rows (catalytic, transferase, O-acetyltransferase activity)
  moved from KEEP_AS_NON_CORE to TOO_GENERAL: the review's own accepted
  reaction-specific MF entails them, so keeping them as "non-core" misdescribed
  the judgement. Actions now match the sibling E. coli and P. aeruginosa
  reviews written for the same module.
- No provider deep-research run was possible in this session (no provider API
  keys); the review rests on the UniProt record, PAINT data for the PANTHER
  family, and the cached Pseudomonas literature already cited.
- Status set to COMPLETE.
- Cytoplasm row changed to MODIFY -> cytosol (GO:0005829): the PTHR42811 PAINT
  node PTN000602332 carries cytosol (IBD), withdrawn only for plant organellar
  SATs (IRD at PTN000602385), and Q88PL0 has no membrane or signal features. The
  record's own SUBCELLULAR LOCATION line is ARBA-derived and no longer cited.


## Comparative cysteine-route audit (2026-11-06)

All four existing decisions retained. Q88PL0 matches the specific serine O-acetyltransferase models; native KT2440 enzymology is not supplied by S-313 cell extracts (PMID10482527) or recombinant PAO1 CysE (PMID42278617). The cytosol refinement remains a phylogenetic/architecture inference, not native fractionation. PAO1 lack of canonical CSC regulation cannot establish absence of interaction in KT2440. No complex membership, virulence process, or activity for the other KT2440 CysE-family paralogs is inferred.

Default Falcon research was attempted normally with --provider falcon and failed with HTTP403. No provider report was fabricated; this section records manual review.

Original GOA payloads, raw UniProt/GOA files and inherited authored proposals are preserved. Current GO checks distinguish the active cysteine synthase MF from obsolete route-specific BP terms GO:0006535 and GO:0019345. Focused gene and helper-history validations are recorded in the audit manifest.
