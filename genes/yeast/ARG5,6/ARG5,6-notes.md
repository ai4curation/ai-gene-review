# ARG5,6 (YER069W, Q01217) notes

- Single 863-aa precursor processed in mitochondria into acetylglutamate kinase (EC 2.7.2.8, N-terminal) and N-acetyl-gamma-glutamyl-phosphate reductase (EC 1.2.1.38, NADP-dependent) [UniProt:Q01217; PMID:1851947 "the ARG5,6 gene encodes acetylglutamyl-P reductase and acetylglutamate kinase, two arginine anabolic enzymes which are localized in the mitochondria"].
- "ARG5,6 encodes a precursor that is maturated in the mitochondria into acetylglutamate kinase and acetylglutamyl-phosphate reductase" [PMID:11553611].
- NAGS/NAGK metabolon with Arg2; the ascomycete-specific C-terminal domain of NAGK "is required to maintain synthase activity and protein level"; mutual feedback-regulation coupling [PMID:12603335].
- Moonlighting DNA binding/transcription: "Chromatin immunoprecipitation experiments revealed that Arg5,6 is associated with specific nuclear and mitochondrial loci in vivo" and "Deletion of Arg5,6 causes altered transcript levels of both nuclear and mitochondrial target genes." [PMID:15486299] -> KEEP_AS_NON_CORE.
- Mitochondrial proteomics HDA [PMID:16823961, PMID:24769239].

## Curation decisions
- Two core MFs: GO:0003991 (in GO:0106098 complex) and GO:0003942; BP GO:0006526/GO:0006592; CC GO:0005759.
- NEW: part_of GO:0106098 NAGS/NAGK complex (IPI, PMID:11553611) - GOA has it only on ARG2.
- RCA cytosol REMOVE; IEA cytoplasm MODIFY -> mitochondrial matrix; NAD binding over-annotated (NADP enzyme); generic grouping terms MODIFY.
