# PP_3571 curation notes

- UniProt names Q88GZ4 as an acetylornithine deacetylase but the record is
  unreviewed and carries no EC number or catalytic-activity section
  [file:PSEPK/PP_3571/PP_3571-uniprot.txt,
  "SubName: Full=Acetylornithine deacetylase"].
- InterPro `IPR010169` and NCBIfam `TIGR01892` support an ArgE-like enzyme, but
  the PANTHER `PTHR43808:SF31` member set is substrate-heterogeneous. It
  includes the reviewed KT2440 lysine-pathway DapE protein Q88MP5
  [file:interpro/panther/PTHR43808/PTHR43808-entries.csv,
  "Q88MP5,Succinyl-diaminopimelate desuccinylase"].
- The PAINT family file assigns GO:0008777 at an ancestral node seeded by both
  Q8P8J5 and P23908, while the member snapshot identifies Q8P8J5 as an
  N-acetyl-L-citrulline deacetylase. This makes the substrate-specific
  propagation insufficient by itself
  [file:interpro/panther/PTHR43808/PTHR43808-paint.tsv,
  "UniProtKB:Q8P8J5|UniProtKB:P23908"].
- The immediate PP_3565-PP_3577 neighborhood contains transport, quinate,
  porin, regulatory, monooxygenase, and siderophore-system genes rather than a
  recognizable arginine-biosynthesis cluster
  [file:projects/P_PUTIDA/data/psepk_gene_list.tsv, "PP_3571"].
First-pass decision: retain generic hydrolase/deacetylase chemistry as non-core;
leave acetylornithine deacetylase activity and L-arginine biosynthesis
`UNDECIDED` pending direct substrate or genetic evidence.
