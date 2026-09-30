# CC2D2A: human–horse sequence comparison

The downloaded human Q9P2K1 sequence (1620 residues) and selected horse A0A5F5PJ44 sequence (1480 residues) share 90.3% identity among 1478 paired residues. Paired coverage is 91.2% of human and 99.9% of horse.

Full alignments, sequence hashes and calculation details: [CC2D2A.json](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/CC2D2A.json). Reproduce with [compare.py](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/compare.py) using the two downloaded UniProt text records. See the [methods and limitations](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/README.md).

- [x] Computed from sequence inputs; no hardcoded results.
- [x] The same script was run on ten different gene pairs.
- [x] Alignment completed and full output retained.
- [ ] Orthology, gene-model completeness and conservation of each biological claim require additional evidence. Sequence similarity alone does not establish them.

Current UniProt sequences were compared; their identity with the original ProtNLM input sequences has not been established.

## Domain context

The horse sequence lacks aligned human residues 1–49 and 147–239. Both intervals fall within the human UniProt record's predicted disordered region 1–241. The long coiled-coil and C2-domain-containing architecture is retained. These gaps therefore do not by themselves demonstrate loss of the conserved ciliary scaffold. This is a domain-context inference, not experimental confirmation of the horse model.
