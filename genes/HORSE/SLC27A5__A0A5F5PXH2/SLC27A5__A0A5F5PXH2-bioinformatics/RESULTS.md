# SLC27A5 (horse, A0A5F5PXH2): comparison with characterised SLC27A5 orthologs and the SLC27A2 paralog

Reproduce (from this directory): `uv run --script compare_orthologs.py`

Inputs: `A0A5F5PXH2.fasta` (horse, 700 aa), `Q9Y2P5.fasta` (human SLC27A5), `Q4LDG0.fasta`
(mouse Slc27a5), `O14975.fasta` (human SLC27A2), all fetched from the UniProt REST API on
2026-10-21. PANTHER subfamilies are taken from each UniProt record: A0A5F5PXH2, Q9Y2P5 and
Q4LDG0 are PTHR43107:SF25 (LONG-CHAIN FATTY ACID TRANSPORT PROTEIN 5); O14975 is
PTHR43107:SF4 (LONG-CHAIN FATTY ACID TRANSPORT PROTEIN 2).

Method: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, gap extend -0.5, free end
gaps. Raw output in `compare_orthologs_output.txt`.

## Output

```
A0A5F5PXH2 length 700
A0A5F5PXH2 vs Q9Y2P5 human SLC27A5: aligned pairs 690; identity 80.87%
AMP-binding motif human 292-303 FIYTSGTTGLPK; horse 302-313 FIYTSGTTGLPK; identical=True
A0A5F5PXH2 vs Q4LDG0 mouse Slc27a5: aligned pairs 689; identity 70.83%
A0A5F5PXH2 vs O14975 human SLC27A2: aligned pairs 609; identity 47.13%
```

## Interpretation

The horse protein is a full-length SLC27A5 ortholog: it aligns over the whole length of
human SLC27A5 at 80.9% identity and of mouse Slc27a5 at 70.8% identity, against 47.1% to the
paralog SLC27A2 (a different PANTHER subfamily). The AMP-binding motif annotated on human
SLC27A5 (residues 292-303, FIYTSGTTGLPK) is identical in horse (302-313; horse carries a
10-residue N-terminal extension). This is consistent with, but does not prove, retention of
the acyl-CoA synthetase activity; no horse protein has been assayed. The analysis says
nothing about substrate specificity (bile acid versus fatty acid), which is inferred only
from the shared SF25 subfamily membership with the experimentally characterised human and
mouse proteins.
