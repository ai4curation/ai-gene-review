---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AURKA
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: O14965
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 29
citation_count: 28
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AURKA (human)

## Current model (mechanistic narrative)

AURKA is a cell-cycle-regulated serine/threonine kinase that accumulates at G2/M and localizes to the spindle pole from prophase through anaphase, where it governs centrosome function and chromosome segregation [PMID:9153231]; its amplification and overexpression in tumors drives centrosome amplification, aneuploidy, and oncogenic transformation [PMID:9174055, PMID:9771714]. Catalytic activity is switched on by phosphorylation of Threonine 288 in the activation loop and switched off by PP1, with which AURKA forms a reciprocal regulatory loop—activated kinase phosphorylates and inhibits PP1, while PP1 dephosphorylates and inactivates the kinase [PMID:11039908, PMID:11551964]. Distinct cofactors engage AURKA at separable sites to direct its localized functions: a crystal structure of AURKA bound to CEP192 Helix-1 defines a centrosomal regulatory interface distinct from the TPX2 binding site [PMID:37083534], and TPX2 co-overexpression additionally drives AURKA into the interphase nucleus [PMID:36797043]. AURKA abundance is set by opposing ubiquitin machinery—the APC/C-FZR1 axis (modulated by PRL-3-mediated FZR1 dephosphorylation) and stabilizing/destabilizing E3 activity of CBLC, counterbalanced by the deubiquitinase USP21 [PMID:30498084, PMID:35149839, PMID:36919585]. Beyond mitosis, AURKA acts kinase-independently in the nucleus by partnering with hnRNP K to transactivate MYC and promote a cancer stem cell phenotype [PMID:26782714], and as a kinase it phosphorylates substrates that rewire tumor-relevant signaling: HDM2/MDM2 to suppress p53 [PMID:24240108], KEAP1 to activate NRF2 and suppress ferroptosis [PMID:38642502], and SPOP to stabilize androgen receptor and c-Myc [PMID:33158056]. It is also embedded in feedback circuits with metabolic and transcriptional regulators, including mitochondrial ATP synthase subunits that couple it to cell-cycle and metabolic fate [PMID:37386025].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016740 transferase activity, GO:0140110 transcription regulator activity
- **localization:** GO:0005815 microtubule organizing center, GO:0005634 nucleus, GO:0005856 cytoskeleton, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle, R-HSA-74160 Gene expression (Transcription), R-HSA-1643685 Disease
- **partners:** TPX2, CEP192, PP1, CDC20, HNRNP K, MDM2, KEAP1, SPOP
- **complexes:** APC/C-FZR1

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1997 | Medium | AURKA (BTAK) encodes a serine/threonine kinase localized on chromosome 20q13 with homology to yeast Ipl1 and Drosophila Aurora, both involved in chromosome segregation; the gene is amplified and overexpressed in breast tumor cell lines. | PMID:9174055 | Oncogene |
| 1997 | High | AURKA (Aik) protein is cell-cycle regulated, accumulates during G2/M and decreases after mitosis, localizes to the spindle pole from prophase through anaphase, and exhibits kinase activity (casein phosphorylation) enhanced at mitosis. | PMID:9153231 | The Journal of biological chemistry |
| 1998 | High | Ectopic overexpression of AURKA (STK15/BTAK) in mouse NIH 3T3 cells and near-diploid human breast epithelial cells induces centrosome amplification, aneuploidy, and oncogenic transformation, defining AURKA as a centrosome-associated kinase whose overexpression drives chromosomal instability. | PMID:9771714 | Nature genetics |
| 1999 | Medium | AURKA (Aurora2/Aik) associates with the cell cycle regulator Cdc20 in HeLa cells; Cdc20-associated kinase activity peaks in early M phase, identifying Cdc20 as an AURKA-interacting protein at mitotic spindle poles. | PMID:10377410 | Proceedings of the National Academy of Sciences of the United States of America |
| 2000 | High | AURKA (Aurora2) is activated by phosphorylation of Threonine 288 within the activation loop; this phosphorylation increases enzymatic activity and can be catalyzed by PKA in vitro. Protein phosphatase 1 (PP1) dephosphorylates T288 and inactivates AURKA in vitro; in vivo T288 phosphorylation is induced by okadaic acid. Additionally, AURKA is degraded via the proteasome, and T288-phosphorylated AURKA may be targeted for mitotic degradation. | PMID:11039908 | Oncogene |
| 2001 | High | AURKA (STK15) contains two functional PP1-binding sites; STK15 and PP1 interact in a cell-cycle-dependent manner peaking at mitosis. Activated STK15 phosphorylates PP1 and inhibits its phosphatase activity in vitro and in vivo. Conversely, PP1 dephosphorylates and inactivates STK15. Non-binding STK15 mutants are superphosphorylated but have reduced kinase activity, and cells expressing these mutants show aberrant chromosome alignment. | PMID:11551964 | The Journal of biological chemistry |
| 2013 | High | AURKA directly interacts with and phosphorylates HDM2 (MDM2) in vitro; this leads to P53 ubiquitination and attenuation of cisplatin-induced P53 activation in gastric cancer cells, promoting cell survival. | PMID:24240108 | Clinical cancer research |
| 2014 | Medium | AURKA promotes STAT3 transcriptional activity through regulation of JAK2 expression and phosphorylation; overexpression of AURKA increases STAT3 Tyr705 phosphorylation and STAT3 nuclear translocation, whereas AURKA knockdown reduces these effects. Inhibition of JAK2 in the presence of AURKA overexpression abrogates AURKA-mediated STAT3 activation, establishing the AURKA-JAK2-STAT3 axis. | PMID:24953013 | Molecular oncology |
| 2014 | Medium | SMAD4 binds to AURKA and induces its proteasomal degradation in a TGFβ-independent manner, thereby suppressing AURKA-mediated β-catenin/TCF transcriptional activity and metastatic phenotypes. | PMID:25061104 | Molecular cancer research |
| 2016 | High | In the nucleus, AURKA translocates from centrosomes and performs kinase-independent oncogenic functions by interacting with hnRNP K to form a transcriptional complex that shifts MYC promoter usage and activates MYC transcription, thereby enhancing breast cancer stem cell phenotype. Blocking AURKA nuclear localization inhibits this transactivating function. | PMID:26782714 | Nature communications |
| 2018 | High | ARID1A occupies the AURKA gene promoter and negatively regulates AURKA transcription; loss of ARID1A results in enhanced AURKA transcription leading to persistent CDC25C activation and G2/M dysregulation, creating a synthetic lethal interaction exploitable therapeutically. | PMID:30097580 | Nature communications |
| 2018 | High | PRL-3 phosphatase interacts with AURKA and promotes its ubiquitination and proteasomal degradation by dephosphorylating FZR1, thereby activating the APC/C-FZR1 complex which targets AURKA. | PMID:30498084 | Cancer research |
| 2018 | High | AURKA directly phosphorylates SPOP at three sites, causing SPOP ubiquitination and degradation; SPOP in turn degrades AURKA via a feedback loop. AURKA-mediated SPOP degradation stabilizes androgen receptor (AR), ARv7, and c-Myc, driving castration-resistant prostate cancer progression. | PMID:33158056 | Cancers |
| 2019 | Medium | CEP41-mediated tubulin glutamylation of cilia activates AURKA and upregulates VEGFA/VEGFR2 expression through HIF1α during endothelial cell responses to shear stress or hypoxia, driving angiogenesis and cilia disassembly (deciliation). | PMID:31885126 | EMBO reports |
| 2020 | Medium | AURKA kinase activity is required for the maintenance of ring-like aMTOC (acentriolar microtubule-organizing center) organization in mouse oocytes; inhibition of AURKA causes loss of aMTOC ring structure, CEP215 clustering at spindle poles, and shorter spindles with highly focused poles. | PMID:31895686 | Reproduction (Cambridge, England) |
| 2021 | High | AURKA deletion in spermatogonia eliminates all developing germ cells (consistent with its mitotic role), while deletion in spermatocytes increases spermatocyte apoptosis, elevates abnormal sperm morphology, and increases progressive sperm motility with decreased PP1 activity in sperm lysate. | PMID:34518881 | Biology of reproduction |
| 2022 | High | CBLC (an E3 ubiquitin ligase) interacts with the kinase domain of AURKA and stabilizes it by conjugating monoubiquitination and K11/K63-linked polyubiquitination, protecting AURKA from degrading K11/K48 polyubiquitination. CBLC depletion decreases AURKA half-life and delays AURKA accumulation/activation during mitotic entry. | PMID:35149839 | Oncogene |
| 2023 | Medium | AURKA functionally interacts with mitochondrial ATP synthase subunits ATP5F1A and ATP5F1B (Complex V core subunits); disruption of this AURKA/ATP5F1A/ATP5F1B nexus triggers G0/G1 arrest accompanied by decreased glycolysis and mitochondrial respiration, with cell fate outcome dependent on the metabolic propensity of triple-negative breast cancer cells. | PMID:37386025 | Cell death discovery |
| 2023 | Medium | AURKA directly interacts with and phosphorylates KEAP1, thereby activating NRF2 and its target gene transcription, suppressing ferroptosis in meningioma; FOXM1 transcriptionally induces AURKA expression in this context. | PMID:38642502 | Redox biology |
| 2023 | High | The crystal structure of AURKA bound to a conserved helix (Helix-1) from CEP192 reveals a distinct binding site on AURKA that is different from the TPX2 binding site; disrupting the CEP192 Helix-1/AURKA interaction in cells causes mitotic defects, establishing the structural basis for centrosomal AURKA regulation distinct from spindle-microtubule regulation by TPX2. | PMID:37083534 | Science advances |
| 2023 | Medium | AURKA interacts with DDX5 to form a transcriptional coactivator complex that induces transcription of the lncRNA TMEM147-AS1, which in turn sponges hsa-let-7b/7c-5p to upregulate AURKA in a positive feedback loop maintaining cisplatin resistance via lipophagy activation in ovarian cancer. | PMID:37217070 | Cancer letters |
| 2023 | Medium | CD73/NT5E directly interacts with AURKA (confirmed by co-IP and molecular docking) and inhibits AURKA ubiquitination; overexpression of CD73/NT5E stabilizes AURKA, downregulates p53 signaling, and regulates hepatic stellate cell activation and senescence in alcohol-related liver fibrosis. | PMID:36778123 | International journal of biological sciences |
| 2023 | Medium | TPX2 co-overexpression promotes AURKA nuclear accumulation in interphase, whereas AURKA overexpression alone is insufficient for nuclear accumulation. Nuclear export and proteasome activity also regulate nuclear AURKA levels. Nuclear AurkA driven by TPX2 co-overexpression promotes pro-tumorigenic processes in MCF10A mammospheres. | PMID:36797043 | Life science alliance |
| 2023 | Medium | USP21 deubiquitinase directly interacts with AURKA (confirmed by co-IP and GST-pulldown) and deubiquitinates AURKA to restore its activity and stability; USP21 knockdown increases AURKA ubiquitination and suppresses laryngeal cancer cell proliferation, migration, and invasion. | PMID:36919585 | The Kaohsiung journal of medical sciences |
| 2021 | Medium | AURKA inhibition suppresses differentiation of THP-1 AML cells by repressing KDM6B (H3K27 demethylase) expression; AURKA and YY1 co-occupy the KDM6B promoter region. Alisertib-mediated AURKA inhibition dissociates this complex, upregulates KDM6B, and drives THP-1 differentiation into monocytes. This effect is blocked by the KDM6B inhibitor GSK-J4. | PMID:29477140 | Molecules and cells |
| 2018 | Medium | AURKA promotes STAT3 activity through regulation of JAK2; pharmacological AURKA inhibition (MLN8237) decreases HDM2 protein levels, induces P53 transcriptional activity, and reduces cell survival in vitro and xenograft tumor growth in vivo in gastric cancer models. | PMID:24240108 | Clinical cancer research |
| 2021 | Medium | AURKA inhibition in Ewing's sarcoma cells induces apoptosis and ferroptosis through the NPM1/YAP1 axis; co-immunoprecipitation confirmed AURKA-NPM1 interaction, and AURKA inhibition disrupts this complex. | PMID:38287009 | Cell death & disease |
| 2023 | Medium | HMMR interacts with AURKA and inhibits its ubiquitination-mediated degradation, elevating AURKA protein levels and subsequently activating the mTORC2/AKT pathway to drive prostate cancer progression; E2F1, upregulated by mTORC2/AKT, transcriptionally promotes HMMR expression, forming a positive feedback loop. | PMID:36750558 | Cell death discovery |
| 2021 | Medium | AURKA promotes psoriasis-related inflammation by blocking autophagy-mediated suppression of the AIM2 inflammasome, acting through activation of the AKT/mTOR pathway; AURKA knockdown inhibits AIM2 inflammasome activation and enhances autophagy, while autophagy inhibition (3-MA) attenuates these effects. | PMID:34710506 | Immunology letters |

## Citations

- PMID:10377410
- PMID:11039908
- PMID:11551964
- PMID:24240108
- PMID:24953013
- PMID:25061104
- PMID:26782714
- PMID:29477140
- PMID:30097580
- PMID:30498084
- PMID:31885126
- PMID:31895686
- PMID:33158056
- PMID:34518881
- PMID:34710506
- PMID:35149839
- PMID:36750558
- PMID:36778123
- PMID:36797043
- PMID:36919585
- PMID:37083534
- PMID:37217070
- PMID:37386025
- PMID:38287009
- PMID:38642502
- PMID:9153231
- PMID:9174055
- PMID:9771714
