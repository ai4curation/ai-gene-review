# CV_2726 (Q7NUH2): comparison with characterized PTHR33164:SF43 members

Script: `compare_sf43_members.py` (run with `uv run compare_sf43_members.py`); raw output in `RESULTS-output.txt`.
Global Needleman-Wunsch alignment, BLOSUM62, gap open -10 / extend -0.5; identity is computed over the shorter sequence.
PANTHER placements are read live from UniProt.

## Results

| Accession | Protein | PANTHER | Identity to Q7NUH2 |
|---|---|---|---|
| P9WME9 | Rv2887, M. tuberculosis | PTHR33164:SF43 | 28.8% |
| O33817 | HcrR-like, Thauera aromatica | PTHR33164:SF43 | 27.2% |
| Q9F4G3 | TcaR, S. aureus COL | PTHR33164:SF43 | 20.4% |
| P70993 | YwhA, B. subtilis | PTHR33164:SF43 | 20.1% |
| P27245 | MarR, E. coli (outgroup) | PTHR33164:SF87 | 24.3% |
| O31541 | YetL, B. subtilis | PTHR42756:SF1 | 21.1% |

## Interpretation

- Q7NUH2 is placed in PTHR33164:SF43, which is named "HTH-TYPE TRANSCRIPTIONAL REPRESSOR YETL".
  UniProt now places B. subtilis YetL itself in a different family (PTHR42756:SF1). The subfamily name
  is therefore a historical label and says nothing about the CV_2726 ligand (YetL responds to flavonoids).
- Inside SF43, CV_2726 shares only 20-29% identity with the characterized members. That is about the same
  as its identity to E. coli MarR, which sits in a different subfamily (SF87). SF43 is a broad grouping, and
  the identities do not single out an ortholog. Rv2887 is the closest characterized SF43 member (28.8%):
  it represses the htm (Rv0560c) methyltransferase gene and is released from DNA by salicylate and
  para-aminosalicylate. At this identity, neither the regulon nor the ligand can be transferred to CV_2726.
- KEGG genomic neighbourhood: CV_2722 acyl-CoA hydrolase, CV_2723 acyl-CoA dehydrogenase, CV_2724 TetR
  regulator, CV_2725 metZ, CV_2727 conserved hypothetical protein, CV_2728 alcohol dehydrogenase, CV_2729 MarC.
  None of these clearly marks a regulon. Strand and operon structure were not analysed.
- C. violaceum OhrR (CV_0210, Q7P1K3; found by UniProt query on 2026-10-21) is placed in PTHR33164:SF5, not SF43,
  so it is a paralog in a different subfamily. Its organic-hydroperoxide-sensing role is not transferred to CV_2726.
