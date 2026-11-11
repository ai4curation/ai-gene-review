# BICDL1 (donkey A0A9L0K8K5): comparison with mouse and human orthologs

Script: `compare_orthologs.py` (PEP 723; run with `uv run --script compare_orthologs.py`). It fetches the three
sequences live from UniProt, makes BLOSUM62 global alignments (gap open -10, extend -0.5) and writes `results.json`.

## Evolutionary placement

A0A9L0K8K5 is in PANTHER subfamily PTHR32123:SF12 (BICD FAMILY-LIKE CARGO ADAPTER 1), the same subfamily as
mouse Bicdl1 (A0JNT9), human BICDL1 (Q6ZP65), Xenopus and zebrafish bicdl1 (from the UniProt PANTHER cross-reference
and `interpro/panther/PTHR32123/PTHR32123-entries.csv`). The PAINT IBDs for vesicle transport along microtubule
(GO:0047496) and Golgi to secretory granule transport (GO:0055107) sit on node PTN001281025 (taxon:33511,
Deuterostomia), seeded by zebrafish bicdl1 and mouse Bicdl1 (MGI:1922915) respectively.

## Results

- Lengths: donkey 626, mouse 577, human 573 residues.
- Donkey vs mouse A0JNT9: 545 identical of 574 aligned pairs (94.95% identity over aligned residues); 52 donkey residues unaligned.
- Donkey vs human Q6ZP65: 552 identical of 573 aligned pairs (96.34% identity over aligned residues); 53 donkey residues unaligned.
- CC1 box (AARLG), the dynein light-intermediate-chain binding motif of activating adaptors: donkey 114, mouse 116, human 113.
- Mouse Lys512, required for Rab6 binding in mouse BICDR-1, aligns to donkey Lys562, in an identical 11-residue context (DAIQQKLNLSQ).
- Donkey has one insertion relative to mouse, residues 442-489 (SSRRIDDDSLEEQIRQTSEDSRALRELMEGERGKLRQSLEELQRLHSQ). It corresponds to the alternative exon of human isoform 2 (see the sibling analysis `genes/EQUAS/BICDL1/BICDL1-bioinformatics/RESULTS-rereview.md`, SEG_ALT). It lies between the N-terminal dynein-binding coiled coil and the C-terminal Rab6-binding region.

## Interpretation

The donkey Ensembl canonical product keeps the full canonical coiled-coil architecture of mouse and human BICDL1,
including the CC1 box and the residue that mouse Rab6 binding depends on, plus one isoform-2-type exon. Nothing in
the sequence argues against transfer of the mouse BICDR-1 activities within SF12. No experiment has been done on the
donkey protein, so all functions are inferred.
