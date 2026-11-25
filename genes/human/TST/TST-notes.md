# TST PTHR11364 review notes

## 2026-11-23 family review

Deep-research automation was not available in this checkout: `just deep-research-falcon human TST --fallback perplexity-lite` failed because only the `claude_code` provider was configured. This manual note summarizes the local UniProt, GOA, PAINT, Reactome and cached-literature evidence used for the review.

Human TST is a PTHR11364:SF6 rhodanese and lies below PTN008517019, the IRD node that blocks 3-mercaptopyruvate sulfurtransferase activity and tRNA wobble uridine thiolation. Parsed cached PAINT tree `.cache/panther_trees/19.0/PTHR11364.json.gz`: the human TST leaf Q16762 is PTN002478497 and has PTN008517019 in its ancestry, whereas human MPST does not.

Core sulfur-transfer activity: TST/rhodanese catalyzes thiosulfate-dependent conversion of HCN to thiocyanate. PMID:9070219 cloned the human liver TST cDNA and showed expression in bacteria and COS7 cells increased rhodanese activity; Reactome records the same TST sulfur transfer from thiosulfate to HCN; Zuhra et al. 2025 showed that overexpressing TST increased, and shRNA downregulating TST decreased, HepG2 KCN-degradation capacity and endogenous cyanide clearance.

Mitochondrial location: UniProt records TST as a mitochondrial matrix protein, Reactome places the curated human reaction in the mitochondrial matrix, and Morgenstern et al. 2021 include TST in the high-confidence human mitochondrial proteome.

Moonlighting RNA import role: Smirnov et al. 2010 identified TST/rhodanese as a human 5S rRNA import factor whose misfolded nascent form binds 5S rRNA and whose knockdown proportionally decreases 5S rRNA import into mitochondria. Smirnov et al. 2011 extended this into a conveyor with MRPL18 that redirects cytosolic 5S rRNA to mitochondria. These rows are experimentally real but secondary to the canonical thiosulfate-cyanide sulfurtransferase reaction.

The Caco-2 epithelial-cell differentiation annotation comes from a proteomic comparison of proliferating and differentiated cells; the abstract reports 53 differentially regulated proteins and pathway analysis, not a direct mechanistic role for TST in differentiation.

Cyanate is not cyanide. The TST GO:0009440 cyanate catabolic process rows cite either ARBA:ARBA00092626 or the TST cDNA paper PMID:9070219, and neither source establishes catabolism of OCN- cyanate by TST.

The exact MPST/TST family did not match an existing production GO-CAM or an existing `modules/` review. The human members are a biochemical paralog pair rather than a stable multi-protein module: MPST participates with GOT2/TXN2, MOCS3/NFS1, and URM1/CTU1/CTU2 in broader sulfur-transfer contexts, while TST is the mitochondrial rhodanese that also moonlights with MRPL18 in 5S rRNA import.
