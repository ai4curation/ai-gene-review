# SPR1 review notes

## 2026-10-10

- Seeded the current `yeast/SPR1` review from GOA. The file contains 17
  current rows covering exo-1,3-beta-glucosidase activity, broad InterPro
  hydrolase/process parents, extracellular and cell-wall localization,
  ascospore-wall/prospore-membrane localization, ascospore formation, a SWAT
  vacuole row, and four PTHR31297 PAINT rows.
- Tried the default `falcon` deep-research provider with `perplexity-lite`
  fallback. Both providers failed because no deep-research credentials are
  configured in this environment, so this review used cached GOA publications,
  UniProt, PTHR31297 PAINT data, and manual literature searches instead.
- PTHR31297 places SPR1 in the same `PTHR31297:SF1` clade as EXG1 and Candida
  XOG1. The exact `GO:0004338 glucan exo-1,3-beta-glucosidase activity`
  assertion is on `PTN001262687`, the fungal extracellular and
  fungal-type-cell-wall beta-glucan assertions are on `PTN001262686`, and broad
  `GO:0009251 glucan catabolic process` is inherited from `PTN001262628`, a
  family-root node seeded by Aspergillus SF34/SF39 exgB/exgD-like members.
- GOA already caches the Muthukumar et al. 1993 SPR1 paper and the Larriba et
  al. 1995 exoglucanase review. UniProt additionally cites the San Segundo et
  al. 1993 SSG1 cloning paper, so PMID:8509335 was fetched as corroborating
  evidence for sporulation-specific exo-1,3-beta-glucanase activity.
- Manual PubMed searches for `SPR1`, `SSG1`, `YOR190W`,
  sporulation-specific beta-glucanase, and ascospore thermoresistance found no
  newer paper that changes SPR1's core function. Recent apparent hits either
  delete endogenous yeast glycosidases for natural-product engineering, monitor
  SPR1 expression/protein abundance without assaying its direct activity, or
  use unrelated `SPR1`/`SSG1` aliases in other organisms.
- The 2009 spore-wall permeability paper is direct for Spr1-GFP localization:
  native-promoter Spr1-GFP localized to the forming prospore membrane during
  meiosis and to the spore wall of mature spores. The 2014 high-throughput
  sporulation localization paper reports prospore-membrane localization in its
  supplementary screen; the full-text cache describes the screen and its
  caveats, but does not expose the SPR1 row from Table S1.
