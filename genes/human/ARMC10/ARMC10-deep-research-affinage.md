---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARMC10
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8N2F6
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 8
citation_count: 8
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARMC10 (human)

## Current model (mechanistic narrative)

ARMC10 (SVH) is an armadillo-repeat protein that governs mitochondrial dynamics and trafficking and serves as a signaling node linking mitochondrial state to cell growth and neuronal repair [PMID:30631047, PMID:24722288]. It acts as a direct substrate of AMPK, which phosphorylates ARMC10 at serine 45; ARMC10 is required downstream of AMPK to drive mitochondrial fission, and its loss prevents AMPK-mediated fission [PMID:30631047]. At mitochondria it associates with the KIF5/Miro1-2/Trak2 trafficking machinery to control the proportion of motile mitochondria in neurons, and its overexpression protects neurons from Aβ-induced mitochondrial fission and death [PMID:24722288]. Independently, ARMC10 functions as a high-affinity cell-surface receptor for the myeloid-derived growth factor oncomodulin, transducing a pro-regenerative signal required for inflammation-induced optic nerve, peripheral sensory, and spinal cord axon regeneration in vivo [PMID:37556559]. An ER-localized splice variant, SVH-B, binds p53 directly and suppresses its transcriptional activity, providing a route by which ARMC10 promotes cell growth and tumorigenicity [PMID:12839973, PMID:17904127]. ARMC10 has additionally been linked to Wnt/β-catenin-dependent regulation of neural progenitor proliferation and mitochondrial protection [PMID:26973462, PMID:38924214].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0048018 receptor ligand activity, GO:0001618 virus receptor activity
- **localization:** GO:0005739 mitochondrion, GO:0005783 endoplasmic reticulum, GO:0005886 plasma membrane
- **pathway (Reactome):** *(none)*
- **partners:** PRKAA1, PRKAA2, KIF5, RHOT1, RHOT2, TRAK2, TP53, OCM
- **complexes:** KIF5/Miro1-2/Trak2 mitochondrial trafficking complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2019 | High | ARMC10 is a direct substrate of AMPK; AMPK phosphorylates ARMC10 at serine 45 (S45) both in vitro and in vivo. ARMC10 overexpression promotes mitochondrial fission, and ARMC10 knockout prevents AMPK-mediated mitochondrial fission, placing ARMC10 downstream of AMPK in the regulation of mitochondrial dynamics. | PMID:30631047 | Nature Communications |
| 2014 | Medium | ARMC10 protein localizes to mitochondria and regulates mitochondrial trafficking in neurons by controlling the number of moving mitochondria (but not mitochondrial aggregation). ARMC10 interacts with the KIF5/Miro1-2/Trak2 mitochondrial trafficking complex. Overexpression of ARMC10 in neurons prevents Aβ-induced mitochondrial fission and neuronal death. | PMID:24722288 | Cell Death & Disease |
| 2023 | High | ArmC10 (ARMC10) functions as a high-affinity cell-surface receptor for the myeloid-derived growth factor oncomodulin (Ocm). ArmC10 deletion suppressed inflammation-induced optic nerve regeneration, the conditioning lesion effect in sensory neurons, and spinal cord axon regeneration. Ocm acting through ArmC10 accelerated optic and peripheral nerve regeneration and enabled spinal cord axon regeneration in mouse models. | PMID:37556559 | Science Translational Medicine |
| 2003 | Medium | Four alternative splicing variants of SVH (ARMC10) — SVH-A, -B, -C, -D — all localize to the endoplasmic reticulum. SVH-B overexpression in liver cells promotes accelerated growth and tumorigenicity, while antisense inhibition of SVH-B induces apoptosis. | PMID:12839973 | Cancer Research |
| 2007 | Medium | SVH-B (ARMC10 splice variant) directly interacts with p53 and suppresses p53 transcriptional activity. Suppression of SVH by RNAi increases p53 transcriptional activity. | PMID:17904127 | FEBS Letters |
| 2016 | Medium | Armc10/SVH knockdown in chick spinal cord reduces proliferation of neural precursor cells (NPCs). Armc10 overexpression inhibits Wnt/β-catenin signaling and regulates progenitor proliferation. These phenotypes require mitochondrial localization of the related Armcx3 protein, suggesting a link between mitochondrial dynamics and neural development. | PMID:26973462 | Frontiers in Cellular Neuroscience |
| 2024 | Medium | ARMC10 regulates mitochondrial dynamics and protects mitochondrial function through activation of the Wnt/β-catenin signalling pathway in an ischemic stroke (OGD/R) cell model. ARMC10 knockdown and overexpression alter expression of mitochondrial dynamics genes (Drp1, Mfn1, Mfn2, Fis1, OPA1), affect mitochondrial ROS, ATP production, and neuronal apoptosis via Wnt/β-catenin. | PMID:38924214 | Journal of Cellular and Molecular Medicine |
| 2025 | Low | ARMC10 knockdown in glioblastoma cells reduces cell proliferation, invasion, migration, lipid levels, and inhibits Notch pathway and fatty acid metabolism protein expression. Notch1 overexpression reverses the inhibitory effects of ARMC10 knockdown, placing ARMC10 upstream of Notch1 in GBM. | PMID:39987562 | Molecular Carcinogenesis |

## Citations

- PMID:12839973
- PMID:17904127
- PMID:24722288
- PMID:26973462
- PMID:30631047
- PMID:37556559
- PMID:38924214
- PMID:39987562
