# PRMT2 curation notes

Deep research status: Perplexity was unavailable in this lane and `claude-code` was not authenticated, so no generated `PRMT2-deep-research-*` file was created. These notes summarize the fetched UniProt record, GOA rows, PTHR11006 PAINT rows and accessible primary-paper text.

## Core biology

PRMT2 is a type-I PRMT-domain protein with an N-terminal SH3 domain. PMID:19405910 supports real PRMT2 type-I activity on histone H4 in vitro, and the review keeps broad protein-arginine and asymmetric arginine methyltransferase rows. That same paper reports that the PRMT2 H4 `kcat` is 800-fold lower than PRMT1, so PRMT2 histone rows are treated as over-annotations rather than as the core PRMT2 function.

PRMT2 is better supported as a transcriptional coregulator than as a major histone enzyme. PMID:12039952 identified PRMT2 as an ERalpha-binding coactivator and found that it can coactivate PR, PPARG and RARA transcriptional responses. PMID:17587566 supports AR-dependent PRMT2 coactivation and ligand-dependent PRMT2 nuclear colocalization with AR.

## Boundary decisions

The obsolete nuclear estrogen, androgen, progesterone, retinoic-acid and thyroid receptor binding rows were modified to the current broader `GO:0005102` signaling receptor binding. The receptor-specific papers support PRMT2 binding to ligand-activated nuclear receptors, but not the obsolete term ids.

NF-kappaB inhibition is kept as a non-core branch. PMID:16648481 reported that PRMT2 inhibits NF-kappaB-dependent transcription through increased nuclear IkappaB-alpha and reduced NF-kappaB DNA binding; the newer PRMT2IP paper keeps the same PRMT2-I-kappaB axis in a human microglial model. Generic protein-binding rows were removed under the project policy.

## PANTHER

The family review keeps the PRMT-domain enzyme-class node as sound but records the root histone/chromatin node PTN008510054 as too broad. PRMT2's weak in vitro H4 activity does not justify propagating a core histone methyltransferase assertion from the whole type-I PRMT family.
