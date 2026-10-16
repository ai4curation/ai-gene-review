# ade3 (SPAC6F12.10c, UniProt O14228) notes

Fetch: correct accession fetched (PUR4_SCHPO, O14228, 1323 aa). Naming trap: S. pombe ade3 = FGAM synthase = ortholog of S. cerevisiae ADE6 (genes/yeast/ADE6); S. cerevisiae ADE3 is C1-tetrahydrofolate synthase. The FLCN paper itself notes [PMID:34805795 "Ptr2 and Ade3 homologs (called Ptr2 and Ade6)"].

## Evidence
- [PMID:967158 "an ade3 mutants lacks FGAR amidotransferase"] (MF evidence not represented as an experimental GOA row).
- Cytoplasm: GFP library [PMID:10759889], ORFeome [PMID:16823372]; Golgi HDA from ORFeome.
- TORC1: [PMID:34805795 "Our results revealed that similar to BFC, Ade3, and Ptr2 are required for efficient repression of TORC1 in response to amino acid starvation (Figures 5C and 5D)."]; vacuole relocalisation on starvation [PMID:34805795 "Similarly, we found that Ade3-GFP is diffuse in amino acid replete conditions and localizes to vacuoles when cells are starved of amino acids for 90 min (Figure 6A)."]; authors call it surprising for an enzyme "whose only known activity is in adenine biosynthesis".

## Decisions
- Core MF GO:0004642, BP GO:0006189, cytoplasm - consistent with genes/yeast/ADE6.
- Vacuole membrane, Golgi and negative regulation of TORC1 signaling kept non-core (experimental, condition-dependent or mechanistically unresolved).
