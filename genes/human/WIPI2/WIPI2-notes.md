# WIPI2 notes

## 2026-09-20 full evidence re-review

Reviewed all 45 source rows, preserving both NOT annotations. Current PAINT PTHR11227 places the relevant PROPPIN IBDs at PTN000132136.

- Pexophagy, nucleophagy and glycophagy are now UNDECIDED. The ancestral assertions have real descendant evidence (SGD:S000001917; SGD:S000001917/S000003455/S000006021; FB:FBgn0035850, respectively). The former categorical reasons incorrectly demanded a cargo receptor function from an execution adaptor. WIPI2 recruits ATG16L1 and enables membrane lipidation, which is direct work in autophagosome formation even when another protein supplies cargo selectivity. GO nucleophagy is not restricted to yeast piecemeal microautophagy. Specific conservation and paralog partitioning remain to be adjudicated, without presuming the IBD wrong.
- Live GO:0034045 is obsolete; the existing GO:7770114 phagophore membrane is the appropriate replacement. The new-term proposal is withdrawn. The local validation ontology predates that new ID, so core locations retain the correct broader GO:0061908 phagophore and membrane specificity in prose. The original source terms are preserved.
- Broad membrane and cytosol locations are retained as core: WIPI2 cycles between the soluble pool and PI3P-rich autophagic membranes. Primary location is not exclusivity. The broad stress-response term is retained as contextual, and the generic protein-containing-complex observation is retained as noncore without inventing permanent membership in the recruited conjugation complex.
- Rechecked PMID:20505359 and the WIPI2/ATG16L1 mechanism in PMID:24954904, alongside available interaction/microscopy studies. PMID:33499712 was retrieved in full; its endogenous WIPI2 puncta under Parkin/valinomycin provide a selective-autophagy localization context, but do not adjudicate the three other cargo classes. PI(3,5)P2 binding remains a supported secondary activity, without asserting that no physiological role could exist.
- Both NOT autophagosome and NOT autophagosome maturation source flags remain intact, as do all isoform/qualifier/evidence fields. Their experimental contexts are compatible with recruitment to early phagophores and release before later maturation. Generic protein-binding removals do not reject the interaction data.
- No existing OpenScientist report was found by gene/accession/alias cache scan. Root coordinates neutral focused adjudication of the three selective-autophagy claims; no duplicate query was launched here.


## 2026-09-20 recovered pexophagy report and primary check

The shared PIK3C3 report supplied useful complex context but did not settle WIPI paralog usage. A primary search identified PMID:37621214, whose full Fig. EV3B directly measures Keima-SKL pexophagy in HeLa cells and finds complete blockade in WIPI2 knockout after phenanthroline. The IBA is retained as noncore with direct target corroboration. The same paper describes context-dependent initiation order; it does not establish universal dependence on upstream ULK1/VPS34 in every selective-autophagy route. Nucleophagy and glycophagy remain separately unresolved.


## Recovery PR evidence follow-up (2026-09-22)

Use location-relevant evidence, correct the glycophagy-specific rationale, and explicitly incorporate the existing OpenScientist alternative without treating shared machinery as proof of every selective route.
