# BioReason-Pro RL Review: GAPDH (human)

Source: GAPDH-deep-research-bioreason-rl.md

- **Correctness**: 4/5
- **Completeness**: 3/5

## Functional Summary Review

The BioReason functional summary states:

> A soluble cytoplasmic oxidoreductase that uses a nicotinamide-binding module to couple NAD-dependent redox chemistry to aldehyde- and phosphate-handling steps within central carbon metabolism. It assembles as a soluble dehydrogenase that channels triose-phosphate intermediates through a catalytic core to support energy and biosynthetic pathways in the cytoplasm, functioning as a NAD-linked hub that integrates carbohydrate breakdown with cellular energy balance.

This accurately captures GAPDH's core enzymatic function: glyceraldehyde-3-phosphate dehydrogenase activity (GO:0004365) in glycolysis (GO:0006096), using NAD+ as a cofactor. The curated review accepts these as core functions. The description of NAD binding, cytoplasmic localization, and role in central carbon metabolism is correct.

However, the summary has notable gaps:

1. **Moonlighting functions omitted**: GAPDH is one of the most well-characterized moonlighting proteins. The curated review describes roles in translational regulation (GO:0006417, kept as non-core), apoptosis (GO:0006915, kept as non-core), innate immune response (GO:0045087, kept as non-core), and nuclear functions (GO:0005634, accepted). BioReason captures none of these.

2. **The GO term predictions are strikingly wrong**: The predicted MF terms include "peptidase inhibitor activity" (GO:0030414), "endopeptidase inhibitor activity" (GO:0004866), and entirely omit the actual GAPDH enzymatic activity. This suggests the model's GO term predictions are based on a different or corrupted feature set, not aligned with the functional summary.

3. The curated review identifies NAD binding (GO:0051287) as accepted and removes several over-broad annotations (GO:0016491 oxidoreductase activity, GO:0016620 oxidoreductase activity acting on aldehydes). BioReason's summary describes the correct chemistry but the GO term output does not match.

Comparison with interpro2go:

There are no GO_REF:0000002 annotations specifically flagged in the curated GAPDH review. BioReason's reasoning from the GAPDH InterPro domains (IPR020831, IPR020828, IPR006424) correctly leads to the dehydrogenase function, which mirrors what interpro2go would produce. However, the disconnect between the sensible functional summary and the wildly inaccurate predicted GO terms (peptidase inhibitor activity?) suggests a systematic problem in the term-prediction module that is separate from the reasoning trace.

## Notes on thinking trace

The trace demonstrates competent reasoning about the Rossmann fold, NAD-binding domain, and catalytic domain architecture. The hypothesis about homotetrameric assembly is correct. The trace stays appropriately focused on the enzymatic function without over-interpreting.
