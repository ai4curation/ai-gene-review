# SDG7 notes

## 2026-11-24

Automated deep research was attempted with Falcon and Perplexity Lite but the shared runtime did not have either provider wired for `deep-research-client`; the failure is summarized in `SDG7-deep-research-manual.md`.

The initial `fetch-gene` call produced an empty GOA table for SDG7. A later retry succeeded and seeded 12 QuickGO rows, including the direct aquaporin Lys3 methyltransferase and endoplasmic-reticulum annotations from PMID:21062871. This review now distinguishes that directly assayed AtPIP2;1/ER activity from the weaker, genetically inferred chromatin H3K36 methyltransferase role used in the GO-CAM.

The model-specific question is whether AT2G44150 can be curated as the SDG7 H3K36me2 writer upstream of SDG8. The GO-CAM source paper reports that the `sdg7 sdg8` double mutant eliminates the H3K36 di- and trimethylation left after loss of SDG8 [PMID:25183522], but this is not a purified-protein assay and does not directly assign the H3K36me1-to-H3K36me2 reaction to SDG7. I therefore proposed a generic H3K36 methyltransferase activity and recorded a GO-CAM disagreement for the exact dimethyltransferase node and strict SDG7-to-SDG8 input edge.
