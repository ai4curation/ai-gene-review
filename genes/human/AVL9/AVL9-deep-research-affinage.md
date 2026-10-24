---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AVL9
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8NBF6
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 5
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AVL9 (human)

## Current model (mechanistic narrative)

AVL9 is a trafficking-associated scaffold and GTPase-activating protein that links membrane transport to cell proliferation, migration, and oncogenic signaling [PMID:25621300, PMID:39566663]. It possesses robust GAP activity toward the Arf1 GTPase and is recruited to secretory vesicles by Rab8, placing it within the secretory/vesicle-trafficking machinery [PMID:41542567]. Loss of AVL9 disrupts intracellular trafficking and mitosis and alters cell migration [PMID:25621300], and in carcinoma cells AVL9 promotes migration through regulation of EGFR, which acts downstream of AVL9 [PMID:34991461], and activates the cyclin-dependent kinase pathway [PMID:33683834]. In pancreatic ductal adenocarcinoma, hypoxia drives HIF-1α-dependent transcription of AVL9, and the induced protein acts as a scaffold that bridges IκBα to SKP1 to enhance IκBα ubiquitination and degradation, thereby activating NF-κB signaling and contributing to chemoresistance [PMID:39566663].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-162582 Signal Transduction
- **partners:** IKBA, SKP1, RAB8, ARF1
- **complexes:** AVL9-IκBα-SKP1 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2014 | Medium | AVL9 knockdown in MDCK cells causes abnormal cystogenesis, arising from both aberrant intracellular trafficking and defective mitosis, and promotes cell migration; establishing roles for AVL9 in intracellular trafficking and cell cycle progression. | PMID:25621300 | Oncoscience |
| 2022 | Medium | AVL9 promotes colorectal carcinoma cell migration by regulating EGFR expression; EGFR knockdown rescues AVL9-induced migration, placing EGFR downstream of AVL9 in this pathway. | PMID:34991461 | Biological procedures online |
| 2024 | High | HIF-1α drives AVL9 transcription under hypoxia in PDAC. AVL9 acts as a scaffold protein that facilitates binding of IκBα to SKP1, leading to enhanced ubiquitination and degradation of IκBα and consequent NF-κB pathway activation, contributing to chemoresistance. | PMID:39566663 | Gastroenterology |
| 2021 | Medium | ALMS1-IT1 lncRNA promotes LUAD cell proliferation, migration and invasion at least partly through AVL9; overexpression of AVL9 rescues the anti-proliferative/migration effects of ALMS1-IT1 knockdown. AVL9 activates the cyclin-dependent kinase pathway, and AVL9 knockdown reverses this activation. | PMID:33683834 | FEBS open bio |
| 2026 | High | Avl9 (and its human ortholog) possesses robust GTPase-activating protein (GAP) activity towards Arf1 GTPase. Avl9 is recruited to secretory vesicles by Rab8, consistent with its role in secretion and cell migration. | PMID:41542567 | bioRxiv |

## Citations

- PMID:25621300
- PMID:33683834
- PMID:34991461
- PMID:39566663
- PMID:41542567
