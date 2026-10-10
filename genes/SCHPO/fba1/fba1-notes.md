# fba1 (S. pombe, UniProt P36580, SPBC19C2.07) notes

Role in module `emp_glycolysis`: fructose-bisphosphate aldolase step (EC 4.1.2.13); S. cerevisiae counterpart FBA1 (also class II).

## Evidence
- Class II (Zn-dependent) aldolase [UniProt:P36580 "SIMILARITY: Belongs to the class II fructose-bisphosphate aldolase"]; 2 Zn2+ per subunit by similarity [UniProt:P36580 "Note=Binds 2 Zn(2+) ions per subunit. One is catalytic and the other"].
- Reversible: condensation in gluconeogenesis and cleavage in glycolysis [UniProt:P36580 "(G3P) to form fructose 1,6-bisphosphate (FBP) in gluconeogenesis and"].
- Essential gene; CRISPRi knockdown accumulates FBP [PMID:39378339 "As expected, fba1-KD caused an accumulation of its substrate, FBP, by 2.4-fold."]; class II enzyme unrelated to human class I [PMID:39378339 "Fission yeast has a Class II aldolase that exhibits no sequence similarity to human Class I aldolases"].
- Knockdown also raised S7P and IMP but not G3P, suggesting rerouting through the PPP (same paper).
- Cytosol and nucleus in the ORFeome screen [PMID:16823372 "we determined the localization of 4,431 proteins"].

## Curation decisions
- IMP to obsolete GO:0061621 -> MODIFY to GO:0006096.
- aldehyde-lyase activity (IEA) -> MODIFY to GO:0004332.
- Zinc ion binding kept non-core (by-similarity cofactor; S. cerevisiae FBA1 review ACCEPTed it because budding yeast has zinc-proteome data).
