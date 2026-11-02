# ALDH12A1 annotation review notes

Identity: Q8VZC3 / At5g62530. Verified fetched PANTHER PTHR43521:SF7 DELTA-1-PYRROLINE-5-CARBOXYLATE DEHYDROGENASE 12A1, MITOCHONDRIAL; broad parent PTHR43521 ALPHA-AMINOADIPIC SEMIALDEHYDE DEHYDROGENASE requires activity restriction in the module.

PMID:11532180 abstract cached, complete publisher HTML independently read at https://onlinelibrary.wiley.com/doi/full/10.1046/j.1365-313X.2001.01101.x (normal URL-cache attempt failed; no fabricated cache). Direct target evidence: Arabidopsis cDNA rescues yeast put2, first 40aa-GFP targets tobacco and Arabidopsis protoplast mitochondria. The source discusses matrix P5CDH from maize and NAD preference from prior potato biochemistry. Curated Arabidopsis NAD+-dependent reaction plus conserved family supports the existing GO:0003842 claim, but no target-specific NAD/NADP ratio was measured there. Matrix placement is a supported curated/class inference beyond simple fluorescence colocalization.

PMID:15548746 full text: 14C-Pro yields labeled Glu/Gln in wild type but not p5cdh; Pro degradation absent, Pro/Arg/Orn hypersensitivity and excess-P5C effects. Native vegetative normality does not negate catabolism. PMID:19635803 full text shows increased mitochondrial ROS with excess proline and explains flux into the P5C-Pro cycle versus oxidation to Glu. Refine ROS metabolism to GO:2000378 negative regulation of ROS metabolism: ALDH12A1 oxidizes GSA/P5C, not ROS directly. Current GO label checked through QuickGO.

PMID:16377568 full text shows salt-regulated antisense transcript cleavage and p5cdh mutant phenotypes. Retain salt response non-core with conditional sign: mutant was slightly more salt tolerant in that experiment, while earlier15548746 conditions did not show changed stress tolerance. No universal positive salt-protection claim.

PMID:36528796 abstract gives direct allelic-mutant evidence, C/N partitioning, 15N remobilization and abnormal C-depleted seeds; retain seed development non-core as resource-remobilization biology. Do not infer a dedicated patterning function.

PMID:11743115 full text and14671022 abstract provide complementary mitochondrial proteomics. PMID:25293756 full text uses crude cytosol; that does not resolve imported mitochondrial proteins versus a persistent cytosolic pool. PMID:28887381 exact S1 rows list mitochondrion for this target. Cytosol/plastid and target-specific Zn/Co binding remain UNDECIDED; no asserted absence from other compartments or exclusion of incidental binding.

## Review provenance and verification

2026-10-26: Applied review and annotation-reviewer skills; consulted sibling annotation reviewer for bounded judgments on compartment inference and source-specific corrections. Normal Falcon research and PMID caching ran concurrently after exact-accession seeding. Falcon failed403 authorization and Perplexity-lite fallback failed401 insufficient quota for each target; no provider report was invented. Manual primary research above replaces the unavailable provider output. FEBA is not applicable to these plant targets. Cached publication files were fetched normally and never hand-edited.

All seeded row payloads, including evidence, source, qualifiers, supporting_entities and the OAT NOT flag, are preserved; only review blocks were authored. No NEW annotation rows were added. GO-CAM absence was not used as evidence for a missing annotation or a new process assertion. Source-specific limitations remain explicit rather than deleting experimental claims merely for inaccessible details.

Validation note: live QuickGO on2026-10-26 confirms GO:0003842 is named L-glutamate gamma-semialdehyde dehydrogenase (NAD+) activity and defines NAD+-dependent chemistry. The local term-validator snapshot uses the older label lacking (NAD+); retain the current label and original payload, documenting this advisory rather than rewriting the source annotation.

## 2026-10-26 PR #5566 root-organelle follow-up

The N-terminal GFP targeting experiment establishes mitochondrial localization in tobacco and Arabidopsis protoplasts (PMID:11532180), independently supporting the organelle claim. Retain mitochondrial residence alongside the existing matrix assignment. Neither the targeting assay nor each proteomic observation must resolve the subcompartment to support this retained annotation. Existing matrix annotations and core functions are preserved.

The current policy retains informative organelle terms; the earlier blanket MODIFY-to-matrix rationale was incorrect. Original machine annotation payloads are preserved.
