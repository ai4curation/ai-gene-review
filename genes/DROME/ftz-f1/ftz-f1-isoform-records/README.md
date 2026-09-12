# Accession, isoform, and prediction-attribution records

Retrieved 2026-09-08. These are source snapshots, not edited annotation evidence.

- [M9NFK2.fasta](https://rest.uniprot.org/uniprotkb/M9NFK2.fasta): the 803-aa ProtNLM target's current sequence.
- [P33244.json](https://rest.uniprot.org/uniprotkb/P33244.json): reviewed FTZ-F1, including the alternative-product mapping and sequence changes attributed to PMID:8096644.
- [P33244-2.fasta](https://rest.uniprot.org/uniprotkb/P33244-2.fasta): reviewed isoform A. It is exactly identical to M9NFK2 (803/803 aa; SHA256 `8e47b8779f9e0ee27c6b92a56b1170a84a3c05cd7eade1dd500c5d6d3c6082b7`). This is a sequence equality check, not a new functional experiment.
- `P33244-1.fasta`: the displayed 1027-aa sequence extracted from `P33244.json`, used as a nonidentical control.
- `M9NFK2-protnlm.json`: exact record extracted from the project's frozen `fly-benchmark/predictions.jsonl.gz`.
- [Q91279.json](https://rest.uniprot.org/uniprotkb/Q91279.json): the function paragraph's recorded phmmer accession, Japanese flounder thyroid hormone receptor beta.
- [O42101.json](https://rest.uniprot.org/uniprotkb/O42101.json): the predicted protein name's recorded phmmer accession, chicken NR5A2/LRH-1.

Run from this directory with Python 3 (standard library only):

```sh
python compare_fasta.py M9NFK2.fasta P33244-2.fasta
python compare_fasta.py M9NFK2.fasta P33244-1.fasta
```

Saved outputs are `sequence-comparison.json` (identical) and `canonical-control-comparison.json` (not identical). The script accepts input paths and computes all results; it has also been checked using two synthetic nonidentical sequences. The comparison establishes current database sequence identity. It does not establish which archived sequence the model originally received.
