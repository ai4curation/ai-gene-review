# DUOX1: human–horse sequence comparison

The downloaded human Q9NRD9 sequence (1551 residues) and selected horse A0A9L0SQG9 sequence (1452 residues) share 91.4% identity among 1452 paired residues. Paired coverage is 93.6% of human and 100.0% of horse.

Full alignment, hashes, parameters and reproducible script: [DUOX1.json](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/DUOX1.json) and [compare.py](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/compare.py).

Pairwise similarity supports homology but does not establish reciprocal orthology, intact gene models, conservation of targeting signals or every biological claim. Current UniProt sequences are compared; identity with the original ProtNLM input sequence is unverified.

## Domain-level check

The global alignment deletes human DUOX1 residues 775–873 from the selected horse sequence. The fetched human UniProt feature table places EF-hand 1 at 815–850 and EF-hand 2 at 851–887. Thus the selected sequence lacks the first annotated EF-hand and most of the second, despite retaining the signal peptide, transmembrane oxidase region and C-terminal FAD/NADPH-binding region. Calcium-responsive activity cannot be transferred from full-length human DUOX1 without resolving this deletion.
