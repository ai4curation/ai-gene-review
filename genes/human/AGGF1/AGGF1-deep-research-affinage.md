---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AGGF1
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q8N302
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 25
citation_count: 25
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AGGF1 (human)

## Current model (mechanistic narrative)

AGGF1 is a secreted angiogenic factor that drives vascular development, vessel integrity, and tissue protection by engaging integrin receptors on the vascular wall while also performing distinct nuclear functions in RNA processing and tumor suppression [PMID:34551592, PMID:27522498, PMID:29885663]. On endothelial cells it signals through integrin α5β1 via an angiogenic motif mapped to residues 604–613 (FQRDDAPAS), activating FAK–Src–AKT and the PI3K p110α/p85α–AKT–GSK3β–p70S6K axis, and it stabilizes endothelial junctions by suppressing VE-cadherin phosphorylation [PMID:34551592, PMID:27522498]. AGGF1-driven angiogenesis additionally requires JNK-dependent assembly of the Becn1–Vps34–Atg14 autophagy complex [PMID:27513923]. On vascular smooth muscle cells AGGF1 acts through integrin α7 (ITGA7) via the same RDDAPAS motif to inhibit MEK1/2–ERK1/2–Elk signaling, sustain the myocardin/SRF contractile program, and suppress neointimal formation; it further enhances integrin α7 binding to LAP–TGF-β1, blocking maturation of TGF-β1 and limiting Smad2/3 activation to attenuate aortic aneurysm [PMID:35202649, PMID:28649088, PMID:37081014]. In developmental settings AGGF1 specifies venous identity and acts high in the hemangioblast hierarchy upstream of scl/fli1/etsrp and of npas4l and mTOR–S6K–Emp2 signaling [PMID:23197652, PMID:24277077, PMID:37881938]. In the nucleus, AGGF1 is a structural component of paraspeckles that nucleates the NONO/PSF/PSPC1/NEAT1 core and functions as a broad alternative-splicing regulator, promoting SRSF6 exon-3 skipping to generate the angiogenically active full-length isoform [PMID:29885663, PMID:40035560]. As a tumor suppressor, AGGF1 binds p53 and MDM2 through its FHA domain to inhibit p53 ubiquitination and stabilize p53, an activity abolished by somatic FHA-domain variants [PMID:33069768]. AGGF1 expression is transcriptionally activated by GATA1 and by NF-κB p65 downstream of AngII/AT1R and HIF-1α, and is post-transcriptionally repressed by miR-27a under hypoxia [PMID:19556247, PMID:29641288, PMID:39905000, PMID:24462738]. Across fibrotic, inflammatory, and atrophic contexts AGGF1 dampens NF-κB and TGF-β/SMAD signaling, forming a complex with SMAD7 and interacting with NF-κB and with TWEAK to restrain pathological responses [PMID:26850475, PMID:23628701, PMID:28958996, PMID:36696895].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0048018 receptor ligand activity, GO:0060089 molecular transducer activity, GO:0003723 RNA binding, GO:0098772 molecular function regulator activity, GO:0140110 transcription regulator activity
- **localization:** GO:0005654 nucleoplasm, GO:0005634 nucleus, GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-8953854 Metabolism of RNA, R-HSA-9612973 Autophagy, R-HSA-1266738 Developmental Biology, R-HSA-1474244 Extracellular matrix organization
- **partners:** ITGA5, ITGB1, ITGA7, TP53, MDM2, SMAD7, NONO, TNFSF12
- **complexes:** paraspeckle (NONO/PSF/PSPC1/NEAT1), Becn1–Vps34–Atg14 autophagy complex, AGGF1–SMAD7 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | High | Integrin α5β1 is the receptor for AGGF1 on endothelial cells. AGGF1 interacts with α5β1 and activates FAK, Src, and AKT. The angiogenic domain of AGGF1 was mapped to amino acids 604–613 (FQRDDAPAS), required for EC adhesion, migration, capillary tube formation, and AKT activation. | PMID:34551592 | Arteriosclerosis, thrombosis, and vascular biology |
| 2022 | High | AGGF1 interacts with integrin α7 (ITGA7) on vascular smooth muscle cells (VSMCs) via the RDDAPAS motif. This interaction is required for AGGF1-mediated VSMC phenotypic switching, inhibition of MEK1/2–ERK1/2–ELK phosphorylation, upregulation of contractile markers (MYH11, α-SMA, SM22), and attenuation of neointimal formation after vascular injury. | PMID:35202649 | The Journal of biological chemistry |
| 2023 | High | AGGF1 enhances the interaction between its receptor integrin α7 and latency-associated peptide (LAP)-TGF-β1, thereby blocking cleavage of LAP-TGF-β1 to mature TGF-β1 and inhibiting Smad2/3 and ERK1/2 phosphorylation in VSMCs, attenuating thoracic aortic aneurysm. | PMID:37081014 | Nature communications |
| 2016 | High | AGGF1 activates autophagy in endothelial cells by activating JNK, which leads to activation of Vps34 lipid kinase and assembly of the Becn1–Vps34–Atg14 complex. Autophagy is required for AGGF1-mediated EC proliferation, migration, capillary tube formation, and therapeutic angiogenesis. | PMID:27513923 | PLoS biology |
| 2016 | High | AGGF1 promotes angiogenesis by activating the catalytic p110α subunit and p85α regulatory subunit of PI3K, leading to AKT, GSK3β, and p70S6K activation. AGGF1 also inhibits VE-cadherin phosphorylation and increases its plasma membrane localization, thereby maintaining vascular integrity. | PMID:27522498 | Human molecular genetics |
| 2012 | High | AGGF1 is required for venous identity specification in zebrafish embryos. AGGF1 activates AKT, and constitutively active AKT rescues the loss of venous markers (flt4, ephb4, dab2) caused by AGGF1 knockdown, establishing AGGF1-AKT signaling as responsible for venous cell fate. | PMID:23197652 | Human molecular genetics |
| 2013 | High | Aggf1 acts upstream of scl, fli1, and etsrp in the genetic hierarchy for hemangioblast specification in zebrafish. Knockdown of aggf1 reduces expression of hemangioblast markers (fli1, etsrp, lmo2, scl) and impairs both primitive and definitive hematopoiesis; the defects are rescued by mRNA for scl, fli-vp16, or etsrp. | PMID:24277077 | Blood |
| 2023 | High | Aggf1 acts upstream of npas4l (cloche) and the mTOR–S6K pathway in hemangioblast specification. Aggf1 knockout reduces mTOR and p70 S6K phosphorylation, resulting in reduced Emp2 protein synthesis. Emp2 knockout impairs hemangioblast specification and angiogenesis by increasing ERK1/2 phosphorylation. mTOR activator MHY1485 rescues hemangioblast defects caused by aggf1 knockdown. | PMID:37881938 | Arteriosclerosis, thrombosis, and vascular biology |
| 2017 | High | AGGF1 inhibits neointimal formation after vascular injury by regulating VSMC phenotypic switching through a MEK1/2–ERK1/2–Elk–myocardin–SRF/p27 signaling pathway. AGGF1 blocks PDGF-BB-induced MEK1/2, ERK1/2, and Elk phosphorylation; inhibits synthetic phenotype switching; and maintains the myocardin/SRF/CArG-box complex. Overexpression of Elk abolishes the effect of AGGF1. | PMID:28649088 | Journal of the American Heart Association |
| 2020 | High | AGGF1 antagonizes MDM2 to inhibit p53 ubiquitination, increases p53 acetylation, phosphorylation, stability, and expression, and activates p53 target genes. AGGF1 interacts with p53 through its FHA domain. Somatic AGGF1 variants in the FHA domain (p.Q467H, p.Y469N, p.N483T) abolish this tumor-suppressive activity. | PMID:33069768 | Cancer letters |
| 2016 | High | Aggf1 regulates liver fibrosis by forming a complex with SMAD7, thereby reducing SMAD3 binding to pro-fibrogenic gene promoters. Aggf1 expression is silenced during HSC activation by DNA methylation, and treatment with the DNA methyltransferase inhibitor 5-Azacytidine restores Aggf1 expression and represses fibrosis in an Aggf1-dependent manner. | PMID:26850475 | Biochimica et biophysica acta |
| 2013 | High | AGGF1 suppresses TNF-α-induced endothelial activation by antagonizing the ERK/NF-κB pathway. AGGF1 decreases NF-κB p65 promoter activity, nuclear distribution, and phosphorylation, and increases IκBα levels. The FHA domain of AGGF1 is required for this anti-inflammatory effect. | PMID:23628701 | Cellular signalling |
| 2009 | High | GATA1 directly binds to the AGGF1 promoter (at the consensus GATA1 site -295 to -300) and transcriptionally activates AGGF1 expression. A rare KTS-associated polymorphism (-294C>T) disrupts GATA1 binding and abolishes its stimulatory effect. Knockdown of GATA1 reduces AGGF1 expression and causes endothelial cell apoptosis and impaired capillary formation, phenotypes rescued by recombinant AGGF1 protein. | PMID:19556247 | The Journal of biological chemistry |
| 2018 | High | Angiotensin II induces AGGF1 expression through NF-κB: p65 binds directly to the AGGF1 promoter. AT1R mediates AngII-induced AGGF1 upregulation (blocked by losartan), whereas AT2R inhibition further increases it. AGGF1 is required for AngII-induced angiogenesis, as siRNA for RELA/p65 or AGGF1 blocks AngII-induced tube formation, and AGGF1 rescues the effect of RELA siRNA. | PMID:29641288 | FASEB journal |
| 2019 | Medium | AGGF1 activates AKT, reduces nuclear localization of Fyn, which increases nuclear Nrf2 and expression of antioxidative genes, thereby inhibiting reactive oxygen species generation in endothelial progenitor cells (EPCs). This mechanism underlies AGGF1's reversal of hyperglycemia-induced EPC dysfunction. | PMID:31092480 | Diabetes |
| 2017 | Medium | Aggf1 interacts with NF-κB and blocks its binding to the Ccl2 gene promoter in hepatocytes, repressing Ccl2 (MCP-1) transcription and thereby attenuating macrophage chemotaxis and hepatic stellate cell activation. | PMID:28958996 | Journal of biomedical research |
| 2014 | Medium | Hypoxia down-regulates AGGF1 protein (but not mRNA) by inducing miR-27a expression, which suppresses AGGF1 through translational inhibition (not RNA degradation). Inhibition of miR-27a prevents hypoxia-induced AGGF1 down-regulation. | PMID:24462738 | Biochimica et biophysica acta |
| 2023 | High | AGGF1 interacts with TWEAK (TNF-like weak inducer of apoptosis), reducing the interaction between TWEAK and its receptor Fn14. This inhibits Fn14-induced NF-κB p65 phosphorylation and reduces expression of MuRF1 (muscle RING finger 1 E3 ubiquitin ligase), resulting in increased MyHC and α-actin. AGGF1 also promotes autophagy in atrophic muscles by activating JNK. | PMID:36696895 | Journal of cachexia, sarcopenia and muscle |
| 2025 | High | AGGF1 is a general alternative splicing factor regulating splicing of 436 genes. Specifically, AGGF1 promotes skipping of exon 3 in SRSF6 pre-mRNA to produce the full-length SRSF6 protein. Full-length SRSF6 is required for endothelial cell proliferation, migration, and capillary tube formation, and rescues the angiogenic defects caused by AGGF1 silencing. | PMID:40035560 | FASEB journal |
| 2022 | High | AGGF1 is a structural and regulatory component of paraspeckles. It forms an outer rim around the NONO/PSF/PSPC1/NEAT1 core and induces paraspeckle formation. AGGF1 interacts with NONO, PSF, and HNRNPK, upregulates the NEAT1_2 transcript, and interacts with NEAT1 RNA (RNA-IP). AGGF1 also regulates alternative RNA splicing (decreases exon skipping/inclusion ratio in a CD44 model) and forms additional AGGF1-positive nuclear condensates (AGGF1-bodies) consistent with liquid-liquid phase separation. | PMID:35608889 | FASEB journal |
| 2018 | Medium | Exogenous AGGF1 attenuates neuroinflammation and BBB disruption after subarachnoid hemorrhage via the PI3K/Akt/NF-κB pathway: AGGF1 increases PI3K, p-Akt, VE-cadherin, Occludin, and Claudin-5 expression, and decreases p-NF-κB p65, TNF-α, and IL-1β. The protective effects are abolished by the PI3K inhibitor LY294002 and by AGGF1 siRNA knockdown. | PMID:29885663 | Journal of neuroinflammation |
| 2025 | Medium | HIF-1α directly regulates AGGF1 expression in endothelial cells under ischemic conditions. AGGF1 upregulates cell cycle protein expression by increasing binding of TNFSF12 (TWEAK) to its receptor FN14 (TNFRSF12A), promoting retinal angiogenesis. | PMID:39905000 | Nature communications |
| 2007 | Low | AGGF1 interacts with inhibitor of differentiation 1 (Id1) as identified by yeast two-hybrid screening of an adult human lung cDNA library, confirmed by reporter gene activation and Western blotting. | PMID:17884784 | Nan fang yi ke da xue xue bao |
| 2018 | Low | Down-regulation of AGGF1 by siRNA inhibits DNA damage repair markers (phospho-γH2AX and phospho-NBS1) in cisplatin-treated colon cancer cells, and AGGF1 co-localizes with γH2AX at sites of double-strand DNA breaks, suggesting a role in DNA damage repair. AGGF1 knockdown increases chemosensitivity to cisplatin. | PMID:33168501 | Nan fang yi ke da xue xue bao |
| 2020 | Medium | Aggf1 3' UTR acts as a trans-regulatory element by competing with Mcl1 mRNA for the same miRNAs (miR-105, miR-101, miR-93) via their 3' UTRs, co-regulating expression of both Aggf1 and Mcl1 proteins in cardiomyocytes during angiotensin II-induced cardiac dysfunction. | PMID:32061268 | Molecular therapy |

## Citations

- PMID:17884784
- PMID:19556247
- PMID:23197652
- PMID:23628701
- PMID:24277077
- PMID:24462738
- PMID:26850475
- PMID:27513923
- PMID:27522498
- PMID:28649088
- PMID:28958996
- PMID:29641288
- PMID:29885663
- PMID:31092480
- PMID:32061268
- PMID:33069768
- PMID:33168501
- PMID:34551592
- PMID:35202649
- PMID:35608889
- PMID:36696895
- PMID:37081014
- PMID:37881938
- PMID:39905000
- PMID:40035560
