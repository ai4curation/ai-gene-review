# topo6 notes

- The GOA file is header-only, so there are no existing GOA annotations to review or convert into NEW rows.
- UniProt identifies topo6 as a Topoisomerase VI fragment and notes homodimerization [file:MISSI/topo6/topo6-uniprot.txt "SubName: Full=Topoisomerase VI"] [file:MISSI/topo6/topo6-uniprot.txt "SUBUNIT: Homodimer"].
- The PANTHER family assigns this entry to DNA topoisomerase 6 subunit B and includes reviewed plant TOP6B members [file:MISSI/topo6/topo6-uniprot.txt "PANTHER; PTHR48444:SF1; DNA TOPOISOMERASE 6 SUBUNIT B"] [file:interpro/panther/PTHR48444/PTHR48444-entries.csv "Q6H442,DNA topoisomerase 6 subunit B"].
- I used contributes_to for type II DNA topoisomerase activity because the entry appears to be a short subunit B fragment rather than the complete topoisomerase complex.
- Because the Miscanthus entry is only a 78 amino acid predicted fragment (PE:4), the GO:0003918 and GO:0009330 core-function calls rest on PANTHER family membership and should be revisited if a full-length gene model changes the assignment.
