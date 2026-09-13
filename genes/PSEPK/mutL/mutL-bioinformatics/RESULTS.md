# MutL pairwise identity results

## Result

The global protein alignment of Pseudomonas putida KT2440 MutL Q88DD1 and
Pseudomonas aeruginosa PAO1 MutL Q9HUL8 contains 627 aligned residue pairs, of
which 521 are identical (83.0941%). The alignment has 638 total columns because
of gap positions. Q88DD1 is 632 amino acids and Q9HUL8 is 633 amino acids.

These values come from `results/mutl_pairwise_identity.tsv`, generated with
Biopython 1.85 `PairwiseAligner` in global mode using match 2, mismatch -1,
gap-open -5, and gap-extension -0.5. The TSV records the input lengths and
SHA-256 sequence digests. The complete alignment is retained in
`results/mutl_pairwise_alignment.txt`.

The high full-length identity supports treating Q9HUL8 as a close sequence
ortholog for an ISS transfer. It does not by itself establish Q88DD1
endonuclease activity; the biochemical activity comes from PMID:23969026 and
still requires direct testing in KT2440.

## Independent script test

The same parameterized script completed on P. putida UvrD Q88C31 and E. coli
UvrD P03018. `results/uvrd_smoke_test.tsv` reports 457 identical residues among
719 aligned residue pairs (63.5605%), with the alignment retained separately.
This test checks that the script accepts a different protein pair and does not
depend on hardcoded MutL sequences or result values.

## Reproducibility checklist

- [x] Scripts take all accessions, inputs, outputs, and alignment scores as parameters.
- [x] Canonical UniProtKB FASTA inputs are retained under `data/`.
- [x] Input sequence lengths and SHA-256 digests are recorded in result TSVs.
- [x] Biopython is pinned to version 1.85 in `pyproject.toml` and `uv.lock`.
- [x] The complete MutL analysis completed as expected.
- [x] Direct TSV and alignment outputs are retained under `results/`.
- [x] The alignment script was tested on a different protein pair.
- [x] `just --justfile genes/PSEPK/mutL/mutL-bioinformatics/justfile all` reruns the workflow.
