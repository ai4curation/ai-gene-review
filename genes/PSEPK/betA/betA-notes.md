# betA review notes

## Identity and scope

- Target: `betA`, PP_5064, UniProt Q88CW6, *Pseudomonas putida* KT2440.
- Reviewed files: `betA-ai-review.yaml`, `betA-goa.tsv`, and `betA-uniprot.txt`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### Reviewed UniProt record

Source: `file:PSEPK/betA/betA-uniprot.txt`.

- `"DE   RecName: Full=Oxygen-dependent choline dehydrogenase"`
- `"DE            EC=1.1.99.1"`
- `"DE   AltName: Full=Betaine aldehyde dehydrogenase"`
- `"DE            EC=1.2.1.8"`
- `"CC   -!- FUNCTION: Involved in the biosynthesis of the osmoprotectant glycine"`
- `"CC       betaine. Catalyzes the oxidation of choline to betaine aldehyde and"`
- `"CC       betaine aldehyde to glycine betaine at the same rate."`
- `"CC       Name=FAD; Xref=ChEBI:CHEBI:57692;"`
- `"DR   GO; GO:0008812; F:choline dehydrogenase activity; IEA:UniProtKB-UniRule."`
- `"DR   GO; GO:0008802; F:betaine-aldehyde dehydrogenase (NAD+) activity; IEA:UniProtKB-EC."`

The entry is reviewed, but both reaction claims are explicitly HAMAP/UniRule inferences rather than organism-specific experiments.

### KT2440 pathway assignment

Source: Belda et al., 2016, PMID:26913973, DOI:10.1111/1462-2920.13230. Full text accessed through the publisher/web search.

- `"the betIBA operon encodes a choline oxidase (BetA) and a betaine aldehyde dehydrogenase (BetB), responsible for the two-step conversion of choline to glycine-betaine"`

This organism-specific reconstruction distinguishes BetA as the first-step choline oxidase/dehydrogenase and BetB as the second-step aldehyde dehydrogenase.

### Family context

The bifunctional BetA statement is experimentally established for some bacterial BetA proteins, including reviewed *E. coli* BetA (UniProt P17444), but no accessible source directly assays both reactions for Q88CW6. Pseudomonad literature generally describes a BetA/BetB enzyme pair.

## Curation conclusions

- Accept choline dehydrogenase activity, FAD binding, membrane association, and glycine-betaine biosynthesis.
- Leave GO:0008802 on BetA UNDECIDED because the automated bifunctional assignment conflicts with the organism-specific two-enzyme pathway description.
- Do not remove the second activity: absence of an accessible KT2440 assay is insufficient to disprove possible BetA bifunctionality.
