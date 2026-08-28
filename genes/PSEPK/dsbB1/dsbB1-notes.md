# dsbB1 curation notes

## Evidence boundary and GO direction

The KT2440 DsbB1 function and localization statements are explicitly marked
"By similarity" and the entry has protein-existence level 3. The review
therefore describes this paralog as predicted rather than directly assayed
[file:genes/PSEPK/dsbB1/dsbB1-uniprot.txt, "Acts by oxidizing the DsbA protein
(By similarity)."].

The official GO definition for GO:0015035 is "Catalysis of the reaction: a
protein with reduced sulfide groups = a protein with oxidized disulfide bonds."
The equality is direction-neutral, so the term is retained as a valid non-core
oxidoreductase annotation rather than interpreted as an oxidation-specific
activity. GO:0009055 electron transfer activity is ranked as core because DsbB
relays electrons from DsbA to quinone.

Canonical *E. coli* experiments show respiratory-chain-dependent DsbA oxidation
acting through DsbB [PMID:9342327, "These results suggest that the respiratory
electron transfer chain participates in the oxidation of DsbA, by acting
primarily on DsbB."] and direct DsbB-catalyzed oxidation of DsbA by ubiquinone
[PMID:12853466]. These studies ground the family mechanism; they do not directly
test the KT2440 paralog.
