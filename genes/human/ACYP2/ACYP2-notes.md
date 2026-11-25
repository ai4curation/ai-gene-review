# ACYP2 notes

## GOA and family

- `ACYP2-goa.tsv` has 11 annotation rows, so the QuickGO fetch did not produce a header-only file.
- Human `ACYP1` and `ACYP2` are the only reviewed human members of `PTHR10029`.
- ACYP2 is `PTHR10029:SF20`; ACYP1 is `PTHR10029:SF21`.
- PAINT has one current `PTHR10029` IBD row, placing `GO:0003998` acylphosphatase activity at `PANTHER:PTN000003030`.
- `just paint-losses human ACYP2` found no IRD or IKR loss on the ACYP2 lineage.
- No production GO-CAM in `gocams/index.tsv` references `UniProtKB:P14621`, and the two human acylphosphatases are alternative monomeric enzymes rather than a multi-part biological module.

## Row calls

- The `GO:0003998` rows were accepted. PMID:8268218 synthesized and expressed the human muscle acylphosphatase gene and assayed benzoylphosphate hydrolysis by the recombinant enzymes [PMID:8268218 "using benzoylphosphate as a substrate and phosphate as a competitive inhibitor"].
- PMID:1645713 describes acylphosphatase purified from human erythrocytes in the cached abstract, so it was not treated as ACYP2-specific direct evidence from the abstract alone [PMID:1645713 "Acylphosphatase, purified from human erythrocytes"]. The source defect on that GOA row is a `WRONG_GENE_PRODUCT` query, not a request to repoint the row to PMID:8268218, because PMID:8268218 already supplies a separate ACYP2 IDA row.
- The PMID:25416956 `GO:0005515` rows were removed under the root-protein-binding policy without disputing the high-throughput Y2H interactions with SULT2B1 or CREBZF.
- The two `GO:0042802` rows from PMID:12374855 and PMID:16084386 were marked over-annotated. Those papers deliberately use human muscle acylphosphatase as an amyloid-aggregation model for mutant proteins and do not show native ACYP2 homodimerization as a function [PMID:12374855 "under conditions where the native fold of the protein is substantially disrupted"].
- The high-throughput `GO:0005739` mitochondrion row from MitoCoP was kept as non-core under the root-organelle policy, but the odd FlyBase-assigned human row and the lack of ACYP2 in the cached MitoCoP main text are now recorded for future checking.
- `GO:0006796` is true but too broad and was modified to `GO:0016311` dephosphorylation. QuickGO reported `GO:0016311` as a current biological-process term whose `is_a` ancestors include `GO:0006796`, and PMID:8268218 supports ACYP2 hydrolysis of benzoylphosphate [PMID:8268218 "using benzoylphosphate as a substrate and phosphate as a competitive inhibitor"].

## Literature

- Perplexity deep research was unavailable in this runtime; the wrapper reported `Provider 'perplexity' not available. Available: claude_code`, so I recorded a manual deep-research note instead of inventing a `-deep-research-perplexity.md` file.
- Cardiac sarcoplasmic-reticulum Ca2+-ATPase is a physiological-substrate lead for the muscle/heart isozyme: heart-muscle acylphosphatase at concentrations in the physiological range hydrolyzed the cardiac SR Ca2+ pump phosphoenzyme and increased Ca2+ uptake and ATP hydrolysis [PMID:8702578 "acylphosphatase from heart muscle, used at concentrations within the physiological range, actively hydrolyzes the phosphoenzyme of cardiac sarcoplasmic reticulum Ca2+ pump"]. The review records this as a candidate substrate rather than as a new process annotation, because the ACYP2 gene product is not yet tied to a specific GO biological process in intact human cells.
- Human common-type crystallography notes that acylphosphatases can hydrolyze 1,3-bisphosphoglycerate, carbamoyl phosphate, succinyl phosphate and pump beta-aspartyl-phosphate intermediates, but that the biological role of acylphosphatase remains open [PMID:16511269 "The biological role of acylphosphatase is not fully understood."]. I used that to narrow, not close, the ACYP2 substrate knowledge gap.
