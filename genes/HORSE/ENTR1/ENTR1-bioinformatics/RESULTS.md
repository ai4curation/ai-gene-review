# Horse ENTR1 (A0A5F5Q1J2): comparison with characterized orthologs and other horse gene models

Script: `compare_orthologs.py` (PEP 723; run with `uv run --script compare_orthologs.py`).
Sequences and PANTHER cross-references were fetched from the UniProt REST API (2026-10-21);
global alignments use BLOSUM62, gap open -10, gap extend -0.5. Raw numbers are in
`results.json`; alignments are in `alignment_*_vs_horse.txt`. The human UniProt record used
for citations is saved as `human_Q96C92-uniprot.txt`.

## PANTHER placement

| Protein | Accession | Length | PANTHER subfamily |
|---|---|---|---|
| Horse ENTR1 (target) | A0A5F5Q1J2 | 459 | PTHR31259:SF3 |
| Horse ENTR1 (other model) | F6QT44 | 448 | PTHR31259:SF3 |
| Horse ENTR1 (other model) | A0A3Q2H8N2 | 360 | PTHR31259:SF3 |
| Mouse Entr1 | A2AIW0 | 432 | PTHR31259:SF3 |
| Human ENTR1 | Q96C92 | 435 | PTHR31259:SF6 |

Horse and mouse ENTR1 are in subfamily SF3, while human ENTR1 is assigned to SF6. All are
single-copy mammalian ENTR1 genes, so the SF3/SF6 split separates one-to-one orthologs.

## Pairwise comparisons (target = A0A5F5Q1J2)

- Human Q96C92 vs horse: 409 paired residues, 85.82% identity over paired residues;
  paired coverage is 94.02% of human and 89.11% of horse.
- Mouse A2AIW0 vs horse: 406 paired residues, 82.27% identity; coverage 93.98% of mouse and
  88.45% of horse.
- Human N-terminal region 1-100 (basal-body targeting / IFT88-binding region, PMID:27767179):
  77 of 100 human residues are paired with horse residues, 64 of them identical.
- The unpaired human residues in that region are 75-97, which is the alternatively spliced
  segment missing from human isoform 2 (VSP_032177). The target model lacks the equivalent
  exon.
- The target has a 37-residue Gly/Arg-rich insertion (horse residues 24-60) with no human or
  mouse counterpart, inside the disordered N-terminal region.

## Other horse gene models of the same gene (ENSECAG00000010463)

- F6QT44 (448 aa) is identical to the target over all 410 paired residues; it lacks the 24-60
  insertion and instead contains the exon equivalent to human residues 75-97.
- A0A3Q2H8N2 (360 aa) is identical to the target over all 360 residues; it shares target
  residues 1-23 and then skips target residues 24-122, resuming at the "DDKLEDL" segment.
- Ensembl lookup (2026-10-21) marks ENSECAT00000070964 (encoding A0A5F5Q1J2) as the canonical
  transcript of ENSECAG00000010463.

## Interpretation

The target is the Ensembl-canonical product of horse ENTR1, not a fragment. Its C-terminal
ENTR1 coiled-coil region is intact and highly conserved. Relative to human isoform 1 it differs
only in the alternatively spliced N-terminal segments, and it retains most of the region that
in human mediates basal-body localization and IFT88 binding.
