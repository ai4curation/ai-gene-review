# CDC19 / PYK1 (YAL038W, P00549) notes

## Activity
- Pyruvate kinase 1, EC 2.7.1.40: PEP + ADP -> pyruvate + ATP, last step of glycolysis [UniProt:P00549 "Reaction=pyruvate + ATP = phosphoenolpyruvate + ADP + H(+);"].
- Allosterically activated by fructose-1,6-bisphosphate [UniProt:P00549 "Activated by fructose-1,6-bisphosphate."]; homotetramer; Mg2+ and K+ cofactors.
- Lys240 mechanistic mutagenesis on purified yeast PK [PMID:10413488 "Site-directed mutagenesis was used to change Lys 240 of yeast pyruvate kinase"].
- PKA phosphorylates Pyk1 (and Pyk2), increasing activity [PMID:12063246 "Saccharomyces cerevisiae pyruvate kinase 1 (Pyk1) was demonstrated to be associated to an immunoprecipitate of yeast protein kinase A holoenzyme"].

## Genetics
- pyk1 mutant grows on lactate but not on glucose/fermentable sugars or glycerol [PMID:323230 "The mutant strain is capable of growth when supplied with lactate as the carbon source but not capable of growth when supplied with dextrose or other fermentable sugars or glycerol as the carbon source."].
- Pyk1 is the major PK; Pyk2 is a minor paralog differentially expressed [PMID:21907146 "Yeast possesses two PYK paralogues (PYK1, PYK2) which are differentially expressed between fermentative and oxidative metabolism"]. Low PYK activity raises PEP, which inhibits TPI and redirects flux to PPP -> oxidant resistance (indirect metabolic effect) [PMID:21907146 "PEP acted as feedback inhibitor of the glycolytic enzyme triosephosphate isomerase (TPI)."].

## Location
- Cytosolic; Cdc19-eGFP used as an abundant cytosolic control in split-GFP study [PMID:27385335 "none of five extremely abundant cytosolic proteins exhibits more than a very weak interaction"].
- Plasma membrane proteome hit (PMID:16622836) most likely reflects contamination by an extremely abundant cytosolic enzyme.

## Moonlighting claims
- SESAME complex: Pyk1 with SAM synthetases, serine enzymes and Acs; reported to phosphorylate histone H3T11 [PMID:26527276 "the yeast PKM2 homolog, Pyk1, is a part of a novel protein complex named SESAME"]. Abstract only; histone-kinase activity of pyruvate kinases is debated in the mammalian literature.

## Pathway-context notes
- YeastPathways GLUCFERMEN-PWY RCA propagates "bifid shunt" (Bifidobacterium fructose-6-phosphate phosphoketolase pathway) -- not a yeast pathway; remove.
- GO:0061620 'glycolytic process through glucose-6-phosphate' is obsolete; replace with glycolysis (GO:0006096).
