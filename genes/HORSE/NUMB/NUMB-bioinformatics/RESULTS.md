# NUMB (horse, A0A5F5PK46) sequence comparison

Script: `compare_sequences.py` (run with `uv run --script compare_sequences.py`);
raw output in `compare_sequences_output.txt`. Sequences were downloaded from the
UniProt REST API on 2026-10-21.

## Results

- A0A5F5PK46 is 652 aa. Human NUMB canonical isoform 1 (P49757, 651 aa) and
  mouse Numb (Q9QZS3, 653 aa) are the reference products.
- Global alignment (BLOSUM62, gap open -10, extend -0.5) against P49757 gives
  630 identical positions (identity over the reference 0.968), with only three
  single-residue indels (a 1-aa deletion after human position 223 and 1-aa
  insertions after human positions 341 and 376).
- Against mouse Q9QZS3: 614 identical positions (0.940), one 1-aa deletion.
- There is no block-sized gap, so the horse model carries both alternatively
  spliced exons of the longest NUMB isoform (the 11-aa PTB-domain insert and the
  48-aa proline-rich-region insert): it is a full-length isoform 1 (p72)
  equivalent, not a fragment or a short isoform.
- The horse sequence contains an NPF motif (position 638) and DPF motifs (343,
  615) in the C-terminal region; mammalian NUMB binds EPS15 and the alpha-adaptin
  appendage of AP-2 (Santolini et al. 2000, PMID:11121447), and these motif
  classes are the canonical EH-domain and alpha-appendage ligands, but this
  script does not test which motifs mediate binding.

## Interpretation

The horse entry is the canonical full-length NUMB product. Together with
PANTHER placement in PTHR47368:SF5 (PROTEIN NUMB HOMOLOG), the same subfamily
as human P49757, mouse Q9QZS3 and rat Q2LC84 (NUMB-like proteins NUMBL fall in
SF4), it is the 1:1 ortholog of human NUMB.
