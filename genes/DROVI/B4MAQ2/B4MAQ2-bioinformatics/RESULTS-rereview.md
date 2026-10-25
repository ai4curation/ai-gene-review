# B4MAQ2 re-review: pairwise comparison with characterised exportins

Script: `compare_exportins_rereview.py` (raw output: `compare_exportins_rereview.out`).
Method: UniProt REST sequences, Biopython global PairwiseAligner, BLOSUM62,
gap open -10, extend -0.5; identity computed over aligned (non-gap) columns.

| Comparator | PANTHER subfamily | Length | Identity to B4MAQ2 |
|---|---|---|---|
| Q9VWE7 D. melanogaster Ranbp21 (Exp5) | PTHR11223:SF3 | 1241 | 0.859 over 1235 columns |
| Q9HAV4 human XPO5 | PTHR11223:SF3 | 1204 | 0.385 over 1176 columns |
| O14980 human XPO1/CRM1 | PTHR11223:SF2 | 1071 | 0.258 over 927 columns |

Interpretation: B4MAQ2 (1238 aa) is near full length relative to D. melanogaster
Ranbp21 (1241 aa) and aligns end to end with it (1235 aligned columns, 85.9%
identity), as expected for a one-to-one Drosophila-genus ortholog. Both proteins
share PANTHER subfamily PTHR11223:SF3 (EXPORTIN-5) with human XPO5. Identity to
the exportin-1 subfamily (SF2) is much lower. The comparison is consistent with
B4MAQ2 being the complete canonical Exportin-5 product of D. virilis, not a
fragment. Pairwise identity is supporting evidence only; the orthology
assignment rests on the shared PANTHER subfamily.
