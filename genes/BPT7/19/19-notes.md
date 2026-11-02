# Bacteriophage T7 Gene 19 (Large Terminase Subunit gp19) — Curation Notes

## Overview
Bacteriophage T7 gene *19* (`P03694`, 586 aa, ~66.1 kDa) encodes the DNA maturation protein gp19, the large subunit of the viral terminase complex (TerL) (`GO:0098009`, `viral terminase, large subunit`) [PMID:6864790, PMID:23632014].

## Structural and Biochemical Functions
1. **Pentameric ATP-Driven DNA Translocation Motor**:
   - Daudén et al. (2013) determined the cryo-EM structure of T7 gp19 and showed that five subunits assemble into a toroidal pentamer surrounding a central dsDNA-accommodating channel and dock onto the dodecameric gp8 portal vertex of the prohead [PMID:23632014, "The terminase is a powerful motor that converts ATP hydrolysis into mechanical movement of the DNA. Here, we have determined the structure of the T7 large terminase by electron microscopy. The five terminase subunits assemble in a toroid that encloses a channel wide enough to accommodate dsDNA."].
   - Its N-terminal ATPase domain binds ATP (`GO:0005524`, `ATP binding`) and catalyzes ATP hydrolysis (`GO:0016887`, `ATP hydrolysis activity`) to drive translocation of concatemeric viral dsDNA into the procapsid (`GO:0019073`, `viral DNA genome packaging`) [PMID:3298244, PMID:23632014].
2. **C-terminal Endonuclease Domain for Concatemer Maturation**:
   - Its Mg2+/Mn2+-dependent (`GO:0046872`, `metal ion binding`) C-terminal RNase H-fold nuclease domain cleaves concatemeric T7 DNA at specific terminal repeat boundaries (`pac` sites) once a unit-length genome is packaged (`GO:0004519`, `endonuclease activity`) [PMID:3298244, PMID:23632014].

## GO Annotation Review
- **Accept**: `GO:0004519` (`endonuclease activity`), `GO:0005524` (`ATP binding`), `GO:0016887` (`ATP hydrolysis activity`), `GO:0019073` (`viral DNA genome packaging`), `GO:0046872` (`metal ion binding`), and `GO:0098009` (`viral terminase, large subunit`).
- **Modify**: Refine `GO:0000166` (`nucleotide binding`) to `GO:0005524` (`ATP binding`), refine `GO:0004518` (`nuclease activity`) to `GO:0004519` (`endonuclease activity`), and refine `GO:0016787` (`hydrolase activity`) to `GO:0016887` (`ATP hydrolysis activity`) and `GO:0004519` (`endonuclease activity`).
- **Remove**: `GO:0051276` (`chromosome organization`), which is an inappropriate cellular chromosome organization term mapped via UniRule; bacteriophage T7 gp19 packages viral concatemeric DNA into procapsids (`GO:0019073`).
