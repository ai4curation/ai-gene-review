# A0A0K2YWP2 sequence comparison: results

Script: `compare_sequences.py` (fetches sequences live from UniProt REST; output in `results.json`).
Run: `uv run python genes/9HYPH/A0A0K2YWP2/A0A0K2YWP2-bioinformatics/compare_sequences.py`

## Records compared

| Accession | Organism / strain | Length | UniParc |
|---|---|---|---|
| A0A0K2YWP2 | Mesorhizobium australicum T-G1 (fragment, EMBL LN864498) | 54 | UPI00067A44EE |
| L0KKS2 | Mesorhizobium australicum WSM2073, locus Mesau_02205 (UP000010998) | 264 | UPI00022DFB2D |
| P33644 | Escherichia coli K-12 PgeF (Swiss-Prot) | 243 | UPI000013AEB1 |

## Findings

- The two Mesorhizobium records are NOT the same sequence: they have different UniParc identifiers
  (UPI00067A44EE vs UPI00022DFB2D) and the sequences are not identical.
- Local alignment (BLOSUM62, gap open -10, extend -0.5) places the whole 54-residue fragment on
  L0KKS2 residues 207-260 with 48/54 identical residues (88.9% identity, no gaps).
- The fragment therefore covers only the C-terminal quarter of the PgeF domain. The catalytic
  cysteine of E. coli PgeF (Cys107, PMID:40632566) aligns to L0KKS2 Cys117, which lies outside
  the fragment.
- L0KKS2 vs E. coli PgeF (global alignment): 101/236 identical aligned residues (42.8%).

## Interpretation

A0A0K2YWP2 is a partial sequence of the T-G1 ortholog of WSM2073 Mesau_02205, from a different
strain, and is not interchangeable with L0KKS2 at the sequence level. The 11% divergence over the
amplified region is consistent with strain-level divergence of an orthologous locus, but a 54-residue
fragment cannot by itself establish orthology versus paralogy; the WSM2073 genome contains a single
PgeF-family gene (Bohu et al. 2015 report "only one" such gene from a keyword search; not
independently re-verified here).
