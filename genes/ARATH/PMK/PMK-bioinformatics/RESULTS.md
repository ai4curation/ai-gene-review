# Peroxisomal targeting-signal scan: Arabidopsis MK, PMK, MVD1, MVD2

Script: `targeting_signals.py` (downloads sequences from UniProt at run time; raw
output in `RESULTS-raw.txt`, run 2026-11-18). Run with the project's shared Python
(Biopython 1.85): `python -I targeting_signals.py > RESULTS-raw.txt`.

Motif definitions used by the script: PTS1 is a C-terminal tripeptide matching
`[SACPG][KRHNQS][LMIVY]`; PTS2 is `[RK][LVIQ]x5[HQ][LAF]` in residues 1-60, the
consensus quoted for plant PTS2 nonapeptides.

## Findings

1. No PTS1 on any of the four proteins. C-terminal tripeptides: MK ICY, PMK HLE,
   MVD1 LPK, MVD2 LPK.
2. The segments UniProt annotates as "Peroxisomal targeting signal PTS2" do not match
   the PTS2 consensus: PMK 57-65 DVKLTSPQL, MVD1 40-48 SVTLDPDHL, MVD2 40-48
   SVTLDPDHL. Neither PMK nor MVD1/MVD2 has any PTS2-consensus match in residues 1-60.
3. The MVD1/MVD2 segment is conserved catalytic-domain sequence: it aligns to
   SVTLHQDQL in human MVD (P53602) and SVTLSQDDL in yeast MVD1 (P32377), both 67%
   identical over the nine residues. Human and yeast MVD are cytosolic. The segment
   overlaps a beta-strand of the MVD1 crystal structure (UniProt FT STRAND 38..43,
   PDB 6N10), so it is not an exposed N-terminal extension.
4. The PMK segment falls in a lineage-specific insertion: the global alignment to yeast
   ERG8 (P24521) places residues 57-65 entirely opposite gaps.
5. MK, which is cytosolic by YFP, has a PTS2-consensus match (KIILAGEHA, 10-18) in the
   conserved GHMP N-terminal glycine-rich region; human MVK has the equivalent
   KVILHGEHA (13-21). A consensus match in this conserved region is not by itself a
   targeting signal.

## Interpretation and limits

- The sequence analysis neither confirms nor refutes peroxisomal import. It shows only
  that the annotated motifs are not canonical PTS2s, so the YFP-fusion experiments
  (PMID:21655959) remain the only evidence for peroxisomal PMK and MVD in Arabidopsis.
  Import by a non-canonical signal, or piggy-back import with a PTS-bearing partner,
  would not be detected by a motif scan.
- Global identity is computed over the shorter sequence from a single BLOSUM62 global
  alignment (gap open -10, extend -0.5); it is a rough measure.
