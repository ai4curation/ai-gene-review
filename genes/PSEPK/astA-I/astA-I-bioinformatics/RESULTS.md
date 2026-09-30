# AstA chain comparison

Run from the repository root:

```bash
uv run python genes/PSEPK/astA-I/astA-I-bioinformatics/compare_astA_chains.py
```

The script retrieves the four current UniProt FASTA records and performs global
pairwise alignments with Biopython `PairwiseAligner`. Percent identity is the
number of identical residues divided by aligned non-gap residue pairs.

| Query | Target | Identical | Aligned residues | Identity |
|---|---|---:|---:|---:|
| PSEPK AstA-I Q88EI3 | P. aeruginosa alpha AruF P80357 | 127 | 334 | 38.0% |
| PSEPK AstA-I Q88EI3 | P. aeruginosa beta AruG P80358 | 291 | 340 | 85.6% |
| PSEPK AstA-II Q88EI2 | P. aeruginosa alpha AruF P80357 | 290 | 338 | 85.8% |
| PSEPK AstA-II Q88EI2 | P. aeruginosa beta AruG P80358 | 134 | 332 | 40.4% |

Q88EI3 is therefore beta-like and Q88EI2 is alpha-like. This agrees with the
chain-specific InterPro and NCBIfam signatures in their UniProt records. The
comparison supports chain assignment, not direct catalytic sufficiency or the
unmeasured KT2440 complex stoichiometry.
