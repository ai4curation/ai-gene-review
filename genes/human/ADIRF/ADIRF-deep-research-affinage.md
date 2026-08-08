---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADIRF
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q15847
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 2
citation_count: 2
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADIRF (human)

## Current model (mechanistic narrative)

ADIRF (also designated APM2/C10orf116) is implicated in cancer chemoresistance and adipocyte biology. In cancer cells, ADIRF acts as a mediator of cisplatin resistance: its overexpression renders sensitive cells resistant, while its silencing sensitizes diverse tumor cell lines to cisplatin and impairs xenograft growth under cisplatin treatment, an effect operating independently of p53 status and mismatch-repair proficiency [PMID:19444912]. The molecular pathway through which ADIRF confers this resistance has not been defined in the available corpus. A separate Low-confidence finding links ADIRF to preadipocyte proliferation, apoptosis suppression, and insulin-stimulated glucose uptake via GLUT4 upregulation [PMID:23467766]. Beyond these phenotypic associations, no direct molecular activity, binding partner, or structural mechanism for ADIRF has been characterized.

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** *(none)*
- **localization:** *(none)*
- **pathway (Reactome):** *(none)*
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2009 | Medium | Overexpression of APM2 (ADIRF) in cisplatin-sensitive HCT116 cells promoted cisplatin resistance, while siRNA-mediated silencing of APM2 sensitized a panel of cancer cell lines (HCT116-K, HCT116, SW620, MCF7, PC-3, OV2008) to cisplatin regardless of p53 status or mismatch-repair (MMR) proficiency. Stable shRNA knockdown of APM2 also significantly inhibited growth of tumor xenografts (HCT116-K and OV2008) in response to cisplatin treatment, establishing APM2 as a mediator of cisplatin resistance. | PMID:19444912 | International journal of cancer |
| 2013 | Low | Overexpression of C10orf116 (ADIRF) in 3T3-L1 preadipocytes stimulated cell proliferation and inhibited apoptosis. Additionally, ectopic C10orf116 expression significantly increased insulin-stimulated glucose uptake in adipocytes by upregulating glucose transporter type 4 (GLUT4) expression, supporting a role for ADIRF in regulating glucose transport and preadipocyte number. | PMID:23467766 | Molecular medicine reports |

## Citations

- PMID:19444912
- PMID:23467766
