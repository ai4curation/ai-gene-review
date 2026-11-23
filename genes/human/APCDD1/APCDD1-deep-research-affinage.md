---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/APCDD1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8J025
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 11
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for APCDD1 (human)

## Current model (mechanistic narrative)

APCDD1 is a membrane-bound glycoprotein that functions as a cell-autonomous negative-feedback inhibitor of Wnt/β-catenin signalling, acting at the cell surface upstream of β-catenin [PMID:20393562]. Mechanistically, its extracellular domain comprises two apposed β-barrel domains (ABD1 and ABD2), with ABD2 forming a large hydrophobic pocket that binds lipid; through this pocket the ectodomain engages WNT ligands via their conserved covalent palmitoleate modification, allowing APCDD1 to titrate WNT at the cell surface [PMID:37155902], and it physically interacts with WNT3A and the co-receptor LRP5 [PMID:20393562]. APCDD1 is itself a direct transcriptional target of the β-catenin/TCF4 complex through TCF/LEF motifs in its 5'-flanking region, establishing a self-limiting feedback loop [PMID:12384519], with expression additionally controlled by DNMT3a-mediated promoter methylation [PMID:28698141] and by miR-130 targeting of its 3'-UTR [PMID:28242765]. Beyond Wnt, APCDD1 acts as a dual inhibitor of BMP signalling during nervous-system and skin development [PMID:32320685]. This activity is deployed across diverse contexts: it modulates Wnt/Norrin signalling to time retinal vascular pruning and blood–retina barrier maturation [PMID:29154126], promotes oligodendrocyte differentiation in association with β-catenin [PMID:25946682], and positively regulates adipogenic differentiation by repressing Wnt [PMID:28242765]. In a context-dependent reversal, APCDD1 sustains rather than represses β-catenin and TCF/LEF activity in dental follicle cells to support osteogenic differentiation [PMID:25592970]. A signal-peptide mutation (Leu9Arg) that disrupts trafficking to the plasma membrane and acts dominant-negatively links APCDD1 to inherited hereditary hypotrichosis [PMID:20393562].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008289 lipid binding, GO:0098772 molecular function regulator activity, GO:0140313 molecular sequestering activity
- **localization:** GO:0005886 plasma membrane, GO:0005783 endoplasmic reticulum
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology
- **partners:** WNT3A, LRP5, WNT7A, CTNNB1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | APCDD1 is a membrane-bound glycoprotein that interacts in vitro with WNT3A and LRP5, two essential components of Wnt signalling, and inhibits Wnt signalling in a cell-autonomous manner upstream of β-catenin. | PMID:20393562 | Nature |
| 2010 | Medium | The disease-causing mutation Leu9Arg in the signal peptide of APCDD1 perturbs its translational processing from the endoplasmic reticulum to the plasma membrane; APCDD1(L9R) likely acts in a dominant-negative manner to inhibit the stability and membrane localization of the wild-type protein. | PMID:20393562 | Nature |
| 2002 | Medium | APCDD1 expression is a direct transcriptional target of the β-catenin/TCF4 complex, activated through two putative TCF/LEF-binding motifs in the 5'-flanking region of APCDD1, and its expression is down-regulated by exogenous wild-type APC and AXIN1. | PMID:12384519 | Cancer research |
| 2017 | High | Apcdd1 modulates Wnt/Norrin signalling in retinal endothelial cells to coordinate the timing of vascular pruning and barrier maturation; Apcdd1-deficient mice show delayed vessel pruning and precocious paracellular barrier formation, while Apcdd1-overexpressing mice show reduced vessel density and increased paracellular barrier permeability. | PMID:29154126 | Neuron |
| 2015 | Medium | Apcdd1 promotes oligodendrocyte (OL) differentiation, suppresses Wnt signalling, and associates with β-catenin in oligodendrocyte systems; Apcdd1 similarly promotes OL differentiation after gliotoxic white matter injury in vivo and acute hypoxia ex vivo. | PMID:25946682 | Glia |
| 2017 | Medium | APCDD1 positively regulates adipogenic differentiation by repressing Wnt signalling; siRNA silencing of APCDD1 increased Wnt pathway proteins (Wnt3a, Wnt5a, Wnt10b, LRP5, β-catenin) and inhibited adipocyte differentiation markers, while adenovirus-mediated APCDD1 overexpression enhanced adipogenesis. Additionally, miR-130 directly targets the 3'-UTR of APCDD1 mRNA to repress its expression. | PMID:28242765 | The Journal of biological chemistry |
| 2020 | Medium | Apcdd1 is a dual inhibitor of both BMP and Wnt signalling pathways in the developing nervous system and skin, functioning during body axis formation and neural differentiation; Apcdd1 also contains an evolutionarily novel protein domain. | PMID:32320685 | Developmental biology |
| 2017 | Medium | APCDD1 expression in osteosarcoma cells is epigenetically silenced by DNMT3a-mediated promoter DNA hypermethylation (not DNMT1 or DNMT3b); ectopic APCDD1 expression suppresses Wnt/β-catenin signalling and inhibits invasion and EMT-like properties of osteosarcoma cells. | PMID:28698141 | Biochemical and biophysical research communications |
| 2015 | Medium | In dental follicle cells (DFCs), APCDD1 sustains rather than inhibits β-catenin expression and TCF/LEF reporter activity, and is required for osteogenic marker expression (RUNX2) and matrix mineralization — an unusual context-dependent role contrasting its inhibitory function in hair follicle and oral squamous carcinoma cells. | PMID:25592970 | Biochemical and biophysical research communications |
| 2015 | Low | APCDD1 knockdown in developing tooth germs alters cell proliferation, cell adhesion molecule localization, epithelial rearrangement in the inner enamel epithelium, and results in ectopic cusp formation, modulating Wnt- and enamel knot-related signalling molecules at the cap stage. | PMID:26170146 | Histochemistry and cell biology |
| 2023 | High | The crystal structure of the APCDD1 extracellular domain reveals two closely apposed β-barrel domains (ABD1 and ABD2); ABD2 has a large hydrophobic pocket that accommodates a bound lipid. The APCDD1 ECD can bind WNT7A, likely via the covalently bound palmitoleate common to all WNTs, suggesting APCDD1 functions as a negative feedback regulator by titrating WNT ligands at the cell surface. | PMID:37155902 | Proceedings of the National Academy of Sciences of the United States of America |

## Citations

- PMID:12384519
- PMID:20393562
- PMID:25592970
- PMID:25946682
- PMID:26170146
- PMID:28242765
- PMID:28698141
- PMID:29154126
- PMID:32320685
- PMID:37155902
