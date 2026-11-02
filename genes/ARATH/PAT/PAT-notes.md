# PAT evidence audit

Q9SIE1 PAT/AAT/MEE17 At2g22250 is the distinct prokaryotic-type class-Ib plastid enzyme, PTHR46383:SF1. Full text of PMID:20883697 publisher Methods 2.5 and Results 3.1/3.2 directly demonstrate AspAT and prephenate transfer using either glutamate or aspartate; aromatic branch remains a core biochemical role even when module focuses on Asp. Native Arabidopsis PAT was purified from cultured cells; recombinant target was also assayed. Primary study PMID:16623902 recombinant specificity experiment uses pine PpAAT, so is not relabeled as Arabidopsis kinetics. Full text of PMID:25070637 contains direct Arabidopsis WT/mutant assays. Correction PMID:28011691 corrects K169S to K169V and replaces a mistakenly assayed single-mutant clone; WT activities reproduce. Do not quote uncorrected mutant values. Comparative PMID:24296073 native silencing is Nicotiana benthamiana, not Arabidopsis; developmental necessity PMID:15634699 is contextual and does not establish a separate catalytic embryo-development mechanism.

All original annotation payloads retained; only review objects were curated. Falcon and perplexity-lite fallback were attempted concurrently with publication caching and failed (403/401 provider errors); no provider report was fabricated. FEBA is not applicable to this plant panel.

All annotations were assessed as biological claims. Specific true functions were retained across evidence codes; broad terms were refined; unresolved compartment/affinity-screen claims were not converted into negative evidence. No NEW annotations were added solely to fill module coverage.

Supplementary-table provenance and exact target rows are in `../ASP2/ASP2-source-analysis/` (or the local ASP2-source-analysis directory for ASP2). PMID:28887381 is a mixed-fraction protein-correlation study, not automatic evidence of every annotated compartment. PMID:21533090 S3 peptide detection and S4 targeting classification were inspected; S5 merely lists prior GO assertions and was not used as independent evidence.


### Final negative-localization audit

The seeded annotation explicitly excludes cytosolic localization. Plastid/chloroplast targeting of PAT supports its principal organellar location, but does not alone establish absence of a minor or conditional cytosolic pool. The precise target-specific exclusion behind the PMID:21166475 proteomic classification could not be resolved from accessible material. The unrelated ASP5 negative-prephenate rationale was removed from this localization row and its source assessment. Original annotation fields, including negation, are preserved.


## PR #5568 follow-up, 2026-10-26

Repaired authored citation spacing and fused numeric prose while preserving original annotation payloads, every action, raw UniProt/GOA records and all existing supporting quotations. Source-cited passages in notes were protected from rewriting. Added a target-specific question and flux experiment for the tyrosine branch. PMID:20883697 identifies At2g22250-mediated prephenate-to-arogenate chemistry and discusses arogenate routes to phenylalanine and tyrosine. No NEW process assertion or quantitative native Tyr flux is inferred from this shared precursor alone.
