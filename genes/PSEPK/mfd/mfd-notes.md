# mfd curation notes

## 2026-08-08 pathway pass

The Q88KZ1 HAMAP record says that Mfd recognizes lesion-stalled RNA polymerase,
mediates its ATP-dependent release, and recruits nucleotide-excision-repair
machinery [file:PSEPK/mfd/mfd-uniprot.txt, "recruitment of nucleotide excision
repair machinery to the damaged"]. Direct E. coli structural work independently
shows stalled-RNAP removal and UvrABC recruitment [PMID:33480355,
"Mfd mediates TCR in bacteria by removing the stalled RNAP concealing the lesion
and recruiting Uvr(A)BC."].

Mfd is a duplex-DNA translocase, not a DNA-unwinding helicase. GO:0003678 was
therefore changed to GO:0015616. The PANTHER family also contains RecG-like
proteins, so module selection additionally requires InterPro IPR004576.
