# RIM9 manual notes

## 2026-10-21

Deep research could not be generated in this environment because the configured providers were unavailable, so this review used the cached Candida RIM9 literature, the cached 2023 LL-37 full text, the UniProt record, and the PTHR28013 PAINT export directly.

Candida albicans RIM9 is the short-form PalI/Rim9-family member in PTHR28013:SF3, separate from the long-form SRD1 protein. The abstract-level Rim9/PalI paralog study explicitly reports that RIM9, not SRD1, is important for alkaline-associated stress responses and hyphal formation.

The plasma-membrane IBA from `PTN001997363` is appropriate for the short Rim9 subfamily. The more specific `cell division site` and `growing cell tip` IBAs are much less secure for C. albicans RIM9: they are placed at the same broad Dikarya node from PomBase polarized-localization seeds, but no cached Candida paper localizes RIM9 to bud necks or hyphal tips. I kept these as over-annotated rather than removing them outright because they are plausible family localizations, just too precise for the available C. albicans evidence.

The 2023 LL-37 paper is the only newer RIM9-linked paper found in this pass. It confirms that a `rim9` deletion changes the Candida cellular response to the antimicrobial peptide LL-37, but that is a downstream stress output of the Rim101 pathway rather than RIM9's core molecular function.

## 2026-10-21 follow-up

The earlier "kept these as over-annotated" framing is superseded for `GO:0035838 growing cell tip`. The `GO:0032153 cell division site` IBA is still marked over-annotated, but now because its only IBD seed is PomBase:SPCC1739.10/Mug33 in `PTHR28013:SF6`, while C. albicans RIM9 is in `PTHR28013:SF3`; that is a cross-subfamily propagation problem rather than simply absent Candida localization evidence.

The `GO:0035838 growing cell tip` IBA was changed to `UNDECIDED` because one donor, PomBase:SPAC13G7.04c/Mac1, is in the same `PTHR28013:SF3` subfamily as RIM9 and C. albicans genuinely makes polarized hyphal tips, so the placement is plausible but untested in Candida. The open adjudication request for `PANTHER:PTN001997363` at `projects/IBA_REVIEW/rereview-2026-09-20/adjudication-requests.yaml:1603` covers these same cell-division-site, growing-cell-tip, and septum PAINT terms.
