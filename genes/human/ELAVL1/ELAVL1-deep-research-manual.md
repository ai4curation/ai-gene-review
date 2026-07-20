# Manual literature synthesis for human ELAVL1 (Q15717)

## Why this file exists

The configured Falcon deep-research request returned HTTP 402, and its Perplexity-lite fallback returned HTTP 401. This manual synthesis was therefore prepared from the reviewed UniProtKB record, the seeded GOA table, the 28 locally cached cited publications, and current QuickGO term definitions. It is not a substitute provider output and is intentionally named deep-research-manual.

## Best-supported functional model

ELAVL1/HuR is a ubiquitously expressed, three-RRM, nucleocytoplasmic shuttling RNA-binding protein. Its defining molecular activity is recognition of AU- and U-rich elements in mRNA 3-prime UTRs. Bound HuR commonly protects transcripts from decay and can promote their translation or oppose miRNA-mediated repression. These effects allow rapid, stimulus-dependent post-transcriptional control of many stress-response, inflammatory, proliferative, and differentiation transcripts.

The core evidence is convergent:

- Recombinant HuR binds c-fos and IL3 AU-rich elements, with all three AU motifs needed for maximal binding (PMID:8626503).
- HuR directly stabilizes an ARE-bearing RNA in vitro and endogenous uPA/uPAR transcripts in human cells; depletion reduces their abundance, and MK2-dependent cytoplasmic accumulation correlates with stabilization (PMID:14517288).
- Structural and fluorescence-polarization studies show that RRM1 is the primary ARE-binding domain and that RRM2/linker contacts increase affinity (PMID:23519412).
- HuR competes with KSRP at an iNOS 3-prime-UTR ARE, providing a direct mechanistic example of stabilization through occupancy of a decay-regulatory element (PMID:16126846).
- HuR binds the PDCD4 3-prime UTR and protects it from miR-21-dependent silencing; ERK8 phosphorylation prevents HuR binding and permits miR-21-mediated decay (PMID:26595526).

## Spatial and regulatory mechanism

HuR is detected in nucleus/nucleoplasm and cytoplasm/cytosol. Its regulated export is functionally important because stabilization of many mature target mRNAs occurs after cytoplasmic accumulation. MAPKAPK2 and PRKCD phosphorylation are linked to cytoplasmic redistribution in direct human-cell studies (PMID:14517288; PMID:18285462). P-body and stress-granule localization are real but conditional; nucleolar staining and broad ribonucleoprotein-complex membership are compatible with an RNA-binding protein but do not independently define its core activity.

HuR homodimerization before RNA binding is supported by inhibitor-based mechanistic experiments (PMID:17632515). Many additional proteins are recovered with HuR, but generic protein binding is not informative enough to treat as a core molecular function. GO:0140517 protein-RNA adaptor activity is mechanistically plausible and phylogenetically supported because HuR binds RNA and helps coordinate proteins at target transcripts, while individual partner claims remain source-specific.

## Context-dependent biological outputs

ELAVL1 affects many processes by changing the fate of particular transcripts. Examples include Th2 differentiation through GATA3 and cytokine messages (PMID:21613615), endothelial stress responses through VASH1 (PMID:23056314), tumor-associated m5C-marked messages through YBX1 recruitment (PMID:31358969), and protection of PDCD4 from miR-21 silencing (PMID:26595526). Orthology-propagated terms for autophagy, glucose response, proliferation, superoxide production, and stem-cell maintenance are therefore credible as downstream contexts but should not displace AU-rich mRNA regulation as the core function.

## Curation conclusions

The highest-specificity supported molecular function is GO:0035925 mRNA 3-prime-UTR AU-rich region binding. GO:0070935 3-prime-UTR-mediated mRNA stabilization is the primary biological process. Nuclear and cytoplasmic compartments are both functional locations because HuR shuttles between them. Generic protein-binding annotations are over-annotations; generic RNA-binding terms should be replaced by the specific ARE-binding term. Endoplasmic-reticulum membership is unsupported by the reviewed protein architecture and localization evidence. The double-stranded-RNA-binding annotation remains unresolved because the available full text of its cited paper does not expose the ELAVL1-specific assay.
