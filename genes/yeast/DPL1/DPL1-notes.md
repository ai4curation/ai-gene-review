# DPL1 (YDR294C) notes

UniProt Q05567, sphinganine/sphingosine-1-phosphate lyase (EC 4.1.2.27), PLP-dependent, integral ER membrane, homo-oligomer [UniProt:Q05567].

- Cloned as BST1, the S1P lyase [PMID:9334171 "A yeast genetic approach was used to clone the first sphingosine phosphate lyase gene, BST1."]; deletion -> sphingoid base sensitivity and S1P accumulation.
- Structure of Dpl1p and activity/substrate residues [PMID:20696404 "We structurally and functionally characterized yeast SPL (Dpl1p)"].
- Committed step of phytosphingosine -> odd-chain fatty acid pathway (PHS-1-P -> 2-hydroxyhexadecanal) [PMID:25345524 "Disruption of the yeast gene encoding long-chain base 1-phosphate lyase, which catalyzes the committed step in the metabolism of phytosphingosine to glycerophospholipids"].
- ER integral, oligomer [PMID:18487605 "confirm it as an integral endoplasmic reticulum-resident protein"; "we demonstrate that Dpl1p exists as an oligomer"].
- Nutrient deprivation response [PMID:10329480 "implicate a role for DPL1 and phosphorylated sphingoid bases in the regulation of global responses to nutrient deprivation in yeast"]; S1P-triggered Ca2+ influx is inhibited by Dpl1 [PMID:11278643 "was inhibited by the functions of S1P lyase (Dpl1p) and the S1P phosphatase (Lcb3p)"].

## Pathway context
- YeastPathways reaction (sphinganine-1-P -> palmitaldehyde + phosphoethanolamine, EC 4.1.2.27) is correct, but the pathway is "sphingolipid biosynthesis (yeast)": Dpl1 is the irreversible exit (degradative) step of sphingoid base metabolism, so the inherited "sphingolipid biosynthetic process" BP is inappropriate; catabolic process is the right BP.
- Peroxisome HDA from PMID:35563734 (Dpl1 not mentioned in main text): likely a proteomic contaminant.
