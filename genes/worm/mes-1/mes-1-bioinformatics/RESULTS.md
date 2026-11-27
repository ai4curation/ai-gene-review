# MES-1 kinase domain: catalytic residue check

Script: `kinase_motifs.py` (run 2026-11-16 with the project interpreter; Biopython 1.85;
reference sequences fetched live from the UniProt REST API).

Question: the GOA rows give MES-1 protein serine/threonine kinase (IBA, from human NEK9)
and protein tyrosine kinase activity (IEA/ISS). Berkowitz and Strome (2000) predicted it is
not an active kinase. Does the MES-1 kinase domain (G5EBL2 residues 656-966) keep the
residues that catalysis needs?

## Output (verbatim)

```
MES-1 (G5EBL2) kinase domain 656-966, length 311
  MES-1 G-x-G-x-x-G matches in N-lobe 656-760: none
  MES-1 HRD-type catalytic loop H[RNC]D: none
  MES-1 DFG: none
  MES-1 any D[FLWY]G: none
  MES-1 APE-type [AP]PE: [(879, 'PPE')]

NEK9_HUMAN (Q8TD19) kinase domain 52-308; aligned columns 105, identity 0.30, score 130.5
  Gly-loop G1                  NEK9_HUMAN G59 -> MES-1 (gap / unaligned)
  Gly-loop G2                  NEK9_HUMAN G61 -> MES-1 (gap / unaligned)
  Gly-loop G3                  NEK9_HUMAN G64 -> MES-1 (gap / unaligned)
  catalytic Asp (HRD)          NEK9_HUMAN D176 -> MES-1 R832
  catalytic Asn (HRDxxxxN)     NEK9_HUMAN N181 -> MES-1 N837

SRC_HUMAN (P12931) kinase domain 270-523; aligned columns 150, identity 0.27, score 92.0
  Gly-loop G1                  SRC_HUMAN G277 -> MES-1 (gap / unaligned)
  Gly-loop G2                  SRC_HUMAN G279 -> MES-1 (gap / unaligned)
  Gly-loop G3                  SRC_HUMAN G282 -> MES-1 E718
  beta3 Lys (VAIK)             SRC_HUMAN K298 -> MES-1 E738
  catalytic Asp (HRD)          SRC_HUMAN D389 -> MES-1 R832
  catalytic Asn (HRDxxxxN)     SRC_HUMAN N394 -> MES-1 N837
  DFG Asp                      SRC_HUMAN D407 -> MES-1 N860
  APE Glu                      SRC_HUMAN E435 -> MES-1 E881
```

## Interpretation

- The catalytic-loop aspartate (the D of HRD, the catalytic base) aligns to Arg832 of
  MES-1 against both NEK9 and SRC. MES-1 has no H-R/N/C-D motif anywhere in its kinase
  domain; its catalytic loop reads HTRVTTLN (830-837). The loop asparagine (N837) is kept.
- The Mg2+-binding aspartate of DFG aligns to Asn860 (MES-1 reads NFG). There is no D-F/L/W/Y-G
  anywhere in the domain.
- There is no G-x-G-x-x-G glycine-rich loop in the MES-1 N-lobe.
- The APE glutamate (E881, in a PPE motif) is retained.
- The N-lobe aligns poorly with both references (local alignment covers only the C-lobe for
  NEK9), so the assignment of the beta3 lysine is unreliable: SRC K298 aligns to E738 here,
  while the PROSITE rule places a predicted ATP-binding Lys at 685. No conclusion is drawn
  about the lysine.

Conclusion: MES-1 lacks the catalytic-loop aspartate, the DFG aspartate and the
glycine-rich loop. All three are required for phosphotransfer in active protein kinases,
so MES-1 is a pseudokinase. This agrees with Berkowitz and Strome (2000) and with the
UniProt DOMAIN note. It is a sequence-based inference; no kinase assay of MES-1 has been
reported.
