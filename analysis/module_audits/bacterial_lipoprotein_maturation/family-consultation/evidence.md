# Lipoprotein family consultation — 2026-11-07

This audit separates conserved reaction chemistry, whole-protein fusion activities, and species-dependent physiological compatibility. The frozen eight gene reviews are comparators, not experimental evidence for themselves. No gene review or original source was changed.

## Tree and membership findings

`tree-inspection.json` records exact cached-tree hashes and descendant membership. PTHR30589/PTN000778741 contains all 39 resolved leaves, including E. coli P60955 and Bacillus O34752. PTHR33695/PTN002134743 contains all 38 resolved leaves, including P00804 and Q45479. PTHR38686/PTN002214718 contains all 25 resolved leaves, including P23930. These are the limited cached reference trees, not exhaustive inventories. KT2440 representatives have official inventory membership but no leaf in these trees. Do not interpret that absence as a loss.

The three Lnt-associated nodes PTN000092528, PTN002459128 and PTN000557706 are absent from the cached Lnt tree. Their assertions occur in the frozen PAINT slice and also in other family slices; exact descent cannot be inferred from GOA absence. Node IDs, term IDs, IBD codes, dates and ordered seed lists remain unchanged. No evolutionary loss is invented.

The frozen reviewed-entry inventories contain 536 Lgt SF0, 421 LspA SF1 and 92 Lnt SF1 entries. These are not counts of every extant family member. Official names are checked separately from descriptive biological names. The generated membership index is an independent classification check, not a source of function evidence.

## Primary evidence and manual findings

- PMID26729647 (full cached text): recombinant E. coli Lgt structure, in-vitro diacylglyceryl transfer and depletion-strain complementation support reaction and membrane architecture. The gene/source audit documents the BL21-derived construct and tags; this is not a purified unmodified KT2440 or Bacillus assay.
- PMID42126242 (full cached text): tested heterologous Lgt rescue depends on enzyme expression, Lpp and host context. Exact excerpt: “only fully complement the E. coli Lgt depletion strain in the absence of Lpp.” The result concerns the tested Salmonella Lgt construct in the E. coli depletion host. It does not prove loss of the native Salmonella chemical activity. The study does not directly assay Bacillus subtilis Lgt. Family chemistry remains coherent without a universal compatibility assertion.
- PMID26912896 (abstract available): Pseudomonas aeruginosa structural/mutational evidence states “Mutagenesis studies identify LspA as an aspartyl peptidase.” This is comparative evidence, not a direct KT2440 assay. PMID10497172 (abstract available) independently reports Bacillus mutagenesis and proposes Asp102/Asp129 as catalytic residues; do not overstate that older experiment as a complete mechanism determination.
- PMID1894646 (abstract available): E. coli PhoA/LacZ fusions support four membrane crossings. These are topology assays, not evidence from a gene name.
- PMID21676878 and PMID28885614 (full cached texts): purified E. coli Lnt transfers a phospholipid-derived acyl group to the free N-terminal amino group of diacylglyceryl-modified apolipoprotein; structure places a nitrilase-like catalytic domain outside the cytoplasmic membrane. Native lipid specificity and heterologous complementation are distinct from the conserved reaction genus.
- PMID17416655 (abstract available): actinomycete proteins failed the tested E. coli complementation context. This cannot establish their intrinsic catalytic inactivity. The acquired official O53493 and A0QZ13 records independently provide curated publication-linked evidence for mycobacterial Lnt chemistry.

## Fusion versus domain evidence

The newly acquired official UniProt records and retrieval URLs/hashes are recorded in `uniprot-provenance.json`; existing source files were not refreshed. O53493 FUNCTION and DOMAIN statements distinguish N-acyltransferase and C-terminal polyprenol-phosphate mannose synthase activities (PubMed11931640,12427759,19661058). The latter has experimentally curated broad lipid-monophosphate substrate usage and a curated dolichyl-phosphate reaction mapping. This supports the biological seed protein without proving family-wide propagation of the exact GO term.

A0QZ13 is a standalone mycobacterial Lnt. Its publication-linked statement says it enhances Ppm1 activity “without itself having PPM synthase catalytic activity”. Thus some unfused proteins can contribute to a Ppm1 system without catalyzing the glycosyltransferase reaction. Neither whole-protein domain fusion nor a shared nitrilase fold proves that all Lnt proteins have another domain's catalytic activity. Conversely, alternative physiological substrate preference is not evidence that every member lacks a secondary amidase reaction. GO0050126 scope is therefore UNRESOLVED, replacing the unsupported blanket negative.

## Ontology findings

`ontology.json` preserves official QuickGO responses and URLs. GO0009003 is active signal peptidase activity, defined by cleavage of hydrophobic N-terminal signals from exported proteins. GO0004190 is the aspartic endopeptidase mechanism. Both refine GO0004175 through separate axes; one is not a substitute for the other. The new manual GO0009003 family assessment is not an invented PAINT assertion. A lipoprotein-specific proposed subtype can retain residual specificity without claiming that signal peptidase activity has no GO term.

GO0016747 is the fitting broad acyltransferase genus for Lnt. GO0140186 instead specifies acyl-CoA and lysyl N6; it is not the phospholipid-to-N-terminal-cysteine reaction. GO0004582 uses dolichyl phosphate and GO0050126 specifies N-carbamoylputrescine hydrolysis; their exact substrate constraints matter. Absence of canonical Lnt does not imply absence of all N-acylation systems in Bacillota (including the independently reviewed LhaT pathway).

## Remaining limits

No loss-free statement is extrapolated beyond the frozen PAINT slice. Three cross-domain Lnt nodes remain unresolved. Abstract-only sources are explicitly identified above and were not represented as full-text reads. This family assessment supports conserved enzyme identity; complete native maturation pathways require the actual species-specific machinery and compatible substrates.

The official release-19 Mycobacterium classification assigns O53493 to PTHR43398:SF1, while UniProt assigns PTHR38686:SF1. The exact classified row and source hash are retained in `fusion-classification.json`; this supports domain-specific membership provenance, not an inferred PAINT lineage.
