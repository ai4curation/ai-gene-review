# PAA1 (YDR071C, UniProt Q12447) notes

## Function
- GNAT acetyltransferase, AANAT subfamily; "Acetylates spermine and probably also other polyamines such as putrescine or spermidine" [UniProt:Q12447].
- Polyamine acetyltransferase: "The recombinant Paa1 protein readily acetylates various polyamines such as putrescine, spermidine, and spermine." [PMID:15723835]
- In vivo target: "When Paa1 is overexpressed, leading to a lower level of spermine, cells show a growth dependence on either of two downstream compounds in the coenzyme A pathway, pantothenate or beta-alanine." [PMID:15723835]
- Secondary arylalkylamine (AANAT) activity in vitro: "It was found to have enzyme activity generally typical for AANAT family members, although the substrate preference pattern was somewhat broader, the specific activity was lower, and the pH optimum was higher." [PMID:11559708]
- Chromatin link is a hypothesis: "These phenotypes suggest that acetylation of polyamines removes them from chromatin and makes the chromatin more accessible." [PMID:15723835]
- Cytoplasmic (HDA) [UniProt:Q12447; PMID:14562095]. Reproducible interactions with PP2C phosphatases Ptc2/Ptc3/Ptc4 (IntAct, NbExp 6-9) [UniProt:Q12447].

## Pathway context
- No YeastPathways reaction for PAA1 in projects/YEAST_PATHWAYS/data/yeastpathways_summary.yaml; no GO-CAM activity.
- Module polyamine_metabolism: PAA1 as diamine N-acetyltransferase (GO:0004145); consistent.

## Decisions
- ACCEPT GO:0004145 IDA/IMP (core). KEEP_AS_NON_CORE GO:0004059 IDA/IBA (in vitro secondary activity).
- MODIFY generic N-acetyltransferase (ARBA) and acyltransferase (InterPro GNAT) to GO:0004145.
- MARK_AS_OVER_ANNOTATED chromatin organization IMP (indirect, inferred from genetic interactions; abstract-only).
- REMOVE 16 protein binding IPI rows (Ptc2/3/4), per repo policy for GO:0005515.
