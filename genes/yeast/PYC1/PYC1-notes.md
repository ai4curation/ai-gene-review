# PYC1 (YGL062W, P11154) review notes

## Evidence journal
- Two PC isozymes; PYC1 is the originally characterised gene. pyc1 nulls keep 10-20% PC activity [PMID:2039506 "The mutants were found to have 10-20% residual pyruvate carboxylase activity"]; anaplerotic role [PMID:2039506 "anaplerotic role in the production of oxaloacetate from pyruvate"].
- No bypass: double mutant needs aspartate on glucose [PMID:1921979 "simultaneous disruption of both genes resulted in inability to grow on glucose as sole carbon source, unless aspartate was added to the medium"].
- PYC1 is the major isozyme: [PMID:8185321 "the pyc1 null strain showed a 3- to 4-fold lower level of Pyc activity"]; pyc1 null cannot grow on ethanol without aspartate [PMID:8185321].
- Cytosolic, unlike animal PC [PMID:2665820 "pyruvate carboxylase was found to be a cytosolic enzyme in both yeasts"; PMID:196563; PMID:2039506 "located exclusively in the cytoplasm"].
- Biotin and Zn cofactors, homotetramer, interacts with PYC2 and RSP5 [UniProt:P11154].

## Pathway observations
- YeastCyc places PYC1/2 in TCA-EUK-PWY -> "aerobic respiration" (over-annotation; anaplerotic, cytosolic) and PWY3O-7 -> "L-homoserine biosynthetic process" (superpathway inflation). ASPBIO-PWY -> "L-aspartate biosynthetic process" kept as non-core (supplies the oxaloacetate that Aat2 transaminates).
- For the threonine module PYC1/PYC2 are an upstream anaplerotic entry (oxaloacetate supply), not part of the aspartate-family pathway itself.
- No biotin-binding GO annotation exists in GOA despite the biotinyl-lysine; raised as a question.
- protein binding rows (PYC2 heteromer, RSP5 WW array) were removed per policy; the PYC1-PYC2 heteromer is real.
