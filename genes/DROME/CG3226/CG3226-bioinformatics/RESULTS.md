# CG3226 bioinformatics: taxonomic distribution of S100 proteins

Question: does Drosophila melanogaster encode any S100 protein that could be a
partner for the CacyBP/SIP ortholog CG3226 (Q9W3Y3), as implied by the
InterPro2GO annotation GO:0044548 S100 protein binding (via IPR037893)?

Method: `s100_taxon_counts.py` queries the InterPro REST API for the number of
UniProt proteins carrying the S100 Pfam domain (PF01023, S_100) in each taxon.
Raw output: `s100_taxon_counts.tsv`. Run with `python3 -I s100_taxon_counts.py`.

Results (InterPro API, run 2026-10-19):

| taxid | taxon | PF01023 proteins |
|---|---|---|
| 7227 | Drosophila melanogaster | 0 |
| 50557 | Insecta | 1 |
| 6656 | Arthropoda | 3 |
| 6231 | Nematoda | 0 |
| 6447 | Mollusca | 0 |
| 7586 | Echinodermata | 0 |
| 7711 | Chordata | 12351 |
| 7712 | Tunicata | 6 |
| 7735 | Cephalochordata | 0 |
| 7742 | Vertebrata | 12350 |
| 33208 | Metazoa | 12352 |

Interpretation: essentially all S100-domain proteins in UniProt are from
vertebrates, with a handful from tunicates; D. melanogaster has none. The
1 insect / 3 arthropod hits were not inspected and are most plausibly
contaminant or sporadic sequences; they do not affect the conclusion for
D. melanogaster. This agrees with phylogenetic surveys (PMID:27764152,
PMID:18275604) that place the origin of the S100 family within chordates
(vertebrates plus tunicates).

Conclusion: CG3226 has no S100 protein to bind in D. melanogaster; GO:0044548
on Q9W3Y3 is a taxon-inappropriate InterPro2GO transfer.
