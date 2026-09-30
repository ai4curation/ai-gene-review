# gpi16 (O94380) — evidence and prediction assessment

Gpi16 is the PIG-T-family accessory subunit of the endoplasmic-reticulum GPI-anchor transamidase complex. Its large lumenal domain and C-terminal membrane anchor support assembly and function of the machinery that attaches preformed GPI anchors to proteins. The catalytic cleavage/transamidation chemistry belongs to the Gpi8/PIG-K subunit, rather than to Gpi16 alone.

## Evidence and family boundary

PIG-T/Gpi16 is distinct from the Gpi8/PIG-K catalytic protease. The full 545-aa target has a predicted signal peptide1–22, lumenal domain23–493, membrane helix494–514 and cytosolic tail515–545 in the [curated sequence record](gpi16-uniprot.txt). GPI transamidase membership supports the protein-attachment process; it does not justify an autonomous peptidase or transamidase MF.

[PMID:15003443](https://pubmed.ncbi.nlm.nih.gov/15003443/) is a computational GPI-site predictor paper used by ComplexPortal as a NAS source, not a direct target-complex purification. The annotation is retained as curated orthology/context. Falcon provides useful yeast/mammalian mechanistic synthesis but misses the target HDA ER localization already attributed to PMID:16823372. Its assertion of no target localization should not override that observation. A conserved PIG-T/PIG-K disulfide is not claimed as experimentally measured in pombe.

## External ProtNLM statements

[Exact retained output](gpi16-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | GPI transamidase component PIG-T | CNN | PIG-T/Gpi16 identity agrees with the curated orthology, PIG-T domain and type-I ER membrane architecture. The name asserts complex membership rather than autonomous transamidase catalysis (O94380; IPR007245; CPX-10141). |

## Source quotations

## Research provenance

The genuine [Falcon report](gpi16-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.

## Direct ortholog evidence for the subunit boundary

Budding-yeast Gpi16 co-purifies with Gaa1 and Gpi8; depletion accumulates complete GPI lipid and unprocessed precursor proteins. Mammalian PIGT knockout and complex experiments establish an essential stabilizing role, while human structural analysis identifies PIGK as the catalytic component. These observations ground the conserved accessory-subunit inference for pombe Gpi16. The three cached articles are abstract-only, and their abstracts explicitly describe these experiments.

- [PMID:11598210](https://pubmed.ncbi.nlm.nih.gov/11598210/): Budding-yeast affinity purification establishes Gpi16 as a GPI-transamidase component, providing direct ortholog evidence.

> These complexes can be affinity purified
> and are shown to consist of Gaa1p, Gpi8p, and Gpi16p (YHR188c).

- [PMID:11483512](https://pubmed.ncbi.nlm.nih.gov/11483512/): Mammalian knockout and complex experiments establish a stabilizing accessory role for PIG-T.

> PIG-T maintains the complex by stabilizing the expression of GAA1 and GPI8.

- [PMID:35165458](https://pubmed.ncbi.nlm.nih.gov/35165458/): The human structure and mutational study identifies PIGK, not PIGT, as the catalytic component.

> The PIGK subunit 
> functions as the catalytic component

