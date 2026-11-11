# A0A8C9H4D2 gene-model comparison (2026-10-20)

Script: `compare_to_human.py` (run with `uv run genes/9PRIM/A0A8C9H4D2/A0A8C9H4D2-bioinformatics/compare_to_human.py` from the repository root). Raw output: `compare_to_human.out`. Inputs: the cached UniProt flat files for A0A8C9H4D2 and human Q68BL7, and `A0A8C9H9A8-uniprot.txt` (downloaded from rest.uniprot.org on 2026-10-20).

## Results

- A0A8C9H4D2 is 439 aa; human OLFML2A Q68BL7 is 652 aa.
- Local alignment: query 9-439 aligns to human 223-652, 418/430 identical (97.2%). Human residues 1-222 have no counterpart in A0A8C9H4D2.
- The human region absent from A0A8C9H4D2 contains 8 cysteines at positions 47, 49, 51, 61, 86, 88, 90, 100, i.e. the two tandem CXCXCX9C motifs, as well as the signal peptide (human 1..27) and the predicted coiled coil (human 157..183).
- A0A8C9H4D2 vs reconstructed human isoform 3 (Q68BL7-3: residues 1-214 missing; 215-223 ATGTGSKAQ -> MSKRDKAGK): query 1-439 aligns to iso3 1-438, 426/438 identical (97.3%). The A0A8C9H4D2 N-terminus (MRKRDKAGK) corresponds to the alternative first exon of human isoform 3.
- A0A8C9H9A8 (655 aa, RefSeq XP_023072932.1 isoform X1, same Ensembl gene ENSPTEG00000015637) is the full-length product of the same Piliocolobus gene: query 9-439 aligns to A0A8C9H9A8 225-655, 430/431 identical (99.8%). A0A8C9H9A8 carries a SignalP signal peptide 1..27 and the olfactomedin domain 397..655; A0A8C9H4D2 has no signal peptide feature.

## Interpretation

A0A8C9H4D2 (XP_023072933.1, isoform X2) is the short alternative-first-exon isoform of Piliocolobus OLFML2A, the counterpart of human isoform 3. It retains the complete C-terminal olfactomedin domain but lacks the signal peptide, both CXCXCX9C motifs and the coiled coil. Whether this short transcript is translated, and where the product goes, has not been tested in any species; without a signal peptide it is not expected to enter the classical secretory pathway.
