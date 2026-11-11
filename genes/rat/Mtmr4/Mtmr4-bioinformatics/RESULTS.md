# Mtmr4 (rat, A0A8I6A3Q2) motif scan

Script: `motif_scan.py` (Python standard library only), run as
`python3 -I motif_scan.py ../Mtmr4-uniprot.txt`.

## Output

```
sequence length: 1191
CX5R catalytic loop (C.{5}R): [(407, 'CSDGWDR')]
PTP active-site HCxxGxxR(T/S): [(406, 'HCSDGWDRT')]
FYVE PI3P-binding R(R/K)HHCR: [(1128, 'RRHHCR')]
PY motif PPxY: [(1001, 'PPLY')]
GPPxxxY CEP55-binding motif: [(5, 'GPPSLEY')]
residue 407: C
```

## Interpretation

- The catalytic cysteine of the myotubularin phosphatase domain is intact at Cys407
  (HCSDGWDRT, the CX5R loop), the same position as the human MTMR4 C407S/C407A
  catalytic-dead mutants used experimentally. Rat Mtmr4 is therefore predicted to be an
  active 3-phosphatase, not a pseudophosphatase.
- The C-terminal FYVE domain carries the R(R/K)HHCR signature (RRHHCR at 1128) that
  forms the PtdIns3P headgroup-binding pocket of FYVE domains.
- A single PPxY (PY) motif at 1001 (PPLY) is present, consistent with the Nedd4 WW
  domain-binding site described for human MTMR4.
- An N-terminal GPPxxxY motif at residue 5 (GPPSLEY) matches the CEP55-binding motif
  reported for human MTMR4.
