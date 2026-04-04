# BioReason-Pro RL Review: pmp20 (SCHPO)

Source: pmp20-deep-research-bioreason-rl.md

- **Correctness**: 1/5
- **Completeness**: 2/5

This is a clear case of BioReason calling a pseudoenzyme active. The curated review, backed by direct experimental evidence (PMID:20356456), establishes that pmp20 has **no thioredoxin-dependent peroxidase activity** and **no glutathione peroxidase activity**. The protein lacks the resolving cysteine required for the canonical peroxiredoxin catalytic cycle. Bioinformatics analysis confirmed only one cysteine (C43) with no resolving-cysteine equivalent. Instead, pmp20 functions as a weak molecular chaperone (holdase), representing a neo-functionalization within the peroxiredoxin family.

BioReason assigns peroxidase activity (GO:0004601) as the molecular function and "response to oxidative stress" (GO:0006979) as the biological process, describing the protein as "a soluble cytoplasmic peroxidase that uses a thioredoxin-like fold to reduce hydrogen peroxide and organic hydroperoxides." This is fundamentally wrong. The model even describes a full peroxiredoxin catalytic cycle with "sulfenic acid" formation and "thioredoxin/thioredoxin reductase" regeneration -- none of which applies to pmp20.

The InterPro domains (thioredoxin-like superfamily, Peroxiredoxin-5-like family) are correctly identified, but BioReason commits the classic error of assuming domain identity equals function. It does not account for the loss of the resolving cysteine or the experimental evidence showing no peroxidase activity. Notably, the GO terms listed from the database include unfolded protein binding (GO:0051082) and protein refolding (GO:0042026), which are consistent with the chaperone function, but BioReason's reasoning completely ignores these in favor of the peroxidase narrative.

BioReason correctly identifies cytoplasmic localization, which is partially correct (the curated review specifies cytosol and nucleus based on HDA data from PMID:16823372).

Key failure modes: **pseudoenzyme called active**; complete failure to integrate negative evidence; **fold-bias** from peroxiredoxin domain leading to wrong function; missing the chaperone neo-functionalization that is the actual biology.
