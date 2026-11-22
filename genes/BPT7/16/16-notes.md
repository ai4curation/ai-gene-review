# Bacteriophage T7 Gene 16 (Internal Virion Protein gp16) — Curation Notes

## Overview
Bacteriophage T7 gene *16* (`P03726`, 1,318 aa, ~143.8 kDa) encodes internal virion protein D (gp16), the largest subunit of the cylindrical internal core complex inside the mature T7 capsid (~4 copies per virion) [PMID:6864790, PMID:20036409, PMID:23306440]. At the initiation of infection, gp16 is ejected through the portal-tail channel into the *Escherichia coli* cell envelope along with gp14 and gp15 to assemble the trans-envelope DNA-ejectosome [PMID:16054667, PMID:34214465].

## Structural and Biochemical Functions
1. **N-terminal Peptidoglycan Lytic Exotransglycosylase Domain (aa 1–156)**:
   - Moak & Molineux (2000, 2004) demonstrated that the N-terminal domain of gp16 possesses peptidoglycan lytic transglycosylase (exotransglycosylase) activity that locally cleaves the β-1,4-glycosidic bond between N-acetylmuramic acid and N-acetylglucosamine in the host peptidoglycan sacculus during genome entry [PMID:14763988, "T7gp16 is a 144 kDa internal head protein that is ejected into the cell at the initiation of infection; its enzyme activity is required only when the cell wall is more highly cross-linked."].
   - In the 2.7 Å cryo-EM structure of the periplasmic tunnel (Swanson et al., 2021), the N-terminal peptidoglycan hydrolase domain of gp16 (gp16-N) binds stoichiometrically to the exterior of the hexameric gp15 periplasmic tube [PMID:34214465, "Gp16 promotes gp15 oligomerization, coordinating peptidoglycan hydrolysis, DNA binding, and lipid insertion."].
2. **Inner Membrane Channel and Cytoplasmic Hub (C-terminal region)**:
   - Following ejection, gp16 spans the host cytoplasmic (inner) membrane and extends into the host cytoplasm to form a ~4,200-residue cytoplasmic hub that ratchets the leading end of the T7 genome into the cell at a constant rate (~75 bp/s) [PMID:10926491, PMID:20036409, PMID:23306440, PMID:34214465].

## GO Annotation Review
- **Accept**: `GO:0140100` (`lytic exotransglycosylase activity`), `GO:0098932` (`symbiont entry into host cell via disruption of host cell wall peptidoglycan`), `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`), `GO:0020002` (`host cell plasma membrane`), and `GO:0044423` (`virion component`).
- **Modify**: Broad catalytic terms (`GO:0003824`, `GO:0008933`, `GO:0016787`, `GO:0016829`) to `GO:0140100`; broad biological process terms (`GO:0000270`, `GO:0039678`, `GO:0044409`, `GO:0046718`, `GO:0098994`) to `GO:0098932` and/or `GO:0099002`; broad `GO:0016020` (`membrane`) to `GO:0020002` (`host cell plasma membrane`).
- **Remove**: `GO:0031640` (`killing of cells of another organism`) and `GO:0042742` (`defense response to bacterium`), which are false automated mappings from `KW-0081` (`Bacteriolytic enzyme`); gp16 locally enlarges gaps in the peptidoglycan layer for non-lytic genome entry without lysing the host cell [PMID:14763988].
