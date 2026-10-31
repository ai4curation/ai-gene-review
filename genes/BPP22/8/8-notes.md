# Gene 8 (SCAF_BPP22, P26748) Notes

## Overview
- **Gene symbol:** `8`
- **UniProt ID:** `P26748` (`SCAF_BPP22`)
- **Protein name:** Scaffolding protein (gp8; Coat protein 8; Gene product 8)
- **Length:** 303 AA

## Function & Structural Insights
- **Procapsid Inner Core & Assembly Chaperone/Adaptor:** Approximately 250–300 copies of gp8 co-assemble with 415 copies of the major coat protein (gp5) and 12 copies of the portal protein (gp1) to form the T=7 icosahedral procapsid, where gp8 forms an internal scaffolding core required for high-fidelity capsid assembly [PMID:9792844, PMID:10764583, PMID:21220301].
- **Portal Oligomerization & Nucleation:** Scaffolding protein catalyzes the oligomerization of monomeric portal protein (gp1) into dodecameric rings and forms a nucleation complex with the portal vertex (10 scaffolding proteins interacting with the 12-fold portal ring) to initiate procapsid assembly and ensure incorporation of a single portal ring per capsid [PMID:21220301, PMID:30787152].
- **C-terminal Helix-Loop-Helix Coat-Binding Domain:** NMR (PDB: `1GP8`, `2GP8`) and cryo-EM (PDB: `2XYY`, `8I1T`) structures show that the C-terminal ~30 residues (residues 269–303) fold into an amphipathic helix-loop-helix (helix-turn-helix) motif stabilized by a hydrophobic core with a highly positively charged surface face that binds electrostatically to the negatively charged N-arm of coat protein gp5 [PMID:9792844, PMID:10764583, PMID:21220301, PMID:36851569].
- **Exit During DNA Packaging & Recycling:** Upon headful viral DNA packaging, intact gp8 molecules exit through pores in the procapsid lattice without proteolysis, relieving electrostatic screening and permitting procapsid expansion into the mature capsid; released gp8 is recycled for subsequent rounds of procapsid assembly [PMID:9792844, PMID:21220301].
- **Translational Autoregulation & Ejection Protein Recruitment:** Also required for recruitment of internal ejection proteins (gp7, gp16, gp20) into the procapsid and autoregulates its own translation via its N-terminal domain [file:genes/BPP22/8/8-uniprot.txt].

## Domains & Orthology
- **InterPro:** `IPR015385` (`Phage_P22_Gp8_scaffold`), `IPR027393` (`Virus_scaffolding_prot_C`)
- **Pfam:** `PF09306` (`Phage-scaffold`, 1 hit)
- **Gene3D:** `G3DSA:4.10.810.10` (`SCAF_BPP22_C`, 1 hit)

## Curation Decisions
- **Existing annotations:** None (`8-goa.tsv` is empty). Do not fabricate `ND` rows.
- **Core function:** `GO:0030674` (`protein-macromolecule adaptor activity`) directly involved in `GO:0019068` (`virion assembly`) and `GO:0046797` (`viral procapsid maturation`), supported by `PMID:9792844`, `PMID:10764583`, `PMID:21220301`, `PMID:30787152`, and `PMID:36851569`.
