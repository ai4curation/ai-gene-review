# DST saved-source analysis results

The parser was executed against the pinned original inputs, then replayed with `--check`; both completed successfully.

| Computation | Result |
|---|---:|
| Official product sequences | 9 |
| IPI source contexts queried | 15 |
| Exact current IntAct record matches | 18 |
| OpenCell DST accession groups | 2 |
| Current products matching the deposited 30-aa 3GJO segment | 3 |
| PANTHER tree nodes / aligned sequences | 306 / 306 |
| IBA source rows / literal ancestral IBD matches | 9 / 9 |

The 3GJO peptide matches Q03001-7 residues 7541–7570, Q03001-8 residues 5142–5171 and Q03001-14 residues 5346–5375. The historical deposited accession/name remains in measurements.json; exact sequence correspondence is the basis for identifying the DST segment. These matches do not establish a full-length natural-product assay.

The OpenCell records are MAPRE1-bait recoveries of two DST prey accession groups at physical CSV lines 12883 and 12884 (zero-based data indexes 12881 and 12882). Every accession and numerical field is retained. The groups do not identify one natural isoform, and the field named pval is reproduced without reinterpreting its scale.

The target PAINT leaf is PTN000747957. Its ungapped sequence exactly matches the 7570-aa official product, and both source ancestral nodes PTN002753757 and PTN002753862 occur on the actual target path. All nine source-specific IBD rows are reproduced. Target self-grounding is legitimate descendant evidence, and donor count is not a confidence score.

Empty current IntAct joins for some historical source rows do not negate their original experiments. The biological review combines the literal records with source-specific original/abstract evidence and explicitly distinguishes purified or fragment assays from co-complex recovery.
