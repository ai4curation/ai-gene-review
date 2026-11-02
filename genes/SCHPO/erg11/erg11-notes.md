# erg11 (SPAC13A11.02c, UniProt Q09736) notes

Module: `ergosterol_biosynthesis` (CYP51); S. cerevisiae ortholog ERG11 (P10614). Fetch verified: Q09736 (CP51_SCHPO).
Naming: UniProt mentions "erg11/cyp1"; the protein is CYP51 (Cyp51A1 in Hughes et al. 2007).

## Evidence
- Essential lanosterol 14alpha-demethylase [PMID:27585850 "Erg11 is a P450 enzyme that catalyzes the key step, lanosterol-14α-demethylation, in the biosynthesis of ergosterol"]; [PMID:27585850 "Tetrad dissection showed that the deletion is lethal"].
- Dap1 binds and activates it [PMID:17276356 "binds and positively regulates Cyp51A1 and Cyp61A1, two P450s required for"].
- Cortical ER + nuclear envelope [PMID:37939137 "As Ost4 and Erg11 localize to both the cortical ER and the nuclear envelope"]; Lem2 interactor [PMID:36799444 "Cho2, Ole1 and Erg11 for Lem2"].

## Curation decisions
- protein binding (Dap1) REMOVE as uninformative; interaction not disputed.
- monooxygenase / paired-donor oxidoreductase IEA MODIFY -> GO:0008398; membrane -> ER membrane.
- UniProt PANTHER xref is PTHR24304:SF2 (labelled 24-hydroxycholesterol 7-alpha-hydroxylase) - a PANTHER labelling quirk worth noting for the module's CYP51 family descriptor.
