# BNA5 (YLR231C) notes

Evidence journal, built from the UniProt record and cached publications (no paid deep research).

## Identity and activity
- Kynureninase (EC 3.7.1.3), PLP-dependent; cleaves L-kynurenine to anthranilate + L-alanine and 3-hydroxy-L-kynurenine to 3-hydroxyanthranilate + L-alanine [UniProt:Q05979 "Reaction=3-hydroxy-L-kynurenine + H2O = 3-hydroxyanthranilate + L-"].
- Genetic/biochemical confirmation in yeast: [PMID:12062417 "for BNA5 (YLR231c) and BNA6 (YFR047c) confirmed that they encode kynureninase and quinolinate phosphoribosyl transferase respectively"].
- Kynurenine pathway mutants are co-lethal with npt1, i.e. the kynurenine (de novo) and Preiss-Handler routes are the only sources of the nicotinic acid moiety [PMID:12062417 "deletion of genes encoding kynurenine pathway enzymes are co-lethal with the Deltanpt1"].
- Pathway position: step 2/3 of quinolinate synthesis from kynurenine (after Bna4 kynurenine 3-monooxygenase, before Bna1 3-HAO) [UniProt:Q05979 "L-kynurenine: step 2/3"].

## Location
- GFP survey: cytoplasm and nucleus [UniProt:Q05979, PMID:14562095].
- Forms cytoophidia (filaments) in stationary/quiescent cells; CTPS cytoophidium disruption promotes Bna5 cytoophidia and is associated with reduced de novo NAD pathway output [PMID:39836171 "promote the assembly of Glt1 and Bna5 cytoophidia and their complexes"]. Condition-specific; non-core.

## Interactions
- IntAct IPI with Rsp5 (P39940) comes from a protein-microarray screen of WW domains [PMID:16606443 "We used protein microarray technology to generate a protein interaction map for 12 of the 13 WW domains"]. Uninformative for function.

## Annotation observations
- GO:0034354 ('de novo' NAD+ from L-tryptophan) is obsolete; its replaced_by GO:0034628 is defined as starting from L-aspartate (the prokaryote/plant route), so it is NOT a suitable replacement for the yeast kynurenine route. Use GO:0009435 NAD+ biosynthetic process (+ GO:0006569 / GO:0019805).
