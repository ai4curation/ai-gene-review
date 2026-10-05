# OLFML2A: human–horse sequence comparison

The downloaded human Q68BL7 sequence (652 residues) and selected horse A0A9L0SKW1 sequence (599 residues) share 91.3% identity among 598 paired residues. Paired coverage is 91.7% of human and 99.8% of horse.

Full alignments, sequence hashes and calculation details: [OLFML2A.json](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/OLFML2A.json). Reproduce with [compare.py](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/compare.py) using the two downloaded UniProt text records. See the [methods and limitations](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/README.md).

- [x] Computed from sequence inputs; no hardcoded results.
- [x] The same script was run on ten different gene pairs.
- [x] Alignment completed and full output retained.
- [ ] Orthology, gene-model completeness and conservation of each biological claim require additional evidence. Sequence similarity alone does not establish them.

Current UniProt sequences were compared; their identity with the original ProtNLM input sequences has not been established.

## Targeting-sequence discrepancy

The global alignment pairs the initiating horse methionine with human residue 1, then places a 26-residue gap opposite human residues 2–27. Human UniProt annotates residues 1–27 as the signal peptide; the horse sequence starts `MDSQVFGDMDQVRMTSEGSDCRCKCIMRPLSKDA`, without the hydrophobic human leader. A further 22-residue internal deletion occurs opposite human residues 123–144. The conserved olfactomedin domain supports family identity, but the selected sequence does not retain the canonical secretion signal. This could reflect a transcript model, isoform or sequence-completeness issue. It does not establish that the horse gene is intracellular, or that the original ProtNLM input lacked the leader.
