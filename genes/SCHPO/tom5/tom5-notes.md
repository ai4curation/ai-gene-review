# tom5 notes

## 2026-11-24 review

- Ran `just fetch-gene SCHPO tom5`, which created the S. pombe GOA stub and UniProt cache.
- `just fetch-gene-pmids SCHPO tom5` reported no PMIDs in GOA for tom5.
- Provider deep research was unavailable: Falcon/Perplexity were not configured and the Claude Code deep-research client was not logged in. I recorded manual research in `tom5-deep-research-manual.md` instead of creating a provider-named report.
- Ran `just paint-losses SCHPO tom5`; no IRD/IKR loss was reported on the S. pombe Tom5 lineage.
- Searched the repository and web for S. pombe tom5, SPBC19G7.19 and G2TRP7. I found no S. pombe-specific Tom5 paper that supersedes the UniProt/orthology-based curation.
- The GO-CAM model uses a root molecular_function activity for tom5. The gene review accepts the GOA `contributes_to` transporter annotation because budding-yeast Tom5 links receptors to the general import pore; this is compatible with retaining a conservative root-MF activity in the GO-CAM for the small accessory subunit.
