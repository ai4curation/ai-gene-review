# HXK1 notes (P04806, YFR053C)

- Hexokinase PI, EC 2.7.1.1; glucose, fructose, mannose [UniProt:P04806 "Reaction=a D-hexose + ATP = a D-hexose 6-phosphate + ADP + H(+);"] [UniProt:P04806 "Reaction=D-fructose + ATP = D-fructose 6-phosphate + ADP + H(+);"]; ITC kinetics of PI and PII [PMID:12611889 "The reaction is exothermic for both isozymes"].
- Hxk1/Hxk2 are the only fructose kinases [PMID:6300872 "lacking both hexokinase A(P-I) and B(P-II) but containing glucokinase (and hence able to grow on glucose but not fructose)"]; Hxk1 prefers fructose [PMID:8917466 "fructose repression of Hxk1 is only transient, which is in line with its preference for fructose as substrate"].
- Glucose-repressed; derepressed on non-fermentable carbon [PMID:11311123 "the HXK1 and GLK1 genes are rapidly de-repressed"].
- Glucose/fructose "import across plasma membrane" IGI/IEA rows: kinase-dependence of low-Km uptake [PMID:6300872 "Low Km uptake was restored to the triple mutant by introduction of the cloned wild-type genes"] — hexokinase is not a transporter.

Decisions: REMOVE bifid shunt, protein binding x2, ARBA transport IEAs; MARK_AS_OVER_ANNOTATED transport IGIs, intracellular glucose homeostasis, mito outer membrane IBA (mammalian HK2-specific), generic parents.

## QA pass (2026-11-19)

- IBA intracellular glucose homeostasis (PTN000455350): donors are mouse/rat Gck, mouse/human HKDC1 and Arabidopsis HXK1/GIN2 (identities checked via UniProt cross-references); all glucose-sensor contexts, no fungal donor. Kept MARK_AS_OVER_ANNOTATED, added propagation_review (PROPAGATION_BAD, CONTEXT_OR_TISSUE_MISMATCH).
- IBA cytoplasmic side of mitochondrial outer membrane: donors human HK2 (P52789) and Brassica M4FD55 both have an N-terminal hydrophobic anchor; yeast Hxk1 starts MVHLGPKKPQARKGSMADVP (no anchor). Kept MARK_AS_OVER_ANNOTATED, added propagation_review (COMPARTMENT_OR_COMPLEX_MISMATCH).
- Cytoplasm IDA (PMID:11254124): first changed to MODIFY to cytosol, then kept ACCEPT when merging main (2026-11-20): a fractionation-type assay cannot resolve cytosol, and cytosol is already carried by the HDA and IBA rows. Hxk1 is not nuclear even in glucose starvation [PMID:37196001 "If there was a significant accumulation of Hxk1 in the nucleus, we should have been able to detect it in the glucose starvation conditions, and we did not"].
- Generic parents (carbohydrate metabolic process, organophosphate metabolic process, carbohydrate derivative metabolic process) -> TOO_GENERAL (ancestors of accepted glycolysis / G6P metabolic process, checked with runoak ancestors).
- SGD description reviewed: no errors.
