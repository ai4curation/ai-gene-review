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

HyuC is PP_4034 near pydB (PP_4036), pydX (PP_4037), and pydA
(PP_4038), with PP_4035 between hyuC and pydB. This proximity makes Q88FQ3 a
candidate for the terminal beta-alanine-synthase step, but it does not resolve
substrate specificity.

### Family and paralog alternatives

Sources:

- `file:genes/PSEPK/hyuC/hyuC-uniprot.txt`
- `file:interpro/panther/PTHR32494/PTHR32494-entries.csv`
- `file:projects/P_PUTIDA/batches/ppu00410_reductive_pyrimidine_degradation.md`

- Q88FQ3 is assigned to `PTHR32494:SF5 ALLANTOATE AMIDOHYDROLASE` and
  `IPR010158 Amidase_Cbmase`.
- The local PTHR32494 exemplar export contains no characterized
  beta-ureidopropionase. Its SF5 examples include the allantoate enzymes PucF
  (O32149) and AllC (P77425).
- Three entries named `hyuC` in the export, Q01264, Q6DTN4, and Q9F464, are
  annotated as N-carbamoyl-L-amino-acid amidohydrolases, introducing a third
  substrate hypothesis related to hydantoin utilization.
- The same PSEPK pathway bucket contains PP_0614 (Q88Q81),
  `"N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 1"`,
  with the same EC 3.5.1.6/3.5.3.9 pair. It is an alternative candidate for
  the terminal pyrimidine-catabolic reaction.
- GO:0016813 is the EC 3.5.3.- linear-amidine branch associated with
  allantoate hydrolysis. Beta-ureidopropionase EC 3.5.1.6 instead lies under
  GO:0016811, the linear-amide branch.

## Curation conclusions

- Leave beta-ureidopropionase, allantoate deiminase, and the
  linear-amidine class UNDECIDED pending substrate-specific biochemistry.
- Accept generic hydrolase activity and add GO:0016810 as the common
  nonpeptide C-N hydrolase class supported across the alternatives.
- Do not assign Q88FQ3 to pyrimidine catabolism as a new GO process in this
  first pass; compare it directly with PP_0614.
