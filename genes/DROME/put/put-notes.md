# Punt literature and annotation notes

## Identity and two core branches

Q24468 is put/punt/Atr-II (CG7904), a type II receptor shared by activin and BMP signaling. PANTHER PTHR23255:SF98 official label: SERINE_THREONINE-PROTEIN KINASE RECEPTOR. Its historical activin-receptor name does not make it branch-exclusive.

[PMID:8415726](https://pubmed.ncbi.nlm.nih.gov/8415726/) establishes high-affinity activin binding by Atr-II; [PMID:8289834](https://pubmed.ncbi.nlm.nih.gov/8289834/) establishes a heteromeric Atr-I/Atr-II complex. The native dACT/Daw–Babo/Punt–Smox relay is independently supported by [PMID:18820452](https://pubmed.ncbi.nlm.nih.gov/18820452/). Full [PMID:19766717](https://pmc.ncbi.nlm.nih.gov/articles/PMC2798586/) shows Daw signaling through Babo-C with Punt, not Wit, in the tested cells.

[PMID:7697720](https://pubmed.ncbi.nlm.nih.gov/7697720/) explicitly distinguishes Punt alone, which did not bind BMP2, from Punt with Tkv or Sax, which formed BMP-binding complexes. Thus BMP binding is complex-dependent. Both type II activin-receptor activity and BMP-receptor activity are core. Punt activates the receptor cascade; the type I receptor is the physiological R-Smad kinase in the canonical relay.

## Localization and downstream outcomes

Full [PMID:35594316](https://pubmed.ncbi.nlm.nih.gov/35594316/) shows tissue-dependent native targeting: basolateral in wing-disc/salivary epithelia and apical plus basolateral in ovarian follicle cells. The apical claim is not simply assigned from a targeting mutant. Both locations refine broad plasma-membrane/membrane rows.

Embryonic patterning, dorsal closure, head involution, tracheal and wing development, neuronal guidance, retinal fate, endocrine responses and NMJ growth are reviewed as specific outputs of the receptor rather than extra catalytic activities. The muscle Punt role in PMID:22959350 should not be conflated with all presynaptic Wit-dependent BMP signaling. PMID:9224720 was finally retrieved and its Dpp/JNK dorsal-closure abstract inspected; independent curated Punt phenotypes support the same claim.

Four precise claims remain UNDECIDED: Malpighian-tubule morphogenesis (10502111), germline stem-cell maintenance and division (9695953), and negative regulation of salivary-gland boundary specification (11598957). The available abstracts do not settle the exact target/assay or sign. This is not a declaration of curator misattribution or evidence of loss.

## Method and source limits

2026-10-25, Codex. Applied the review and annotation-reviewer workflow to standard `just fetch-gene` seeds. All original GOA rows are retained and independently assigned decisions; matching term claims are treated consistently across evidence codes. Molecular activities are distinguished from tissue-specific developmental outputs. Broad terms are refined where a concrete supported function is available, and generic protein binding is removed or replaced without denying the physical interaction.

Falcon authentication and Perplexity fallback quota failures had already been established in this session. Research therefore used primary publications, curated UniProt statements, and manual notes; no provider-named research file was fabricated. Missing primary caches were fetched sequentially. One 429 failure for PMID:9224720 was retried successfully. Some other full-text retrievals were rate-limited; abstract-only status remains accurately recorded. A title naming another pathway component is never used to reject an experimental annotation. Where the full assay cannot be established and no independent target support settles the precise claim, UNDECIDED is retained.

UniProt quotes are from curated experimental/function/location statements or legitimate sequence features, never GO annotation lines, protein names, ARBA-only text, or protein-existence labels. Record-section metadata was derived with `just backfill-record-sections`. No NEW biological-process annotations were manufactured to complete a pathway. Core activities are backed by direct or independently curated evidence.

## Completion

83 original annotations reviewed: MODIFY 10, ACCEPT 50, KEEP_AS_NON_CORE 19, UNDECIDED 4. Core functions and source reviews completed; gene validation passed without warnings. No branch change or commit was made.
