# alg44 primary-source review notes

## Review session 2026-10-25

Applied review and annotation-reviewer instructions. Verified current UniProt accession, PAO1 organism (NCBITaxon:208964) and gene symbol before normal `just fetch-gene`. Preserved every source annotation field, including evidence, qualifier, supporting entities and reference; only review decisions were added. No GO-CAM index entry was found for this accession. All PMID quotes refer to the normal publication cache; no cached source, GOA or UniProt file was hand-edited. Abstract-only sources were not treated as complete papers. No unsupported NEW process rows were added.

The actual default-provider attempts `just deep-research-falcon PSEAE alg44 --fallback perplexity-lite` failed: Edison/Falcon HTTP403 and fallback HTTP401 insufficient quota. These notes record manual primary-source research and are not a provider report. `just fetch-fitness PSEAE alg44` could not retrieve a local/remote FEBA result and did not establish an organism mapping/result; no fitness phenotype is claimed. Source and provider attempts were performed alongside publication caching. UniProt family/domain memberships are classification evidence, not DE/GO/ARBA predictions used as proof of chemistry.

Alg44 is a c-di-GMP receptor and co-polymerase, with cytoplasmic PilZ and periplasmic MFP-like regions. PMID25817996 directly measures ligand binding and provides the PilZ–c-di-GMP structure. PMID18524915 establishes topology and requires both Alg8 and Alg44 in vivo; it identifies Alg8 as the major GT. Therefore seeded enables alginate synthase is over-annotated; core_functions uses contributes_to_molecular_function without changing the seeded qualifier.

PMID16797016 full original article was inspected in Uwe Remminghorst's 2007 thesis, Chapter III (PDF pages 71–82, printed pages 58–69), https://mro.massey.ac.nz/bitstreams/55746141-71a5-48b8-b1b2-8abf9db2eb49/download . Preface identifies this chapter as the published FEBS paper. The methods/results examine deletion/complementation, uronic-acid production, cell morphology, PhoA/LacZ topology fusions, and tagged protein identity. Purification for identification uses denaturing 6 M guanidinium conditions. There is no ATP/CoA/fatty-acid ligase assay; removal of the IDA ligase assertion rests on this full-text inspection and demonstrated alternative molecular role, not missing abstract discussion. The dependent fatty-acid metabolic mapping is removed consistently. The cached PMID remains abstract-only and was not hand-edited. The paper discusses biofilm context but does not directly assay biofilm architecture; the true peripheral biofilm role is retained without claiming such an assay. Its early wholly periplasmic interpretation is qualified by the later topology study.

QuickGO GO:0009276 defines the peptidoglycan cell-wall layer, not the entire cell envelope. Replace it laterally with plasma membrane plus periplasmic space. Three bile-acid/efflux IBAs at PTN000769583 conflict with the specialized alginate system, not because of their donor count. Actual UniProt membership PTHR30386:SF19 is officially MULTIDRUG EXPORT PROTEIN EMRA-RELATED; shared grouping is not proof of retained efflux function. Alg44-specific domains IPR058834, IPR058835, IPR058833 and PilZ IPR009875 provide more informative architecture.

## Sources checked

- [PMID:16797016] Alg44, a unique protein required for alginate biosynthesis in Pseudomonas aeruginosa.: Original article read in full as Chapter III of the author thesis (URL/pages in notes). No fatty-acid–CoA ligase assay appears in its methods/results. Older localization interpretation is qualified by PMID18524915.
- [PMID:18524915] Membrane topology and roles of Pseudomonas aeruginosa Alg8 and Alg44 in alginate polymerization.: Direct P. aeruginosa mutagenesis/topology; not a purified Alg44 glycosyltransferase assay.
- [PMID:25817996] Dimeric c-di-GMP is required for post-translational regulation of alginate production in Pseudomonas aeruginosa.: Direct P. aeruginosa Alg44 regulatory-ligand evidence; c-di-GMP binding is distinct from polymer glycosyltransferase chemistry.


## PR #5552 follow-up, 2026-10-26

Recorded the confirmed PseudoCAP GO:0004467 source defect with DELETE_ROW rather than guessing a replacement activity or gene. The original article was re-inspected in the locally cached author thesis; its assays do not support fatty-acid activation. The cause is UNKNOWN; another suspicious PseudoCAP row is not proof of a common systematic error. Kept plasma membrane as the c-di-GMP core activity location because the PilZ domain faces the cytoplasm; periplasmic exposure remains correctly represented by the source annotation rows and assembly-role description.

The schema has no PseudoCAP resource enum; source_defects uses OTHER with PseudoCAP explicitly named in the explanation. The export therefore appears in reports/source-defects/OTHER.md, rather than a dedicated PseudoCAP report.
