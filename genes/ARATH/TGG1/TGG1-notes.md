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


## Module-member evidence audit — 2026-10-25

Reviewed every original row (27) and core function using review/annotation-reviewer instructions, current cached primary publications and the existing research. Preserved all source annotation fields and all pre-existing proposed rows. Reused the existing genuine Falcon provider report and its artifacts. These plant targets do not require bacterial FEBA retrieval.

PMID19703694 directly assays TGG1, TGG4 andTGG5, including lower-efficiency O-beta-glucosidase activity. Therefore broad O-glycoside hydrolase is refined to beta-glucosidase, not to the S-glycoside thioglucosidase reaction. Main damage-triggered defense is supported by16640593, with herbivore-specific effects; no universal benefit to all attackers implied. Cohort organellar/ribosomal assignments are unresolved rather than declared contamination. Updated signaling core distinguishes ABA/acrolein calcium positioning from39894892 AITC responses; the required signaling role is not simply hydrolysis of an intact vacuolar substrate.

Broad and substrate-specific terms were assessed consistently across evidence codes. No NEW rows were added. Previously proposed rows were evaluated for direct participation rather than filled from pathway adjacency. Experimental cohort calls whose protein-level data were not verified were left UNDECIDED; full-text availability alone was not treated as proof of a target-specific assay. Original sources and provider reports were not hand-edited.

### Final cross-row QA, 2026-10-26

Kept location claims consistent with retained experimental compartments: a supported apoplast assignment refines a general extracellular prediction, while a main cytosolic or vacuolar location does not by itself disprove a secondary predicted pool. Conditional Arabidopsis ESP activity is distinguished from a universal coding knockout. Original annotation fields remain unchanged.


## 2026-10-26 — PR #5550 source-level correction

Revisited review findings 1–3 against the actual publication cache and the primary sources. Removed generic source-unresolved boilerplate where the assay design is adjudicable. Restored relevant verbatim biochemical and localization evidence; did not restore label-only CHAIN features, unrelated introductory statements, or quotations that no longer support the revised claim. Existing source annotation fields were preserved.

Primary supplemental check for PMID:18431481: [annotated-protein workbook s005](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0001994.s005&type=supplementary), worksheet `supplTable5`, and [abundance workbook s003](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0001994.s003&type=supplementary), worksheet `supplTable1`, explicitly classify AT5G26000 as **"not plastid"**. Internal workbook titles and article table numbering differ, so file identifier plus locus are the stable join. These are direct reads of publisher supplements, not an inference from absent targeting signals. Working downloads are under `.cache/module-audit-logs/18431481-s003` and `18431481-s005`; source caches were not manually modified.

Read PMID:28887381 full text, especially "Identification of True Membrane-associated Proteins" and Fig. 7: washed microsomes and sucrose gradients distinguish membrane association but do not separate organelles; named compartments are imported from SUBAcon/GFP knowledge. The paper states "no organelle fell in a single cluster". Mark the specific compartment claim as over-annotated while preserving proteomic detection. This applies projects/ORGANELLES.md at the actual resolution of the assay.

A normal force-fetch recovered the full text of PMID:16648217; the thylakoid-fraction result is assessed alongside the later explicit non-plastid classification. PMID:15821981 remains abstract-only; its accessible abstract explicitly calls non-ribosomal co-migration a possible association, warranting MARK_AS_OVER_ANNOTATED rather than REMOVE.
