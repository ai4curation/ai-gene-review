# MSI1 rereview notes

## 2026-09-28 IBA rereview

- Re-read `MSI1-ai-review.yaml`, `MSI1-goa.tsv`, the Falcon deep-research report, and the cached publications for the CAF-1 and Rpd3L evidence.
- Fetched `interpro/panther/PTHR22850/PTHR22850-paint.tsv` for the WD repeat RBAP46/RBAP48/MSI1 family. The current PAINT rows place broad RbAp46/48 nuclear, histone-binding, chromatin-remodeling, and transcription-regulation assertions at `PTN000522733`; a fungal RbAp48-like paralog node, `PTN001110151`, carries cytoplasm plus Rpd3L/Rpd3L-Expanded complex assertions.
- Added missing structured `propagation_review` blocks to the `GO:0005634` nucleus and `GO:0005737` cytoplasm IBA rows. The nucleus row is core and transfer is supported by direct yeast Msi1 localization plus the nuclear CAF-1 role [PMID:11238915; PMID:30239791]. The cytoplasm row is supported but non-core because direct evidence shows Msi1/Cac3 localizes to both nucleus and cytoplasm and suppresses RAS/cAMP signaling through the cytoplasmic kinase Npr1 independently of CAF-1 [PMID:11238915].
- The two Rpd3L IBA rows remain correct as `REMOVE`: `PTN001110151` spans several fungal RbAp48-like paralogs, and the current PAINT rows seed `GO:0033698` from Ume1 plus *S. pombe* Prw1 and `GO:0070210` from Prw1. In budding yeast, Ume1 is the WD40 subunit shared by Rpd3L and Rpd3S, whereas Msi1 is the CAF-1 Cac3 subunit [PMID:16286008; PMID:9030687].
- Searched for newer MSI1/CAC3 literature with queries covering `Saccharomyces MSI1 CAC3 Cac3 CAF-1` and 2024-2026. The hits were database pages, older CAF-1/RAS primary papers, theses, or homolog/plant MSI1 material; no newer primary *S. cerevisiae* MSI1/CAC3 paper changed the current functional calls.
