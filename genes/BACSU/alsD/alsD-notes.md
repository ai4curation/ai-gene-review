# alsD: bacterial fermentation review

## Scope and research

Reviewed all 2 seeded rows for BACSU/alsD (Q04777); original terms, evidence, references and supporting entities are preserved. Manual primary-source research and the annotation-reviewer/core-function-synthesizer workflows were used. The default Falcon request and automatic Perplexity-lite fallback both failed (session log `/tmp/alcohol-alsD-deep.log`); no provider-authored report was fabricated. The wrapper did not expose a more specific cause. `fetch-fitness` was attempted but returned no usable FEBA data (`/tmp/alcohol-alsD-fitness.log`); no fitness inference is made. No accession match was found in `gocams/index.tsv`.

## Biological synthesis

AlsD is the zinc-containing acetolactate decarboxylase of Bacillus subtilis. It converts acetolactate to (R)-acetoin and carbon dioxide, connecting AlsS-dependent acetolactate formation to acetoin accumulation and downstream 2,3-butanediol production. The alsSD operon is induced during stationary-phase and anaerobic growth. The enzyme can convert both acetolactate enantiomers to (R)-acetoin; the native pathway supplies (S)-acetolactate.

- [PMID:29796971](https://pubmed.ncbi.nlm.nih.gov/29796971/): B. subtilis acetolactate decarboxylase structure and kinetics support zinc-dependent acetoin production; UniProt Q04777 cross-reference to 5XNE links the target. General introductory stereochemistry is corroborated by the curated target reaction.
- [PMID:7685336](https://pubmed.ncbi.nlm.nih.gov/7685336/): Native cloning/regulation identifies alsD as the acetoin-producing acetolactate decarboxylase in alsSD.
- [PMID:10809684](https://pubmed.ncbi.nlm.nih.gov/10809684/): Native physiological context places AlsD downstream of AlsS in anaerobic butanediol formation.

## Curation boundaries

No new process annotation was added to fill a pathway diagram. Exact catalytic functions supply the core synthesis. Broad molecular-function rows are refined rather than removed. Duplicate claims receive consistent actions. Abstract-only sources are identified in reference assessments, and assay conditions or strain identities not stated there are not invented.

## Family grounding

Actual target UniProt membership, checked against official PANTHER names: PTHR35524 ALPHA-ACETOLACTATE DECARBOXYLASE; PTHR35524:SF1 ALPHA-ACETOLACTATE DECARBOXYLASE. Family labels do not independently establish substrate activity. In particular, surprising subfamily names are retained verbatim rather than relabeled to fit the pathway. No PTN selector is guessed.
