---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD49
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8WVL7
self_evaluation_pairwise: win
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

# Affinage mechanistic annotation for ANKRD49 (human)

## Current model (mechanistic narrative)

ANKRD49 is a predominantly nuclear ankyrin-repeat protein that promotes cell survival and tumor cell invasion across germ-cell and lung cancer contexts [PMID:26043108, PMID:37964204]. In male germ cells it acts through the NF-κB (p65) pathway, where it augments starvation-induced autophagy and, by modulating nuclear translocation of p65, inhibits etoposide-induced intrinsic mitochondrial apoptosis involving caspase-9 and Bcl-2 family proteins [PMID:26043108, PMID:30798416]. In non-small-cell lung cancer ANKRD49 drives MMP-2/9–dependent invasion and metastasis through MAPK signaling that is wired differently across cell lines: a P38–ATF-2 axis in A549 adenocarcinoma cells [PMID:35775112], and a JNK–c-Jun/ATF2 axis in H1299 and H1703 cells, where ANKRD49 elevates JNK phosphorylation and the resulting c-Jun:ATF2 heterodimer binds the MMP-2 and MMP-9 promoters to drive their transcription [PMID:37964204]. ANKRD49 additionally promotes epithelial-mesenchymal transition by physically interacting with PKNOX1, which transcriptionally activates TGF-β1 to engage SMAD signaling, upregulating α-SMA while suppressing E-cadherin [PMID:41821002]. The biochemical activity of the ankyrin repeats themselves and a unifying upstream signal connecting these branches have not been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140110 transcription regulator activity
- **localization:** GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-9612973 Autophagy, R-HSA-5357801 Programmed Cell Death, R-HSA-162582 Signal Transduction, R-HSA-1643685 Disease
- **partners:** PKNOX1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2015 | Medium | ANKRD49 resides primarily in the nucleus of spermatogonia, spermatocytes, and round spermatids. Overexpression of ANKRD49 augments starvation-induced autophagy in male germ GC-1 cells, while shRNA knockdown attenuates autophagy. Inhibition of NF-κB pathway (by inhibitors or p65 siRNA) prevents ANKRD49-dependent autophagy augmentation, demonstrating that ANKRD49 enhances autophagy via the NF-κB pathway. | PMID:26043108 | PloS one |
| 2019 | Medium | ANKRD49 inhibits etoposide-induced intrinsic (mitochondrial) apoptosis in GC-1 cells. Overexpression of ANKRD49 attenuates etoposide-induced apoptosis while knockdown promotes it. The effect involves the intrinsic pathway (caspase 9, Bcl-2 family proteins). Mechanistically, ANKRD49 modulates nuclear translocation of NF-κB p65, and blocking NF-κB (inhibitor or p65 siRNA) abolishes the anti-apoptotic effect of ANKRD49. | PMID:30798416 | Molecular and cellular biochemistry |
| 2022 | Medium | ANKRD49 promotes invasion and migration of lung adenocarcinoma A549 cells in vitro and in vivo by upregulating MMP-2 and MMP-9 activities through the P38/ATF-2 signalling pathway. | PMID:35775112 | Journal of cellular and molecular medicine |
| 2023 | High | In NCI-H1299 (LUAD) and NCI-H1703 (LUSC) cells, ANKRD49 promotes invasion and metastasis via a JNK-ATF2/c-Jun-MMP-2/9 axis. ANKRD49 elevates JNK phosphorylation, activating c-Jun and ATF2, which interact in the nucleus to bind the MMP-2 and MMP-9 promoters and drive their transcription. This mechanism is distinct from the P38/ATF-2 pathway previously described in A549 cells. | PMID:37964204 | BMC cancer |
| 2026 | Medium | ANKRD49 physically interacts with PKNOX1 (demonstrated by Co-IP and immunofluorescence co-localization). PKNOX1 binds the TGF-β1 promoter (ChIP and luciferase reporter assay), driving TGF-β1 transcription and subsequent SMAD pathway activation. This ANKRD49–PKNOX1–TGF-β1/SMAD axis promotes epithelial-mesenchymal transition (EMT) in NSCLC cells, upregulating α-SMA and TGF-β1 while suppressing E-cadherin. | PMID:41821002 | Cancer cell international |

## Citations

- PMID:26043108
- PMID:30798416
- PMID:35775112
- PMID:37964204
- PMID:41821002
