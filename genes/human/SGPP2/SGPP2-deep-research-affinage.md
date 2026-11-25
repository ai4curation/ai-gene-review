---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/SGPP2
affinage_run_date: 2026-06-10T07:46:31
uniprot_accession: Q8IWX5
self_evaluation_pairwise: win
faith_pct: 80.0
n_discoveries: 14
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for SGPP2 (human)

## Current model (mechanistic narrative)

SGPP2 is a sphingosine-1-phosphate (S1P) phosphohydrolase that dephosphorylates S1P to sphingosine within the sphingolipid recycling pathway, thereby setting the local balance between S1P and sphingosine/ceramide and shaping ER homeostasis, inflammatory tone, and angiogenic signaling across multiple tissues [PMID:27059959]. Genetic loss of Sgpp2 in mice elevates ER stress markers in pancreatic β-cells and impairs adaptive β-cell proliferation under metabolic challenge, establishing a role in maintaining ER homeostasis [PMID:27059959]. By controlling S1P levels, SGPP2 modulates downstream S1P-receptor signaling: its transcriptional induction degrades S1P and suppresses the S1PR1-STAT3-VEGFA angiogenic axis, impairing endothelial tube formation and migration [PMID:41408309], while in lung adenocarcinoma SGPP2 overexpression instead raises intracellular S1P, downregulates SGPP1, and drives GSK3β(Ser9) phosphorylation, β-catenin nuclear translocation, and CyclinD1 induction to promote proliferation and EMT [PMID:41782112]. SGPP2 expression is governed by a network of transcription factors and signals including CEBPD acting downstream of PERK-eIF2α ER stress [PMID:41408309], TFAP2A (which SGPP2 reciprocally inhibits) [PMID:41782112], SP1 [PMID:39514710], and the AnxA1/FPR2-ALX pro-resolution axis [PMID:20862244], and it is repressed post-transcriptionally by miR-31 [PMID:26494556]. In contexts of acute injury and inflammation SGPP2 acts as a promoter of mucosal barrier disruption downstream of inflammatory stimuli [PMID:27130484] and modulates endothelial metabolic reprogramming, mitochondrial respiration, and HIF-1α stability [PMID:37703934].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016787 hydrolase activity, GO:0016740 transferase activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-162582 Signal Transduction, R-HSA-8953897 Cellular responses to stimuli
- **partners:** TFAP2A
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2016 | High | SGPP2 (SPPase 2) is a sphingosine-1-phosphate (S1P) phosphohydrolase that catalyzes dephosphorylation of S1P to sphingosine, functioning in the sphingolipid recycling pathway; Sgpp2 knockout mice exhibit defective adaptive β-cell proliferation following high-fat diet or streptozotocin challenge, and untreated Sgpp2-null β-cells display significantly increased endoplasmic reticulum (ER) stress response proteins compared to wild-type, establishing a role for SGPP2 in maintaining β-cell ER homeostasis and the sphingolipid recycling pathway in pancreatic islets. | PMID:27059959 | The Journal of biological chemistry |
| 2016 | High | Sgpp2 deletion in mice significantly reduced DSS-induced colitis severity; Sgpp2-null mice failed to mount a systemic inflammatory response, exhibited suppressed intestinal epithelial cell apoptosis, improved mucosal barrier integrity, and enhanced E-cadherin expression. SGPP2 knockdown in cultured cells attenuated LPS-induced paracellular permeability, placing SGPP2 as a promoter of mucosal barrier disruption downstream of inflammatory stimuli. | PMID:27130484 | FASEB journal |
| 2010 | Medium | SGPP2 gene expression is upregulated downstream of annexin A1 (AnxA1) activation of the FPR2/ALX receptor in HEK293 cells and human peripheral blood leukocytes; lymph nodes from AnxA1-null mice show lower SGPP2 gene activity, identifying SGPP2 as a downstream genomic target of the AnxA1/FPR2-ALX pro-resolution signaling axis. | PMID:20862244 | PloS one |
| 2012 | Medium | The N-terminal region of FPR2/ALX is dispensable for AnxA1-induced SGPP2 modulation, whereas it is required for AnxA1-mediated induction of JAG1 and JAM3; this domain-mapping establishes that AnxA1 regulation of SGPP2 via FPR2/ALX is independent of the receptor N-terminal domain. | PMID:22610094 | The Journal of biological chemistry |
| 2021 | Medium | NUDT21 positively regulates SGPP2 expression in gastric cancer cells; SGPP2 was identified by RNA-sequencing as a transcriptional target of NUDT21 and shown to mediate NUDT21's tumor-promoting effects on cell proliferation, migration, and invasion. | PMID:34660260 | Frontiers in oncology |
| 2025 | High | CEBPD transcription factor directly binds the SGPP2 promoter and transcriptionally upregulates SGPP2 in endothelial cells; this process is dependent on PERK-eIF2α-mediated ER stress. SGPP2 upregulation degrades S1P, reducing S1PR1-STAT3-VEGFA angiogenic signaling, impairing tube formation, migration, and invasion of HUVECs and contributing to impaired angiogenesis in chronic endometritis. | PMID:41408309 | Journal of translational medicine |
| 2024 | Medium | SP1 transcription factor activates SGPP2 transcription in lung adenocarcinoma cells; SGPP2 knockdown inhibited LADC cell viability and invasion and induced apoptosis in vitro and suppressed tumor growth in vivo; SP1 overexpression rescued the inhibitory effects of SGPP2 shRNA, establishing an SP1→SGPP2 regulatory axis promoting LADC progression. | PMID:39514710 | Anti-cancer drugs |
| 2026 | High | TFAP2A transcription factor directly binds the SGPP2 promoter and transcriptionally activates SGPP2 expression in lung adenocarcinoma; SGPP2 in turn reciprocally inhibits TFAP2A expression. SGPP2 overexpression downregulates SGPP1, increases intracellular S1P, promotes lipid accumulation, and induces phosphorylation of GSK3β at Ser9, leading to β-catenin nuclear translocation and CyclinD1 upregulation, driving proliferation, migration, and EMT in LUAD. | PMID:41782112 | Journal of translational medicine |
| 2026 | Medium | SGPP2 overexpression in neonatal rat cardiomyocytes under oxygen-glucose deprivation (OGD) alleviates cardiomyocyte injury by inhibiting ER stress and activating the SIRT1/AMPK signaling pathway; rescue experiments with the ER stress inducer tunicamycin or the SIRT1 inhibitor EX527 counteracted the protective effects of SGPP2, placing SGPP2 upstream of SIRT1/AMPK in the anti-ER stress pathway in cardiomyocytes. | PMID:41614930 | Current issues in molecular biology |
| 2031 | Medium | In LPS-stimulated human umbilical vein endothelial cells (HUVECs), SGPP2 expression is upregulated; SGPP2 overexpression improved endothelial cell barrier function and enhanced mitochondrial respiration capacity but produced oxidative respiration chain uncoupling, and also inhibited HIF-1α protein degradation, indicating SGPP2 modulates metabolic reprogramming downstream of LPS/inflammatory signaling in endothelial cells. | PMID:37703934 | Free radical biology & medicine |
| 2024 | Medium | SGPP2 knockdown in keratinocytes using siRNA reduces production of inflammatory cytokines IL-1β and IL-8; conditioned media from high-SGPP2-expressing keratinocytes indirectly influences fibroblast extracellular matrix remodeling, establishing a paracrine role for keratinocyte SGPP2 in inflammatory cytokine regulation and ECM remodeling linked to skin aging. | PMID:39194756 | Current issues in molecular biology |
| 2013 | Low | SGPP2 expression in glioblastoma tissues is significantly decreased compared to normal gray matter, and reduced SGPP2 expression is correlated with increased S1P content in glioblastoma; decreased SGPP2 (alongside increased SPHK1) contributes to a metabolic shift favoring S1P over ceramide in glioblastoma, supporting tumor angiogenesis. | PMID:24265321 | The Journal of biological chemistry |
| 2026 | Medium | A regulatory axis involving DKC1 and SOX2 drives expression of SGPP2 in colorectal cancer cells; DKC1-mediated dysregulation of sphingolipid metabolism (involving SGPP2) perturbs very-long-chain fatty acid ceramide levels and promotes chemoresistance. | PMID:42151151 | Nature communications |
| 2015 | Medium | miR-31 directly targets SGPP2 (and Smad4) in gastric cancer cells; increased miR-31 represses SGPP2 at both mRNA and protein levels and is associated with inhibition of GC cell proliferation, promotion of apoptosis, and attenuation of migration linked to downregulation of STAT3. | PMID:26494556 | Cancer gene therapy |

## Citations

- PMID:20862244
- PMID:22610094
- PMID:24265321
- PMID:26494556
- PMID:27059959
- PMID:27130484
- PMID:34660260
- PMID:37703934
- PMID:39194756
- PMID:39514710
- PMID:41408309
- PMID:41614930
- PMID:41782112
- PMID:42151151
