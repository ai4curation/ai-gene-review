# ARO9 (YHR137W, P38840) notes

Pathway context: aromatic aminotransferase II; catabolic (Ehrlich) Phe/Tyr/Trp transamination, back-up for ARO8 in biosynthesis; YeastCyc EC 2.6.1.58 (Phe/Tyr:pyruvate) and 2.6.1.28 (Trp:phenylpyruvate).

- Acceptor specificity: phenylpyruvate, 4-hydroxyphenylpyruvate, pyruvate; NOT 2-oxoglutarate [UniProt:P38840 "pyruvate as amino acceptors. Does not accept glutamate or 2-"]. Hence the GOA GO:0008793 (aromatic-aa:2-oxoglutarate) rows (EXP, IMP, IEA, 5 RCA) are MODIFIED to GO:0047312 L-phenylalanine:pyruvate / GO:0080098 L-tyrosine:pyruvate transaminase.
- Induced by aromatic amino acids [PMID:9491083 "ARO9 expression is induced when aromatic amino acids are present in the growth medium"].
- All kynurenine aminotransferase activity [PMID:9491082 "In particular, it is responsible for all the measured kynurenine aminotransferase activity."]; GO:0016212 specifies 2-oxoglutarate, kept non-core with caveat (no kynurenine:pyruvate GO term).
- Redundant contribution to Phe/Tyr biosynthesis [PMID:9491082 "aro8 and aro9 double mutants which are auxotrophic for both phenylalanine and tyrosine"] - kept non-core.
- Methionine salvage KMTB [PMID:18625006 "The aromatic amino acid transaminases, Aro8p and Aro9p, and the branched chain amino acid transaminases, Bat1p and Bat2p, seemed to be the main enzymes exhibiting 4-methylthio-2-oxobutyrate transaminase activity."]; L-isoleucine:2-OG RCA rows MODIFY -> GO:0010326.
- Kradolfer 1982 (PMID:6763508) has no cached abstract; specificity claims rely on UniProt's curation of it.
