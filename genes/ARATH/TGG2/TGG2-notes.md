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


## Module-member evidence audit — 2026-10-25

Reviewed every original row (21) and core function using review/annotation-reviewer instructions, current cached primary publications and the existing research. Preserved all source annotation fields and all pre-existing proposed rows. Reused the existing genuine Falcon provider report and its artifacts. These plant targets do not require bacterial FEBA retrieval.

Native redundancy withTGG1 is directly supported by16640593; loss of both changes damage-induced hydrolysis and some generalist herbivore outcomes. The19703694 purified isoforms areTGG1/4/5, so TGG2 secondary O-glucosidase remains inherited/comparative, not claimed directly assayed there. Refined O-hydrolase to the already-present beta-glucosidase term. Unchecked chloroplast/plastid/ribosome data remain undecided. No new seed-turnover process is inferred:31850033 explicitly does not findTGG1/2 responsible for the germination decline.

Broad and substrate-specific terms were assessed consistently across evidence codes. No NEW rows were added. Previously proposed rows were evaluated for direct participation rather than filled from pathway adjacency. Experimental cohort calls whose protein-level data were not verified were left UNDECIDED; full-text availability alone was not treated as proof of a target-specific assay. Original sources and provider reports were not hand-edited.

### Final cross-row QA, 2026-10-26

Kept location claims consistent with retained experimental compartments: a supported apoplast assignment refines a general extracellular prediction, while a main cytosolic or vacuolar location does not by itself disprove a secondary predicted pool. Conditional Arabidopsis ESP activity is distinguished from a universal coding knockout. Original annotation fields remain unchanged.
