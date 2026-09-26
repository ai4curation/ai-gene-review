---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGAP21
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q5T5U3
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 15
citation_count: 15
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGAP21 (human)

## Current model (mechanistic narrative)

ARHGAP21 is a large multifunctional Rho-family GTPase-activating protein that couples membrane and adhesion signaling to actin cytoskeletal remodeling, vesicular trafficking, and tissue morphogenesis [PMID:17347647, PMID:23235160]. It is recruited to the Golgi by GTP-bound ARF1 through a bipartite Arf-binding domain comprising a PH domain and an adjacent C-terminal alpha helix, both of which engage the ARF1 switch regions [PMID:17347647]. At its catalytic core it inactivates Cdc42, and also RhoA and RhoC, thereby controlling actin dynamics in contexts ranging from dynein-dependent retrograde transport of Shiga toxin to the Golgi and surface delivery of influenza neuraminidase [PMID:19692570, PMID:22318733], to cell-cell junction stability and HGF-induced epithelial-mesenchymal transition, where it additionally binds alpha-tubulin to promote its acetylation [PMID:23200924, PMID:23235160]. Its GAP activity is dynamically restrained by direct binding of beta-arrestin 1 across the GAP domain following angiotensin II receptor stimulation, gating RhoA-driven stress fiber formation [PMID:21173159], and the same beta-arrestin1/ARHGAP21/Cdc42 scaffold operates downstream of membrane-associated PTEN to orient the mitotic spindle during 3D glandular morphogenesis [PMID:28749339]. ARHGAP21 further acts as a scaffold for FAK and PKCzeta signaling to suppress cell migration [PMID:19268501, PMID:18662671], stabilizes filamin A by recruiting HSP90alpha through its PDZ domain to block FLNA ubiquitination [PMID:41957357], and is regulated by SUMO2/3 modification at lysine K1443 [PMID:22922005]. Through RhoC inactivation it controls hematopoietic progenitor adhesion, mobilization, and erythroid commitment [PMID:29212046].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity, GO:0060090 molecular adaptor activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005794 Golgi apparatus, GO:0005634 nucleus, GO:0005829 cytosol, GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-5653656 Vesicle-mediated transport, R-HSA-1266738 Developmental Biology
- **partners:** ARF1, ARRB1, PTK2, PRKCZ, CDC42, PTEN, FLNA, HSP90AA1
- **complexes:** beta-arrestin1/ARHGAP21/Cdc42 scaffold

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2007 | High | Crystal structure of ARF1(GTP)-bound form in complex with the Arf-binding domain (ArfBD) of ARHGAP21 at 2.1 Å resolution showed that ArfBD comprises a PH domain adjoining a C-terminal alpha helix, and that ARF1 interacts with both motifs through its switch regions, triggering structural rearrangement of the PH domain. Site-directed mutagenesis confirmed both the PH domain and helical motif are essential for ARF1 binding and Golgi recruitment of ARHGAP21. | PMID:17347647 | The EMBO journal |
| 2010 | High | β-arrestin 1 directly binds to ARHGAP21 in a region that transects the RhoA effector GAP domain, inhibiting its GAP function. This interaction is dynamically increased following angiotensin II stimulation of the type 1A receptor, and the complex modulates the temporal activation of RhoA leading to stress fiber formation. A cell-permeant peptide disrupting the β-arrestin 1/ARHGAP21 complex resulted in more active ARHGAP21, less efficient RhoA signaling, and attenuated stress fiber formation. | PMID:21173159 | Molecular and cellular biology |
| 2009 | Medium | ARHGAP21 is expressed in nuclear and perinuclear regions of glioblastoma cell lines and interacts with the C-terminal region of FAK. ARHGAP21 depletion by shRNAi increases FAK phosphorylation and downstream signaling activation, increases Cdc42 activity, MMP-2 production, and cell migration, indicating ARHGAP21 negatively regulates FAK signaling and cell migration. | PMID:19268501 | Biochimica et biophysica acta |
| 2008 | Medium | ARHGAP21 associates with PKCzeta and FAK in cardiac tissue and is redistributed to Z-lines and costameres after pressure overload. Co-transfection studies showed ARHGAP21 associates with PKCzeta-GST and endogenous FAK; pulldown assay confirmed ARHGAP21 binds the C-terminal region of FAK. ARHGAP21 binds to PKCzeta phosphorylated on Thr410 in sham and SHR rats, and to FAK phosphorylated on Tyr925 only in SHR. | PMID:18662671 | Biochemical and biophysical research communications |
| 2009 | Medium | Constitutively active Cdc42 or knockdown of the Cdc42-specific GAP ARHGAP21 inhibited retrograde transport of Shiga toxin to the Golgi apparatus. Shiga toxin addition greatly decreases levels of active Cdc42-GTP in an ARHGAP21-dependent manner, demonstrating that ARHGAP21 and Cdc42-based signaling regulates dynein-dependent retrograde transport. | PMID:19692570 | Molecular biology of the cell |
| 2012 | Medium | ARHGAP21 presents GAP activity for RhoA and RhoC in PC3 prostate cancer cells (not just Cdc42), and its depletion results in decreased proliferation and increased migration. ARHGAP21 is localized in the nucleus and cytoplasm of prostate cancer cell lines. | PMID:23200924 | Biochimica et biophysica acta |
| 2012 | Medium | ARHGAP21 is transiently redistributed to cell-cell junctions 4 hours after initiation of cell-cell adhesion, where it interacts with Cdc42 and decreases Cdc42 activity. ARHGAP21 also interacts with α-tubulin and is essential for α-tubulin acetylation during epithelial-mesenchymal transition (EMT). Cells lacking ARHGAP21 show weaker cell-cell adhesions, increased migration, and diminished HGF-induced EMT. | PMID:23235160 | The Journal of biological chemistry |
| 2012 | Medium | ARHGAP21 is post-translationally modified by SUMO2/3; co-immunoprecipitation and in vitro SUMOylation mapped the SUMOylation site to lysine K1443. A 250 kDa modified form of ARHGAP21 is differentially expressed among cell lines and human primary cells. ARHGAP21 co-localizes with SUMO2/3 in cytoplasm and membrane compartments. | PMID:22922005 | FEBS letters |
| 2012 | Medium | ARHGAP21 regulates Cdc42 activity to control transport of influenza virus neuraminidase (NA) to the cell surface. Depletion of ARHGAP21 or expression of constitutively active Cdc42 promoted NA transport to plasma membranes, while overexpression of ARHGAP21 or shRNA targeting Cdc42 decreased cell surface NA. Silencing ARHGAP21 increased influenza A virus replication. | PMID:22318733 | The Journal of biological chemistry |
| 2017 | High | PTEN controls 3D glandular morphogenesis through a membrane-associated β-arrestin1/ARHGAP21/Cdc42 scaffolding complex. PTEN knockdown impairs β-arrestin1 membrane localization and β-arrestin1-ARHGAP21 interactions, reducing Cdc42 activation and disrupting mitotic spindle orientation. Silencing of ARHGAP21 enhanced Cdc42 activation and rescued aberrant morphogenic processes of PTEN-deficient cultures. A membrane-binding defective mutant of PTEN C2 domain abrogated these rescue properties. | PMID:28749339 | eLife |
| 2017 | Medium | Arhgap21 haploinsufficiency in mice leads to enhanced RhoC activity in bone marrow cells, impaired hematopoietic progenitor adhesion, enhanced mobilization of LSK and myeloid progenitors, and reduced erythroid commitment. ARHGAP21 knockdown in human CMP and MEP cells recapitulated decreased erythroid commitment, indicating Arhgap21 functions in hematopoiesis at least partially through RhoC inactivation. | PMID:29212046 | Stem cell research |
| 2015 | Medium | ARHGAP21 co-localizes with actin in MIN6 beta cells and with insulin in neonatal pancreatic islets. Antisense-mediated knockdown of ARHGAP21 reduces F-actin polymerization, increases basal insulin secretion (but not GSIS), increases pERK1/2, and upregulates VAMP2 and SNAP25 gene expression, indicating ARHGAP21 regulates insulin secretion via actin rearrangement and pERK1/2 signaling. | PMID:25744409 | Life sciences |
| 2024 | Medium | In C. elegans, PAC-1/ARHGAP21 is enriched at cell contact sites in a manner dependent on afadin (AFD-1), and genetic interactions indicate afd-1 and pac-1 regulate epidermal morphogenesis through parallel mechanisms. E-cadherin is required for polarized distribution of AFD-1, which in turn promotes PAC-1/ARHGAP21 enrichment at cell contacts. | PMID:38556137 | Developmental biology |
| 2026 | Medium | ARHGAP21 directly binds to filamin A (FLNA) via its PDZ domain interacting with the 1-1200 aa fragment of FLNA. ARHGAP21 also directly binds and recruits HSP90α to stabilize FLNA by inhibiting its ubiquitination and degradation. Overexpression of FLNA reversed the actin cytoskeleton remodeling-related suppression of tumor metastasis caused by ARHGAP21 knockdown in HCC cells. | PMID:41957357 | Cell death discovery |
| 2023 | Low | ARHGAP21 knockdown in NSCLC cells significantly decreased ubiquitination of β-catenin, upregulated N-cadherin, and activated the WNT signaling pathway by affecting expression of APC, GSK3β, and Axin, promoting cell migration and metastasis in vivo. | PMID:37712268 | Nan fang yi ke da xue xue bao |

## Citations

- PMID:17347647
- PMID:18662671
- PMID:19268501
- PMID:19692570
- PMID:21173159
- PMID:22318733
- PMID:22922005
- PMID:23200924
- PMID:23235160
- PMID:25744409
- PMID:28749339
- PMID:29212046
- PMID:37712268
- PMID:38556137
- PMID:41957357
