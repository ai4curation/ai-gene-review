# BCAT2 (horse A0A9L0TSN4): gene-model re-review

Global alignments to human O15382 (392 aa; free end gaps; match 2, mismatch -1,
open -10, extend -0.5). Site columns give target/human residue. Reproduce with
`uv run python genes/HORSE/BCAT2/BCAT2-bioinformatics/compare_models_rereview.py`.

| model | group | length | identity % | human coverage % | N-terminal residues before human Met1 | human positions unaligned |
|---|---|---|---|---|---|---|
| A0A3Q2HXS7 | uniprot_horse | 427 | 83.38 | 93.62 | 59 | 9-33 |
| A0A5F5PUM8 | uniprot_horse | 300 | 82.67 | 76.53 | None | 1-92 |
| A0A9L0TSN4 | uniprot_horse | 452 | 83.42 | 100.0 | 59 | none |
| F7B9V7 | uniprot_horse | 405 | 80.87 | 100.0 | 0 | none |
| ENSECAP00000009482.3 | ensembl_horse | 405 | 80.87 | 100.0 | 0 | none |
| ENSECAP00000078936.1 | ensembl_horse | 427 | 83.38 | 93.62 | 59 | 353-377 |
| ENSECAP00000051992.2 | ensembl_horse | 300 | 82.67 | 76.53 | None | 1-92 |
| ENSECAP00000038196.2 | ensembl_horse | 427 | 83.38 | 93.62 | 59 | 9-33 |
| ENSECAP00000057595.1 | ensembl_horse | 480 | 83.42 | 100.0 | 59 | none |
| ENSECAP00000090181.1 | ensembl_horse | 452 | 83.42 | 100.0 | 59 | none |
| O35854 | reviewed_ortholog | 393 | 81.38 | 100.0 | 0 | none |
| O35855 | reviewed_ortholog | 393 | 83.67 | 100.0 | 0 | none |
| Q5EA40 | reviewed_ortholog | 393 | 84.18 | 100.0 | 0 | none |

## Conserved catalytic and substrate residues (target/human)

| model | PLP Schiff-base Lys (MOD_RES 229) | CXXC Cys1 (mature C315) | CXXC Cys2 (mature C318) | substrate BINDING 126 | substrate BINDING 168 | substrate BINDING 234 | substrate BINDING 296 | substrate BINDING 297 | substrate BINDING 340 |
|---|---|---|---|---|---|---|---|---|---|
| A0A3Q2HXS7 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | V/V | V/V | T/T |
| A0A5F5PUM8 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | V/V | V/V | T/T |
| A0A9L0TSN4 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | V/V | V/V | T/T |
| F7B9V7 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | V/V | V/V | T/T |
| ENSECAP00000009482.3 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | V/V | V/V | T/T |
| ENSECAP00000078936.1 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | V/V | V/V | T/T |
| ENSECAP00000051992.2 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | V/V | V/V | T/T |
| ENSECAP00000038196.2 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | V/V | V/V | T/T |
| ENSECAP00000057595.1 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | V/V | V/V | T/T |
| ENSECAP00000090181.1 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | V/V | V/V | T/T |
| O35854 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | V/V | V/V | T/T |
| O35855 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | V/V | V/V | T/T |
| Q5EA40 | K/K | C/C | C/C | R/R | Y/Y | Y/Y | I/V | V/V | T/T |

## Benchmark N-terminal extension

A0A9L0TSN4 residues 1-59 (upstream of Met60): `MRSAAEPGPGQAPYNWGGRARLGGRAGGHPAGGAVSGAWPGRLSSGPRPGRGQLPATST` (Gly 15, Arg 7, Pro 8, Asp+Glu 1).
First 20 residues found in reviewed orthologs: none.
First 20 residues found in horse models: A0A3Q2HXS7, A0A9L0TSN4, ENSECAP00000078936.1, ENSECAP00000038196.2, ENSECAP00000057595.1, ENSECAP00000090181.1.

## Benchmark body from Met60

A0A9L0TSN4 residues 60-452 (393 aa) begin at the Met aligned to human Met1. Identical horse models: none. C-terminal 12 residues: benchmark `YGTGAHEWMFPV`; orthologs O15382 `YGIRAHEWMFPV`, O35854 `YGTSAHDWMLRV`, O35855 `YGASAHDWMFRV`, Q5EA40 `YGSKAHEWMLPV`.
