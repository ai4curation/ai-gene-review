# purT curation notes

- UniProt identifies Q88MW1 as Formate-dependent phosphoribosylglycinamide formyltransferase [file:PSEPK/purT/purT-uniprot.txt "RecName: Full=Formate-dependent phosphoribosylglycinamide formyltransferase"].
- PurT uses formate, ATP, and GAR rather than the folate-bound donor used by PurN
  [PMID:8117714 "catalyzes the production of beta-formyl GAR from formate, ATP, and beta-GAR."].
- Remove `GO:0004644` and `GO:0016742`: they place the EC 6.3.1.21 C-N ligase in
  folate-dependent transferase chemistry. Replace the generic catalytic/process terms
  with `GO:0043815` and `GO:0006189`; retain nucleotide, ATP, magnesium, and metal
  binding as non-core.
- Open question: Under which carbon and folate conditions does PurT rather than PurN provide most GAR transformylase flux?
