# IRAK3: human–horse sequence comparison

The downloaded human Q9Y616 sequence (596 residues) and selected horse A0A3Q2HDT6 sequence (567 residues) share 80.7% identity among 554 paired residues. Paired coverage is 93.0% of human and 97.7% of horse.

Full alignment, hashes, parameters and reproducible script: [IRAK3.json](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/IRAK3.json) and [compare.py](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/compare.py).

Pairwise similarity supports homology but does not establish reciprocal orthology, intact gene models, conservation of targeting signals or every biological claim. Current UniProt sequences are compared; identity with the original ProtNLM input sequence is unverified.

## Architecture check

The selected horse sequence lacks human residues 2–43, reaching the beginning of the annotated death domain at residues 41–106. The kinase-like domain is retained. Receptor-complex assembly requires caution because the N-terminal interaction region is shortened.
