# LD / LUMINIDEPENDENS (At4g02560, UniProt Q38796) curation notes

## 2026-10 review session (autonomous pathway module)

- Accession verified: Q38796 LUMI_ARATH, At4g02560.
- Deep research (falcon) failed (HTTP 429).
- Nuclear, apex-expressed [PMID:10363371 "Subcellular localization studies indicate that LD is a nuclear protein, consistent with its previously proposed transcriptional regulatory role."]
- FLD/LD/SDG26 complex [PMID:32541063]; AuPC with APRF1, EFLs [PMID:35766439 "We demonstrate that these components form a multi-subunit autonomous pathway complex (AuPC)."]
- Ref2/PNUTS-like CPF phosphatase module subunit with APRF1/TOPP4 [PMID:38851185 "LD is structurally related to Ref2 in yeast and PNUTS in mammals."]
- SUF4 interaction [PMID:17138694 "Thus, we propose that LD binds to SUF4 to suppress its activity in the absence of FRI ."]
- Prion-like domain [PMID:27114519].

## Decisions
- DNA binding (IEA) and DNA-binding TF activity (TAS x2) marked over-annotated: no DNA binding shown; homeodomain-like region is a TFIIS-type bundle; DNA binding in AuPC maps to SDG26.
- SUF4 protein binding -> DNA-binding transcription factor binding (GO:0140297).
- NEW: negative regulation of gene expression, epigenetic (GO:0045814).
- No MF assigned in core function (no GO term fits a PNUTS-like scaffold without demonstrated PP1 regulation).


## 2026-10-26 complete annotation audit

All 15 existing rows, including the prior NEW epigenetic-process assertion, were reassessed and retained in payload. The newer PMID:38851185 full text supports LD as a Ref2/PNUTS-like bridge rather than a DNA-binding transcription factor. It explicitly leaves the phosphatase substrate unresolved; the prior question about whether any LD phosphatase-module role exists has been updated to this experimentally meaningful gap. The SUF4 interaction remains a specific TF-binding refinement, and the primary genetic/chromatin evidence supports flowering and transcriptional regulation. No catalytic MF was manufactured for LD.

All seeded rows were reviewed, with original term, evidence, source, supporting-entity and qualifier/NOT payloads preserved. The shared normal Falcon attempt and perplexity-lite fallback both failed; logs are retained under `.cache/module-audit-logs/autonomous-flowering-fetch/ARATH-LD-provider.log`. No provider report was fabricated. Manual primary-literature assessment and normal publication fetching supplied this review. Source access limits are stated per reference/claim. Generic protein binding follows the current informative-function policy; its removal does not reject the physical interactions. Nuclear localization does not by itself exclude additional compartments.
