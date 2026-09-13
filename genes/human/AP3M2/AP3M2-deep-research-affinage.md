---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AP3M2
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: P53677
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 6
citation_count: 6
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AP3M2 (human)

## Current model (mechanistic narrative)

AP3M2 is the mu-2 subunit of the AP-3 adaptor complex and functions in endolysosomal protein trafficking and the biogenesis of lysosome-related organelles (LROs) [PMID:41950095]. Its clearest mechanistic role is in pigment cells: CRISPR-Cas9 disruption of ap3m2 in zebrafish iridophores reduces guanine crystal number, alters crystal morphology, and produces distinct iridosome maturation defects, establishing AP3M2 as essential for LRO formation and crystal growth via endolysosomal trafficking [PMID:41950095]. In the nervous system, Ap3m2 knockout mice develop spontaneous epileptic seizures and show altered alcohol-related behaviors, linking the protein to GABAergic transmission, with expression controlled by an upstream H3K4me3 regulatory site [PMID:24923803]. Beyond its role in LRO biogenesis and neuronal function, AP3M2 has been linked to cytokine (IL-6) secretion in astrocytes [PMID:30371777] and to autophagy and ROS pathways in colorectal cancer cells [PMID:39488930], but these connections have not been mechanistically reconstructed in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005768 endosome, GO:0005764 lysosome
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport
- **partners:** *(none)*
- **complexes:** AP-3 adaptor complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2014 | Medium | Ap3m2 knockout mice exhibit spontaneous epileptic seizures and altered alcohol preference and withdrawal phenotypes, establishing AP3M2 as functionally relevant in the nervous system for GABAergic transmission and addiction-related behaviors. Genetic and alcohol-induced regulation of Ap3m2 expression was demonstrated, and an upstream H3K4me3 site with strain-dependent methylation differences was identified as a candidate regulatory variant. | PMID:24923803 | Genetics |
| 2007 | Medium | AP3M2 knockout mice display spontaneous epileptic seizures, implicating AP3M2 in GABAergic transmission and neuronal function. Mutation screening of AP3M2 in human epilepsy patients found no coding mutations but identified 21 sequence variations (16 novel) in UTRs and introns. | PMID:17293072 | Brain & development |
| 2019 | Low | Knockdown of AP3M2 in human iPSC-derived astrocytes reduced interleukin-6 secretion levels, placing AP3M2 in a pathway regulating cytokine secretion in astrocytes. | PMID:30371777 | Human molecular genetics |
| 2024 | Low | AP3M2 knockdown in colorectal cancer cell lines (HCT-116, CACO2, HT29) significantly reduced cell viability and revealed an interaction between AP3M2 expression and autophagy-related genes and reactive oxygen species (ROS) levels, indicating AP3M2 modulates autophagy and ROS pathways in CRC cells. | PMID:39488930 | Tissue & cell |
| 2026 | High | Ap3m2 is a key regulator of lysosome-related organelle (LRO) biogenesis in zebrafish iridophores; CRISPR-Cas9 knockout of ap3m2 caused reduced guanine crystal number, altered crystal morphology, and distinct iridosome maturation defects, establishing AP3M2 as essential for LRO formation and crystal growth through endolysosomal trafficking. | PMID:41950095 | Proceedings of the National Academy of Sciences of the United States of America |
| 2013 | Low | Molecular analysis of a transparent zebrafish pigmentation mutant (pinky) identified ap3m2 as a candidate gene, along with hps1 and rabggta, implicated in Hermansky-Pudlak syndrome-related pigment cell defects, suggesting AP3M2 involvement in chromatophore biogenesis. | PMID:23639161 | Journal of fish biology |

## Citations

- PMID:17293072
- PMID:23639161
- PMID:24923803
- PMID:30371777
- PMID:39488930
- PMID:41950095
