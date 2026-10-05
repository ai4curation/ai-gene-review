# GCN5 notes

Falcon deep research supports the existing core interpretation of GCN5 as the catalytic lysine acetyltransferase subunit of yeast SAGA/ADA chromatin coactivator complexes: "Purified recombinant and native Gcn5-containing complexes catalyze acetyl-CoA-dependent histone acetylation, and loss or catalytic mutation of Gcn5 abolishes nucleosomal HAT activity" [file:yeast/GCN5/GCN5-deep-research-falcon.md].

The main substrate-specific evidence remains histone H3 acetylation, with Falcon summarizing that "ADA/Gcn5 acetylates multiple H3 lysines with strong preference for H3K14 and detectable activity on H3K9, K18, K23, K27, and K36" [file:yeast/GCN5/GCN5-deep-research-falcon.md].

Falcon also supports retaining the histone crotonyltransferase annotation as a genuine catalytic activity: "Purified Gcn5-Ada2-Ada3 (ADA) crotonylates histone H3 in vitro at K9, K14, K18, K23, and K27" [file:yeast/GCN5/GCN5-deep-research-falcon.md].

Generic `protein binding`, broad `DNA-templated transcription`, cytoplasmic/mitochondrial localization, and stress-response phenotypes should remain non-core or removed where the current YAML already marks them that way, because Falcon frames the best-supported function as nuclear chromatin coactivation through histone acylation rather than generic interaction or pleiotropic phenotype terms [file:yeast/GCN5/GCN5-deep-research-falcon.md].

## 2026-10-01 current GOA and IBA refresh

`just fetch-gene yeast GCN5 --force` refreshed GCN5 from 69 saved source rows to 82 current GOA rows, adding 21 current assertions and leaving eight old exact-source rows that are now retired in GOA. I preserved those eight rows with `retired: true` rather than deleting them.

All four current GCN5 IBA rows trace to the same PANTHER node, `PANTHER:PTN000720593`, in the cached `interpro/panther/PTHR45750/PTHR45750-paint.tsv` export. The node transfers histone acetyltransferase complex membership, histone H3 acetyltransferase activity, chromatin remodeling, and positive regulation of RNA polymerase II transcription across the conserved eukaryotic GCN5/KAT2 clade; the separate `PANTHER:PTN001111731` ATAC row in the cache is a metazoan node and does not apply to yeast Gcn5.

The refreshed current GOA rows are mostly split/repeated physical-interaction support. I accepted the new `part_of` rows for SAGA, SLIK, and ADA complex membership, and removed the eight new generic `GO:0005515 protein binding` rows because their Hfi1/Ada1 and Ada2 co-complex evidence is better captured by specific complex terms. The new `PMID:31969703` SAGA cryo-EM row is direct support for endogenous yeast SAGA structure, but still only supports complex membership rather than a separable Gcn5 binding activity ["To determine the structure of SAGA, we purified the endogenous complex from Saccharomyces cerevisiae using a strain with a C-terminal TAP-tag on subunit Spt20", PMID:31969703].

The current GOA refresh also materialized broader catalytic rows already supported by yeast literature: `GO:0061733 protein-lysine-acetyltransferase activity` from the 1999 Gcn5 substrate-specificity work and `GO:0140064 peptide crotonyltransferase activity` from the 2019 Gcn5/Esa1 crotonyltransferase study.

I searched for 2024-2026 GCN5/YGR252W/SAGA papers. The only newer direct yeast Gcn5 paper that changed current GOA was Pavon-Verges et al. 2026 on Sus1 and the cell wall integrity pathway. It supports Gcn5 involvement in stress transcription and nucleosome displacement at CWI-dependent promoters but does not change the core function, which remains SAGA/ADA histone acyltransferase activity ["These findings highlight a functional cooperation between Sus1 and Gcn5 in promoting transcriptional activation under stress", PMID:42047951].

PMID:15340070 is Drosophila-centered and locally cached with the abstract only, but UniProt cites its full text for yeast GCN5 sensitivity to genotoxic stress. I therefore kept the `GO:0006974 DNA damage response` IMP row as a non-core phenotype rather than removing it as wrong-organism support.
