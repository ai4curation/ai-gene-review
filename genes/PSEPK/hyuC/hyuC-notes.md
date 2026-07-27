# hyuC review notes

## Identity and scope

- Target: `hyuC`, PP_4034, UniProt Q88FQ3, *Pseudomonas putida* KT2440.
- Reviewed files: `hyuC-ai-review.yaml`, `hyuC-goa.tsv`, and `hyuC-uniprot.txt`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### UniProt record

Source: `file:PSEPK/hyuC/hyuC-uniprot.txt`.

- `"DE   SubName: Full=N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 2"`
- `"DE            EC=3.5.1.6"`
- `"DE            EC=3.5.3.9"`
- `"CC       Note=Binds 2 Zn(2+) ions per subunit."`
- `"DR   GO; GO:0047652; F:allantoate deiminase activity; IEA:UniProtKB-EC."`
- `"DR   GO; GO:0003837; F:beta-ureidopropionase activity; IEA:UniProtKB-EC."`

The record is unreviewed and the dual substrate assignment is inherited from submitted names and EC mapping. It does not provide a KT2440 substrate assay.

### Pathway context

Source: Hidese et al., 2012, PMID:22782928, DOI:10.1093/jb/mvs079. Abstract retrieved from NCBI E-utilities.

- `"The pathway is controlled by three enzymes: dihydropyrimidine dehydrogenase (DPD), dihydropyrimidinase and beta-alanine synthase."`

HyuC is PP_4034 in the same local locus as pydB (PP_4036), pydX (PP_4037), and pydA (PP_4038). Its N-carbamoyl-beta-alanine amidohydrolase assignment matches the terminal beta-alanine synthase/ureidopropionase step. No accessible source directly tested allantoate turnover by Q88FQ3.

## Curation conclusions

- Accept beta-ureidopropionase as the core physiological activity based on locus and pathway coherence.
- Leave allantoate deiminase UNDECIDED rather than removing it: the family/EC ambiguity cannot be resolved without substrate-specific biochemistry.
- Treat generic hydrolase terms as non-core or over-annotated.
