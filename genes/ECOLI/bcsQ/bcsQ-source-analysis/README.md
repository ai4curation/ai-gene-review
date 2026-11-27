# BcsQ intact record and downstream-start fragment

The preserved local UniProt records encode P0DP92 (250 residues) and P37655 (242 residues). P37655 residues 2-242 exactly match P0DP92 residues 10-250. P37655 starts with initiator methionine where the full-length sequence has Val9; its downstream GTG start therefore does not make the two records equivalent. The original paper places the premature stop at codon 6 of the full reading frame and repairs TAG to TTG in W3110 to generate AR3110 (PMID:24097954).

The raw P37655 record assigns it to reference proteome UP000000625. P0DP92 has no reference-proteome membership line and represents the functional full-length/repaired protein. Thus the curated relationship is P0DP92 to the same-locus reference-proteome counterpart P37655, not equivalence and not automatic function transfer. No reciprocal proteome relationship is invented.

The P0DP92 sequence record also states an A249K variant in strain 1094. The 2021 and 2024 BcsRQ structures use genes from strain 1094 and recombinant expression hosts. Those data support closely related full-length BcsQ function but are not an identical-sequence assay of the repaired K-12 allele, and are not assays of the 242-residue fragment.

Run `uv run python genes/ECOLI/bcsQ/bcsQ-source-analysis/compare_records.py` from the repository root to regenerate sequence-comparison.json. It reads the preserved raw records and records their SHA256 values; it does not refresh or alter source files. Native fragment expression and intrinsic nucleotide activities remain unresolved.
