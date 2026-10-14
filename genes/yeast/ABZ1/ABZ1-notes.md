# ABZ1 (YNR033W, P37254) notes

Built from the UniProt record, the cached publications and GOA. No deep research provider was run.

- Activity: ADC synthase, EC 2.6.1.85, chorismate + L-glutamine -> 4-amino-4-deoxychorismate + L-glutamate [UniProt:P37254]. It is a bifunctional PabA-PabB fusion: "protein with similarity to the two components of PABA synthase described for prokaryotes (Escherichia coli PabA and PabB), suggesting that PABA synthase is bifunctional in yeast" [PMID:8346682].
- Genetics: "The cloned sequence was confirmed to be PABA synthase by gene disruption." [PMID:8346682]
- Biochemistry, from the ABZ2 paper: "Addition to the reaction mixture of purified Abz1p led to a decrease in chorismate and the concomitant formation of ADC." [PMID:17873082]
- Location: "Since Abz1p is also a cytoplasmic enzyme, it is clear that the synthesis of PABA in S. cerevisiae takes place in the cytoplasm" [PMID:17873082]. The GFP survey also places it in the cytoplasm [PMID:14562095].

## Curation decisions
- The MF (GO:0046820) rows are accepted from every source. The ISS rows to E. coli PabA and PabB are valid because each matches one of the two fused domains.
- The chorismate metabolic process RCA row is accepted. This is the one gene in the batch that really consumes chorismate.
- GO:0035999 (THF interconversion) is removed as superpathway inflation.
- GO:0046656 (folic acid biosynthesis) is changed to GO:0046654 (THF biosynthesis), because yeast does not make folic acid itself.
