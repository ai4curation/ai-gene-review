# FAN1 acquisition journal

## 2026-10-25 — private intake checkpoint

These are agent-authored acquisition notes. They document actual sources and workflow outcomes, not a provider research report or scientific annotation assessment. The future authored guide is [FAN1-source-guide.md](FAN1-source-guide.md); this private intake carries its proposed initial content as `SOURCE-GUIDE.md`.

ROOT accepted the read-only ownership preflight at fixed main `188ffae230806a6c652be526ec3b9643d2b8cbad`, with runtime commit `5e62db5cf9887be68578d786c36f0e647a90cf7b`. A genuine isolated `just fetch-gene human FAN1 --uniprot-id Q9Y2M0` succeeded. It produced 51 PENDING contexts and the two literal UniProt products, Q9Y2M0-1 and Q9Y2M0-2. Publication acquisition succeeded. No existing normal source or runtime preimage was changed or restored.

One normal Falcon request and its configured perplexity-lite fallback failed: Falcon returned an authentication/HTTP 403 error and the fallback returned HTTP 401 with quota failure. No provider research file was produced, and no text was fabricated under a provider filename. Private raw logs remain mode 0600. Publication caching ran concurrently with the provider attempt.

The initial preflight QuickGO request omitted `includeFields`; its term, taxon and protein name fields are null. The legacy private filename `QuickGO-enriched.json` was retained unchanged and does not describe that request accurately. A later, separately receipted request using the actual frozen fetcher's `includeFields` parameters returns the same ordered 51 assertions, with only those three names populated. Its deterministic projection exactly equals the genuine TSV. Both responses and the failed initial comparison are preserved; this is not an invented capture of the fetcher's in-process response.

Actual PANTHER v19 tree/MSA/geneinfo responses place target PTN002496574 in PTHR15749, with exact 1,017-residue displayed-sequence agreement. All five GOA IBA assertions match actual IBD rows at ancestor PTN000405526; no NOT row is found on the saved target path. This is a source-placement check, not adjudication of the five biological assertions. Self-WITH is preserved as legitimate target grounding, not called circular support.

The schema check exited 0, reporting `No issues found`. All 51 reviews remain PENDING and status remains INITIALIZED. There are no core functions, new annotations or quotations. Source-provenance partition: 34 PMID contexts in seven whole-reference groups; 17 database contexts in seven groups. Subsequent science must retain the exact source and product objects and assess original assay/species/construct scope independently.

The 22 normal-source records comprise 17 publications, two Reactome records and three PANTHER machine records. Thirteen are exact fixed-main preimages and nine are genuine additions. The provisional seed dependency selection is 12 normal records plus two machine files; ten uncited acquired publication records remain private until scientifically justified. Final public delivery must recheck source collisions against then-current main. No canonical, Git, history or remote mutation was performed.


The following lane entries are historical checkpoints; their PENDING counts describe those separate snapshots. The final integration checkpoint below records the current state.


## Direct literature review — 2026-10-25

Draft 34 contexts: 11 ACCEPT, 10 MODIFY, 9 KEEP_AS_NON_CORE, 4 UNDECIDED. Source-specific HR/NER claims in the inaccessible Kratz full paper and the two adaptor-reader definitions remain unresolved. See [FAN1-source-guide.md](FAN1-source-guide.md) for actual source scope.

