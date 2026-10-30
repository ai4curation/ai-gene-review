# CDC8 (P00572) notes

Module: `dntp_de_novo_synthesis`, role = dTMP kinase.

## Evidence journal
- CDC8 = thymidylate kinase [PMID:6088527 "we show, by several biochemical criteria, that thymidylate kinase is the product of the CDC8 gene."; PMID:6091111 "We conclude that CDC8 is the structural gene for dTMP kinase, which catalyzes an essential step in DNA precursor biosynthesis."]
- dUMP is a weaker substrate; not mitochondrial [PMID:6094555 "Kinetic analysis gives a Km of 0.5 mM for dTMP and 2 mM for dUMP."; "Subcellular fractionation indicates that thymidylate kinase is found in the combined nuclear and cytoplasmic fraction but not in the mitochondria."]
- dTDP kinase side activity in vitro [PMID:19540237 "the purified Cdc8 protein possessed thymidylate-specific nucleoside diphosphate kinase activity in addition to thymidylate kinase activity."; "In the direct dTDP phosphorylation, only about 10% of dTDP were converted to dTTP"]

## Annotation decisions
- dTMP kinase, dTDP and dTTP biosynthesis ACCEPT. NDP kinase, dUMP kinase, dUDP biosynthesis KEEP_AS_NON_CORE.
- GO:0047507 (RCA, YeastCyc RXN-14122 with EC 2.7.4.13): MODIFY to GO:0120136 dUMP kinase activity.
- GO:0006207 RCA: REMOVE. Protein binding with NET1 (HT AP-MS): REMOVE.

## YeastCyc
- DTMPKI-RXN lists EC 2.7.4.9 plus 2.7.4.12 and 2.7.4.13; only 2.7.4.9 is the yeast enzyme's assigned activity.
