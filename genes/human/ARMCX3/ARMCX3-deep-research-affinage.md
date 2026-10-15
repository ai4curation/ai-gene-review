---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARMCX3
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9UH62
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 10
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARMCX3 (human)

## Current model (mechanistic narrative)

ARMCX3 (Alex3) is an integral membrane protein of the mitochondrial outer membrane that controls mitochondrial dynamics and trafficking, particularly in neurons [PMID:22569362, PMID:19304657]. It assembles into the Kinesin/Miro1/Trak2 motor adaptor complex in a Ca2+-dependent manner, positioning it as a regulator of mitochondrial movement [PMID:22569362], and it further recruits Gαq into this complex to transduce GPCR signals onto the transport machinery independently of the canonical PLCβ pathway; CNS-specific loss of ARMCX3 abolishes Gαq-mediated control of mitochondrial trafficking and dendritic growth and causes ER stress, neuronal and motor neuron death, and severe motor deficits [PMID:38320000]. ARMCX3 protein stability is regulated by the non-canonical Wnt/PKC pathway, which drives its degradation and thereby modulates mitochondrial morphology [PMID:23844091]. Beyond its trafficking role, ARMCX3 interacts with the transcription factors Sox10 and SOX9: it binds Sox10 at the outer mitochondrial membrane and potentiates Sox10-dependent transactivation without intrinsic transcriptional activity [PMID:19304657], and its interaction with SOX9 drives hepatic cell proliferation, with ARMCX3 knockout protecting mice against high-fat-diet-induced NAFLD and chemically induced hepatocarcinogenesis [PMID:33807672]. ARMCX3 also acts as a negative regulator of white adipose tissue browning and mitochondrial oxidative activity, with its expression repressed by thermogenic stimulation and induced by obesity [PMID:35705702].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-9609507 Protein localization
- **partners:** MIRO1, TRAK2, GNAQ, SOX10, SOX9
- **complexes:** Miro1/Trak2/Kinesin motor adaptor complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2012 | High | ARMCX3 (Alex3) localizes to mitochondria and regulates mitochondrial dynamics and trafficking in neurons. Alex3 physically interacts with the Kinesin/Miro/Trak2 complex in a Ca2+-dependent manner, placing it in the motor adaptor complex that controls mitochondrial movement. | PMID:22569362 | Nature Communications |
| 2009 | Medium | ARMCX3 is an integral membrane protein of the mitochondrial outer membrane that physically interacts with the transcription factor Sox10. In the cytoplasm, Sox10 is peripherally associated with the mitochondrial outer membrane, and overexpression of ARMCX3 increases the amount of mitochondrially associated Sox10. ARMCX3 lacks intrinsic transcriptional activity but enhances Sox10-mediated transactivation of the nicotinic acetylcholine receptor alpha3 and beta4 subunit gene promoters. | PMID:19304657 | The Journal of Biological Chemistry |
| 2013 | Medium | The non-canonical Wnt/PKC pathway regulates mitochondrial dynamics by inducing degradation of Alex3 (ARMCX3). Wnt treatment attenuates Alex3-induced mitochondrial aggregation by reducing Alex3 protein levels; the canonical Wnt pathway does not affect this, but the Wnt/PKC non-canonical pathway controls both mitochondrial aggregation and Alex3 protein stability. | PMID:23844091 | PLoS ONE |
| 2016 | Medium | In chick spinal cord, ARMCX3 overexpression regulates neural progenitor proliferation and neural maturation, and these phenotypic effects require its mitochondrial localization. ARMCX3 acts as an inhibitor of Wnt-β-catenin signaling in neural development. | PMID:26973462 | Frontiers in Cellular Neuroscience |
| 2017 | Low | ARMCX3 (Alex3) overexpression in non-small cell lung cancer cells suppresses invasion and migration by downregulating phospho-AKT and Slug and upregulating E-cadherin, placing ARMCX3 upstream of the AKT/Slug/E-cadherin axis. | PMID:28705116 | Tumour Biology |
| 2021 | High | ARMCX3 mediates hepatic tumorigenesis under dietary lipotoxicity. ARMCX3 knockout in mice protected against high-fat-diet-induced NAFLD and chemically induced hepatocarcinogenesis, promoting apoptosis and macrophage infiltration. SOX9 was identified as a mediator of ARMCX3 effects in hepatic cells, with the SOX9–ARMCX3 interaction required for ARMCX3-driven hepatic cell proliferation. | PMID:33807672 | Cancers |
| 2022 | Medium | ARMCX3 is a negative regulator of white adipose tissue browning. Armcx3-KO mice show induced WAT browning, and adenoviral overexpression of ARMCX3 in differentiating brown adipocytes downregulates thermogenesis-related genes and reduces mitochondrial oxidative activity. Armcx3 expression is repressed by cold or β3-adrenergic thermogenic stimulation and upregulated by obesity. | PMID:35705702 | International Journal of Obesity |
| 2024 | High | ARMCX3 (Alex3) forms a mammalian-specific mitochondrial complex with Gαq and the Miro1/Trak2 adaptor complex. Gαq activation inhibits mitochondrial trafficking in neurons independently of the canonical PLCβ pathway. CNS-specific Alex3 knockout mice showed that Alex3 is required for Gαq-mediated effects on mitochondrial trafficking and dendritic growth. Alex3-deficient mice had elevated ER stress response proteins, increased neuronal death, motor neuron loss, and severe motor deficits. | PMID:38320000 | Science Signaling |
| 2024 | Low | A regulatory axis involving Prx II, the transcription factor ATF3, and miR-181b-5p collectively modulates Armcx3 expression, which is implicated in mitochondrial transport. Prx II deficiency reduces Armcx3 levels via this pathway in neuronal (HT22) cells. | PMID:38637880 | Cell Communication and Signaling |
| 2024 | Low | ARMCX3 knockdown in dental pulp stem cells (hDPSCs) accelerates neural differentiation and reduces inflammatory cytokine levels under LPS-induced inflammation. ARMCX3 overexpression increases ROS production, and ROS inhibition reverses the effects of ARMCX3 overexpression, indicating ARMCX3 regulates neural differentiation and inflammation at least partly through ROS signaling. | PMID:39296219 | Heliyon |

## Citations

- PMID:19304657
- PMID:22569362
- PMID:23844091
- PMID:26973462
- PMID:28705116
- PMID:33807672
- PMID:35705702
- PMID:38320000
- PMID:38637880
- PMID:39296219
