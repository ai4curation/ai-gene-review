# Syk Gene Review Notes

## 2025-01-14 - Missing Annotation Fix

**Issue**: Validation failure due to 25 annotations present in the current GOA file but missing from the YAML file.

**Root Cause**: The GOA file has been updated with new annotations since the original review was completed. These include:
- GO:0032991 (protein-containing complex) with multiple evidence types
- GO:0005829 (cytosol) with multiple Reactome references
- GO:0019815 (B cell receptor complex) with IDA evidence

**Action Taken**:
1. Used the GOA validator's `seed_missing_annotations` function to automatically add the 25 missing annotations
2. Fixed PMID:22451653 title to match the correct publication title
3. Added 15 new references from the GOA file

**Annotations Added**: All missing annotations were seeded as PENDING for future review, including:
- Multiple cytosol localizations from different Reactome pathways
- Protein complex memberships
- B cell receptor complex association

**Validation Status**: After seeding missing annotations and fixing the title, the gene now passes validation with only warnings about PENDING annotations.

**Note**: The newly seeded annotations represent legitimate additions to the GOA database and should be reviewed in future curation cycles.

## Complete BCR-panel reassessment, 2026-10-26

All baseline rows were manually assessed, including roles outside BCR signaling. The original term, reference, evidence, partner, isoform, qualifier and NOT payloads remain unchanged. No new annotation was added; mouse Syk retains its two historically inherited NEW rows. Actual Falcon/fallback and publication-retrieval jobs were run by the shared acquisition workflow. Provider failures were recorded honestly; provider prose is not used as primary evidence. Normal additional publication recovery and direct source inspection resolved the principal catalytic and binding claims. Incomplete source access remains explicit in individual review reasons rather than being converted into wrong-gene or negative-function conclusions.

The principal molecular activity is non-receptor tyrosine phosphorylation with tandem-SH2-mediated phosphotyrosine recognition. A broad kinase assertion is refined to supported chemistry rather than removed. Cytoplasm is retained alongside finer pools, and membrane recruitment does not imply integral membrane topology. Binding to a phosphotyrosine ligand is distinguished from binding to another protein's SH2 domain. Purified recombinant and mixed-species DT40 complementation assays retain their construct species; DT40 host identity does not identify every tested protein.

Native mouse kinase/receptor studies (8798454/8626447/9000133/15845454/17086186) support the core across BCR, Fc, lectin and integrin routes. Native OxLDL-treated macrophages in full 25946330 connect Syk to ROS–JNK–BECN1 signaling and positive autophagic flux. Negative autophagy in the Tau context (31324720) uses human SH-SY5Y mechanisms and mouse tauopathy pharmacology. Both can hold without a sign-consistency exception because they are distinct biological assertions. Stress-granule work in 26429917 uses arsenite/proteasome stress, not nutrient deprivation; old nutrient and negative-TORC donor claims remain unresolved when their exact experimental chain could not be recovered. Current QuickGO donor retrieval is stored only as provenance in Syk-source-analysis and never cited as evidence of function.

The full TULA2 study 27609517 establishes GPVI–FcRgamma signaling, not an intrinsic receptor tyrosine kinase. The existing collagen-activated RTK term is therefore corrected to the broader collagen-activated signaling pathway. Its domain pull-downs support real SH2-domain binding as well as phosphotyrosine recognition, rather than conflating the two directions. Mouse Syk phosphosites retain mouse numbering.

Full 22496641 Figure S5A immunoprecipitates Lyn (preserved partner P25911) and recovers Syk from LPS-treated neutrophils; this refines to protein tyrosine kinase binding. P31809 is CEACAM1, a different coassociated partner in the same paper. Its bare-binding annotation is removed as uninformative without denying the complex. Native knockout and human Ikaros donor evidence do not justify assigning Syk the import-carrier function, so protein nuclear import is refined to positive regulation.

The human IL8-production donor result (25251945) does not establish mouse IL8 production: primary comparative 10028286 explicitly identifies the mouse/rat IL8 gene loss. This is an output-specific transfer-scope problem, not loss of Syk or universal rodent chemokine absence. Platelet activation and Fc-epsilon signaling proposals were already in the baseline and remain supported by actual Syk signaling work (9171347/9000133), not newly manufactured coverage.


Full primary PMID:9314552 directly establishes native mouse macrophage Fc-gamma-receptor signaling and phagocytosis, including substrate phosphorylation and failed internalization despite actin-cup formation. This independently supports the core process despite an annotation-coverage advisory. No NEW row is added solely to make core and annotation inventories identical. Legacy provider reports are not cited as primary evidence merely to silence their separate advisory.


## PR 5584 source and scope follow-up

Live QuickGO ancestry confirms GO:0038096 is a descendant of GO:0007166, already represented twice. Both broad rows are refined to supported receptor branches, preserving Fc-gamma coverage without NEW redundancy. Full PMID9314552 shows native receptor-triggered Syk activation and downstream signaling, but discusses kinase-versus-adaptor explanations of the knockout phagocytic defect. Comparator LYN/HCK/FGR annotations show that receptor-proximal kinases are not conventionally excluded from this process; their annotation state is not supporting evidence. Cached GO-CAM 62b4ffe300006474 models mouse Syk as a kinase in BCR signaling and makes no negative statement about Fc-gamma signaling. Both inherited NEW rows remain unchanged.
