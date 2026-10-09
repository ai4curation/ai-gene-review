# MLO2 (Arabidopsis thaliana, Q9SXB6, At1g11310) notes

Sources: UniProt, GOA (12 rows), falcon deep research, cached papers (full text:
PMID:35794475, 37767715, 38124479, 28674541; abstract only: 10677553, 16525893,
16732289, 32156686). New PMIDs verified via PubMed citation lookup.

## Identity / structure
- Clade V MLO, co-ortholog of barley MLO with MLO6, MLO12; 7TM, cytosolic C-terminal CaMBD
  [file:ARATH/MLO2/MLO2-deep-research-falcon.md "MLO2 is a plant-specific, seven-transmembrane protein"].
- PM localization: [PMID:38124479 "Here, MLO2-GFP co-localized with mCherry-EXO70H4 in PM speckles and the cell wall"].
  Golgi-associated puncta reported by deep research (Qin 2020; abstract-only cache, not quoted directly).

## Molecular function
- Ca2+ channel, heterologous: [PMID:35794475 "we used patch-clamp to directly measure transport activity of AtMLO2 and recorded large inward currents that depended on external Ca2+ concentrations"];
  [PMID:35794475 "We also found that AtMLO2 was permeable to Ba2+ and Mg2+, but not to K+ or Na+"].
- CaM feedback: [PMID:35794475 "A dramatic inhibition of Ca2+ entry was observed in all cases"].
- CAM2 binding, LW/RR mutant reduces binding in most assays [PMID:37767715].

## Process (necessity, not participation in defense)
- [PMID:16732289 "Here, we demonstrate a conserved requirement for MLO proteins in powdery mildew pathogenesis"].
- mlo2 partial, triple full resistance [PMID:38124479 "mlo2-5 (∼64%) mutants supported significantly lower levels of host cell entry compared to Col-0, while mlo2-5 mlo6-2 mlo12-1 triple mutants were completely resistant (∼0%)"].
- [PMID:28674541 "our results point to a role of Arabidopsis MLO2, MLO6, and MLO12 in enabling defense suppression during invasion by adapted powdery mildew fungi"].
- Trichome wall/EXO70H4 phenotype is triple-mutant only [PMID:38124479].

## Decisions
- defense response (IEA) and defense response to fungus (IMP) -> MODIFY to GO:0031348
  negative regulation of defense response (consistent with HORVU/MLO review).
- GO:0031348 IMP ACCEPT; response to fungus KEEP_AS_NON_CORE.
- ND MF -> MODIFY; NEW calcium channel activity (IDA PMID:35794475), calmodulin binding (IDA PMID:37767715).
- extracellular region (HDA) and chloroplast (ISM) REMOVE; Golgi, plasmodesma KEEP_AS_NON_CORE.
- No NEW BP terms: no defense term passes participation; calcium ion transmembrane
  transport not added because only heterologous evidence and in planta role unknown.
