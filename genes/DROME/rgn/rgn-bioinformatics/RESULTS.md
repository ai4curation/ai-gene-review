# rgn (M9PFV8) architecture and family-placement checks

Script: `rgn_architecture.py` (run with `uv run --script rgn_architecture.py > rgn_architecture_results.json`).
Raw output: `rgn_architecture_results.json`. Sequences are fetched live from UniProt REST.

## Questions

1. Does Rgn carry the determinants that make TGN38/TGOLN2 (the PAINT seeds of PANTHER:PTN000575073) a trans-Golgi network resident: a single transmembrane segment and a cytoplasmic tyrosine sorting motif (SDYQRL)?
2. Is there detectable pairwise similarity between Rgn and the TGN38/TGOLN2 seeds, compared with the C-type lectins (REG1A, REG3A, fly lectin-galC1) that sit in a different PANTHER family (PTHR22803)?
3. Does the Rgn CTLD retain canonical sugar/Ca2+-binding motifs (EPN or QPD, and WND)?

## Methods

- Kyte-Doolittle hydropathy, window 19, threshold 1.6, ignoring the first 30 residues (signal peptide region).
- C-terminal YxxPhi motif search in the last 40 residues.
- Local Smith-Waterman alignment (BLOSUM62, gap open -10, extend -0.5) of M9PFV8 against each comparator, with a composition-preserving control: each comparator was shuffled 200 times (seed 7227) and realigned.
- Motif search within the PROSITE PS50041 CTLD span (residues 70-199).

## Results

| Comparator | PANTHER | TM-like segment | C-terminal YxxPhi | Local score vs Rgn | Max shuffled score | Fraction of shuffles >= real |
|---|---|---|---|---|---|---|
| TGOLN2 human O43493 | PTHR23211:SF0 (PAINT seed) | 381-404 | YQRL | 95.0 | 129.0 | 0.345 |
| Ttgn1/TGN38 rat P19814 | PTHR23211:SF0 (PAINT seed) | 301-324 | YQRL | 79.5 | 98.0 | 0.12 |
| REG1A human P05451 | PTHR22803 | none | none | 161.0 | 72.5 | 0.0 |
| REG3A human Q06141 | PTHR22803 | none | none | 101.0 | 65.0 | 0.0 |
| lectin-galC1 fly Q9VIX1 | PTHR22803 | none | none | 81.0 | 70.5 | 0.0 |

Rgn itself (M9PFV8, 808 aa; and isoform Q9Y102, 800 aa) has no TM-like segment after the signal peptide and no C-terminal YxxPhi motif.

The best local alignments of Rgn to TGOLN2 (Rgn residues 278-753) and TGN38 (Rgn residues 258-493) fall in the charged, low-complexity region that MobiDB-lite marks as disordered, and their scores are within the range of composition-matched shuffled sequences. Rgn similarity to the PTHR22803 C-type lectins maps to the Rgn CTLD (residues ~43-201) and exceeds every shuffled control.

CTLD (70-199): cysteines at 74, 91, 174, 190 and 198. EPN absent; QPD absent; WND absent.

Isoforms: Q9Y102 (isoform A/D) is identical to M9PFV8 (isoform B/C) except that it lacks 8 residues (YVQLISNS) inside the CTLD, near residue 160 of M9PFV8.

## Interpretation

- Rgn lacks both the transmembrane anchor and the cytoplasmic YQRL sorting signal that underlie TGN38/TGOLN2 residence and recycling to the trans-Golgi network. The trans-Golgi network localization asserted at PANTHER:PTN000575073 therefore has no structural basis in Rgn.
- Pairwise similarity between Rgn and the TGN38/TGOLN2 seeds is not distinguishable from composition-matched shuffles, so this analysis gives no support for the PTHR23211 grouping beyond shared compositional bias. This is a pairwise test, not a phylogeny; it cannot exclude a remote relationship, but it means no residue-level conservation with the seeds was detected.
- The CTLD is detectably related to REG-family and other C-type lectins, but lacks the EPN/QPD and WND motifs used for Ca2+-dependent sugar binding in canonical CTLDs, consistent with the UniProt PROSITE-ProRule caution that conserved residues are missing. Carbohydrate binding is therefore not predicted from motif conservation.
