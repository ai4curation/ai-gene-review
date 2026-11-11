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

## 2026-10-15 re-review after OpenScientist TreeGrafter control batch

- Blinded run [file:PSEPK/PP_3571/PP_3571-hypotheses/function-hypothesis-go-0008777/openscientist.md,
  "The identity gradient says the specific-substrate call belongs on PP_5186."]
  verdict: partially supported / too general with paralog confusion.
- Reproduced locally (Biopython global NW/BLOSUM62, gap -10/-0.5): E. coli ArgE
  P23908 active site/Zn ligands H80 D82 D112 E144 E145 E169 H355 map to PP_3571
  H77 D79 D109 E141 E142 E169 H363 (all conserved). Identity over aligned columns:
  PP_5186 vs P23908 50.3%; PP_3571 vs P23908 37.3%, vs PP_1525 DapE 36.3%,
  vs PP_5186 34.1%, vs Q8P8J5 34.1%, vs P0AED7 DapE 32.4%.
- PP_5186 is genes/PSEPK/argE (Q88CJ5, PANTHER SF1) [file:PSEPK/argE/argE-uniprot.txt,
  "PTHR43808:SF1; ACETYLORNITHINE DEACETYLASE"].
- Not adopted: the run's SF31 => N-acetylcitrulline deacetylase lead. In the local
  PTHR43808 member snapshot ~380 SF31 members are named succinyl-diaminopimelate
  desuccinylase (including KT2440 DapE Q88MP5); Q8P8J5 is the only reason for the label.
- Lead only: cyclic ArgJ pathway argument (PMID:42765862, PMID:1339419 not cached).
- Decision: GO:0008777 UNDECIDED -> MODIFY to GO:0016811; core function set on GO:0016811.
