# PPP4R4 horse canonical (A0A9L0S938) compared with human PPP4R4 (Q6NUP7)

Script: `compare_to_human.py` (run from repo root with `uv run python`). Raw output: `results.json`.
Inputs are the cached UniProt flat files for A0A9L0S938, human Q6NUP7 and horse A0A9L0S961.
Alignment: global, BLOSUM62, gap open -10, extend -0.5, free end gaps; identity over aligned pairs.

## Results

- A0A9L0S938 (869 aa) vs human Q6NUP7 (873 aa): 95.4% identity over 869 aligned pairs, covering 99.5% of human.
  Both end with the same C-terminal motif (`QPRKATLKSRKSNP`).
- A0A9L0S938 vs horse A0A9L0S961 (865 aa): 99.5% identity over 865 aligned pairs (100% of A0A9L0S961);
  the two products differ only at the extreme C-terminus (`...QPRKATLKSRKSNP` vs `...QPRKATFLNI`), consistent
  with alternative 3' splicing of one gene (both are Ensembl ENSECAG00000019485 translations).

## Evolutionary grounding

Both horse products and human PPP4R4 are classified in PANTHER PTHR21467:SF0 (UniProt DR lines), the only
subfamily of the PPP4R4 family, and A0A9L0S938 receives its IBAs from the same PAINT node (PTN001087371) as
human Q6NUP7. Together with near full-length 95% identity this supports one-to-one orthology and transfer of
the human experimental findings (PPP4C binding, cytosolic PPP4C-PPP4R4 complex) by inference only; no
experimental data exist for horse PPP4R4.
