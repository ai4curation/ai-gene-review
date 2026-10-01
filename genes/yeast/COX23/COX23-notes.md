# COX23 curation notes

## 2026-10-01 current GOA refresh

- Re-fetched COX23 against current GOA/UniProt; the live GOA set remained at 13 rows and the refresh backfilled current supporting entities on the two IBA rows and two UniProt-SubCell rows.
- Re-read cached PMID:15145942, PMID:19703468, PMID:14562095, PMID:22984289, and PMID:28357365. The cached literature continues to support Cox23 as an intermembrane-space complex IV assembly factor whose molecular activity is unknown.
- Fetched the missing PTHR46811 PAINT slice. Both live IBA rows, `GO:0005739 mitochondrion` and `GO:0033108 mitochondrial respiratory chain complex assembly`, are placed at `PANTHER:PTN005321770` and seeded by budding-yeast COX23. The yeast seed is valid descendant evidence, not a circularity problem.
- Kept both IBA rows as non-core: mitochondrial localization is a generic parent of the intermembrane-space rows, and `GO:0033108` is a broad respiratory-chain assembly parent of Cox23's experimentally supported complex IV assembly role.
- Web/PubMed searches for exact yeast COX23/Cox23/YHR116W mentions in 2024-2026 did not find a newer direct *S. cerevisiae* COX23 primary paper that changed the GO review; a 2025 DMO2 paper reports DMO2 overexpression suppression of `cox23` respiratory deficiency, but this is contextual for COX23 rather than a new Cox23 action.
