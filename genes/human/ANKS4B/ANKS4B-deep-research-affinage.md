---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKS4B
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8N8V4
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 8
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKS4B (human)

## Current model (mechanistic narrative)

ANKS4B is a multifunctional scaffold protein whose expression is driven by the transcription factors HNF4α and HNF1α, placing it downstream of these master regulators in multiple tissues [PMID:22589549, PMID:32793175]. Its best-defined role is as an organizer of the apical brush border: it is targeted to microvilli by a noncanonical cryptic sequence containing a coiled-coil motif and a basic-hydrophobic repeat, where the isolated region behaves as an oligomer [PMID:32636301]. There it assembles a tripartite complex with MYO7B and USH1C that undergoes liquid-liquid phase separation through strong multivalent interactions, generating dense condensates implicated in intermicrovillar adhesion and brush border assembly [PMID:31644917]. This activity distinguishes ANKS4B from its closest ankyrin-repeat homologs USH1G/SANS, which cannot target microvilli via the corresponding region [PMID:32636301]. In pancreatic β-cells, ANKS4B binds the ER chaperone GRP78 and modulates ER stress-induced apoptosis, with overexpression enhancing and suppression reducing susceptibility to ER-stress death [PMID:22589549]. Independently, ANKS4B restricts Zika virus replication by suppressing virus-induced autophagy without affecting viral entry [PMID:32793175].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0140313 molecular sequestering activity
- **localization:** GO:0005856 cytoskeleton, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-9612973 Autophagy
- **partners:** MYO7B, USH1C, GRP78
- **complexes:** ANKS4B–MYO7B–USH1C intermicrovillar adhesion complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2012 | High | ANKS4B (Anks4b) is a direct transcriptional target of HNF4α in pancreatic β-cells; HNF4α activates the Anks4b promoter, and Anks4b expression is decreased in β-cell-specific HNF4α knockout islets and HNF4α knockdown MIN6 cells. | PMID:22589549 | The Journal of biological chemistry |
| 2012 | Medium | ANKS4B protein binds to GRP78 (glucose-regulated protein 78), a major ER chaperone, and overexpression of ANKS4B enhances ER stress response and ER stress-associated apoptosis in MIN6 β-cells, while suppression of ANKS4B reduces β-cell susceptibility to ER stress-induced apoptosis. | PMID:22589549 | The Journal of biological chemistry |
| 2019 | High | ANKS4B, MYO7B, and USH1C form a specific tripartite complex that undergoes liquid-liquid phase separation in vitro and in cells, generating dense condensates; this phase separation requires strong multivalent interactions among the three proteins and is proposed to underlie tip-link density formation in microvilli. | PMID:31644917 | Cell reports |
| 2020 | High | ANKS4B is directed to apical brush border microvilli by a noncanonical cryptic targeting sequence in a previously unannotated region; this region contains a coiled-coil motif and a basic-hydrophobic repeat required for microvillar targeting and brush border assembly, and the isolated sequence functions as an oligomer. | PMID:32636301 | The Journal of biological chemistry |
| 2020 | Medium | The closest homolog of ANKS4B, USH1G, lacks the inherent ability to target to microvilli via the corresponding sequence region, identifying a point of functional divergence between the two ankyrin repeat-based scaffolds. | PMID:32636301 | The Journal of biological chemistry |
| 2020 | Medium | ANKS4B restricts Zika virus (ZIKV) replication by suppressing ZIKV-induced autophagy; ANKS4B knockout cells show enhanced viral RNA, protein, and titer, and inhibition of autophagy equalizes replication levels between ANKS4B-sufficient and -deficient cells. ANKS4B does not affect viral entry. | PMID:32793175 | Frontiers in microbiology |
| 2020 | Medium | ZIKV infection downregulates ANKS4B expression by reducing the levels of its transcriptional activators HNF1α and HNF4α in cultured cells and neonatal mice. | PMID:32793175 | Frontiers in microbiology |
| 2024 | Low | ANKS4B contains predicted nuclear export sequences (NESs) but lacks functional nuclear localization sequences (NLSs), contrasting with its paralog SANS/USH1G which shuttles between nucleus and cytoplasm; ANKS4B does not localize to the nucleus and does not interact with the nuclear splicing protein PRPF31. | PMID:39594604 | Cells |

## Citations

- PMID:22589549
- PMID:31644917
- PMID:32636301
- PMID:32793175
- PMID:39594604
