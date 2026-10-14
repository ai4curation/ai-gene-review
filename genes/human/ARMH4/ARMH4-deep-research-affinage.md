---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARMH4
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q86TY3
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARMH4 (human)

## Current model (mechanistic narrative)

ARMH4 is a cell-surface protein with intracellular signaling competence that potentiates growth-factor receptor signaling and shapes cellular morphology and inflammatory output across tissues [PMID:36220098, PMID:41390521]. Mechanistically, ARMH4 physically interacts with the receptor tyrosine kinases IGF1R and FGFR1 to sensitize the PI3K-Akt-mTORC1 and Ras-MEK-ERK pathways, thereby promoting protein synthesis and suppressing autophagy; it further sustains IGF1R and FGFR1 expression through the transcription factor c-Myc, establishing a positive-feedback growth circuit that drives aging [PMID:41390521]. In cerebellar Purkinje cells, ARMH4 regulates dendrite morphogenesis through its conserved cytoplasmic domain in a manner augmented by disrupting its endocytosis, consistent with surface-localized signaling [PMID:36220098]. In podocytes, ARMH4 suppresses release of the inflammatory mediators IL-1β and IL-8 [PMID:36649229]. Upstream transcriptional inputs include LMX1B in podocytes [PMID:36649229] and Wnt/β-catenin signaling in cardiac progenitors [PMID:31655130].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-162582 Signal Transduction
- **partners:** IGF1R, FGFR1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2022 | Medium | Armh4 has a critical, multifaceted role in Purkinje cell dendrite morphogenesis in mice. Armh4 overexpression disrupts dendrite morphogenesis, and this effect requires its conserved cytoplasmic domain and is augmented by disrupting its endocytosis, placing Armh4 at the cell surface with intracellular signaling competence. | PMID:36220098 | Neuron |
| 2023 | Medium | ARMH4 overexpression in primary kidney epithelial cells reduces release of inflammatory mediators IL-1β and IL-8 (CXCL8), while ARMH4 silencing in mature human podocytes has the opposite effect, indicating ARMH4 modulates cytokine release and inflammatory signaling in podocytes. | PMID:36649229 | PloS one |
| 2023 | Low | ARMH4 transcript levels increase in response to overexpression of the podocyte transcription factor LMX1B, identifying LMX1B as an upstream transcriptional regulator of ARMH4 in podocytes. | PMID:36649229 | PloS one |
| 2019 | Low | Lithium chloride-induced stimulation of Wnt/β-catenin signaling elevates Armh4 expression in second heart field subpharyngeal mesodermal progenitors and outflow tract/right ventricle/atrial cardiomyocytes, placing Armh4 downstream of Wnt/β-catenin in cardiac progenitors. | PMID:31655130 | Gene expression patterns : GEP |
| 2025 | Medium | ARMH4 interacts physically with IGF1R and FGFR1 to sensitize activation of the PI3K-Akt-mTORC1 and Ras-MEK-ERK pathways, promoting protein synthesis and inhibiting autophagy. Additionally, ARMH4 is required to maintain IGF1R and FGFR1 expression levels through regulation of the transcription factor c-Myc, forming a positive-feedback growth signaling circuit that promotes aging. | PMID:41390521 | Nature communications |

## Citations

- PMID:31655130
- PMID:36220098
- PMID:36649229
- PMID:41390521
