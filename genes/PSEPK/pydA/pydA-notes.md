# pydA review notes

## Identity and scope

- Target: `pydA`, PP_4038, UniProt Q88FQ0, *Pseudomonas putida* KT2440.
- Reviewed files: `pydA-ai-review.yaml`, `pydA-goa.tsv`, and `pydA-uniprot.txt`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### UniProt record

Source: `file:PSEPK/pydA/pydA-uniprot.txt`.

- `"DE   RecName: Full=dihydrouracil dehydrogenase (NAD(+))"`
- `"GN   OrderedLocusNames=PP_4038"`
- `"CC   -!- FUNCTION: Involved in pyrimidine base degradation. Catalyzes"`
- `"DR   GO; GO:0004159; F:dihydropyrimidine dehydrogenase (NAD+) activity; IEA:UniProtKB-EC."`

The UniProt function text is electronically inferred. It supports the reaction assignment but is not direct KT2440 biochemical evidence.

### KT2440 pathway genetics

Source: Hidese et al., 2012, PMID:22782928, DOI:10.1093/jb/mvs079. Abstract retrieved from NCBI E-utilities.

- `"The putative DPD genes, pydX and pydA, are tandemly arranged in the Pseudomonas putida genome."`
- `"a pydA strain of P. putida fails to grow on a minimal media containing uracil or thymine as a sole nitrogen source"`
- `"demonstrating the physiological importance of DPD in the reductive pathway."`

This is direct organism-specific genetic evidence for the pydXA DPD locus and its physiological pathway role. The abstract does not report purified PydA alone; therefore the individual-subunit GO qualifier should be interpreted as contribution to the assembled heteromer.

### Heteromeric enzyme context

Source: Hidese et al., 2011, PMID:21169495, DOI:10.1128/JB.01178-10. Abstract cached at `publications/PMID_21169495.md`.

- `"E. coli dihydropyrimidine dehydrogenase is the first member of a novel NADH-dependent subclass of iron-sulfur flavoenzymes"`

The abstract establishes the family-level NADH-dependent heterotetrameric
iron-sulfur-flavoenzyme architecture. It does not name the P. putida proteins,
so the Q88FQ1/Q88FQ0 pairing is instead grounded in the KT2440 locus evidence
and the two records' complementary domain architectures.

## Curation conclusions

- Accept GO:0004159 at the assembled-enzyme level; `contributes_to` is more precise than `enables` for PydA alone.
- Accept cytoplasmic localization.
- Treat broad oxidoreductase parents as supporting or over-annotated rather than separate core functions.
