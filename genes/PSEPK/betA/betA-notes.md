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

Source: Belda et al., 2016, PMID:26913973, DOI:10.1111/1462-2920.13230.

- The cached record is abstract-only and does not expose a checkable betIBA
  reaction passage. An earlier working note quoted an inaccessible full-text
  sentence; that sentence is no longer used as annotation support.
- The cached abstract of PMID:17116241 directly states that `"the betBA genes
  were required for choline"` transformation and osmoprotection. This
  organism-specific genetic evidence supports pathway membership without
  assigning an unsupported substrate to BetT-I.

### Family context

The bifunctional BetA statement is experimentally established for some
bacterial BetA proteins, including reviewed *E. coli* BetA (UniProt P17444),
where the dedicated BetB protein P17445 also occurs, and a characterized
*Halomonas* BetA. Co-occurrence of BetB therefore does not argue against BetA
bifunctionality. No accessible source directly assays both reactions for
Q88CW6, so the automated family-level assignment remains unresolved for the
KT2440 protein.

## Curation conclusions

- Accept choline dehydrogenase activity, FAD binding, membrane association, and glycine-betaine biosynthesis.
- Leave GO:0008802 on BetA UNDECIDED because the EC/HAMAP-derived IEA lacks a Q88CW6-specific biochemical assay.
- Do not remove the second activity: absence of an accessible KT2440 assay is insufficient to disprove possible BetA bifunctionality.
