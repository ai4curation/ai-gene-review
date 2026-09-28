---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AKAP12
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q02952
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 41
citation_count: 44
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AKAP12 (human)

## Current model (mechanistic narrative)

AKAP12 (SSeCKS/Gravin) is a large multivalent scaffold protein that spatiotemporally compartmentalizes kinases, cytoskeletal regulators, and signaling lipids to govern cytoskeletal architecture, cell-cycle progression, receptor recycling, and barriergenesis [PMID:9744295, PMID:10982843, PMID:14657015, PMID:12808449]. Its scaffolding logic is built from defined, phosphorylation-gated binding modules: it carries a PKA RII-binding domain establishing it as a bona fide AKAP [PMID:9885289, PMID:10469144], cyclin-binding (CY) motifs that overlap PKC phosphorylation sites (Ser507/515) so that PKC phosphorylation releases cytoplasmically sequestered cyclin D1 for nuclear translocation [PMID:10982843, PMID:22249313], calmodulin-binding sites antagonized by PKC phosphorylation [PMID:11820772], and direct PKCα-binding motifs through which AKAP12 binds and dampens PKC activity to restrain Rb-mediated senescence and cytoskeletal remodeling [PMID:21099353, PMID:21903576]. Through this architecture AKAP12 organizes actin-based cytoskeleton and adhesion, sequestering Src to caveolin-rich lipid rafts to disengage FAK and suppressing RhoA/Cdc42 to block podosome formation, and scaffolding phosphoinositides via MARCKS-like polybasic domains to direct lamellipodial chemotaxis [PMID:9744295, PMID:16547152, PMID:22710722, PMID:25356636]. It functions as a tumor and metastasis suppressor by attenuating Raf/MEK/ERK signaling away from a sequestered PKC pool, reducing MMP-2, VEGF, and invasion [PMID:9187136, PMID:16740695, PMID:20018890]. In endothelial and astrocytic compartments AKAP12 drives blood-brain/blood-retinal barrier formation by suppressing HIF-1α/VEGF and inducing angiopoietin-1, and by compartmentalizing PKA-VASP/Rac1 signaling at endothelial junctions and leading edges while restraining the Rho kinase pathway [PMID:12808449, PMID:17442832, PMID:31162891, PMID:33260683]. As an AKAP it phosphorylation-dependently re-associates with the β2-adrenergic receptor to enable resensitization and recycling [PMID:14657015, PMID:19055733], and in cardiomyocytes couples to PDE8 to limit intracellular cAMP and contractility [PMID:38506047]; it also scaffolds PKA-mediated phosphorylation of ATR-S435 to recruit XPA during nucleotide excision repair [PMID:27683220]. AKAP12 expression and stability are tightly controlled, undergoing epigenetic silencing by HDAC3/HDAC7 and Src-driven HDAC1 recruitment, and HDAC6-mediated deacetylation that triggers ubiquitin-proteasomal degradation [PMID:17626016, PMID:20568114, PMID:22584896, PMID:36122629, PMID:29484387].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity, GO:0008092 cytoskeletal protein binding, GO:0008289 lipid binding, GO:0140313 molecular sequestering activity
- **localization:** GO:0005856 cytoskeleton, GO:0005886 plasma membrane, GO:0005634 nucleus, GO:0005783 endoplasmic reticulum, GO:0005794 Golgi apparatus, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1640170 Cell Cycle, R-HSA-1643685 Disease, R-HSA-73894 DNA Repair, R-HSA-1500931 Cell-Cell communication, R-HSA-1266738 Developmental Biology
- **partners:** PRKACA, PRKCA, SRC, CCND1, ATR, AKAP5, ADRB2, B4GALT1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1998 | High | SSeCKS/AKAP12 associates with and controls elaboration of a cortical cytoskeletal matrix resistant to Triton X-100 extraction; ectopic SSeCKS expression in NIH3T3 cells caused cell flattening, loss of actin stress fibers and vinculin-associated adhesion plaques, and increased integrin-independent FAK tyrosine phosphorylation, establishing a direct role for SSeCKS in controlling actin-based cytoskeletal architecture. | PMID:9744295 | Cell motility and the cytoskeleton |
| 1997 | High | SSeCKS re-expression in v-Src-transformed NIH3T3 cells suppressed oncogenic transformation parameters (soft agar growth, invasiveness, focus formation, low-serum growth) without inhibiting Src kinase activity or JNK activity, but induced ERK2 activity; SSeCKS restored vinculin-associated adhesion plaques, actin stress fibers, and filopodia, indicating tumor suppression via cytoskeletal and signaling control rather than direct Src kinase inhibition. | PMID:9187136 | Cancer research |
| 2000 | High | SSeCKS induces G1 arrest by ERK2-dependent decrease in cyclin D1 expression and pRb phosphorylation; SSeCKS encodes two cyclin-binding (CY) motifs flanking PKC phosphorylation sites (Ser507/515) that bind cyclins D1 and E; K→S mutations in either CY motif ablate cyclin binding; PKC phosphorylation of SSeCKS at Ser507/515 releases cyclin D1 from cytoplasmic sequestration, allowing nuclear translocation; forced cyclin D1 re-expression fails to rescue SSeCKS-induced G1 arrest, demonstrating additional mechanisms. | PMID:10982843 | Molecular and cellular biology |
| 2002 | High | SSeCKS encodes four calmodulin (CaM) binding sites conforming to the 1-5-10 motif; CaM binding is antagonized by PKC pre-phosphorylation of SSeCKS; two major cyclin-binding (CY) sites overlap the major PKC phosphorylation site (Ser507/515), and cyclin D binding is attenuated by PKC pre-phosphorylation, demonstrating phosphorylation-dependent modulation of SSeCKS scaffolding activity. | PMID:11820772 | Biochemical and biophysical research communications |
| 2001 | High | SSeCKS/AKAP12 directly binds the cytoplasmic domain of beta1,4-galactosyltransferase I (GalT); identified by yeast two-hybrid screen and confirmed by reciprocal co-immunoprecipitation of both endogenous and transfected proteins; SSeCKS domains localized to Golgi (2.52) and filopodia (1.12) recapitulate GalT distribution; SSeCKS-GalT interaction restores normal adhesive phenotype disrupted by a dominant-negative GalT construct. | PMID:11493668 | Journal of cell science |
| 2003 | High | Gravin/AKAP12 (AKAP250) dynamically associates with the beta2-adrenergic receptor (β2AR); the AKAP domain of gravin is essential for receptor binding (deletion abolishes binding); agonist stimulation induces gravin phosphorylation at two canonical PKA sites within its AKAP domain; PKA phosphorylation of these sites is required for scaffold-receptor association and for receptor resensitization; the AKAP-anchored PKA provides the catalytic activity responsible for phosphorylating the scaffold. | PMID:14657015 | The EMBO journal |
| 2003 | High | SSeCKS in astrocytes decreases VEGF expression through AP-1 reduction and stimulates angiopoietin-1 expression; conditioned media from SSeCKS-overexpressing astrocytes blocks angiogenesis in vivo and in vitro, increases tight junction proteins in endothelial cells, and decreases sucrose permeability, establishing SSeCKS as a regulator of BBB differentiation. | PMID:12808449 | Nature medicine |
| 2004 | High | AKAP12 encodes three isoforms (alpha, beta, gamma) from three independent promoters with distinct tissue expression profiles; the alpha isoform contains an N-terminal myristoylation motif shown by deletion mapping and GFP chimeras to be necessary and sufficient for targeting AKAP12alpha to the endoplasmic reticulum, a novel AKAP12 subcellular compartment. | PMID:15496411 | The Journal of biological chemistry |
| 2005 | Medium | AKAP12 contains five nuclear localization signals (NLS) in its central region (including a novel X2-NLS class) that confer nuclear targeting potential; this is suppressed by a negatively charged C-terminus mediating nuclear exclusion; three basic residue-rich regions in the N-terminal domain (similar to MARCKS) control AKAP12 localization to ganglioside-rich regions at the cell periphery, establishing a hierarchy of targeting domains. | PMID:15923193 | The Journal of biological chemistry |
| 2006 | High | SSeCKS re-expression suppresses podosome formation via inhibition of RhoA and Cdc42 activity (>5-fold reduction); activated RhoA and Cdc42 rescue podosome formation in SSeCKS-expressing v-Src cells; SSeCKS does not affect Tks5/Fish tyrosine phosphorylation or total cellular tyrosine phosphorylation, placing SSeCKS downstream of Src kinase activity but upstream of RhoA/Cdc42-mediated cytoskeletal remodeling. | PMID:16547152 | Molecular cancer research |
| 2006 | High | SSeCKS metastasis-suppressor activity correlates with suppression of VEGF expression in prostate cancer cells and tumor stroma; forced re-expression of VEGF165 or VEGF121 is sufficient to partially reverse SSeCKS metastasis suppression in both experimental and spontaneous lung metastasis models; SSeCKS also upregulates antiangiogenic genes (vasostatin, collagen 18a1) and downregulates proangiogenic genes (osteopontin, HIF-1alpha, angiopoietin). | PMID:16740695 | Cancer research |
| 2007 | High | AKAP12 downregulates HIF-1alpha protein by enhancing its interaction with pVHL (von Hippel-Lindau protein) and PHD2 (prolyl hydroxylase 2), leading to decreased VEGF and increased angiopoietin-1 in astrocytes; conditioned media from AKAP12-overexpressing astrocytes induces tight junction protein expression in human retinal microvascular endothelial cells, promoting blood-retinal barrier formation. | PMID:17442832 | The Journal of neuroscience |
| 2007 | High | v-Src downregulates SSeCKS alpha promoter via recruitment of HDAC1 to a USF1-Sp1/Sp3 complex at E- and GC-box elements (-106 to -49); v-Src increases Sp1/Sp3 binding to the GC-box without altering protein abundance; Src-induced tyrosine phosphorylation of TFII-I increases its binding to the SSeCKS proximal promoter and is required for full transcriptional repression; trichostatin A (HDAC inhibitor) but not 5-azacytidine restores SSeCKS transcript levels. | PMID:17626016, PMID:20568114 | The Journal of biological chemistry |
| 2008 | Medium | AKAP12 in astrocytes reduces phosphorylation of PKCzeta in retinal endothelial cells; PKCzeta knockdown decreases VEGF and increases thrombospondin-1 (TSP-1); inhibition of Rho kinase (Y27632) downstream of PKCzeta also decreases VEGF and increases TSP-1, establishing an AKAP12→PKCzeta→Rho kinase→VEGF/TSP-1 pathway mediating barriergenesis. | PMID:18397319 | The FEBS journal |
| 2008 | Medium | Loss of SSeCKS/AKAP12 in knockout mice results in prostatic hyperplasia with focal dysplasia; SSeCKS-null prostate tissues exhibit significantly higher AKT(pS473) levels relative to wild-type, suggesting SSeCKS attenuates PI3K/AKT signaling in vivo. | PMID:18593908 | Cancer research |
| 2009 | High | SSeCKS suppresses serum-induced Raf/MEK/ERK pathway activation, leading to decreased MMP-2 expression and inhibition of chemotaxis and Matrigel invasion; constitutively active MEK1, MEK2, ERK1, or PKCalpha restores invasiveness and chemotaxis; SSeCKS attenuation of ERK activation requires its PKC-binding domain (aa 553-900), suggesting direct PKC scaffolding; jasplakinolide (actin stabilizer) nullifies SSeCKS inhibition of MEK/ERK activation but not podosome inhibition. | PMID:20018890 | The Journal of biological chemistry |
| 2010 | High | AKAP12-null MEF exhibit premature senescence marked by polyploidy and multinucleation; senescence is Rb-dependent; PKCα activation induces p16(Ink4a)/Rb through MEK-dependent downregulation of Id1; PKCδ downregulates Lats1/Warts kinase required for cytokinesis; Akap12 directly scaffolds and attenuates PKCα/δ, controlling Rb-mediated cell aging and cytokinesis. | PMID:21099353 | Cell cycle |
| 2011 | High | SSeCKS directly binds PKCα through two homologous motifs (EG(I/V)(T/S)XWXSFK(K/R)(M/L)VTP(K/R)K(K/R)X(K/R)XXXEXXXE(E/D); aa 592-620 and 741-769); SSeCKS binding to PKCα decreases kinase activity; SSeCKS scaffolding of PKC increases at confluence correlating with decreased PKCα activity; SSeCKS-null MEF show increased PKC activity and defective phorbol ester-induced actin cytoskeletal reorganization, rescued by full-length SSeCKS but not by PKC-binding domain-deleted SSeCKS. | PMID:21903576 | The Journal of biological chemistry |
| 2012 | High | SSeCKS sequesters cyclin D1 in the cytoplasm of quiescent glomerular parietal epithelial cells (PECs); PKC phosphorylation of SSeCKS disrupts binding, resulting in nuclear translocation of cyclin D1; co-immunoprecipitation demonstrates cyclin D1-SSeCKS complex in PECs; SSeCKS-null mice show PEC hyperplasia with increased nuclear cyclin D1 and worse glomerular disease. | PMID:22249313 | Laboratory investigation |
| 2012 | High | SSeCKS contains a Src-binding domain (aa 153-166) homologous to the caveolin-1 Src-binding domain; this domain mediates SSeCKS-Src interaction, SSeCKS-enhanced Src activity, and sequestration of Src to caveolin-rich lipid rafts; SSeCKS suppresses adhesion-induced Src activation (SrcpoY416) and FAK-Y925 phosphorylation while increasing FAK(pY397) and cell adhesion to fibronectin; lipid raft sequestration of Src disengages Src from FAK-associated adhesion complexes. | PMID:22710722 | Oncogene |
| 2012 | High | AKAP12 depletion in zebrafish (akap12 morphants) causes severe hemorrhage due to disorganized interendothelial cell-cell adhesions; AKAP12 knockdown in endothelial cells reduces expression of PAK2 (actin cytoskeletal regulator) and AF6 (connector of intercellular adhesion molecules to actin); PAK2 or AF6 knockdown phenocopies AKAP12 depletion; overexpression of PAK2 and AF6 rescues hemorrhage in akap12 morphants. | PMID:22192928 | Experimental & molecular medicine |
| 2012 | High | HDAC7 epigenetically silences AKAP12 in endothelial cells; siRNA depletion of HDAC7 causes H3 histone acetylation at the AKAP12 promoter, increasing AKAP12 mRNA and protein; elevated AKAP12 after HDAC7 depletion is responsible for inhibited migration and tube formation; AKAP12 mediates PKC-dependent phosphorylation of STAT3, which binds to the AKAP12 promoter and maintains elevated AKAP12 levels in a positive feedback loop. | PMID:22584896 | Angiogenesis |
| 2013 | High | AKAP12/gravin promoter contains two functional HIF-binding sites; site-directed mutagenesis identified the distal HIF-binding site as essential for hypoxia-induced gravin expression; gravin gain-of-function inhibits microvascular endothelial tube formation ('braking' system for angiogenesis); gravin functionally couples to control endothelial barrier function in response to PKA agonists. | PMID:24029533 | FASEB journal |
| 2014 | High | PKA compartmentalization by AKAP12 is required for cAMP-mediated endothelial barrier stabilization; siRNA depletion of AKAP12 significantly impairs endothelial barrier function; AKAP12 depletion redistributes PKA and Rac1 away from endothelial junctions and inactivates Rac1; TAT-Ahx-AKAPis peptide (competitive PKA-AKAP disruptor) destabilizes barrier and dampens forskolin/rolipram-mediated barrier enhancement. | PMID:25188285 | PloS one |
| 2014 | High | SSeCKS controls chemotaxis and lamellipodia formation by scaffolding phosphoinositides through its three MARCKS polybasic domains (PBD); loss of SSeCKS shifts leading edge from lamellipodia to filopodia-like extensions, enriches PIP3, Akt, PKC-ζ, Cdc42-GTP, and active Src at the leading edge, and recruits Frabin (Cdc42-GEF) via PIP2/3 binding; full-length SSeCKS or ΔPBD-deleted SSeCKS fails to rescue, whereas ΔSrc variant rescues, placing PIP scaffolding above Src-binding in chemotaxis control. | PMID:25356636 | PloS one |
| 2014 | Medium | AKAP12 modulates meningeal EMT by regulating the TGF-β1-non-Smad-SNAI1 signaling pathway; AKAP12 expression in meningeal cells is regulated by integrated signals of TGF-β1, retinoic acid (RA), and oxygen tension; AKAP12-KO mice show impaired meningeal reconstruction after CNS injury. | PMID:25229625 | Nature communications |
| 2015 | High | Hypoxia selectively induces AKAP12 variant 2 (AKAP12v2) in metastatic melanoma; AKAP12v2 causes a shift in PKA-mediated phosphorylation events (identified by kinome-wide phosphoproteomics and MS) under hypoxia; this shift is due to changes in AKAP12 localization rather than structural differences between variants; the AKAP12-dependent phosphorylation shift alters tumor cell invasion and migration in vitro and metastasis in vivo. | PMID:25792458 | Proceedings of the National Academy of Sciences of the United States of America |
| 2016 | High | AKAP12 scaffolds PKA to mediate phosphorylation of ATR at Ser435, a modification required for cAMP-enhanced nucleotide excision repair (NER); UV exposure promotes ATR-directed phosphorylation of AKAP12 at S732, driving nuclear translocation of the AKAP12-ATR-pS435 complex; this complex recruits XPA to UV-damaged DNA and enhances 5' strand incision; preventing AKAP12-PKA or AKAP12-ATR interaction abrogates ATR-pS435, delays XPA recruitment, impairs NER, and increases UV-induced mutagenesis. | PMID:27683220 | Nucleic acids research |
| 2019 | High | AKAP12 localizes to lamellipodia in migrating endothelial cells and to tip cells at the angiogenic front in postnatal retina; AKAP12 co-localizes with PKA type II-α regulatory subunit, Arp2/3 complex components, and VASP; AKAP12 deletion results in defective vascular plexus extension; VEGF-stimulated PKA-dependent phosphorylation of VASP at Ser157 requires AKAP12, demonstrated by co-localization of phospho-Ser157 VASP with AKAP12 at the leading edge. | PMID:31162891 | Acta physiologica |
| 2020 | High | AKAP12 loss in endothelial cells causes upregulation/activation of the Rho kinase pathway and increased endothelial permeability with dysregulation of ZO-1/Claudin-5; Rho kinase inhibitor Y-27632 reverses increased permeability in AKAP12-deficient cells and tightens the BBB in Akap12 knockout mice after stroke, placing AKAP12 upstream of the Rho kinase pathway in BBB maintenance. | PMID:33260683 | International journal of molecular sciences |
| 2020 | Medium | Notch signaling suppresses Akap12 expression during renal tubule morphogenesis; loss of Notch signaling increases Akap12 expression and results in abnormally long primary cilia; ectopic Akap12 expression phenocopies Notch loss (long cilia, defective lumen formation); Akap12 inhibits Notch-mediated transcription, suggesting a negative feedback loop. | PMID:32474964 | FASEB journal |
| 2022 | High | HDAC6 directly interacts with AKAP12 and deacetylates it at K526/K531; deacetylation of AKAP12 at K531 by HDAC6 increases its ubiquitination level, facilitating proteasome-dependent degradation; deletion of AKAP12 in HDAC6-knockdown cells restores cell motility defects and reactivates PKC isoforms, placing AKAP12 downstream of HDAC6-mediated degradation in colon cancer metastasis control. | PMID:36122629 | Cancer letters |
| 2024 | High | AKAP12 overexpression in cardiac myocytes reduces total intracellular cAMP levels through PDE8 (not PDE4D); AKAP12-overexpressing mice show reduced cardiomyocyte contractility and impaired calcium handling in response to isoproterenol, reversed by selective PDE8 inhibitor (PF-04957325); AKAP12OX mice develop systolic dysfunction and left ventricular enlargement; patients with end-stage heart failure show upregulated AKAP12. | PMID:38506047 | Circulation research |
| 1999 | High | SSeCKS/clone 72 contains a PKA RII-binding domain (aa 1495-1524) identified by deletion mutagenesis, confirming it is an AKAP; PKC-induced serine phosphorylation of SSeCKS causes rapid translocation to perinuclear sites, coincident with retraction of stellate processes in mesangial cells; ablation of SSeCKS by antisense retroviral vectors induces fibroblastic morphology, thick longitudinal stress fibers, and repositioning of vinculin-associated focal complexes. | PMID:9885289, PMID:10469144 | Journal of cell science / European journal of biochemistry |
| 2002 | High | SSeCKS tyrosine phosphorylation by mitogens (EGF, PDGF, serum) is FAK-dependent: FAK-deficient cells cannot phosphorylate SSeCKS upon EGF stimulation, rescued by re-expression of wild-type FAK but not FAK-Y397 mutant; purified FAK or Src fail to directly phosphorylate SSeCKS in vitro; phosphorylation is independent of Src/Fyn/Yes/Abl; unphosphorylated bacterially expressed SSeCKS co-sediments with F-actin; tyrosine phosphorylation modulates SSeCKS-actin interaction. | PMID:12083796 | Experimental cell research |
| 2008 | High | AKAP12/gravin is selectively required for resensitization and recycling of the beta2-adrenergic receptor: AKAP12 knockdown in A431 or HEK293 cells abolishes receptor resensitization, while AKAP5 knockdown does not; AKAP5 knockdown abolishes Erk1/2 activation downstream of beta2AR while AKAP12 knockdown does not, demonstrating non-redundant pathway segregation between the two AKAPs. | PMID:19055733 | Journal of molecular signaling |
| 2011 | Medium | AKAP12 forms higher-order homo-oligomers (behaving as dimers or tetramers ~840 kDa by steric-exclusion chromatography); both N-terminal (aa 1-840) and C-terminal (aa 840-1782) regions independently form dimers; AKAP12 and AKAP5 form hetero-oligomers demonstrated by affinity chromatography and steric-exclusion chromatography; beta-adrenergic agonist stimulation increases AKAP5-AKAP12 docking 4-fold; AKAP12 overexpression potentiates AKAP5-mediated ERK1/2 activation. | PMID:21554706, PMID:21831305 | Journal of molecular signaling |
| 2017 | High | Stromal SSeCKS/AKAP12 suppresses metastatic peritoneal colonization by attenuating secretion of Cxcl9/10 from peritoneal membrane fibroblasts; SSeCKS-null peritoneal fibroblasts exhibit senescence (SA-β-gal, p21, p16) and secrete elevated Cxcl10 in response to inflammatory mediators; Cxcr3 knockdown abrogates enhanced chemotaxis to KO peritoneal fluid; SSeCKS scaffolding-site mutants and kinase inhibitors show PKC, PKA, and PI3K/Akt pathways are responsible for Cxcl10 secretion control. | PMID:29050279 | Oncotarget |
| 2018 | Medium | SSeCKS/AKAP12 in lung fibroblasts suppresses metastatic melanoma colonization by attenuating Src/STAT3-dependent senescence-associated secretory phenotype; SSeCKS Src-scaffolding domain is required to attenuate IFNα-induced Stat3 activation in KO lung fibroblasts; KO lung endothelial cells exhibit increased E-Selectin levels facilitating melanoma adhesion. | PMID:30323895 | Oncotarget |
| 2018 | Medium | HDAC3 directly binds within the intron-1 region of AKAP12 and this binding is indispensable for HDAC3-mediated inhibition of AKAP12 expression; HDAC3 inhibitors (TSA, RGFP966) restore AKAP12 expression; AKAP12 knockdown increases PI3K/AKT signaling activity, establishing PI3K/AKT as downstream of AKAP12 in colorectal cancer cells. | PMID:29484387 | International journal of oncology |
| 2015 | Medium | SSeCKS expression is decreased in differentiated Schwann cells; long-term SSeCKS knockdown changes Schwann cell morphology, accelerates myelin gene expression induced by cAMP, and enhances myelination in Schwann cell-DRG co-culture; SSeCKS suppression promotes Akt (Ser473) phosphorylation in cAMP-treated Schwann cells, identifying SSeCKS as a negative regulator of Schwann cell myelination. | PMID:19757038 | Neurochemical research |

## Citations

- PMID:10469144
- PMID:10982843
- PMID:11493668
- PMID:11820772
- PMID:12083796
- PMID:12808449
- PMID:14657015
- PMID:15496411
- PMID:15923193
- PMID:16547152
- PMID:16740695
- PMID:17442832
- PMID:17626016
- PMID:18397319
- PMID:18593908
- PMID:19055733
- PMID:19757038
- PMID:20018890
- PMID:20568114
- PMID:21099353
- PMID:21554706
- PMID:21831305
- PMID:21903576
- PMID:22192928
- PMID:22249313
- PMID:22584896
- PMID:22710722
- PMID:24029533
- PMID:25188285
- PMID:25229625
- PMID:25356636
- PMID:25792458
- PMID:27683220
- PMID:29050279
- PMID:29484387
- PMID:30323895
- PMID:31162891
- PMID:32474964
- PMID:33260683
- PMID:36122629
- PMID:38506047
- PMID:9187136
- PMID:9744295
- PMID:9885289
