# IIL1 (Q94AR8, At4g13430) review notes

## Identity
- IPMI large subunit 1 (IPMI LSU1, AtLeuC, MAM-IL1). Single-copy large subunit of the heterodimeric isopropylmalate isomerase (aconitase superfamily; domains 1-3 + [4Fe-4S] cluster). [PMID:19597944 "The genome contains a single gene for the large subunit (At4g13430, IPMI LSU1) and three genes for the small subunits of this enzyme"]
- Domain split: [PMID:19597944 "However, in IPMIs of bacteria, archaea and plants domains 1–3 are found in a large subunit, while domain 4 is found in a small subunit."]
- Heterodimer formation: [PMID:20663849 "We demonstrate here that AtLeuC physically interacts with AtLeuD proteins to form functional IPMIs. The IPMIs are localized to chloroplast stroma."] (abstract only). Caveat: Chen et al. 2021 found no LeuC-LeuD Y2H interaction [PMID:33568694 "However, no interactions could be found between LeuC and any of the LeuDs in our Y2H experiments"].

## Dual pathway role (shared subunit)
- [PMID:19597944 "Metabolic profiling of large subunit mutants revealed accumulation of intermediates of both Leu biosynthesis and Met chain elongation, and an altered composition of aliphatic glucosinolates demonstrating the function of this gene in both pathways."]
- Leu: [PMID:19597944 "The IPMI substrate, 2-IPM, accumulates when transcript of IPMI LSU1 is reduced sufficiently."]
- GSL: [PMID:19493961 "In this study we found that knocking out either of the candidate genes, AtleuC1 or AtIMD1 , reduced the level of Met-GSLs, indicating that both genes are actually involved in Met-GSL biosynthesis."]
- Pathway specificity is set by the small subunit: [PMID:19597944 "Thus, the resulting IPMI heterodimer is pathway-specific even if the large subunit per se is not."]; [PMID:32612621 "The function of IPMI is defined by the small subunits."]
- No in vitro enzyme assay of Arabidopsis IPMI in the cached literature; MF assignments rest on mutant metabolite accumulation [PMID:19493961 "In addition, a high-throughput in vitro enzyme assay system is required for further confirmation of predicted gene function."]

## Localization
- Chloroplast stroma (proteomics + He 2010). [PMID:19597944 "In Arabidopsis the latter protein has also been detected in the stroma fraction of chloroplasts by a proteomic study"]
- Expression along vasculature [PMID:24608865 "The promoter of IPMI LSU1 showed relatively high activity mainly in or along the vasculature, similar to the promoters of IPMI SSU2 and IPMI SSU3"]

## Curation decisions
- All MF/BP/CC annotations accepted except GO:0050486 intramolecular hydroxytransferase (IMP, Sawada 2009) -> MODIFY to GO:0120528 (EC 4.2.1.170 is a hydro-lyase; GO has a specific term).
- NEW: GO:0009316 3-isopropylmalate dehydratase complex (IPI, PMID:20663849) to capture subunit semantics. The large subunit is a structural/catalytic component, so this is not a substrate/necessity inference.
- Core functions expressed as contributes_to (complex-level activity) for GO:0003861 (with SSU1, Leu) and GO:0120528 (with SSU2/SSU3, glucosinolates).
- Falcon deep research not available at time of review.
