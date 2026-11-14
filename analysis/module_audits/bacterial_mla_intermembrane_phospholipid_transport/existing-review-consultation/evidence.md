# Existing Mla panel: evidence and identity scope

Consulted 2026-11-07. Existing publication, UniProt and provider files were not refreshed.

## Pseudomonas putida KT2440 Ttg2D structure

Official RCSB polymer entity: https://data.rcsb.org/rest/v1/core/polymer_entity/5UWB/1
Official SIFTS mapping: https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/5uwb
Official ligand: https://data.rcsb.org/rest/v1/core/nonpolymer_entity/5UWB/2

The deposited 5UWB polymer canonical sequence contains all 215 residues of frozen Q88P91 followed by LEHHHHHH. Its source organism is KT2440 (taxon 160488), and its expression host is Escherichia coli. The structure uses selenomethionine; normalization of MSE to M permits this sequence comparison. SIFTS maps both chains to Q88P91 residues 1–215 with identity 1.0. This establishes the target protein, not a native KT2440 transport assay.

The 5UWB ligand entity is named "DI-PALMITOYL-3-SN-PHOSPHATIDYLETHANOLAMINE" (component PEF). The paper describes re-refinement of 4FCZ density as suggestive of tetra-acyl, cardiolipin-like lipid. Thus lipid occupancy and a hydrophobic binding cavity are supported; the chemical identity and native stoichiometry must not be overstated from this model alone.

PMID28388411 calls 5UWB "re-refined coordinates for 4FCZ". Its binding experiments establish interaction with MlaC; the discussion's complete handoff sequence is a model. Later PMID34873038,39080293 and40168124 measure different transfer segments and contexts.

## Assays and direction

PMID39080293 Fig5 caption says: "Fluorescence increase corresponds to a reduction in NBD-PE FRET quenching by Rhodamine-PE as lipids are transferred from the MlaA proteoliposome to the MlaFEDB proteoliposome." Its running text mis-expands PE as phosphatidyl glycerol. The reporter is NBD-PE, not NBD-PG. Reconstituted proteoliposome transport and K-12 BW25113 mutant rescue are distinct experiments, neither a direct KT2440 assay.

PMID40168124 says: "We demonstrate that OmpF3–MlaA simultaneously recruits apo MlaC and phospholipids, thus greatly enhancing lipid transfer to MlaC in solution." It also says "there is no preferential loading of either of the two lipid classes in solution" for PE and PG. Overexpressed and endogenously tagged MlaC are nevertheless PG-enriched; endogenous work uses BW25113 and purified OmpF–MlaA comes from BL21 expression. The native PG-enrichment mechanism is unresolved.

PMID30284446 abstract reports purified MlaD-to-MlaC phospholipid transfer. This is positive donor handoff evidence, not merely binding, but does not by itself demonstrate the complete GO0120014 membrane-to-membrane carrier activity of MlaD without the rest of the pathway. The cached abstract is the consulted source; no unseen full-text assay details are claimed.

## Ontology and complex roles

Official snapshots GO_0120014.json, GO_0120010.json, GO_1990531.json, GO_0031234.json, GO_0006974.json and GO_0015914.json were retrieved from https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:NNNNNNN. Each snapshot retains the definition, identity, current status and child relationships. GO0120014 requires membrane/particle removal, aqueous shielding in a hydrophobic pocket and delivery to an acceptor membrane/particle. MlaFEDB contribution and MlaC carrier activity are distinguished. Isolated-protein inactivity alone is not a universal annotation rule. GO1990531 explicitly requires a P-type ATPase complex; the ABC complex replacement corrects mechanism, not a hierarchical refinement. GO0120010 is an is_a child of GO0015914.

## MlaB stress context

PMID20128927 full text tests K-12 derivatives AB1157/DM4100, including yrbB transposon stress-survival and complementation. The unchanged nalidixic-acid MIC does not eliminate the survival phenotype. Whether MlaB executes a DNA-damage-induced response or supplies constitutive envelope protection is unresolved; DNA damage response is broader than DNA repair. Neither membrane localization nor the number of PAINT seed proteins disproves this process.
