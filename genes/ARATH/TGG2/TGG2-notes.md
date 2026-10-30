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


## 2026-10-26 — PR #5550 source-level correction

Revisited review findings 1–3 against the actual publication cache and the primary sources. Removed generic source-unresolved boilerplate where the assay design is adjudicable. Restored relevant verbatim biochemical and localization evidence; did not restore label-only CHAIN features, unrelated introductory statements, or quotations that no longer support the revised claim. Existing source annotation fields were preserved.

Primary supplemental check for PMID:18431481: [annotated-protein workbook s005](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0001994.s005&type=supplementary), worksheet `supplTable5`, and [abundance workbook s003](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0001994.s003&type=supplementary), worksheet `supplTable1`, explicitly classify AT5G25980 as **"not plastid"**. Internal workbook titles and article table numbering differ, so file identifier plus locus are the stable join. These are direct reads of publisher supplements, not an inference from absent targeting signals. Working downloads are under `.cache/module-audit-logs/18431481-s003` and `18431481-s005`; source caches were not manually modified.

Read PMID:28887381 full text, especially "Identification of True Membrane-associated Proteins" and Fig. 7: washed microsomes and sucrose gradients distinguish membrane association but do not separate organelles; named compartments are imported from SUBAcon/GFP knowledge. The paper states "no organelle fell in a single cluster". Mark the specific compartment claim as over-annotated while preserving proteomic detection. This applies projects/ORGANELLES.md at the actual resolution of the assay.
