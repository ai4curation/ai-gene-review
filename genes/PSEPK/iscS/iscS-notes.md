# iscS curation notes

## Target selection

PP_0842/Q88PK8 is the relay-relevant IscS paralog. The module-level
OpenScientist analysis reports 72.5% identity to *E. coli* IscS, the
IscS-specific IPR010240 signature, and placement in the canonical
`iscS-iscU-iscA-hscB` locus; PP_2435 lacks that specific signature and locus
context. [file:projects/P_PUTIDA/deep-research/PSEPK__bacterial-mnma-trna-wobble-uridine-thiolation-sulfur-relay__ppu04122-deep-research-openscientist.md
"only PP_0842 carries the IscS-specific InterPro **IPR010240
(Cys_deSase_IscS)**"]

## Functional boundary

IscS is a multi-branch cysteine desulfurase, not a tRNA-specific enzyme. The
review therefore retains both tRNA wobble-uridine thiolation and [2Fe-2S]
cluster assembly as core processes, while the reusable MnmA module includes
only the Tus-relay branch. The cluster-binding annotation is valid but non-core:
the local feature table records a transient [2Fe-2S] ligand shared with IscU.
[file:PSEPK/iscS/iscS-uniprot.txt "ligand shared with IscU"]

The ordered relay assignment is transferred from the reconstituted *E. coli*
system, where IscS directly transfers persulfide sulfur to TusA; no direct
KT2440 reconstitution was identified. [PMID:16387657 "IscS transfers the
persulfide sulfur to TusA."]
