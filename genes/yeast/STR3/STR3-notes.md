# STR3 (YGL184C) notes

## Identity
- Cystathionine beta-lyase (Str3p), PLP-dependent, trans-sulfuration enzyme family; EC 4.4.1.13 [UniProt:P53101].
- Reactions: L,L-cystathionine + H2O = L-homocysteine + pyruvate + NH4+ (RHEA:13965) and S-substituted L-cysteine + H2O = thiol + pyruvate + NH4+ (RHEA:18121) [UniProt:P53101].
- C-terminus ends ...NIKSSKL: a canonical PTS1 (-SKL) peroxisomal targeting signal (read from the UniProt sequence).

## Evidence
- Genetic: STR3 disruption blocks conversion of cysteine to homocysteine [PMID:10821189 "yielding yeast strains that cannot convert cysteine into homocysteine"].
- Biochemical: purified Str3p is a PLP-dependent cystathionine beta-lyase that also cleaves cysteinylated thiol precursors (3MH, 4MMP) [PMID:21478306 "Characterization of the enzymatic properties of Str3p confirmed it to be a pyridoxal-5'-phosphate-dependent cystathionine β-lyase"].
- Purified Str3p and Cys3p cleave the cysteine-furfural conjugate to release 2-furfurylthiol [PMID:29436228 "Str3p and Cys3p were able to cleave the cysteine-furfural conjugate to release 2-furfurylthiol"].
- Peroxisomal membrane proteome (MS) identified Str3p (PMID:11565790, abstract only). SGD describes Str3p as a peroxisomal cystathionine beta-lyase possibly redox-regulated by the peroxisomal glutathione transferase Gto1p (https://wiki.yeastgenome.org/index.php/STR3; Barreto et al. 2006, https://pmc.ncbi.nlm.nih.gov/articles/PMC1595348).
- Global GFP screen (C-terminal GFP fusions, which would mask a C-terminal PTS1) reported cytoplasm and nucleus [UniProt:P53101 "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:14562095}. Nucleus"].

## Pathway context
- Second step of forward transsulfuration (cystathionine -> homocysteine), after Str2p. YeastPathways places the reaction in the cytosol; the PTS1 and the peroxisome IDA suggest the step happens in the peroxisome. This compartment discrepancy matters for the module.
- GO:0019346 transsulfuration is obsolete (consider GO:0071269 / GO:0019344); for STR3 the direction is homocysteine synthesis (GO:0071269).
