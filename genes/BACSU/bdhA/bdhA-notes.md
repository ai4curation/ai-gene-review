# bdhA: bacterial fermentation review

## Scope and research

Reviewed all 11 seeded rows for BACSU/bdhA (O34788); original terms, evidence, references and supporting entities are preserved. Manual primary-source research and the annotation-reviewer/core-function-synthesizer workflows were used. The default Falcon request and automatic Perplexity-lite fallback both failed (session log `/tmp/alcohol-bdhA-deep.log`); no provider-authored report was fabricated. The wrapper did not expose a more specific cause. `fetch-fitness` was attempted but returned no usable FEBA data (`/tmp/alcohol-bdhA-fitness.log`); no fitness inference is made. No accession match was found in `gocams/index.tsv`.

## Biological synthesis

BdhA, formerly YdjL, is the major acetoin reductase/2,3-butanediol dehydrogenase of Bacillus subtilis. The zinc-containing enzyme catalyzes NADH-dependent reduction of (R)-acetoin to (R,R)-2,3-butanediol and the reverse NAD+-dependent oxidation. It acts in the cytoplasm during oxygen-limited fermentation; loss of bdhA abolishes detectable acetoin reductase/butanediol dehydrogenase activity and early stationary-phase butanediol production. A pool of the protein also accumulates extracellularly during stationary phase.

- [PMID:18820069](https://pubmed.ncbi.nlm.nih.gov/18820069/): Direct native bdhA/ydjL disruption and enzyme activities establish the major acetoin/butanediol conversion step; abstract-only cache does not itself resolve product enantiomers.
- [PMID:21856851](https://pubmed.ncbi.nlm.nih.gov/21856851/): Full-text protein identification includes YdjL in the medium, supporting contextual extracellular localization as well as the curated cytoplasmic pool.
- [PMID:33722570](https://pubmed.ncbi.nlm.nih.gov/33722570/): Full text lists BdhA in the BrxC-associated proteome; it does not establish a specific BdhA redox-repair mechanism.
- [PMID:36781054](https://pubmed.ncbi.nlm.nih.gov/36781054/): Direct B. subtilis R,R-BDH structure and enzymatic characterization support catalytic zinc and stereochemical substrate preference; the target record links the same enzyme to PDB 6IE0.

## Curation boundaries

No new process annotation was added to fill a pathway diagram. Exact catalytic functions supply the core synthesis. Broad molecular-function rows are refined rather than removed. Duplicate claims receive consistent actions. Abstract-only sources are identified in reference assessments, and assay conditions or strain identities not stated there are not invented.

PMID:18820069 establishes the native reaction but its abstract does not report chiral separation. The curated Rhea reaction and later structure/enzymatic characterization PMID:36781054 support the R,R assignment. Stationary-phase secretion is retained as non-core; protein association with BrxC does not establish a new catalytic or regulatory function. Very late residual butanediol in the knockout suggests a minor alternative route.

## Family grounding

Actual target UniProt membership, checked against official PANTHER names: PTHR43161 SORBITOL DEHYDROGENASE; PTHR43161:SF26 GALACTITOL 1-PHOSPHATE 5-DEHYDROGENASE. Family labels do not independently establish substrate activity. In particular, surprising subfamily names are retained verbatim rather than relabeled to fit the pathway. No PTN selector is guessed.
