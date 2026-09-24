---
title: "Retraction Register"
---

# Retraction Register

<!-- GENERATED FILE. Do not edit by hand. Regenerate with `uv run --no-dev python projects/RETRACTIONS/check_retractions.py`. -->

Every `PMID:` cited anywhere in the gene reviews, checked against PubMed's retraction metadata. Generated 2026-09-17 from **3736** review files and **25088** distinct cited PMIDs (**25087** resolved at PubMed, **1** unresolved). See the [project page](../RETRACTIONS.md) for method and curation guidance.

**7 retracted**, 13 under expression of concern, 659 with a published erratum.

## Retracted publications (actionable)

A retraction withdraws the *source*. It does not by itself refute a GO annotation, but every annotation resting on one of these papers needs re-examination, and the citation itself should carry `is_invalid: true`.

| PMID | Title | Journal / year | Notice | Cited by | Cited as | Annotation evidence? | Already flagged `is_invalid` |
|---|---|---|---|---|---|---|---|
| PMID:16616141 | Evidence that low doses of Taxol enhance the functional transactivatory properties of p53 on p21 waf promot... | FEBS Lett 2006 | PMID:40963457 | human/TP53 | GO annotation evidence, reference list, supporting text | **yes** | no |
| PMID:19225519 | APP binds DR6 to trigger axon pruning and neuron death via distinct caspases. | Nature 2009 | PMID:38110576 | human/TNFRSF21 | reference list | no | yes |
| PMID:22483618 | Lysyl oxidase-like 2 deaminates lysine 4 in histone H3. | Mol Cell 2012 | PMID:27392148 | human/LOXL2 | reference list, supporting text | no | yes |
| PMID:27782176 | Functional kinomics establishes a critical node of volume-sensitive cation-Cl- cotransporter regulation in ... | Sci Rep 2016 | PMID:42642456 | mouse/Mtor | GO annotation evidence, reference list | **yes** | no |
| PMID:29371969 | MiR-124 acts as a target for Alzheimer's disease by regulating BACE1. | Oncotarget 2017 | PMID:42664430 | human/BACE1 | GO annotation evidence, reference list | **yes** | no |
| PMID:31638206 | MicroRNA‑4500 suppresses tumor progression in non‑small cell lung cancer by regulating STAT3. | Mol Med Rep 2019 | PMID:41645757 | human/STAT3 | GO annotation evidence, reference list, supporting text | **yes** | no |
| PMID:32125225 | Actin‑like protein 8 executes a promoting function in the malignant progression of endometrial cancer: iden... | Biosci Biotechnol Biochem 2020 | PMID:35078223 | human/ACTL8 | reference list | no | yes |

Of these, **4** are cited as the `original_reference_id` of a GO annotation (human/BACE1, human/STAT3, human/TP53, mouse/Mtor) - these are the ones a curator should look at first.

## Expressions of concern

The record is questioned but not withdrawn. Worth reading the notice before leaning on the paper; not grounds for removing an annotation.

