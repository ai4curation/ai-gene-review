# Rac1 (rat) ortholog sequence comparison

Script: `compare_orthologs.py` (fetches canonical sequences from the UniProt REST API).
Raw output: `output.txt`.

## Result

The canonical sequences of rat Rac1 (Q6RUV5), human RAC1 (P63000) and mouse Rac1 (P63001)
are identical over all 192 residues (192/192 identical positions for both human and mouse versus rat).

## Interpretation

Because the three proteins are identical in sequence, molecular-function and cellular-component
annotations transferred by ISO/ISS from human or mouse RAC1 carry no sequence-divergence risk.
Whether a transferred biological-process term is appropriate depends only on whether the
source annotation describes a function Rac1 itself performs, not on sequence.
