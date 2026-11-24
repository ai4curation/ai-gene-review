# Tango5 isoform and family placement (re-review 2026-10-21)

Script: `compare_isoforms.py` (run with `uv run compare_isoforms.py`); raw output in
`compare_isoforms_output.json`. Sequences, features and PANTHER placements are fetched
live from UniProt REST and the InterPro API.

## Results

- Q7KVQ7 (428 aa) is an exact C-terminal suffix of Q9W2S1 (530 aa), starting at Q9W2S1 residue 103 (an internal Met).
- Q7KVQ7 therefore lacks only the first 102 residues of Q9W2S1, which UniProt marks as a disordered, low-complexity/polar N-terminal region (MobiDB-lite disordered region 1..132 in Q9W2S1).
- All four Phobius transmembrane helices, the KMS1 N-terminal Pfam domain and the VMP1 C-terminal helical Pfam domain are present in both entries at shifted coordinates (+102).
- PANTHER: Q7KVQ7, Q9W2S1 and human VMP1 (Q96GC9) are all placed in PTHR10281:SF1 VACUOLE MEMBRANE PROTEIN 1.
- Global pairwise identity to human VMP1: Q7KVQ7 0.542 over 397 aligned columns; Q9W2S1 0.552 over 404 aligned columns.

## Interpretation

Q7KVQ7 is a shorter alternative-start isoform of Tango5. It differs from the longer product Q9W2S1 only by lacking a disordered N-terminal extension, and it keeps the whole conserved membrane-embedded VMP1 core. GO Central attaches the PAINT IBA annotations for this gene to Q9W2S1, so Q9W2S1 serves as the gene's representative product. Because the two entries share the same PANTHER subfamily as human VMP1 and the same conserved core, family-level inferences for Q9W2S1 also apply to Q7KVQ7.
