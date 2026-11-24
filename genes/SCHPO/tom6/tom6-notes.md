# tom6 notes

## 2026-11-24 review

- Ran `just fetch-gene SCHPO tom6`, which created the S. pombe GOA stub and UniProt cache.
- `just fetch-gene-pmids SCHPO tom6` reported no PMIDs in GOA for tom6.
- Provider deep research was unavailable: Falcon/Perplexity were not configured and the Claude Code deep-research client was not logged in. I recorded manual research in `tom6-deep-research-manual.md` instead of creating a provider-named report.
- `just paint-losses SCHPO tom6` could not check losses because the UniProt record has no PANTHER family assignment.
- Searched the repository and web for S. pombe tom6, SPAC823.17 and O13886. I found no S. pombe-specific Tom6 paper that supersedes the UniProt/orthology-based curation.
- I deliberately did not add matrix/IMS/inner-membrane TOM route process rows to tom6: the fetched GOA has no such rows, Tom6 is best supported as a Tom22/Tom40 assembly and stability factor, and adding every TOM-mediated route from the complex role alone would over-annotate a sparse review.
- The GO-CAM model uses a root molecular_function activity for tom6. This remains appropriately conservative because the review identifies a TOM-complex structural or assembly role rather than a specific elemental molecular_function term.
