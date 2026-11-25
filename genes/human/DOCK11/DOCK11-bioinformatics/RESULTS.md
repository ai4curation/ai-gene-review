# DOCK11 historical construct sequence

The saved AY692226.1/AAU04438.1 translation and human Q5JSL3 sequences both contain 2,073 residues. The computed positional comparison finds three differences:

| Position | Historical clone | UniProt snapshot |
|---|---|---|
| 376 | L | F |
| 740 | K | N |
| 1984 | E | K |

The full computed result and input hashes are in [results/DOCK11.json](results/DOCK11.json). The source sequences are [NCBI AY692226.1](https://www.ncbi.nlm.nih.gov/nuccore/AY692226.1) and [UniProt Q5JSL3](https://www.uniprot.org/uniprotkb/Q5JSL3/entry). The historical human construct therefore is not sequence-identical to this current reference snapshot. These differences do not establish loss of function and do not negate the original measured activity.

- [x] The comparison script has no hardcoded gene input or expected output.
- [x] The script was run on a different protein (DOCK6 identity control) and on different-length DOCK2 products.
- [x] The equal-length analyses completed; unequal lengths explicitly returned inconclusive.
- [x] Direct computed outputs and source hashes are included.
- [x] Methods, provenance, reproducible commands and interpretive limits are documented.
