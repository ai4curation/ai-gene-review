---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB3
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9Y575
self_evaluation_pairwise: win
faith_pct: 83.33333333333333
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

# Affinage mechanistic annotation for ASB3 (human)

## Current model (mechanistic narrative)

ASB3 is a substrate-recognition adaptor for a Cullin-based E3 ubiquitin ligase that drives K48-linked polyubiquitination and proteasomal degradation of multiple signaling receptors and effectors, positioning it as a negative regulator of inflammatory, antiviral, and apoptotic pathways [PMID:15899873, PMID:39162488, PMID:39266719, PMID:38334450]. It engages substrates through its N-terminal ankyrin repeats and couples them to the Elongin-B/C complex via its C-terminal SOCS box [PMID:15899873]. Through this mechanism ASB3 targets TNF-R2 to limit TNF-R2-mediated JNK activation [PMID:15899873], degrades TRAF6 in intestinal epithelial cells to restrain NF-κB-driven proinflammatory cytokine production—with ASB3-knockout mice resistant to DSS-induced colitis [PMID:39162488]—and ubiquitinates MAVS at lysine 297 to suppress TBK1/IRF3 phosphorylation and type I interferon responses, thereby increasing influenza susceptibility [PMID:39266719]. ASB3 also promotes degradation of death receptor 5 (DR5), and its loss sensitizes hepatocellular carcinoma cells to TRAIL-induced apoptosis while suppressing chemically induced liver carcinogenesis in vivo [PMID:38334450]. In cancer, ASB3 acts as a tumor suppressor: it inhibits epithelial-mesenchymal transition and colorectal proliferation, migration, and metastasis [PMID:28088228], and its depletion triggers a caspase-8/Beclin1 axis that promotes mitochondrial apoptosis [PMID:31016535]. Despite predominant testis expression, ASB3 is dispensable for mouse spermatogenesis and fertility [PMID:40755808].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-168256 Immune System, R-HSA-392499 Metabolism of proteins, R-HSA-5357801 Programmed Cell Death, R-HSA-162582 Signal Transduction
- **partners:** TNFRSF1B, TRAF6, MAVS, TNFRSF10B, ELOB, ELOC
- **complexes:** Elongin-B/C

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2005 | High | ASB3 binds TNF-R2 via its ankyrin repeats (interacting with the C-terminal 37 amino acids of TNF-R2) and recruits Elongin-B/C via its SOCS box, acting as an E3 ubiquitin ligase adaptor that promotes K48-linked polyubiquitination of TNF-R2 on multiple lysine residues within its C-terminal region, leading to proteasome-mediated degradation of TNF-R2 and inhibition of TNF-R2-mediated JNK activation. | PMID:15899873 | Molecular and cellular biology |
| 2000 | Low | ASB3 contains N-terminal ankyrin repeats and a C-terminal SOCS box that couples ASB3 and its binding partners to the Elongin-B/C complex, potentially targeting them for degradation. | PMID:11111040 | Gene |
| 2017 | Medium | ASB3 knockdown promotes colorectal cancer cell proliferation, migration, and invasion in vitro and tumorigenicity and hepatic metastasis in vivo; overexpression of wild-type ASB3 (but not clinical missense mutants) inhibits these phenotypes; ASB3 inhibits epithelial-mesenchymal transition as evidenced by up-regulation of β-catenin and E-cadherin and down-regulation of TCF8, N-cadherin, and vimentin. | PMID:28088228 | Chinese journal of cancer |
| 2019 | Medium | ASB3 knockdown in hepatocellular carcinoma cells enhances mitochondrial apoptosis via activation of caspase-8, which cleaves Beclin1; the C-terminal fragment of cleaved Beclin1 localizes to mitochondria and initiates mitochondrial apoptosis; autophagy activation downstream of ASB3 depletion contributes to caspase-8 activation in this pathway. | PMID:31016535 | Science China. Life sciences |
| 2024 | High | ASB3 catalyzes K48-linked polyubiquitination of TRAF6 in intestinal epithelial cells, leading to TRAF6 degradation; loss of ASB3 stabilizes TRAF6 protein, decelerates NF-κB activation (reduced IκBα phosphorylation), and reduces production of proinflammatory cytokines IL-1β, IL-6, and TNF-α; ASB3 knockout mice are resistant to DSS-induced colitis. | PMID:39162488 | mBio |
| 2024 | High | ASB3 interacts with MAVS and directly mediates K48-linked polyubiquitination and proteasomal degradation of MAVS at lysine 297, thereby inhibiting phosphorylation of TBK1 and IRF3, suppressing downstream IFN-β and interferon-stimulated gene (ISG) transcription, and increasing susceptibility to influenza virus infection; ASB3 expression is upregulated by RNA virus infection. | PMID:39266719 | Cell death and differentiation |
| 2024 | High | ASB3 interacts with death receptor 5 (DR5) and promotes its K48-linked ubiquitination and proteasomal degradation; ASB3 knockdown stabilizes DR5 and sensitizes hepatocellular carcinoma cells to TRAIL-induced apoptosis in a DR5-dependent manner; liver-specific Asb3 deletion suppresses DEN-induced liver cancer development in mice. | PMID:38334450 | FASEB journal |
| 2025 | Medium | ASB3 is predominantly expressed in mouse testis and localizes to elongated spermatids; however, Asb3 knockout mice (generated by CRISPR-Cas9) show no detectable defect in spermatogenesis, sperm quantity, sperm motility, or male fertility, indicating ASB3 is dispensable for these processes in mice. | PMID:40755808 | PeerJ |

## Citations

- PMID:11111040
- PMID:15899873
- PMID:28088228
- PMID:31016535
- PMID:38334450
- PMID:39162488
- PMID:39266719
- PMID:40755808
