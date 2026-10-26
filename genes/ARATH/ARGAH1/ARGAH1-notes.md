# ARGAH1 annotation review notes

Identity: P46637 / At4g08900. Verified fetched PANTHER PTHR11358 ARGINASE/AGMATINASE and SF26 GUANIDINO ACID HYDROLASE, MITOCHONDRIAL. This plant implementation differs from the animal/fungal PTHR43782 family; functional restriction is needed, not a family-name transfer.

PMID:32754173 full text provides actual AtARGAH1 crystal/product-binding and solution SAXS data. Binuclear manganese site, hexamer, and neighboring-subunit contribution to substrate binding are direct. The existing GO:0000287 magnesium annotation is a precise ion-identity error: MODIFY to GO:0030145 manganese ion binding. All magnesium mentions concern MgCl2 in the Medicago crystallization recipe, not bound Mg in AtARGAH1. Generic metal binding is refined to manganese. Hexamerization is a core biochemical property. No extrapolation that every possible Mg association has been disproved.

PMID:7770544 cache contains bibliographic text only (full-text fetch failed); later primary sources independently establish the catalytic claim. PMID:18425591 abstract directly reports ARGAH1 pollen enzyme activity, not ARGAH2. PMID:18567826 was read in full via a normally fetched URL cache: both tagged proteins target the mitochondrial matrix in tobacco BY-2 cells, using E1beta colocalization and digitonin versus Triton access controls. Native argah1 retains about85% total seedling arginase activity, so the minor contribution in this context is not absence of function.

PMID:28716421 abstract: ARGAH1+ADC2 and ARGAH2+ADC2 each rescue putrescine-deficient yeast; purified coupled assays are specifically AtARGAH2+AtADC1. Retain ARGAH1 agmatinase and putrescine synthesis as supported capacity, without assigning the paralog's Km or claiming native stress-flux dominance. Chloroplast targeting is reported for the Arabidopsis constructs in Nicotiana leaves, but no additional NEW localization assertion is manufactured.

Urea cycle is retained as contextual ornithine/arginine recycling, not mammalian nitrogen detoxification: live GO definition does not require excretion, and18419821 native metabolite changes support recycling. Core is arginine hydrolysis/nitrogen mobilization. Cytosol HDA and cobalt IMAC claims remain unresolved with exact assay limits; see shared source-analysis report.

## Review provenance and verification

2026-10-26: Applied review and annotation-reviewer skills; consulted sibling annotation reviewer for bounded judgments on compartment inference and source-specific corrections. Normal Falcon research and PMID caching ran concurrently after exact-accession seeding. Falcon failed403 authorization and Perplexity-lite fallback failed401 insufficient quota for each target; no provider report was invented. Manual primary research above replaces the unavailable provider output. FEBA is not applicable to these plant targets. Cached publication files were fetched normally and never hand-edited.

All seeded row payloads, including evidence, source, qualifiers, supporting_entities and the OAT NOT flag, are preserved; only review blocks were authored. No NEW annotation rows were added. GO-CAM absence was not used as evidence for a missing annotation or a new process assertion. Source-specific limitations remain explicit rather than deleting experimental claims merely for inaccessible details.
