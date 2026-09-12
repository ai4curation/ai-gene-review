# lnuA notes

## 2026-06-13 AMR GO-gap review

Selected because this is a high-value zero-GOA case where UniProt/CARD and old biochemical literature point to a missing GO molecular function. The UniProt entry is historically named `linA`, while CARD labels the ARO determinant `lnuA`; the review uses `lnuA` as the project symbol and records `linA` as an alias [file:genes/STAHA/lnuA/lnuA-uniprot.txt]. The original linA sequence paper supports the phenotype: linA confers resistance to lincomycin by inactivating it in S. haemolyticus [PMID:3091456]. The follow-up biochemical paper identifies lincosaminide O-nucleotidyltransferases and reports lincomycin 3-(5'-adenylate) and clindamycin 4-(5'-adenylate) products [PMID:2846528].

The AMR mapping file records `ARO:3000221` as a GO gap because GO lacks a lincosamide O-nucleotidyltransferase molecular-function term [file:projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml]. The review proposes that term and uses only broad `GO:0016740` transferase activity as an interim MF.
