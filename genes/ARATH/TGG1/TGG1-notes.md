# TGG1 (P37702, At5g26000) review notes

## Session 2026-09-30

No falcon deep-research file was present during review. Additional PMIDs cached:
11950967, 15316292, 19114538, 19880612, 25304201, 31636648, 32145024, 39894892.

### Enzyme activity
- Recombinant TGG1 (Pichia) hydrolyzes sinigrin; weak O-beta-glucosidase
  [PMID:19703694 "All myrosinases also displayed O-beta-glucosidase activity, although with
  lower efficiency compared to the myrosinase activity."]. UniProt Km 45 uM sinigrin vs 34 mM
  pNPG -> O-glucosidase activity is non-core.
- tgg1 tgg2 double mutant: no leaf myrosinase activity; single mutants wild-type-like
  [PMID:16640593 "Glucosinolate breakdown in crushed leaves of tgg1 or tgg2 single mutants
  was comparable to that of wild-type, indicating redundant enzyme function."]

### Defense
- Double mutant improves weight gain of T. ni and M. sexta; aphids unaffected
  [PMID:16640593 "Reproduction of two Homoptera, Myzus persicae and Brevicoryne brassicae,
  was unaffected by myrosinase mutations."]

### Localization / cell types
- Guard cells and phloem myrosin cells [PMID:11950967 "Promoter activity was found to be
  highly specific and restricted to guard cells and distinct cells of the phloem."]
- Vacuolar proteome includes At5g26000 [PMID:15539469 "the corresponding myrosinase gene
  products (At5g25980 and At5g2600)"]
- Plastid/thylakoid/ribosome proteomics hits treated as contamination of an extremely
  abundant secretory protein (MARK_AS_OVER_ANNOTATED); peroxisome/apoplast/secretory
  vesicle kept non-core.

### Guard-cell signaling
- Most abundant guard-cell protein; tgg1 hyposensitive to ABA [PMID:19114538 "tgg1 mutants
  were hyposensitive to abscisic acid (ABA) inhibition of guard cell inward K(+) channels
  and stomatal opening"]
- tgg1 tgg2 fails ABA/MeJA closure [PMID:19433491]; acrolein [PMID:32145024]; AITC
  [PMID:39894892], the latter proposing no glucosinolate hydrolysis is involved.
- Decision: GO:0010119 ACCEPT (second core function, MF unresolved); response to ABA
  KEEP_AS_NON_CORE.

### Other decisions
- carbohydrate metabolic process (IEA) -> MODIFY to GO:0019762.
- Core: GO:0019137 thioglucosidase activity; GO:0019762, GO:0002213; GO:0000325.
