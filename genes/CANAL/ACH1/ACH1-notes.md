# ACH1 evidence notes

- The PTHR43609 PAINT batch places the fungal ACH1 enzyme at PTN000484586 for
  `GO:0003986` acetyl-CoA hydrolase activity, `GO:0006083` acetate metabolic
  process, and `GO:0008775` acetate CoA-transferase activity; PTN000484602 is
  the Ascomycota mitochondrial placement. Candida albicans ACH1 is P83773 in
  the same PTHR43609:SF1 subfamily as S. cerevisiae ACH1.
- Carman et al. 2008 directly tested C. albicans ACH1. The ach1 deletion strain
  had mild, complemented growth defects on acetate and ethanol, ACH1 was induced
  on acetate/ethanol/glycerol, and CaACH1 complemented S. cerevisiae ach1,
  supporting a conserved role in acetate/acetyl-CoA metabolism. [PMID:18689527]
- The old hydrolase name is misleading as the sole activity. Fleck and Brock
  2009 re-characterized S. cerevisiae Ach1p and found strongest CoASH transfer
  from succinyl-CoA to acetate, with only minor acetyl-CoA hydrolase activity,
  arguing that fungal Ach1 proteins act as mitochondrial CoA-transferases in
  acetate detoxification. [PMID:19298859]
- Vylkova et al. 2011 found ACH1 in a C. albicans screen for mutants defective
  in environmental alkalinization and confirmed that ach1 loss delays
  neutralization of acidic amino-acid medium. This supports the CGD pH-response
  process row as a real phenotype, but the phenotype is downstream of ACH1
  carbon metabolism rather than a distinct molecular activity. Current GO has
  `GO:0045852 pH elevation` under `GO:0006885 regulation of pH`, but existing
  pH-elevation terms cover internal pH changes rather than fungal
  alkalinization of the extracellular medium. [PMID:21586647]
- UniProt curates C. albicans ACH1 as cytoplasmic from Pitarch et al. 2004
  proteomics, while CGD and PAINT carry mitochondrial and cytosolic placements
  inferred from S. cerevisiae Ach1. The mitochondrial call best matches the
  fungal CoA-transferase model; the cytoplasm/cytosol calls are retained as
  secondary localization evidence. [file:CANAL/ACH1/ACH1-uniprot.txt]
