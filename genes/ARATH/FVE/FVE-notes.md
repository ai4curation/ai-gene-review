# FVE / MSI4 (At2g19520, UniProt O22607) curation notes

## 2026-10 review session (autonomous pathway module)

- Accession verified: O22607 MSI4_ARATH; UniProt primary name MSI4, synonyms FVE, ACG1. Folder uses the flowering-pathway symbol FVE (gene_symbol FVE in stub).
- Deep research (falcon) failed (HTTP 402).
- RbAp48-like WD40 protein; FLC chromatin hyperacetylated in fve [PMID:14745447 "We conclude that FVE participates in a protein complex repressing FLC transcription through a histone deacetylation mechanism."]
- CUL4-DDB1 and CLF-PRC2 [PMID:21282611 "the MSI4 protein is a DDB1 and CUL4-associated factor that represses FLC expression through its association with a CLF-Polycomb Repressive Complex 2 (PRC2)"]
- PDP/LHP1 PRC2 [PMID:29314758 "We demonstrated that FVE, MSI5, and PDP3 were co-purified with LHP1."]
- HDA5/HDA6/FLD complex [PMID:25922987].
- RdDM via SUVH9 [PMID:33942410]; cold-response repressor (acg1) [PMID:14745450].

## Decisions
- Core: histone binding (IBA) in PRC2 (ESC/E(Z) complex) and HDAC complexes.
- 12 bare protein-binding rows removed (complex memberships captured by CC terms).
- Metal ion binding -> zinc ion binding (non-core).
- Photoperiodism flowering term -> GO:0048510.


## 2026-10-26 complete annotation audit

All42 rows were reassessed. PRC2-associated CC assertions are retained with context-specific membership, while the description no longer calls FVE an invariant core subunit or implies that one fixed HDA5/HDA6/FLD assembly explains all activity. Both epigenetic-regulation rows now share the same directional refinement. The mitochondrial HDA row retains OVER only after inspecting all seven deposited spreadsheets: exact FVE entries say nucleus and the mixed-microsome experiment does not establish mitochondrial residence. This supersedes the old absence-of-targeting-signal rationale. Cytoplasmic/cytosolic and nucleolar experimental reports are retained separately with source-access limits; nuclear function is not used to reject them. DA photoperiodism remains unresolved, not dismissed by the label autonomous. See FVE-source-analysis for checksummed extraction. No new annotations were added.

All seeded rows were reviewed, with original term, evidence, source, supporting-entity and qualifier/NOT payloads preserved. The shared normal Falcon attempt and perplexity-lite fallback both failed; logs are retained under `.cache/module-audit-logs/autonomous-flowering-fetch/ARATH-FVE-provider.log`. No provider report was fabricated. Manual primary-literature assessment and normal publication fetching supplied this review. Source access limits are stated per reference/claim. Generic protein binding follows the current informative-function policy; its removal does not reject the physical interactions. Nuclear localization does not by itself exclude additional compartments.

The final source check supersedes the earlier unverified retention rationale for the cytoplasm/cytosol rows: both are now UNDECIDED because their exact target image/table could not be recovered. The nucleolar row remains non-core on independent direct target corroboration in PMID:15608277 Figure1 (NU:no:NAS), not merely nuclear plausibility. Original nuclear assertions are independently supported and retained. No experimental localization is removed for incomplete access.
