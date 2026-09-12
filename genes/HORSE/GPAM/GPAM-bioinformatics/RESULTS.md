# GPAM: human–horse sequence comparison

The downloaded human Q9HCL2 sequence (828 residues) and selected horse A0A9L0TTC1 sequence (790 residues) share 94.2% identity among 790 paired residues. Paired coverage is 95.4% of human and 100.0% of horse.

Full alignment, hashes, parameters and reproducible script: [GPAM.json](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/GPAM.json) and [compare.py](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/compare.py).

Pairwise similarity supports homology but does not establish reciprocal orthology, intact gene models, conservation of targeting signals or every biological claim. Current UniProt sequences are compared; identity with the original ProtNLM input sequence is unverified.

## Architecture check

The selected horse sequence lacks human residues 370–407 internally. Named human substrate-binding positions 278, 279, 288, 293, 328 and 462 remain outside this deletion, but enzymatic competence of the exact shortened sequence is not measured.
