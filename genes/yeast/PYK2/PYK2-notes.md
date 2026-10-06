# PYK2 notes (P52489, YOR347C)

- Pyruvate kinase, EC 2.7.1.40 [UniProt:P52489 "Reaction=pyruvate + ATP = phosphoenolpyruvate + ADP + H(+);"]; Mg2+ and K+ cofactors by similarity only (ECO:0000250).
- Second, functional PK isoenzyme [PMID:9139918 "it encodes a second functional pyruvate kinase isoenzyme, Pyk2p"]; overexpression fully replaces Pyk1 [PMID:9139918 "could completely substitute for the PYK1-encoded enzymatic activity"].
- FBP-insensitive and glucose-repressed [PMID:9139918 "Pyk2p is active without fructose-1,6-bisphosphate"]; [PMID:9139918 "PYK2 gene expression is subject to glucose repression"]; proposed low-flux isoform [PMID:9139918 "may be used under conditions of very low glycolytic flux"].
- Lower expression and specific activity than Pyk1 in pyk1 pyk2 background with ectopic expression [PMID:21907146 "activity in PYK2-expressing cells was lower: the TEF1pr-PYK2 strain had 22% and the CYCpr-PYK2 strain 5% activity"].
- Peripheral mitochondrial association of all glycolytic activities [PMID:16962558 "all glycolytic enzymes are associated with mitochondria in yeast"] (abstract only; activity assays cannot separate Pyk1/Pyk2).
- Melatonin pull-down hit [PMID:31708896 "pyruvate kinase 1 (Pyk2p; band a)"] - note the paper's own naming confusion (calls it pyruvate kinase 1 but lists Pyk2p); kept non-core.

Decisions: ACCEPT PK activity (all evidence), glycolysis, cytoplasm/cytosol; REMOVE bifid shunt (RCA mis-mapping from GLUCFERMEN-PWY); MODIFY obsolete GO:0061620 -> GO:0006096; MARK_AS_OVER_ANNOTATED monocarboxylic acid metabolic process (ARBA); KEEP_AS_NON_CORE Mg/K binding, mitochondrion, melatonin binding.
