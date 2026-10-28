# TetH family comparison (CMMMech tetrathionate hydrolase examples)

Script: `compare_teth.py` (run `uv run python compare_teth.py > results.txt`). Raw output: `results.txt`.
Sequences are fetched live from UniProt and NCBI; alignments are Biopython global/local
Needleman-Wunsch/Smith-Waterman with BLOSUM62 (gap open -10, extend -0.5). Identity is
identical/aligned positions.

## Sequences compared

- B7J3C9, Af-Tth of A. ferrooxidans ATCC 23270 (Swiss-Prot; biochemically, structurally and genetically characterised).
- F9ZNI0, Atc_1595 of A. caldus SM-1.
- A0A060URH6, tetH of A. ferrivorans CF27 (ENA project PRJEB5721).
- A0A5P9XPU3, GCD22_00683 of A. thiooxidans ATCC 19377 (235 aa).
- Comparators: ABP38225 (A. caldus KU / ATCC 51756 TetH, the gene product studied by
  Rzhepishevska et al. 2007); A0A5P9XS05 (GCD22_02315, a second, full-length tth in the same
  A. thiooxidans ATCC 19377 genome); QFX95165 (GCD22_00682, the ORF immediately upstream of
  GCD22_00683); AEM46280 and AEM48684 (A. ferrivorans SS3 tetH1 Acife_0037 and tetH2 Acife_2602).

## Key results

1. Identity to Af-Tth (B7J3C9): F9ZNI0 58.9%, A0A060URH6 57.9%, A0A5P9XS05 58.6%, ABP38225 57.4%,
   over 97-98% of B7J3C9 in each case. These are full-length family members.
2. Orthology to characterised genes:
   - F9ZNI0 vs ABP38225 (A. caldus KU TetH): 99.2% over 503 aligned. F9ZNI0 is the SM-1 ortholog of the characterised A. caldus TetH.
   - A0A060URH6 vs AEM46280 (A. ferrivorans SS3 tetH1): 98.8% over 503 aligned; vs tetH2 (AEM48684) only 35.4%. A0A060URH6 is the tetH1 ortholog, the copy whose transcripts dominate on tetrathionate (Christel et al. 2016).
3. Catalytic acid: the residue aligned to Af-Tth Asp325 (essential, D325N inactive) is Asp in every sequence that covers it (F9ZNI0 D323, A0A060URH6 D323, A0A5P9XPU3 D212, A0A5P9XS05 D323, ABP38225 D337). Af-Tth Cys301 aligns to Ala in all of the others.
4. A0A5P9XPU3 is a fragment. The 235-aa product aligns only to the middle of Af-Tth: A0A5P9XPU3 (A. thiooxidans ATCC 19377, GCD22_00683): 140/235 = 59.6% identity; covers 47.1% of B7J3C9.
   Its N-terminus (MDGLKEALPVQTQFYGNAL...) begins inside the propeller; there is no signal peptide.
   The upstream ORF GCD22_00682 (QFX95165, 107 aa) carries a TetH-like signal-peptide N-terminus
   in another reading frame (82.2% identical to the SS3 tetH1 N-terminus). Translation of the
   locus CP045571.1:618911-622560 finds the N-terminal region in frame +2 (B7J3C9 13-105) and the
   central region in frame +0 (B7J3C9 111-349), and no segment matching the C-terminal ~150
   residues (B7J3C9 350-499) at ≥35% identity over ≥30 residues within 2 kb downstream.
   The locus therefore encodes a frame-shifted, C-terminally truncated tth copy (either a
   genuine pseudogene or an indel error in the PacBio-only assembly; this analysis cannot
   distinguish them). The same genome carries an intact 503-aa tth (A0A5P9XS05, GCD22_02315;
   83.8% identical to A0A5P9XPU3 over its 234 aligned residues), which is the appropriate
   representative of A. thiooxidans ATCC 19377 TetH.

## Limitations

Pairwise alignments only; no phylogeny. Frame analysis uses stop-free segments and a simple
identity threshold, so short or divergent C-terminal remnants could be missed. The assembly
was not re-examined at read level.
