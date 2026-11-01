# PpG2–KT2440 protein comparisons

Run `just run` in this directory. The script accepts two UniProt flat files and an output path; it extracts sequences without changing the downloaded records. Biopython 1.85 is pinned in inline uv metadata. Global alignment uses match 2, mismatch −1, gap opening −10 and extension −0.5. Outputs include exact source hashes, alignments and counts. Results and biological limitations are in RESULTS.md. This is a pairwise comparison, not a reconstructed phylogeny or a catalytic assay.
