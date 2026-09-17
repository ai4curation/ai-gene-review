# pydX review notes

## Identity and scope

- Target: `pydX`, PP_4037, UniProt Q88FQ1, *Pseudomonas putida* KT2440.
- Reviewed files: `pydX-ai-review.yaml`, `pydX-goa.tsv`, and `pydX-uniprot.txt`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### UniProt record

Source: `file:PSEPK/pydX/pydX-uniprot.txt`.

- `"DE   RecName: Full=dihydrouracil dehydrogenase (NAD(+))"`
- `"GN   OrderedLocusNames=PP_4037"`
- `"CC       Name=FMN; Xref=ChEBI:CHEBI:58210;"`
- `"DR   GO; GO:0051536; F:iron-sulfur cluster binding; IEA:InterPro."`

These statements are electronic family/rule inferences, not a purified-protein assay.

### KT2440 pathway evidence

Source: Hidese et al., 2012, PMID:22782928, DOI:10.1093/jb/mvs079. Abstract retrieved from NCBI E-utilities.

- `"The putative DPD genes, pydX and pydA, are tandemly arranged in the Pseudomonas putida genome."`
- `"The pathway is controlled by three enzymes: dihydropyrimidine dehydrogenase (DPD), dihydropyrimidinase and beta-alanine synthase."`

The direct deletion phenotype reported in the abstract is for pydA, not pydX. PydX assignment therefore rests on the tandem paired-enzyme architecture, sequence family, and the bacterial heteromeric DPD classification.

### Heteromeric enzyme context

Source: Hidese et al., 2011, PMID:21169495, DOI:10.1128/JB.01178-10.

- `"E. coli dihydropyrimidine dehydrogenase is the first member of a novel NADH-dependent subclass of iron-sulfur flavoenzymes"`

The cached abstract directly supports the bacterial NADH-dependent
iron-sulfur-flavoenzyme architecture. It does not identify the P. putida
accessions or assign the two subunit roles, so those points are not attributed
to this paper.

### OpenScientist report

Source: `file:PSEPK/pydX/pydX-deep-research-openscientist.md`.

- The report identifies PydX as the PreT-like electron-input subunit and PydA as the pyrimidine-reduction subunit of the heteromeric DPD.
- Its assignment of electron-relay function agrees with the paired-gene evidence and domain architecture.
- The report notes a flavin ambiguity: UniProt assigns FMN to Q88FQ1, whereas characterized electron-input orthologs are expected to carry FAD. The review therefore does not assert a resolved subunit-specific flavin identity.

## Curation conclusions

- Accept DPD activity as a contribution to the assembled PydXA enzyme, with a qualifier caveat.
- Add GO:0003954 NADH dehydrogenase activity for the PydX electron-input half-reaction.
- Accept iron-sulfur cluster binding as an informative subunit-level function.
- Do not elevate generic oxidoreductase activity to core status.
