# RIM9 manual notes

## 2026-10-21

Deep research could not be generated in this environment because the configured providers were unavailable, so this review used cached primary literature, the local UniProt record, and the PTHR28013 PAINT export directly.

RIM9 is in the fungal PalI/Rim9 PTHR28013:SF3 subfamily. PANTHER places three cellular-component terms at `PTN001997363`: plasma membrane, cell division site, and growing cell tip. The plasma-membrane IBA is well supported for budding yeast because SGD:RIM9 itself is a seed for the PAINT node and Obara et al. directly imaged endogenously expressed Rim9-GFP at patchy plasma-membrane sites.

The two polarized-subcompartment IBAs are weaker for S. cerevisiae RIM9. They trace to PomBase descendants, while the cached RIM9 target paper reports patchy plasma membrane plus Golgi/endosome-like and vacuolar signals, not bud-neck, bud-tip, or mating-projection enrichment. They are kept as unresolved rather than removed because the PAINT placement is coherent for the fungal family and there is no S. cerevisiae-specific loss evidence.

The vacuolar-lumen IDA row cites an abstract-only Tos7 paper. The review keeps the row as non-core because Obara et al. do show alkaline-induced movement of Dfg16/Rim9-GFP to the vacuolar lumen, but the plasma membrane is the core functional site.

I did not keep a new pH-response process row for RIM9. Li and Mitchell show that `rim9` mutants block Rim1/Rim101 C-terminal cleavage under alkaline growth conditions, but the later AID experiment in Obara et al. argues that Rim9 is an auxiliary stabilizing component rather than the pH sensor that directly performs signal recognition; the plasma-membrane localization rows and the core-function prose capture the supported role without asserting a new broad process annotation.
