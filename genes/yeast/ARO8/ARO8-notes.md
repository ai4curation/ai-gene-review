# ARO8 (YGL202W, P53090) notes

Pathway context: aromatic aminotransferase I, final step of Phe/Tyr biosynthesis (EC 2.6.1.57); also 2-aminoadipate (EC 2.6.1.39) and KMTB (methionine salvage) transamination.

- aro8 aro9 double mutant is Phe/Tyr auxotroph; singles are not [PMID:9491082 "aro8 and aro9 double mutants which are auxotrophic for both phenylalanine and tyrosine"; "Neither of the single mutants displays any nutritional requirement on minimal ammonia medium."].
- Broad specificity [PMID:9491082 "In vitro, aromatic aminotransferase I is active not only with the aromatic amino acids, but also with methionine, alpha-aminoadipate, and leucine when phenylpyruvate is the amino acceptor"]; ~half of extract 2-oxoadipate aminotransferase [PMID:9491082 "Its contribution amounts to half of the glutamate:2-oxoadipate activity detected in cell-free extracts"].
- Purified enzyme: AAA-AT [PMID:21982920 "We conclude the enzyme should be categorized as a α-aminoadipate aminotransferase."]; structure, PLP-Lys305, domain-swapped homodimer [PMID:23893908 "Aro8 crystallized with two biologically relevant homodimers"].
- Methionine salvage KMTB transamination [PMID:18625006 "The aromatic amino acid transaminases, Aro8p and Aro9p, and the branched chain amino acid transaminases, Bat1p and Bat2p, seemed to be the main enzymes exhibiting 4-methylthio-2-oxobutyrate transaminase activity."].
- Robot Scientist Adam confirmed YGL202W 2-aminoadipate aminotransferase (PMID:19342587, IDA accepted).
- Mapping errors flagged: GO:0004400 histidinol-phosphate transaminase (RCA; from EC 2.6.1.9 listed on RXN-10814) REMOVE; GO:0052656 L-isoleucine:2-oxoglutarate transaminase (RCA, from R15-RXN EC 2.6.1.88 methionine transamination) MODIFY -> GO:0010326. Chorismate metabolic process (superpathway) REMOVE.
- YeastCyc also attaches HIS5 to RXN-10814 (Phe:2-OG transamination) - see HIS5 review; no yeast evidence for HIS5 in Phe synthesis.
