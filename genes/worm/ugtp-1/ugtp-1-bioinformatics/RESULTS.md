# ugtp-1 bioinformatics: is there a CMP-sialic acid pathway in C. elegans?

Question: GOA carries IBA annotations transferring CMP-N-acetylneuraminate (CMP-sialic acid)
transmembrane transport to UGTP-1 from the SLC35A1 node PTN008496232. That function is only
meaningful if the organism makes CMP-sialic acid.

Method: `sialic_pathway_check.py` (stdlib only; run with `python3 -I sialic_pathway_check.py`)
counts UniProtKB entries carrying the EC numbers of sialic-acid biosynthesis and use, for
C. elegans (taxon 6239), with human and Drosophila as positive controls. Raw output: `results.tsv`
(run 2026-10-28).

## Results

| EC | Enzyme | C. elegans | Human | Drosophila |
|---|---|---|---|---|
| 2.5.1.57 | Neu5Ac-9-phosphate synthase (NANS) | 0 | 6 | 1 |
| 2.7.7.43 | CMP-Neu5Ac synthetase (CMAS) | 0 | 8 | 1 |
| 2.4.3.1 | alpha-2,6-sialyltransferase | 0 | 7 | 5 |
| 2.4.3.4 | alpha-2,3-sialyltransferase | 0 | 22 | 0 |

C. elegans has no UniProtKB entry with any of these activities, while both controls do;
in particular no CMP-sialic acid synthetase was found in C. elegans.

## Interpretation

No CMP-sialic acid synthetase and no sialyltransferase are annotated for C. elegans, so the worm
apparently cannot make or use CMP-sialic acid. CMP-sialic acid transport is therefore unlikely to
be a physiological function of UGTP-1, even though UGTP-1 belongs to the SLC35A subfamily that
includes the mammalian CMP-sialic acid transporter SLC35A1. The test rests on annotation, not on
a genome-wide homology search, so an unannotated divergent enzyme cannot be excluded.
