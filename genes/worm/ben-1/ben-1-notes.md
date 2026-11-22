# ben-1 notes

## 2026-11-22

- Started the beta-tubulin/benzimidazole lane with `worm/ben-1`, UniProt
  `Q18817`, because BEN-1 is the C. elegans beta-tubulin that Driscoll et al.
  identified as the source of benzimidazole sensitivity and later natural
  diversity work repeatedly resolved as the main Caenorhabditis
  albendazole-resistance beta-tubulin.
- Treated this PR as a gene review rather than a module: a benzimidazole-target
  module would need resolved alpha/beta tubulin heterodimer or microtubule
  parts, but the target specificity is isotype-level, and the parasite side is
  still duplicate-heavy. The simple UniProt HAECO query returns dozens of
  unreviewed unnamed beta-tubulin entries, so the Haemonchus tbb-isotype-1 and
  tbb-isotype-2 representatives need resolution before a parasite ortholog
  review or module part is safe.
- `just mod-description-deep-research worm ben-1` found no curated WormBase
  description. `just deep-research worm ben-1 --provider perplexity` failed
  because Perplexity was unavailable, and `--provider claude-code` failed
  because the deep-research client was not logged in. This review therefore
  used the seeded GOA references, the cached PTHR11588 tubulin family review,
  UniProt, and targeted PubMed searches instead of a provider file.
- The main 1989 Driscoll paper is abstract-only in the local cache despite
  having a PMCID. Its abstract is still enough for the core curation decisions:
  it says molecular cloning and sequence analysis established that `ben-1`
  encodes a beta-tubulin, ben-1 deletions are fully benzimidazole-resistant,
  and animals lacking ben-1 are viable and coordinated.
- Hahnel et al. 2018 mapped natural C. elegans albendazole resistance to many
  low-frequency `ben-1` loss-of-function variants. Collins et al. 2024 used a
  ben-1 loss-of-function allele as a high-resistance control for quantitative
  albendazole testing of beta-tubulin variants. Shaver et al. 2026 extended the
  same logic across Caenorhabditis species and cautioned that high-impact
  missense variants in `ben-1` do not predict albendazole resistance equally
  well in every species.
- The GOA chemosensory and egg-laying behavior rows are phenotype-level IMPs.
  The Driscoll abstract does not mention chemosensation, so the exact basis of
  the chemosensory row remains unresolved. Lacroix et al. used the old TBB-5
  name for the tubulin isoform that WormBase maps to ben-1; current C. elegans
  beta-tubulin literature lists no separate tbb-5 gene. Their TBB-5
  uterine-muscle RNAi experiment supports a ben-1 egg-laying phenotype, but
  BEN-1 performs the structural microtubule work rather than the behavioral
  process itself.
