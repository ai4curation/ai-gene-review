# NQM1 (YGR043C, UniProt P53228) notes

Module: `pentose_phosphate_pathway` (minor transaldolase, paralog of TAL1). Not in YeastCyc.

## Evidence journal
- Crystal structure and identification as transaldolase [PMID:18831051 "The crystal structure and identification of NQM1/YGR043C, a transaldolase from Saccharomyces cerevisiae."] (title-only cache; UniProt cites it for EC 2.2.1.2 and homodimer [UniProt:P53228]).
- Active in vitro but dispensable under standard growth [PMID:25887987 "While in vitro NQM1 is active on the same substrates, under normal laboratory growth conditions Tal1p is fully sufficient to maintain PPP activity while deletion of its isozyme Nqm1p has no apparent phenotype."]; authors conclude [PMID:25887987 "While NQM1 appears not to function in the pentose phosphate pathway"] (under the conditions tested).
- Glucose-repressed; induced on non-fermentable carbon, caloric restriction, osmotic/oxidative stress; deletion increases H2O2 tolerance [PMID:25887987 "deletion of NQM1 is shown to confer resistance to oxidizing substances."].

## Curation decisions
- Core MF GO:0004801, BP GO:0009052 (conditional/minor), CC cytoplasm.
- Nucleus (IBA, HDA) and oxidative stress (IMP) kept as non-core.
- Module note: the module's characterisation of NQM1 as a minor transaldolase is fine, but PMID:25887987 explicitly says it does not detectably contribute to PPP flux under glucose growth.
