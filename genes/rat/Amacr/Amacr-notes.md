# Amacr (rat, P70473) notes

## Re-review 2026-10-04

**GOA changes (refresh in commit a3cf70b6d):**
- Two new ISO rows split by donor identifier: GO:0005739 mitochondrion and GO:0005777 peroxisome, each with WITH/FROM `UniProtKB:Q9UHK6|UniProtKB:Q9UHK6-1` (human AMACR, protein plus canonical isoform). Protein-level siblings already exist.
- No rows retired.

**PENDING resolved:**
- Both rows -> KEEP_AS_NON_CORE, each with its own propagation_review naming the isoform donor. The human enzyme is dual-targeted [PMID:11060344 "The enzyme activity is found not only in peroxisomes but also is present in mitochondria of human liver and fibroblasts."], and rat has direct fractionation data [PMID:11060359 "Subcellular fractionation experiments, however, revealed that both in humans and rats alpha-methylacyl-CoA racemase is bimodally distributed to both the peroxisome and the mitochondrion."; PMID:7649182 "the rat enzyme co-distributed exclusively with mitochondrial marker enzymes"].

**Actions changed:**
- GO:0005102 signaling receptor binding (ISO, human AMACR): MARK_AS_OVER_ANNOTATED -> REMOVE. The only receptor interaction reported for AMACR is PTS1 recognition by the peroxisomal import receptor Pex5p [PMID:11060344 "From the in vitro interaction between recombinant racemase and recombinant human PTS1 receptor (Pex5p) ..."]. Pex5p is a cargo-import receptor, not a signaling receptor in the sense of the GO:0005102 definition. QuickGO (2026-10-04) returns no GO:0005102 annotation for Q9UHK6 or Q9UHK6-1, so the donor appears to have been withdrawn (propagation_review: SOURCE_STALE_OR_MISSING).

**Support strengthened (actions unchanged):** EXP/IDA rows that cited only paper titles now also carry claim-bearing abstract quotes:
- PMID:9106621 (R)-ibuprofenoyl-CoA inversion assay
- PMID:7649182 rat mitochondrial co-distribution
- PMID:11060359 bimodal distribution
- PMID:11964182 racemase step in cholic acid synthesis
- PMID:8020470 trihydroxycoprostanoyl-CoA substrate

**Description:** removed the curation commentary ("The review accepts..."). Added the biology: (2S)-requirement of beta-oxidation, dual targeting, and the ibuprofen epimerase role.

**Open questions:**
- PMID:14561759 (rat liver peroxisome proteomics) supports the peroxisome IDA only through the curator's reading of the full text; the abstract does not name Amacr.
- core_functions lists both GO:0008206 bile acid metabolic process and its descendant GO:0006699 bile acid biosynthetic process. This is redundant but harmless; left as is.
