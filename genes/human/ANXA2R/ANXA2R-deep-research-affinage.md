---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANXA2R
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q3ZCQ2
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

# Affinage mechanistic annotation for ANXA2R (human)

## Current model (mechanistic narrative)

ANXA2R (AXIIR) is a receptor for Annexin II (ANXA2) that couples extracellular and overexpression signals to opposing apoptotic and pro-survival/proliferative programs depending on cellular context [PMID:23640736, PMID:22223826]. When overexpressed, cytoplasmic ANXA2R binds and activates pro-Caspase-8 independently of FADD, driving downstream Caspase-3/7 activation, Caspase-9 activation, and downregulation of BCL2 and BCL-XL to induce apoptosis [PMID:23640736]; in uveal melanoma cells this apoptotic output is opposed by a protective autophagy flux [PMID:27183438]. In ligand-driven contexts, ANXA2R engages stromal- and osteoblast-derived Annexin II to mediate multiple myeloma cell adhesion and growth via activation of ERK1/2 and AKT signaling [PMID:22223826], and in cervical and endothelial cells ANXA2R sits upstream of PI3K/AKT and ERK1/2 signaling and of MMP2/MMP9 expression to support proliferation, migration, invasion, and angiogenesis [PMID:25633185, PMID:31938090]. As a metabolic receptor, hepatocyte ANXA2R receives muscle (FAP)-secreted ANXA2 to activate SREBP1c-driven de novo lipogenesis and hepatic steatosis [PMID:42225205]. ANXA2R expression is constrained at two levels: its translation is repressed by two cooperating 5'UTR upstream open reading frames acting together with hnRNPA2B1, hnRNPA0, and ELAVL1, which focus ribosomes onto uORF1 and limit leaky scanning [PMID:27789685], and its transcription is silenced by oxidative-stress-induced promoter hypermethylation, which in melanocytes drives apoptosis and impairs keratinocyte SCF secretion [PMID:38806323].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060089 molecular transducer activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005829 cytosol, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-5357801 Programmed Cell Death, R-HSA-162582 Signal Transduction, R-HSA-1430728 Metabolism
- **partners:** ANXA2, CASP8, HNRNPA2B1, HNRNPA0, ELAVL1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | Medium | AXIIR (ANXA2R) overexpression induces apoptosis independent of Annexin II and FADD: AXIIR localizes to the cytoplasm, binds and activates pro-Caspase-8, which subsequently activates Caspase-3/7; AXIIR also downregulates BCL2 and BCL-XL and activates Caspase-9. Inhibition of Caspase-8 partially abolishes AXIIR-induced apoptosis, while BCL-XL overexpression does not. AXIIR translation is tightly inhibited under baseline conditions. | PMID:23640736 | Apoptosis : an international journal on programmed cell death |
| 2012 | Medium | AXIIR (ANXA2R) expressed on multiple myeloma (MM) cells mediates adhesion of MM cells to stromal cells via stromal/osteoblast-derived Annexin II (AXII). OCL-derived AXII enhances MM cell growth through AXIIR. AXII activates ERK1/2 and AKT signaling pathways in MM cells downstream of AXIIR. | PMID:22223826 | Blood |
| 2016 | High | The 5'UTR of ANXA2R mRNA contains two upstream open reading frames (uORFs) that act in a fail-safe manner to inhibit translation from the main AUG. hnRNPA2B1, hnRNPA0, and ELAVL1 bind the 5'UTR of AXIIR mRNA, focus translation onto uORF1, and attenuate leaky scanning that bypasses uORFs, forming a multiple fail-safe translational repression system. | PMID:27789685 | Nucleic acids research |
| 2015 | Medium | AXIIR knockdown in HUVECs inhibits proliferation, adhesion, migration, tube formation in vitro and suppresses angiogenesis in vivo; these effects are mediated at least partly through suppression of MMP2 and MMP9 expression. Knockdown causes S/G2 cell cycle arrest but does not induce apoptosis. | PMID:25633185 | Cellular physiology and biochemistry |
| 2016 | Medium | Overexpression of AXIIR in uveal melanoma (Mum2C) cells reduces cell viability and activates apoptosis, while simultaneously inducing autophagy and increasing autophagy flux. Inhibition of autophagy with chloroquine enhances AXIIR-overexpression-induced apoptosis, indicating that autophagy acts as a protective mechanism counteracting AXIIR-induced apoptosis. | PMID:27183438 | Cancer biotherapy & radiopharmaceuticals |
| 2018 | Medium | AXIIR knockdown in HeLa cervical cancer cells inhibits proliferation, migration, and invasion, and induces apoptosis via increased Caspase-3/-8/-9 expression; knockdown also decreases MMP-2/-9 expression and downregulates Akt, p-Akt, ERK1/2, and p-ERK1/2, placing AXIIR upstream of PI3K/Akt and ERK1/2 signaling in cervical cancer cells. | PMID:31938090 | International journal of clinical and experimental pathology |
| 2024 | Medium | ANXA2R is hypermethylated under oxidative stress in vitiligo lesions, leading to its downregulation. Reduced ANXA2R expression induces melanocyte apoptosis and inhibits secretion of stem cell factor (SCF) from keratinocytes, impairing melanocyte survival. | PMID:38806323 | Journal of dermatological science |
| 2026 | High | Muscle-derived ANXA2 (secreted by fibroadipogenic progenitors, FAPs) acts on hepatocyte-expressed ANXA2R to promote de novo lipogenesis through activation of the SREBP1c signaling pathway, driving hepatic steatosis. FAP-specific ANXA2 knockout alleviated hepatic steatosis and systemic metabolic disturbances in vivo. | PMID:42225205 | Metabolism: clinical and experimental |

## Citations

- PMID:22223826
- PMID:23640736
- PMID:25633185
- PMID:27183438
- PMID:27789685
- PMID:31938090
- PMID:38806323
- PMID:42225205
