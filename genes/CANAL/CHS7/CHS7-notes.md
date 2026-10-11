# CANAL CHS7 notes

## 2026-10-11

### Setup

- Ran `UV_FROZEN=1 just fetch-gene CANAL CHS7`, which seeded 13 GOA rows for
  `Q5AA40`.
- Ran `UV_FROZEN=1 just fetch-gene-pmids CANAL CHS7`; the only PMID in the
  seeded review was already cached.
- Tried `UV_FROZEN=1 just deep-research-falcon CANAL CHS7 --fallback
  perplexity-lite`, but both providers failed because `agentapi` and provider
  API keys are unavailable. This file is the manual research record.
- Fetched `PMID:17559412` after targeted web search for newer *Candida* CHS7
  papers. That 2007 promoter-heterozygosity paper is abstract-only in the local
  cache, as is the 2005 CGD/GOA reference.

### Direct Candida literature

- `PMID:16079341` is the direct CGD paper for *Candida albicans* CHS7. The
  cached abstract says that "most chitin synthesis in Candida albicans, one of
  the fungi most commonly isolated from opportunistic mycoses and infections,
  depends on CHS7" and that "C. albicans chs7Delta null mutants showed reduced
  levels of chitin and CS activity, and were resistant to Calcofluor." It also
  reports that "CaChs7p was unable to restore CSIII activity in a Saccharomyces
  cerevisiae chs7Delta null mutant, because it was unable to direct ScChs3p
  export from the endoplasmic reticulum", confirming conserved biology but
  species-specific client recognition.
- The same abstract supports the broad morphogenesis phenotype but is more
  equivocal on narrow negative-regulation terms: "C. albicans chs7Delta null
  mutants did not show any defect in growth rate, but yeast cells displayed
  minor morphogenetic defects affecting septum formation, and showed an
  increased tendency to form filaments"; "CaChs7p was not required for
  germ-tube emission, and null mutant strains underwent the dimorphic transition
  correctly"; and "chs7Delta hyphae were very curved and had irregular lateral
  walls, resulting in very compact colonies that seemed unable to spread out
  radially on the surface".
- `PMID:17559412` follows up CHS7 expression rather than defining a new CHS7
  activity. It describes "natural heterozygosity in the promoter of the CaCHS7
  gene in the SC5314 strain" and says the "presence of this region in the
  promoter (L allele) significantly reduced the transcription of the gene as
  compared with its absence (S allele)." Phenotypically, "The HeteroL strain
  showed reduced levels of chitin, a partial resistance to calcofluor, and a
  moderate degree of morphogenetic alterations in hypha-inducing media."

### PAINT and ortholog context

- The PTHR35329 PAINT file places four assertions on the compact fungal CHS7
  ancestor `PANTHER:PTN002175570`: `GO:0005789 endoplasmic reticulum membrane`,
  `GO:0044183 protein folding chaperone`, `GO:0006031 chitin biosynthetic
  process`, and `GO:0006457 protein folding`.
- The `chitin biosynthetic process` IBA is seeded by both CGD `CAL0000175393`
  and SGD `S000001184`; CHS7 therefore being present in the IBA WITH/FROM list
  is expected self-seeding of the PTN node, not circularity.
- The complete `yeast/CHS7` review accepts the same PAINT node as a
  client-specific ER membrane chaperone/escort for Chs3 and updates the stale
  `GO:0051082` unfolded-protein binding rows to `GO:0044183 protein folding
  chaperone`. Current PAINT now asserts `GO:0044183` directly at
  `PTN002175570`, so a new Candida annotation to `GO:0044183` by IBA is justified
  from the current family node even though the current GOA feed lacks it.
- `gocams/index.tsv` has no cached GO-CAM rows for `Q5AA40`, CGD
  `CAL0000175393`, or the Candida `CHS7` symbol.

### Curation decisions

- Accept the IBA rows from `PTN002175570` for ER membrane, chitin biosynthesis,
  and protein folding; the exact same fungal ancestor now carries
  `GO:0044183 protein folding chaperone`, which should be proposed as `NEW`.
- Accept the UniProt subcellular-location IEA to ER membrane; it matches the
  PAINT localization, the UniProt curated ER-membrane comment, and the conserved
  CHS7-family client-export function.
- Accept the direct IMP row for `GO:0006031 chitin biosynthetic process` because
  the cached abstract directly reports lowered chitin and chitin synthase
  activity in `chs7Delta`.
- Keep the direct `GO:0030447 filamentous growth` and `GO:0044182 filamentous
  growth of a population of unicellular organisms` rows as non-core morphology
  phenotypes. The cached abstract supports altered hyphal colony growth and
  wall morphology but does not make them CHS7's direct function.
- The direct negative-regulation row for filamentous growth of a population is
  supported as a non-core phenotype by the abstract's statement that
  `chs7Delta` cells had "an increased tendency to form filaments" and formed
  compact colonies that did not spread normally.
- The flocculation and negative-regulation-of-flocculation rows are plausible
  CGD full-text curation from `PMID:16079341`, but the abstract-only cache is not
  enough to verify the flocculation assay or sign. Mark them `UNDECIDED` rather
  than second-guessing CGD.
- `GO:0000128 flocculation` itself is a broad observed mutant phenotype from
  the same abstract-only paper. It is peripheral to Chs7's ER chaperone/export
  role but should be kept as non-core rather than rejected.
- `GO:0006888 endoplasmic reticulum to Golgi vesicle-mediated transport` by ISS
  to SGD CHS7 fits the orthologous export-chaperone role, so accept it. The
  broader `GO:0051223 regulation of protein transport` ISS row should be
  modified to the same ER-to-Golgi term.
- The seeded `GO:0003674 molecular_function` ND row is superseded by the
  current family-level `GO:0044183` assertion and should be removed.
