# CG5565 ProtNLM2 function-description review

## Original prediction

> Catalyzes the dephosphorylation of D,L-glyceraldehyde 3-phosphate in vitro

Original wording and all model/source metadata are retained in [CG5565-protnlm-source.json](CG5565-protnlm-source.json).

## Assessment

**UNC — the stated in vitro D,L-glyceraldehyde 3-phosphate phosphatase activity is unverified.** The exact accession is the native 240-residue CG5565-PA protein. It has an intact HAD-family phosphatase fold, and a curated ortholog transfer from experimentally characterized human PUDP supports pseudouridine 5′-phosphate phosphatase activity. PMID:20722631 establishes strong human PUDP preference for pseudouridine 5′-phosphate while also measuring weaker activity against other phosphate esters.

The prediction uses structural donor Q9V1B3, a Pyrococcus glyceraldehyde-3-phosphate phosphatase, with TM-align scores approximately 0.734/0.739. Its UniProt reaction description is itself transferred by similarity from Q58832. The conserved HAD fold does not establish equivalent substrate preference. No assay of CG5565 with D,L-glyceraldehyde 3-phosphate was found.

The prediction explicitly says “in vitro.” A possible side activity would therefore not be disproved by a different physiological substrate, and no in-vitro-versus-in-vivo error is assigned. An enzyme assay should compare pseudouridine 5′-phosphate with both glyceraldehyde 3-phosphate stereoisomers and include no-enzyme and catalytically inactive controls. [PUDP biochemical study](https://doi.org/10.1042/BJ20100174); [source donor Q9V1B3](https://www.uniprot.org/uniprotkb/Q9V1B3/entry).

[Sequence comparison](CG5565-bioinformatics/RESULTS.md) independently confirms a nearly complete match to human PUDP with both catalytic Asp positions retained. This supports an intact PUDP-like enzyme, while leaving the predicted alternative substrate activity untested.
