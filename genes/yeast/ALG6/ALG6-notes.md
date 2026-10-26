# ALG6 (YOR002W, UniProt Q12001) notes

## Activity / role
- First glucosyltransferase [PMID:8877369 "alg6 mutants accumulate lipid-linked Man9GlcNAc2, suggesting that this locus encodes an endoplasmic glucosyltransferase."]
- Structure and in vitro activity [PMID:32103179 "Here we present the cryo-electron microscopy structure of yeast ALG6 at 3.0 Å resolution, which reveals a previously undescribed transmembrane protein fold."]; catalytic base [PMID:32103179 "Finally, mutating Asp69 to an alanine abolished ALG6 function, and mutating it to an asparagine strongly reduced activity."]
- Lumenal [PMID:32103179 "The final seven steps occur in the lumen of the endoplasmic reticulum (ER) and require dolichylphosphate-activated mannose and glucose as donor substrates"]
- Paralogue of Alg8 [PMID:8877369 "Alg6p has sequence similarity to Alg8p, a protein required for glucosylation of Glc1Man9GlcNAc2."]

## Curation observations
- aerobic respiration IMP (PMID:15794922) is an indirect phenotype of an LLO defect, so MARK_AS_OVER_ANNOTATED [PMID:15794922 "another N-glycosylation mutant with a LLO defect, alg6, was respiratory deficient"].
- The YeastPathways cytosol row is wrong for this lumenal enzyme, so it is REMOVED. ALG6 belongs to the lumenal module, not n_glycan_llo_assembly_cytoplasmic.
