# PP_3206 curation notes

- UniProt Q88HZ6 supplies only an epimerase/dehydratase-fold name
  [file:PSEPK/PP_3206/PP_3206-uniprot.txt "RecName: Full=NAD-dependent
  epimerase/dehydratase domain-containing protein"]. This does not establish an
  epimerase substrate or reaction.
- OpenScientist identifies the KEGG K26183/FdeJ and R13076 assignment but also
  states that the reaction is inferred rather than experimentally demonstrated
  [file:PSEPK/PP_3206/PP_3206-deep-research-openscientist.md "FdeJ's specific
  reaction (oxaloacetate-releasing hydrolysis, KEGG R13076) is therefore a
  pathway/orthology inference"].
- A committed global alignment gives 51.1% identity to Hsero_1012/D8J0X4
  [file:PSEPK/PP_3206/PP_3206-bioinformatics/RESULTS.md "Pairwise identity over
  aligned residue pairs: 51.1%"], not the report's unreproduced 52.4%. Neither
  sequence has direct R13076 evidence.
- Organism-level evidence establishes flavonoid A-ring fission in P. putida
  [PMID:8071218 "Pseudomonas putida degraded quercetin via an initial fission in
  its A-ring"], while the Herbaspirillum pathway produces oxaloacetate after
  meta-cleavage [PMID:27059806 "After meta-cleavage of the A-ring, the subsequent
  metabolic steps generate oxaloacetic acid that is metabolized via the
  tricarboxylic acid cycle."]. Neither paper identifies PP_3206 as the catalyst.
- GO:0016822 and GO:0009812 are therefore provisional ISS annotations. No
  cellular-component term or sugar-epimerase function is asserted.
