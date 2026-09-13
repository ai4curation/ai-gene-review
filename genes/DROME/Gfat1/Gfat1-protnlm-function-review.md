# Gfat1 ProtNLM2 function-description review

## Original prediction

> Catalyzes the first step in hexosamine metabolism, converting fructose-6P into glucosamine-6P using glutamine as a nitrogen source

Original wording and all model/source metadata are retained in [Gfat1-protnlm-source.json](Gfat1-protnlm-source.json).

## Assessment

**NPI for the complete glutamine-dependent catalytic reaction.** The model assigns conversion of fructose-6-phosphate using glutamine as nitrogen donor to Gfat1-PF. The exact target is a native 434-residue isoform matching the C-terminal region of full-length Gfat1, and lacks the catalytic cysteine and most of the glutaminase module. The retained SIS region cannot itself extract nitrogen from glutamine. This is an isoform-scope error, not proof of a wrong input sequence or absence of every possible regulatory/sugar-binding function.

The [reproducible alignment](Gfat1-bioinformatics/RESULTS.md) maps the missing domain. [PMID:16339762](https://pubmed.ncbi.nlm.nih.gov/16339762/) establishes the coupled glutaminase/synthase mechanism; [PMID:19059404](https://pubmed.ncbi.nlm.nih.gov/19059404/) demonstrates ligand-bound isolated human isomerase domains and supports retention of binding without assuming the full reaction. Bacterial donor Q8KG38 and model score 0.96 are preserved in the original source JSON.
