# TYW1B vs TYW1: conservation of cofactor-binding motifs

Script: `compare_paralogs.py` (run from the repo root with
`uv run python genes/human/TYW1B/TYW1B-bioinformatics/compare_paralogs.py`).
Raw output: `compare_paralogs.out`.

Inputs: canonical sequences of human TYW1 (Q9NV66, 732 aa) and TYW1B (Q6NUM6, 668 aa)
parsed from the UniProt flat files in the gene folders; yeast Tyw1 (Q08960) and
Pyrococcus abyssi Taw1 (Q9V1F9) downloaded from the UniProt REST API. Global
Needleman-Wunsch alignment, BLOSUM62, gap open -10, extend -0.5 (Biopython PairwiseAligner).

## Results

- TYW1 vs TYW1B: 639/668 aligned positions identical (95.7%). TYW1 vs yeast Tyw1: 46.9%
  identity over the aligned region; TYW1B vs yeast Tyw1: 45.1%.
- TYW1 segments without a TYW1B counterpart: 46-91, 368-377, 390-395.
- Flavodoxin domain: TYW1 residues 85-89 (SQTGT, a UniProt FMN-binding feature that
  corresponds to the flavodoxin phosphate-binding loop) fall inside the TYW1 segment 46-91
  that is absent from canonical TYW1B. The UniProt TYW1B FMN feature at 43-47 (EMQGF)
  therefore does not correspond to the TYW1 FMN loop in this alignment. The second FMN
  region (TYW1 176-208) is retained in TYW1B (130-162) with one substitution (A204V in
  TYW1 numbering).
- Radical SAM cluster: the CX3CX2C cysteines (TYW1 C416/C420/C423) are retained in
  TYW1B (C352/C356/C359).
- Auxiliary cluster: P. abyssi Taw1 Cys45/Cys58/Cys71 (UniProt/HAMAP auxiliary
  [4Fe-4S] ligands; two clusters shown experimentally in PMID:23043105) align to TYW1
  C381/C394/C407, all three conserved in yeast Tyw1. In TYW1B, C381 aligns to P325 and
  C394 has no counterpart; only C407 (TYW1B C343) is retained. TYW1B residues 322-338
  (VDAPRERSLLQTHILWN) replace TYW1 GYQLIGSHSGVKLCRWT. This replacement is 15/17 identical
  to the alternative segment of TYW1 isoform 2 (UniProt VSP_024066, VHAPRERRLLQTHILWN,
  after which TYW1 isoform 2 truncates), so canonical TYW1B appears to use the
  counterpart of that alternative exon.
- Of the eight TYW1 cysteines conserved in yeast Tyw1, two (C381, C394) are lost in TYW1B.

## Interpretation (inference, not experiment)

Canonical TYW1B lacks the flavodoxin phosphate-binding loop and two of the three
cysteines that coordinate the auxiliary [4Fe-4S] cluster, which binds pyruvate in the
archaeal enzyme. On this sequence evidence alone, canonical TYW1B is not expected to
have the full tRNA 4-demethylwyosine synthase activity of TYW1. The analysis covers only
the canonical UniProt isoform; whether another TYW1B transcript keeps the TYW1-like exons
was not assessed.
