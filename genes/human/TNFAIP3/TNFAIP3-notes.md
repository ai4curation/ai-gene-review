# TNFAIP3 notes

## 2026-11-22 ORGANELLES lysosome batch 2

- One GO:0005764 row: IEA GO_REF:0000044 from the UniProt "Lysosome" location item, which has no evidence tag. Review and GOA agree; no sub-compartment rows.
- PMID:18952128 (Li et al. 2009, BBA; PMCID PMC2657479, DOI 10.1016/j.bbamcr.2008.09.013): full text read in PMC (cache is abstract-only). The authors describe "a lysosome-interacting compartment" and a "perinuclear membrane compartment that interacts dynamically with the lysosomes"; the overlap shown is of overexpressed A20 and TRAF2 in COS7 cells with LysoTracker-stained organelles (LysoTracker was the reagent listed). Endogenous TRAF2 degradation under TNF plus actinomycin D or TWEAK is partly A20-dependent and attenuated by lysosomal inhibitors, in MEFs.
- PMID:18329387 (Li et al. 2008, BBA; PMC2587335, DOI 10.1016/j.bbamcr.2008.01.029): PMC returned no full text; fetched abstract-only into the cache. [PMID:18329387 "a fraction of endogenous and ectopically expressed A20 is localized to an endocytic membrane compartment that is in association with the lysosome"].
- Call: ACCEPT -> MARK_AS_OVER_ANNOTATED; UniProt WRONG_TERM CHECK source defect (SUSPECTED). KEEP_AS_NON_CORE is the close alternative if the 2008 full text shows endogenous A20 with LAMP1 or cathepsin.
- Description sentence on lysosomal localization reworded to the lysosome-associated endocytic compartment.
