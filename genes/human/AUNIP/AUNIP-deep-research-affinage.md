---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AUNIP
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9H7T9
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 3
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AUNIP (human)

## Current model (mechanistic narrative)

AUNIP is a DNA-binding protein that governs DNA double-strand break (DSB) repair pathway choice by directing breaks toward homologous recombination [PMID:29042561]. It possesses intrinsic DNA-binding activity with a strong preference for substrates that mimic structures formed at stalled replication forks, and this activity is required for its own recruitment, and that of its partner CtIP, to sites of damage [PMID:29042561]. Through physical interaction with CtIP, AUNIP promotes CtIP accumulation at DSBs and thereby drives CtIP-dependent DNA-end resection and HR repair [PMID:29042561]. Loss of AUNIP, or ablation of its DNA-binding ability, sensitizes cells to DSB-inducing agents—particularly those generating replication-associated DSBs—and to single-strand-break-inducing chemotherapies, with AUNIP deficiency impairing DNA repair and heightening apoptotic susceptibility [PMID:29042561, PMID:42096614]. Genetic interaction mapping places AUNIP in a buffering relationship with the BRCA1-A complex in the context of PARP inhibitor response [PMID:37645833].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003677 DNA binding
- **localization:** GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-73894 DNA Repair
- **partners:** CTIP
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2017 | High | AUNIP physically interacts with CtIP (co-immunoprecipitation/pulldown) and is required for efficient CtIP accumulation at DNA double-strand breaks (DSBs), thereby promoting CtIP-dependent DNA-end resection and homologous recombination (HR) repair. | PMID:29042561 | Nature communications |
| 2017 | High | AUNIP possesses intrinsic DNA-binding ability with a strong preference for DNA substrates that mimic structures generated at stalled replication forks; this DNA-binding activity is necessary for recruitment of AUNIP and its binding partner CtIP to DSBs. | PMID:29042561 | Nature communications |
| 2017 | High | Loss of AUNIP or ablation of its DNA-binding ability causes cell hypersensitivity to DSB-inducing agents, particularly those that induce replication-associated DSBs, establishing AUNIP as a key determinant of DSB repair pathway choice toward HR. | PMID:29042561 | Nature communications |
| 2023 | Medium | Systematic pairwise genetic interaction mapping revealed context-specific buffering interactions between AUNIP and BRCA1-A complex genes in the context of PARP inhibitor response, placing AUNIP in a functional relationship with the BRCA1-A complex in DNA repair. | PMID:37645833 | bioRxiv |
| 2026 | Medium | AUNIP loss (CRISPR/Cas9 knockout) profoundly enhanced cytotoxicity of a TROP2-directed ADC (DS-1062a, delivering a topoisomerase I inhibitor) and multiple SSB-inducing chemotherapies in HNSCC and ESCA models; mechanistically, AUNIP deficiency led to impaired DNA repair, attenuated stress-response signaling, and heightened apoptotic susceptibility. | PMID:42096614 | Molecular carcinogenesis |

## Citations

- PMID:29042561
- PMID:37645833
- PMID:42096614
