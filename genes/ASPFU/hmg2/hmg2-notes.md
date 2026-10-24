# ASPFU hmg2 notes

## 2026-10-24

### Setup and literature search

- Fetched `ASPFU/hmg2` with `just fetch-gene ASPFU hmg2`, seeding 10 GOA
  rows for UniProt Q4WSY2 / AFUA_1G11230.
- `just fetch-gene-pmids ASPFU hmg2` found no GOA-cited PMIDs, because all
  current rows are GO_REF-backed IBA/IEA annotations.
- Attempted Falcon deep research with Perplexity Lite fallback:
  `just deep-research-falcon ASPFU hmg2 --fallback perplexity-lite`.
  Both providers failed because no usable deep-research API credentials were
  available (`OPENAI_API_KEY`, `EDISON_API_KEY`, `ASTA_API_KEY`, or
  `PERPLEXITY_API_KEY`).
- Cached the UniProt-cited HMG-CoA reductase background papers,
  `PMID:16110826` and `PMID:22106303`; both were available as abstract-only
  records in this branch.
- A web/PubMed sweep for `Aspergillus fumigatus hmg2 HMG-CoA reductase`,
  `AFUA_1G11230`, and azole-resistance papers found and cached the full-text
  hmg2-specific paper:
  [PMID:34641518 "this study, the gene hmg1, recently related to azole resistance, and its paralogue hmg2 were studied in a collection of fifteen azole-resistant strains without cyp51A modifications"].

### HMG-CoA reductase / PAINT context

- `hmg2` is in PANTHER `PTHR10572:SF24`, the same subfamily as `hmg1`,
  yeast HMG1/HMG2, and fission-yeast hmg1.
- Current PAINT places conserved class I HMG-CoA reductase activity,
  isoprenoid biosynthesis, and sterol biosynthesis at `PTN000060346`.
- Current PAINT places two compartments at `PTN000060347`: the well-supported
  ER membrane term `GO:0005789` and a deeper peroxisomal membrane term
  `GO:0005778` whose sole seed is human HMGCR (`UniProtKB:P04035`).
- Current PAINT places fungal ergosterol biosynthesis at `PTN000832055`; hmg2
  is a descendant of this fungal node.
- The broad InterPro-derived `GO:0015936 coenzyme A metabolic process` and
  `GO:0016616 oxidoreductase activity, acting on the CH-OH group of donors,
  NAD or NADP as acceptor` rows mirror `hmg1` and the yeast/PomBase
  HMG-CoA reductase reviews: they are generic parent or by-product mappings
  rather than new hmg2-specific roles.

### Aspergillus-specific biology

- UniProt curates Hmg2 as the second A. fumigatus HMG-CoA reductase in the
  early mevalonate module: "Hmg1 and hmg2 catalyze the reduction of
  hydroxymethylglutaryl-CoA (HMG-CoA) to mevalonate".
- Gonzalez-Jimenez et al. studied hmg2 explicitly in the context of
  cyp51A-independent azole resistance and reported that both hmg1 and hmg2
  encode HMG-CoA reductases involved in ergosterol biosynthesis
  [PMID:34641518 "Both genes encode HMG-CoA reductases and are involved in the ergosterol biosynthesis"].
- The same paper found several Hmg2 sterol-sensing-domain substitutions in
  clinical isolates, but hmg2 is much more weakly expressed than hmg1 and the
  resistance contribution of these variants remained uncertain
  [PMID:34641518 "The gene hmg2 in the wild-type strain shows very low levels of expression in basal conditions or stimulated with the presence of VCZ"].
