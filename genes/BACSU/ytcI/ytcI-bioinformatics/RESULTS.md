# YtcI (C0SPB0) pairwise identity to characterised PTHR43605:SF10 relatives

Script: `pairwise_identity.py` (run from the repository root with
`uv run python genes/BACSU/ytcI/ytcI-bioinformatics/pairwise_identity.py`). Sequences are fetched
live from UniProt; global alignment with Biopython PairwiseAligner, BLOSUM62, gap open -10,
extend -0.5. Raw output: `pairwise_identity.tsv` (run 2026-11-02).

| Target | Description | % identity (aligned columns) |
|---|---|---|
| A0A0H2XHR6 | S. aureus USA300 MbcS (SAUSA300_2542), PMID:36806679 | 58.3 |
| A4YDT1 | M. sedula Msed_0406 4-hydroxybutyrate-CoA ligase | 40.2 |
| Q08AH3 | human ACSM2A | 36.0 |
| Q88KS6 | P. putida PP_2213 | 33.8 |

Context gathered with UniProt REST queries on the same date:

- MbcS (A0A0H2XHR6) is classified in PANTHER PTHR43605:SF10 and NCBIfam NF047394 ("acyl-CoA
  synthetase MbcS"), the same subfamily and NCBIfam family as YtcI.
- YtcI is the only PTHR43605 member and the only NF047394 member in the B. subtilis 168 reference
  proteome (UP000001570).

Interpretation: at 58% identity, sole family member in the genome and shared NCBIfam family,
YtcI is the probable B. subtilis counterpart of MbcS, the S. aureus short-chain (2-methylbutyrate,
isobutyrate) acyl-CoA synthetase that feeds branched-chain fatty acid synthesis. This is a
homology inference only; no reciprocal genome-wide search or phylogeny was run, and YtcI itself
has not been assayed.
