---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADISSP
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q9GZN8
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 7
citation_count: 5
gates_passed: False
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADISSP (human)

> ⚠️ **CAUTION — trust gate(s) tripped; review before using:**
>
> - Affinage's own head-to-head self-evaluation scored this record `pairwise = tie` (not `win`) vs the curated UniProt reference — treat the narrative with extra scepticism.

## Current model (mechanistic narrative)

ADISSP (C20orf27) is an adipose-specific secreted signaling protein that functions as an adipokine coupling adrenergic input to thermogenesis and glucose homeostasis [PMID:36496438]. Its expression is enriched in brown adipose tissue and its secretion is stimulated by β3-adrenergic activation [PMID:36496438]; once released, it binds a surface receptor on adipocytes and activates protein kinase A independently of β-adrenergic signaling to drive white adipose tissue browning [PMID:36496438]. Adipose-specific knockout impairs WAT browning and renders mice susceptible to high-fat diet-induced obesity and hyperglycemia, establishing ADISSP as a required upstream regulator of thermogenesis and glucose handling [PMID:36496438]. Recombinant ADISSP additionally activates insulin-independent Akt signaling in white fat to promote glucose disposal and normalize hyperglycemia in type 1 and type 2 diabetic models [PMID:42030391]. In cancer settings, ADISSP interacts with the catalytic subunit of protein phosphatase 1 (PP1c) and promotes colorectal cancer cell proliferation through activation of the TGFβR-TAK1-NFκB cascade [PMID:32024300]. The identity of its adipocyte surface receptor and the molecular route from receptor engagement to PKA and Akt activation have not been characterized in the available corpus.

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0048018 receptor ligand activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1430728 Metabolism
- **partners:** PPP1CA
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2022 | Medium | Adissp (C20orf27/FLJ20550) is an adipose-secreted signaling protein whose expression is adipose-specific and highly enriched in brown adipose tissue (BAT); its secretion is stimulated by β3-adrenergic activation. | PMID:36496438 | Nature Communications |
| 2022 | Medium | Adissp binds to a putative receptor on the adipocyte surface and activates protein kinase A (PKA) independently of β-adrenergic signaling, promoting white adipose tissue (WAT) browning/thermogenesis. | PMID:36496438 | Nature Communications |
| 2022 | High | Adipose-specific Adissp knockout mice are defective in WAT browning and are susceptible to high-fat diet-induced obesity and hyperglycemia, establishing Adissp as a required upstream regulator of thermogenesis and glucose homeostasis. | PMID:36496438 | Nature Communications |
| 2026 | Medium | Recombinant Adissp (rAdissp) protein activates insulin-independent Akt signaling in white fat to stimulate glucose disposal, normalizing hyperglycemia in both type 1 and type 2 diabetic mouse models. | PMID:42030391 | Science Advances |
| 2020 | Medium | C20orf27 (ADISSP) promotes colorectal cancer cell growth and proliferation by interacting with PP1c (the catalytic subunit of type 1 phosphatase) and activating the TGFβR-TAK1-NFκB signaling cascade; NFκB inhibition reverses this effect. | PMID:32024300 | Cancers |
| 2025 | Low | C20orf27 (ADISSP) promotes hepatocellular carcinoma cell proliferation and migration by regulating cyclin-related proteins (MDM2, PCNA, Cyclin E1, CDK2, p-Rb) and acts upstream of NT5E as a downstream target. | PMID:40690096 | Discover Oncology |
| 2025 | Low | C20orf27 (ADISSP) mediates colorectal cancer cell proliferation through XBP1 signaling under normal lipid conditions, but switches to promoting metastasis via MST1 signaling under high-lipid conditions, demonstrating context-dependent pathway utilization. | PMID:40876696 | Cellular Signalling |

## Citations

- PMID:32024300
- PMID:36496438
- PMID:40690096
- PMID:40876696
- PMID:42030391
