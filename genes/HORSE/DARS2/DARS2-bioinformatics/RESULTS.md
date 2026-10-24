# DARS2: human–horse sequence comparison

The downloaded human Q6PI48 sequence (645 residues) and selected horse A0A9L0SB67 sequence (616 residues) share 90.3% identity among 607 paired residues. Paired coverage is 94.1% of human and 98.5% of horse.

Full alignment, hashes, parameters and reproducible script: [DARS2.json](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/DARS2.json) and [compare.py](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/compare.py).

Pairwise similarity supports homology but does not establish reciprocal orthology, intact gene models, conservation of targeting signals or every biological claim. Current UniProt sequences are compared; identity with the original ProtNLM input sequence is unverified.

## Architecture check

The selected horse sequence retains a positively charged N-terminal extension corresponding to the human mitochondrial transit region, but lacks human residues 341–376 internally. This does not establish relaxed tRNA(Asn) substrate specificity.
