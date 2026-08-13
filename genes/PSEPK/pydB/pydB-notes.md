# pydB review notes

## Identity and scope

- Target: `pydB`, PP_4036, UniProt A0A140FWK2, *Pseudomonas putida* KT2440.
- Reviewed files: `pydB-ai-review.yaml`, `pydB-goa.tsv`, and `pydB-uniprot.txt`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### UniProt record

Source: `file:PSEPK/pydB/pydB-uniprot.txt`.

- `"DE   RecName: Full=D-hydantoinase/dihydropyrimidinase"`
- `"DE            EC=3.5.2.2"`
- `"CC   -!- FUNCTION: Catalyzes the hydrolysis of dihydropyrimidines and of the"`
- `"CC       Reaction=5,6-dihydrouracil + H2O = 3-(carbamoylamino)propanoate + H(+);"`
- `"CC       Note=Binds 2 Zn(2+) ions per subunit."`
- `"DR   GO; GO:0004157; F:dihydropyrimidinase activity; IEA:UniProtKB-EC."`

All functional statements in this record are electronic rule/family assignments, but the reaction, EC number, zinc ligands, and family architecture are mutually consistent.

### KT2440 pathway evidence

Source: Hidese et al., 2012, PMID:22782928, DOI:10.1093/jb/mvs079. Abstract retrieved from NCBI E-utilities.

- `"The pathway is controlled by three enzymes: dihydropyrimidine dehydrogenase (DPD), dihydropyrimidinase and beta-alanine synthase."`

PydB lies adjacent to pydX/pydA and has the matching dihydropyrimidinase family/EC assignment, supporting its placement as the second pathway enzyme. The accessible abstract does not describe a purified KT2440 PydB assay.

## Curation conclusions

- Accept GO:0004157 and pyrimidine-containing compound catabolism as core.
- Retain cytosol as the most precise seeded localization.
- Keep reaction-class parents as non-core and mark only the generic hydrolase root as over-annotated.
