# alsS: bacterial fermentation review

## Scope and research

Reviewed all 9 seeded rows for BACSU/alsS (Q04789); original terms, evidence, references and supporting entities are preserved. Manual primary-source research and the annotation-reviewer/core-function-synthesizer workflows were used. The default Falcon request and automatic Perplexity-lite fallback both failed (session log `/tmp/alcohol-alsS-deep.log`); no provider-authored report was fabricated. The wrapper did not expose a more specific cause. `fetch-fitness` was attempted but returned no usable FEBA data (`/tmp/alcohol-alsS-fitness.log`); no fitness inference is made. No accession match was found in `gocams/index.tsv`.

## Biological synthesis

AlsS is a catabolic acetolactate synthase of Bacillus subtilis that condenses two pyruvate molecules to acetolactate using thiamine diphosphate and magnesium. Together with AlsD it supplies acetoin, which can be reduced by BdhA to 2,3-butanediol during oxygen-limited fermentation. AlsS is FAD-independent and forms an oligomer of a single polypeptide type, distinct from heteromeric anabolic acetohydroxyacid synthases. Its 2-ketoisovalerate decarboxylase side activity can also be used in engineered isobutanol pathways.

- [PMID:25393087](https://pubmed.ncbi.nlm.nih.gov/25393087/): Direct target structure and enzyme characterization support acetolactate synthesis and ThDP/Mg cofactors; the KIV side activity is distinguished from the native acetoin pathway.
- [PMID:32855421](https://pubmed.ncbi.nlm.nih.gov/32855421/): Full text explicitly identifies the B. subtilis starting enzyme as FAD-independent and an oligomer of one polypeptide type; subsequent engineered stability variants are not treated as native protein properties.
- [PMID:10809684](https://pubmed.ncbi.nlm.nih.gov/10809684/): Native B. subtilis fermentation establishes the alsSD contribution to acetoin/butanediol formation, not a universal ethanol route.
- [PMID:19684168](https://pubmed.ncbi.nlm.nih.gov/19684168/): The accessible abstract demonstrates B. subtilis AlsS KIV-decarboxylase activity in vitro and in engineered E. coli; it does not by itself establish native valine or isobutanol biosynthesis.
- [PMID:7685336](https://pubmed.ncbi.nlm.nih.gov/7685336/): Cloning and native regulation of alsS/alsD link the genes to post-exponential acetoin formation.

## Curation boundaries

No new process annotation was added to fill a pathway diagram. Exact catalytic functions supply the core synthesis. Broad molecular-function rows are refined rather than removed. Duplicate claims receive consistent actions. Abstract-only sources are identified in reference assessments, and assay conditions or strain identities not stated there are not invented.

Live QuickGO GO:0005948 describes a large/small-chain heteromer. PMID:32855421 instead states that B. subtilis AlsS is FAD-independent and made of one polypeptide type. PAINT PTHR18968 cached IBD nodes PTN000438682 (synthase/FAD) and PTN000438758 (complex/valine) were inspected: synthase activity remains valid, whereas the cofactor/complex transfer is contradicted by the target. No precise ancestral pruning point is invented. Native valine participation remains UNDECIDED; engineered E. coli precursor supply is not treated as native B. subtilis evidence. The similarity-derived UniProt FAD features conflict with target-specific literature.

## Family grounding

Actual target UniProt membership, checked against official PANTHER names: PTHR18968 THIAMINE PYROPHOSPHATE ENZYMES; PTHR18968:SF129 ACETOLACTATE SYNTHASE. Family labels do not independently establish substrate activity. In particular, surprising subfamily names are retained verbatim rather than relabeled to fit the pathway. No PTN selector is guessed.

The pre-existing PTHR18968 family review scopes FAD binding and heteromeric complex membership away from SF129, consistent with these removals; no family edit is needed. Its valine scope is narrower than the unresolved native-role question retained here.
