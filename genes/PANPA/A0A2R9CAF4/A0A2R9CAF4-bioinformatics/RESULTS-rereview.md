# A0A2R9CAF4 vs human SLC26A11 — re-review comparison (2026-10-20)

Script: `compare_to_human_rereview.py` (global Needleman-Wunsch, BLOSUM62, gap open -10 / extend -0.5;
sequences: local `A0A2R9CAF4-uniprot.txt`, Q86WA9 and Q80ZD3 fetched from UniProt REST).
Raw output: `compare_to_human_rereview.out`.

## Results

- A0A2R9CAF4 length: 606 aa; human SLC26A11 Q86WA9 length: 606 aa.
- Bonobo vs human: 601/606 identical aligned positions (99.2%), no gaps; full-length product, not a fragment.
- Bonobo vs mouse Q80ZD3 (593 aa): 486/589 identical aligned positions (82.5%).
- Human Glu-320 (the pH-sensing residue of PMID:42509233) is conserved as E320 in A0A2R9CAF4.

## Interpretation

A0A2R9CAF4 is a full-length product of the bonobo SLC26A11 gene (UniProt CTD cross-reference 284129,
the human SLC26A11 GeneID). Human and mouse SLC26A11 are both in PANTHER subfamily PTHR11814:SF55
(SODIUM-INDEPENDENT SULFATE ANION TRANSPORTER), queried from the PANTHER API; bonobo is not a PANTHER
reference genome, so its subfamily is inferred from orthology to these members, not from a direct HMM call.
