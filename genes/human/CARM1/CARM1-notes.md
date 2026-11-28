# CARM1 curation notes

Deep research status: Perplexity was unavailable in this lane and `claude-code` was not authenticated, so no generated `CARM1-deep-research-*` file was created. These notes summarize the fetched UniProt record, GOA rows, Reactome entries, PTHR11006 PAINT rows and accessible primary-paper text.

## Core biology

CARM1/PRMT4 is a type-I protein arginine methyltransferase and transcriptional coactivator. UniProt summarizes the core activity as mono- and asymmetric dimethylation of arginine residues and specifically says CARM1 "methylates histone H3 at 'Arg-17' (H3R17me), forming mainly asymmetric dimethylarginine" (`file:human/CARM1/CARM1-uniprot.txt`, CC:FUNCTION). PMID:15471871 directly supports the FXR/BSEP H3R17 axis: CARM1 occupancy at the BSEP promoter increases with FXR activation, and CARM1 is required for CDCA-induced BSEP mRNA and H3 Arg-17 methylation.

## Boundary decisions

The H3R2 rows are downgraded. The cited CARM1 `IMP` row points to PMID:17898714, which is the PRMT6/H3R2 paper and says PRMT6 catalyzes H3R2 dimethylation and controls global H3R2me2a in vivo. Reactome still records that CARM1 can methylate H3R2 in vitro, so the propagated CARM1 rows are marked over-annotated rather than globally wrong, but Reactome also states that PRMT6 is the major cellular H3R2 methyltransferase.

CARM1's replication-fork role from PMID:33412112 is retained as non-core. The paper found that CARM1 associates with replication forks, promotes PARP1 recruitment and PARylation at forks, slows fork speed and promotes fork reversal independently of CARM1 methyltransferase activity.

The `GO:0045943` positive regulation of transcription by RNA polymerase I row is modified to positive regulation of transcription by RNA polymerase II, because PMID:15471871 assays a bile salt export pump Pol II promoter controlled by FXR. Generic protein-binding rows were removed under the project policy.

## PANTHER

The PTHR11006 family review treats the deep type-I `GO:0016274` protein-arginine N-methyltransferase node as sound. Root `GO:0042054` histone methyltransferase, `GO:0006338` chromatin remodeling and `GO:0006355` regulation of DNA-templated transcription rows are too broad for every type-I PRMT branch, and the H3R2 node is not a robust CARM1 family-level assertion.
