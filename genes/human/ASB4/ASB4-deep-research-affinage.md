---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB4
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9Y574
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

# Affinage mechanistic annotation for ASB4 (human)

## Current model (mechanistic narrative)

ASB4 is the substrate-recognition subunit of an elongin B/elongin C/cullin/Roc E3 ubiquitin ligase complex that targets specific proteins for ubiquitination and proteasomal degradation, coupling oxygen sensing and metabolic signaling to differentiation and energy homeostasis [PMID:17636018, PMID:11111040]. Its ligase activity is regulated by oxygen tension: FIH hydroxylates an asparagine residue in ASB4 in normoxia, an oxygen-dependent modification linked to substrate binding and degradation [PMID:17636018]. Through its SOCS box, ASB4 ubiquitinates and degrades the transcriptional regulator ID2 in trophoblasts, driving trophoblast differentiation and placental vascular patterning, and a degradation-resistant ID2 mutant blocks both responses [PMID:24586788]; loss of ASB4 allows insulin to elevate ID2 post-transcriptionally, linking the pathway to preeclampsia pathology [PMID:36768469]. In hypothalamic POMC and NPY neurons, ASB4 binds and ubiquitinates IRS4 in a SOCS box-dependent manner to dampen insulin/AKT signaling [PMID:21955513], and acts downstream of AgRP to regulate satiety—being suppressed by fasting, required for calcitonin-induced meal termination via Calcr expression, and controlling glucose homeostasis in POMC neurons [PMID:35536884]. Separately, ASB4 engages GPS1/CSN1 through its ankyrin-repeat domain, independent of the SOCS box, to suppress JNK activity and reduce IRS-1 serine phosphorylation [PMID:17276034].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016874 ligase activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology
- **partners:** FIH, ID2, IRS4, GPS1
- **complexes:** elongin B/elongin C/cullin/Roc E3 ubiquitin ligase

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2007 | Medium | ASB4 is a substrate for FIH (factor inhibiting HIF1α)-mediated asparagine hydroxylation via an oxygen-dependent mechanism; ASB4 interacts with FIH and is hydroxylated by FIH in normoxia, which is postulated to promote substrate binding and degradation. | PMID:17636018 | Molecular and cellular biology |
| 2007 | Medium | ASB4 functions as the substrate recognition subunit of an elongin B/elongin C/cullin/Roc E3 ubiquitin ligase complex, mediating ubiquitination and proteasomal degradation of substrate proteins; overexpression of ASB4 in embryonic stem cells promotes differentiation into the vascular lineage. | PMID:17636018, PMID:11111040 | Molecular and cellular biology |
| 2014 | High | ASB4 ubiquitinates and promotes proteasome-dependent degradation of the transcriptional regulator ID2 in trophoblast cells, thereby promoting trophoblast differentiation and vascular patterning in the placenta; co-transfection of a degradation-resistant ID2 mutant with ASB4 inhibits both differentiation and functional vascular responses. | PMID:24586788 | PloS one |
| 2007 | Medium | ASB4 (Asb-4) interacts with GPS1 (CSN1) via its ankyrin repeat domain (independent of the SOCS box) and reduces GPS1 protein levels; co-expression of ASB4 with GPS1 inhibits c-Jun NH2-terminal kinase (JNK) activity and reduces insulin-stimulated IRS-1 serine 307 phosphorylation. | PMID:17276034 | Cellular signalling |
| 2011 | High | ASB4 co-localizes with IRS4 in hypothalamic POMC and NPY neurons, physically interacts with IRS4 (confirmed by Co-IP in cell lines and rat hypothalamic extracts), ubiquitinates IRS4 in a SOCS box-dependent manner, promotes IRS4 proteasomal degradation, and reduces both basal and insulin-stimulated AKT (Thr308) phosphorylation. | PMID:21955513 | BMC neuroscience |
| 2009 | Medium | Overexpression of ASB4 specifically in POMC neurons of the arcuate nucleus increases food intake, reduces fat mass, increases lean mass, raises metabolic rate (O2 consumption and CO2 production), increases locomotor activity, and elevates POMC mRNA; ASB4 expression in the hypothalamus is regulated by insulin (paraventricular nucleus) and leptin (paraventricular nucleus and arcuate nucleus). | PMID:19934378 | Endocrinology |
| 2022 | High | ASB4 acts downstream of AgRP in the hypothalamus to regulate satiety and glucose homeostasis: hypothalamic Asb4 expression is suppressed by fasting in an AgRP-dependent manner; acute Asb4 knockdown causes hyperphagia via increased meal size; Asb4-deficient mice are resistant to calcitonin-induced meal termination and show reduced Calcr (calcitonin receptor) expression in neurons; POMC neuron-specific Asb4 deletion causes glucose intolerance independent of obesity. | PMID:35536884 | Science signaling |
| 2023 | Medium | In the absence of ASB4, insulin (but not leptin) elevates ID2 protein levels post-transcriptionally in trophoblasts, implicating hyperinsulinemia in perturbing ASB4-mediated ID2 degradation and contributing to enhanced preeclampsia pathology. | PMID:36768469 | International journal of molecular sciences |
| 2002 | Medium | Asb4 is an imprinted gene showing differential expression between parthenogenetic and androgenetic mouse embryos, confirmed in normal diploid embryos from reciprocal F1 crosses. | PMID:11820791 | Biochemical and biophysical research communications |
| 2014 | Medium | ASB4 expression promotes migration and invasion of hepatocellular carcinoma (HCC) cells; suppression of ASB4 in HCC cell lines (PLC, MHCC97-L) reduces migration and invasion, while ectopic ASB4 expression in Hep3B cells enhances migration; ASB4 mRNA levels are negatively regulated by miR-200a through a validated binding site in the ASB4 3' UTR. | PMID:24815387 | Bioscience trends |

## Citations

- PMID:11111040
- PMID:11820791
- PMID:17276034
- PMID:17636018
- PMID:19934378
- PMID:21955513
- PMID:24586788
- PMID:24815387
- PMID:35536884
- PMID:36768469
