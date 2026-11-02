# Actbeta literature and annotation notes

## Identity and core mechanism

O61643 is Actbeta/activin-beta (CG11062), a secreted 946-residue precursor with a mature TGF-beta-family signaling ligand. PANTHER PTHR11848:SF309 has the official label INHIBIN BETA CHAIN; that family label does not establish a vertebrate-like inhibin-alpha/beta antagonist in flies.

[PMID:18820452](https://pubmed.ncbi.nlm.nih.gov/18820452/) directly reports that native dACT and Daw signal through Babo with Punt and activate dSMAD2. This is the principal native-ligand anchor. Historical receptor studies using vertebrate activin establish receptor behavior, not identification of the native fly ligand. A negative Myoglianin result in this assay is not generalized to all isoforms/tissues, given later Babo-isoform results.

The original neural remodeling study [PMID:12581521](https://pubmed.ncbi.nlm.nih.gov/12581521/) includes stage-specific dActivin loss and reduced EcR-B1-associated remodeling. [PMID:18171686](https://pubmed.ncbi.nlm.nih.gov/18171686/) demonstrates redundant Actbeta/Daw control of neuroblast proliferation through Babo/Smox. These do not establish exclusive Actbeta use of Babo-B.

## Contextual roles

[PMID:28178568](https://pmc.ncbi.nlm.nih.gov/articles/PMC5373560/) establishes midgut enteroendocrine Actbeta and enhanced AKH response in fat body under chronic high-sugar diet. Sugar responsiveness, glucose balance and positive glycogen-catabolic regulation are downstream endocrine outputs, not glucose binding or carbohydrate enzyme activity. [PMID:25255438](https://pubmed.ncbi.nlm.nih.gov/25255438/) establishes postsynaptic NMJ effects distinct from presynaptic bouton growth. [PMID:28853393](https://pubmed.ncbi.nlm.nih.gov/28853393/) distinguishes parallel activin/Smox and BMP/Mad inputs in R8 fate. Wing growth findings are retained in their experimental context rather than generalized to every tissue.

The Follistatin interaction in PMID:18077144 is real biological regulation of a ligand, but bare protein binding is uninformative and is removed under the project policy. Actbeta is the ligand, not the protease processing it; no peptide-maturation process is added.

## Method and source limits

2026-10-25, Codex. Applied the review and annotation-reviewer workflow to standard `just fetch-gene` seeds. All original GOA rows are retained and independently assigned decisions; matching term claims are treated consistently across evidence codes. Molecular activities are distinguished from tissue-specific developmental outputs. Broad terms are refined where a concrete supported function is available, and generic protein binding is removed or replaced without denying the physical interaction.

Falcon authentication and Perplexity fallback quota failures had already been established in this session. Research therefore used primary publications, curated UniProt statements, and manual notes; no provider-named research file was fabricated. Missing primary caches were fetched sequentially. One 429 failure for PMID:9224720 was retried successfully. Some other full-text retrievals were rate-limited; abstract-only status remains accurately recorded. A title naming another pathway component is never used to reject an experimental annotation. Where the full assay cannot be established and no independent target support settles the precise claim, UNDECIDED is retained.

UniProt quotes are from curated experimental/function/location statements or legitimate sequence features, never GO annotation lines, protein names, ARBA-only text, or protein-existence labels. Record-section metadata was derived with `just backfill-record-sections`. No NEW biological-process annotations were manufactured to complete a pathway. Core activities are backed by direct or independently curated evidence.

## Completion

24 original annotations reviewed: KEEP_AS_NON_CORE 10, ACCEPT 10, REMOVE 1, MODIFY 3. Core functions and source reviews completed; gene validation passed without warnings. No branch change or commit was made.
