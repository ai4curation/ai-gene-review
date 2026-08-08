# fluG (Aspergillus nidulans) — curation notes

UniProt P38094 (FLUG_EMENI). GSI-related cytoplasmic protein; upstream-most
activator of conidiation. Upstream-activation tier of the
`conidiation_regulatory_cascade` module.

- Required for the extracellular developmental signal; fluG-null = fluffy/aconidial.
  [PMID:7926755 "The Aspergillus nidulans fluG gene is required for production of an extracellular developmental signal and is related to prokaryotic glutamine synthetase I"].
- UniProt: "May function as a GSI-related enzyme in synthesizing a small" signal —
  i.e. classical glutamine synthetase activity is putative, not demonstrated
  (A. nidulans glutamine synthesis is via GlnA). GO:0004356 / GO:1901704 kept
  non-core with this caveat; no MF asserted in core_functions.
- GO:0016787 hydrolase activity (IEA) flagged over-annotation (FluG is a GS-family
  ligase, not a hydrolase). GO:0045461 ST biosynthetic process flagged
  over-annotation (regulator → GO:0010914).
