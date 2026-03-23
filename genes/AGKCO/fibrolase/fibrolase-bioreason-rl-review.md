# BioReason-Pro RL Review: fibrolase (AGKCO)

Source: fibrolase-deep-research-bioreason-rl.md

- **Correctness**: 2/5
- **Completeness**: 2/5

## Functional Summary Review

The BioReason summary states:

> A membrane-tethered zinc-dependent endopeptidase that presents an extracellular catalytic module and a single-pass membrane anchor to execute proteolysis at the cell surface. By cleaving membrane-proximal and extracellular substrates, it modulates signaling pathways that shape neural function and endocrine communication, thereby contributing to nervous system activity and stress-responsive pathways while operating as an integral membrane protein.

This summary is fundamentally incorrect in multiple ways:

1. **Not membrane-tethered**: The summary describes fibrolase as a "membrane-tethered" "integral membrane protein." The curated review explicitly states fibrolase is a "secreted venom protein" localized to the extracellular region (GO:0005576). The curated review even removes the plasma membrane annotation (GO:0005886) as incorrect: "Fibrolase is a secreted soluble enzyme that functions in the extracellular environment... It has no transmembrane domains or membrane-association motifs."

2. **Not involved in neural/endocrine function**: The summary claims fibrolase "modulates signaling pathways that shape neural function and endocrine communication." This appears to be confabulated from the generic ADAM/reprolysin family biology. Fibrolase is a snake venom metalloproteinase that cleaves fibrin and fibrinogen -- its function is fibrinolytic, disrupting hemostasis in envenomated prey.

3. **No mention of venom or fibrinolytic function**: The curated review identifies fibrolase as a "non-hemorrhagic snake venom zinc metalloproteinase (EC 3.4.24.72) from southern copperhead that exhibits direct fibrinolytic activity." The core biological processes are venom-mediated fibrinolysis (GO:0044484) and toxin activity (GO:0090729). None of this appears in the BioReason summary.

4. **Zinc metalloendopeptidase activity is the one correct element**: BioReason correctly identifies the metalloendopeptidase catalytic mechanism with zinc dependency, matching GO:0004222 in the curated review.

**Root cause**: BioReason appears to have defaulted to the generic ADAM/reprolysin family functional template (membrane-anchored sheddase involved in neural/endocrine signaling) without recognizing that fibrolase is a secreted venom enzyme. The ADAM/reprolysin domain annotation (IPR001590) covers both membrane-bound ADAMs and secreted SVMPs (snake venom metalloproteinases), but BioReason assumed the membrane-bound model.

Comparison with interpro2go:

The ai-review.yaml does not contain GO_REF:0000002 annotations for fibrolase. However, some IEA annotations make errors analogous to BioReason's: GO_REF:0000118 (TreeGrafter) assigned plasma membrane (GO:0005886), which the curated review removes. BioReason's error of inferring membrane-tethered localization parallels this automated annotation error. Both are caused by the ADAM/reprolysin domain family encompassing both membrane-bound and secreted enzymes, with the automated methods defaulting to the more common membrane-bound variant.

## Notes on thinking trace

The trace identifies the metallopeptidase catalytic domain and reprolysin/ADAM-type assignment correctly. However, it then infers "a single-pass membrane topology" and "type I membrane protease" from the ADAM family template, which is incorrect for this secreted venom protein. The trace also hypothesizes "neurexins/neuroligins or amyloid precursor-like substrates" as targets, reflecting ADAM biology rather than venom metalloproteinase biology.
