# palI manual notes

## 2026-10-21

Deep research could not be generated in this environment because the configured providers were unavailable, so this review used the cached full-text PalI paper, the UniProt record, and the PTHR28013 PAINT export directly.

A. nidulans PalI is itself one of the experimental descendants used by PAINT to place plasma-membrane localization at `PTN001997363`, and it is in PTHR28013:SF3 with fungal short Rim9 proteins and fission-yeast Mac1. The cached full text directly reports that functional PalI-GFP localizes to the plasma membrane, septae, and hyphal tips.

Unlike the Neurospora ortholog, palI has direct evidence for process annotations: the paper shows impaired alkaline-induced PacC processing in a null `palI` mutant and shows that coexpressed PalI specifically promotes plasma-membrane accumulation of PalH-GFP. I added those as `NEW` rows to `GO:0009268 response to pH` and `GO:1903078 positive regulation of protein localization to plasma membrane`.

## 2026-10-21 follow-up

The initial process-row terms above were superseded after review. The PacC cleavage phenotype is a cell-autonomous germling response to an alkaline shift, and the fungal comparator check points to `GO:0071469 cellular response to alkaline pH`, the term CGD uses for C. albicans ACH1, rather than the broader multicellular `GO:0010446 response to alkaline pH`.

The PalH-GFP trafficking phenotype was narrowed to `GO:0072659 protein localization to plasma membrane`: PalI promotes PalH delivery to plasma-membrane specks only in the stoichiometric coexpression experiment, while PalH is still partly internal without PalI. The Neurospora comparison above refers to the unreviewed SF3 ortholog `prr-5`/Q7SFN5.
