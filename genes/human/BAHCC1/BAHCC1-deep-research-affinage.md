---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/BAHCC1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9P281
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 10
citation_count: 8
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for BAHCC1 (human)

## Current model (mechanistic narrative)

BAHCC1 is a dual histone-reader chromatin regulator that couples recognition of repressive and replication-associated histone marks to control gene silencing, DNA replication, and cell fate [PMID:33139953, PMID:40592879]. Its BAH module directly engages H3K27me3 through a hydrophobic trimethyl-lysine-binding cage, co-localizing BAHCC1 with Polycomb-marked genes and, together with associated transcriptional corepressors, enforcing their silencing [PMID:33139953]. A separate tandem Tudor domain selectively reads H4K20me1 and recruits both BAHCC1 and the MCM complex to replication origins, promoting origin activation and cell-cycle progression [PMID:40592879]. In mice, a germline point mutation abolishing BAH–H3K27me3 engagement causes partial postnatal lethality, establishing the physiological importance of this reading activity [PMID:33139953]. BAHCC1 acts as an oncogenic effector in acute leukemia, where it is transcriptionally induced by MLL-ENL and sustains leukemic immortalization in part by repressing the H3K27me3-marked cell-cycle inhibitor Cdkn1c [PMID:33139953, PMID:38452334], and in melanoma, where it associates with BRG1-containing remodeling complexes at E2F/KLF-dependent cell-cycle and DNA-repair gene promoters [PMID:37924516]. It is also required for early neuronal commitment and chromatin accessibility during differentiation [PMID:32969152].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0042393 histone binding, GO:0140110 transcription regulator activity, GO:0003677 DNA binding
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-4839726 Chromatin organization, R-HSA-69306 DNA Replication, R-HSA-74160 Gene expression (Transcription), R-HSA-1643685 Disease
- **partners:** MCM, BRG1, TMEM97
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2020 | High | The BAH module of BAHCC1 (BAHCC1BAH) directly recognizes and binds H3K27me3 through a hydrophobic trimethyl-L-lysine-binding 'cage', mediating co-localization of BAHCC1 with H3K27me3-marked genes and enforcing transcriptional silencing of those genes in mammalian cells. | PMID:33139953 | Nature genetics |
| 2020 | High | BAHCC1 interacts with transcriptional corepressors, and in acute leukemia cells its depletion or disruption of the BAHCC1BAH–H3K27me3 interaction causes derepression of H3K27me3-targeted tumor suppressor and differentiation genes, suppressing oncogenesis. | PMID:33139953 | Nature genetics |
| 2020 | High | Germline mutation in mice disrupting Bahcc1's H3K27me3 engagement causes partial postnatal lethality, establishing a role for BAHCC1 BAH–H3K27me3 reading in developmental viability. | PMID:33139953 | Nature genetics |
| 2025 | High | An evolutionarily conserved tandem Tudor domain (TTD) in BAHCC1 selectively reads H4K20me1, promotes recruitment of BAHCC1 and the MCM (Mini-chromosome Maintenance) complex to replication origin sites, and facilitates replication origin activation and DNA replication. Depletion of BAHCC1 or disruption of the BAHCC1TTD–H4K20me1 interaction reduces H4K20me1 levels and MCM loading, causing defects in replication origin activation and cell cycle progression. | PMID:40592879 | Nature communications |
| 2024 | Medium | MLL-ENL upregulates Bahcc1 by binding to its promoter, and Bahcc1 in turn mediates MLL-ENL-driven leukemic immortalization at least partly through repression of the H3K27me3-marked cell cycle inhibitor Cdkn1c. Depletion of Bahcc1 suppresses MLL-ENL leukemogenic activity in bone marrow transplantation models. | PMID:38452334 | Blood advances |
| 2024 | Medium | TMEM97 positively regulates BAHCC1 expression in retinal pigment epithelium (RPE) cells, and BAHCC1 in turn promotes pro-inflammatory cytokine expression (IL1β, CCL2) via NFκB (p50, p52, p65). Co-immunoprecipitation demonstrated a physical association between TMEM97 and BAHCC1 proteins. | PMID:38290642 | Cellular signalling |
| 2023 | Medium | In melanoma cells, BAHCC1 associates with BRG1-containing chromatin remodeling complexes at the promoters of E2F/KLF-dependent cell-cycle and DNA-repair genes, regulating their expression. BAHCC1 silencing leads to decreased cell proliferation and delayed DNA repair, and BAHCC1 deficiency cooperates with PARP inhibition to induce melanoma cell death. | PMID:37924516 | Cell reports |
| 2020 | Medium | Loss of Bahcc1 in mouse embryonic stem cells leads to early arrest in neuronal commitment, failure to induce a neuronal gene expression program, and global reduction in chromatin accessibility at regions marked by H3K4me3 at the onset of differentiation. The Reno1 lncRNA locus forms increasing spatial contacts with Bahcc1 during neurogenesis, forming a regulatory circuit required for neuronal commitment. | PMID:32969152 | EMBO reports |
| 2006 | Medium | Targeted disruption of the mouse homolog of KIAA1447 (Bahcc1) causes hind leg motor dysfunction, establishing a developmental role for Bahcc1 in motor function in vivo. | PMID:16807365 | FASEB journal |
| 2013 | Low | Computational/structural analysis identified a hidden tandem Tudor domain within human BAHCC1, predicting a histone-reading function consistent with the protein's chromatin association. | PMID:23677940 | Bioinformatics |

## Citations

- PMID:16807365
- PMID:23677940
- PMID:32969152
- PMID:33139953
- PMID:37924516
- PMID:38290642
- PMID:38452334
- PMID:40592879
