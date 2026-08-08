---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACTR5
affinage_run_date: 2026-06-09T22:02:40
uniprot_accession: Q9H9F9
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 3
citation_count: 2
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACTR5 (human)

## Current model (mechanistic narrative)

ACTR5 is a component of the INO80 chromatin remodeling complex that functions as a dependency for hepatocellular carcinoma proliferation [PMID:36563143]. Its loss-of-function activates CDKN2A expression and ablates CDK/E2F-driven cell cycle signaling, thereby attenuating tumor growth [PMID:36563143]. ACTR5 acts together with its partner IES6 through a mechanism distinct from the canonical INO80 complex, since high-density CRISPR tiling profiles of ACTR5 and IES6 diverge from those of other INO80 subunits [PMID:36563143]. Beyond this chromatin-associated cell cycle role, no further biochemical mechanism (substrate specificity, recruitment, or structural basis of CDKN2A repression) has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle, R-HSA-4839726 Chromatin organization
- **partners:** IES6
- **complexes:** INO80 chromatin remodeling complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2022 | Medium | ACTR5, a component of the INO80 chromatin remodeling complex, is essential for hepatocellular carcinoma (HCC) tumor progression; its suppression activates CDKN2A expression and ablates CDK/E2F-driven cell cycle signaling, attenuating HCC tumor growth. | PMID:36563143 | Science advances |
| 2022 | Medium | ACTR5 and its interacting partner IES6 operate via an INO80-independent mechanism to support HCC cell proliferation, as revealed by differential CRISPR tiling profiles compared to other INO80 complex members. | PMID:36563143 | Science advances |
| 2025 | Low | A de novo variant in ACTR5 enhanced type I interferon (IFN-β) signaling, placing ACTR5 as a positive regulator of type I IFN signaling. | PMID:40386946 | Arthritis & rheumatology (Hoboken, N.J.) |

## Citations

- PMID:36563143
- PMID:40386946
