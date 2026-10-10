# ARG3 (YJL088W, P05150) notes

- Ornithine carbamoyltransferase, EC 2.1.3.3: "Reaction=carbamoyl phosphate + L-ornithine = L-citrulline + phosphate +" [UniProt:P05150]; gene cloned: "The yeast arg3 gene, coding for ornithine carbamoyltransferase" [PMID:7029528].
- Location: soluble (cytosolic) in S. cerevisiae, in contrast to the mitochondrial acetylated-cycle enzymes [PMID:205532]. UniProt: "SUBCELLULAR LOCATION: Cytoplasm." Mammalian, Neurospora and S. pombe OTCases are mitochondrial, so the IBA "mitochondrion" (PTN000150427) is a compartment mismatch for budding yeast -> REMOVE with propagation_review.
- Epiarginase regulation: "In the presence of ornithine and arginine, ornithine carbamoyltransferase (OTCase) and arginase form a one-to-one enzyme complex in which the activity of OTCase is inhibited whereas arginase remains catalytically active" [PMID:12679340]. Complex term GO:1903269 accepted; bare protein binding IPI to CAR1 removed as uninformative (interaction itself is real).

## Curation decisions
- Core MF GO:0004585; BP GO:0006526 + GO:0019240 (citrulline is the direct product); CC GO:0005829.
- Generic IEA (amino acid metabolic process; carboxyl/carbamoyltransferase) MODIFY to specific; amino acid binding over-annotated.
