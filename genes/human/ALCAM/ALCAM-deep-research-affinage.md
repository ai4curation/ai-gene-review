---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ALCAM
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q13740
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 41
citation_count: 41
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ALCAM (human)

## Current model (mechanistic narrative)

ALCAM (CD166) is a transmembrane immunoglobulin-superfamily cell adhesion molecule that engages in strong heterophilic binding to CD6 (KD ~0.4–1 µM) through its membrane-distal N-terminal Ig domain and weaker homophilic ALCAM–ALCAM interactions (KD ~29–48 µM) [PMID:7760007, PMID:15048703, PMID:26146185]. Homophilic adhesion is biphasic: the N-terminal Ig domain mediates ligand binding, while membrane-proximal Ig domains drive clustering that controls avidity [PMID:11306570]. Crystal structures of the CD6 SRCR domains bound to the two N-terminal ALCAM Ig domains define the interface, and native mass spectrometry shows that heterophilic CD6–ALCAM and homophilic ALCAM–ALCAM engagement compete [PMID:26146185]. Intracellularly, ALCAM is recruited to cell-cell contacts by α-catenin and couples to the actin cortex; this linkage does not alter individual bond affinity but stiffens the cortex and strengthens overall adhesion to CD6 at the immunological synapse [PMID:10673383, PMID:24496453]. ALCAM surface levels are dynamically controlled by clathrin-mediated endocytosis with recycling, an endophilin-A3/galectin-8-driven clathrin-independent pathway, and ADAM17-mediated ectodomain shedding that is induced by TGF-β and restrained by the tetraspanin CD9 [PMID:15769845, PMID:32193381, PMID:27130882, PMID:24385212, PMID:23052204]. Through CD6–ALCAM engagement at the immunological synapse, ALCAM sustains DC-induced T-cell proliferation and is required for γδ T cell activation [PMID:16352806, PMID:16818742]. In vivo, ALCAM is required for hematopoietic stem cell self-renewal and engraftment, lymphatic network formation and dendritic cell migration, blood-brain barrier tight-junction integrity and leukocyte transmigration, and intestinal stem cell niche maintenance via Wnt signaling [PMID:23280653, PMID:23169771, PMID:28069965, PMID:28462380]. In cancer, ALCAM controls MMP-2 activation through MT1-MMP processing and promotes survival signaling through PI3K/AKT–YAP and AKT–FOXO axes [PMID:16204050, PMID:24482231, PMID:24891117]. ALCAM additionally serves as a binding partner for ILT3 (LILRB4), galectin-8, and S100B, and its expression is regulated transcriptionally by NF-κB and HIF-1α and post-translationally by the E3 ligase CHIP and by PRMT1 [PMID:29263213, PMID:27130882, PMID:23729438, PMID:21572107, PMID:38956900, PMID:28279658, PMID:27175582].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098631 cell adhesion mediator activity, GO:0060089 molecular transducer activity
- **localization:** GO:0005886 plasma membrane, GO:0031410 cytoplasmic vesicle, GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-168256 Immune System, R-HSA-1500931 Cell-Cell communication, R-HSA-162582 Signal Transduction, R-HSA-5653656 Vesicle-mediated transport, R-HSA-1643685 Disease
- **partners:** CD6, CD9, ADAM17, LILRB4, LGALS8, S100B, SOSTDC1, CTNNA1
- **complexes:** immunological synapse

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1995 | High | ALCAM (CD166) was identified as a ligand for CD6: COS cells transfected with ALCAM cDNA bound a CD6 immunoglobulin fusion protein (CD6-Rg), and an ALCAM-Rg fusion protein bound COS cell transfectants expressing CD6, establishing a direct heterophilic ALCAM–CD6 receptor–ligand interaction. | PMID:7760007 | The Journal of experimental medicine |
| 1997 | High | The CD6-binding site of ALCAM maps to the N-terminal Ig-like domain, and mutagenesis of hALCAM identified residues critical for CD6 binding on the predicted A'GFCC'C" β-sheet of this domain; all critical residues are conserved in mouse ALCAM, explaining cross-species CD6/ALCAM interaction. | PMID:9209500 | European journal of immunology |
| 1998 | Medium | ALCAM (MEMD) mediates homophilic (ALCAM–ALCAM) cell-cell clustering in CD6-negative melanoma cells; transfection of ALCAM into ALCAM-negative melanoma cells restored cell-cell interaction, demonstrating that ALCAM expression is sufficient for homophilic adhesion in this context. | PMID:9502422 | The American journal of pathology |
| 2000 | High | CD6–CD166 heterophilic interaction has a KD of ~0.4–1.0 µM with fast off-rate (Koff ≥0.4 s⁻¹); homophilic ALCAM–ALCAM interaction is ~100-fold weaker (KD ~29–48 µM, Koff ≥5.3 s⁻¹), demonstrating that heterophilic binding is substantially stronger than homophilic binding. | PMID:15048703 | European journal of immunology |
| 2000 | Medium | α-catenin is required to recruit ALCAM to cell–cell contacts; prostate cancer cell lines lacking α-catenin show cytoplasmic ALCAM staining, whereas transfection of α-N-catenin restores ALCAM localization to cell-cell junctions alongside E-cadherin. | PMID:10673383 | Biochemical and biophysical research communications |
| 2001 | High | Homophilic ALCAM–ALCAM cell adhesion requires two structurally and functionally distinct modules: (1) ligand binding mediated by the membrane-distal N-terminal Ig domain, and (2) avidity control through ALCAM clustering involving membrane-proximal Ig domains. A transmembrane deletion mutant lacking the ligand-binding domain inhibited cell-cell adhesion by interfering with ALCAM avidity without affecting soluble homophilic ligand binding. | PMID:11306570 | The Journal of biological chemistry |
| 2001 | Medium | ALCAM expression on yolk sac endothelium supports hematopoietic progenitor cell development; ALCAM-transfected adult endothelial cells (EOMA) supported hematopoietic progenitor development compared to vector controls, and ALCAM was found to be involved in capillary tube formation and hemangioblast differentiation. | PMID:11568000 | Blood |
| 2004 | High | CD6–ALCAM interactions are required not only for establishing initial DC–T-cell contact but also for sustaining T-cell proliferation; ALCAM-blocking antibodies and recombinant ALCAM-Fc proteins strongly and sustainably inhibited DC-induced T-cell proliferation, and simultaneous crosslinking of CD6 and CD3 induced proliferation comparable to CD3+CD28 co-stimulation. | PMID:16352806 | Blood |
| 2005 | High | ALCAM controls MMP-2 activation in melanoma: truncation of ALCAM (dominant-negative) severely impaired pro-MMP-2 activation by reducing MT1-MMP transcript levels and impairing MT1-MMP processing. ALCAM depletion by RNAi recapitulated this failure of the proteolytic cascade mainly through incomplete MT1-MMP processing. Extensive cell–cell contacts, wild-type ALCAM, and cell–matrix interactions were all required for efficient MMP-2 activation. | PMID:16204050 | Cancer research |
| 2005 | High | ALCAM undergoes ligand engagement-induced internalization via a clathrin-mediated pathway (colocalizing with clathrin but not caveolin) and recycles back to the cell surface, as shown by surface biotinylation and recycling assays. This endocytic pathway enables intracellular delivery of ALCAM-targeted immunotoxins. | PMID:15769845 | Journal of cell science |
| 2006 | High | CD6 and CD166 are recruited together to the center of the immunological synapse between γδ T cells and antigen-loaded tumor cells, colocalizing with γδ TCR/CD3. CD166 transfection into a CD166-negative tumor line markedly enhanced γδ T cell activation, while shRNA-mediated CD166 knockdown reduced it, demonstrating that CD6–CD166 engagement at the synapse is required for γδ T cell activation by nonpeptide antigen-presenting tumor cells. | PMID:16818742 | Journal of immunology |
| 2006 | Medium | ALCAM gene silencing in breast cancer cells (MCF-7) reduced BCL-2 protein levels and triggered apoptosis (caspase-7 activation, PARP cleavage) and autophagy (MAP1LC3, Beclin1 upregulation), indicating ALCAM supports cell survival downstream of BCL-2. | PMID:16865058 | Medical science monitor |
| 2007 | Medium | NDRG2 expressed in dendritic cells prevents down-regulation of ALCAM during monocyte-to-DC differentiation; NDRG2 siRNA knockdown specifically reduced ALCAM expression in differentiating DCs and diminished their ability to induce T cell proliferation, while NDRG2 overexpression in U937 cells conferred resistance to GM-CSF/IL-4-induced ALCAM reduction. | PMID:17911180 | Journal of leukocyte biology |
| 2008 | High | DM-GRASP/ALCAM/CD166 is required for cardiac morphogenesis in Xenopus laevis; loss-of-function reduced expression of first-heart-field markers (Tbx20, TnIc) but not second-heart-field markers (Isl-1, BMP-4), caused defective cell adhesion and cardiac morphogenesis, and DM-GRASP expression rescued the phenotype caused by loss of non-canonical Wnt11-R signaling, demonstrating functional coupling between ALCAM and Wnt11-R during cardiac development. | PMID:18598690 | Developmental biology |
| 2011 | Medium | NF-κB P50/P65 heterodimer activates both CD166/ALCAM and miR-9-1 transcription after serum deprivation. miR-9, induced with a delay, represses ALCAM protein translation via its 3'-UTR, creating a negative auto-regulatory loop. miR-9 also promotes cell migration partly via inhibition of CD166. | PMID:21572107 | Nucleic acids research |
| 2012 | High | ALCAM directly associates with the tetraspanin CD9 and ADAM17/TACE on the leukocyte surface; CD9 upregulates both homophilic and heterophilic ALCAM-mediated adhesion by (1) promoting ALCAM clustering and (2) inhibiting ADAM17 sheddase activity to increase ALCAM surface expression. | PMID:23052204 | Cellular and molecular life sciences |
| 2012 | Medium | ALCAM regulates motility, invasiveness, and adherens junction formation in uveal melanoma; shRNA knockdown of ALCAM reduced cell motility and invasion and disrupted adherens junction formation, while ALCAM overexpression enhanced recruitment of β-catenin and N-cadherin to adherens junctions. ALCAM is necessary but not sufficient to promote metastasis-associated behaviors. | PMID:22745734 | PloS one |
| 2012 | High | ALCAM mRNA is locally translated in retinal ganglion cell axonal growth cones, regulated by the 3'-UTR and dependent on ERK and TOR kinase activity. Local growth cone translation of ALCAM is required for enhanced axon elongation on ALCAM substrate, rapid compensation for experimentally induced ALCAM internalization, and axonal preference for ALCAM-containing lanes. | PMID:22421359 | Journal of cell science |
| 2013 | High | ALCAM regulates long-term hematopoietic stem cell (HSC) self-renewal and engraftment; Alcam-/- mice show reduced long-term repopulating capacity and engraftment efficiency, age-associated expansion of CD150hi LT-HSCs with myeloid-biased output, and premature elevation of age-associated genes (Selp, Clu, Cdc42, Foxo3). | PMID:23280653 | Stem cells |
| 2013 | High | ALCAM mediates adhesion, migration, and tube formation in lymphatic endothelial cells (LECs) and supports dendritic cell adhesion to lymphatic endothelium. ALCAM knockout mice have reduced LEC numbers, defects in organized lymphatic vessel network formation, and compromised DC migration from lung to draining lymph nodes. | PMID:23169771 | FASEB journal |
| 2013 | High | S100B binds CD166/ALCAM and induces dose- and time-dependent NF-κB activation in endothelial cells. siRNA knockdown of CD166/ALCAM completely inhibited S100B-induced NF-κB activation in RAGE-/- cells. In vivo, ALCAM siRNA attenuated delayed-type hypersensitivity (DTH) by ~40–50%; ALCAM-/- mice showed compensatory RAGE upregulation. | PMID:23729438 | Journal of immunology |
| 2014 | High | ALCAM is shed from metastatic prostate cancer cells by the sheddase ADAM17 in response to TGF-β signaling, and this ectodomain shedding is required for effective bone metastasis; shRNA knockdown of ALCAM in bone-metastatic PC3 cells greatly diminished skeletal dissemination and tumor growth in bone, associated with increased apoptosis and decreased proliferation. | PMID:24385212 | Cancer research |
| 2014 | High | ALCAM intracellular domain coupling to the actin cortex does not affect the affinity of individual ALCAM–CD6 bonds, but does control ALCAM recruitment to adhesion sites and membrane tether formation. Linking ALCAM to the actin cortex stiffens the cortex and strengthens overall cell adhesion to CD6 at the immunological synapse. | PMID:24496453 | Journal of cell science |
| 2014 | Medium | CD166 promotes anti-apoptotic signaling in liver cancer via PI3K/AKT: AKT upregulates CD166 expression post-transcriptionally, and CD166 in turn promotes AKT expression and activity (positive feedback). CD166 also activates YAP through transcriptional regulation via CREB and post-transcriptional stabilization via AMOT130 inhibition. CD9 enhances CD166-mediated YAP regulation by facilitating CD166–CD166 homophilic interaction. | PMID:24482231 | The Journal of biological chemistry |
| 2014 | Medium | CD166 regulates MCAM protein stability by suppressing the ubiquitin E3 ligases βTrCP and Smurf1 through PI3K/AKT and c-Raf/MEK/ERK signaling, thereby protecting MCAM from proteasomal degradation. | PMID:26004137 | Cellular signalling |
| 2014 | Medium | CD166 regulates FOXO protein stability and subcellular localization through AKT: CD166 overexpression accelerates FOXO ubiquitination and degradation and shifts FOXO from nucleus to cytoplasm, while CD166 knockdown reduces FOXO phosphorylation. AKT overexpression rescues CD166 knockdown-induced FOXO dephosphorylation and anti-carcinogenic effects, placing AKT between CD166 and FOXO. | PMID:24891117 | Oncology reports |
| 2015 | High | Crystal structures of the three SRCR domains of CD6 and the two N-terminal Ig domains of CD166 were solved by X-ray crystallography. Structural analysis revealed the CD6/CD166 binding interface, showed that a SNP in CD6 introduces glycosylation that sterically hinders the CD6/CD166 interaction, and native mass spectrometry demonstrated competition between heterophilic CD6-CD166 and homophilic CD166-CD166 interactions. | PMID:26146185 | Structure |
| 2016 | High | ILT3 (LILRB4) binds CD166/ALCAM directly; CRISPR-Cas9 knockout of CD166 abolished ILT3.Fc binding and its tumor-inhibitory effect. ILT3.Fc binding to CD166 inhibits tumor cell growth through inactivation of the p70 S6 kinase (p70S6K) signaling pathway. | PMID:29263213 | Journal of immunology |
| 2016 | High | CD166 in multiple myeloma cells inhibits osteoblastogenesis by suppressing Runx2 gene expression in osteoblast progenitors, and promotes osteoclastogenesis by activating TRAF6-dependent signaling in osteoclast progenitors; CD166 silencing reduced skeletal dissemination and osteolytic lesion formation in vivo. | PMID:27634757 | Cancer research |
| 2017 | High | ALCAM knockout mice develop more severe EAE (experimental autoimmune encephalomyelitis) with increased CNS-infiltrating leukocytes; passive transfer experiments linked this to absence of ALCAM on blood-brain barrier endothelial cells. ALCAM KO mice also show reduced expression of BBB tight junction proteins and increased CNS blood vessel permeability, establishing ALCAM as a component required for tight junction assembly and BBB integrity. | PMID:28069965 | Proceedings of the National Academy of Sciences of the United States of America |
| 2016 | Medium | ALCAM mediates preferential diapedesis of CD4+ Th1 cells (but not Th17 cells) across the human BBB in vitro; antibody-mediated ALCAM inhibition reduced Th1 but not Th17 diapedesis under static conditions. ALCAM also contributes to rolling, adhesion, and diapedesis of CD14+ monocytes across the human BBB under flow and static conditions. | PMID:28273717 | Journal of cerebral blood flow and metabolism |
| 2017 | High | CD166 loss in intestinal crypts reduces active-cycling Lgr5+ ISC numbers; homeostasis is maintained by transit-amplifying compartment expansion (not slow-cycling Bmi1+ ISC stimulation). Loss of active-cycling ISCs is coupled to defective Paneth cell terminal differentiation linked to reduced Wnt3 ligand expression and depleted nuclear β-catenin in CD166-/- Paneth cells. | PMID:28462380 | Cellular and molecular gastroenterology and hepatology |
| 2017 | High | ALCAM mediates DC migration through afferent lymphatics and promotes allospecific immune reactions; anti-murine ALCAM blocking antibody reduced DC transmigration across lymphatic endothelial monolayers, DC emigration from human skin explants, lymphangiogenic processes in vitro, and prevented corneal allograft rejection by retaining DCs in the cornea. | PMID:31031759 | Frontiers in immunology |
| 2017 | Medium | E3 ubiquitin ligase CHIP directly regulates ALCAM protein stability through the ubiquitin proteasome system; CHIP negatively correlates with CD166 in head and neck cancer samples, and CHIP expression represses cancer stem-like cell characteristics via targeting CD166 for degradation. | PMID:28279658 | Experimental cell research |
| 2019 | Medium | PRMT1 interacts with ALCAM directly (confirmed by co-immunoprecipitation and LC-MS); PRMT1 silencing reduced ALCAM protein levels and suppressed melanoma tumor growth and metastasis, while re-expression of ALCAM in PRMT1-silenced cells restored colony formation and metastatic ability, placing ALCAM downstream of PRMT1. | PMID:27175582 | Molecular medicine reports |
| 2020 | High | CD166/ALCAM is internalized via a clathrin-independent endocytic pathway driven by endophilin-A3 (not A1 or A2 isoforms) and extracellular galectin-8. Endophilin-A3 physically interacts with CD166-containing early endocytic carriers. This endocytic modality modulates CD166 surface abundance and regulates adhesive and migratory properties of cancer cells. | PMID:32193381 | Nature communications |
| 2020 | High | SOSTDC1 interacts with ALCAM/CD166 (identified by immunoprecipitation and mass spectrometry, confirmed by confocal microscopy and competition ELISA); this interaction involves the N-terminal region of SOSTDC1, which contains a sequence similar to the CD6-binding motif for ALCAM. ALCAM also interacts with α2β1 and α1β1 integrins. Knockdown of either SOSTDC1 or ALCAM, or antibody blockade, reduces invasion by inhibiting Src and PI3K/AKT signaling. | PMID:32801337 | Oncogene |
| 2016 | High | Galectin-8 interacts with ALCAM/CD166 in a glycosylation-dependent manner (demonstrated by surface plasmon resonance with recombinant glycosylated ALCAM ectodomain and endogenous ALCAM from breast cancer cells); ALCAM-silenced cells showed reduced binding to Gal-8. Exogenous Gal-8 caused ALCAM surface segregation/trapping at the cell surface. | PMID:27130882 | Biochimica et biophysica acta |
| 2022 | Medium | ALCAM/CD166 is involved in binding and uptake of cancer-derived extracellular vesicles (EVs) by recipient cancer cells; ALCAM participates in EV docking and subsequent uptake, demonstrated in colorectal and ovarian cancer cell systems. | PMID:35628559 | International journal of molecular sciences |
| 2022 | High | The CD6/ALCAM pathway promotes lupus nephritis (LN) via T cell-mediated responses; ALCAM is expressed by renal structural cells while CD6 is exclusive to T cells in the LN kidney. Antibody blockade of CD6 in murine lupus and immune-complex glomerulonephritis models significantly decreased immune cell infiltration, inflammatory markers, and disease measures. | PMID:34981775 | The Journal of clinical investigation |
| 2024 | Medium | Hypoxia promotes ALCAM expression in macrophages via HIF-1α binding to the ALCAM promoter; ALCAMhigh macrophages co-localize with exhausted CD8+ T cells in the tumor spatial microenvironment and promote T cell exhaustion. HIF-1α inhibition reduces ALCAM expression in macrophages and potentiates T cell anti-tumor function. | PMID:38956900 | Advanced science |

## Citations

- PMID:10673383
- PMID:11306570
- PMID:11568000
- PMID:15048703
- PMID:15769845
- PMID:16204050
- PMID:16352806
- PMID:16818742
- PMID:16865058
- PMID:17911180
- PMID:18598690
- PMID:21572107
- PMID:22421359
- PMID:22745734
- PMID:23052204
- PMID:23169771
- PMID:23280653
- PMID:23729438
- PMID:24385212
- PMID:24482231
- PMID:24496453
- PMID:24891117
- PMID:26004137
- PMID:26146185
- PMID:27130882
- PMID:27175582
- PMID:27634757
- PMID:28069965
- PMID:28273717
- PMID:28279658
- PMID:28462380
- PMID:29263213
- PMID:31031759
- PMID:32193381
- PMID:32801337
- PMID:34981775
- PMID:35628559
- PMID:38956900
- PMID:7760007
- PMID:9209500
- PMID:9502422
