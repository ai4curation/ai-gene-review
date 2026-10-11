# Y56A3A.16 (RUB-1) domain architecture vs Rubicon / Pacer

Reproduce: `uv run python domain_architecture.py` (fetches sequences from UniProt REST and
domain coordinates from the InterPro API live; outputs `results/*.tsv`; console log saved in
`results/summary.txt`). Alignments: Biopython PairwiseAligner, BLOSUM62, gap open -11 / extend -1.
Run date of the saved results: 2026-10-10.

## Domain architecture (InterPro member-database hits)

| Protein | Length | RUN domain | PIKBD (PF21054) | RH domain (PF13901/SM01175) |
|---|---|---|---|---|
| human RUBCN Q92622 | 972 | 18-190 | 487-698 | 737-939 |
| human RUBCNL/Pacer Q9H714 | 662 | none | 202-411 | 450-651 |
| fly Rubicon Q9W3C9 | 827 | 50-207 | 458-483, 514-579 | 619-826 |
| worm Y56A3A.16 G2HK09 | 597 | none | none | 365-582 |
| worm Y56A3A.16 G2HK08 (alt isoform) | 595 | none | none | 365-580 |

The fly protein has the full vertebrate-Rubicon architecture (N-terminal RUN, PI3K-binding
PIKBD region, C-terminal RH). The worm protein has only the C-terminal RH domain; neither
worm isoform in UniProt carries a detectable RUN or PIKBD region.

## RUN-domain search in the worm N-terminus

Smith-Waterman scores of worm residues 1-364 against the RUN domains of human RUBCN and fly
Rubicon were indistinguishable from 200 shuffled-sequence controls (z = -0.04 and 1.31).
No divergent RUN domain is detectable by this simple test (a profile/structure search would
be more sensitive; absence here is not proof of absence).

## Sequence identity (local alignment)

| Pair | RH identity | RH score | Full-length identity (cols) | Full score |
|---|---|---|---|---|
| RUBCN vs Pacer | 56.4% | 663 | 38.0% (632) | 925 |
| RUBCN vs fly | 40.7% | 414 | 34.4% (733) | 724 |
| Pacer vs fly | 38.7% | 404 | 40.1% (257) | 524 |
| RUBCN vs worm | 32.2% | 273 | 31.1% (238) | 295 |
| Pacer vs worm | 32.3% | 283 | 32.6% (239) | 305 |
| fly vs worm | 32.7% | 253 | 31.4% (245) | 281 |

## Interpretation

- Fly Rubicon aligns over most of its length with human RUBCN (733 columns, highest full-length
  score among fly comparisons) and shares the RUN domain that RUBCN uses to bind/inhibit VPS34
  and that Pacer lacks; architecturally it is Rubicon-like, consistent with it being the single
  pre-duplication member of the family in insects.
- Worm Y56A3A.16 is a divergent family member: only the RH domain is recognisable, and it is
  roughly equidistant (~32% identity) from RUBCN, Pacer and fly Rubicon. Sequence alone
  cannot assign it to the Rubicon or Pacer side; PANTHER places it in subfamily SF1 with
  invertebrate Rubicon (UniProt cross-reference `DR   PANTHER; PTHR45971:SF1` in both
  `genes/worm/Y56A3A.16/Y56A3A.16-uniprot.txt` and `genes/DROME/Rubicon/Rubicon-uniprot.txt`). Its RH domain has fewer cysteines (13) than the RH domains of the other
  three proteins (17-18), so some zinc-coordinating positions may not be conserved (not
  examined residue-by-residue here).
- Functional assignment therefore has to rest on experiments (Nakamura et al. 2019,
  PMID:30783089), which found RNAi of Y56A3A.16 increases autophagy, i.e. Rubicon-like
  negative regulation.
