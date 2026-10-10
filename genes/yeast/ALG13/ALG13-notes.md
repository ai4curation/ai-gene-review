# ALG13 (YGL047W, P53178) notes

Pathway context: cytoplasmic-face LLO assembly (GlcNAc-PP-Dol + UDP-GlcNAc -> GlcNAc2-PP-Dol, EC 2.4.1.141), with ALG14.

- Bipartite enzyme; Alg13 catalytic, Alg14 membrane anchor. [PMID:16100110 "We show that Alg14 functions as a membrane anchor that recruits Alg13 to the cytosolic face of the ER, where catalysis of GlcNAc2-PP-dol occurs."] [PMID:16100110 "Alg13 contains a predicted catalytic domain, but lacks any membrane-spanning domains."]
- Activity requires Alg14; cytosolic Alg13 inactive. [PMID:16100113 "Immunoprecipitating Alg13p from solubilized extracts resulted in the formation of GlcNAc(2)-PP-Dol but required Alg14p for activity"] [PMID:16100113 "localizes both to the membrane and cytosol; the latter form, however, is enzymatically inactive."]
- Depletion phenotype. [PMID:15615718 "down-regulation of either causes growth retardation, reduced N-glycosylation of carboxypeptidase Y, and accumulation of dolichyl-PP-GlcNAc."]
- NMR: binds UDP-GlcNAc via C-terminal half. [PMID:18547528 "This glycosyltransferase is unusual in that it is active only in the presence of a binding partner, Alg14."]

Curation observations
- IDA "cytoplasmic side of Golgi membrane" from PMID:16100110 contradicts the same abstract (ER); MODIFY to GO:0098554.
- Protein binding (Alg14) removed (captured by GO:0043541); identical protein binding over-annotated.
- MF modelled as contributes_to GO:0004577 with in_complex GO:0043541.
