# TMEM175 review notes

## Why this gene was selected

Flagged in `projects/FUNCTION_KNOWLEDGE_GAPS/contested-functions-2025-2026.md` as the sharpest
contested-function case found in the 2025-2026 literature: GOA carries `proton channel activity`
and `potassium ion leak channel activity` for the same protein, each with IDA support, and two
2026 papers reach opposite conclusions about which is the physiological function.

## The K+ channel assignment (consensus)

TMEM175 was identified as the endolysosomal K+ leak conductance:
[PMID:26317472 "Here, we directly recorded organelle K(+) conductance and discovered a major
K(+)-selective channel KEL on endosomes and lysosomes. KEL is formed by TMEM175, a protein with
unknown function."] and [PMID:26317472 "Lysosomes lacking TMEM175 exhibit no K(+) conductance,
have a markedly depolarized"].

Independently confirmed with structure-function analysis of selectivity in the absence of a
canonical TVGYG filter: [PMID:32228865 "Transmembrane protein 175 (TMEM175) was recently
identified as a constitutively-active potassium (K+) selective channel expressed in lysosomal
membranes responsible for establishing a membrane potential across the lysosomal membrane"].

Structural work on the prokaryotic ortholog established the selectivity series:
[PMID:28723891 "These results show that CmTMEM175 is selective for K+, Rb+ and Cs+ over Na+,
consistent with the selectivity of the eukaryotic TMEM175."].

## The H+ channel assignment (contested)

Three groups reported proton conduction:
[PMID:35750034 "Parkinson's disease-risk protein TMEM175 is a proton-activated proton channel in
lysosomes."], [PMID:35333573 "pH regulates potassium conductance and drives a constitutive proton
current in human TMEM175."], and [PMID:37390818 "Upon changing the bath pH to acidic
conditions, TMEM175 becomes a proton-activated proton channel conducting a higher inward proton
current at lower pH (Figure 2C)."].

This is directly challenged in 2026:
[PMID:41134537 "Thus, we conclude that the primary function of lysosomal TMEM175 is to conduct K+,
not protons."] with the key phenotypic argument
[PMID:41134537 "Finally, pH measurements in a range of cell types with TMEM175 knockouts reveal
either no pH change or alkalinization, opposite to the prediction if the protein is a proton
channel."].

The opposing 2026 position maintains proton selectivity at acidic luminal pH:
[PMID:41533442 "While follow-up studies confirmed a dominant K+-conductance at neutral pH, it was
shown that acidic pH on the luminal side (pHlum) of TMEM175 strongly increases channel conductance
and shifts ion selectivity in favor of H+"].

A Journal of Cell Biology commentary summarises the state of play:
[PMID:41295951 "demonstrate that TMEM175 is instead a K+ channel, minimally permeable to H+."]

## Curation position taken

- `GO:0022841` potassium ion leak channel activity → **core**. Supported by independent labs across
  a decade, and not contested by either 2026 paper (both agree K+ conductance dominates at neutral pH).
- `GO:0015252` proton channel activity and the associated BP terms (`GO:0035752`, `GO:1902600`) →
  **KEEP_AS_NON_CORE**, with the dispute recorded in each `reason`. Not removed: these are
  experimental annotations whose underlying recordings are real, and a channel can be genuinely
  H+-permeable without that being its physiological role. Per project rules, an IDA is not
  overruled from an abstract.
- `GO:0005267` potassium channel activity → **MODIFY** to `GO:0022841`; correct in kind but
  under-specific, since the channel is constitutively open rather than gated.
- `GO:0050544` arachidonate binding → non-core modulatory input.
- Bare `protein binding` → over-annotated.

## Open question for experts

Is the disagreement reconcilable as a difference in recording configuration (luminal pH, excised
patch vs whole-lysosome) rather than a contradiction? Both 2026 papers agree K+ dominates at
neutral pH; they disagree about behaviour at acidic luminal pH and about the magnitude of the
native lysosomal H+ leak.
