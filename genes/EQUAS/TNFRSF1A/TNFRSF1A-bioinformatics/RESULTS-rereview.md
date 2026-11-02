# TNFRSF1A (donkey): comparison of the two gene models (re-review, 2026-10-21)

Script: `compare_isoforms_rereview.py` (run with `uv run --script compare_isoforms_rereview.py`);
raw output in `results-isoforms-rereview.json`. Sequences come from the UniProt REST API and the exon
structure from the Ensembl REST API (gene ENSEASG00005016176, donkey chromosome 22, minus strand).

## Result

- A0A9L0JKX4 (410 aa, Ensembl ENSEAST00005054546, not the Ensembl canonical transcript) is identical to
  A0A8C4MD74 (453 aa, Ensembl ENSEAST00005025834, the Ensembl canonical transcript) except for one
  contiguous block of 43 residues.
- Deleted block (A0A8C4MD74 positions 65-107): GTYLHNDCLGPGLDTDCRECENGTFTASENHLRQCLSCSKCRK
- The 410-aa transcript lacks exactly one exon of the canonical transcript: exon 3 (ENSEASE00005153555, 129 nt = 43 codons, in frame).
- Both UniProt entries map to the same Ensembl gene, so A0A9L0JKX4 is an exon-3-skipping alternative
  transcript model of TNFRSF1A, not a separate gene or a paralog.

## Interpretation

The skipped exon encodes the C-terminal half of the first cysteine-rich domain and most of the second
(the region aligned to human P19438 residues 64-106, see `RESULTS.md`). Ensembl transcript models of
this kind are computational; this analysis does not establish that the exon-3-skipped mRNA is
expressed in donkey tissues. No such isoform is listed among the five human P19438 isoforms.
