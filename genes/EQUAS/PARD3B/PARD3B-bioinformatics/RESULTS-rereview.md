# PARD3B re-review: conservation of the PDZ2-PDZ3 linker (2026-10-21)

Reproduce (from this folder):
`uv run --script compare_interpdz_rereview.py ../PARD3B-uniprot.txt Q8TEW8.fasta 469-497 383-468 498-585 > compare_interpdz_rereview_output.txt`

Rationale: Huo & Macara 2014 (PMID:24859006) map LKB1 binding of Par3L/PARD3B to a short
sequence between PDZ2 and PDZ3 that is absent from PARD3, and show that swapping it for
the PARD3 sequence abolishes LKB1 binding. Human PARD3B PDZ2 is 383-468 and PDZ3 is
498-585 (UniProt Q8TEW8 features), so the linker is human 469-497. The paper does not
give the exact residues of the essential sub-segment, so the whole linker is tested.

Method: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5; human
PARD3B (Q8TEW8.fasta, already in this folder) aligned to donkey A0A9L0JEY6 (local
UniProt flat file), mouse Pard3b Q9CSB4 and human PARD3 Q8TEW0 (fetched from UniProt).

## Output (compare_interpdz_rereview_output.txt)

```
donkey: human PARD3B 469-497: 29 of 29 aligned, 26 identical
mouse_Pard3b: human PARD3B 469-497: 29 of 29 aligned, 25 identical
human_PARD3: human PARD3B 469-497: 29 of 29 aligned, 15 identical
donkey: human PARD3B 383-468: 86 of 86 aligned, 85 identical
human_PARD3: human PARD3B 383-468: 86 of 86 aligned, 52 identical
donkey: human PARD3B 498-585: 88 of 88 aligned, 84 identical
human_PARD3: human PARD3B 498-585: 88 of 88 aligned, 72 identical
```

## Interpretation

The PDZ2-PDZ3 linker of donkey PARD3B is 26/29 identical to human PARD3B and the
corresponding mouse Pard3b linker (the protein used in the LKB1 experiments) is 25/29
identical, whereas human PARD3 shares only 15/29 residues there. The linker is
therefore a PARD3B-subfamily (PANTHER PTHR16484:SF4) feature that the donkey protein
retains, consistent with conservation of the LKB1-binding property. This is a sequence
argument only; LKB1 binding has not been tested for the donkey protein.
