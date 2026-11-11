# NCU02539 (Q7SHS5) re-review sequence analysis

Date: 2026-10-21. Script: `compare_mcm4_rereview.py` (run with `uv run --script compare_mcm4_rereview.py`);
raw output: `results_rereview.txt`. Sequences were fetched live from UniProt REST.

## Method

Global pairwise alignment (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5) of the
target against three experimentally studied Mcm4 orthologs, plus regular-expression searches for MCM
motor motifs in each sequence: Walker A (`G[DN]P[GS].[AST]KS`), Walker B
(`[ILV][ACILMV][ACILMV][ACILMV]DE[FLM][DN]K`), the SRF arginine-finger region (`SRF[DE]`), and an
N-terminal C4 zinc finger (`C..C.{10,40}C..C`).

## Results

| Protein | Length | Identity over aligned | Coverage of ortholog | Walker A | Walker B | SRF |
|---|---|---|---|---|---|---|
| Q7SHS5 N. crassa NCU02539 | 1013 | - | - | 645 GDPSTSKS | 705 VCCIDEFDK | 777 SRFD |
| P30665 S. cerevisiae MCM4 | 933 | 0.558 | 0.971 | 568 GDPSTSKS | 628 VCCIDEFDK | 700 SRFD |
| P29458 S. pombe cdc21/Mcm4 | 911 | 0.593 | 0.976 | 545 GDPSTSKS | 605 ICCIDEFDK | 677 SRFD |
| P33991 H. sapiens MCM4 | 863 | 0.490 | 0.981 | 510 GDPGTSKS | 570 ICCIDEFDK | 642 SRFD |

The target Walker A motif GDPSTSKS at residues 645-652 is identical to that of both yeast Mcm4
proteins, and the Walker B and SRF arginine-finger motifs are also conserved.

The UniProt Walker A and Walker B MOTIF features (662-669 and 726-729) are misplaced. Those
coordinates contain APRGVYTS and MEQQ, not nucleotide-binding motifs. The real motifs lie about 17-21
residues upstream. This matches the record's PROSITE-ProRule caution that conserved residues needed to
propagate feature annotation are missing. The caution is a feature-placement artefact and does not
indicate loss of the ATPase.

None of the three fungal Mcm4 proteins (target, S. cerevisiae, S. pombe) contains a canonical C4
zinc-finger pattern; each has a single CxxC (target 423 CSVC). Human MCM4 has a C4 pattern
(306-331). So the absence of a canonical zinc finger in the target is shared with characterised fungal
Mcm4 proteins and is not a target-specific defect.

## Identity conclusion

Q7SHS5 is a full-length Mcm4. Alignment covers 97-98% of each characterised ortholog, the target has
an extra ~80 residues at the N-terminus (residues 1-162 are predicted disordered by MobiDB-lite), and
all AAA+ motor motifs are present. It is not a fragment or an alternative gene model.
