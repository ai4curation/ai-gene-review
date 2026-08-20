# betB review notes

## Identity and scope

- Target: `betB`, PP_5063, UniProt Q88CW7, *Pseudomonas putida* KT2440.
- Reviewed files: `betB-ai-review.yaml`, `betB-goa.tsv`, and `betB-uniprot.txt`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### Reviewed UniProt record

Source: `file:PSEPK/betB/betB-uniprot.txt`.

- `"DE   RecName: Full=Betaine aldehyde dehydrogenase"`
- `"DE            EC=1.2.1.8"`
- `"CC   -!- FUNCTION: Involved in the biosynthesis of the osmoprotectant glycine"`
- `"CC       betaine. Catalyzes the irreversible oxidation of betaine aldehyde to"`
- `"CC       the corresponding acid."`
- `"CC       Reaction=betaine aldehyde + NAD(+) + H2O = glycine betaine + NADH + 2"`
- `"CC       Note=Binds 2 potassium ions per subunit."`
- `"CC   -!- SUBUNIT: Dimer of dimers."`
- `"DR   GO; GO:0008802; F:betaine-aldehyde dehydrogenase (NAD+) activity; IEA:UniProtKB-UniRule."`

### KT2440 pathway assignment

Source: Belda et al., 2016, PMID:26913973, DOI:10.1111/1462-2920.13230.

- The cached record is abstract-only and does not contain a checkable betIBA
  reaction passage. The inaccessible sentence retained in an earlier working
  note is no longer used as annotation support.
- PMID:17116241 provides checkable KT2440 evidence that `"the betBA genes were
  required for choline"` transformation and osmoprotection.

Source: Zhang et al., 2024, PMCID:PMC11200750. Full text accessed through PMC/web search.

- The abstract reports that `"betB-encoding betaine-aldehyde dehydrogenase was identified"` in KT2440 salt-stress transcriptomics and that overexpression of `betB` improved growth under high salinity.

The overexpression phenotype supports an osmoprotection role but does not replace the reaction-specific UniProt/HAMAP evidence.

## Curation conclusions

- Accept GO:0008802 as BetB's core molecular function and glycine-betaine biosynthesis from choline as its pathway.
- Keep metal ion binding as non-core mechanistic support.
- Mark generic oxidoreductase activity as over-annotated.
