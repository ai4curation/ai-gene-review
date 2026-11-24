# INP51 / SJL1 notes (YIL002C, P40559)

- PI(4,5)P2 5-phosphatase [PMID:9565610 "recombinant Inp51p exhibits intrinsic phosphatidylinositol 4,5-bisphosphate 5-phosphatase activity"]; inp51 cells have elevated PI(4,5)P2 [PMID:9565610 "Cells lacking INP51 have a 2-4-fold increase in levels of phosphatidylinositol 4,5-bisphosphate"]
- Membrane-associated [PMID:9560389 "Inp51p (108 kD), Inp52p (136 kD) and Inp53p (124 kD) are membrane-associated."]; mostly cytoplasmic GFP [PMID:17452534 "Although Sjl1-GFP mostly localized to the cytoplasm"]
- Activated by Tax4/Irs4 [PMID:15265867 "The EPS15 homology domain-containing proteins TAX4 and IRS4 bind and activate the PI(4,5)P 5-phosphatase INP51 via an Asn-Pro-Phe motif in INP51."]
- SAC domain activity reported only for Sac1, Inp52, Inp53 [PMID:10224048 "The 5-phosphatase domains of synaptojanin, Inp52p, and Inp53p are also catalytic"]; UniProt states Inp51 does not use PI(3,5)P2, PI3P or PI4P [UniProt:P40559]. Hence IBA GO:0043813 (PTN000878771) and derived GO:0036092 removed.
- IP3 5-phosphatase IBA (PTN002597976): not tested in yeast; over-annotation.
- 2026-11-24 re-review of the IP3 5-phosphatase IBA (PTN002597976): the line above is out of date. PMID:11094088 (full text) assayed purified Inp52 on Ins(1,4,5)P3 with no hydrolysis and summarises Inp51, Inp52 and Inp53 as specific for PtdIns(4,5)P2 [PMID:11094088 "Each of these enzymes specifically hydrolyzes PtdIns(4,5)P 2 forming PtdIns(4)P."]. No negative assay on Inp51 itself was read, so the row stays MARK_AS_OVER_ANNOTATED.
