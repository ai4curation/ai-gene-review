# PSA1 (VIG9/MPG1/SRB1, YDL055C, P41940) notes

Pathway context: dolichol-phosphate sugar donor supply; YeastPathways PWY3O-123 assigns Psa1 to "Man-1-P + GDP + H+ -> GDP-Man + Pi" (EC 2.7.7.22).

- Activity is GTP-dependent GDP-mannose pyrophosphorylase (EC 2.7.7.13). [PMID:11055399 "The Saccharomyces cerevisiae VIG9 gene encodes GDP-mannose pyrophosphorylase, which synthesizes GDP-mannose from GTP and mannose-1-phosphate."] [PMID:9195935 "We demonstrated the enzyme activity of Vig9 protein using a recombinant fusion protein produced in Escherichia coli."]
- vig9 is glycosylation defective; null lethal; ts allele has cell wall defect. [PMID:9195935 "A genomic DNA fragment that complements a newly identified protein glycosylation-defective mutation, vig9, of Saccharomyces cerevisiae was cloned."] [PMID:11055399 "These results indicated a critical role of GDP-mannose in maintenance of cell-wall integrity."]
- Cytoplasmic [UniProt:P41940]; very abundant (97,100 molecules/cell) [UniProt:P41940].

Curation observations
- YeastCyc reaction mis-assignment: EC 2.7.7.22 (GDP + Pi) vs the demonstrated EC 2.7.7.13 (GTP + PPi). RCA GO:0008928 "mannose-1-phosphate guanylyltransferase (GDP) activity" REMOVED. The module curator should use EC 2.7.7.13 / GO:0004475.