Human nuclease direction is demonstrated in [PMID:20603015](https://pubmed.ncbi.nlm.nih.gov/20603015/) and [PMID:20603073](https://pubmed.ncbi.nlm.nih.gov/20603073/). Defined synthetic ICL processing and predominantly three-nucleotide excision in [PMID:25430771](https://pubmed.ncbi.nlm.nih.gov/25430771/) limit both process and molecular-function specificity. No new quotation was added.


## 2026-10-25 — database-provenance review checkpoint

The 17 assigned contexts were manually reviewed: nine ACCEPT and eight MODIFY. All 34 direct-literature contexts remain PENDING in this lane. The source terms, evidence codes, original references, qualifiers, supporting entities and two natural-product objects remain exact. There are no NEW annotations, core functions, publication quotations or status/description changes at this checkpoint. The combined gene review and final status will be established separately.

The actual PANTHER v19 target path, sequence and all five IBD assertions are positive. Human self-WITH is valid evidence, and no propagation failure is manufactured for a sound ancestral function. Current target experiments support narrower binding, nuclease and crosslink-repair recommendations. The phosphodiesterase-I reaction definition has the wrong terminus for the measured human activity; the 5′-to-3′ exonuclease term is retained at a breadth that allows the experimentally resolved three-nucleotide products. The DNA-specific mononucleotide child is not used.

Both selected HPA images were inspected, with antigen and natural-product limits retained. The exact Reactome target has its own nucleoplasm compartment and participates as a recruited nuclease; it is distinct from the damaged DNA substrate. The graph's source-modeled dimer is not generalized to every preparation. The database lane independently read four complete-access original main articles only at the stated Methods/Results/caption passages, with no original figure-pixel or supplement claim. Its separate HPA pixel reading is recorded precisely.

Eleven whole-reference assessment proposals accompany the candidate, retaining every original identity, title and finding. They preserve cache availability separately from external original access and actual reading. PMID:25430771 lacks an availability key in its legacy normal cache, and no key or inferred flag was fabricated. No new normal publication fetch was required; all 22 normal records and 228 owner preimages remained unchanged.

The first typed-ancestry check incorrectly expected site of DNA damage to lie below nucleus. The actual response disproved that expectation; the failed check is retained privately, and the final reason calls this a contextual location refinement. This is a correction to the evidence-check expectation, not a source edit or a changed biological judgment. Five initial GO-reference URL attempts returned 404 and were replaced by actual successful official reference pages; a Reactome batch omission was recovered through bounded single-object reads. Failures are retained and are not evidence.

The complete public reading guide is [FAN1-source-guide.md](FAN1-source-guide.md). The private evidence packet carries exact block indices, source hashes, response receipts, route proofs, manual deltas and focused validation outputs. ROOT owns later integration and canonical publication.


## 2026-10-25 — integrated annotation and core synthesis checkpoint

All 51 imported contexts are now reviewed: 20 ACCEPT, 18 MODIFY, nine KEEP_AS_NON_CORE and four UNDECIDED. Every accepted lane review object remains exact. Four shared references retain complete, separately labeled direct and database reading notes; all 14 reference identities, original findings and both natural products remain unchanged. The legacy PMID:25430771 availability field remains absent. No NEW annotation or publication quotation was introduced.

The synthesis uses two coordinated catalytic units because the schema has one molecular-function slot per unit. They describe the measured 5′-to-3′ processing and internal 5′-flap incision of the same enzyme, both contributing directly to interstrand-crosslink repair. The terms are non-ancestral, and the common process is not counted as two pathways. Flap-DNA recognition is explicitly retained as substrate positioning within these catalytic descriptions, rather than a separate autonomous binding core. The broad DNA exonuclease term is deliberately retained because the narrower DNA-specific child's current definition requires mononucleotide release. The flap-term wording does not establish physiological Okazaki-fragment maturation or exclude the other observed activity.

The core location is the experimentally observed damage site. The broader nucleoplasmic pools supported by HPA and Reactome remain positive annotations and are described separately; their presence does not mean all detectable nucleoplasmic protein is actively catalyzing repair. No obligatory complex term, reader-adaptor function, constitutive replication-fork role, general mismatch-repair role or core HR mechanism is synthesized. The four unresolved direct contexts remain exact, including the inaccessible reference-specific HR/NER assertions and the reader definition's unestablished third-protein bridge.

The standalone description and three question/experiment pairs focus on repair-substrate selection, recruitment versus adaptor organization, and the two natural products. The 533-residue product is neither equated with the assayed enzyme nor declared devoid of all possible function. Current status remains INITIALIZED pending ROOT's later canonical validation. The complete combined evidence and public source locators are in [FAN1-source-guide.md](FAN1-source-guide.md).

Authorship is explicit: eng_resume authored the database lane and synthesis, ROOT authored the direct lane, and eng_resume performed the separately pinned bounded direct-lane reading. This is combined evidence synthesis, not an independent whole-gene re-curation. Original images read by ROOT, HPA images read in the database lane and additional text read during the bounded peer remain separate scopes. No canonical, Git, history, source-cache or remote mutation occurred.
