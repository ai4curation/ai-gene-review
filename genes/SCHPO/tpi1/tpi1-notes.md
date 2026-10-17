# tpi1 (S. pombe, UniProt P07669, SPCC24B10.21) notes

Role in module `emp_glycolysis`: triose-phosphate isomerase step (EC 5.3.1.1); S. cerevisiae counterpart TPI1.

## Evidence
- Reaction GAP <-> DHAP [UniProt:P07669 "Reaction=D-glyceraldehyde 3-phosphate = dihydroxyacetone phosphate;"].
- Cloned by complementation of S. cerevisiae tpi1 [PMID:3912263 "Gene tpi, encoding the glycolytic enzyme triose phosphate isomerase (TPI) from the fission yeast Schizosaccharomyces pombe was cloned by complementation of a Saccharomyces cerevisiae tpil mutant."] (abstract only; the paper is mainly about transcription start sites).
- Cytosol by ORFeome screen [PMID:16823372 "we determined the localization of 4,431 proteins"].

## Curation decisions
- IGI to obsolete GO:0061621 -> MODIFY to GO:0006096.
- GO:0046166 G3P biosynthetic process (IBA) kept non-core, as for S. cerevisiae TPI1.

## GO-CAM note
- The PomBase glycolysis model 663d668500002302 contains two tpi1 activity nodes (663d668500002432 and 68b0f0d000002382), both triose-phosphate isomerase activity in cytosol part_of GO:0061621; apparent duplicate.
