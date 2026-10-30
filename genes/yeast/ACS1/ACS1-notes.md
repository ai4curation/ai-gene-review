# ACS1 notes (Q01574, YAL054C)

Evidence journal for the ACS1 review (YeastPathways module: pdh_bypass_acetyl_coa_synthesis). No paid deep research was run.

- Activity: acetate + ATP + CoA -> acetyl-CoA + AMP + PPi (EC 6.2.1.1) [UniProt:Q01574]. Both ACS genes encode active enzymes [PMID:8910545 "Saccharomyces cerevisiae contains two structural genes, ACS1 and ACS2, each encoding an active acetyl-coenzyme A synthetase."]
- Kinetics/specificity: high affinity, uses propionate [PMID:8910545 "The Km for acetate of Acs1p was about 30-fold lower than that of Acs2p and Acs1p, but not Acs2p, could use propionate as a substrate."]
- Phenotype: required for growth on acetate, dispensable on ethanol [PMID:1363452 "As expected, the mutant was unable to grow on acetate as sole carbon source."; "disruption of the ACS1 gene did not affect growth on media containing ethanol as the sole carbon source"]
- Nucleocytosolic acetyl-CoA / histone acetylation on non-fermentable carbon [PMID:16857587 "In glycerol with ethanol, Acs1p is an alternate acetyl-CoA source for HATs."; "Yeast mitochondrial and nucleocytosolic acetyl-CoA pools are biochemically isolated."]
- Localization: UniProt lists microsome, cytoplasm, mitochondrion, nucleus [UniProt:Q01574]; mitochondrial proteomics hits (PMID:14576278, PMID:16823961) kept as non-core.

## Curation decisions
- GO:0019654 "pyruvate fermentation to acetate" (IMP, PMID:1363452) -> MODIFY to GO:0045733 acetate catabolic process: the phenotype is failure to use acetate, not to make it.
- Amide-bond ligase (GO:0016880) is an in vitro side reaction (PMID:18305111) -> non-core.
- Ethanol catabolic process (RCA, PWY3O-4300) non-core: ACS1 catalyses the last step but is dispensable on ethanol.
