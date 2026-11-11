# Medea literature and annotation notes

## Identity and shared co-Smad mechanism

O62609 is Med/Medea/dSMAD4 (CG1775), not the unrelated gene anachronism. PANTHER PTHR13703:SF45 official label: MOTHERS AGAINST DECAPENTAPLEGIC HOMOLOG. The gene review is not restricted to activin: both Mad/BMP and Smox/activin complexes are central functions.

[PMID:9502724](https://pubmed.ncbi.nlm.nih.gov/9502724/) establishes Mad/Medea complex formation and partner-dependent nuclear translocation from a cytoplasmic pool. [PMID:10320478](https://pubmed.ncbi.nlm.nih.gov/10320478/) and [PMID:9887103](https://pubmed.ncbi.nlm.nih.gov/9887103/) establish receptor-dependent Smox/Medea complexes. Medea is a co-Smad, not a receptor kinase or an activin-exclusive R-Smad.

Primary [PMID:9694800](https://pubmed.ncbi.nlm.nih.gov/9694800/) identifies Medea as a tinman-enhancer binding factor. [PMID:20010841](https://pubmed.ncbi.nlm.nih.gov/20010841/) reports activating Mad/Medea input through competitive DNA binding at the dad activating element. [PMID:12705870](https://pubmed.ncbi.nlm.nih.gov/12705870/) establishes the Mad/Medea/Schnurri repressor assembly at brinker. These support both DNA-binding activation and repression without contradiction: promoter and partner context differ. The newer NMJ motif study PMID:36029115 shows that elements called silencers in other contexts can mediate activation in motor neurons. Full PMID:18794353 establishes SUMO-associated nuclear export.

## Developmental outputs and uncertainty

Embryonic dorsal–ventral patterning, imaginal tissues, cardiac mesoderm, glial support of retinal targeting, ovarian somatic stem cells and synaptic maturation are contextual outcomes. Medea’s MH1 DNA-binding contribution is distinct from an assertion that a complex works without R-Smads or additional cofactors. Highwire binding is real (PMID:15046722) but bare protein binding is removed as uninformative.

Five rows remain UNDECIDED: the leg-morphogenesis assay in abstract-only PMID:11290719; two precise female germline stem-cell maintenance/division claims from PMID:9695953; the salivary-gland boundary sign in PMID:11598957; and direct I-SMAD binding. Earlier dispensability of Medea during oogenesis (9502724) is not equated to absence of a role in every stem-cell stage, and no misattribution is alleged. Dad inhibition of pathway complexes does not alone establish direct Medea–Dad binding.

## Method and source limits

2026-10-25, Codex. Applied the review and annotation-reviewer workflow to standard `just fetch-gene` seeds. All original GOA rows are retained and independently assigned decisions; matching term claims are treated consistently across evidence codes. Molecular activities are distinguished from tissue-specific developmental outputs. Broad terms are refined where a concrete supported function is available, and generic protein binding is removed or replaced without denying the physical interaction.

Falcon authentication and Perplexity fallback quota failures had already been established in this session. Research therefore used primary publications, curated UniProt statements, and manual notes; no provider-named research file was fabricated. Missing primary caches were fetched sequentially. One 429 failure for PMID:9224720 was retried successfully. Some other full-text retrievals were rate-limited; abstract-only status remains accurately recorded. A title naming another pathway component is never used to reject an experimental annotation. Where the full assay cannot be established and no independent target support settles the precise claim, UNDECIDED is retained.

UniProt quotes are from curated experimental/function/location statements or legitimate sequence features, never GO annotation lines, protein names, ARBA-only text, or protein-existence labels. Record-section metadata was derived with `just backfill-record-sections`. No NEW biological-process annotations were manufactured to complete a pathway. Core activities are backed by direct or independently curated evidence.

## Completion

87 original annotations reviewed: ACCEPT 53, KEEP_AS_NON_CORE 13, REMOVE 1, MODIFY 15, UNDECIDED 5. Core functions and source reviews completed; gene validation passed without warnings. No branch change or commit was made.
