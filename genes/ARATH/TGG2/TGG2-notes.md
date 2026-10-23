# TGG2 (Q9C5C2, At5g25980) review notes

## Session 2026-09-30

No falcon deep-research file was present during review.

### Function
- Redundant with TGG1 for leaf glucosinolate breakdown; double mutant lacks activity
  [PMID:16640593 "leaf extracts of tgg1tgg2 double mutants had undetectable myrosinase
  activity in vitro"]. No purified-enzyme assay of TGG2 is cached; thioglucosidase
  activity rests on genetics (tgg1 single mutant = TGG2 only, wild-type breakdown).
- Expressed only in myrosin idioblasts [PMID:25304201 "TGG1 is expressed in stomata as
  well as in MIs , but TGG2 is expressed exclusively in MIs ( Barth and Jander, 2006 )."]
- MVP1 binds TGG2 specifically and is needed for its trafficking [PMID:19880612
  "MVP1 interacted specifically with the Arabidopsis myrosinase protein, THIOGLUCOSIDE
  GLUCOHYDROLASE2 (TGG2), but not TGG1"].
- Vacuolar proteome includes At5g25980 [PMID:15539469]. Peroxisome proteome explicitly
  lists TGG2 [PMID:17951448].

### Stomatal role - conflict
- tgg1 tgg2 double mutant impaired in ABA/MeJA closure [PMID:19433491], but TGG2 is not
  expressed in guard cells by reporter and was absent from the guard-cell proteome
  [PMID:19114538 "Unlike TGG1, TGG2 was not found in any of the gel-based"]. Stomatal and
  ABA annotations kept as non-core for TGG2.

### Decisions
- Beta-glucosidase IBA -> KEEP_AS_NON_CORE (paralogs retain weak O-glucosidase).
- carbohydrate metabolic process -> MODIFY to GO:0019762.
- Plastid/chloroplast/ribosome HDA -> MARK_AS_OVER_ANNOTATED; plasmodesma, peroxisome,
  apoplast, secretory vesicle -> KEEP_AS_NON_CORE.
- Core: GO:0019137; GO:0019762, GO:0002213; GO:0000325.
