# RIM9 manual notes

## 2026-10-21

Deep research could not be generated in this environment because the configured providers were unavailable, so this review used cached primary literature, the local UniProt record, and the PTHR28013 PAINT export directly.

RIM9 is in the fungal PalI/Rim9 PTHR28013:SF3 subfamily. PANTHER places three cellular-component terms at `PTN001997363`: plasma membrane, cell division site, and growing cell tip. The plasma-membrane IBA is well supported for budding yeast because SGD:RIM9 itself is a seed for the PAINT node and Obara et al. directly imaged endogenously expressed Rim9-GFP at patchy plasma-membrane sites.

The two polarized-subcompartment IBAs are weaker for S. cerevisiae RIM9. They trace to PomBase descendants, while the cached RIM9 target paper reports patchy plasma membrane plus Golgi/endosome-like and vacuolar signals, not bud-neck, bud-tip, or mating-projection enrichment. They are kept as unresolved rather than removed because the PAINT placement is coherent for the fungal family and there is no S. cerevisiae-specific loss evidence.

The vacuolar-lumen IDA row cites an abstract-only Tos7 paper. The review keeps the row as non-core because Obara et al. do show alkaline-induced movement of Dfg16/Rim9-GFP to the vacuolar lumen, but the plasma membrane is the core functional site.

I added a conservative `NEW` `GO:0009268 response to pH` row because RIM9 lacks an existing ambient-pH process annotation despite full-text evidence that Rim9 is part of the upstream Rim101 integral-membrane pH-sensing machinery and indirectly supports pH sensing by maintaining Rim21 level and plasma-membrane localization.
