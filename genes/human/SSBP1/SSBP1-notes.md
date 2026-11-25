# SSBP1 notes

SSBP1 is the only reviewed human member of PTHR10302. PANTHER places it in
PTHR10302:SF0, the mitochondrial SSB branch, while the family as a whole mixes
bacterial SSB, mitochondrial SSB, and plant OSB proteins. The existing family
review already captures the main non-human issue: the Eukaryota node supporting
mitochondrial nucleoid and positive regulation of mitochondrial DNA replication
also reaches two chloroplastic OSB branches that should be pruned.

The human review keeps the PAINT ssDNA-binding, nucleoid, DNA-replication and
positive-mtDNA-replication rows for SSBP1. The experimental literature directly
supports this branch: purified TWNK is stimulated by mitochondrial SSBP1
([PMID:12975372]), a minimal POLG/TWNK/mtSSB replisome requires mtSSB to make
full-length mtDNA-sized products ([PMID:15167897]), and human or Drosophila mtSSB
organizes the ssDNA template for POLG ([PMID:26446790]). Metazoan-specific SSBP1
surface variants separate the POLG and helicase-stimulation outputs while
largely preserving ssDNA binding ([PMID:21953457]), which makes the generic
GO:0008047 enzyme activator IBA acceptable for human even though its root PAINT
placement remains unresolved for the full bacterial/plant/mitochondrial family.

The Reactome mitochondrial matrix TAS rows were spot-checked against live
Reactome participants on 2026-11-23 without refreshing the existing cached
Reactome files. All ten events that GOA maps to SSBP1 still list UniProtKB:Q04837
as a participant. The CLPXP/LONP1 rows should be read only as matrix-location
support, not as evidence that SSBP1 executes mitochondrial protein degradation.

No production GO-CAM in gocams/index.tsv uses UniProtKB:Q04837. There is a
Drosophila module, modules/dmel_mitochondrial_dna_replisome.yaml, that captures
the analogous PolG1/PolG2/mtDNA-helicase/mtSSB replisome, but adding a human
POLG/POLG2/TWNK/SSBP1 module would expand beyond this one-family content PR.
