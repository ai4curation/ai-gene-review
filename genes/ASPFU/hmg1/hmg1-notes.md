# ASPFU hmg1 notes

## 2026-10-24

### Setup and literature search

- Fetched `ASPFU/hmg1` with `just fetch-gene ASPFU hmg1`, seeding 11 GOA rows for UniProt Q4WHZ1 / AFUA_2G03700.
- Attempted Falcon deep research with Perplexity Lite fallback:
  `just deep-research-falcon ASPFU hmg1 --fallback perplexity-lite`.
  Both providers failed because no usable deep-research API credentials were available
  (`OPENAI_API_KEY`, `EDISON_API_KEY`, `ASTA_API_KEY`, or `PERPLEXITY_API_KEY`).
- Cached the GOA-cited full-text paper:
  [PMID:22106303 "reduced TAFC biosynthesis following lovastatin-mediated Hmg1 inhibition, and increased TAFC biosynthesis following Hmg1 overexpression"].
- Web/PubMed sweep for `Aspergillus fumigatus hmg1 HMG-CoA reductase`,
  `AFUA_2G03700`, and recent triazole-resistance literature found two additional
  full-text papers and a 2026 preprint.
- Cached the clinical sterol-sensing-domain resistance paper:
  [PMID:30226177 "We found mutations in hmg1 and erg6, encoding enzymes Hmg1 and Erg6, respectively, which are involved in ergosterol biosynthesis"].
- Cached the 2026 directed-evolution paper:
  [PMID:41778915 "Reintroduction of the novel mutations in hmg1, abcC, ptaB, and erg25B into wild-type A. fumigatus and correction of the srbA mutation in the evolved strain validated their contribution toward triazole resistance"].
- The web sweep also found the 2026 bioRxiv preprint "Triazole Stress Induces
  Accelerated Degradation of Aspergillus fumigatus Hmg1"; this was left as
  background only because it is a preprint and not needed to adjudicate the
  current GOA assertions.

### HMG-CoA reductase / PAINT context

- `hmg1` is in PANTHER `PTHR10572:SF24`, the same subfamily as yeast HMG1/HMG2
  and fission-yeast hmg1.
- Current PAINT places conserved class I HMG-CoA reductase activity at
  `PTN000060346`: `GO:0004420`, `GO:0008299`, and `GO:0016126`.
- Current PAINT places two compartments at `PTN000060347`: the well-supported
  ER membrane term `GO:0005789` and a deeper peroxisomal membrane term
  `GO:0005778` whose sole seed is human HMGCR (`UniProtKB:P04035`).
- Current PAINT places fungal ergosterol biosynthesis at `PTN000832055` from
  the yeast HMG2 seed; hmg1 is a descendant of this fungal node and the
  biological process is sound for Aspergillus.
- The broad InterPro-derived `GO:0015936 coenzyme A metabolic process` and
  `GO:0016616 oxidoreductase activity, acting on the CH-OH group of donors,
  NAD or NADP as acceptor` rows mirror the yeast and PomBase HMG-CoA reductase
  reviews: they describe generic parents or by-products rather than new core
  functions.

### Aspergillus-specific biology

- Yasmin et al. directly link Hmg1 to mevalonate supply for both ergosterol
  biosynthesis and the mevalonate-derived TAFC siderophore branch. HMG-CoA
  reductase inhibition by lovastatin reduced TAFC output, while `hmg1`
  overexpression increased TAFC production, lovastatin resistance, and
  ergosterol content [PMID:22106303 "To assess directly the involvement of Hmg1 in TAFC production, we tried to delete the hmg1 gene. However, these efforts remained futile, most likely because of the essentiality of this gene"].
- `GO:1900551 N',N'',N'''-triacetylfusarinine C biosynthetic process` is a real
  downstream effect of mevalonate supply, but Hmg1 does not catalyze a dedicated
  TAFC step. It should be kept as non-core, not elevated to a primary siderophore
  biosynthetic enzyme role.
- Hagiwara et al. and Handelman et al. show that Hmg1 sterol-sensing-domain
  mutations can contribute to triazole resistance by perturbing ergosterol
  regulation [PMID:30226177 "All mutations of hmg1 found in this study are present in SSD, suggesting that mutations in SSD are important for conferring azole resistance"].
  These papers support Hmg1's centrality in sterol homeostasis and feedback
  regulation, but they do not add a separate GO molecular function beyond the
  reductase activity.
