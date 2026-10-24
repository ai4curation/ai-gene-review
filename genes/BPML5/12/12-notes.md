# Mycobacteriophage L5 Gene 12 (Endolysin B / LysB, Q05328) Notes

## Overview
- **Gene symbol**: `12`
- **UniProt ID**: `Q05328` (`LYSB_BPML5`)
- **Length**: 254 AA (28.8 kDa)
- **Organism**: Mycobacterium phage L5 (`NCBITaxon:31757`)

## Function and Structural Homology to D29 LysB
- L5 gp12 is the Endolysin B (LysB) mycolylarabinogalactan esterase located at the right end of the L5 lysis cassette (`10`-`11`-`12`) [PMID:19555454, "Mycobacteriophages accomplish this by producing two lysis enzymes, Lysin A (LysA) that hydrolyses peptidoglycan, and Lysin B (LysB), a novel mycolylarabinogalactan esterase, that cleaves the mycolylarabinogalactan bond to release free mycolic acids."].
- Payne et al. (2009) determined the crystal structure and enzymatic activity of the closely related Cluster A phage D29 gp12 (LysB, `O64205`), showing an alpha/beta hydrolase fold (`IPR029058`) with a cutinase-like Ser82-Asp166-His240 catalytic triad and a C-terminal four-helix lipid-binding linker domain (`IPR041855`) [PMID:19555454, "The D29 LysB structure shows an alpha/beta hydrolase organization with a catalytic triad common to cutinases, but which contains an additional four-helix domain implicated in the binding of lipid substrates."]; [PMID:19555454, "The catalytic triad Ser82-Asp166-His240 is located at the edge of the central β-sheet between the α/β sandwich and the linker domain."].
- All three catalytic triad residues (Ser82, Asp166, His240) and the G-Y-S-Q-G pentapeptide motif (`AGYSQGAIV` at residues 79-87) are strictly conserved in L5 gp12 (`FT   ACT_SITE 82`, `166`, `240`) [file:BPML5/12/12-uniprot.txt, "Cleaves the ester linkage joining the mycolic acid-rich outer membrane to arabinogalactan, releasing free mycolic acids."].
- `GO:0016787` (`hydrolase activity`) is refined (`MODIFY`) to `GO:0052689` (`carboxylic ester hydrolase activity`), `GO:0031640` (`killing of cells of another organism`) is refined (`MODIFY`) to `GO:0044659` (`viral release from host cell`), `GO:0003824` (`catalytic activity`) is marked `TOO_GENERAL`, and `GO:0042742` (`defense response to bacterium`) is removed (`REMOVE`).
