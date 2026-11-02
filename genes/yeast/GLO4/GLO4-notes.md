# GLO4 (YOR040W) notes

UniProt Q12320; mitochondrial glyoxalase II, EC 3.1.2.6; precursor with transit peptide [UniProt:Q12320].

## Evidence journal
- Active Glo4p is in the mitochondrial matrix [PMID:9261170 "The active Glo2p protein is localized in the cytoplasm and the active Glo4p in the mitochondrial matrix"]; active recombinant protein required removal of the transit peptide [PMID:9261170 "to get an active Glo4p protein in E. coli, the putative mitochondrial transit peptide at the N-terminal end had to be removed"].
- Mature N-terminus Met-11 [PMID:10600466 "revealed Met-11 of the primary translation product of the gene as the N-terminal amino acid"].
- Expressed only on glycerol [PMID:9261170 "Whereas the GLO2 gene is expressed on both glucose and glycerol, the GLO4 gene is only active on glycerol"].
- Broad pH profile (6.5-9) vs Glo2 [UniProt:Q12320; PMID:10600466].
- Found in three mitochondrial proteomes (HDA) [PMID:14576278; PMID:16823961; PMID:24769239].

## Decisions
- REMOVE: is_active_in cytosol (RCA, YeastPathways PWY-901). The pathway is modelled as cytosolic and the compartment was propagated to both glyoxalase II paralogues; Glo4 is a matrix enzyme.
- zinc ion binding KEEP_AS_NON_CORE; all else ACCEPT.
