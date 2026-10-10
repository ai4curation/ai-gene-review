# SCHPO mst1 review notes

## 2026-10-10

- Rebased from `origin/main` in `codex/schpo-mst1-fungal-myst` and seeded the
  review with `UV_FROZEN=1 just fetch-gene SCHPO mst1`.
- `just deep-research-falcon SCHPO mst1 --fallback perplexity-lite` failed
  because neither `agentapi` nor any supported provider API key was available
  in this environment. I did not create a provider-named deep-research file.
- `just fetch-gene` and `just fetch-gene-pmids` cached all eight PMID sources
  already cited by GOA: PMID:10759889, PMID:16199868, PMID:16823372,
  PMID:19040720, PMID:19915592, PMID:20299449, PMID:29192674, and
  PMID:33723569.
- A live literature search for newer fission-yeast `mst1`/`KAT5` papers found
  PMID:38662722, the 2024 PLoS One follow-up on the `mst1-W66R` chromodomain
  allele. I cached it locally because it strengthens, but does not overturn,
  the 2021 conclusion that Mst1 contributes to DSB repair.

## Curation decisions

- The PTHR10615 PAINT rows that transfer from PTN004172926 all fit
  `mst1`: the node is broad, but `mst1` is an ESA1/TIP60-family MYST HAT with
  direct fission-yeast evidence for nuclear chromatin localization and histone
  acetylation.
- The fungal H4 acetyltransferase IBA at PTN000834946 is appropriate for the
  PTHR10615:SF218 ESA1 subfamily. The `mst1` GOA file also has an older
  PomBase ISO from budding-yeast ESA1 for the same H4 activity; the newer PAINT
  assertion is the better propagation, but both support the same conserved
  activity.
- The `Swr1 complex` row from PMID:19040720 is sound in spirit but points at
  the wrong complex for Mst1. The comparative proteomics paper puts Mst1 in the
  fission-yeast NuA4 table, whereas Swr1C shares Arp4/Alp5, Swc4, Yaf9, Act1,
  and other chromatin-environment subunits but not Mst1.
- PMID:20299449 directly supports Mst1-dependent H3K4 acetylation at
  pericentric heterochromatin, so both the H3K4 molecular-function row and the
  positive heterochromatin-formation process row should be retained.
- PMID:33723569 and the newer PMID:38662722 show separable Mst1 contributions
  to single-DSB resection and CPT-induced genome-wide damage repair, so the DSB
  localization and DNA repair-dependent chromatin remodeling rows should be
  retained.
- The acyltransferase extension from PMID:29192674 is weaker than the seeded
  S. pombe EXP/IDA evidence codes imply. That paper tested budding-yeast Esa1
  and human TIP60 for 2-hydroxyisobutyryltransferase activity; it did not test
  S. pombe Mst1. The 2-hydroxyisobutyryltransferase row is plausible by
  conserved MYST chemistry, but the butyryltransferase row is not directly
  supported by the cached paper.
