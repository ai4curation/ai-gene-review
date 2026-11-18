# thiG (Q88CS6) active-site conservation

Script: `thig_active_site.py` (Biopython global alignment, BLOSUM62). Input: the cached
`thiG-uniprot.txt`; reference entries E. coli ThiG P30139 and B. subtilis ThiG O31618
fetched from UniProt REST on 2026-11-12. Raw output: `thig_active_site.out`.

## Results

- P30139 (256 aa) vs Q88CS6 (270 aa): 44.3% identity over 253 aligned positions.
- O31618 (256 aa) vs Q88CS6 (270 aa): 52.4% identity over 254 aligned positions.
- The Schiff-base active-site lysine of both references maps to Q88CS6 Lys112
  (output lines "ACT_SITE K95 [ECO:0000250] -> Q88CS6 K112" and "ACT_SITE K98 [] -> Q88CS6 K112").
- The DXP-binding residues map to identical residues in Q88CS6 (G173, A199, G200, N221),
  except reference Thr205/Thr208, which is Ser222 in Q88CS6 (a conservative hydroxyl
  substitution).

## Interpretation

Q88CS6 retains the catalytic lysine and the DXP phosphate/sugar-binding residues of
characterised ThiG enzymes, consistent with an active thiazole synthase rather than a
diverged paralog.

# Partner enzymes: ThiH, ThiO and ThiF presence

Script: `thih_presence.py` (UniProt REST queries by organism, gene name, EC number and, for
ThiH, InterPro IPR012726; run 2026-11-12). Raw output: `thih_presence.out`.

| Organism | ThiH (EC 4.1.99.19) | ThiO (EC 1.4.3.19) | ThiF (EC 2.7.7.73) |
|---|---|---|---|
| P. putida KT2440 | 0 entries | 1 (Q88Q83, PP_0612) | 0 entries |
| B. subtilis 168 | 0 entries | 1 (O31616) | 1 (O31619) |
| E. coli K-12 | 1 (P30140) | 0 entries | 1 (P30138) |

KT2440 and B. subtilis encode ThiO but no ThiH, so their ThiG proteins cannot be part of a
ThiG-ThiH 2-iminoacetate synthase complex. KT2440 also has no protein annotated as ThiF.
These are absence-of-annotation results from database queries, not a sequence search of the genomes.
