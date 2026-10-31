# ARATH NAGK full annotation audit

All 21 normally seeded annotations reviewed; all original machine fields retained. No NEW rows proposed.

## Biological and evidence distinctions

At3g57560/Q9SCL7 is the true NAG kinase despite a misleading PANTHER subfamily display name; UniProt and direct primary assays establish identity. PMID:16377628 provides biochemistry and stromal localization, PMID:17913711 the PII/NAGK complex, PMID:19631611 metabolite-dependent interaction, and PMID:28294536 E. coli complementation and native developmental genetics. The early work reports arginine-enhanced association whereas later MgATP-conditioned assays report arginine inhibition of complex formation; these are assay-context observations, not grounds to deny feedback relief. Do not generalize one metabolite effect across conditions. Protein-binding rows are removed under the current policy with the interactions preserved. The supposedly ACCase-only PMID:20018655 full text also confirms NAGK capture. Supplemental PMID:28887381 Mapp row897 identifies a True membrane, plastid-classified NAGK pool, not cytosol. Exact gene-level thylakoid data in PMID:20061580 are not exposed by the cache; thylakoid and cytosol assertions remain unresolved without denying possible pools. No new developmental annotations are manufactured solely from necessity phenotypes.

## Sources and access

- PMID:16377628: The PII signal transduction protein of Arabidopsis thaliana forms an arginine-regulated complex with plastid N-acetyl glutamate kinase. Abstract/bibliographic cache only; no inaccessible assay detail asserted.
- PMID:17913711: Structural basis for the regulation of N-acetylglutamate kinase by PII in Arabidopsis thaliana. Abstract/bibliographic cache only; no inaccessible assay detail asserted.
- PMID:19631611: Metabolite regulation of the interaction between Arabidopsis thaliana PII and N-acetyl-l-glutamate kinase. Abstract/bibliographic cache only; no inaccessible assay detail asserted.
- PMID:28294536: Acetylglutamate kinase is required for both gametophyte function and embryo development in Arabidopsis thaliana. Abstract/bibliographic cache only; no inaccessible assay detail asserted.
- PMID:15150219: Interactions between the nitrogen signal transduction protein PII and N-acetyl glutamate kinase in organisms that perform oxygenic photosynthesis. Abstract/bibliographic cache only; no inaccessible assay detail asserted.
- PMID:20018655: Chloroplast acetyl-CoA carboxylase activity is 2-oxoglutarate-regulated by interaction of PII with the biotin carboxyl carrier subunit. Full text cached (gene-specific supplementary tables separately assessed where available).
- PMID:28887381: Global Analysis of Membrane-associated Protein Oligomerization Using Protein Correlation Profiling. Full text cached (gene-specific supplementary tables separately assessed where available).
- PMID:20061580: AT_CHLORO, a comprehensive chloroplast proteome database with subplastidial localization and curated information on envelope proteins. Full text cached (gene-specific supplementary tables separately assessed where available).
- PMID:18431481: Sorting signals, N-terminal modifications and abundance of the chloroplast proteome. Full text cached (gene-specific supplementary tables separately assessed where available).

## Provider attempts and provenance

Normal Falcon with perplexity-lite fallback and publication caching were attempted in parallel. Falcon failed authentication (403), fallback failed quota (401); no fabricated provider report was created. FEBA is not applicable to these plant genes. Logs are in `.cache/module-audit-logs/arginine-ARATH-NAGK-*.log`. GOA was used only by the normal seed/validation pipeline; it was not biological evidence.
