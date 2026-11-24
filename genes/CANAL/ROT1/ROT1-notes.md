# ROT1 curation notes

## 2026-11 PTHR28090 fungal PAINT review

Fetched the C. albicans `ROT1` GOA and reviewed its three PTHR28090 IBA rows. `GO:0005789 endoplasmic reticulum membrane` and `GO:0006458 'de novo' protein folding` come from `PANTHER:PTN001999053`, the Dikarya Rot1 node. `GO:0007118 budding cell apical bud growth` comes from `PANTHER:PTN001999057`, a Saccharomycetales node also seeded by SGD `ROT1`.

The 2026 C. albicans Rot1 paper [PMID:42042339] supplied the target-specific evidence this review needed: the CTG-corrected Candida gene complements lethal S. cerevisiae `rot1`, and repressing `CaROT1` impairs N-glycosylation, early lipid-linked oligosaccharide synthesis, ER-stress tolerance, cell-wall composition, and filamentation. I accepted the core ER membrane and de novo folding rows, retained the budding-growth IBA as a non-core downstream morphogenesis outcome, and removed only the old CGD ND placeholders.

Newer-paper search: PMID:42042339 was not previously cached and is now the main direct Candida reference.
