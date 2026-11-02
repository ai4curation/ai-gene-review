# EPT1 (YHR123W, P22140) notes

## Identity
- sn-1,2-diacylglycerol ethanolaminephosphotransferase, EC 2.7.8.1 (also 2.7.8.2 in vitro); CDP-alcohol phosphatidyltransferase family; multi-pass membrane protein [UniProt:P22140].

## Evidence
- Distinct CPT1/EPT1 enzymes; double null lacks both activities but is viable [PMID:1847919 "The Saccharomyces cerevisiae CPT1 and EPT1 genes are structural genes encoding distinct sn-1,2-diacylglycerol choline- and ethanolaminephosphotransferases."]
- Broad aminoalcohol specificity [PMID:1847919 "The EPT1 gene product utilized CDP-ethanolamine, -monomethylethanolamine, -dimethylethanolamine, and -choline to significant extents"].
- ept1 mutants lose most EPT activity; overexpression raises it [PMID:2848840 "The ethanolaminephosphotransferase activities in membranes prepared from ept1 and ept2 mutants were reduced 30- to 90-fold"]; dual activity [PMID:2848840 "the EPT1 gene product possesses both ethanolamine- and cholinephosphotransferase activities"].
- UniProt: does not substantially contribute to PC synthesis in vivo [UniProt:P22140].
- Localization: Golgi (GFP, PMID:14562095), ER (PMID:26928762 HDA).

## Curation decisions
- Core: GO:0004307 + PE biosynthesis; cholinephosphotransferase/PC rows non-core.
- Cytosol RCA rows removed (integral membrane protein).
- protein binding (Ept1-Cpt1 paralog interaction, three HTP/interactome papers) removed per policy.
