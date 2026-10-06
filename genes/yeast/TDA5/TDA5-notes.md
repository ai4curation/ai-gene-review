# TDA5 (Q06417) notes

Module: `dolichol_phosphate_sugar_donor_supply`, roles = polyprenol dehydrogenase and dolichal reductase (DHRSX type). No YeastCyc reaction.

## Evidence journal
- Functional ortholog of DHRSX [PMID:42201967 "Here, we identified TDA5 as a yeast ortholog of DHRSX."; "Deletion of TDA5 caused glycosylation defects, reduced dolichol levels, and accumulated polyprenol."; "All these phenotypes were rescued by expression of DHRSX, but not by DFG10 or SRD5A3."]
- Residual dolichol implies a bypass [PMID:42201967 "this bypass cannot be explained by the action of Tda5 alone and other factors are likely involved"]
- DHRSX biochemistry [PMID:38821050 "The first and third steps are performed by DHRSX"; "DHRSX has a unique dual substrate and cofactor specificity, allowing it to act as a NAD+-dependent dehydrogenase and as a NADPH-dependent reductase in two non-consecutive steps."]
- DHRSX localises to lipid droplets [PMID:38821050 "Co-staining with a lipid droplet stain revealed that these structures were lipid droplets, consistent with prior high-throughput studies suggesting enrichment of DHRSX in lipid droplets."]
- UniProt: SDR family, 2 TM; location "Mitochondrion membrane" is curator inference (ECO:0000305) [UniProt:Q06417]

## Annotation decisions
- ND root MF: MODIFY to GO:0160196 polyprenol dehydrogenase (NAD+) activity.
- NEW: GO:0160196 (IMP, PMID:42201967) and GO:0043048 dolichyl monophosphate biosynthetic process. Dolichal reductase (GO:0160197) not asserted: no yeast-specific evidence for step 3; raised as a question.
- Mitochondrion HDA x2 and mitochondrial membrane IEA: KEEP_AS_NON_CORE. ER HDA: ACCEPT.
- No direct enzyme assay for Tda5 exists yet.
