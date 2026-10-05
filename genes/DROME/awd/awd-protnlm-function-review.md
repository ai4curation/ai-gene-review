# awd ProtNLM2 function-description review

## Original prediction

> Major role in the synthesis of nucleoside triphosphates other than ATP. The ATP gamma phosphate is transferred to the NDP beta phosphate via a ping-pong mechanism, using a phosphorylated active-site intermediate

Original wording and all model/source metadata are retained in [awd-protnlm-source.json](awd-protnlm-source.json).

## Assessment

**CNN: supported, already represented by the NDP-kinase annotation.** The exact target contains the complete 153-residue experimentally characterized awd enzyme with a 15-residue N-terminal extension. Catalytic and binding residues are preserved, supporting the phosphate-transfer mechanism described. Primary purification and mutagenesis studies establish fly awd activity; [sequence analysis](awd-bioinformatics/RESULTS.md) connects those results to the selected product.

[PMID:1320004](https://pubmed.ncbi.nlm.nih.gov/1320004/) describes purified native Drosophila NDP kinase; [PMID:7559441](https://pubmed.ncbi.nlm.nih.gov/7559441/) tests catalytic-site variants. The reviewed same-gene P08879 donor record supplies the established phosphohistidine mechanism. Current FlyBase and UniProt disagree about the N-terminal initiation, documented in the analysis; this does not invalidate the preserved catalytic core.
