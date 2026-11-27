# Baboon literature and annotation notes

## Identity and isoform scope

A1Z7L8 is babo/Atr-I (CG8224). The displayed UniProt sequence is Babo-B (A1Z7L8-1); the gene-level review encompasses isoforms A, B and C and does not assign every tissue phenotype to the displayed isoform. PANTHER PTHR23255:SF71 official label: RECEPTOR PROTEIN SERINE_THREONINE KINASE. A UniProt free-text sentence calls Punt a type I receptor; the primary evidence identifies Punt as type II, and that sentence is not used for receptor classification.

[PMID:8289834](https://pubmed.ncbi.nlm.nih.gov/8289834/) shows activin binding by Atr-I when coexpressed with Atr-II and heteromeric receptor assembly. This historical assay is not evidence that the native Actbeta ligand was used. [PMID:9887103](https://pubmed.ncbi.nlm.nih.gov/9887103/) establishes Babo association with dSmad2, phosphorylation of its terminal SSXS motif and Medea complex formation. [PMID:10320478](https://pubmed.ncbi.nlm.nih.gov/10320478/) supports receptor-dependent phosphorylation and nuclear translocation. [PMID:18820452](https://pubmed.ncbi.nlm.nih.gov/18820452/) supplies native dACT/Daw evidence.

The full [PMID:19766717](https://pmc.ncbi.nlm.nih.gov/articles/PMC2798586/) establishes Daw preference for Babo-C and a requirement for Punt rather than Wit in the tested cells. It does not establish exclusive Actbeta→Babo-B specificity. The gene review therefore avoids that inference. Babo can phosphorylate Mad conditionally, especially when Smox constraint is altered; this is cross-talk, not grounds to discard its canonical activin role.

## Contextual roles and interpretation

Neuroblast proliferation, eye-antennal disc growth, mushroom-body remodeling, axon/dendrite development and wing morphogenesis are distinct developmental outputs. The Ptc/Smoothened paper PMID:11934850 explicitly includes Babo rescue and is not misattributed because of its title. Adult lifespan effects depend on tissue, ligand and timing. PMID:24244197 supports repression of muscle autophagy, while PMID:29615416 documents different adult proteostasis/lifespan conditions; the broad lifespan annotation is not assigned a universal sign.

PMID:25255438 distinguishes Babo/Smox-dependent postsynaptic physiology from presynaptic NMJ growth. The original Babo–Smox protein-binding row is refined to type I receptor activity because its own primary study demonstrates phosphorylation, not merely association.

## Method and source limits

2026-10-25, Codex. Applied the review and annotation-reviewer workflow to standard `just fetch-gene` seeds. All original GOA rows are retained and independently assigned decisions; matching term claims are treated consistently across evidence codes. Molecular activities are distinguished from tissue-specific developmental outputs. Broad terms are refined where a concrete supported function is available, and generic protein binding is removed or replaced without denying the physical interaction.

Falcon authentication and Perplexity fallback quota failures had already been established in this session. Research therefore used primary publications, curated UniProt statements, and manual notes; no provider-named research file was fabricated. Missing primary caches were fetched sequentially. One 429 failure for PMID:9224720 was retried successfully. Some other full-text retrievals were rate-limited; abstract-only status remains accurately recorded. A title naming another pathway component is never used to reject an experimental annotation. Where the full assay cannot be established and no independent target support settles the precise claim, UNDECIDED is retained.

UniProt quotes are from curated experimental/function/location statements or legitimate sequence features, never GO annotation lines, protein names, ARBA-only text, or protein-existence labels. Record-section metadata was derived with `just backfill-record-sections`. No NEW biological-process annotations were manufactured to complete a pathway. Core activities are backed by direct or independently curated evidence.

## Completion

45 original annotations reviewed: KEEP_AS_NON_CORE 13, MODIFY 10, ACCEPT 22. Core functions and source reviews completed; gene validation passed without warnings. No branch change or commit was made.
