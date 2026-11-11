# A0A444Z7V7 (peanut Ahy_B05g078721): placement among CSLD and CESA proteins

Script: `csld_placement.py` (run with `uv run csld_placement.py`). Sequences are downloaded
from UniProt REST, aligned with MAFFT `--auto`, and a neighbour-joining tree is built from
identity distances (Biopython). Raw output: `csld_placement.txt`; tree: `csld_tree.nwk`.

## Question

UniProt places A0A444Z7V7 in PANTHER PTHR13301 with no subfamily assignment, and the InterPro
API also returns PTHR13301 without a subfamily. Which CSLD clade does the protein belong to,
and which characterised protein is its closest phylogenetic relative?

## Results

- The target is full length: 1139 aa, compared with 1145 aa for Arabidopsis CSLD2 and CSLD3.
  Aligned coverage against AtCSLD3 is 1131 columns.
- Pairwise identity: AtCSLD3/KJK (Q9M9M4) 0.858; AtCSLD2 (Q9LFL0) 0.852; OsCSLD2 0.832;
  OsCSLD1 0.795; AtCSLD4 0.740; the other CSLDs 0.64-0.70; AtCESA1/AtCESA6 about 0.49.
- NJ tree, rooted on AtCESA1: the target groups with the AtCSLD2 + AtCSLD3 pair, then with
  OsCSLD2 and OsCSLD1. The CSLD clade is separated from CESA1/CESA6 by a long branch.
  The target therefore belongs to the angiosperm CSLD2/CSLD3 clade. Within that clade the tree
  cannot tell whether it is an ortholog of CSLD2 or of CSLD3. The Arabidopsis pair looks like
  a Brassicaceae-lineage duplication, which would make the peanut protein a co-ortholog of both.
- The residues annotated by PIRSR in the target are identical in every CSLD and in both CESAs:
  catalytic D410 and D842, metal-binding D627, and nucleotide-sugar-binding S374, K380, E381
  and K602/K603. The single QxxRW motif (QVLRW, positions 880-884), which processive GT2
  beta-glycan synthases need, is present.

## Interpretation

- The closest experimentally characterised relative, chosen by phylogenetic placement, is
  Arabidopsis CSLD3/KOJAK (Q9M9M4). AtCSLD2 is equally close. CSLD3 has the biochemical
  evidence: it is a UDP-glucose-dependent beta-1,4-glucan synthase (PMID:32169960,
  PMID:21765420).
- The catalytic machinery is intact, so the target has no pseudo-enzyme signature.
- This NJ identity tree is a quick placement check, not a maximum-likelihood phylogeny.
  It supports clade membership but does not support claims about which paralog duplicated when.
