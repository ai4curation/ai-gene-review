# merA (Q3SJ73) vs Tn501 MerA (P00392): conservation of catalytic landmarks

Script: `compare_tn501.py` (Biopython global alignment, BLOSUM62, gap open -10 / extend -0.5;
sequences fetched live from UniProt REST). Rerun the script to reproduce the output.

## Results

- Q3SJ73 is 541 aa; Tn501 MerA (P00392), the biochemically characterised reference enzyme, is 561 aa.
- Global alignment: 539 aligned positions, 330 identical (61.2% identity over aligned positions).
- Every Tn501 catalytic landmark located by motif or position aligns to a cysteine in Q3SJ73:
  - NmerA GMTCxxC motif: P00392 C11 and C14 align to Q3SJ73 C13 and C16 (Q3SJ73 has one N-terminal HMA repeat, GMTCDHC).
  - Redox-active disulfide: P00392 C136 and C141 align to Q3SJ73 C117 and C122 (Q3SJ73 motif CVNVGC).
  - MerA-specific C-terminal cysteine pair: P00392 C558 and C559 align to Q3SJ73 C538 and C539 (Q3SJ73 C-terminus ...SCCAG).

## Interpretation

Q3SJ73 keeps all three cysteine sets that the Tn501 work showed are needed for Hg(II) handling and
reduction, including the C-terminal pair that distinguishes MerA from other class-I pyridine
nucleotide-disulfide oxidoreductases. This supports assigning Q3SJ73 to the true mercuric reductase
clade rather than to a paralogous family member. It is sequence evidence only: no activity, expression or
phenotype has been measured for this protein.
