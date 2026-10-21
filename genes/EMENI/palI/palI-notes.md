# palI manual notes

## 2026-10-21

Deep research could not be generated in this environment because the configured providers were unavailable, so this review used the cached full-text PalI paper, the UniProt record, and the PTHR28013 PAINT export directly.

A. nidulans PalI is itself one of the experimental descendants used by PAINT to place plasma-membrane localization at `PTN001997363`, and it is in PTHR28013:SF3 with fungal short Rim9 proteins and fission-yeast Mac1. The cached full text directly reports that functional PalI-GFP localizes to the plasma membrane, septae, and hyphal tips.

Unlike the Neurospora ortholog, palI has direct evidence for process annotations: the paper shows impaired alkaline-induced PacC processing in a null `palI` mutant and shows that coexpressed PalI specifically promotes plasma-membrane accumulation of PalH-GFP. I added those as `NEW` rows to `GO:0009268 response to pH` and `GO:1903078 positive regulation of protein localization to plasma membrane`.
