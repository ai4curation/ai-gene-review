# paaJ (P0C7L2) notes, E. coli K-12

## Deep research

`just deep-research ECOLI paaJ --provider falcon` was attempted on 2026-10-23 and failed
("Exception: Failed to authenticate"; all providers failed). No deep-research file exists;
the review is built from cached literature and the UniProt record.

## Function

PaaJ is a bifunctional beta-ketothiolase used twice in the lower phenylacetate pathway:

1. C8 thiolysis: 3-oxo-5,6-dehydrosuberyl-CoA + CoA -> 2,3-dehydroadipyl-CoA + acetyl-CoA (EC 2.3.1.223).
   [PMID:20660314 "A complete conversion of 3-oxo-5,6-dehydrosuberyl-CoA into 2,3-dehydroadipyl-CoA and acetyl-CoA"]
   The expected direct product is the 3,4-isomer; the 3,4 to 2,3 isomerization is probably by PaaG
   [PMID:20660314 "This 3,4–2,3 isomerization reaction probably was catalyzed by enoyl-CoA isomerase PaaG, which was present in the assay."]
   Caveat: the PaaJ used by Teufel et al. was from Pseudomonas sp. strain Y2
   [PMID:20660314 "Recombinant enzymes from Escherichia coli (PaaZ, PaaH) or Pseudomonas sp. strain Y2 (PaaABC(D)E, PaaG, PaaJ, PaaF) were tagged"].
   No GO term exists for EC 2.3.1.223; GO:0003988 (acyl-CoA + acetyl-CoA = CoA + 3-oxoacyl-CoA) covers it generically.
2. Final step: 3-oxoadipyl-CoA + CoA -> succinyl-CoA + acetyl-CoA (EC 2.3.1.174; GO:0033812, an is_a child of GO:0003988).
   [PMID:17259607 "in vivo and in vitro studies revealed that the paaE gene encodes the beta-ketoadipyl-CoA thiolase"]
   (paaE is the P. putida U name of the paaJ ortholog; the abstract covers both P. putida and E. coli; abstract only.)
   [PMID:20660314 "PaaJ finally cleaved 3-oxoadipyl-CoA into the central metabolites succinyl-CoA"]
- E. coli paaJ deletion mutant cannot grow on phenylacetate [PMID:12846838 "paaF, paaG, paaH, paaJ or paaZ gene are unable to grow with phenylacetate as carbon source"].
- No stable complex with PaaF/PaaH [PMID:22961985 "No complex between PaaF, PaaH, and PaaJ, equivalent to the fatty acid β-oxidation complex, was detected."].

## Curation decisions

- GO:0019619 3,4-dihydroxybenzoate catabolic process (InterPro PcaF signature IPR012793): PaaJ
  catalyzes the same 3-oxoadipyl-CoA thiolysis as PcaF of the protocatechuate branch of the
  beta-ketoadipate pathway, but in E. coli the substrate comes from phenylacetate. No
  evidence was found that E. coli K-12 degrades protocatechuate, so this row is marked
  over-annotated. It is not removed because I could not cite a source showing the pathway is absent.
- GO:0006974 DNA damage response (IEP, mitomycin C microarray): marked over-annotated, following the glgX precedent.
- Module conformance: core_functions carry GO:0003988 (C8 thiolysis, no specific term) and GO:0033812.
