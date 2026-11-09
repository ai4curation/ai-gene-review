# Hmd (Q58194) versus P5C reductases: pairwise sequence check

Script: `compare_p5cr.py` (run with `uv run python genes/METJA/hmd/hmd-bioinformatics/compare_p5cr.py`);
raw output in `output.txt`. Sequences are fetched live from UniProt REST.

## Question

PANTHER places Q58194 in PTHR11645:SF0 (pyrroline-5-carboxylate reductase 3), and PAINT
node PTN000182176 gives it P5C reductase activity and L-proline biosynthesis by IBA. Is the
sequence relationship to the characterised P5C reductases strong enough to carry residue-level
claims, and does Hmd keep the P5CR nucleotide motif?

## Results (from output.txt)

| comparator | SW local score | z vs 100 shuffles | global identity (shuffled baseline) |
|---|---|---|---|
| O27211 Hmd, M. thermautotrophicus | 1143 | 174.9 | 66.9% (29.4%) |
| P0A9L8 ProC, E. coli | 46 | 1.9 | 30.6% (28.2%) |
| P32263 PRO3, S. cerevisiae | 40 | 0.6 | 30.6% (29.5%) |
| P32322 PYCR1, human | 52 | 3.1 | 27.2% (27.9%) |
| Q53H96 PYCR3, human | 62 | 5.6 | 26.5% (27.5%) |

- Hmd versus Hmd is unmistakable (z about 175); Hmd versus every P5C reductase is at or near
  the shuffled-sequence background (z 0.6 to 5.6, global identity within 3 points of the
  shuffled baseline). Any relationship is below what pairwise alignment detects; PANTHER's
  HMM-based placement must rest on remote, profile-level (fold) similarity.
- The four P5C reductases each have a [GA]x[GA]xx[GA] dinucleotide-binding-like motif in their
  first 40 residues (GCGNMG, GCGVMG, GAGQLA, GAGRMA). Hmd has no such motif there (its
  N-terminus reads MKIAILGAGCYRTH...).
- Residue 176 of Q58194 is Cys (the FeGP iron ligand). Because the P5CR alignments are at
  background, the residues they place opposite Cys176 (none, Cys131, Ala97, Ala103) are not
  meaningful homologous positions.

## Interpretation and limits

Pairwise alignment cannot show shared catalytic residues between Hmd and P5C reductases,
because it cannot align them reliably at all. This is a two-hour sanity check, not a
phylogeny: it does not test PANTHER's HMM or tree, and a profile or structure comparison could
still detect the remote Rossmann-fold relationship the literature describes.
