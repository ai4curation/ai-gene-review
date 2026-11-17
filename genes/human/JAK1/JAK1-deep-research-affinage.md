---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/JAK1
affinage_run_date: 2026-06-10T01:55:23
uniprot_accession: P23458
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 35
citation_count: 35
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for JAK1 (human)

## Current model (mechanistic narrative)

JAK1 is a non-receptor tyrosine kinase that serves as an obligate signaling hub for cytokine and interferon receptors, coupling receptor engagement to STAT activation across immune, hematopoietic, and developmental programs [PMID:8232552, PMID:28965767]. It is mutually dependent on partner kinases for interferon signaling — acting with TYK2 in the IFN-α/β pathway and with JAK2 in the IFN-γ pathway — where its activity and pseudokinase (JH2) domain are required for correct receptor complex assembly and STAT phosphorylation [PMID:8232552, PMID:9249040, PMID:31892268]. JAK1 function is non-redundant in vivo: conditional deletion impairs hematopoietic stem cell self-renewal, cytokine sensing, and NK cell development, and JAK2 cannot compensate for its loss [PMID:28965767, PMID:30671064]. Beyond canonical STAT signaling, JAK1 directly phosphorylates a defined set of substrates: PERK during ER stress to drive a PERK/JAK1/STAT3 axis [PMID:25113558], SIRT1 at Y280/Y301 to enable SIRT1-STAT3 negative feedback [PMID:29789426], and PD-L1 at Y112 to recruit STT3A and stabilize PD-L1 glycosylation, linking IL-6/JAK1 signaling to immune evasion [PMID:31305264]. JAK1 activity is tightly controlled by multiple layers: dephosphorylation by receptor-associated PTPs including TCPTP [PMID:9238016, PMID:18948751], proteasomal turnover modulated by SOCS1 competition (antagonized by EHBP1L1) [PMID:36775874], HDAC1-dependent acetylation at K1109 [PMID:39384195], and positive regulation by ZDHHC3/7-mediated palmitoylation that facilitates activation-loop transphosphorylation [PMID:37356718]. Its catalytic state is further shaped by activating hinge mutations that confer drug resistance [PMID:21393331] and by a JAK1-selective allosteric cysteine (C817) in the pseudokinase domain that is targetable by electrophilic inhibitors [PMID:36097295]. Loss-of-function JAK1 mutations abrogate IFN-γ responsiveness and PD-L1 induction, mediating resistance to PD-1 blockade [PMID:27903500], while biallelic missense mutations cause a human immune dysregulation phenotype with impaired cytokine signaling [PMID:28008925].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016740 transferase activity, GO:0140657 ATP-dependent activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005886 plasma membrane, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-168256 Immune System, R-HSA-162582 Signal Transduction, R-HSA-74160 Gene expression (Transcription), R-HSA-392499 Metabolism of proteins, R-HSA-1643685 Disease
- **partners:** TYK2, JAK2, STAT3, SIRT1, PERK, TCPTP, AJUBA, STING
- **complexes:** cytokine receptor-JAK signaling complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1993 | High | JAK1 is required for both interferon-alpha/beta and interferon-gamma signal transduction. A JAK1-deficient cell line was completely defective in interferon response; complementation with JAK1 restored signaling. JAK1 and TYK2 are mutually dependent in the IFN-α pathway, and JAK1 and JAK2 are mutually dependent in the IFN-γ pathway, likely reflecting a requirement for these kinases in correct assembly of interferon receptor complexes. | PMID:8232552 | Nature |
| 1997 | High | Receptor-associated constitutive protein tyrosine phosphatase (PTP) activity controls JAK1 kinase function. Inhibition of PTP activity with pervanadate activates JAKs and leads to JAK1-dependent, IL-4Rα-mediated STAT6 activation independently of receptor dimerization. This indicates that constitutive PTP activity suppresses persistent receptor-linked JAK1 activity. | PMID:9238016 | Proceedings of the National Academy of Sciences of the United States of America |
| 1997 | Medium | Kinase-deficient dominant-negative forms of JAK1 and TYK2 each independently inhibit IFN-α–induced STAT phosphorylation and transcriptional activation, establishing that JAK1 kinase activity is required upstream of TYK2 in the IFN-α signaling cascade. | PMID:9249040 | European journal of biochemistry |
| 1997 | Medium | Jak1 kinase is required for a specific cell migration (epiboly) and anterior specification in zebrafish embryos. Injection of dominant-negative Jak1 RNA reduces epiboly and decreases goosecoid expression and anterior structures, establishing a developmental role for JAK1 beyond cytokine signaling. | PMID:9096349 | Proceedings of the National Academy of Sciences of the United States of America |
| 1998 | Medium | Hepatitis B virus HBx protein specifically activates JAK1 (but not JAK2 or TYK2) through direct protein–protein interaction with JAK1, elevating JAK1 tyrosine phosphorylation and kinase activity, and subsequently activating STAT3 and STAT5. | PMID:9738022 | The Journal of biological chemistry |
| 2003 | High | JAK1 is required for IFN-γ–mediated growth arrest and/or apoptosis of v-abl–transformed pre-B cells. JAK1-deficient transformed cells were more tumorigenic in vivo, and their increased tumorigenicity correlated with loss of IFN-γ responsiveness, establishing JAK1's role in intrinsic IFN-γ–dependent tumor surveillance rather than in promotion of tumorigenesis. | PMID:12576323 | Blood |
| 2007 | High | JAK1 is required for myoblast proliferation and acts as a checkpoint preventing premature differentiation. JAK1 knockdown induces accelerated MyoD, MEF2, p21Cip1, and p27Kip1 induction and faster Id1 downregulation. Downstream, JAK1-STAT1-STAT3 constitutes the pathway through which LIF stimulates myoblast proliferation and represses differentiation. | PMID:17908914 | The Journal of cell biology |
| 2008 | Medium | Myricetin directly binds to JAK1 (and STAT3) with higher affinity for JAK1 than STAT3, inhibiting JAK1 phosphorylation and EGF-induced cell transformation. Ex vivo and in vitro pull-down assays confirmed direct binding; myricetin inhibited JAK1 phosphorylation without affecting EGFR autophosphorylation. | PMID:18995957 | Cancer letters |
| 2008 | Medium | TCPTP (protein tyrosine phosphatase) dephosphorylates and negatively regulates JAK1 and STAT3 signaling during the cell cycle. TCPTP-deficient MEFs show enhanced SFK, JAK1, and STAT3 activation; however, JAK1 and STAT3 (not SFK) signaling was not required for the enhanced G1/S transition observed. | PMID:18948751 | Cell cycle (Georgetown, Tex.) |
| 2011 | Medium | Activating mutations in JAK1 at Phe958 and Pro960 (hinge region of kinase domain) render JAK1 constitutively active and resistant to ATP-competitive JAK inhibitors. These mutations can both activate JAK1 oncogenically and confer drug resistance. | PMID:21393331 | Haematologica |
| 2014 | Medium | ER stress activates JAK1 in astrocytes in a PERK-dependent manner. JAK1 phosphorylates PERK, and this PERK/JAK1/STAT3 axis drives IL-6 and chemokine expression. Disruption of PERK abrogates ER stress–induced STAT3 activation. | PMID:25113558 | Molecular and cellular biology |
| 2015 | Medium | CXCL12/CXCR4 signaling promotes immunological synapse formation and T cell activation through Gi and JAK1/JAK2 kinase activation, contributing to actin polymerization at the APC contact site and MTOC polarization. | PMID:25917087 | Journal of immunology |
| 2016 | High | Loss-of-function JAK1 mutations in tumor cells result in inability to respond to interferon-gamma (IFN-γ), preventing IFN-γ–induced PD-L1 expression and interferon-stimulated gene induction, thereby mediating primary resistance to PD-1 blockade. | PMID:27903500 | Cancer discovery |
| 2016 | High | Biallelic JAK1 missense mutations (P733L and P832S) cause reduced JAK1 and STAT phosphorylation following cytokine stimulation, reduced interferon-regulated gene induction, and dysregulated cytokine production. The P733L mutation is primarily responsible. Reconstitution experiments revealed a phosphorylation-independent role of JAK1 in signal transduction. | PMID:28008925 | Nature communications |
| 2016 | Medium | AJUBA LIM protein binds specifically to the FERM domain of JAK1 to dissociate JAK1 from the IFN-γ receptor, inhibiting STAT1 phosphorylation and nuclear translocation, thereby suppressing the JAK1-STAT1-IFIT2 network and promoting cancer cell survival. | PMID:27893714 | Oncogene |
| 2017 | High | Conditional Jak1 deletion in hematopoietic stem cells (HSCs) reduces self-renewal, alters lymphoid/myeloid differentiation, decreases competitiveness, prevents cell cycle entry in response to hematopoietic stress, and markedly reduces cytokine sensing including to type I interferons and IL-3. JAK2 constitutive activation cannot fully rescue JAK1 loss in HSCs. | PMID:28965767 | Cell stem cell |
| 2018 | High | JAK1 phosphorylates SIRT1 at tyrosine residues Y280 and Y301 within the histone deacetylase catalytic domain in response to IL-6 stimulation. This phosphorylation does not alter SIRT1 deacetylase activity but is required for SIRT1 interaction with STAT3, enhancing SIRT1 suppression of STAT3 acetylation and transcriptional activity, constituting a negative feedback of the JAK1-STAT3 pathway. | PMID:29789426 | The Journal of biological chemistry |
| 2019 | High | IL-6-activated JAK1 directly phosphorylates PD-L1 at Tyr112, which recruits the ER-associated N-glycosyltransferase STT3A to catalyze PD-L1 glycosylation and maintain PD-L1 stability, linking oncogenic IL-6/JAK1 signaling to immune evasion. | PMID:31305264 | The Journal of clinical investigation |
| 2019 | Medium | JAK1 (not JAK2) is the STAT3-activating kinase mediating extrinsically activated STAT3 in TKI-treated CML stem cells, driven by IL-6. This was established using selective JAK1/2 inhibitors and genetic inactivation, and combined Bcr-Abl + JAK1 inhibition reduced CML stem cell colony formation and leukemic stem cells. | PMID:30842608 | Leukemia |
| 2019 | High | Conditional deletion of JAK1 (but not JAK2) in NKp46+ NK cells markedly reduces NK cell numbers in bone marrow, spleen, blood, and liver, impairs NK cell development, and impairs NK cell–mediated tumor surveillance. JAK2 is dispensable for NK cell survival and cannot compensate for JAK1 loss. | PMID:30671064 | Frontiers in immunology |
| 2019 | Medium | TROY (orphan TNF receptor) directly interacts with JAK1, increases JAK1 phosphorylation, and promotes STAT3 phosphorylation and transcriptional activity in a JAK1-dependent manner. JAK1 inhibition or knockdown significantly inhibits TROY-induced STAT3 activation, GBM cell migration, and temozolomide resistance. | PMID:32629176 | Neoplasia (New York, N.Y.) |
| 2019 | Medium | The JAK1 pseudokinase domain (JH2) has distinct regulatory functions across different receptor complexes: in IL-2 signaling JAK1 is dominant over JAK3 and strictly requires both JH1 and JH2; in IFN-γ signaling both JAK1 and JAK2 are indispensable for STAT1 activation and JAK1 JH2 (rather than kinase activity) is the key requirement. Mutations in the JAK1 JH2 αC-helix (L633) reduce basal and cytokine-induced STAT activation. | PMID:31892268 | Cancers |
| 2019 | Medium | TRAF6 negatively regulates JAK1 activation in IL-2 signaling by binding to the TRAF6-binding site on the IL-2R β-chain, which overlaps with the JAK1-binding site. A β-chain mutation that inactivates TRAF6 binding while retaining JAK1 binding abrogated TRAF6-dependent reduction in JAK1-Erk pathway activation. | PMID:21155952 | Genes to cells |
| 2022 | High | Itaconate and 4-octyl itaconate (OI) directly modify JAK1 at multiple cysteine residues (C715, C816, C943, C1130) and inhibit JAK1 kinase activity and phosphorylation, suppressing M2 macrophage polarization in response to IL-4, IL-13, IFN-β, and IFN-γ in vitro and in vivo. | PMID:35235776 | Cell metabolism |
| 2022 | High | JAK1 contains a druggable allosteric cysteine (C817) in its non-catalytic pseudokinase domain (absent from JAK2 and JAK3). Electrophilic compounds targeting C817 block JAK1-dependent trans-phosphorylation and cytokine signaling. Cells expressing a C817A JAK1 mutant are insensitive to these allosteric inhibitors, confirming C817 as the functional engagement site. | PMID:36097295 | Nature chemical biology |
| 2022 | High | Influenza A virus PB2 protein targets mammalian JAK1 at lysine residues K859 and K860 for ubiquitination and proteasomal degradation, suppressing IFN-α/β signaling and STAT1/STAT2 activation as a mechanism of immune evasion. | PMID:36271046 | Nature communications |
| 2022 | Medium | DPYSL2 (dihydropyrimidinase-like 2) directly interacts with JAK1, and this binding is required for activating STAT3 and subsequent vimentin expression, promoting breast cancer cell migration and metastasis. | PMID:35575798 | The Journal of cell biology |
| 2022 | Medium | JAK1 directly interacts with TGF-β receptor I subunit (TβRI). Silencing JAK1 promotes myofibroblast transdifferentiation; this is mediated via constitutive STAT3 activation that requires JAK1. Silencing unphosphorylated STAT3 suppresses TGF-β signaling, SMAD3 activation, and ECM production, revealing a noncanonical JAK1/STAT3 regulatory axis in lung fibroblasts. | PMID:36283961 | American journal of physiology. Lung cellular and molecular physiology |
| 2023 | High | HDAC1 deacetylates JAK1 at lysine 1109; HDAC inhibition (SAHA) increases JAK1 K1109 acetylation, promoting JAK1 proteasomal degradation and reducing STAT3-driven FGL1 transcription, thereby enhancing CD8+ T cell antitumor activity. | PMID:39384195 | Journal for immunotherapy of cancer |
| 2023 | Medium | EHBP1L1 interacts with and stabilizes JAK1 protein by competing with SOCS1 for JAK1 binding, thereby protecting JAK1 from proteasomal degradation and maintaining elevated JAK1/STAT1/PD-L1 signaling in renal cell carcinoma. | PMID:36775874 | Advanced science |
| 2023 | High | JAK1 is palmitoylated endogenously in dorsal root ganglion (DRG) neurons and in HEK293T cells. ZDHHC3 and ZDHHC7 are the dominant protein acyltransferases (PATs) for JAK1. Palmitoylation is critical for JAK1 kinase activity (even in vitro) and facilitates transphosphorylation of key activation loop sites, but minimally affects JAK1 localization in neurons. A leukemia-associated JAK1 mutation overrides palmitoylation-dependence of JAK1 activity. JAK1 palmitoylation is required for neuropoietic cytokine-dependent signaling and neuronal survival. | PMID:37356718 | The Journal of biological chemistry |
| 2023 | Medium | METTL3 deposits m6A on the 3' UTR of JAK1 mRNA to promote JAK1 translation via YTHDF1 recognition, increasing JAK1 protein levels and contributing to STAT3 pathway activation and colorectal cancer progression. | PMID:38001065 | Cell death & disease |
| 2023 | Medium | JAK1 kinase activity is required for HDV replication. JAK1 inhibition modulates ERK1/2 activation and S-HDAg (small hepatitis delta antigen) phosphorylation, which is crucial for viral replication. Co-immunoprecipitation confirmed JAK1 interaction within the HDV replication complex. | PMID:37925078 | Journal of hepatology |
| 2024 | Medium | Chemotherapy-induced JAK1 activation occurs through an alternative mechanism: DNA damage induces JAK1-SQ phosphorylation that releases JAK1 pseudokinase domain (JH2) inhibition, allowing JAK1 activation without cytokine receptor engagement. This leads to STAT6 nuclear translocation and GAS6 secretion, activating TAM kinases to confer chemoresistance in Ewing sarcoma. | PMID:38906855 | Nature communications |
| 2025 | Medium | STING acts downstream of IFN-α/β receptor (IFNAR) in endothelial cells and interacts directly with JAK1 upon IFN-I stimulation, promoting JAK1 phosphorylation. This interaction requires STING palmitoylation at Cysteine 91 but not the STING C-terminal tail (CTT) domain, and drives JAK1-STAT signaling for tumor vessel normalization and CD8+ T cell infiltration. | PMID:39817453 | The Journal of clinical investigation |

## Citations

- PMID:12576323
- PMID:17908914
- PMID:18948751
- PMID:18995957
- PMID:21155952
- PMID:21393331
- PMID:25113558
- PMID:25917087
- PMID:27893714
- PMID:27903500
- PMID:28008925
- PMID:28965767
- PMID:29789426
- PMID:30671064
- PMID:30842608
- PMID:31305264
- PMID:31892268
- PMID:32629176
- PMID:35235776
- PMID:35575798
- PMID:36097295
- PMID:36271046
- PMID:36283961
- PMID:36775874
- PMID:37356718
- PMID:37925078
- PMID:38001065
- PMID:38906855
- PMID:39384195
- PMID:39817453
- PMID:8232552
- PMID:9096349
- PMID:9238016
- PMID:9249040
- PMID:9738022
