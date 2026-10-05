---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AP1S3
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q96PC3
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

# Affinage mechanistic annotation for AP1S3 (human)

## Current model (mechanistic narrative)

AP1S3 encodes σ1C, a sigma subunit of the AP-1 clathrin adaptor complex that governs endosomal membrane trafficking in keratinocytes, where its loss drives cutaneous autoinflammation [PMID:24791904, PMID:27388993]. AP1S3 is required for endosomal translocation of TLR3, and its depletion mislocalizes TLR3 and blunts downstream TLR3 signaling [PMID:24791904]. Independently, AP1S3 loss-of-function disrupts keratinocyte autophagy, causing accumulation of the autophagy adaptor p62, which activates NF-κB and drives overexpression of IL-36α; this cascade is recapitulated by pharmacological autophagy inhibition and reversed by IL-36 blockade in patient keratinocytes, defining the mechanistic route from adaptor dysfunction to autoinflammatory disease [PMID:27388993]. Beyond its keratinocyte role, AP1S3 physically binds the HCV E2 envelope protein and shields it from E6AP-mediated ubiquitin-dependent proteasomal degradation, and a synthetic peptide carrying the AP1S3-recognized motif inhibits HCV infection [PMID:27079945].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005768 endosome
- **pathway (Reactome):** *(none)*
- **partners:** TLR3, HCV E2
- **complexes:** AP-1 adaptor complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2014 | Medium | AP1S3 (encoding AP-1 complex subunit σ1C) is required for endosomal translocation of TLR3 in keratinocytes; AP1S3 knockdown disrupted TLR3 trafficking to endosomes and markedly inhibited downstream TLR3 signaling | PMID:24791904 | American journal of human genetics |
| 2016 | High | AP1S3 loss-of-function disrupts keratinocyte autophagy, causing abnormal accumulation of the autophagy adaptor p62, which in turn activates NF-κB signaling and leads to overexpression of IL-36α; this autoinflammatory cascade was recapitulated by pharmacological autophagy inhibition and reversed by IL-36 blockade in patient keratinocytes | PMID:27388993 | The Journal of investigative dermatology |
| 2016 | Medium | AP1S3 interacts physically with HCV E2 protein (shown by co-immunoprecipitation) and protects E2 from ubiquitin-mediated proteasomal degradation; the E3 ligase E6AP was identified as mediating E2 ubiquitylation; a synthetic peptide containing the AP1S3-recognized motif inhibited HCV infection | PMID:27079945 | Antiviral research |
| 2016 | Low | AP-1/σ1A (AP1S1) and AP-1/σ1B (AP1S2) complexes differentially regulate neuronal early endosome maturation: σ1A binds ArfGAP1 (with higher affinity for brain-specific ArfGAP1), which recruits Rabex-5 to endosomes, enhancing Rab5(GTP)-stimulated Vps34 PI3-kinase activity required for multivesicular body formation; σ1B (AP1S2) binding of Rabex-5 prevents this complex and reduces endosomal Rabex-5. (Note: this paper characterizes σ1A and σ1B isoforms but not σ1C/AP1S3 directly.) | PMID:27411398 | Scientific reports |
| 2025 | Low | AP1S3 knockdown in breast cancer cells (MDA-MB-231 and MDA-MB-436) inhibited proliferation and migration; mechanistically, AP1S3 activates the PI3K/AKT/mTOR pathway to facilitate lipid metabolism, and its silencing reduced lipid droplet accumulation, free fatty acid levels, total cholesterol, and downregulated lipid metabolism-related genes | PMID:40555003 | Biochemical and biophysical research communications |
| 2008 | Low | Sigma subunits (σ1A, σ1B, σ1C) are essential for stability of human AP-1 complexes, demonstrated using the AP-2 complex as a model; however, no major alteration of stability, subcellular localization, or function of the AP-1 complex was observed in fibroblasts from a patient carrying an AP1S2 mutation, suggesting functional redundancy among AP-1 sigma subunit isoforms (σ1A/AP1S1, σ1B/AP1S2, σ1C/AP1S3) in peripheral tissues | PMID:18428203 | Human mutation |

## Citations

- PMID:18428203
- PMID:24791904
- PMID:27079945
- PMID:27388993
- PMID:27411398
- PMID:40555003
