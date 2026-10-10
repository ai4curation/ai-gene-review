# CPA2 (YJR109C, P03965) notes

Evidence journal built from UniProt and cached abstracts.

- Large (synthetase, CarB-family) subunit of arginine-specific CPSase A; two ATP-grasp domains plus C-terminal MGS-like domain [UniProt:P03965].
- Ammonia-dependent activity of the large subunit alone: [PMID:206535 "The large component catalyzed the synthesis of carbamoylphosphate from ammonia."]; [PMID:206652 "a heavy subunit (mol. wt 80000) capable of catalysing synthesis of carbamoyl phosphate with ammonia as a nitrogen donor"].
- [PMID:8626695 "essentially all of the carboxyl-terminal domain of CPA2 is required for catalytic function"]; [PMID:8626695 "interaction with CPA1 led to an increase in the Vmax of CPA2 in crude extracts."]
- Gene: [PMID:6358221 "A cloned fragment of yeast chromosomal DNA carrying the gene CPA2 coding for the large subunit of arginine-specific carbamyl phosphate synthetase has been sequenced."]
- Cofactor Mg2+/Mn2+ (by similarity) [UniProt:P03965]. Cytoplasmic [UniProt:P03965; PMID:205532].

## Curation decisions
- Core MF: carbamoyl-phosphate synthase (ammonia) activity GO:0004087 (enables) plus contributes_to GO:0004088; in complex GO:0005951; cytosol; arginine biosynthesis.
- Pyrimidine nucleotide biosynthesis IDA -> KEEP_AS_NON_CORE. ATP binding / metal ion binding IEA -> KEEP_AS_NON_CORE.
