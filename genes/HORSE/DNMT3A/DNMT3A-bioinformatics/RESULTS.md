# DNMT3A: human–horse sequence comparison

The downloaded human Q9Y6K1 sequence (912 residues) and selected horse A0A9L0TK01 sequence (873 residues) share 97.3% identity among 873 paired residues. Paired coverage is 95.7% of human and 100.0% of horse.

Full alignments, sequence hashes and calculation details: [DNMT3A.json](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/DNMT3A.json). Reproduce with [compare.py](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/compare.py) using the two downloaded UniProt text records. See the [methods and limitations](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/README.md).

- [x] Computed from sequence inputs; no hardcoded results.
- [x] The same script was run on ten different gene pairs.
- [x] Alignment completed and full output retained.
- [ ] Orthology, gene-model completeness and conservation of each biological claim require additional evidence. Sequence similarity alone does not establish them.

Current UniProt sequences were compared; their identity with the original ProtNLM input sequences has not been established.

## Chromatin-reader versus catalytic-domain conservation

The horse model lacks aligned human residues 339–374, overlapping the end of the PWWP domain (human UniProt annotation 292–350) and adjacent sequence. The ADD domain (human 482–614) and C-terminal methyltransferase domain (634–912) are retained. Loss of a PWWP segment makes normal histone-guided genomic targeting uncertain, but does not imply loss of the separable methyltransferase reaction: experimentally studied PWWP substitutions can alter targeting while retaining de novo DNA methylation (PMID:30478443). Broad nuclear localization and gene-expression regulation are therefore more defensible than transfer of precise heterochromatin-targeting properties.
