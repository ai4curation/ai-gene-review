# RecC Walker A (P-loop) motif scan

## Question

Do the RecC subunits of E. coli K-12 (P07648) and P. putida KT2440 (Q88DZ4)
carry a Walker A ATP-binding motif? Both receive electronic `ATP binding`
(GO:0005524) and `DNA helicase activity` (GO:0003678) annotations, while the
helicase motors of RecBCD are RecB and RecD.

## Method

`walker_a_scan.py` reads the SQ block of each UniProt flat file and reports every
match to the canonical Walker A consensus `[AG]-x(4)-G-K-[ST]` and to a relaxed
`G-x(4)-G-K` pattern. RecB and RecD from the same two organisms are positive
controls. Command (run from the repository root):

```
python3 -I analysis/module_audits/bacterial_recbcd_end_resection/walker_a_scan.py \
  genes/ECOLI/recC/recC-uniprot.txt genes/PSEPK/recC/recC-uniprot.txt \
  genes/ECOLI/recB/recB-uniprot.txt genes/ECOLI/recD/recD-uniprot.txt \
  genes/PSEPK/recB/recB-uniprot.txt genes/PSEPK/recD/recD-uniprot.txt
```

## Output (2026-11-09)

```
P07648	length=1122	strict_[AG]x4GK[ST]=[]	relaxed_Gx4GK=[]
Q88DZ4	length=1160	strict_[AG]x4GK[ST]=[]	relaxed_Gx4GK=[]
P08394	length=1180	strict_[AG]x4GK[ST]=[(23, 'ASAGTGKT')]	relaxed_Gx4GK=[]
P04993	length=608	strict_[AG]x4GK[ST]=[(171, 'GGPGTGKT')]	relaxed_Gx4GK=[(171, 'GGPGTGK')]
Q88DZ5	length=1224	strict_[AG]x4GK[ST]=[(21, 'ASAGTGKT')]	relaxed_Gx4GK=[]
Q88DZ6	length=691	strict_[AG]x4GK[ST]=[(221, 'GGPGTGKT')]	relaxed_Gx4GK=[(221, 'GGPGTGK')]
```

## Interpretation

Neither RecC sequence contains a Walker A motif, under the strict or the relaxed
pattern, whereas every RecB and RecD control has one near its N-terminal motor
domain. The P-loop-like (SSF52540 / Gene3D 3.40.50.300) folds that InterPro
detects in RecC therefore lack the nucleotide-binding loop of an active
SF1 helicase motor. This is consistent with RecC being a helicase-like,
non-motor subunit. A motif scan cannot exclude non-canonical nucleotide binding;
it only shows that there is no sequence basis for an ATP-binding site of the
helicase type.
