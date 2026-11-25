---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABHD11
affinage_run_date: 2026-06-09T22:02:37
uniprot_accession: Q8NFV4
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

# Affinage mechanistic annotation for ABHD11 (human)

## Current model (mechanistic narrative)

ABHD11 is a mitochondrial serine hydrolase that safeguards 2-oxoglutarate dehydrogenase complex (OGDHc) function and thereby sustains TCA cycle flux and mitochondrial 2-oxoglutarate (2-OG) metabolism [PMID:32792488, PMID:40664791]. It was identified in an unbiased genome-wide screen as a determinant of cellular 2-OG levels that physically associates with OGDHc and maintains the catalytic competence of its lipoyl domain; loss or inhibition of ABHD11 impairs lipoylation and causes rapid 2-OG accumulation [PMID:32792488]. Mechanistically, ABHD11 acts as a deglutarylating thioesterase that selectively removes glutaryl adducts from the lipoate moiety of the OGDHc lipoyl domain, so that its absence allows glutaryl-lipoyl adducts to accumulate and rewires mitochondrial/TCA metabolism [PMID:40664791]. This enzymatic activity controls metabolic programming of human CD8+ T cells, favoring central memory formation and attenuating oxidative phosphorylation [PMID:40664791]. Pharmacological inhibition of ABHD11 dampens T cell cytokine production through a compromised TCA cycle that elevates 24,25-epoxycholesterol biosynthesis and activates the liver X receptor (LXR), suppressing effector function and delaying type 1 diabetes onset in mice [PMID:41184294]. In vitro, ABHD11 displays lipase/esterase-type activity toward para-nitrophenyl butyrate without acting on acylglycerols or acyl-CoAs, and is amenable to selective nanomolar inhibition [PMID:27544863].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016787 hydrolase activity, GO:0140098 catalytic activity, acting on RNA
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-168256 Immune System
- **partners:** OGDH
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2020 | High | ABHD11 associates with the 2-oxoglutarate dehydrogenase complex (OGDHc) and maintains catalytic activity of its lipoyl domain by preventing the formation of lipoyl adducts; loss or inhibition of ABHD11 impairs lipoylation of OGDHc and drives a rapid increase in 2-OG levels, linking ABHD11 to regulation of functional lipoylation and mitochondrial 2-OG metabolism. | PMID:32792488 | Nature communications |
| 2024 | High | ABHD11 acts as a deglutarylating thioesterase that selectively removes glutaryl adducts from lipoate on the OGDHc lipoyl domain; loss of ABHD11 causes accumulation of glutaryl-lipoyl adducts, driving 2-oxoglutarate accumulation and rewiring of mitochondrial/TCA cycle metabolism, and influences metabolic programming of human CD8+ T cells. | PMID:40664791 | Nature chemical biology |
| 2024 | High | ABHD11 acts as a thioesterase to selectively remove glutaryl adducts from lipoate (deglutarylation), maintaining TCA cycle integrity; this activity influences human T cell metabolic reprogramming, increasing central memory T cell formation and attenuating oxidative phosphorylation. | PMID:bio_10.1101_2024.09.11.612392 | bioRxiv |
| 2025 | High | Pharmacological inhibition of ABHD11 (mitochondrial hydrolase maintaining α-KGDH/OGDHc function) dampens cytokine production by human and mouse T cells; the anti-inflammatory mechanism involves a compromised TCA cycle leading to increased 24,25-epoxycholesterol biosynthesis and subsequent liver X receptor (LXR) activation, suppressing T cell effector function and delaying onset of type 1 diabetes in murine models. | PMID:41184294 | Nature communications |
| 2016 | Medium | Human ABHD11 exhibits lipase/esterase-type activity (hydrolyzes para-nitrophenyl butyrate) but does not utilize mono- or diacylglycerols, oleoyl-CoA, or arachidonoyl-CoA as substrates, and shows no amidase, protease, phosphatase, sulfatase, phospholipase C, or phosphodiesterase activity; a homology model based on bacterial esterase YbfF was generated revealing initial active-site features; potent nanomolar inhibitors with selectivity among metabolic serine hydrolases were identified by competitive activity-based protein profiling. | PMID:27544863 | European journal of pharmaceutical sciences |
| 2020 | Medium | ABHD11 is a serine hydrolase localized in mitochondria that can synthesize the endocannabinoid 2-arachidonoyl glycerol (2-AG) in vitro; however, ABHD11 knockout mice have similar 2-AG levels as wild-type mice and display a lean metabolic phenotype, resisting diet-induced weight gain with modulation of bile salts associated with reduced fat intestinal absorption. | PMID:32579589 | PloS one |
| 2011 | Medium | ABHD11 serine hydrolase activity (measured by activity-based proteomics) is elevated in human lung adenocarcinoma compared to matched non-neoplastic tissue, and increased ABHD11 activity correlates with development of distant metastases. | PMID:21596165 | Journal of proteomics |
| 2020 | Medium | Knockout of Abhd11 in mouse embryonic stem cells (ESCs) hampers ESC expansion and differentiation, triggers autophagic flux and apoptosis, and disrupts GSK3β/β-catenin and ERK signaling; ABHD11 overexpression exerts anti-apoptotic effects; Abhd11 KO causes misexpression of key metabolic enzymes related to lipid synthesis, glycolysis, and amino acid metabolism, implicating ABHD11 in lipid metabolic homeostasis in ESCs. | PMID:32733886 | Frontiers in cell and developmental biology |

## Citations

- PMID:21596165
- PMID:27544863
- PMID:32579589
- PMID:32733886
- PMID:32792488
- PMID:40664791
- PMID:41184294
- PMID:bio_10.1101_2024.09.11.612392
