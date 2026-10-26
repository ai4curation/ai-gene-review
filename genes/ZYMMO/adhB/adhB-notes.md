# adhB: bacterial fermentation review

## Scope and research

Reviewed all 6 seeded rows for ZYMMO/adhB (P0DJA2); original terms, evidence, references and supporting entities are preserved. Manual primary-source research and the annotation-reviewer/core-function-synthesizer workflows were used. The default Falcon request and automatic Perplexity-lite fallback both failed (session log `/tmp/alcohol-adhB-deep.log`); no provider-authored report was fabricated. The wrapper did not expose a more specific cause. `fetch-fitness` was attempted but returned no usable FEBA data (`/tmp/alcohol-adhB-fitness.log`); no fitness inference is made. No accession match was found in `gocams/index.tsv`.

## Biological synthesis

AdhB is the iron-dependent alcohol dehydrogenase II of Zymomonas mobilis. It catalyzes reversible NAD-linked ethanol/acetaldehyde interconversion and supports ethanol production through acetaldehyde reduction. The catalytic iron lies near the nicotinamide cofactor. This enzyme is distinct from the zinc-dependent AdhA isozyme; zinc inhibits AdhB, while iron or cobalt can support its activity during purification.

- [PMID:2935393](https://pubmed.ncbi.nlm.nih.gov/2935393/): Purified Zymomonas isozyme biochemistry establishes different metals and reaction-direction activities. The abstract does not specify ZM4, so quantitative isozyme fractions are not asserted as fixed ZM4 values.
- [PMID:21295587](https://pubmed.ncbi.nlm.nih.gov/21295587/): Direct ZM4 AdhB structures establish bound NAD and catalytic iron; the introduction also distinguishes zinc-dependent AdhA. AdhB structural details are not transferred to AdhA.

## Curation boundaries

No new process annotation was added to fill a pathway diagram. Exact catalytic functions supply the core synthesis. Broad molecular-function rows are refined rather than removed. Duplicate claims receive consistent actions. Abstract-only sources are identified in reference assessments, and assay conditions or strain identities not stated there are not invented.

PMID:2935393 reports about 90% ethanol-oxidizing extract activity for ADH II but about half the physiological acetaldehyde-reducing activity for ADH I. These are different assay directions; they do not justify treating AdhA as negligible. The older abstract does not specify ZM4. PMID:21295587 supplies direct ZM4 AdhB structural context. ED-driven Zymomonas fermentation is not an EMP two-ATP claim.

## Family grounding

Actual target UniProt membership, checked against official PANTHER names: PTHR11496 ALCOHOL DEHYDROGENASE; PTHR11496:SF102 ALCOHOL DEHYDROGENASE 4. Family labels do not independently establish substrate activity. In particular, surprising subfamily names are retained verbatim rather than relabeled to fit the pathway. No PTN selector is guessed.
