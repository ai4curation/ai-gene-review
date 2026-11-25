# DFG10 (P40526) notes

Module: `dolichol_phosphate_sugar_donor_supply`, role = polyprenal reductase (SRD5A3). No YeastCyc reaction.

## Evidence journal
- Polyprenal, not polyprenol, reductase [PMID:38821050 "The SRD5A3 yeast orthologue Dfg10 also shows activity on polyprenal but not on polyprenol."]
- dfg10 lipid phenotype [PMID:38821050 "We first measured polyisoprenoid levels from Dfg10-deficient yeast, and noted a 4-fold decrease in dolichol, accompanied by a 36-fold increase in polyprenol and a 45-fold increase in polyprenal"]
- Ortholog of SRD5A3, glycosylation defect [PMID:20637498 "This experiment shows that SRD5A3 is the diverged human ortholog of the yeast DFG10 gene"]
- Non-steroid substrate [PMID:20637498 "This study also illustrates that the predicted steroid 5-alpha reductase domain is involved in the reduction of a non-steroid lipid"]

## Annotation decisions
- ISS 3-oxo-5-alpha-steroid 4-dehydrogenase: MODIFY to GO:0160198 polyprenal reductase.
- Dolichol-linked oligosaccharide biosynthesis (IBA, IMP): KEEP_AS_NON_CORE (upstream supplier of the carrier).
- Lipid metabolic process / CH-CH oxidoreductase IEA: MODIFY to specific terms. Pseudohyphal growth IMP: KEEP_AS_NON_CORE.