| PMID | Title | Journal / year | Notice | Cited by | Cited as | Annotation evidence? | Already flagged `is_invalid` |
|---|---|---|---|---|---|---|---|
| PMID:19033661 | AIP1 functions as an endogenous inhibitor of VEGFR2-mediated signaling and inflammatory angiogenesis in mice. | J Clin Invest 2008 | PMID:40955656 | human/DAB2IP, human/VEGFA | GO annotation evidence, reference list, supporting text | **yes** | no |
| PMID:20473329 | SIRPalpha1 receptors interfere with the EGFRvIII signalosome to inhibit glioblastoma cell transformation an... | Oncogene 2010 | PMID:37264082 | human/EGFR, human/PTPN11 | GO annotation evidence, reference list, supporting text | **yes** | no |
| PMID:14730064 | Calcium sensors and their interacting protein kinases: genomics of the Arabidopsis and rice CBL-CIPK signal... | Plant Physiol 2004 | PMID:38739113 | ARATH/CIPK24 | GO annotation evidence, reference list | **yes** | no |
| PMID:19624469 | Modulation of drought resistance by the abscisic acid receptor PYL5 through inhibition of clade A PP2Cs. | Plant J 2009 | PMID:41995107 | ARATH/PYR1 | GO annotation evidence, reference list, supporting text | **yes** | no |
| PMID:20208519 | Transcription-independent ARF regulation in oncogenic stress-mediated p53 responses. | Nature 2010 | PMID:41699183 | human/MYC | GO annotation evidence, reference list, supporting text | **yes** | no |
| PMID:22689054 | GRP78 regulates clusterin stability, retrotranslocation and mitochondrial localization under ER stress in p... | Oncogene 2013 | PMID:41912777 | human/CLU | GO annotation evidence, reference list, supporting text | **yes** | no |
| PMID:24147005 | The coordination of cell growth during fission yeast mating requires Ras1-GTP hydrolysis. | PLoS One 2013 | PMID:31600315 | SCHPO/cdc42 | GO annotation evidence, reference list, supporting text | **yes** | no |
| PMID:24608080 | MicroRNA-27a/b regulates cellular cholesterol efflux, influx and esterification/hydrolysis in THP-1 macroph... | Atherosclerosis 2014 | PMID:34217526 | human/LPL | GO annotation evidence, reference list | **yes** | no |
| PMID:25084135 | MicroRNA-19b promotes macrophage cholesterol accumulation and aortic atherosclerosis by targeting ATP-bindi... | Atherosclerosis 2014 | PMID:34217524 | human/ABCA1 | GO annotation evidence, reference list | **yes** | no |
| PMID:25446899 | Cancer exosomes perform cell-independent microRNA biogenesis and promote tumorigenesis. | Cancer Cell 2014 | PMID:40930611 | human/AGO2 | GO annotation evidence, reference list | **yes** | no |
| PMID:25465408 | C2-domain abscisic acid-related proteins mediate the interaction of PYR/PYL/RCAR abscisic acid receptors wi... | Plant Cell 2014 | PMID:40828150 | ARATH/PYR1 | GO annotation evidence, reference list, supporting text | **yes** | no |
| PMID:29794473 | MiR-27b Impairs Adipocyte Differentiation of Human Adipose Tissue-Derived Mesenchymal Stem Cells by Targeti... | Cell Physiol Biochem 2018 | PMID:37125420 | human/LPL | GO annotation evidence, reference list | **yes** | no |
| PMID:29961672 | miR-15b reduces amyloid-β accumulation in SH-SY5Y cell line through targetting NF-κB signaling and BACE1. | Biosci Rep 2018 | PMID:33835140 | human/APP | GO annotation evidence, reference list, supporting text | **yes** | no |

## Errata (informational)

659 cited papers have a published erratum. **An erratum is normally benign** - most correct an author name, an affiliation, a funding statement or a figure legend, and the science stands unchanged. They are listed here for completeness only and require no action unless the correction happens to touch the result being cited.

