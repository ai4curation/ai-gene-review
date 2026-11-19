# TDH2 notes (P00358)

Shared GAPDH family evidence (TDH1/TDH2/TDH3 are paralogous NAD+-dependent phosphorylating GAPDHs, EC 1.2.1.12):
- Activity partition among paralogs [PMID:3905788 "The contribution of the TDH1, TDH2, and TDH3 gene products to the total glyceraldehyde-3-phosphate dehydrogenase activity in wild type cells is 10-15, 25-30, and 50-60%, respectively"]; all three active [PMID:3905788 "These data confirm that the three yeast glyceraldehyde-3-phosphate dehydrogenase genes encode catalytically active enzyme"].
- Same relative expression on glucose and ethanol (supports gluconeogenic as well as glycolytic role) [PMID:3905788 "The relative proportions of expression of each gene is the same in cells grown in the presence of glucose or ethanol as carbon source"].
- Tdh2/Tdh3 homotetramers; Tdh3 lower Vmax [PMID:3905788 "The apparent Vmax for the homotetramer encoded by TDH3 is 2-3-fold lower than the homotetramer encoded by TDH2"].
- Cell wall + cytosol [PMID:11158358 "Tdh2 and Tdh3 polypeptides are present in the cell wall, as well as in the cytosol, of exponentially growing cells"]; [PMID:11158358 "Tdh1 is only detected in stationary-phase cells, again in both cytosol and cell wall extracts"].
- Side activity: NAD(P)H hydratase [UniProt:P00358 "FUNCTION: As a side activity, catalyzes the hydration of the"]; NADP binding IEA from IPR006424 judged over-annotation for an NAD-specific GAPDH.
- Peripheral mitochondrial pool [PMID:16962558 "all glycolytic enzymes are associated with mitochondria in yeast"]; minor lipid-particle co-fractionation [PMID:10515935 "glyceraldehyde-3-phosphate dehydrogenase (GAPDH) and Yju3p (the amount of Yju3p was greater than GAPDH)"].
- Melatonin affinity pull-down hit [PMID:31708896 "glyceraldehyde-3-phosphate dehydrogenase (Tdh1p, Tdh2p, Tdh3p; band f)"]; weak affinity-capture evidence marked over-annotated.
- NO/S-nitrosation and apoptosis (TDH2/TDH3 IMP) [PMID:17726063 "NO signalling and GAPDH S-nitrosation are linked with H2O2-induced apoptotic cell death"] (abstract only; kept non-core).

TDH2-specific:
- Chromatin association by HyCCAPP/ChIP, condition-independent [PMID:27184763 "Both Tdh2 and Rpa190 showed enrichment compared to the negative control, but no significant difference between the two growth conditions"] -> promoter-specific chromatin binding MARK_AS_OVER_ANNOTATED.
- Protein binding IPI with ubiquitin (UBI4) from ubiquitin-conjugate proteomics [PMID:15699485 "we identified 127 proteins that are candidate substrates for the 26S proteasome"] -> REMOVE (uninformative; substrate status).

Decisions: as TDH1 plus REMOVE protein binding, MARK_AS_OVER_ANNOTATED promoter-specific chromatin binding, KEEP_AS_NON_CORE nucleus, apoptotic process, ROS metabolic process.

## QA pass (2026-11-19)

- Glucose metabolic process is TOO_GENERAL in the review (entailed by the accepted glycolysis/gluconeogenesis rows).
- ROS metabolic process (IMP, PMID:17726063) changed KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED: the reason already argued an indirect effect, and GAPDH has no ROS-metabolising activity [PMID:17726063 "Blockage of NO synthesis with Nomega-nitro-L-arginine methyl ester leads to a decrease of GAPDH S-nitrosation and of intracellular reactive oxygen species (ROS) accumulation, increasing survival"]. Not removed (abstract only).
- Added the SGD description (deep-research-sgd) and PMID:24292082 (GAPDH-derived antimicrobial peptides) as references, with the antimicrobial-peptide sentence in the description, matching TDH1.
- Extended the truncated UniProt CC:FUNCTION quotes. Status set to COMPLETE.
