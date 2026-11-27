# PAN5 (YHR063C, P38787) notes

## Identity
- 2-dehydropantoate 2-reductase (ketopantoate reductase, KPR), EC 1.1.1.169; ApbA/KPR_N + KPR_C domains (PF02558, PF08546); PANTHER PTHR43765:SF2 [UniProt:P38787].
- Reaction: "Reaction=(R)-pantoate + NADP(+) = 2-dehydropantoate + NADPH + H(+);" [UniProt:P38787]. Function statement is by similarity (ECO:0000250) to E. coli PanE (P0A9J4).

## Function / pathway
- Yeast synthesises pantothenate de novo; the pantoate branch uses Ecm31 (ketopantoate hydroxymethyltransferase) and the beta-alanine branch uses Fms1-dependent polyamine oxidation [PMID:11154694 "Thus, contrary to previous reports, yeast is naturally capable of pantothenic acid biosynthesis"]. The cached abstract does not mention PAN5; the SGD ISS/IC annotations from this paper rest on PanE similarity.
- Pan5 catalyses step 2/2 of (R)-pantoate formation from 3-methyl-2-oxobutanoate [UniProt:P38787 "PATHWAY: Cofactor biosynthesis; (R)-pantothenate biosynthesis; (R)-"].

## Localization
- Cytoplasm by GFP survey [PMID:14562095]. No evidence of mitochondrial localization.
- The IBA "mitochondrion" (PTN001093729, taxon Fungi) has a single donor, SGD:S000002605 = CBS2/YDR197W, a mitochondrial COB translational activator that is a divergent member of PTHR43765 (confirmed by UniProt PANTHER xref query). Mitochondrial location of a translational activator is not a property that should propagate to the cytosolic KPR. The IBA "cytoplasm" at PTN002464833 also lists CBS2 as donor, but PAN5 has its own HDA for cytoplasm.

## Open questions
- No direct enzymology or deletion phenotype for PAN5 found in cached literature; redundancy with other NADPH-dependent reductases (as for E. coli PanE/IlvC) is possible.
