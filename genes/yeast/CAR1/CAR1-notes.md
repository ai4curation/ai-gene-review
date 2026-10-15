# CAR1 (YPL111W, P00812) notes

Evidence journal (no paid deep research run; built from UniProt and cached publications).

- Arginase, EC 3.5.3.1, homotrimer, arginase family; hydrolyses L-arginine to urea + L-ornithine [UniProt:P00812].
- Purified yeast enzyme: "The purified enzyme has a specific activity of 885 mumol urea min-1 mg-1 and a Km for arginine of 15.7 mM" and "The native trimeric enzyme has a sedimentation coefficient of 5.95 S" [PMID:2404017].
- Metals: "there is a weakly associated Mn2+ that binds to the trimeric enzyme" and "the loosely associated catalytic Mn2+ ion and the more tightly associated structural Zn2+ ion confer stability to the enzyme" [PMID:1939179].
- Induction: CAR1 mRNA "was markedly increased, however, in wild-type cells grown in the presence of inducer" and "arginase production is probably controlled at the level of gene expression" [PMID:14582193]. UniProt: induced by arginine or homoarginine [UniProt:P00812].
- Location: soluble fraction with OTCase and the other ornithine-to-arginine enzymes [PMID:205532 "the two first catabolic enzymes, arginase and ornithine aminotransferase, were in the"].
- Epiarginase regulation (moonlighting): "In this complex, arginase acts as a negative allosteric effector for ornithine transcarbamoylase" [PMID:2404017]; "OTCase and arginase form a one-to-one enzyme complex in which the activity of OTCase is inhibited whereas arginase remains catalytically active" and "In arginase, two cysteines at the C terminus of the protein are crucial for its epiarginase function but not for its catalytic activity and trimeric structure" [PMID:12679340].

## Curation decisions
- Core MF 1: GO:0004053 arginase activity; BP GO:0006527 L-arginine catabolic process; CC cytosol.
- Core MF 2: GO:0090369 ornithine carbamoyltransferase inhibitor activity, in GO:1903269 complex with ARG3 (prevents futile cycling of arginine synthesis/degradation).
- Urea cycle (IBA/IEA/IDA/IMP): yeast is not ureotelic; arginase is the first step of arginine catabolism to use arginine as nitrogen source (urea is further hydrolysed by DUR1,2). Experimental rows MODIFY -> L-arginine catabolic process; IBA MARK_AS_OVER_ANNOTATED (consistent with ARG1 review).
- protein binding (ARG3) REMOVE: superseded by complex/inhibitor annotations (consistent with ARG3 review).
