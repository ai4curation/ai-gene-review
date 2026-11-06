# opgG curation notes

## 2026-11-06 evidence review

All 9 pristine seeded rows were reviewed. Raw UniProt/GOA and original annotation payloads are protected by the root seed-state and independent review baseline. Default Falcon was attempted once for this gene and returned HTTP 403 authentication failure; no provider report was fabricated. Manual primary-source review supplied the judgments. PAINT lineage checks found no IRD/IKR.

PMID:37735577 methods use BL21(DE3) genomic templates CAQ31569.1 and CAQ31910.2, signal-sequence deletion and C-terminal His6. Exact precursor comparison shows 100% identity to frozen K-12 P33136 (511 aa) and P40120 (551 aa). Intrinsic chemistry is transferable across this identity bridge; native physiological assays are not thereby K-12 experiments. See opgG-source-analysis/sequence-bridge.md for reproducible accession/hash and precursor-numbering evidence.

OpgD has substantial specific beta-1,2 hydrolysis (kcat 29 s^-1; Km 8.6 mg/mL; Table 1), while OpgG shows 0.11 U/mg and 0.79% OpgD activity at 8 mg/mL substrate. The paper explicitly leaves a cofactor requirement and beta-1,6 transfer hypothesis open. This is not evidence of generic GH186 interchangeability or absence of intrinsic OpgG catalysis. Native chain trimming is supported by biochemical/genetic synthesis for OpgD, not a direct assay of native branched intermediates.

OpgG core records OPG-system participation with unresolved native chemistry, without using binding as a placeholder core or forcing a physiological hydrolase/branching reaction. Added the specific measured intrinsic GO:0033913 MF with explicit low-activity and native-role limits: substrate selectivity and catalytic-pocket evidence support an intrinsic activity rather than a noise-level unrelated reaction, but this does not prove physiological primacy. The hydrolysis term is not a core requirement. Existing biosynthetic assertions are refined or retained, not added from knockout-only necessity. PMID:15313617 branching remains a structural hypothesis.

No NEW biological process was proposed. No speculative biofilm, motility, pathogenicity or general stress process was added from downstream phenotypes. Abstract-only experimental localization rows are retained where independent target evidence establishes the location; absent accessible peptide tables are not treated as negative evidence.


## 2026-11-06 PR2142 follow-up

Applied projects/ENZYME_SPECIFICITY.md to the inherited GO:0033913 proposal. The roughly 127-fold E. coli activity difference, dedicated OpgD comparator and absence of a hydrolysis-specific native phenotype warrant residual-activity caution; they do not alone establish promiscuous noise given substrate selectivity, retained catalytic residues and the ligand-bound pocket in PMID:37735577. The proposal is retained with evolved physiological function unresolved and outside the core. No cofactor-dependent enhancement is treated as observed. For KT2440, ISS transfers predicted capability only, not the donor rate or physiological role. All inherited NEW payloads and actions remain unchanged.
