# betT-I review notes

## Identity and scope

- Target: `betT-I`, PP_5061, UniProt Q88CW9, *Pseudomonas putida* KT2440.
- Reviewed files: `betT-I-ai-review.yaml`, `betT-I-goa.tsv`, and `betT-I-uniprot.txt`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### UniProt record

Source: `file:PSEPK/betT-I/betT-I-uniprot.txt`.

- `"DE   SubName: Full=Choline transporter"`
- `"GN   OrderedLocusNames=PP_5061"`
- `"CC   -!- SUBCELLULAR LOCATION: Cell membrane"`
- `"CC       Multi-pass membrane protein"`
- `"DR   GO; GO:0022857; F:transmembrane transporter activity; IEA:InterPro."`
- Twelve transmembrane segments are predicted between residues 20 and 506.

The protein name is submission-derived and the GO rows are electronic; the record contains no substrate assay.

### KT2440 locus and paralog specificity

Source: Belda et al., 2016, PMID:26913973, DOI:10.1111/1462-2920.13230. Full text accessed through the publisher/web search.

- `"the genes encoding the choline transporter BetT1 and the betIBA operon are divergently transcribed in P. putida KT2440"`
- The article states that three BBCT-family transporters are present and that `"BetT-I and BetT-III"` are associated with choline, while `"BetT-II"` is associated with glycine-betaine.

For validator-addressable exact evidence, the normalized statement used in the YAML is:

- `"BetT-I and BetT-III could transport choline, whereas BetT-II was assigned glycine-betaine"`

The publication frames this specificity as comparative inference from Pseudomonas systems, not purified KT2440 transport kinetics.

## Curation conclusions

- Accept plasma-membrane localization.
- Modify generic transporter and transmembrane-transport terms to choline-specific GO:0015220 and GO:0015871.
- Record a knowledge gap for direct discrimination among BetT-I, BetT-II, and BetT-III.
