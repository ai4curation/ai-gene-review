# ProtNLM function paragraph: dati / Q9V4C9

## Original prediction

> May be involved in transcriptional regulation

[Original prediction JSON](dati-predictions-source.json) preserves the model score 0.25, phmmer accession O43345 and score 1037.9. O43345 is human ZNF208; it is not assumed to be the Dati ortholog.

## Assessment: LSP for the broad qualified regulatory claim

[PMID:25291190](https://pubmed.ncbi.nlm.nih.gov/25291190/) identifies Dati as a nuclear zinc-finger transcription factor related to Rotund/Squeeze and vertebrate ZNF384, with gene-specific neuronal specification phenotypes: “dati encodes a zinc finger transcription factor closely related to rotund (rn) and squeeze (sqz) with homologs in several species, including humans”. This is supported family placement and biological context, strengthened by experimentally characterized DNA binding in Nmp4/ZNF384 ([PMID:11867614](https://pubmed.ncbi.nlm.nih.gov/11867614/)). This exact gene was already identified as a transcription factor in the 2014 primary study, and the curated [dati review](dati-ai-review.yaml) carries GO:0003700 DNA-binding transcription factor activity as its core molecular function. That term is part of GO:0006355 regulation of DNA-templated transcription, so the gene already carries a more specific statement than "may be involved in transcriptional regulation". GOA itself has no equivalent molecular-function or transcription-regulation row. The claim is correct but less precise than the curated annotation; this does not establish whether the paper was in model training.

The paragraph does not specify activation, repression, a DNA motif or a direct target gene. Its broad qualified statement is therefore correct but less specific than the curated annotation, while the separate activating-activity GO claim remains UNC. Q9V4C9 is a complete 1140-residue isoform whose six C2H2 fingers are intact, so no feature required by the claim is missing from this product. No AI-generated description or unrelated ZNF208 functional assertion is used as validation.
