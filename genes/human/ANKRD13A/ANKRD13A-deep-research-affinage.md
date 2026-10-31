---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD13A
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8IZ07
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 7
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKRD13A (human)

## Current model (mechanistic narrative)

ANKRD13A is a ubiquitin-interacting-motif (UIM) scaffold protein that selectively recognizes Lys-63-linked polyubiquitin chains on diverse membrane and signaling substrates to direct VCP/p97-dependent membrane remodeling and trafficking [PMID:26797118, PMID:40975168]. Through its UIMs it binds ubiquitinated Caveolin-1 and assembles a ternary complex with VCP/p97 on endosomal membranes to route Cav-1 oligomers for lysosomal trafficking [PMID:26797118], and it cooperates with the E3 ligase RNF11 and the ITCH-dependent ubiquitination of ANKRD13A itself to gate binding to activated EGFR and its sorting toward lysosomal degradation [PMID:31985874]. Upon PINK1/Parkin-driven mitochondrial depolarization, ANKRD13A relocates to depolarized mitochondria and recruits VCP/p97 to the outer membrane to promote membrane rupture required for mitophagy [PMID:40975168], and it is similarly recruited to ubiquitinated Toxoplasma parasitophorous vacuoles with VCP/p97 and UBXD1 to drive their acidification and restrict the parasite [PMID:37975677]. Beyond trafficking, ANKRD13A binds ubiquitinated RIP1 within TNF complex-II via its UIM and limits FADD/caspase-8 recruitment, raising the threshold for TNF-induced apoptosis without affecting NF-κB activation [PMID:34839354].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0031386 protein tag activity
- **localization:** GO:0005768 endosome, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-9612973 Autophagy, R-HSA-5357801 Programmed Cell Death
- **partners:** VCP, RNF11, ITCH, EGFR, RIPK1, CAVEOLIN-1, UBXD1
- **complexes:** TNF complex-II

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2016 | High | ANKRD13A (Ankrd13 family) contains ubiquitin-interacting motifs (UIMs) that bind preferentially to Lys-63-linked polyubiquitin chains on Caveolin-1 (Cav-1), forming a ternary complex with VCP/p97 on endosomal membranes to facilitate lysosomal trafficking of ubiquitinated Cav-1 oligomers. | PMID:26797118 | The Journal of biological chemistry |
| 2020 | High | ANKRD13A forms a complex with RNF11 (RING finger protein 11) in vivo via its UIMs, and this interaction is modulated by EGF stimulation. A ternary complex of ANKRD13A, RNF11, and activated EGFR is transiently assembled during early receptor endocytosis. Loss of ITCH E3 ligase abrogates ANKRD13A ubiquitination while loss of RNF11 increases it; the ubiquitination status of ANKRD13A controls its ability to bind activated EGFR, thereby regulating EGFR sorting for lysosomal degradation. | PMID:31985874 | The FEBS journal |
| 2021 | High | ANKRD13A acts as a novel component of TNF signaling complex-II (death-inducing complex). It binds to ubiquitinated RIP1 via its UIM domain and limits the association of FADD and caspase-8 with RIP1, thereby setting a higher threshold for TNF-induced cell death without affecting NF-κB activation. ANKRD13A deficiency shifts the cellular response to TNF from survival to apoptosis. | PMID:34839354 | Cell death and differentiation |
| 2025 | High | ANKRD13A relocates to depolarized mitochondria upon PINK1/Parkin activation and promotes mitophagy by recruiting VCP/p97 to the mitochondrial outer membrane (OMM). VCP and its recruitment factors including ANKRD13A are required for OMM rupture, which exposes inner mitochondrial membrane mitophagy receptors for autophagic recognition. | PMID:40975168 | The Journal of biological chemistry |
| 2023 | Medium | ANKRD13A is recruited to ubiquitinated Toxoplasma gondii parasitophorous vacuoles (PVs) in IFNγ-stimulated endothelial cells together with p97/VCP and UBXD1. PV ubiquitination is a prerequisite for ANKRD13A recruitment, and its deposition directs Tg PVs to acidification, restricting parasite survival. | PMID:37975677 | mSphere |
| 2013 | Medium | Ankrd13A controls focal adhesion formation and distribution in lens and neural crest cells. miR-204 directly targets Ankrd13A; elevated Ankrd13A (from miR-204 inactivation) causes abnormal focal adhesion dynamics, reduced cell motility, and aberrant lens morphogenesis. In vivo restoration of Ankrd13A levels rescued the lens phenotype. | PMID:23620728 | PloS one |
| 2021 | Low | ANKRD13A recognizes Lys-63-linked polyubiquitin chains on HLA class I (HLA-I), and elevated ANKRD13A expression (induced by lncRNA USP30-AS1 via H3K4me3/H3K27Ac chromatin changes) promotes HLA-I internalization from the cell membrane, contributing to immune evasion in AML cells. | PMID:34694569 | Human cell |

## Citations

- PMID:23620728
- PMID:26797118
- PMID:31985874
- PMID:34694569
- PMID:34839354
- PMID:37975677
- PMID:40975168
