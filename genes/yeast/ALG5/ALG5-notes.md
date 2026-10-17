# ALG5 (YPL227C, P40350) notes

Pathway context: dolichol-phosphate sugar donor supply (YeastPathways PWY3O-1565, UDP-Glc + Dol-P -> Dol-P-Glc + UDP, EC 2.4.1.117).

- Activity: Dol-P-Glc synthase. [PMID:8076653 "This enzyme catalyzes the transfer of glucose from UDP-glucose to dolichyl phosphate."]
- Genetics: overexpression raises, deletion abolishes activity; CPY underglycosylated. [PMID:8076653 "whereas a deletion of the yeast gene leads to a loss of this activity and a concomitant underglycosylation of carboxypeptidase Y"]
- alg5 mutants accumulate non-glucosylated LLO. [PMID:6369318 "alg5 and alg6 mutants accumulated Man9GlcNAc2"]
- Topology: catalytic domain cytoplasmic. [PMID:9560251 "Alg5p is a type II transmembrane protein with both N and C termini in the cytoplasm, which synthesizes dolichol-phosphoglucose from dolicholphosphate and UDP-glucose"]; UniProt note: UDP-Glc interaction at the cytoplasmic side, Dol-P-Glc used in the lumen [UniProt:P40350].
- Drosophila wol/ALG5 partially complements yeast alg5 hypoglycosylation (source of the yeast IMP for N-glycosylation). [PMID:18403407 "The wol/ALG5 cDNA was able to partially complement the hypoglycosylation phenotype of alg5 mutant S. cerevisiae"]

Curation observations
- RCA "cytosol" (is_active_in) is a pathway-converter default; changed to cytoplasmic side of ER membrane (GO:0098554).
- RCA "carbohydrate biosynthetic process" is generic; marked over-annotated.
- No GO term exists for "dolichyl glucosyl phosphate biosynthetic process" (unlike GO:0180047 for Dol-P-Man); GO:0006488 used as process.
