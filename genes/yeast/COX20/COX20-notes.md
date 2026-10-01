# COX20 curation notes

## 2026-10-01 current GOA refresh

- Re-fetched COX20, preserving the old `GO:0051082 unfolded protein binding` row as retired after the 2026 GOA feed replaced it with SGD's direct `GO:0044183 protein folding chaperone` IDA row from PMID:10671482.
- Re-read cached PMID:10671482 and PMID:31752220. The cached PMID:10671482 record is abstract-only, but the abstract itself directly states inner-membrane localization, Cox20 binding to newly synthesized pCox2, and the membrane-bound chaperone role that supports `GO:0044183`, `GO:0033617`, and `GO:0005743`. PMID:31752220 supports COX20-dependent reductions in programmed-cell-death markers under oxidative stress, but that phenotype remains secondary to Cox20's Cox2/chaperone role rather than a separate conserved core function.
- Checked the local PTHR31586 PAINT snapshot. Both live IBA rows are placed on `PANTHER:PTN001269069` and seeded by budding-yeast COX20 plus human COX20 descendant evidence. The yeast self-seed is valid descendant evidence for PAINT, not a circularity problem.
- Reclassified generic `GO:0005739 mitochondrion` rows as non-core because Cox20's experimentally supported core location is the mitochondrial inner membrane.
- Web/PubMed searches for exact yeast COX20/Cox20/YDR231C mentions in 2024-2026 did not find a newer direct *S. cerevisiae* COX20 primary paper that changed the GO review.
