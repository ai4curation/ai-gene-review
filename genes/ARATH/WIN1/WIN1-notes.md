# ARATH WIN1 full annotation audit

All 24 normally seeded annotations reviewed; all original machine fields retained. No NEW rows proposed.

## Biological and evidence distinctions

Current UniProt name WIN1 is retained; TUP5 is the same At1g80600/Q9M8M7 product, explicitly identified in full PMID:23321422. Functional GFP complementation establishes chloroplast targeting, and two stromal proteomic assignments support the finer core location. Mitochondrial assignment remains uncertain: UniProt is by-similarity and the PMID:28887381 original supplement classifies this row as plastid with no dual-localization flag. That result does not exclude a second location. Copper capture cannot be adjudicated from the abstract of PMID:20018591; normal force-fetch plus Europe PMC and web full-text attempts did not retrieve the target-specific table (500/captcha); use UNDECIDED, not REMOVE. PMID:18266921 explicitly separates WIN1 from WIN2/3: WIN1 overexpression suppresses rather than promotes resistance, so do not copy WIN2/3 effects. Root-development refinement preserves the stronger primary-root phenotype without assigning a direct blue-light sensor function.

## Sources and access

- PMID:23321422: The Arabidopsis TUMOR PRONE5 gene encodes an acetylornithine aminotransferase required for arginine biosynthesis and root meristem maintenance in blue light. Full text cached (gene-specific supplementary tables separately assessed where available).
- PMID:18266921: Arabidopsis proteins important for modulating defense responses to Pseudomonas syringae that secrete HopW1-1. Abstract/bibliographic cache only; no inaccessible assay detail asserted.
- PMID:20018591: Divalent metal ions in plant mitochondria and their role in interactions with proteins and oxidative stress-induced damage to respiratory function. Abstract/bibliographic cache only; no inaccessible assay detail asserted.
- PMID:28887381: Global Analysis of Membrane-associated Protein Oligomerization Using Protein Correlation Profiling. Full text cached (gene-specific supplementary tables separately assessed where available).
- PMID:18431481: Sorting signals, N-terminal modifications and abundance of the chloroplast proteome. Full text cached (gene-specific supplementary tables separately assessed where available).
- PMID:25293756: A proteomic strategy for global analysis of plant protein complexes. Full text cached (gene-specific supplementary tables separately assessed where available).
- PMID:16207701: The oligomeric stromal proteome of Arabidopsis thaliana chloroplasts. Abstract/bibliographic cache only; no inaccessible assay detail asserted.
- PMID:20061580: AT_CHLORO, a comprehensive chloroplast proteome database with subplastidial localization and curated information on envelope proteins. Full text cached (gene-specific supplementary tables separately assessed where available).

## Provider attempts and provenance

Normal Falcon with perplexity-lite fallback and publication caching were attempted in parallel. Falcon failed authentication (403), fallback failed quota (401); no fabricated provider report was created. FEBA is not applicable to these plant genes. Logs are in `.cache/module-audit-logs/arginine-ARATH-WIN1-*.log`. GOA was used only by the normal seed/validation pipeline; it was not biological evidence.
