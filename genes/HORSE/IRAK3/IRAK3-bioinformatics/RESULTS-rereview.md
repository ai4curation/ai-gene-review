# IRAK3 (horse) re-review: gene-model comparison

Script: `compare_gene_models_rereview.py` (run with `uv run --no-project --with biopython --with requests python compare_gene_models_rereview.py`).
Output: `results-rereview.json`. Sequences fetched live from UniProt REST; transcript structure from Ensembl REST (gene ENSECAG00000026958). Global alignment, BLOSUM62, gap open -10, extend -0.5, free end gaps.

## Horse IRAK3 gene models

Ensembl gene ENSECAG00000026958 (IRAK3) has three protein-coding transcripts. The Ensembl canonical transcript is ENSECAT00000029063 (14 exons, 614 aa, UniProt F6QZW8, RefSeq XP_023499869.1 isoform X1). The benchmark accession A0A3Q2HDT6 is the non-canonical transcript ENSECAT00000032597 (12 exons, 567 aa), whose first exon (82869200-82869293) lies downstream of the canonical first exon (82854864-82854933). A third model, ENSECAT00000078473 (553 aa, A0A5F5PKF5, XP_023499870.1 isoform X2), skips most of the death domain.

Benchmark A0A3Q2HDT6 vs canonical F6QZW8: 567 paired residues, 564 identical (99.5%); the benchmark covers 92.3% of the canonical product. Benchmark residues 4-567 are an exact substring of F6QZW8 starting at canonical residue 51. The benchmark therefore replaces canonical residues 1-50 with the three-residue start MIT, from an alternative first exon.

## Mapping of human Q9Y616 features

| Human feature (Q9Y616) | Benchmark A0A3Q2HDT6 | Canonical F6QZW8 | Mouse Q8K4B2 |
|---|---|---|---|
| N-terminal 1-40 | absent (0/40) | 6-45 | 1-40 |
| Death domain 41-106 | 64/66, residues 1-64 | 66/66, 46-111 | 66/66 |
| Ser110 (IRAK1 site) | N68 | N115 | T110 |
| Protein kinase domain 165-452 | 288/288, 123-410 | 288/288, 170-457 | 288/288 |
| CGS291-293 | CGS249-251 | CGS296-298 | CGN |
| DFA311-313 | DFA269-271 | DFA316-318 | DFA |

Identity to human Q9Y616: benchmark 80.5% over 554 paired residues; canonical F6QZW8 81.4% over 596 paired residues (100% of human).

## Interpretation

The benchmark accession is an alternative Ensembl gene model, not the canonical product. It lacks the 45-residue N-terminal extension and the first residues of the PROSITE death-domain boundary, while the Pfam death-domain match, the complete pseudokinase domain with the noncanonical CGS/DFA configuration, and the C-terminal region are retained. Whether this alternative first exon is used in vivo is not established here. Human Ser110, the IRAK1/PIN1 site, is not conserved in horse (Asn), so the IL-33/PIN1 nuclear-translocation mechanism characterised for human IRAK-M cannot be assumed for horse.
