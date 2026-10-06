# MAE1 notes (P36013, YKL029C)

Evidence journal (module context: gluconeogenesis; YeastCyc assigns malate + NAD+ -> pyruvate + CO2 + NADH, EC 1.1.1.38).

- Sole malic enzyme; knockout abolishes activity [PMID:9603875 "Disruption of open reading frame YKL029c, which is homologous to malic enzyme genes from other organisms, abolished malic enzyme activity in extracts of glucose-grown cells."]
- Cofactor: assayed with NADP+; reported to use both [PMID:9603875 "malic enzyme from S. cerevisiae has been reported to use both NAD + and NADP + as electron acceptors"]
- Mitochondrial [PMID:9603875 "Subcellular fractionation experiments indicated that malic enzyme in S. cerevisiae is a mitochondrial enzyme."]; matrix [UniProt:P36013]
- Role: pyruvate provision for biosynthesis, redundant with pyruvate kinase [PMID:9603875 "Mutants lacking both enzymes could be rescued by addition of alanine or pyruvate to ethanol cultures."]

## Curation decisions / module observations
- Three RCA rows assign L-malate dehydrogenase (NAD+) (EC 1.1.1.37, malate -> oxaloacetate) to Mae1p -> REMOVE (wrong reaction; MDH1-3 account for all MDH activity, PMID:1447211).
- Cytosol RCA (PWY3O-94) -> REMOVE (mitochondrial enzyme).
- Gluconeogenesis and aerobic respiration RCAs -> over-annotated: Mae1p runs malate -> pyruvate, opposite to C2 gluconeogenic flux; not a TCA enzyme.
- Module curator: MAE1 does not belong in the core of a gluconeogenesis module in S. cerevisiae; better placed as an anaplerotic/pyruvate-supply step.
