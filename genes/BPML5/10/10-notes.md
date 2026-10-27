# Mycobacteriophage L5 Gene 10 (Endolysin A / LysA, Q05285) Notes

## Overview
- **Gene symbol**: `10`
- **UniProt ID**: `Q05285` (`ENLYS_BPML5`)
- **Length**: 292 AA (32.4 kDa)
- **Organism**: Mycobacterium phage L5 (`NCBITaxon:31757`)

## Function and Modular Architecture
- L5 gp10 is the Endolysin A (LysA) peptidoglycan hydrolase encoded at the left end of the L5 lysis cassette (genes `10`-`11`-`12`), which in Cluster A mycobacteriophages is located to the left of the virion structural and assembly genes [PMID:19555454, "Of the 53 phages with a siphoviral morphotype, the thirteen genomes constituting Cluster A [including L5, D29, Bxb1 (Hatfull & Sarkis, 1993, Ford et al., 1998, Mediavilla et al., 2000) and Che12 (Hatfull et al., 2006)] have the lysis cassette situated to the left of the virion structural and assembly genes, whereas all of the other genomes have the lysis cassette positioned to the right of the structural genes (Fig. 1C)."].
- Payne & Hatfull (2012) classified L5 gp10 as an Organization-C (`Org-C`) endolysin composed of an N-terminal `N4` peptidase domain (homologous to the mycobacterial cell-wall peptidase RipA / Rv1477) and a C-terminal `C1` cell-wall-binding motif, lacking a central glycoside hydrolase/muramidase domain [PMID:22470512, "The observation that some organizations lack the central catalytic domain (Org-C, Org-H, Org-M, and Org-T) is consistent with the interpretation that the N-terminal domains are important for peptidoglycan hydrolysis. These are all relatively small proteins (<325 aa) and include the smallest of the mycobacteriophage endolysins, L5 gp10 and Saintus gp5, which are 292 and 225 residues respectively."].
- Following holin (gp11)-mediated permeabilization of the host cytoplasmic membrane, gp10 accesses and cleaves the mycobacterial peptidoglycan meshwork (`GO:0009253` `peptidoglycan catabolic process`) to mediate `GO:0044659` (`viral release from host cell`) in concert with LysB (gp12).
- `GO:0042742` (`defense response to bacterium`) is a spurious keyword mapping from `KW-0081` (`Antimicrobial`) and is removed (`REMOVE`).
