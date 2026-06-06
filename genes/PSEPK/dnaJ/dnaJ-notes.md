# dnaJ (Chaperone protein DnaJ / Hsp40) — Pseudomonas putida KT2440

UniProt: Q88DU3 (DNAJ_PSEPK); OrderedLocusNames PP_4726; 375 aa; reference proteome UP000000556.
Evidence level: PE 3 (Inferred from homology). All annotations are propagated by the HAMAP rule MF_01152;
there are no gene-specific experimental publications for the P. putida ortholog. Functional knowledge is
transferred from the well-characterized E. coli DnaJ ortholog (P08622) and the DnaJ family.

## FUNCTION
DnaJ (Hsp40) is the J-domain co-chaperone of the DnaK (Hsp70) chaperone system. It binds unfolded/misfolded
substrate proteins and, via its J-domain, stimulates the ATPase activity of DnaK to drive stable substrate
capture; the cycle is completed with the nucleotide exchange factor GrpE.
- [UniProt "Participates actively in the response to hyperosmotic and heat shock by preventing the aggregation of stress-denatured proteins and by disaggregating proteins, also in an autonomous, DnaK-independent fashion."]
- [UniProt "Unfolded proteins bind initially to DnaJ; upon interaction with the DnaJ-bound protein, DnaK hydrolyzes its bound ATP, resulting in the formation of a stable complex."]
- [UniProt "GrpE releases ADP from DnaK; ATP binding to DnaK triggers the release of the substrate protein, thus completing the reaction cycle."]
- [UniProt "Several rounds of ATP-dependent interactions between DnaJ, DnaK and GrpE are required for fully efficient folding."]
- [UniProt "Also involved, together with DnaK and GrpE, in the DNA replication of plasmids through activation of initiation proteins."]

The J domain drives DnaK ATPase stimulation; the two zinc centers have distinct roles.
- [UniProt "The J domain is necessary and sufficient to stimulate DnaK ATPase activity."]
- [UniProt "Zinc center 1 plays an important role in the autonomous, DnaK-independent chaperone activity of DnaJ. Zinc center 2 is essential for interaction with DnaK and for DnaJ activity."]

## SUBUNIT
- [UniProt "Homodimer."]

## COFACTOR
DnaJ coordinates structural zinc via its cysteine-rich (CR-type) zinc-finger domain (residues 134-212).
- [UniProt "Name=Zn(2+)"]
- [UniProt "Binds 2 Zn(2+) ions per monomer."]
- Eight Cys residues coordinate two Zn(2+): center 1 (C147, C150, C200, C203) and center 2 (C164, C167, C186, C189) per the FT BINDING records.

## SUBCELLULAR LOCATION
- [UniProt "Cytoplasm"]

## DOMAIN ARCHITECTURE
- J domain: residues 5-70 (conserved HPD; here "HPDRN" at ~33-37).
- Gly/Phe-rich linker region.
- CR-type zinc finger: residues 134-212, four CXXCXGXG repeats (147-154, 164-171, 186-193, 200-207).
- C-terminal substrate-binding / dimerization domains.
- [UniProt "Belongs to the DnaJ family."]

## GO REVIEW NOTES
- All seven GOA annotations are IEA (InterPro2GO, UniRule, TreeGrafter, combined IEA). No experimental
  evidence exists for this specific protein, so terms are accepted/refined based on homology to E. coli DnaJ
  and the strong, conserved HAMAP rule.
- ATP binding (GO:0005524, InterPro2GO): DnaJ does NOT itself bind/hydrolyze ATP. It stimulates the ATPase
  activity of DnaK; the ATP-binding partner is DnaK. UniProt lists no ATP-binding feature for DnaJ. This is a
  known erroneous InterPro2GO propagation to the DnaJ family and should be REMOVED (consistent with the
  E. coli DnaJ review, P08622).
- zinc ion binding (GO:0008270): specific and correct (2 Zn per monomer); ACCEPT. No broad "metal ion binding"
  (GO:0046872) annotation is present in this GOA, so none to down-rank here.
- heat shock protein binding (GO:0031072): vague but not wrong — DnaJ binds DnaK (an Hsp70). The more specific
  GO:0051087 "protein-folding chaperone binding" better captures the co-chaperone interaction.
- unfolded protein binding is NOT in this GOA TSV (only in the UniProt DR cross-refs), so it is not reviewed as
  an existing annotation here.

## CORE vs NON-CORE
- Core MF: protein folding chaperone activity / DnaK ATPase stimulation; binding of unfolded substrate and of
  the Hsp70 chaperone DnaK; zinc ion binding (structural).
- Core BP: protein folding, protein refolding, response to heat / cellular response to stress.
- Non-core BP: DNA replication (plasmid/phage initiation) — a downstream application of chaperone activity,
  co-opting the DnaK/DnaJ/GrpE machine; not in this GOA TSV but noted for completeness.
