---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARMCX1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9P291
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 12
citation_count: 12
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARMCX1 (human)

## Current model (mechanistic narrative)

ARMCX1 (ALEX1) is a mammalian-specific armadillo repeat protein with two functional dimensions: regulation of mitochondrial dynamics in neurons and tumor suppression in epithelial cancers [PMID:28009275, PMID:11162520]. In adult neurons it localizes to mitochondria and enhances mitochondrial transport, and this localization is required for its pro-survival and pro-regenerative effects following axonal injury [PMID:28009275]; after traumatic brain injury it preserves mitochondrial function, neuronal viability, and axonal integrity through a Miro1-dependent transport pathway, and its protein levels are suppressed post-injury by miR-223-3p [PMID:37454781, PMID:38492796]. As a tumor suppressor, ARMCX1 acts as a substrate-recruiting adaptor for the ubiquitin-proteasome system, bridging the E3 ligase FBXW7 to drive degradation of c-Myc and the E3 ligase TRIM21 to drive degradation of β-catenin, thereby inactivating cell-cycle and EMT programs [PMID:39285446, PMID:41533266]; it additionally restrains tumor-cell behavior by suppressing thrombin/PAR-1-induced RhoA/Rac1 activation and by acting upstream of JAK1/STAT3 signaling [PMID:28315004, PMID:30907988]. Its expression is activated transcriptionally by CREB and Wnt/β-catenin signaling via a promoter CRE element, and it is frequently silenced by promoter hypermethylation across carcinomas [PMID:20398052, PMID:22494058]. Conditional knockout indicates ARMCX1 is dispensable for baseline retinal and optic nerve homeostasis, consistent with an injury- and stress-responsive role [PMID:39139090].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-162582 Signal Transduction
- **partners:** FBXW7, TRIM21, MIRO1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2016 | High | Armcx1 is a mammalian-specific, mitochondria-localized protein that enhances mitochondrial transport in adult retinal ganglion cells (RGCs); its pro-survival and pro-regeneration effects after axotomy depend on its mitochondrial localization, as shown by overexpression and knockdown experiments in a mouse optic nerve injury model. | PMID:28009275 | Neuron |
| 2001 | Medium | ALEX1/ARMCX1 encodes a novel human armadillo repeat protein (453 amino acids) with two ARM repeats, localizes to chromosome Xq21.33-q22.2, and shows homology to ALEX2 and ALEX3; its mRNA expression is lost or significantly reduced in lung, prostate, colon, pancreas, and ovarian carcinomas compared to normal tissues. | PMID:11162520 | Biochemical and biophysical research communications |
| 2010 | Medium | ALEX1/ARMCX1 transcription is regulated by a cyclic AMP response element (CRE) and an E-box in its promoter; CREB directly activates ALEX1 promoter activity, and Wnt/β-catenin signaling upregulates ALEX1 expression in a CRE-dependent manner. | PMID:20398052 | Cancer science |
| 2012 | Medium | ALEX1/ARMCX1 overexpression suppresses anchorage-dependent and -independent colony formation in human colorectal carcinoma cell lines (HCT116); the ALEX1 gene promoter is highly methylated in HCT116 and SW480 cells, silencing its expression. | PMID:22494058 | Cancer science |
| 2017 | Medium | ALEX1/ARMCX1 inhibits gastric cancer metastasis by suppressing thrombin-induced (PAR-1-mediated) activation of Rho GTPases; overexpression disrupts cytoskeletal structure and reduces RhoA/Rac1 activity, while ALEX1 promoter is highly methylated in GC cells and tissues. | PMID:28315004 | Journal of gastroenterology |
| 2015 | Low | ALEX1/ARMCX1 overexpression in breast cancer cells activates the intrinsic apoptosis pathway by upregulating Bax, cytosolic cytochrome c, active caspase-9, and active caspase-3 while downregulating Bcl-2 and mitochondrial cytochrome c; ALEX1 depletion has the opposite effect. | PMID:25921134 | Asian Pacific journal of cancer prevention |
| 2019 | Medium | miR-106b directly targets ALEX1/ARMCX1 in gastric cancer cells; ALEX1 upregulation rescues apoptosis induced by miR-106b inhibition and promotes phosphorylation of JAK1 and STAT3, indicating ALEX1 acts upstream of the JAK1/STAT3 signaling pathway. | PMID:30907988 | Cellular physiology and biochemistry |
| 2023 | Medium | After traumatic brain injury (TBI), Armcx1 expression decreases in neurons while miR-223-3p increases; miR-223-3p directly targets and reduces Armcx1 protein levels; Armcx1 overexpression protects against TBI-induced mitochondrial dysfunction, neuronal cell death, and axonal injury, while knockdown exacerbates these effects. | PMID:37454781 | Neurobiology of disease |
| 2024 | Medium | Armcx1 regulates neurological recovery after TBI through a mitochondrial transport pathway involving Miro1; Armcx1 inhibition reduces Miro1 expression and leads to impaired mitochondrial transport, abnormal mitochondrial morphology, reduced ATP levels, and increased neuronal apoptosis. | PMID:38492796 | Neuroscience |
| 2024 | Medium | ARMCX1 inhibits lung adenocarcinoma by recruiting the E3 ubiquitin ligase FBXW7 to mediate ubiquitinated degradation of c-Myc, thereby suppressing c-Myc nuclear accumulation and inactivating cell cycle and EMT signaling. | PMID:39285446 | Biology direct |
| 2026 | Medium | ARMCX1 promotes ubiquitination and proteasomal degradation of β-catenin in nasopharyngeal carcinoma by recruiting the E3 ubiquitin ligase TRIM21, thereby suppressing cell cycle progression and epithelial-mesenchymal transition; β-catenin overexpression rescues the tumor-suppressive effects of ARMCX1. | PMID:41533266 | Cellular oncology |
| 2024 | Medium | Conditional knockout of Armcx1 globally and in retinal neurons (using β-actin-Cre and Six3-Cre) shows no evidence of aberrant retinal or optic nerve development or RGC degeneration up to 15 months under normal physiological conditions, indicating Armcx1 is dispensable for baseline retinal homeostasis. | PMID:39139090 | Genesis |

## Citations

- PMID:11162520
- PMID:20398052
- PMID:22494058
- PMID:25921134
- PMID:28009275
- PMID:28315004
- PMID:30907988
- PMID:37454781
- PMID:38492796
- PMID:39139090
- PMID:39285446
- PMID:41533266
