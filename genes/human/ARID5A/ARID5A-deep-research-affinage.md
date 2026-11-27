---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARID5A
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q03989
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 22
citation_count: 22
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARID5A (human)

## Current model (mechanistic narrative)

ARID5A (Arid5a) is a bifunctional nucleic acid-binding protein that governs inflammatory gene expression by acting either as a cytoplasmic RNA-stabilizing factor or as a nuclear transcription factor, depending on its subcellular localization [PMID:29358370, PMID:38866324]. Its founding and best-characterized activity is post-transcriptional: cytoplasmic Arid5a binds stem-loop or AU-rich elements in the 3' UTRs of pro-inflammatory transcripts—including IL-6, Stat3, T-bet, and OX40—to stabilize them, directly counteracting the destabilizing ribonucleases Regnase-1 and Roquin-1 and thereby driving cytokine production and Th17/Th1 differentiation [PMID:23676272, PMID:27022145, PMID:27671645, PMID:29244194]. Localization is dynamic and decisive for function: Arid5a is imported via importin-α/β1 and exported by CRM1, with inflammatory stimulation (LPS, IL-17) shifting it to the cytoplasm where stabilization occurs, and it associates with UPF1 and, upon IL-17-driven export, with the 40S ribosome (18S rRNA) and the translation initiation complex to enhance translation of C/EBPβ, C/EBPδ, and IκBζ [PMID:30301788, PMID:29358370, PMID:39058386]. Structurally, its ARID domain binds DNA with a defined preference while flanking intrinsically disordered regions modulate both DNA specificity and RNA interactions, explaining its dual nucleic-acid engagement [PMID:38866324]. In the nucleus it functions as a sequence-specific transcription factor, co-activating Sox9 on the Col2a1 promoter with histone H3 acetylation, repressing the metabolic genes Ppar-γ2, Cd36, and Fabp4, and activating the AIM2 inflammasome promoter [PMID:21346191, PMID:31289228, PMID:42148117, PMID:40632872]. Arid5a abundance is tightly controlled by an NF-κB/IL-6 induction loop and by p38 MAPK-driven phosphorylation that recruits the WWP1 E3 ligase for K48-linked ubiquitination and degradation, with AUF-1 destabilizing its own mRNA; it is induced upstream by TNF via NF-κB1/TRAF2, by β2-adrenergic/cAMP/PKA/CREB signaling, and by IL-17, and repressed by Rbpjl [PMID:28168301, PMID:30301788, PMID:35725649, PMID:41574607, PMID:32302067]. Through these activities Arid5a contributes to autoimmune and inflammatory pathology (septic shock, EAE, collagen-induced arthritis, nephropathy), tumor immune evasion via IDO1/CCL2-driven tryptophan catabolism, and cardiac and metabolic homeostasis [PMID:27671645, PMID:34006522, PMID:38316094, PMID:41574607, PMID:40632872].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003723 RNA binding, GO:0003677 DNA binding, GO:0140110 transcription regulator activity, GO:0140313 molecular sequestering activity, GO:0045182 translation regulator activity
- **localization:** GO:0005829 cytosol, GO:0005634 nucleus, GO:0005840 ribosome, GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-8953854 Metabolism of RNA, R-HSA-168256 Immune System, R-HSA-74160 Gene expression (Transcription), R-HSA-392499 Metabolism of proteins, R-HSA-162582 Signal Transduction
- **partners:** REGNASE-1, ROQUIN-1, WWP1, AUF-1, UPF1, TRAF2, SOX9, RBPJL
- **complexes:** 40S ribosomal subunit, eukaryotic translation initiation complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | High | Arid5a is an RNA-binding protein that stabilizes IL-6 mRNA (but not TNF-α mRNA) by binding to the 3' UTR of IL-6 mRNA, and counteracts the destabilizing effect of the ribonuclease Regnase-1 on IL-6 mRNA. | PMID:23676272 | Proceedings of the National Academy of Sciences of the United States of America |
| 2016 | High | Arid5a selectively stabilizes Stat3 mRNA (but not Stat1 or Stat5 mRNA) in CD4+ T cells in an IL-6-dependent manner, directing naive CD4+ T cells toward Th17 differentiation. | PMID:27022145 | The Journal of experimental medicine |
| 2016 | High | Arid5a binds to the conserved stem-loop structure in the 3' UTR of T-bet mRNA and stabilizes it, thereby promoting IFN-γ production in Th1 cells and contributing to septic shock. | PMID:27671645 | Proceedings of the National Academy of Sciences of the United States of America |
| 2017 | High | During late-phase LPS stimulation, p38 MAPK phosphorylates Arid5a and recruits the E3 ubiquitin ligase WWP1, which ubiquitinates Arid5a via K48-linked polyubiquitination, leading to its proteasomal degradation. Additionally, NF-κB and an IL-6 positive feedback loop activate Arid5a gene expression during early-phase LPS stimulation, and AUF-1 destabilizes Arid5a mRNA by binding AU-rich elements in its 3' UTR. | PMID:28168301 | Nucleic acids research |
| 2018 | High | Arid5a is recruited to the adaptor TRAF2 upon IL-17 stimulation, stabilizes IL-17-induced cytokine transcripts by binding their 3' UTRs, counteracts MCPIP1 (Regnase-1)-mediated mRNA degradation, and inducibly associates with the eukaryotic translation initiation complex to facilitate translation of the transcription factors IκBζ and C/EBPβ. | PMID:30301788 | Science signaling |
| 2018 | High | Arid5a is a dynamic protein that resides in both cytoplasm and nucleus; upon inflammatory stimulation (LPS), nuclear Arid5a levels decrease and cytoplasmic levels increase. Nuclear import occurs via the classical importin-α/β1 pathway, and nuclear export is regulated by CRM1 (chromosomal region maintenance 1). Arid5a associates with UPF1 (up-frameshift protein 1). Cytoplasmic localization is required for its mRNA stabilization function. | PMID:29358370 | Proceedings of the National Academy of Sciences of the United States of America |
| 2018 | High | Arid5a stabilizes OX40 mRNA in CD4+ T cells under Th17 conditions by recognizing an alternative decay element (ADE)-like stem-loop structure in the OX40 3' UTR, and impairs RNA-destabilizing functions of both Regnase-1 and Roquin-1 on this same stem-loop. | PMID:29244194 | European journal of immunology |
| 2011 | High | Arid5a physically interacts with Sox9 in the nucleus, up-regulates chondrocyte-specific transcriptional activity of Sox9, binds directly to the Col2a1 gene promoter, and stimulates histone H3 acetylation at the Col2a1 promoter region. | PMID:21346191 | Molecular biology of the cell |
| 2021 | Medium | Arid5a stabilizes Ido1 (IDO1) and Ccl2 mRNAs in tumor cells, augmenting tryptophan catabolism and creating an immunosuppressive tumor microenvironment that facilitates immune evasion. | PMID:34006522 | Cancer immunology research |
| 2019 | Medium | Arid5a represses transcription of Ppar-γ2, and Arid5a and Ppar-γ2 are dynamically counterregulated by each other to maintain adipose tissue homeostasis. Arid5a deficiency leads to persistent Ppar-γ2 expression and enhanced fatty acid uptake. | PMID:31289228 | Proceedings of the National Academy of Sciences of the United States of America |
| 2025 | Medium | ARID5A stabilizes MAVS (Mitochondrial Antiviral Signaling Protein) mRNA, leading to NF-κB and TBK1 activation, which amplifies aging and inflammation phenotypes in the heart. | PMID:40301689 | Nature cardiovascular research |
| 2024 | High | The ARID domain of Arid5a binds DNA with a defined preference (determined by NMR) and RNA via a consensus motif (determined by high-throughput in vitro binding); intrinsically disordered regions (IDRs) flanking the ARID domain modulate DNA-binding specificity/affinity and are crucial for RNA interactions. Transcriptome-wide iCLIP2 reveals weak preference for (A)U-rich regions in pre-mRNA transcripts related to RNA processing. | PMID:38866324 | The Journal of biological chemistry |
| 2024 | High | Arid5a inducibly interacts with conventional IL-17 target mRNAs including CEBPB and CEBPD (identified by RIP-Seq), and associates with 18S rRNA (a 40S ribosome constituent) upon IL-17-driven nuclear export, facilitating global protein synthesis and controlling C/EBP expression at the translational rather than mRNA accumulation level. | PMID:39058386 | The Journal of experimental medicine |
| 2024 | Medium | ARID5A stabilizes IDO1 mRNA in colorectal cancer cells, leading to tryptophan-to-kynurenine conversion that induces CAR T cell exhaustion via aryl hydrocarbon receptor (AhR) activation. | PMID:38316094 | Translational oncology |
| 2022 | Medium | Rbpjl binds to the promoter region of Arid5a and down-regulates its expression, thereby repressing IL-6/STAT3 signaling in pancreatic acinar cells. | PMID:35725649 | Cell & bioscience |
| 2026 | Medium | TNF induces Arid5a expression and cytoplasmic relocalization through the NF-κB1/TRAF2 pathway; cytoplasmic Arid5a stabilizes proinflammatory transcripts and enhances expression of chemokines driving rheumatoid arthritis. Arid5a-/- mice are resistant to collagen-induced arthritis with reduced Th17 cells in synovial tissue. | PMID:41574607 | JCI insight |
| 2021 | Medium | Arid5a promotes transcription of the lncRNA AU021063, which in turn stabilizes Trib3 and activates Mek/Erk signaling to promote breast cancer metastasis. Genetic ablation of Arid5a abolished breast cancer metastasis in vitro and in vivo. | PMID:34389433 | Cancer letters |
| 2020 | Medium | β2-adrenergic receptor stimulation induces Arid5a expression via the cAMP/PKA/CREB pathway in cardiac fibroblasts, and Arid5a induction is required for β2AR-mediated IL-6 mRNA upregulation (post-transcriptional stabilization). | PMID:32302067 | Pharmacology research & perspectives |
| 2026 | Medium | Arid5a functions as a transcription factor that binds to the AIM2 promoter to transcriptionally activate AIM2 expression, promoting inflammasome activation and pyroptosis in podocytes. | PMID:42148117 | Frontiers in immunology |
| 2025 | Medium | In skeletal muscle, Arid5a acts as a transcriptional repressor of lipid uptake genes Cd36 and Fabp4, reducing muscle triacylglycerol accumulation. This function is activated downstream of a mutant glucocorticoid receptor (GR rs6190 polymorphism). | PMID:40632872 | Science advances |
| 2002 | Medium | ATP suppresses MRF-1 (Arid5a) mRNA and protein synthesis in microglia at the transcriptional level via Ca2+ influx through P2X7 receptors; ATP does not affect MRF-1 protein degradation rate or total protein synthesis. | PMID:12363408 | Brain research |
| 2002 | Medium | MRF-1 (Arid5a) is released from microglia into the extracellular space, and this release is markedly enhanced by ATP and PAF (platelet-activating factor) through a Ca2+-dependent mechanism requiring P2X7 receptor activation. | PMID:12420315 | Glia |

## Citations

- PMID:12363408
- PMID:12420315
- PMID:21346191
- PMID:23676272
- PMID:27022145
- PMID:27671645
- PMID:28168301
- PMID:29244194
- PMID:29358370
- PMID:30301788
- PMID:31289228
- PMID:32302067
- PMID:34006522
- PMID:34389433
- PMID:35725649
- PMID:38316094
- PMID:38866324
- PMID:39058386
- PMID:40301689
- PMID:40632872
- PMID:41574607
- PMID:42148117
