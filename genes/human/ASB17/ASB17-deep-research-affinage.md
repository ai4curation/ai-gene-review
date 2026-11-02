---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB17
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8WXJ9
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 6
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASB17 (human)

## Current model (mechanistic narrative)

ASB17 is a testis-enriched E3 ubiquitin ligase that controls spermatogenesis through substrate-specific ubiquitin-dependent proteasomal degradation [PMID:35070814, PMID:15460110, PMID:15204681]. Containing two ankyrin repeats and a SOCS box, it is expressed exclusively in spermatogenic cells, peaking in round spermatids [PMID:15460110, PMID:15204681]. During spermiation, ASB17 binds the actin-associated junctional protein ESPN and targets it for degradation to dismantle the apical ectoplasmic specialization; its loss causes ESPN accumulation, disorganized ES junctions, spermatid retention, and oligozoospermia [PMID:35070814]. ASB17 additionally promotes spermatogenic cell apoptosis by interacting with BCL2-family proteins and selectively driving ubiquitylation-dependent degradation of the anti-apoptotic factors BCLW and MCL1, with its deficiency reducing both basal and etoposide-induced germ-cell apoptosis [PMID:33803505]. Beyond the testis, ASB17 acts in immune cells where, in contrast to its degradative role, it binds the TRAF6 Zn-finger domain and stabilizes TRAF6 by inhibiting K48-linked polyubiquitination, thereby enhancing LPS-induced NF-κB-dependent cytokine expression [PMID:35174103]. Genetic redundancy with the paralog ASB15 partially buffers its spermatogenic function [PMID:36398235].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016874 ligase activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1474165 Reproduction, R-HSA-5357801 Programmed Cell Death, R-HSA-168256 Immune System
- **partners:** ESPN, BCLW, MCL1, TRAF6, ASB15
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | High | ASB17 functions as an E3 ubiquitin ligase required for spermiation; ASB17 interacts with Espin (ESPN), an actin-binding structural component of the apical ectoplasmic specialization (ES) junction, and mediates ubiquitin-dependent proteasomal degradation of ESPN to facilitate ES removal during spermiation. Knockout mice lacking ASB17 show excess ESPN accumulation, disorganized ES junctions, and retention of spermatids in the seminiferous epithelium (oligozoospermia). | PMID:35070814 | Translational andrology and urology |
| 2021 | Medium | ASB17 promotes apoptosis by interacting with BCL2 family members (BCL2, BCLX, BCLW, MCL1) and specifically targeting BCLW and MCL1 for ubiquitylation-dependent proteasomal degradation. ASB17 deficiency reduces apoptosis of spermatogenic cells and prevents etoposide-induced apoptosis of spermatogonia in vivo. Apoptosis promotion occurs in a caspase-dependent manner in vitro. | PMID:33803505 | Biology |
| 2022 | Medium | ASB17 facilitates LPS-induced NF-κB activation by interacting with TRAF6 (via ASB17 aa177–250 binding the TRAF6 Zn finger domain) and stabilizing TRAF6 protein by inhibiting K48-linked TRAF6 polyubiquitination. ASB17 knockout impairs LPS-induced pro-inflammatory cytokine expression (CCL2, IL-6) in bone marrow-derived dendritic cells. | PMID:35174103 | Frontiers in cellular and infection microbiology |
| 2004 | Medium | Murine ASB-17 is expressed exclusively in the testis and specifically in spermatogenic cells (highest in round spermatids), but not in Leydig cells or epididymis, suggesting a cell-type-specific role in spermatogenesis. The protein contains two ankyrin repeats and one SOCS box (~34 kDa, 295 aa). | PMID:15460110, PMID:15204681 | Zygote (Cambridge, England) |
| 2012 | Low | ASB-17 was identified as a binding partner of SelV (Selenoprotein V) in a yeast two-hybrid or pull-down screen; however, the specificity of this interaction was NOT confirmed by co-immunoprecipitation (which confirmed SelV interactions with OGT and ASB-9 but not ASB-17). | PMID:22670524 | Molekuliarnaia biologiia |
| 2022 | Medium | Asb15/Asb17 double-knockout mice show normal fertility but an increase in giant cells in testicular tubules, suggesting minor functional compensation between ASB15 and ASB17 during spermatogenesis. | PMID:36398235 | American journal of translational research |

## Citations

- PMID:15204681
- PMID:15460110
- PMID:22670524
- PMID:33803505
- PMID:35070814
- PMID:35174103
- PMID:36398235
