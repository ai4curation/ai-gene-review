# CORGL lysC research notes

## 2026-11-01 — native aspartokinase and alternative initiation

P26512 is the reviewed ATCC13032 product (taxon196627). The record already supplies Alpha P26512-1 and Beta P26512-2 under alternative products. PMID:1956296 explicitly clones/sequences the ATCC13032 lysC/asd cluster and reports a purified aspartokinase containing 47kDa and18kDa proteins. This native evidence supports the two products; their modern representation is alternative initiation at one locus, not a second independent pathway gene.

PMID:20573952 full text resolves alpha2beta2 architecture, with catalytic alpha N-terminal domains and regulatory beta chains/alpha C-terminal domains. Exact support: “The N-terminal portion of the α subunit functions as a catalytic domain, whereas the β subunit and C-terminal portion of the α subunit serve as regulatory domains.” The structural experiments used recombinant E.coli coexpression, intentionally disabled the native internal ribosome-binding site and supplied beta separately. That engineered expression layout must not become a claim that native alpha and beta are independent loci. PMID:17350037 abstract corroborates the regulatory ACT-domain dimer and threonine-dependent assembly but is not needed as an additional independent assay of whole-enzyme native flux.

LysC phosphorylates aspartate with ATP. Wild type is concertedly inhibited by lysine and threonine; a feedback-resistant S301F construct is a separate experimental condition. The module should require the complete alpha2beta2 native activity at one locus and represent beta as a regulatory translation product, not as a separate aspartokinase. Existing aspartate kinase MF is accepted gene-wide, not assigned independently to beta. The generic amino-acid BP is refined to the supported lysine/threonine/methionine branches. Cytosol remains an inference consistent with TreeGrafter and soluble biosynthetic chemistry, not a direct localization experiment.

Family evidence in the immutable record: PTHR21499 ASPARTATE KINASE; SF3 ASPARTOKINASE; TIGR00656 asp_kin_monofn and TIGR00657 asp_kinases. This is not the fused E.coli ThrA/MetL architecture. All six seeded rows adjudicated; no NEW.

## Source acquisition and scope

Normal `just fetch-gene` generated the UniProt record, GOA export and seeded review. The 41 original rows across this five-gene panel and all ten raw files were snapshotted before curation. An initial folder-code misunderstanding was corrected to canonical CORGL; the five new folders were moved without changing raw bytes or machine annotation payloads. The original and migrated baselines and an explicit migration record are retained in `.cache/module-audit-logs/bacterial-threonine-corgl-20261101/`.

A normal Falcon research request failed with HTTP403 authentication failure. This is a provider failure, not a research report; no provider-named report was fabricated. The shared authentication failure was not repeatedly retried for the other four genes. The nonhuman MOD-description command was run for all five under canonical CORGL and reported no configured MOD provider. Research below is manual synthesis of immutable primary caches and the reviewed UniProt record.

No raw annotation was removed or rewritten. Ordinary relationship qualifiers played no part in the judgment. No NEW annotation was proposed: the original set and supported refinements already cover the supported biosynthetic functions. No unverified universal bacterial architecture or native production flux is inferred from recombinant protein or engineered production strains.
