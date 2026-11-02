# IRC24 (P40580) vs Nre1 (P40579) — computed structural provenance

Tools/versions actually invoked (all run in-session, 2026-10-09):
- AlphaFold DB REST API `https://alphafold.ebi.ac.uk/api/prediction/{acc}` and file server `/files/AF-*-model_v6.*` — model entity AF-P40580-F1, **v6**, modelCreatedDate 2025-08-01, AlphaFold Monomer v2.0 pipeline, globalMetric (mean pLDDT) 96.38. (Seed cited v4; current DB release is v6.)
- RCSB PDB file download: 3KZV (2.00 Å, Nre1 apo; only GOL+HOH), 6UHX (2.75 Å, Nre1+NADP (NAP), chains A/B).
- In-session Python (numpy): manual PDB parser, Needleman–Wunsch (BLOSUM62), Kabsch superposition, pocket detection, crude cavity grid. **Biopython/Phenix were NOT used on the AlphaFold model**: the code-executor sandbox is ephemeral and cannot share files with the Phenix tool environment, and Biopython is not an allowed import. RCSB files are present in the job `data/` dir for optional Phenix validation.
- Foldseek web server (`https://search.foldseek.com/api`, mode 3diaa; databases afdb-swissprot, afdb50, pdb100) — query = AF-P40580-F1 v6.

## Core computed metrics
| Metric | Value |
|---|---|
| Sequence identity Irc24 vs Nre1 (6UHX-A, 253 res) | 135/253 = **53.4%** |
| CA superposition RMSD (AF Irc24 → 6UHX-A) | **1.36 Å** over 253 pairs |
| Pocket residues (≤6 Å of NADP nicotinamide) | 18 |
| Identical pocket residues | **15/18 (83%)** |
| Catalytic triad | Ser-Tyr-Lys strictly conserved (Nre1 S136/Y150/K154 = Irc24 S143/Y157/K161) |
| Mean Irc24 pLDDT over pocket residues | **96.6** (range 93.6–98.8) |
| Pocket hydrophobic fraction | Nre1 50% / Irc24 65% |
| Pocket charged residues | Nre1 4 / Irc24 1 |
| Crude enclosed-cavity volume (relative only) | Nre1 ~1016 vs Irc24 ~1061 (<5% apart) |

## Pocket residue-by-residue (within 6 Å of NADP nicotinamide, 6UHX chain A)
| Nre1 res | Nre1 aa | Irc24 res | Irc24 aa | identity | dist (Å) | Irc24 pLDDT |
|---|---|---|---|---|---|---|
| 183 | T | 192 | T | SAME | 3.1 | 95.1 |
| 186 | Q | 195 | Q | SAME | 3.1 | 95.2 |
| 150 | Y | 157 | Y | SAME (cat. Tyr) | 3.2 | 98.1 |
| 179 | G | 188 | G | SAME | 3.2 | 95.5 |
| 136 | S | 143 | S | SAME (cat. Ser) | 3.3 | 98.5 |
| 181 | V | 190 | V | SAME | 3.3 | 96.1 |
| 137 | S | 144 | S | SAME | 3.5 | 98.2 |
| 185 | M | 194 | M | SAME | 3.5 | 93.6 |
| 178 | P | 187 | P | SAME | 3.6 | 97.4 |
| 180 | I | 189 | V | DIFF (conservative) | 3.8 | 96.3 |
| 14  | I | 14  | I | SAME | 4.2 | 97.7 |
| 138 | D | 145 | G | **DIFF (non-conservative, 2nd shell)** | 4.8 | 97.2 |
| 135 | V | 142 | V | SAME | 5.0 | 98.8 |
| 154 | K | 161 | K | SAME (cat. Lys) | 5.1 | 98.7 |
| 182 | D | 191 | D | SAME | 5.3 | 95.4 |
| 189 | I | 198 | I | SAME | 5.9 | 95.7 |
| 177 | A | 186 | A | SAME | 5.9 | 98.4 |
| 184 | D | 193 | Q | DIFF (acidic→amide, rim) | 6.0 | 93.6 |

## Foldseek nearest neighbours (query AF-P40580-F1 v6, prob=1 for all listed)
**afdb-swissprot:** Nre1 (seqId 51.7) › bacterial Benzil reductases Q8RJB2/O32099 › Tropinone reductase 2 (P50163/P50164) › Sepiapterin reductase (Q64105) › Cyclopentanol/Cyclohexanol dehydrogenase › L-fucose dehydrogenase › FabG.
**pdb100:** 6UHX & 3KZV (Nre1) › **6YC8 KRED1-Pglu benzil reductase (seqId 44.9)** › FabG/oxoacyl-ACP reductases › 17β-hydroxysteroid dehydrogenase type 14 (6FFB/6H0M/6EMM/6QCK/6GTB/6G4L).

Interpretation: every nearest neighbour with a known substrate reduces a **ring/cyclic carbonyl** (diaryl, bicyclic alkaloid, pterin, alicyclic, steroid). No small aliphatic-dicarbonyl (methylglyoxal) reductase appears. → natural substrate most plausibly a ring/fused-ring carbonyl; methylglyoxal least supported. Inference from pocket + neighbour annotations, not docking.
