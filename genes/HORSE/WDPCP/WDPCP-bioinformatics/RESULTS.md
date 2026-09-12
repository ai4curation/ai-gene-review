# WDPCP: human–horse sequence comparison

The downloaded human O95876 sequence (746 residues) and selected horse A0A3Q2KRK8 sequence (705 residues) share 88.1% identity among 704 paired residues. Paired coverage is 94.4% of human and 99.9% of horse.

Full alignments, sequence hashes and calculation details: [WDPCP.json](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/WDPCP.json). Reproduce with [compare.py](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/compare.py) using the two downloaded UniProt text records. See the [methods and limitations](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/README.md).

- [x] Computed from sequence inputs; no hardcoded results.
- [x] The same script was run on ten different gene pairs.
- [x] Alignment completed and full output retained.
- [ ] Orthology, gene-model completeness and conservation of each biological claim require additional evidence. Sequence similarity alone does not establish them.

Current UniProt sequences were compared; their identity with the original ProtNLM input sequences has not been established.

## Domain context

The horse model lacks aligned human residues 1–33 and 721–729. The structural CPLANE study (PMID:35427153) identifies a human-specific approximately 35-residue N-terminal extension relative to mouse; the N-terminal difference is therefore compatible with ordinary mammalian variation. The short C-terminal deletion falls in an unresolved tail, but that tail mediates phosphoinositide binding. Disorder does not make this second deletion functionally irrelevant: its effect on lipid affinity is untested. The WD40/alpha-solenoid scaffold is extensively conserved, supporting broad ciliary and cytoskeletal roles.
