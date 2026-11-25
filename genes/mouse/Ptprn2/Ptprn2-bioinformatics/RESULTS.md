# Ptprn2 (P80560) ortholog comparison

Script: `compare_orthologs.py` (run with `uv run --no-project --with biopython --with requests python compare_orthologs.py`).
Raw output: `compare_orthologs_output.txt`.

## Results

- Mouse Ptprn2 P80560 (1001 aa), rat phogrin Q63475 (1004 aa) and human PTPRN2 Q92932 (1015 aa) are all
  classified in PANTHER subfamily PTHR46106:SF5 (UniProt PANTHER cross-references).
- Global BLOSUM62 alignment: mouse vs rat 92.9% identity; mouse vs human 70.7% identity (computed over the shorter sequence length).
- The rat catalytic cysteine C934, whose C934S mutation abolished phosphatidylinositol phosphatase activity in PMID:20097759,
  aligns to mouse C931, with identical local context PIIVHCSDGAGR in mouse (926-937) and rat (929-940).

## Interpretation

Mouse and rat Ptprn2 are orthologs in the same PANTHER subfamily, and the residue required for the rat
protein's phosphoinositide phosphatase activity is conserved in mouse with identical flanking sequence. This
supports inferring (not establishing) that mouse Ptprn2 has the same activity; it has not been assayed for the
mouse protein.
