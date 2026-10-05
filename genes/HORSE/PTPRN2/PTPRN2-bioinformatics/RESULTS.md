# PTPRN2: human–horse sequence comparison

The downloaded human Q92932 sequence (1015 residues) and selected horse A0A9L0T4W6 sequence (976 residues) share 71.0% identity among 947 paired residues. Paired coverage is 93.3% of human and 97.0% of horse.

Full alignment, hashes, parameters and reproducible script: [PTPRN2.json](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/PTPRN2.json) and [compare.py](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/compare.py).

Pairwise similarity supports homology but does not establish reciprocal orthology, intact gene models, conservation of targeting signals or every biological claim. Current UniProt sequences are compared; identity with the original ProtNLM input sequence is unverified.

## Architecture check

The selected horse sequence has a divergent C-terminal region, including deletion of human residues 989–1003 within the annotated phosphatase domain. The N-terminal signal sequence and transmembrane segment are retained. Substrate-specific enzymatic activity requires more than the global homology assignment.
