# EOGT natural products and tested clone

All three UniProt natural products reconstruct exactly from the recorded alternative-sequence edits and match the independent official FASTA, residue for residue. The translated human clone KC347596.1/AGC92970.1 matches only Q5NDL2-1, the 527-residue product used in PMID:23671640. These sequence checks delimit which product the functional experiments establish.

| Natural product | Length | Recorded sequence differences | Projected targeting/activity-related sequence |
|---|---:|---|---|
| Q5NDL2-1 | 527 aa | Displayed sequence | Signal 1–17; annotated mature chain 18–527; DYD 295–297; HDEL 524–527 |
| Q5NDL2-2 | 208 aa | F208C followed by loss of canonical residues 209–527 | Retains signal sequence; lacks canonical DYD and HDEL segments |
| Q5NDL2-3 | 443 aa | Loss of canonical residues 278–361 | Retains signal sequence; lacks DYD; HDEL projects to 440–443 |

Signal cleavage and motif meanings are UniProt annotations, not experimentally determined by this script. The chain projection merely counts surviving canonical residues and is not a prediction that the shorter products are processed into functional enzymes. No natural product has been deleted from the review, and no shorter product is labelled functionally equivalent to the canonical enzyme.

[PMID:23671640](https://pmc.ncbi.nlm.nih.gov/articles/PMC3650022/), Results/Figure 1 and Methods, tested the 527-residue human protein in fly S2 cells. Its DYD-to-AYA mutant has reduced rather than abolished activity. The paper's low-activity prediction for a shorter transcript lacking the DYD region is not a direct assay of natural isoform 3. It also does not establish the behavior of the more extensively truncated isoform 2. The human clone's EMBL record identifies HEK293T as the source cell line; that source identity is distinct from the fly host used for the functional assay.

The 527-residue clone and canonical sequence have SHA256 `3a148377908f52a8d44d9e4dafaf90c551fe2d6b5bed139b06f43bafa8598be7`. Full sequences, edit coordinates, exact-match checks, projected features and their original evidence tags are in `products.json`. See [README](README.md) for source URLs, pinned inputs and replay.

## Quality checks

- [x] The analysis script takes input/output paths; no hardcoded gene-specific inputs, expected lengths, coordinates or conclusions.
- [x] Tested on a second real input: six ENTPD1 products reconstructed at 510, 517, 306, 372, 402 and 522 aa, all matching independent official FASTA.
- [x] EOGT reconstruction completed with exact matches for all three products and the tested clone.
- [x] Direct generated results and input snapshots accompany this summary.
- [x] Sequence provenance and biological limits are distinguished; retained motifs are not treated as proof of equivalent function.
