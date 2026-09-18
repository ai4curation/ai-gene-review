# NCU04302 E2 comparison results

The full-length target sequence is 75.0% identical to fission-yeast Ubc9 P40984 across 156 aligned residue pairs (99.36% target coverage), and 62.42% identical to human Ubc9 P63279 across 157 residue pairs (100% target coverage). It is 42.0% identical to the recorded Arabidopsis ubiquitin-E2 donor P42745 across 150 residue pairs (95.54% target coverage).

| Query | Reference | Identities / aligned residue pairs | Identity | Target coverage | Global BLOSUM62 score |
|---|---|---:|---:|---:|---:|
| Q1K772 | P40984, fission-yeast Ubc9 | 117 / 156 | 75.00% | 99.36% | 650.0 |
| Q1K772 | P63279, human Ubc9 | 98 / 157 | 62.42% | 100.00% | 550.0 |
| Q1K772 | P42745, Arabidopsis UBC2 | 63 / 150 | 42.00% | 95.54% | 323.5 |

These complete-sequence relationships support the Ubc9 assignment in combination with the curated PAINT placement and conserved catalytic UBC architecture. Characterized Ubc9 enzymes use SUMO (PMID:9435231); the fission-yeast reference has direct SUMO-conjugation genetics (PMID:12597774). The much broader E2 fold also encompasses ubiquitin E2s, explaining why a homologous donor does not justify retaining its modifier specificity. This is a targeted reference comparison, not an exhaustive subfamily tree, a prediction of kinetic constants, or proof of prediction-time sequence identity.

The alternative-query test used P42745: it produced 100% identity and full coverage against itself, 39.74% identity to P63279 and 41.33% to P40984. Those results are preserved in control-alignments.json. No biological conclusions are encoded in the analysis script.

## Reproducibility checklist

- [x] Scripts accept external inputs and contain no hardcoded sequence results or biological verdicts.
- [x] Tested on a second query, P42745, including an exact self-alignment control.
- [x] Analyses completed successfully using pinned Biopython 1.85.
- [x] Complete alignments, scores, identities, coverages and sequence hashes are preserved in JSON.
- [x] Reference accession provenance, algorithm parameters and limitations are documented in README.md.
