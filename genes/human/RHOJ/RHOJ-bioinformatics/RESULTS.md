# RHOJ: exact selected product and same-gene reference

Selected G3V4H1 has 153 residues; reference Q9H4E5 has 214 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–103 | 1–103 | 103 |
| 115–115 | 104–104 | 1 |
| 121–127 | 105–111 | 3 |
| 160–181 | 112–133 | 5 |
| 182–184 | 140–142 | 2 |
| 195–201 | 143–149 | 2 |
| 205–208 | 150–153 | 1 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Motif: Effector region | 50–58 | 9 / 9 | 9 |
| Binding site:  | 31–31 | 1 / 1 | 1 |
| Binding site:  | 33–33 | 1 / 1 | 1 |
| Binding site:  | 34–34 | 1 / 1 | 1 |
| Binding site:  | 35–35 | 1 / 1 | 1 |
| Binding site:  | 35–35 | 1 / 1 | 1 |
| Binding site:  | 36–36 | 1 / 1 | 1 |
| Binding site:  | 50–50 | 1 / 1 | 1 |
| Binding site:  | 53–53 | 1 / 1 | 1 |
| Binding site:  | 53–53 | 1 / 1 | 1 |
| Binding site:  | 75–75 | 1 / 1 | 1 |
| Binding site:  | 78–78 | 1 / 1 | 1 |
| Binding site:  | 136–136 | 0 / 1 | 0 |
| Binding site:  | 177–177 | 1 / 1 | 0 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.

## Re-run 2026-10-20: target sequence read from the UniProt record

The analysis script was revised so it reads the target sequence from the gene's UniProt record rather than from the ProtNLM2 source file, and was re-run; `results.json` and related outputs now reflect this re-run. The original results above are kept unchanged for the record.

Selected G3V4H1 has 153 residues; reference Q9H4E5 has 214 residues.
Exact shared N-terminal prefix: residues 1-103; downstream sequence is divergent.

### Ensembl transcripts of ENSG00000126785

| Transcript | Name | Biotype | Canonical | Protein length |
|---|---|---|---|---|
| ENST00000316754 | RHOJ-201 | protein_coding | True | 214 |
| ENST00000555125 | RHOJ-202 | protein_coding | False | 178 |
| ENST00000557133 | RHOJ-203 | protein_coding_CDS_not_defined | False | None |
| ENST00000557447 (G3V4H1 source) | RHOJ-204 | nonsense_mediated_decay | False | 153 |
| ENST00000900057 | RHOJ-205 | protein_coding | False | 159 |
| ENST00000900058 | RHOJ-206 | protein_coding | False | 127 |
| ENST00000900059 | RHOJ-207 | protein_coding | False | 224 |
| ENST00001118000 | RHOJ-208 | nonsense_mediated_decay | False | 176 |
| ENST00001118001 | RHOJ-209 | protein_coding | False | 176 |
| ENST00001118002 | RHOJ-210 | nonsense_mediated_decay | False | 186 |
| ENST00001127201 | RHOJ-211 | nonsense_mediated_decay | False | 186 |
| ENST00001134244 | RHOJ-212 | protein_coding | False | 214 |

### G-box and CAAX motifs (1-based start positions; empty = absent)

| Motif | Q9H4E5 | G3V4H1 |
|---|---|---|
| G1 P-loop GxxxxGK[ST] | [28] | [28] |
| G3 DTAGQE | [75] | [75] |
| G4 [NT][KQ]xD | [133] | [] |
| G5 [ST]A[KL] | [176] | [] |
| CAAX box (C-terminal) | [211] | [] |

### Global alignment segments

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1-103 | 1-103 | 103 |
| 115-115 | 104-104 | 1 |
| 121-127 | 105-111 | 3 |
| 160-181 | 112-133 | 5 |
| 182-184 | 140-142 | 2 |
| 195-201 | 143-149 | 2 |
| 205-208 | 150-153 | 1 |

### Reference (Q9H4E5) feature mapping

| Feature | Interval | Within shared prefix | Mapped | Identical |
|---|---|---|---|---|
| Propeptide: Removed in mature form | 212-214 | False | 0 | 0 |
| Motif: Effector region | 50-58 | True | 9 | 9 |
| Binding site:  | 31-31 | True | 1 | 1 |
| Binding site:  | 33-33 | True | 1 | 1 |
| Binding site:  | 34-34 | True | 1 | 1 |
| Binding site:  | 35-35 | True | 1 | 1 |
| Binding site:  | 35-35 | True | 1 | 1 |
| Binding site:  | 36-36 | True | 1 | 1 |
| Binding site:  | 50-50 | True | 1 | 1 |
| Binding site:  | 53-53 | True | 1 | 1 |
| Binding site:  | 53-53 | True | 1 | 1 |
| Binding site:  | 75-75 | True | 1 | 1 |
| Binding site:  | 78-78 | True | 1 | 1 |
| Binding site:  | 136-136 | False | 0 | 0 |
| Binding site:  | 177-177 | False | 1 | 0 |
| Modified residue: Cysteine methyl ester | 211-211 | False | 0 | 0 |
| Lipidation: S-palmitoyl cysteine | 3-3 | True | 1 | 1 |
| Lipidation: S-palmitoyl cysteine | 11-11 | True | 1 | 1 |
| Lipidation: S-farnesyl cysteine | 211-211 | False | 0 | 0 |

Residues mapped downstream of the shared prefix are placed by global alignment across a non-homologous tail and should not be read as conserved features.
A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.
