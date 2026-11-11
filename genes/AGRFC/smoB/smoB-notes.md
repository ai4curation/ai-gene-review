# smoB (Atu3278, A9CEY6) notes

## Deep research
- 2026-11-10: perplexity deep research fails in this environment (no provider credentials;
  "All providers failed", tried on smoA). Review built from UniProt and cached literature.

## Literature (PMID:35074914, full text)
- Originally annotated as SDR; hypothesized 6-OG reductase. Activity shown by 18O exchange at C6 of
  glucose with NADP+ only
  [PMID:35074914 "Only enzymatic reactions conducted in the presence of NADP+ produced product labeled with 18O at C6: NAD+ failed to produce any product, supporting our observations by ITC and defining the cofactor specificity of SmoB."]
- ITC: NADPH Kd ~2 uM, no NADH binding.
- Structures 7BBY/7BBZ/7BC0/7BC1; trimer; AKR fold; catalytic tetrad Asp71/Tyr76/Lys104/His151
  [PMID:35074914 "The overall fold has high structural conservation with members of the aldo-keto reductase (AKR) superfamily."]

## Decisions
- cytosol (TreeGrafter): KEEP_AS_NON_CORE (soluble, intracellular pathway).
- oxidoreductase activity (InterPro): MODIFY to GO:0016616.
- NEW GO:1902777 (performs the terminal pathway step).
- Proposed NTR 6-dehydroglucose reductase activity (RHEA:70779, EC 1.1.1.432).
- PANTHER PTHR43364:SF1 (OXIDOREDUCTASE YDHF), with E. coli YdhF and B. subtilis YcsN.
