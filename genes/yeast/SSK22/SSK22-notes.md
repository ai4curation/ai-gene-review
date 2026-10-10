# SSK22 (YCR073C, UniProt P25390) curation notes

## Identity
- Serine/threonine-protein kinase SSK22 (MAP kinase kinase kinase SSK22), STE family MAPKKK; kinase domain aa 1034-1310 [file:yeast/SSK22/SSK22-uniprot.txt]. Paralog of SSK2 (lacks Ssk2's extra N-terminal ~176 aa).
- Low abundance (56 molecules/cell) [file:yeast/SSK22/SSK22-uniprot.txt "Present with 56 molecules/cell in log phase SD medium."].

## Function: redundant MAP3K of the Sln1 branch
- Pbs2 activation by Ssk2 and Ssk22 [PMID:7624781 "Pbs2p was activated by MAP kinase kinase kinases (MAPKKKs) Ssk2p and Ssk22p that are under the control of the SLN1-SSK1 two-component osmosensor."].
- Either MAPKKK suffices; complementation of ssk2 ssk22 ste50 by SSK22 [PMID:9742096 "Either SSK2, SSK22, or STE11 MAPKKK can activate PBS2 by phosphorylation."].
- Ssk22 kinase domain binds Pbs2 docking site RSD-I [PMID:12853477 "The Pbs2 docking site constitutively bound the Ssk2/Ssk22 kinase domain."].
- Ssk1 binds Ssk2/Ssk22 N-terminal regulatory domain [PMID:18573873 "Ssk1 binds to an N-terminal regulatory domain of the Ssk2/Ssk22 MAPKKKs, as demonstrated by both two-hybrid analyses and coprecipitation assays"].
- Unlike Ssk2, Ssk22 activation strictly depends on Ssk1; weaker than Ssk2 in salt stress [PMID:23457455 "The activation of Ssk22p, on the other hand, was totally dependent on Ssk1p."; "Actually, upon nonionic osmotic stress, the Ssk2p and Ssk22p can function equally well."].
- Ssk22 not required for Ssk2's actin recovery role; Ssk22 fragment does not bind actin in two-hybrid [PMID:12181352].
- Any Ssk22-specific function unknown [PMID:18573873 "Also, whether the apparently redundant Ssk22 has any specific function is unknown."].

## Localization
- No Ssk22-specific imaging; GOA has ND for CC plus IEA cytoplasm. Operates with cytoplasmic Ssk1/Pbs2.

## Annotation decisions
- Kinase MF rows (HDA, IEA, ISS, EC, Rhea): ACCEPT.
- GO:0038066 rows: ACCEPT.
- Protein binding x3 (Ssk1; HTP): REMOVE (interaction real, no informative MF term).
- NEW GO:0007234 osmosensory signaling via phosphorelay pathway: Ssk22 is directly activated by Ssk1 like Ssk2 (which carries this term by IGI/IPI); the Ssk1 dependence of Ssk22 is shown in PMID:23457455. Comparator: Ssk2 (same role) carries it; Pbs2/Hog1 (further downstream) do not.
