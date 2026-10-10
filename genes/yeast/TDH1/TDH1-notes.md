# TDH1 notes (P00360)

Shared GAPDH family evidence (TDH1/TDH2/TDH3 are paralogous NAD+-dependent phosphorylating GAPDHs, EC 1.2.1.12):
- Activity partition among paralogs [PMID:3905788 "The contribution of the TDH1, TDH2, and TDH3 gene products to the total glyceraldehyde-3-phosphate dehydrogenase activity in wild type cells is 10-15, 25-30, and 50-60%, respectively"]; all three active [PMID:3905788 "These data confirm that the three yeast glyceraldehyde-3-phosphate dehydrogenase genes encode catalytically active enzyme"].
- Same relative expression on glucose and ethanol (supports gluconeogenic as well as glycolytic role) [PMID:3905788 "The relative proportions of expression of each gene is the same in cells grown in the presence of glucose or ethanol as carbon source"].
- Tdh2/Tdh3 homotetramers; Tdh3 lower Vmax [PMID:3905788 "The apparent Vmax for the homotetramer encoded by TDH3 is 2-3-fold lower than the homotetramer encoded by TDH2"].
- Cell wall + cytosol [PMID:11158358 "Tdh2 and Tdh3 polypeptides are present in the cell wall, as well as in the cytosol, of exponentially growing cells"]; [PMID:11158358 "Tdh1 is only detected in stationary-phase cells, again in both cytosol and cell wall extracts"].
- Side activity: NAD(P)H hydratase [UniProt:P00360 "FUNCTION: As a side activity, catalyzes the hydration of the"]; NADP binding IEA from IPR006424 judged over-annotation for an NAD-specific GAPDH.
- Peripheral mitochondrial pool [PMID:16962558 "all glycolytic enzymes are associated with mitochondria in yeast"]; minor lipid-particle co-fractionation [PMID:10515935 "glyceraldehyde-3-phosphate dehydrogenase (GAPDH) and Yju3p (the amount of Yju3p was greater than GAPDH)"].
- Melatonin affinity pull-down hit [PMID:31708896 "glyceraldehyde-3-phosphate dehydrogenase (Tdh1p, Tdh2p, Tdh3p; band f)"]; weak affinity-capture evidence marked over-annotated.
- NO/S-nitrosation and apoptosis (TDH2/TDH3 IMP) [PMID:17726063 "NO signalling and GAPDH S-nitrosation are linked with H2O2-induced apoptotic cell death"] (abstract only; kept non-core).

TDH1-specific:
- Stationary-phase/stress-induced minor isoform [UniProt:P00360 "INDUCTION: Expressed when cells enter stationary phase, due to glucose"].
- IPI mitochondrion rows are with ENO1 (SGD:S000003486) and ENO2 (SGD:S000001217): co-IP with anti-enolase [PMID:16962558 "enolase takes part in a large macromolecular complex associated to mitochondria"].

Decisions: ACCEPT GAPDH activity, glycolysis, gluconeogenesis, cytosol/cytoplasm; MODIFY generic oxidoreductase -> GO:0004365 and obsolete GO:0061620 -> GO:0006096; REMOVE bifid shunt; MARK_AS_OVER_ANNOTATED NADP binding, melatonin binding; KEEP_AS_NON_CORE mitochondrion, lipid droplet, cell wall, PM, NAD binding, glucose metabolic process.
