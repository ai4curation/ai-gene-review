# EFR3A (horse): comparison of all horse UniProt gene models (re-review)

Human reference: Q14156 (821 residues, N-terminus MPTRVCCCCSALRPRYKRLVDNIFPEDPKD).

| Accession | Length | Ensembl gene | Transcript | First exon (chr9) | N-terminus | Identity to human (paired) | Human residues unpaired | Residues at human Cys6-Cys9 | Mouse basic patch (PMID:24360784) mapped | GO in record |
|---|---|---|---|---|---|---|---|---|---|---|
| A0A3Q2GU27 | 821 | ENSECAG00000014883.4 | ENSECAT00000044066 | 74857303-74857521 | MPTRVCCCCSALRPRYKRLVDNIFPEDPKD | 98.54% over 821 | none | CCCC | K50->K50 R53->R53 R61->R61 R68->R68 R70->R70 | GO:0005886, GO:0072659 |
| A0A3Q2KQA4 | 794 | ENSECAG00000014883.4 | ENSECAT00000035827 | 74857303-74857521 | MPTRVCCCCSALRPRYKRLVDNIFPEDPKD | 98.49% over 794 | 259-285 | CCCC | K50->K50 R53->R53 R61->R61 R68->R68 R70->R70 | none |
| F6UA29 | 848 | ENSECAG00000014883.4 | ENSECAT00000016194 | 74889945-74890081 | MKDYVQVPAAELEKPYELTSTRESTTFLCL | 98.29% over 821 | none | CCCC | K50->K77 R53->R80 R61->R88 R68->R95 R70->R97 | GO:0005829, GO:0098978, GO:0005886, GO:0098793, GO:0072659, GO:0016082 |
| A0A9L0S4L8 (benchmark) | 796 | ENSECAG00000014883.4 | ENSECAT00000116354 | 74894800-74895054 | MIDKDGLVKADMEKLTFYAVSAPEKLDRIG | 98.24% over 796 | 2-26 | ---- | K50->K25 R53->R28 R61->R36 R68->R43 R70->R45 | GO:0005886 |

All horse EFR3A models derive from Ensembl gene(s): ENSECAG00000014883.4.

Alignment: Biopython PairwiseAligner global, match 2, mismatch -1, gap open -10, extend -0.5. Exon coordinates are from the Ensembl REST lookup of each transcript. Per-model details, including sequence hashes, are in `horse_models_rereview.json`.
