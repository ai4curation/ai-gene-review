# Q6YYC5 re-review sequence comparison (2026-10-20)

Script: `compare_sequences_rereview.py` (raw output in `compare_sequences_rereview.out`).
Sequences fetched live from UniProt REST; global alignment, BLOSUM62, gap open -10 / extend -0.5.
PANTHER subfamily placements are taken from `interpro/panther/PTHR45751/PTHR45751-entries.csv`
and the Q6YYC5 UniProt record, not from this script.

## Output

```
Target length 401 N-term MGGVIGAL
Target RING-region C/H residues: [(356, 'C'), (359, 'C'), (370, 'C'), (372, 'H'), (374, 'C'), (375, 'C'), (378, 'C'), (385, 'C'), (388, 'C')]
Q6YYC5	rice Os08g0135400 (target, PTHR45751:SF16)	len=401	identity_vs_target=1.000	N-term=MGGVIGAL	MG_start=True	RING_CH_conserved=9/9
Q9SAL0	AtRGLG4 AT1G79380 (PTHR45751:SF16)	len=401	identity_vs_target=0.601	N-term=MTMGNFLK	MG_start=False	RING_CH_conserved=8/9
Q8RX26	AtRGLG3 AT5G63970	len=367	identity_vs_target=0.536	N-term=MNMSNKRN	MG_start=False	RING_CH_conserved=8/9
Q9SS90	AtRGLG1 AT3G01650 (SF15)	len=489	identity_vs_target=0.584	N-term=MGGGNSKE	MG_start=True	RING_CH_conserved=8/9
Q9LY87	AtRGLG2 AT5G14420 (SF29)	len=468	identity_vs_target=0.603	N-term=MGTGNSKE	MG_start=True	RING_CH_conserved=8/9
Q8LB88	AtRGLG5 (SF30)	len=433	identity_vs_target=0.601	N-term=MGGSSSKE	MG_start=True	RING_CH_conserved=8/9
```

## Interpretation

- Global identity of Q6YYC5 to every Arabidopsis RGLG paralog is similar (about 54-60%), so
  pairwise identity alone does not identify the ortholog. The orthology call rests on PANTHER:
  Q6YYC5 and AtRGLG4 (Q9SAL0) are both placed in subfamily PTHR45751:SF16 (E3 UBIQUITIN-PROTEIN
  LIGASE RGLG4), while AtRGLG1, AtRGLG2 and AtRGLG5 sit in SF15, SF29 and SF30. Both proteins are
  401 residues long. (The repo entries table lists AtRGLG3 Q8RX26 under SF11, which is unexpected for
  the near-paralog of RGLG4 and was not adjudicated here.)
- The cysteine/histidine residues of the Q6YYC5 RING region (residues 356-389) are conserved in
  all Arabidopsis RGLGs at 8 of 9 positions, consistent with an intact RING zinc-binding module.
- Q6YYC5 begins Met-Gly (MGGVIG...), but residue 6 is Gly, not the Ser/Thr found in the
  myristoylated AtRGLG1 (MGGGNSKE) and AtRGLG2 (MGTGNSKE). The N-terminus therefore does not match
  the canonical N-myristoylation consensus, and plasma-membrane anchoring cannot be inferred from it.
  AtRGLG4 and AtRGLG3, the closest relatives, lack an N-terminal Gly altogether.
