# adh4 (SPAC5H10.06c, UniProt Q09669) notes

## Identity
- Iron-activated group III ADH family [UniProt:Q09669 "Belongs to the iron-containing alcohol dehydrogenase"], ortholog of S. cerevisiae ADH4; PANTHER PTHR11496:SF102. UniProt gives Zn2+ cofactor by similarity only.
- Transcript induced by zinc deficiency (UniProt, PMID:18203864, not cached).

## Mitochondrial ethanol oxidation
- [PMID:16999687 "exhibit antimycin A-sensitive oxygen uptake activity that is exclusively dependent on ethanol"]
- Matrix location from detergent latency [PMID:16999687 "which demonstrates that the enzyme is located in the matrix"].
- [PMID:16999687 "we show conclusively that the novel mitochondrial ADH is encoded by adh4"].
- Also mitochondrial in the ORFeome YFP screen (HDA PMID:16823372).

## Back-up fermentative ADH
- Induced in adh1 null cells [PMID:15040954 "ADH4-like gene product (SPAC5H10.06C named adh4(+))"]; adh1 adh4 double null non-fermentative [PMID:15040954 "only these two ADHs produce ethanol for fermentative growth"].
- Open issue: how a matrix enzyme supports cytosolic fermentation (shuttle? relocalisation?). Not resolved by cached abstracts.
- adh4 is NOT in the PomBase fermentation GO-CAM (gomodel:678073a900000393); the module lists it as the iron-ADH variant.

## Review decisions
- ARBA carboxylic acid catabolic process REMOVED (ethanol is not a carboxylic acid; no evidence).
- All experimental rows accepted. Considered NEW ethanol catabolic process (GO:0006068) for the mitochondrial oxidation, but left as a suggested question (PomBase curators did not add it; S. pombe cannot grow on ethanol).
- Core functions differ from S. cerevisiae ADH4 review (which uses Ehrlich leucine catabolism): S. pombe-specific evidence is for mitochondrial ethanol oxidation and back-up fermentation.
