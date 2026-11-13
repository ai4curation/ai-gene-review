# LSC1 (YOR142W, P53598) notes

- Alpha subunit of succinyl-CoA ligase; both LSC genes required for activity [PMID:9874242 "Succinyl-CoA ligase activity was absent in mitochondria isolated from strains deleted for one or both LSC genes"].
- Yeast enzyme is ATP-specific [PMID:9874242 "The yeast succinyl-CoA ligase was shown to utilize ATP but not GTP for succinyl-CoA synthesis"]. S. cerevisiae has one beta subunit (Lsc2).
- => IBA GO:0004776 (GDP-forming) from the shared animal alpha-subunit node removed: contradicted for yeast.
- Phenotype: lsc mutants grow on acetate but are impaired on glycerol/pyruvate [PMID:9874242 "growth on glycerol or pyruvate was impaired"].
- Alpha binds CoA and phosphate (By similarity) [UniProt:P53598].

## 2026-11-11 re-review from an evolutionary perspective

Scope: LSC1 and LSC2 together with their PANTHER families (PTHR11117 alpha, PTHR11815 beta) and the other reviewed members (S. pombe SPAC16E8.17c and SPCC1620.08, P. putida sucC and sucD, human SUCLA2).

- The alpha family is rooted at LUCA (PTN000122012). The eukaryotic clade (PTN000122014) branches from within the bacterial sequences, below a horizontal-transfer node, as sister to Proteobacteria [PANTHER release 19 tree, read with genes/yeast/LSC2/LSC2-bioinformatics/scs_family_evolution.py].
- The alpha subunit does not set nucleotide specificity [PMID:9765290 "Because the two succinyl-CoA synthetases incorporate the same alpha-subunit, the determinants of nucleotide specificity must reside within the beta-subunit"].
- So a nucleotide-specific term on an alpha subunit depends on which beta subunits the genome encodes. Fungi kept only the A-type (SUCLA2-lineage) beta subunit [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "Fourteen of fifteen fungal genomes in the tree, including S. cerevisiae, S. pombe, Candida albicans, Neurospora crassa, Cryptococcus neoformans and the chytrid Batrachochytrium dendrobatidis, encode only an A-type beta subunit."].
- Consequence for the GO:0004776 (GDP-forming) IBA: REMOVE is kept, now argued from the node. The placement at the root is defensible (animal and Dictyostelium seeds have a G-type beta partner; E. coli and P. aeruginosa seeds have a dual-specificity enzyme [PMID:10671455 "Scs synthesizes essentially an equimolar amount of ATP and GTP"]), but the fungal branch PTN000874203 needs pruning. Recorded in the family review as NEEDS_PRUNING with member exceptions for LSC1 and SPAC16E8.17c.
- Physiological consequence of having no GDP-forming enzyme: matrix GTP must be imported [PMID:36012783 "Because in yeast, succinyl-CoA ligase produces ATP instead of GTP"].
- The role is conserved across kingdoms [PMID:16270230 "These three cDNAs were used to complement the respective Saccharomyces cerevisiae mutants deficient in the alpha- and beta-subunit, demonstrating that they encode functionally active polypeptides"].
- Acetate phenotype refined [PMID:21246628 "Deletion of any of the genes for the enzymes solely involved in the TCA cycle (IDH1, KGD1 and LSC1), except for SDH1, caused little defect in acetate utilization on YNBA but resulted in significant growth impairment on YPA"].
- OpenScientist run (LSC1-hypotheses/alpha-gdp-forming-partner-availability): supports removal of GO:0004776 and pruning of the fungal branch. It dated the beta duplication to the animal lineage from pairwise identities and PMID:9765291; the local trees put it earlier (Dictyostelium and Monosiga have both copies). The annotation decision is the same either way. The run knew the gene and the hypothesis, so it is a second reading of the same evidence, not independent evidence.
- Mitochondrial matrix was not added as a NEW row. Lsc1 already carries mitochondrial nucleoid (a matrix structure), and the only yeast-specific sub-compartment evidence beyond that is the rule-based transit peptide; the S. pombe orthologs carry matrix as a PomBase IC.
- Deep research: only the OpenScientist provider was available in this session (no falcon/perplexity keys). Literature was searched through PubMed directly (queries: "LSC1 OR LSC2 OR succinyl-CoA ligase/synthetase AND yeast"; succinyl-CoA synthetase nucleotide specificity; Fraser ME and Lambeth DO author searches).
- Not done: gene reviews for human SUCLG1 and SUCLG2 and E. coli sucC/sucD, which are the PAINT seeds for the nucleotide-specific terms.
