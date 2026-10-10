# pyk1 (SPAC4H3.10c, UniProt Q10208) notes

Module: `emp_glycolysis` (pyruvate_kinase_step); S. cerevisiae counterparts CDC19 (P00549) and PYK2 (P52489).
`just fetch-gene SCHPO pyk1` fetched the correct accession (Q10208, KPYK_SCHPO).

## Evidence
- Sole pyruvate kinase of S. pombe; reaction pyruvate + ATP = PEP + ADP + H+, Mg2+ and K+ cofactors [UniProt:Q10208 "Reaction=pyruvate + ATP = phosphoenolpyruvate + ADP + H(+);"].
- Recombinant enzyme purified after expression in S. cerevisiae; sigmoidal PEP kinetics made hyperbolic by FBP; dimer-tetramer equilibrium [PMID:9790887 "The purified enzyme showed sigmoidal kinetics with respect to PEP;"] [PMID:9790887 "in the presence of FBP, the kinetics were restored to Michaelis-Menten behavior."].
- Cytosolic; used as a bulk-autophagy cytosolic cargo [PMID:37939137 "We used the cytosolic protein Pyk1, a bulk autophagy cargo, to verify whether a protein enclosed within the autophagosome is resistant to AID-mediated degradation"].

## Curation decisions
- GO:0061621 canonical glycolysis (IDA, PMID:9790887) is obsolete in current GO -> MODIFY to GO:0006096 glycolytic process. The PomBase GO-CAM 663d668500002302 still uses GO:0061621 as part_of.
- Mg2+/K+ binding IEA kept as non-core cofactor statements.
- Consistent with the CDC19 review core function (GO:0004743, GO:0006096, cytosol). Unlike S. cerevisiae, S. pombe has a single PK (no PYK2-like glucose-repressed paralog).
