# A0A8B8L1Z3 re-review: placement among PTHR45496 relatives (2026-10-20)

Script: `compare_sequences_rereview.py` (run with `uv run compare_sequences_rereview.py`);
raw output: `compare_sequences_rereview.out`. Relative sequences are UniProt FASTA
downloads in `relatives.fasta`.

## Subfamily placement (PANTHER 19.0 classification files)

- A0A8B8L1Z3 (Abrus precatorius LOC113860185) is in PTHR45496:SF19 "J DOMAIN-CONTAINING PROTEIN".
- The only Arabidopsis thaliana member of PTHR45496:SF19 is Q9FMF3 (At5g64360), named EIP9,
  and called DNAJ1 (Harris et al. 2018) or SDJ1 (Zhao et al. 2019).
- Its paralogs are in other subfamilies: SDJ2/DNAJ2 (At2g01710, A0A1P8B2U5) in SF1,
  SDJ3 (At1g62970, Q0WQM3) in SF10, and ADMETOS (Q9SZ59) with At4g38065 and At4g11930 in SF32.
  At5g09540 (Q9LXB9) is in SF28.
- The PAINT node PTN002896004 (taxon:3398, Magnoliopsida) has IBD seeds from members of
  SF1 (At2g01710), SF10 (At1g62970), SF19 (At5g64360) and SF32 (At4g11940, which is ADMETOS).
  It therefore sits above all of these subfamilies, and an Abrus SF19 protein descends from it.
  PAINT asserts nucleus (GO:0005634) and GO:0001228 "DNA-binding transcription activator
  activity, RNA polymerase II-specific" at this node.

## Global alignment identity to the query (BLOSUM62, gap open -10 / extend -0.5)

| Relative | Subfamily | Length | Identical residues / 474 |
|---|---|---|---|
| A0A3N7GRR1 (Populus) | SF19 | 611 | 0.536 |
| U5FLI7 (Populus) | SF19 | 614 | 0.532 |
| Q9FMF3 EIP9/SDJ1 | SF19 | 464 | 0.460 |
| Q0WQM3 SDJ3 | SF10 | 797 | 0.359 |
| A0A1P8B2U5 SDJ2 | SF1 | 355 | 0.300 |
| Q9LXB9 At5g09540 | SF28 | 280 | 0.276 |
| Q9SZ59 ADMETOS | SF32 | 264 | 0.173 |

The query is most similar to the SF19 members, as its subfamily assignment predicts.
Among Arabidopsis proteins it is closest to EIP9/SDJ1. The query (474 aa) and EIP9 (464 aa)
have similar lengths, so the query looks like a full-length product rather than a fragment.

## J-domain HPD motif

- The query's J domain (residues 70-135) has no His-Pro-Asp tripeptide. At the
  helix II-III loop it reads `...LALLLEPHRNPF...`.
- EIP9/SDJ1, SDJ3, ADMETOS and At5g09540 also lack HPD. SDJ2 is the only one of these
  that has HPD (`HPDKNR`).
- The HPD motif is needed for J-domain stimulation of Hsp70 ATPase activity, so these
  sequences do not support a canonical Hsp70-cochaperone role for the query.
- The aligned windows printed by the script are only approximate. The finding that HPD
  is absent comes from a direct substring search of each sequence.
