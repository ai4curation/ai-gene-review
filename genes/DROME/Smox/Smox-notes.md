# Smox literature and annotation notes

## Identity, relay and direct DNA evidence

O96660 is Smox/dSmad2 (CG2262), the activin-branch R-Smad. PANTHER PTHR13703:SF25 official label is MOTHERS AGAINST DECAPENTAPLEGIC HOMOLOG; this generic family label does not make Smox the BMP R-Smad Mad.

[PMID:10320478](https://pubmed.ncbi.nlm.nih.gov/10320478/) establishes receptor-dependent Smox phosphorylation, nuclear translocation and association with Medea. [PMID:9887103](https://pubmed.ncbi.nlm.nih.gov/9887103/) identifies Babo-mediated terminal SSXS phosphorylation. These are biochemical signaling roles, not solely perturbation-based pathway membership. Smox participates in the signaling step after phosphorylation and is not an inert substrate.

Full [PMID:24244197](https://pmc.ncbi.nlm.nih.gov/articles/PMC3820802/) reports endogenous Smox ChIP at Atg8a and an EMSA using recombinant MH1 domain: “EMSA analysis reveals that recombinant Smox protein (MH1-DNA binding domain) binds to Smad binding element (AGAC AGAC) located in Atg8a promoter.” This establishes direct fly DNA-binding competence without importing assumptions about vertebrate SMAD2/SMAD3 isoforms. The promoter is transcriptionally repressed in the muscle autophagy context; Smox activates other targets in other settings.

Full [PMID:28315837](https://pubmed.ncbi.nlm.nih.gov/28315837/) used overexpressed HA-Smad2 phosphomimetic protein for localization and ChIP-on-chip. It reports many peaks, no enriched motif and possible weak overexpression-induced interactions. Those data support chromatin association, but they do not by themselves prove intrinsic DNA binding or every physiological target. Nuclear and cytosolic pools are both retained.

## Context and unresolved binding

Smox regulates developmental growth, neural remodeling, R8 fate, postsynaptic physiology, metabolic responses and context-dependent adult proteostasis. These outputs are retained as non-core where precise. Its restraint on Babo-to-Mad signaling is cross-talk and is not an assignment of Smox as the normal BMP effector. Generic TGIF/Hox protein-binding annotations are removed as uninformative without denying the interactions.

I-SMAD binding remains UNDECIDED. Inspected evidence establishes co-SMAD Medea binding; Dad effects on BMP receptors and complexes do not establish or disprove a direct Smox–Dad interaction. No phylogenetic-loss or donor-count argument is made.

## Method and source limits

2026-10-25, Codex. Applied the review and annotation-reviewer workflow to standard `just fetch-gene` seeds. All original GOA rows are retained and independently assigned decisions; matching term claims are treated consistently across evidence codes. Molecular activities are distinguished from tissue-specific developmental outputs. Broad terms are refined where a concrete supported function is available, and generic protein binding is removed or replaced without denying the physical interaction.

Falcon authentication and Perplexity fallback quota failures had already been established in this session. Research therefore used primary publications, curated UniProt statements, and manual notes; no provider-named research file was fabricated. Missing primary caches were fetched sequentially. One 429 failure for PMID:9224720 was retried successfully. Some other full-text retrievals were rate-limited; abstract-only status remains accurately recorded. A title naming another pathway component is never used to reject an experimental annotation. Where the full assay cannot be established and no independent target support settles the precise claim, UNDECIDED is retained.

UniProt quotes are from curated experimental/function/location statements or legitimate sequence features, never GO annotation lines, protein names, ARBA-only text, or protein-existence labels. Record-section metadata was derived with `just backfill-record-sections`. No NEW biological-process annotations were manufactured to complete a pathway. Core activities are backed by direct or independently curated evidence.

## Completion

71 original annotations reviewed: MODIFY 12, ACCEPT 36, KEEP_AS_NON_CORE 20, REMOVE 2, UNDECIDED 1. Core functions and source reviews completed; gene validation passed without warnings. No branch change or commit was made.
