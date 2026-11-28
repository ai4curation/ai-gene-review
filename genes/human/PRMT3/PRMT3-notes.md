# PRMT3 curation notes

Deep research status: Perplexity was unavailable in this lane and `claude-code` was not authenticated, so no generated `PRMT3-deep-research-*` file was created. These notes summarize the fetched UniProt record, GOA rows, the PRMT3 Reactome event, PTHR11006 PAINT rows and accessible primary-paper text.

## Core biology

PRMT3 is a cytosolic type-I protein arginine methyltransferase with a zinc-finger substrate-recognition region. The most specific current Reactome event for PRMT3 says that PRMT3 associates with cytosolic ribosomes, whose main in vivo substrate is the small ribosomal subunit protein RPS2, and methylates arginines in the RPS2 RG-rich N-terminal tail to form asymmetric dimethylarginines.

## Boundary decisions

The nuclear histone branch is real but not primary. PMID:39513743 identifies ZNF200 as a PRMT3-binding protein that stabilizes PRMT3, promotes PRMT3 nuclear translocation and increases H4R3me2a, so the H4R3 row is kept as non-core and the nuclear location rows are kept as non-core.

The ALDH1A1 branch is kept as a direct methyltransferase-independent function. PMID:33495566 reports that PRMT3 binds ALDH1A1 and inhibits ALDH1A1 retinal dehydrogenase activity, causing negative regulation of retinoic-acid-responsive gene expression. PMID:25737013 is the PRMT9/SAP145 paper and is only used on a bare RPS2 protein-binding row, so that row is removed under the protein-binding policy without asserting that the paper supports a PRMT3 catalytic function.

## PANTHER

The root PTHR11006 protein-arginine methyltransferase node is sound for PRMT3. The family-wide histone, chromatin and transcription PAINT nodes are broader than the conserved PRMT3 branch: PRMT3 can act in the nucleus with ZNF200, but its central branch is cytosolic RPS2 methylation.
