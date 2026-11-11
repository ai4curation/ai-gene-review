# merA (Q3SJ73) vs Tn501 MerA (P00392): conservation of catalytic landmarks

Script: `compare_tn501.py` (Biopython global alignment, BLOSUM62, gap open -10 / extend -0.5;
sequences fetched live from UniProt REST). Rerun the script to reproduce the output.

## Results

- Q3SJ73 is 541 aa; Tn501 MerA (P00392), the biochemically characterised reference enzyme, is 561 aa.
- Global alignment: 539 aligned positions, 330 identical (61.2% identity over aligned positions).
- Against the two non-MerA PTHR43014 subfamily representatives in the committed family entry list,
  Q3SJ73 is far more distant than it is from Tn501 MerA:
  - P9WHH7 (M. tuberculosis LpdA, PTHR43014:SF1; the IBD seed for GO:0003955): 493 aa, 456 aligned
    positions, 152 identical (33.3%).
  - P77212 (E. coli RclA, PTHR43014:SF4): 441 aa, 435 aligned positions, 140 identical (32.2%).
- Every Tn501 catalytic landmark located by anchored motif or position aligns to a cysteine in Q3SJ73:
  - NmerA GMTCxxC motif: P00392 C11 and C14 align to Q3SJ73 C13 and C16 (Q3SJ73 has one N-terminal HMA repeat, GMTCDHC).
  - Redox-active disulfide: P00392 C136 and C141 align to Q3SJ73 C117 and C122 (Q3SJ73 motif CVNVGC).
  - MerA-specific C-terminal cysteine pair: P00392 C558 and C559 align to Q3SJ73 C538 and C539 (Q3SJ73 C-terminus ...SCCAG).

## Interpretation

Q3SJ73 keeps all three cysteine sets that the Tn501 work showed are needed for Hg(II) handling and
reduction, including the C-terminal pair that distinguishes MerA from other class-I pyridine
nucleotide-disulfide oxidoreductases. This supports assigning Q3SJ73 to the true mercuric reductase
clade rather than to a paralogous family member, and the identity gap quantifies it: 61.2% to the
characterised MerA against 33.3% to the SF1 quinone reductase that seeds the GO:0003955 IBD and 32.2%
to the SF4 RclA representative. It is sequence evidence only: no activity, expression or phenotype has
been measured for this protein.
