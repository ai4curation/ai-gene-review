# ECR (CER10/AtTSC13/AOD2; At3g55360; Q9M2U2) review notes

## Identity and function
- Very-long-chain enoyl-CoA reductase, TSC13/TECR ortholog; final step of elongation cycle [PMID:15829606 "ECR is an enzyme that catalyzes the last step of VLCFA elongation, reduction of the enoyl-CoA, in eukaryotic cells."].
- Complements yeast tsc13; interacts with Elo2p/Elo3p [PMID:14673020 "AtTSC13 is shown to interact physically with the Elo2p and Elo3p components of the yeast elongase complex"].
- cer10 mutants: reduced wax, altered seed TAG and sphingolipid VLCFAs; involved in all VLCFA elongation [PMID:15829606 "demonstrating in planta that ECR is involved in all VLCFA elongation reactions in Arabidopsis"]; developmental defects attributed to sphingolipids.
- Functional GFP-ECR on ER membrane [PMID:15829606 "confirming that GFP-ECR is localized to the ER membrane"].
- Interacts with PAS2 by BiFC [PMID:18799749].
- glh6 is a cer10 allele; trichome papillae/branching defects possibly indirect [PMID:24014871].

## GO term check
- GO:0009922 fatty acid elongase activity = condensation (KCS) step per current definition, so the IMP GO:0009922 for ECR is the wrong step -> MODIFY to GO:0102758.

## Reference problem
- PMID:1847001 (wax biosynthetic process IMP, TAIR 2003) resolves to "Chrysotile asbestos and health in Zimbabwe" (verified via PubMed esummary). WRONG_IDENTIFIER; likely intended Koornneef et al. 1989 J Hered cer mutant paper (no PMID found via esearch). Biology accepted on the basis of PMID:15829606.

## Decisions
- MODIFY: fatty acid elongase activity (IMP) -> GO:0102758.
- REMOVE: protein binding (IPI).
- MARK_AS_OVER_ANNOTATED: cytosol (HDA).
- KEEP_AS_NON_CORE: trichome branching, trichome papilla formation, cutin-based cuticle development (all IMP, PMID:24014871).
- ACCEPT: all others (ER, ER membrane, elongase complex, enoyl-CoA reductase, VLCFA biosynthesis, sphingolipid metabolism, wax biosynthesis x2, IEA parents).
