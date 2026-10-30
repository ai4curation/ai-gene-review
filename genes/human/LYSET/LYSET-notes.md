# LYSET (lysosomal enzyme trafficking factor; TMEM251, GCAF; UniProtKB:Q8N6I4) - review notes

HGNC approved symbol is LYSET (previous symbol TMEM251; alias GCAF; HGNC:20218). The
dismech disease entry "Dysostosis Multiplex, Ain-Naz Type" binds hgnc:20218. Literature
work was done manually from cached publications (no provider deep-research file was
available when the review was written).

## Biology

- LYSET is a small (163 aa) protein with two transmembrane domains that localises to the
  Golgi [PMID:36074821 "LYSET is a small, poorly characterized protein containing two
  transmembrane domains. It co-localizes with GNPTAB in the Golgi apparatus"].
- Three 2022 genome-wide CRISPR screens independently identified it as essential for the
  mannose 6-phosphate (M6P) pathway. LYSET binds GNPTAB (GlcNAc-1-phosphotransferase alpha/beta)
  and keeps it stable, cleaved by site-1 protease, active, and retained in Golgi stacks:
  - [PMID:36074822 "Without LYSET, GlcNAc-1-phosphotransferase was unstable because of a
    hydrophilic transmembrane domain."]
  - [PMID:36074821 "These data support a model in which LYSET interacts with GNPTAB and is
    important for proper localization of GNPTAB in Golgi stacks."]
  - [PMID:36096887 "TMEM251 localizes to the Golgi and is required for the cleavage and
    activity of GNPT, the enzyme that catalyzes M6P modification"].
- Loss of LYSET abolishes M6P tagging globally, causes hypersecretion/missorting of soluble
  lysosomal hydrolases and storage, and mislocalises GNPTAB to lysosomes; Lyset-knockout mice
  and tmem251 zebrafish mutants phenocopy mucolipidosis II.
- LYSET does not itself carry the phosphotransferase activity. There is no GO molecular
  function term for "stabilises a partner enzyme / retains it in the Golgi"; its core role is
  captured with the biological process terms protein stabilization (of GNPTAB) and lysosomal
  transport / protein targeting to lysosome.

## Disease

Biallelic LYSET loss-of-function variants cause dysostosis multiplex, Ain-Naz type (OMIM
619345; also called mucolipidosis type V) [PMID:33252156 "Our work implicates TMEM251 in the
pathogenesis of a novel disorder"].

## Curation decisions

- "protein binding" (GNPTAB) is real but uninformative; removed in favour of process terms.
- "regulation of vesicle-mediated transport" (macropinocytic cargo turnover) is an indirect
  consequence of hydrolase depletion -> over-annotation.
