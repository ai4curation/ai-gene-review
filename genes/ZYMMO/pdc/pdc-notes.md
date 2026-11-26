# pdc: bacterial fermentation review

## Scope and research

Reviewed all 6 seeded rows for ZYMMO/pdc (P06672); original terms, evidence, references and supporting entities are preserved. Manual primary-source research and the annotation-reviewer/core-function-synthesizer workflows were used. The default Falcon request and automatic Perplexity-lite fallback both failed (session log `/tmp/alcohol-pdc-deep.log`); no provider-authored report was fabricated. The wrapper did not expose a more specific cause. `fetch-fitness` was attempted but returned no usable FEBA data (`/tmp/alcohol-pdc-fitness.log`); no fitness inference is made. No accession match was found in `gocams/index.tsv`.

## Biological synthesis

Pyruvate decarboxylase catalyzes the thiamine diphosphate- and magnesium-dependent conversion of pyruvate to acetaldehyde and carbon dioxide in Zymomonas mobilis. The acetaldehyde supplies the two alcohol dehydrogenase isozymes for ethanol formation during sugar fermentation. The enzyme forms a homotetramer with cofactor-binding sites at subunit interfaces and, unlike yeast pyruvate decarboxylases, does not require substrate-dependent allosteric activation.

- [PMID:3546263](https://pubmed.ncbi.nlm.nih.gov/3546263/): Purification and genomic-clone expression establish Zymomonas pyruvate decarboxylase activity; the accessible abstract does not independently identify the culture as ZM4.
- [PMID:9685367](https://pubmed.ncbi.nlm.nih.gov/9685367/): Direct Zymomonas enzyme structure supports the homotetramer and TPP-binding site; no native localization experiment is inferred.

## Curation boundaries

No new process annotation was added to fill a pathway diagram. Exact catalytic functions supply the core synthesis. Broad molecular-function rows are refined rather than removed. Duplicate claims receive consistent actions. Abstract-only sources are identified in reference assessments, and assay conditions or strain identities not stated there are not invented.

## Family grounding

Actual target UniProt membership, checked against official PANTHER names: PTHR43452 PYRUVATE DECARBOXYLASE; PTHR43452:SF1 PYRUVATE DECARBOXYLASE C186.09-RELATED. Family labels do not independently establish substrate activity. In particular, surprising subfamily names are retained verbatim rather than relabeled to fit the pathway. No PTN selector is guessed.
