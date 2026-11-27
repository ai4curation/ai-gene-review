# SNAP23 (horse, A0A3Q2HTF1): sequence comparison with characterised orthologs

## Method

`compare_to_human.py` (PEP 723 script; run with
`uv run --script compare_to_human.py ../SNAP23-uniprot.txt <reference.fasta>`)
performs a Biopython global alignment (BLOSUM62, gap open -10, gap extend -0.5)
of the horse UniProt sequence against a reference ortholog and reports identity,
the horse residues aligned to the reference palmitoylated cysteines, and identity
within the two t-SNARE coiled-coil motifs. Reference residue numbers are labelled
"human" in the script output even when the reference is the mouse sequence.

References: human SNAP23 O00161 (`human-SNAP23-O00161-uniprot.txt`,
`human-SNAP23-O00161.fasta`) and mouse Snap23 O09044 (`mouse-Snap23-O09044.fasta`),
both downloaded from UniProt REST on 2026-10-21. Raw outputs:
`compare_to_human_output.txt`, `compare_to_mouse_output.txt`.

## Results

- Horse A0A3Q2HTF1 is 211 aa, the same length as human SNAP23 isoform SNAP-23a (O00161-1, 211 aa); mouse Snap23 is 210 aa.
- Horse vs human: 211 aligned pairs, no gaps, 184 identical (87.2%).
- Horse vs mouse: 210 aligned pairs, 188 identical (89.5%).
- N-terminal SNARE motif (Qb, human 14..76): 59/63 identical to human.
- C-terminal SNARE motif (Qc, human 146..208): 52/63 identical to human.
- The cysteine-rich palmitoylation linker is conserved: human C79, C80, C83, C85 and C87 (S-palmitoylated, PubMed:21044946) align to horse C79, C80, C83, C85 and C87. Human C112 (also reported S-palmitoylated) aligns to horse S112; mouse also has S at this position.
- The last four residues differ from both human and mouse (horse ...KRLLPQ, human ...KKLIDS, mouse ...KKLIDS). This lies after the end of the second SNARE motif and may reflect a genuine sequence difference or the Ensembl gene model for the final exon; it does not remove the SNARE motif.

## Interpretation

A0A3Q2HTF1 is a full-length SNAP23 product with both SNARE motifs and the
palmitoylated membrane-anchoring linker. UniProt places it, like human O00161,
in PANTHER subfamily PTHR19305:SF4 (SYNAPTOSOMAL-ASSOCIATED PROTEIN 23), so it is
the ortholog of the experimentally characterised human and mouse SNAP23 rather
than of SNAP25 (SF5), SNAP29 or SNAP47.
