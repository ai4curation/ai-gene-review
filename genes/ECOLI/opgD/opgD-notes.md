# opgD curation notes

## 2026-11-06 evidence review

All 11 pristine seeded rows were reviewed. Raw UniProt/GOA and original annotation payloads are protected by the root seed-state and independent review baseline. Default Falcon was attempted once for this gene and returned HTTP 403 authentication failure; no provider report was fabricated. Manual primary-source review supplied the judgments. PAINT lineage checks found no IRD/IKR.

PMID:37735577 methods use BL21(DE3) genomic templates CAQ31569.1 and CAQ31910.2, signal-sequence deletion and C-terminal His6. Exact precursor comparison shows 100% identity to frozen K-12 P33136 (511 aa) and P40120 (551 aa). Intrinsic chemistry is transferable across this identity bridge; native physiological assays are not thereby K-12 experiments. See opgG-source-analysis/sequence-bridge.md for reproducible accession/hash and precursor-numbering evidence.

OpgD has substantial specific beta-1,2 hydrolysis (kcat 29 s^-1; Km 8.6 mg/mL; Table 1), while OpgG shows 0.11 U/mg and 0.79% OpgD activity at 8 mg/mL substrate. The paper explicitly leaves a cofactor requirement and beta-1,6 transfer hypothesis open. This is not evidence of generic GH186 interchangeability or absence of intrinsic OpgG catalysis. Native chain trimming is supported by biochemical/genetic synthesis for OpgD, not a direct assay of native branched intermediates.

Added only the missing specific MF GO:0033913, supported by product analysis, substrate selectivity and the sequence bridge. No NEW process term: broad existing biosynthesis rows already cover the OPG maturation role. A glucan hydrolase can participate in biosynthetic product processing without itself polymerizing glucan. OpgD loss changes products rather than abolishing all synthesis (PMID:15175282).

No NEW biological process was proposed. No speculative biofilm, motility, pathogenicity or general stress process was added from downstream phenotypes. Abstract-only experimental localization rows are retained where independent target evidence establishes the location; absent accessible peptide tables are not treated as negative evidence.
