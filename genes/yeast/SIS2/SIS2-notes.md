# SIS2 / HAL3 (YKR072C, P36024) notes

## Identity
- HFCD superfamily (PPCDC-like) protein; moonlighting: (1) non-catalytically-complete subunit of the heterotrimeric phosphopantothenoylcysteine decarboxylase (PPCDC) with Cab3 (Ykl088w); (2) inhibitory subunit of the Ser/Thr phosphatase Ppz1 [UniProt:P36024].

## PPCDC role
- Active yeast PPCDC is a Cab3 + Hal3/Vhs3 heterotrimer in which each partner contributes one catalytic residue [PMID:19915539 "the active yeast enzyme is a heterotrimer that consists of Ykl088w and Hal3/Vhs3 monomers that separately provides two essential catalytic residues"].
- Hal3/Vhs3 carry the His (oxidative decarboxylation step) and Cab3 carries the Cys [PMID:26514574 "Instead, Hal3 and Vhs3 only contain the His, while Cab3 has the requisite Cys residue, in addition to a non-functional His"]. Hence the correct qualifier for PPCDC activity is contributes_to; homotrimeric Hal3 is inactive.
- Hal3 and Vhs3 are redundant for this role (hal3 vhs3 synthetic lethality) [PMID:15192104 "We have found that the vhs3 and hal3 mutations are synthetically lethal."].
- Part of the larger CoA-synthesizing protein complex: Cab3 binds Sis2 and Vhs3 [PMID:23789928 "Cab3 also binds to Sis2 and Vhs3 that were previously characterized as subunits of phosphopantothenoylcysteine decarboxylase."].

## Ppz1 regulation
- Hal3 binds the C-terminal catalytic domain of Ppz1 and inhibits it in vitro; HAL3 effects on salt tolerance require PPZ1 [PMID:9636153 "In vitro experiments reveal that the protein phosphatase activity of Ppz1p is inhibited by Hal3p."].
- Hal3 binds Ppz1 as a monomer, de-oligomerising from PPCDC trimers [PMID:26514574 "we provide evidence that Hal3 binds Ppz1 as a monomer (1:1 stoichiometry)"].
- Cell-cycle (G1/S) effects of HAL3 overexpression in sit4 mutants are mediated by Ppz1 [PMID:10022927 "We show here that the described effects of HAL3/SIS2 on sit4 mutants are fully mediated by the Ppz1 phosphatase."]. The earlier chromatin association [PMID:7705654] is a fractionation result whose functional relevance was not followed up.

## Notes for module
- Sis2/Vhs3 are the His-donor subunits; Cab3 is the Cys-donor subunit. PPCDC "enables" rows from YeastPathways/IBA should be read as contributes_to.
