# OpuCC sequence identity check

`3PPQ-entity1.json` is the unmodified response from the RCSB core API URL recorded in `provenance.json`. `identity-mapping.json` records comparison against the frozen `../opuCC-uniprot.txt`. Extract the UniProt sequence after SQ, remove spaces and newlines, and compare with `entity_poly.pdbx_seq_one_letter_code_can` after its eight-residue MGHHHHHH tag. The remaining 303 residues match exactly. The RCSB SIFTS mapping independently maps entity positions9–311 to O32243 positions1–303. This is a deposited-sequence identity check, not a claim that every residue has resolved atomic coordinates.

The author-hosted full paper was inspected for constructs and ligand assays. Its source URL and download checksum are recorded in provenance; full PDFs and pdftotext outputs are kept in the ignored acquisition cache. Choline, carnitine, glycine betaine and ectoine were tested; a COS-bound structure is not claimed.
