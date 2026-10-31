# PGI1 notes (P12709, YBR196C)

- Glucose-6-phosphate isomerase, EC 5.3.1.9 [UniProt:P12709 "Reaction=alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate;"]; anomeric specificity alpha-G6P <-> beta-F6P [PMID:1730590 "phosphoglucoisomerase selectively catalyzes the reversible conversion between alpha-D-[2-13C]glucose 6-phosphate and beta-D-[2-13C]fructose 6-phosphate"].
- Side anomerase activity on G6P, F6P [PMID:1730590 "also considerably accelerates the anomerization of both D-hexose 6-phosphates"] [PMID:6572382 "confirming that the anomerization of Glc-6-P is enzyme catalyzed"] and M6P [PMID:4570473 title "its 1-epimerization by phosphoglucose isomerase"].
- Single-copy, only G6P/F6P interconversion step; null cannot grow on glucose or fructose alone, fails to sporulate on acetate without glucose [PMID:3020369 "the phosphoglucose isomerase reaction is the only step catalysing the interconversion of glucose-6-P and fructose-6-P"].
- Cytosolic [UniProt:P12709 "SUBCELLULAR LOCATION: Cytoplasm, cytosol"].

Decisions: REMOVE bifid shunt; MODIFY three obsolete glycolysis rows -> GO:0006096; anomerase/epimerase rows KEEP_AS_NON_CORE; SIS-domain generic terms and PM HDA MARK_AS_OVER_ANNOTATED.
