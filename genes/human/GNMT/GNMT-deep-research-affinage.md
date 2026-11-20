---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/GNMT
affinage_run_date: 2026-06-10T01:55:21
uniprot_accession: Q14749
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 15
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for GNMT (human)

## Current model (mechanistic narrative)

GNMT is a homotetrameric S-adenosylmethionine (SAM)-dependent methyltransferase that transfers a methyl group from SAM to glycine, generating sarcosine and S-adenosylhomocysteine (SAH) and thereby acting as a regulatory node controlling the cellular SAM:SAH ratio and methyl-donor homeostasis [PMID:9655336]. Its enzymatic output is held in check by feedback inhibition from 5-methyltetrahydrofolate, and structural and biochemical dissection shows this regulation is mediated through the N-terminal tail: truncation of residues 1-8 or a phosphomimetic at serine 9 abolishes 5-methyltetrahydrofolate binding while preserving catalytic turnover, uncoupling folate feedback from activity and—when constitutively active—depleting SAM, raising SAH, and inducing methyl-donor stress [PMID:42244597]. Through this control of one-carbon flux, GNMT increases hepatic folate retention and folate-dependent homocysteine remethylation via methionine synthase [PMID:21210071] and supports folate-dependent purine/pyrimidine synthesis, limiting uracil misincorporation into DNA, with the enzyme translocating from cytoplasm to nucleus under prolonged folate depletion [PMID:23922098]. Beyond catalysis, GNMT binds PREX2 and promotes its HectH9-mediated proteasomal degradation, restraining AKT signaling and proliferation [PMID:28205209], and acts as a regulator of mitochondrial Complex II activity [PMID:31668391]. GNMT loss in mouse liver triggers NK-cell activation and TRAIL/DR5-mediated injury and fibrogenesis [PMID:25531568]. Its expression is transcriptionally repressed by MYC at the GNMT promoter [PMID:30760754] and post-transcriptionally repressed by miR-873-5p [PMID:31668391]. Benzo[a]pyrene induces serine-9 phosphorylation that drives nuclear translocation and modulates CYP1A1 expression [PMID:30987732].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016740 transferase activity, GO:0008289 lipid binding
- **localization:** GO:0005829 cytosol, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-392499 Metabolism of proteins
- **partners:** PREX2, HECTH9
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1998 | High | Crystal structure of apo-GNMT determined at 2.5 Å resolution, revealing it is a homotetramer (monomer Mr ~32,423 Da, 292 amino acids) with a three-domain monomer structure and a central channel. The tetramer assembles with intertwined N-terminal domains. Comparison with the AdoMet-bound structure showed only localized changes in the binding pocket residues between apo and substrate-bound forms. | PMID:9655336 | Protein science |
| 1998 | High | GNMT catalyzes methyl group transfer from S-adenosylmethionine (SAM) to glycine, producing S-adenosylhomocysteine (SAH) and sarcosine (N-methylglycine). The enzyme is inhibited by 5-methyltetrahydrofolate pentaglutamate, functioning as a regulatory enzyme controlling the SAM:SAH ratio. | PMID:9655336 | Protein science |
| 2011 | High | GNMT expression increases hepatic folate concentration and promotes folate-dependent homocysteine remethylation via methionine synthase. GNMT transgenic mice had significantly increased hepatic folate, while GNMT knockout mice had reduced folate and decreased methionine synthase expression. GNMT also reduced antifolate methotrexate cytotoxicity in cell lines. | PMID:21210071 | Molecular medicine |
| 2013 | High | GNMT supports folate-dependent pyrimidine and purine nucleotide synthesis and reduces uracil misincorporation into DNA. During prolonged folate depletion, GNMT translocates from cytoplasm into the nucleus. Loss of GNMT impairs nucleotide biosynthesis in vitro and in vivo. | PMID:23922098 | International journal of cancer |
| 2014 | High | In Drosophila, Gnmt is transcriptionally upregulated by dFoxO in the fat body in response to Toll-pathway activation (sterile inflammation from necrosis) and during fasting. Gnmt upregulation leads to increased sarcosine and reduced SAM levels in hemolymph, functioning as a rheostat for SAM metabolism and energy homeostasis. | PMID:24746817 | Cell reports |
| 2014 | High | GNMT deficiency in mice triggers NK cell activation and TRAIL-mediated liver injury and fibrogenesis. Genetic deletion of TRAIL in GNMT-/- mice (double TRAIL-/-/GNMT-/- mice) protected against chronic liver injury and fibrogenesis. In vivo silencing of DR5 (TRAIL receptor) also protected GNMT-/- mice from liver injury, establishing the TRAIL/DR5 axis as a key pathway downstream of GNMT deficiency. | PMID:25531568 | Laboratory investigation |
| 2017 | High | GNMT interacts with PREX2 (a PTEN inhibitor) and promotes its degradation through an E3 ligase HectH9-mediated proteasomal ubiquitination pathway. Depletion of GNMT or HectH9 results in PREX2 accumulation, AKT activation, and enhanced cell proliferation. Elevated PREX2 protein with AKT activation was confirmed in Gnmt knockout mouse liver. | PMID:28205209 | International journal of cancer |
| 2019 | Medium | GNMT functions as an essential regulator of mitochondrial Complex II (succinate dehydrogenase) activity in the electron transport chain. In NAFLD, GNMT is post-transcriptionally repressed by miR-873-5p in hepatocytes, leading to disrupted mitochondrial functionality and impaired fatty acid β-oxidation. | PMID:31668391 | Molecular metabolism |
| 2019 | Medium | Benzo[a]pyrene (BaP) treatment induces phosphorylation of GNMT at serine 9, which is required for BaP-induced nuclear translocation of GNMT. A serine 9 mutant incapable of phosphorylation showed dramatically decreased nuclear translocation and increased CYP1A1 expression upon BaP treatment. PKC and JNK were identified as candidate kinases for this phosphorylation. | PMID:30987732 | Journal of food and drug analysis |
| 2019 | High | MYC transcriptionally represses GNMT by binding to the GNMT promoter. ChIP assay showed MYC antibodies precipitated the human GNMT promoter. MYC overexpression inhibited GNMT promoter activity and endogenous GNMT protein; shRNA knockdown or pharmacological inhibition of MYC induced GNMT promoter activity and mRNA expression in hepatoma cells. GNMT and MYC expression were negatively correlated in human HCC samples. | PMID:30760754 | Scientific reports |
| 2020 | Medium | GNMT is a direct molecular target of carnosine in renal tubular epithelial cells, identified by cellular thermal shift assay (CETSA) and molecular docking. Increased GNMT expression mimicked carnosine's protective effects (reducing inflammation and fibrosis), and inhibition of GNMT abolished carnosine's protective effects, placing GNMT downstream of carnosine in this pathway. | PMID:33241846 | Clinical science |
| 2024 | Medium | In Drosophila fat body, Gnmt protein is degraded via the nuclear ubiquitin-proteasome system (UPS) under conditions of SAM shortage (nutrient deprivation or inhibition of SAM synthesis). This degradation maintains SAM levels. Inhibition of nuclear UPS-mediated Gnmt degradation causes starvation tolerance, demonstrating that Gnmt turnover is a mechanism for buffering SAM consumption. | PMID:bio_10.1101_2024.08.21.609067 | bioRxiv |
| 2024 | Medium | Aurora kinase A (AurA) promotes nuclear localization of FOXO3, which induces GNMT expression, thereby consuming SAM. AurA inhibition increases GNMT expression and reduces cellular SAM levels, leading to decreased H3K4me3 and H3K36me3 on Il6 and Tnf gene regions in trained macrophages, dampening trained immunity. This places GNMT in the mTOR-FOXO3-GNMT axis regulating SAM-dependent histone methylation. | PMID:bio_10.1101_2024.11.11.622956 | bioRxiv |
| 2026 | Medium | The GNMT N-terminal tail (specifically phosphorylation at serine 9, S9ph) is required for both catalytic turnover of SAM and for 5-methyltetrahydrofolate (5mTHF) binding/feedback inhibition. Distal N-terminal truncation (residues 1-8) or phosphomimetic substitution at S9 abolished 5mTHF binding while maintaining catalytic activity, uncoupling folate-feedback regulation from enzymatic function. S9ph is abundant in mouse liver and further enriched in aged mice. Constitutively active GNMT mutants in hepatocyte cell lines depleted SAM, increased SAH, disrupted protein methylation, impaired growth, and induced methyl-donor stress transcriptional responses. | PMID:42244597 | bioRxiv |
| 2025 | Low | Choline upregulates GNMT expression (mRNA and protein) in hepatocytes in a concentration-dependent manner. GNMT knockdown reversed the protective effects of choline on lipid synthesis genes (FAS, ACC), fatty acid oxidation (CPT1), lipoprotein assembly (ApoB100, MTTP), and bile acid metabolism (CYP7A1, CYP27A1, BSEP). AMPK inhibition reduced GNMT protein expression and elevated MYC, suggesting choline regulates GNMT through the AMPK/MYC axis. | PMID:41233636 | Stress biology |

## Citations

- PMID:21210071
- PMID:23922098
- PMID:24746817
- PMID:25531568
- PMID:28205209
- PMID:30760754
- PMID:30987732
- PMID:31668391
- PMID:33241846
- PMID:41233636
- PMID:42244597
- PMID:9655336
- PMID:bio_10.1101_2024.08.21.609067
- PMID:bio_10.1101_2024.11.11.622956
