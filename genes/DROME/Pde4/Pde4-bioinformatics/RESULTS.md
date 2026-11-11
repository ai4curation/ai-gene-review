# Pde4 (dunce) Q9W4S9 vs the canonical dnc entry P12252

Script: `compare_dnc_entries.py` (run with `uv run compare_dnc_entries.py > compare_dnc_entries.json`).
It fetches Q9W4S9, P12252 and human PDE4D (Q08499) from UniProt REST, aligns them
(BLOSUM62, global with free end gaps) and maps the P12252 PDEase domain, active-site and
ligand-binding features onto Q9W4S9. Raw output: `compare_dnc_entries.json`.

## Results (from compare_dnc_entries.json, 2026-10-21)

- Lengths: Q9W4S9 983 aa (isoform N); P12252 1070 aa (isoform II); human PDE4D Q08499 809 aa.
- Q9W4S9 and P12252 share an identical C-terminal block of 614 residues; the two entries differ only in their N-terminal regions (alternative first exons / initiation sites of the dnc locus).
- The P12252 PDEase domain (656-985) maps to Q9W4S9 569-898, the same span UniProt annotates as the PDEase domain on Q9W4S9.
- All P12252 catalytic features map with identical residues: proton-donor active site 732 -> Q9W4S9 645; cAMP-binding positions 732-736, 773, 890, 941 -> 645-649, 686, 803, 854; divalent-metal-binding positions 736, 772, 773, 890 -> 649, 685, 686, 803.
- Q9W4S9 PDEase domain vs human PDE4D: 234 of 330 aligned positions identical (about 71 percent).

## Interpretation

Q9W4S9 is not a fragment or a defective gene model: it is the complete product of the
dnc transcripts encoding isoforms N and G, with the full PDE4 catalytic domain and every
catalytic and metal-binding residue annotated on the canonical entry. The biochemical
evidence for cAMP hydrolysis obtained with dnc cDNAs therefore applies to the shared
catalytic region of this product.