| PMID | Title | Journal / year | Cited by | Cited as |
|---|---|---|---|---|
| PMID:40205054 | Multimodal cell maps as a foundation for structural and functional genomics. | Nature 2025 | human/AAGAB, human/ABCD4, human/ABI2, ... (+274 more) [277 genes] | GO annotation evidence, reference list, supporting text |
| PMID:21988832 | Toward an understanding of the protein interaction network of the human liver. | Mol Syst Biol 2011 | human/AIMP2, human/ALDH7A1, human/ALDOA, ... (+80 more) [83 genes] | GO annotation evidence, reference list, supporting text |
| PMID:12534463 | Complete genome sequence and comparative analysis of the metabolically versatile Pseudomonas putida KT2440. | Environ Microbiol 2002 | PSEPK/PP_3768, PSEPK/aceK, PSEPK/algG, ... (+76 more) [79 genes] | reference list, supporting text |
| PMID:16823372 | ORFeome cloning and global analysis of protein localization in the fission yeast Schizosaccharomyces pombe. | Nat Biotechnol 2006 | SCHPO/SPAC8E11.10, SCHPO/SPCC16C4.02c, SCHPO/acn1, ... (+58 more) [61 genes] | GO annotation evidence, reference list, supporting text |
| PMID:21903422 | Mapping a dynamic innate immunity protein interaction network regulating type I interferon production. | Immunity 2011 | human/AGO2, human/AIP, human/ATG7, ... (+28 more) [31 genes] | GO annotation evidence, reference list, supporting text |
| PMID:32612234 | Extensive signal integration by the phytohormone protein network. | Nature 2020 | ARATH/ABI1, ARATH/ABI5, ARATH/ARF19, ... (+23 more) [26 genes] | GO annotation evidence, reference list, supporting text |
| PMID:36115835 | Quantitative fragmentomics allow affinity mapping of interactomes. | Nat Commun 2022 | human/ABCA1, human/ABCA7, human/ABRAXAS2, ... (+20 more) [23 genes] | GO annotation evidence, reference list, supporting text |
| PMID:28650476 | CrY2H-seq: a massively multiplexed assay for deep-coverage interactome mapping. | Nat Methods 2017 | ARATH/AP1, ARATH/ARF19, ARATH/AT5G03720, ... (+12 more) [15 genes] | GO annotation evidence, reference list, supporting text |
| PMID:14743216 | A physical and functional map of the human TNF-alpha/NF-kappa B signal transduction pathway. | Nat Cell Biol 2004 | human/AZI2, human/C1QBP, human/CLTC, ... (+10 more) [13 genes] | GO annotation evidence, reference list, supporting text |
| PMID:14519844 | Divergent retroviral late-budding domains recruit vacuolar protein sorting factors by using alternative ada... | Proc Natl Acad Sci U S A 2003 | human/CHMP1A, human/CHMP1B, human/CHMP2A, ... (+9 more) [12 genes] | GO annotation evidence, reference list, supporting text |
| PMID:20211142 | An atlas of combinatorial transcriptional regulation in mouse and man. | Cell 2010 | human/ATF2, human/ATF3, human/ATF4, ... (+9 more) [12 genes] | GO annotation evidence, reference list, supporting text |
| PMID:39251607 | Systematic identification of post-transcriptional regulatory modules. | Nat Commun 2024 | human/ABL1, human/AGO2, human/BAIAP2, ... (+9 more) [12 genes] | GO annotation evidence, reference list, supporting text |
| PMID:35922511 | A physical wiring diagram for the human immune system. | Nature 2022 | human/APP, human/CD28, human/CD320, ... (+8 more) [11 genes] | GO annotation evidence, reference list, supporting text |
| PMID:24722188 | Protein interaction network of alternatively spliced isoforms from brain links genetic risk factors for aut... | Nat Commun 2014 | human/CRMP1, human/CTBP1, human/DPYSL2, ... (+7 more) [10 genes] | GO annotation evidence, reference list, supporting text |
| PMID:15489334 | The status, quality, and expansion of the NIH full-length cDNA project: the Mammalian Gene Collection (MGC). | Genome Res 2004 | human/AADACL2, human/ADAM5, human/C18orf21, ... (+6 more) [9 genes] | reference list |
| PMID:19464326 | HSPB7 is a SC35 speckle resident small heat shock protein. | Biochim Biophys Acta 2009 | human/CRYAA, human/CRYAB, human/HSPB2, ... (+5 more) [8 genes] | GO annotation evidence, reference list, supporting text |
| PMID:28298427 | Systematic protein-protein interaction mapping for clinically relevant human GPCRs. | Mol Syst Biol 2017 | human/ADRB2, human/CALR, human/FZD7, ... (+4 more) [7 genes] | GO annotation evidence, reference list, supporting text |
| PMID:36508461 | A role for brassinosteroid signalling in decision-making processes in the Arabidopsis seedling. | PLoS Genet 2022 | ARATH/BRI1, ARATH/BZR1, ARATH/CRY1, ... (+4 more) [7 genes] | GO annotation evidence, reference list, supporting text |
| PMID:15962010 | Sulphatase activities are regulated by the interaction of sulphatase-modifying factor 1 with SUMF2. | EMBO Rep 2005 | human/ARSA, human/GALNS, human/GNS, ... (+3 more) [6 genes] | GO annotation evidence, reference list, supporting text |
| PMID:17711858 | The MIT domain of UBPY constitutes a CHMP binding and endosomal localization signal required for efficient ... | J Biol Chem 2007 | human/CHMP1A, human/CHMP1B, human/CHMP4B, ... (+3 more) [6 genes] | GO annotation evidence, reference list, supporting text |
| PMID:17853893 | Human ESCRT and ALIX proteins interact with proteins of the midbody and function in cytokinesis. | EMBO J 2007 | human/CD2AP, human/CHMP5, human/PDCD6IP, ... (+3 more) [6 genes] | GO annotation evidence, reference list |
| PMID:23614719 | Human prefoldin inhibits amyloid-β (Aβ) fibrillation and contributes to formation of nontoxic Aβ aggregates. | Biochemistry 2013 | human/PFDN1, human/PFDN2, human/PFDN4, ... (+3 more) [6 genes] | GO annotation evidence, reference list, supporting text |
| PMID:25438055 | AMBRA1 links autophagy to cell proliferation and tumorigenesis by promoting c-Myc dephosphorylation and deg... | Nat Cell Biol 2015 | human/AMBRA1, human/BECN1, human/MYC, ... (+3 more) [6 genes] | GO annotation evidence, reference list, supporting text |
| PMID:27303730 | GcsR, a TyrR-Like Enhancer-Binding Protein, Regulates Expression of the Glycine Cleavage System in Pseudomo... | mSphere 2016 | PSEPK/gcvH1, PSEPK/gcvH2, PSEPK/gcvP1, ... (+3 more) [6 genes] | reference list |
| PMID:11859360 | The genome sequence of Schizosaccharomyces pombe. | Nature 2002 | SCHPO/cdc7, SCHPO/cmc4, SCHPO/mug151, ... (+2 more) [5 genes] | reference list |
| PMID:12763021 | APH1, PEN2, and Nicastrin increase Abeta levels and gamma-secretase activity. | Biochem Biophys Res Commun 2003 | human/APH1A, human/APH1B, human/NCSTN, ... (+2 more) [5 genes] | GO annotation evidence, reference list, supporting text |
| PMID:19855925 | Structural analysis of the complex between calmodulin and full-length myelin basic protein, an intrinsicall... | Amino Acids 2010 | human/CALM1, human/CALM3, mouse/Calm1, ... (+2 more) [5 genes] | GO annotation evidence, reference list, supporting text |
| PMID:20654576 | Distinct functions of human MVB12A and MVB12B in the ESCRT-I dependent on their posttranslational modificat... | Biochem Biophys Res Commun 2010 | human/MVB12A, human/MVB12B, human/TSG101, ... (+2 more) [5 genes] | GO annotation evidence, reference list, supporting text |
| PMID:29320478 | An extracellular network of Arabidopsis leucine-rich repeat receptor kinases. | Nature 2018 | ARATH/BAK1, ARATH/BRI1, ARATH/CLV1, ... (+2 more) [5 genes] | GO annotation evidence, reference list, supporting text |
| PMID:10625637 | Distinct classes of phosphatidylinositol 3'-kinases are involved in signaling pathways that control macroau... | J Biol Chem 2000 | human/ATG14, human/BECN1, human/PIK3C3, ... (+1 more) [4 genes] | GO annotation evidence, reference list, supporting text |
| PMID:11823423 | A mutant EGF-receptor defective in ubiquitylation and endocytosis unveils a role for Grb2 in negative signa... | EMBO J 2002 | mouse/Cbl, mouse/Egf, mouse/Egfr, ... (+1 more) [4 genes] | GO annotation evidence, reference list |
| PMID:15383276 | A protein interaction network links GIT1, an enhancer of huntingtin aggregation, to Huntington's disease. | Mol Cell 2004 | human/CRMP1, human/GADD45G, human/HTT, ... (+1 more) [4 genes] | GO annotation evidence, reference list, supporting text |
| PMID:17274640 | A limited screen for protein interactions reveals new roles for protein phosphatase 1 in cell cycle control... | J Proteome Res 2007 | human/CDH1, human/PTEN, human/RB1, ... (+1 more) [4 genes] | GO annotation evidence, reference list, supporting text |
| PMID:17881773 | Peroxisomes in human and mouse testis: differential expression of peroxisomal proteins in germ cells and di... | Biol Reprod 2007 | human/ACAA1, human/ACOX1, human/PEX13, ... (+1 more) [4 genes] | GO annotation evidence, reference list, supporting text |
| PMID:19416851 | Identification of small subunits of mammalian serine palmitoyltransferase that confer distinct acyl-CoA sub... | Proc Natl Acad Sci U S A 2009 | human/KDSR, human/SPTLC1, human/SPTLC2, ... (+1 more) [4 genes] | GO annotation evidence, reference list, supporting text |
| PMID:25284079 | Arabidopsis acyl-CoA-binding protein ACBP3 participates in plant response to hypoxia by modulating very-lon... | Plant J 2015 | ARATH/CTR1, ARATH/EIN3, ARATH/NPR1, ... (+1 more) [4 genes] | GO annotation evidence, reference list, supporting text |
| PMID:26005850 | Central role for PICALM in amyloid-β blood-brain barrier transcytosis and clearance. | Nat Neurosci 2015 | human/APP, human/CLTC, human/LRP1, ... (+1 more) [4 genes] | GO annotation evidence, reference list, supporting text |
| PMID:9634230 | Deciphering the biology of Mycobacterium tuberculosis from the complete genome sequence. | Nature 1998 | MYCTU/Rv0311, MYCTU/Rv0898c, MYCTU/Rv3660c, ... (+1 more) [4 genes] | reference list |
| PMID:16213212 | Regulation of p53 translation and induction after DNA damage by ribosomal protein L26 and nucleolin. | Cell 2005 | human/HRAS, human/TP53, mouse/Trp53 | GO annotation evidence, reference list, supporting text |
| PMID:16809764 | Histone deacetylase 8 safeguards the human ever-shorter telomeres 1B (hEST1B) protein from ubiquitin-mediat... | Mol Cell Biol 2006 | human/HSPA1A, human/HSPA1B, human/STUB1 | GO annotation evidence, reference list, supporting text |

(40 of 659 shown, most-cited first; the full list is in `retraction-check.tsv`.)

## Unresolved PMIDs

1 cited PMID(s) returned no PubMed record and could not be checked. These are typically malformed or withdrawn identifiers rather than retractions: PMID:34521819.
