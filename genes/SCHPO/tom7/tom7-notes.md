# tom7 notes

## 2026-11-24 review

- Ran `just fetch-gene SCHPO tom7`, which created the S. pombe GOA stub and UniProt cache.
- `just fetch-gene-pmids SCHPO tom7` reported no PMIDs in GOA for tom7.
- Provider deep research was unavailable: Falcon/Perplexity were not configured and the Claude Code deep-research client was not logged in. I recorded manual research in `tom7-deep-research-manual.md` instead of creating a provider-named report.
- Ran `just paint-losses SCHPO tom7`; no IRD/IKR loss was reported on the S. pombe Tom7 lineage.
- Searched the repository and web for `Schizosaccharomyces pombe tom7`, `SPBC27B12.10c`, `O42999`, and Tom7 fission yeast terms. A manual literature search found no S. pombe Tom7 paper defining a molecular activity more specific than its TOM-complex structural or regulatory role.
- The GO-CAM model uses a root molecular_function activity for tom7. This agrees with retaining the PomBase MF ND row because the review did not identify a more specific elemental molecular_function term.
