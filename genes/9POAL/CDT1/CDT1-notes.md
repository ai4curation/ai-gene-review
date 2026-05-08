# CDT1 (MsCDT1) - Miscanthus sinensis - Notes

## Gene Identity

- UniProt: B5BSU2 (CDT1_MISSI)
- Gene: CDT1 (also MsCDT1)
- Organism: Miscanthus sinensis (Chinese silver grass)
- Taxon: NCBITaxon:62337
- Protein: 55 AA, cysteine-rich peptide (15/55 = 27.3% Cys residues)
- Family: CYSTM1 (Pfam: PF12734), PANTHER: PTHR35470
- PANTHER subfamily: PTHR35470:SF6 (CYSTEINE-RICH TRANSMEMBRANE MODULE 2)

## Key Literature

### PMID:19017626 - Kuramata et al. (2009) Plant Cell Physiol
- Original identification of DcCDT1 from Digitaria ciliaris growing in a former mining area
- Isolated via functional screening using Cd-sensitive ycf1 yeast mutant
- DcCDT1 encodes 55 AA peptide with 15 Cys residues (27.3%)
- Five homologs (OsCDT1-OsCDT5) identified in rice, all upregulated by CdCl2 treatment
- GFP fusions show DcCDT1 and OsCDT1 targeted to cytoplasmic membranes AND cell walls
- Transgenic Arabidopsis overexpressing DcCDT1 or OsCDT1 showed Cd-tolerant phenotype
- Mechanism: prevents entry of Cd into cells, limiting cellular accumulation
- Also confers Cu tolerance (CuCl2)
- [PMID:19017626 "DcCDT1 and OsCDT1 function to prevent entry of Cd into yeast and plant cells and thereby enhance their Cd tolerance"]

### PMID:19816106 - Matsuda et al. (2009) Plant Signal Behav
- Commentary/review on the CDT family
- Monocots have multiple CDT homologs (rice has 5), dicots have only 1
- Confirmed plasma membrane and cell wall targeting via GFP fusions
- Cd tolerance via lowered accumulation in transgenic Arabidopsis
- [PMID:19816106 "Constitutive expression of DcCDT1 or OsCDT1 confers Cd-tolerance to transgenic A. thaliana plants by lowering the accumulation of Cd in the cells"]

## ISS Reference Proteins

The ISS annotations on MsCDT1 are transferred from two experimentally characterized proteins:

### A9ZPI1 (DcCDT1 - Digitaria ciliaris)
- The original CDT1 from southern crabgrass
- Experimentally characterized: function (IDA), subcellular location (IDA)
- Evidence: PMID:19017626, PMID:19816106
- Same subfamily as OsCDT1 (PTHR35470:SF12)

### Q5VRD7 (OsCDT3 - Oryza sativa)
- Rice CDT3, experimentally characterized
- Plasma membrane localized, involved in ALUMINIUM tolerance (PMID:23888867)
- Same PANTHER subfamily as MsCDT1 (PTHR35470:SF6)
- Note: CDT3 was characterized for Al tolerance, not just Cd

### Q5VSB5 (OsCDT1 - Oryza sativa)
- Rice CDT1, characterized in PMID:19017626
- In PANTHER subfamily SF12 (different from MsCDT1 which is in SF6)

## PANTHER Subfamily Note

MsCDT1 (B5BSU2) is in PTHR35470:SF6, same as OsCDT3 (Q5VRD7), OsCDT5, and indica CDT3/CDT5.
DcCDT1 (A9ZPI1), OsCDT1 (Q5VSB5), and OsCDT2 are in PTHR35470:SF12.
This means MsCDT1 is phylogenetically closer to CDT3/CDT5 than to CDT1 from crabgrass/rice,
despite sharing the name "CDT1". The ISS transfers from Q5VRD7 (CDT3, same subfamily) are
phylogenetically more appropriate than those from A9ZPI1 (DcCDT1, different subfamily).

## Protein Features

- Single transmembrane helix (residues 24-40)
- CYSTM domain (PF12734)
- Highly cysteine-rich C-terminal region: CECCLDCLCCCCS
- Predicted to chelate heavy metals via cysteine residues at plasma membrane

## Mechanism of Action

Based on the literature, CDT proteins function by:
1. Localizing to the plasma membrane and cell wall
2. Chelating heavy metal ions (Cd2+, Cu2+, possibly Al3+) via cysteine-rich regions
3. Preventing metal ion entry into the cell
4. Reducing intracellular metal accumulation
