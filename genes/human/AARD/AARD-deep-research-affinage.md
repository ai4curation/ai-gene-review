---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AARD
affinage_run_date: 2026-06-09T22:02:35
uniprot_accession: Q4LEZ3
self_evaluation_pairwise: 
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

# Affinage mechanistic annotation for AARD (human)

## Current model (mechanistic narrative)

AARD is a Sertoli cell-specific protein that functions as a transcriptional target of androgen signaling during testis development [PMID:17486547, PMID:27959439]. Its expression is restricted to Sertoli cells, where it is upregulated during mouse testis differentiation coincident with early testis cord formation [PMID:17486547]. Ligand-bound androgen receptor (AR) directly activates Aard transcription by binding an androgen-responsive element in its promoter; accordingly, AARD protein is lost in Sertoli cell-selective AR knockout mice and induced by testosterone in primary Sertoli cells [PMID:27959439]. Beyond its position downstream of AR signaling in the Sertoli cell, no molecular activity, interaction partners, or cellular function for AARD have been characterized in the available corpus.

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
| 2007 | Medium | Aard mRNA expression is specifically upregulated in Sertoli cells during mouse testis differentiation, with elevated expression coinciding with early testis cord formation; expression is restricted to Sertoli cells in both embryonic and adult mouse testis. | PMID:17486547 | The International journal of developmental biology |
| 2016 | High | Aard transcription in mouse Sertoli cells is directly regulated by androgen receptor (AR): ligand-bound AR binds the androgen-responsive element in the Aard promoter to activate transcription; AARD protein is downregulated in Sertoli cell-selective AR knockout mice and upregulated by testosterone in primary Sertoli cells in vitro. | PMID:27959439 | Molecular medicine reports |

## Citations

- PMID:17486547
- PMID:27959439
