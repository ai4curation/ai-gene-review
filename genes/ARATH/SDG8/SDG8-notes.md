# SDG8 notes

## 2026-11-24

Automated deep research was attempted with Falcon and Perplexity Lite but neither provider was available in the shared runtime; the manual replacement is in `SDG8-deep-research-manual.md`.

The initial `fetch-gene` call produced an empty GOA table for SDG8 even though UniProt listed several TAIR/GO annotations. A later retry succeeded and seeded 26 QuickGO rows; the review now adjudicates the standing nucleus, chromatin, broad methyltransferase, H3K4 methyltransferase, H3K36 NOT, protein-binding, reproductive-development, carotenoid, immune and nitrate-response assertions, and proposes H3K36 dimethyltransferase, H3K36 trimethyltransferase and broad histone reader annotations as `NEW`.

GO-CAM consistency notes for the final shared PR:

- The SDG8 `GO:0140955 histone H3K36 trimethyltransferase activity` node is supported and should stay.
- The SDG8 chromatin location is supported by mutant ChIP data at AP1, AtDMC1, MYB99, LAZ5, RPM1 and brassinosteroid-responsive genes.
- The model's SDG7-to-SDG8 order is plausible as one H3K36me2-to-H3K36me3 route, but the strict direct edge over-specifies SDG7 biochemistry. SDG8 is required for global H3K36me2 as well as H3K36me3 in the 2008 bulk assay, while SDG7 is currently implicated by the residual H3K36 methylation left in sdg8.
- `GO:0140673 transcription elongation-coupled chromatin remodeling` over-imports the animal/yeast Eaf3 role into this Arabidopsis model; the paper supports MRG-mediated recruitment of HAM1/HAM2 to raise H4 acetylation at flowering-gene loci, not a generic Pol II passage-coupled chromatin restoration cycle.
