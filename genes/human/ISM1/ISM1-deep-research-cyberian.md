---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T18:27:25.629878'
end_time: '2026-01-22T18:47:47.310011'
duration_seconds: 1221.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ISM1
  gene_symbol: ISM1
  uniprot_accession: B1AKI9
  protein_description: 'RecName: Full=Isthmin-1; Flags: Precursor;'
  gene_info: Name=ISM1; Synonyms=C20orf82, ISM;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the isthmin family. .
  protein_domains: AMOP_dom. (IPR005533); Angio_Inhib/Adhesion_GPCR. (IPR051867);
    TSP1_rpt. (IPR000884); TSP1_rpt_sf. (IPR036383); AMOP (PF03782)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 21
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** B1AKI9
- **Protein Description:** RecName: Full=Isthmin-1; Flags: Precursor;
- **Gene Information:** Name=ISM1; Synonyms=C20orf82, ISM;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the isthmin family. .
- **Key Domains:** AMOP_dom. (IPR005533); Angio_Inhib/Adhesion_GPCR. (IPR051867); TSP1_rpt. (IPR000884); TSP1_rpt_sf. (IPR036383); AMOP (PF03782)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ISM1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ISM1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ISM1** (gene ID: ISM1, UniProt: B1AKI9) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Isthmin-1 (ISM1): A Multifunctional Secreted Protein with Roles in Development, Angiogenesis, and Metabolism

## Introduction

Isthmin-1 (ISM1) is a secreted glycoprotein that was first identified in 2002 through an unbiased secretion cloning screen of Xenopus laevis gastrula embryos [pera-2002-isthmin-discovery-abstract]. The protein was named after the isthmus (midbrain-hindbrain boundary) where it was prominently expressed during early embryonic development. Since its discovery, ISM1 has emerged as a multifunctional protein with diverse roles spanning embryonic patterning, angiogenesis inhibition, apoptosis regulation, vascular permeability, immune modulation, and metabolic control [li-2023-isthmin-review-abstract].

Human ISM1 (UniProt: B1AKI9) encodes a precursor protein of 499 amino acids (approximately 60 kDa), while the mouse ortholog contains 461 amino acids. The protein exhibits remarkable evolutionary conservation, with mouse and human ISM1 sharing 93% amino acid sequence identity, and 78% identity with the frog ortholog [pera-2002-isthmin-discovery-abstract]. This high degree of conservation suggests critical cellular functions maintained across vertebrate evolution [valle-dorado-2022-isthmin-family-abstract].

ISM1 functions primarily as a secreted signaling molecule that acts through multiple cell-surface receptors to regulate diverse biological processes. The protein has garnered significant attention for its potential therapeutic applications in cancer treatment, metabolic disease, and lung pathology, though recent structural studies have challenged some of its reported metabolic functions [cao-2025-crystal-structure-abstract].

## Protein Structure and Domains

ISM1 possesses a modular architecture consisting of three main regions: an N-terminal signal peptide, a central thrombospondin type 1 repeat (TSR) domain, and a C-terminal adhesion-associated domain in MUC4 and other proteins (AMOP) domain [li-2023-isthmin-review-abstract][valle-dorado-2022-isthmin-family-abstract].

The TSR domain encompasses approximately 60 amino acids and forms a reverse three-stranded beta-sheet structure stabilized by three conserved disulfide bonds. This domain contains conserved tryptophan, arginine, and cysteine residues characteristic of TSR-containing proteins. ISM1 contains a "WSLW motif" that is potentially involved in heparin binding and may contribute to its anti-angiogenic functions [valle-dorado-2022-isthmin-family-abstract]. The TSR domain is implicated broadly in cell-cell and cell-ECM interactions, tumor metastasis, angiogenesis, TGF-beta activation, wound healing, and axon guidance.

The AMOP domain comprises approximately 100-160 amino acids and represents a novel extracellular domain originally identified in certain splice variants of MUC4. This domain has been described in only four proteins: MUC4, SUSD2, ISM1, and ISM2 [li-2023-isthmin-review-abstract]. The recent crystal structure determination of ISM1's AMOP domain (PDB: 9C6T) revealed a distinctive fold with similarities to bacterial streptavidin. The structure has been described as resembling "a hand holding chopsticks," where the central antiparallel beta-strands function as fingers, terminal helices act as chopsticks, and middle helices serve as a thumb [cao-2025-crystal-structure-abstract]. This streptavidin-like barrel architecture is conserved among AMOP domains, though surface helices and loops vary considerably, providing structural plasticity that may underpin diverse functions.

Importantly, the AMOP domain contains conserved cysteine residues involved in disulfide bond formation (eight invariant cysteines) and harbors a critical RKD sequence that was initially proposed as an integrin-binding motif [zhang-2011-integrin-dual-effect-abstract]. However, recent structural analysis has challenged this interpretation, demonstrating significant steric clashes between the AMOP domain and integrin receptors that are incompatible with canonical RGD-mediated integrin binding [cao-2025-crystal-structure-abstract]. The AMOP domain also possesses a KGD motif reported to bind integrin alphaIIbeta3.

ISM1 undergoes critical post-translational modifications including N-glycosylation and C-mannosylation that regulate its secretion and function [osorio-2019-nodal-signaling-abstract][cao-2025-crystal-structure-abstract]. Detailed biochemical analysis has revealed two putative N-glycosylation sites at positions Asn39 and Asn285, and two C-mannosylation sites at Trp223 and Trp226 within the TSR domain [yoshimoto-2021-cmannosylation-abstract].

A landmark study by Yoshimoto et al. demonstrated that C-mannosylation of ISM1 regulates intracellular transport from the endoplasmic reticulum to the Golgi apparatus and is essential for efficient secretion [yoshimoto-2021-cmannosylation-abstract]. When C-mannosylation-defective ISM1 mutants were expressed, secretion decreased significantly compared to wild-type cells. Interestingly, when C-mannosylation is lacking, N-glycosylation at Asn39 and Asn285 is induced as a compensatory mechanism to rescue secretory function. This interplay between C-mannosylation and N-glycosylation represents a novel regulatory mechanism for ISM1 secretion. Because the TSR domain is highly conserved across species, C-mannosylation of ISM1 is likely present in other vertebrates [valle-dorado-2022-isthmin-family-abstract].

## Receptor Binding and Signal Transduction

ISM1 exerts its biological effects through at least three identified receptors, each mediating distinct cellular responses depending on cell type and physiological context.

### GRP78: The High-Affinity Receptor

Cell-surface glucose-regulated protein 78 kDa (GRP78) serves as a high-affinity receptor for ISM1, with a dissociation constant (Kd) of 8.6 nM [chen-2014-grp78-apoptosis-abstract]. GRP78, also known as BiP (binding immunoglobulin protein), is a member of the HSP70 heat shock chaperone family and serves as a major endoplasmic reticulum stress response protein. Under normal conditions, GRP78 predominantly localizes to the ER lumen. However, in stressed cells, including cancer cells and activated endothelial cells, GRP78 is overexpressed and a portion translocates to the cell surface where it serves as a signaling receptor [chen-2014-grp78-apoptosis-abstract].

The ISM1-GRP78 interaction triggers two distinct downstream effects. First, in terms of apoptosis induction, ISM1 binding to cell-surface GRP78 leads to clathrin-dependent internalization, followed by trafficking to mitochondria where ISM1 interacts with adenine nucleotide translocase (AAC/ANT), blocking ADP/ATP exchange and inducing mitochondrial dysfunction and apoptosis [chen-2014-grp78-apoptosis-abstract]. This selective targeting mechanism makes ISM1 an attractive agent for cancer therapy, as cancer cells typically express high levels of cell-surface GRP78 while normal cells remain resistant to ISM1-induced apoptosis.

Second, regarding vascular permeability regulation, ISM1 binding to GRP78 induces a direct GRP78-Src interaction, leading to cytoplasmic Src activation and enhanced endothelial monolayer permeability [venugopal-2015-vascular-permeability-abstract]. Systemic ISM1 administration leads to profound lung vascular hyperpermeability, and ISM1 is significantly upregulated in LPS-treated mouse lung, contributing to pulmonary vascular dysfunction in acute lung injury [venugopal-2015-vascular-permeability-abstract].

### Integrin alphavbeta5: The Low-Affinity Receptor

Integrin alphavbeta5 serves as a low-affinity receptor for ISM1 [zhang-2011-integrin-dual-effect-abstract]. Remarkably, ISM1 exhibits dual functionality through this receptor depending on its physical state. Soluble ISM1 functions as an integrin alphavbeta5 antagonist, suppressing endothelial cell tube formation and inducing apoptosis through integrin-mediated death (IMD). This involves direct recruitment and activation of caspase-8 without causing anoikis [zhang-2011-integrin-dual-effect-abstract]. Activated caspase-8 can first be detected 4 hours after ISM treatment, and knockdown of the beta5-integrin subunit suppresses caspase-8 and caspase-3 activation as well as PARP cleavage.

In contrast, immobilized ISM1 promotes endothelial cell adhesion, survival, and haptotactic migration by functioning as an integrin alphavbeta5 agonist and activating focal adhesion kinase (FAK) [zhang-2011-integrin-dual-effect-abstract]. This dual functionality has significant implications for understanding how ISM1 may perform therapeutically in vivo, where its physical state fundamentally alters biological outcomes through the same receptor.

### Integrin alpha8beta1: Developmental Receptor

More recently, integrin alpha8beta1 was identified as a receptor for ISM1 specifically in the context of kidney development [gao-2023-kidney-development-abstract]. Using HRP-induced proximity-labeling in embryonic kidney rudiments (E11.5), researchers demonstrated that ISM1 binding to integrin alpha8beta1 activates downstream targets including FAK, AKT, and ERK, promoting cell-cell adhesion and mesenchyme condensation during early renal branching morphogenesis.

### NODAL Signaling Pathway Interaction

Beyond direct receptor binding, ISM1 also modulates the NODAL signaling pathway through direct interaction with pathway components. ISM1 binds to both the NODAL ligand and the type I receptor ACVR1B through its AMOP domain, compromising NODAL-ACVR1B complex formation and down-regulating SMAD2 phosphorylation [osorio-2019-nodal-signaling-abstract]. Notably, ISM1 specifically inhibits NODAL-induced signaling while having minimal effect on TGF-beta1, ACTIVIN-A, or BMP4 signaling, demonstrating ligand-dependent selectivity within the TGF-beta superfamily.

## Biological Functions

### Anti-angiogenic Activity and Cancer

ISM1 potently inhibits angiogenesis through multiple mechanisms. Both full-length ISM1 and the AMOP domain fragment inhibit capillary network formation in a dose-dependent manner [li-2023-isthmin-review-abstract]. The protein suppresses tumor growth and angiogenesis in mouse models when stably overexpressed in cancer cells, including melanoma and glioma models.

The anti-tumor properties of ISM1 extend beyond anti-angiogenesis to include direct apoptosis induction in cancer cells expressing high levels of cell-surface GRP78. Normal cells and benign tumor cells, which express low levels of cell-surface GRP78, remain resistant to ISM1-induced apoptosis [chen-2014-grp78-apoptosis-abstract]. A peptide derived from the AMOP domain (BC71) activates p53 and caspase-8 pathways.

Building on these anti-cancer properties, researchers have developed therapeutic peptides derived from ISM1's AMOP domain. The cyclic peptide BC71, harboring the RKD motif from ISM1's AMOP domain, functions as a potent proapoptotic ligand of cell-surface GRP78 [kao-2018-bc71-peptide-abstract]. Using hydrogen-deuterium exchange mass spectrometry, researchers identified that BC71 preferentially binds ATP-bound GRP78 at amino acids 244-257. Critically, intravenous administration of BC71 suppressed xenograft tumor growth in mice as a single agent, with significant reduction in tumor angiogenesis and increased apoptosis via caspase-8 activation. Fluorescent-labeled BC71 accumulates specifically in tumors by targeting cell-surface GRP78, suggesting potential applications not only as a therapeutic but also as a PET imaging agent for cancer prognosis [kao-2018-bc71-peptide-abstract].

Paradoxically, ISM1 expression is elevated in certain cancers including colorectal cancer, where it correlates with shorter overall survival, lymph node involvement, and advanced disease stages [wu-2021-colorectal-cancer-abstract]. In colorectal cancer, ISM1 promotes epithelial-mesenchymal transition (EMT) markers (increased N-cadherin and Snail, decreased E-cadherin) and correlates positively with immune checkpoint markers including PD-L1, PD-1, CTLA-4, and LAG3, potentially contributing to immunotherapy resistance. ISM1 expression is also elevated in gastric cancer and hepatocellular carcinoma. This apparent contradiction between ISM1's anti-angiogenic properties and its elevation in cancer remains incompletely understood and may reflect context-dependent functions in the tumor microenvironment [li-2023-isthmin-review-abstract].

### Developmental Functions

ISM1 plays essential roles during embryonic development. Its expression at the midbrain-hindbrain boundary as part of the FGF-8 synexpression group initially suggested developmental patterning functions [pera-2002-isthmin-discovery-abstract].

In terms of left-right asymmetry and organ positioning, ectopic ISM1 expression causes defective left-right asymmetry and abnormal heart positioning in chick embryos through inhibition of NODAL signaling [osorio-2019-nodal-signaling-abstract]. Treatment with ISM1 reduced asymmetric NODAL gene expression in the left lateral plate mesoderm by approximately 70%.

For kidney development, ISM1 is expressed in metanephric mesenchyme and regulates mesenchyme condensation through integrin alpha8beta1-mediated cell adhesion. ISM1-deficient mice exhibit defective ureteric bud bifurcation and impaired mesenchyme condensation, ultimately leading to renal agenesis and hypoplasia/dysplasia in approximately 60% of homozygous mutants [gao-2023-kidney-development-abstract]. ISM1 regulates this process through enhancement of GDNF/Ret signaling, which is essential for normal branching morphogenesis.

Regarding craniofacial development, ISM1 heterozygous deletions are associated with cleft lip and palate susceptibility in humans. Knockdown of ISM1 in Xenopus results in severe perturbation of craniofacial morphogenesis and reduces expression of LHX8, a known clefting locus [li-2023-isthmin-review-abstract].

ISM1 also functions in hematopoiesis, as demonstrated through detailed studies in zebrafish. Berrun et al. identified ism1 as highly expressed in hematopoietic-supportive stromal cell lines and showed that it is co-expressed with FGF ligands essential for HSC specification [berrun-2018-hematopoiesis-abstract]. Loss-of-function experiments using morpholinos revealed that ism1 knockdown leads to reduced numbers of neutrophils, macrophages, and erythrocytes. Clonal methylcellulose assays demonstrated a reduction in total hematopoietic stem and progenitor cells (HSPCs). Morphant embryos displayed slowed circulation and blood pooling at 48 hours post-fertilization, while hearts appeared morphologically normal, indicating a specific hematopoietic defect rather than cardiovascular dysfunction [berrun-2018-hematopoiesis-abstract]. These findings establish ISM1 as required for normal generation of HSPCs and their downstream progeny during vertebrate hematopoiesis.

### Metabolic Functions and Controversy

A landmark 2021 study identified ISM1 as an adipokine that promotes glucose uptake in adipose tissue while simultaneously suppressing lipid synthesis in the liver [jiang-2021-adipokine-glucose-abstract]. ISM1 was reported to activate PI3K-AKT signaling independently of insulin and IGF-1 receptors, and ISM1 knockout mice exhibited impaired glucose tolerance, reduced adipose glucose uptake, and reduced insulin sensitivity. Therapeutic dosing of recombinant ISM1 improved diabetes in diet-induced obese mice and ameliorated hepatic steatosis [jiang-2021-adipokine-glucose-abstract].

However, a recent structural and biochemical study has challenged these findings [cao-2025-crystal-structure-abstract]. Researchers at Yale demonstrated that purified ISM1 alone does NOT activate AKT phosphorylation in pre-adipocytes. Instead, co-purifying contaminants from expression systems, specifically PDGF-A and GDF15, were responsible for the metabolic activity previously attributed to ISM1. Both proteins copurify through immobilized metal affinity chromatography (IMAC) purification, and recombinant PDGF-AA robustly stimulated AKT phosphorylation at nanomolar concentrations. GDF15 has established roles in metabolism including increased insulin sensitivity and decreased liver lipogenesis, matching ISM1's reported metabolic effects [cao-2025-crystal-structure-abstract].

This controversy remains unresolved and calls for careful reassessment of ISM1's reported metabolic functions using highly purified protein preparations verified for the absence of contaminating growth factors.

Adding further complexity, a recent clinical study found that serum ISM1 levels are positively correlated with macrovascular complications in type 2 diabetic patients [wang-2025-macrovascular-abstract]. Wang et al. demonstrated that ISM1 levels were significantly higher in T2DM subjects than normal controls, and highest in patients with macrovascular complications (median 2.07 ng/mL vs 1.20 ng/mL in T2DM). Positive correlations emerged between ISM1 and systolic/diastolic blood pressure, triglycerides, fasting blood glucose, HbA1c, and insulin resistance markers. This contrasts with earlier observations suggesting that elevated ISM1 may be protective against diabetes, and suggests context-dependent changes in ISM1 expression during disease progression that warrant further investigation.

### Lung Homeostasis and Inflammatory Regulation

ISM1 is highly expressed in the mouse and human lung and plays important roles in pulmonary homeostasis. ISM1-deficient mice exhibit spontaneous and progressive lung emphysema, increased alveolar macrophage number and functional heterogeneity, enduring lung inflammation, and significant lung function decline, phenotypes similar to human COPD [nguyen-2022-lung-injury-abstract]. ISM1 functions as a lung-resident anti-inflammatory protein that selectively triggers apoptosis of alveolar macrophages harboring high levels of cell-surface GRP78.

In acute lung injury models, ISM1 deficiency leads to heightened acute inflammatory response with enhanced neutrophil and monocyte infiltration, increased pro-inflammatory cytokines including TNF-alpha, and greater post-injury fibrosis [nguyen-2022-lung-injury-abstract]. ISM1 suppresses inflammation through NF-kappaB pathway inhibition. Therapeutically, intranasal delivery of recombinant ISM1 reduces LPS-induced leukocyte infiltration and dampens inflammatory cascades, suggesting potential clinical applications for ARDS and pulmonary fibrosis.

## The Isthmin Protein Family: ISM1 and ISM2

ISM1 belongs to a small protein family that includes ISM2 (also known as Tail), both containing the characteristic TSR-AMOP domain architecture [valle-dorado-2022-isthmin-family-abstract]. Human ISM1 (~60 kDa) and ISM2 (~63.9 kDa) share similar structures but exhibit distinct expression patterns and potentially different functions.

ISM1 is located on human chromosome 20 (20p12.1), comprising 464 amino acids encoded by six exons spanning 77.7 kb. In zebrafish, while the teleost genome was duplicated early in evolution, there is only one ism1 copy that shares synteny with human ISM1, whereas two ism2 paralogs exist (ism2a and ism2b) on different chromosomes [berrun-2018-hematopoiesis-abstract][valle-dorado-2022-isthmin-family-abstract].

Phylogenetic analysis demonstrates remarkable conservation of both ISM1 and ISM2 across vertebrates, suggesting important cellular functions [valle-dorado-2022-isthmin-family-abstract]. ISM1 contains a "WSLW motif" while ISM2 has "WSPW," both potentially involved in heparin binding. Both proteins possess an RKD motif in the AMOP domain implicated in integrin binding, though structural studies have challenged whether this motif can actually engage integrins.

The functional relationship between ISM1 and ISM2 remains incompletely characterized. In developmental timing, ism1 expression in zebrafish is detected early during shield stage, tail-bud stage, and early somitogenesis, while ism2 expression is not detected until 24 hours post-fertilization [valle-dorado-2022-isthmin-family-abstract]. In pathological contexts, ISM1 and ISM2 show differential expression: in preeclampsia, trophoblastic cells strongly express ISM1 while serum ISM2 concentrations are reduced; conversely, ISM2 shows prominent expression in choriocarcinoma. Both ISM1 upregulation in multiple cancers (gastric, hepatocellular, colorectal) and ISM2 in choriocarcinoma suggest distinct roles in tumorigenesis [valle-dorado-2022-isthmin-family-abstract].

## Tissue Expression and Localization

ISM1 is a secreted protein that acts extracellularly. In terms of tissue distribution, ISM1 is expressed in diverse tissues including brain, lung, vasculature, skin, mucosal surfaces, and selected lymphocyte populations [li-2023-isthmin-review-abstract][valle-dorado-2022-isthmin-family-abstract]. The lung shows particularly high expression, establishing ISM1 as a lung-resident protein with immunomodulatory functions.

A detailed study of ISM1 expression in the immune system revealed selective expression in specific lymphocyte populations [valle-rios-2014-immune-cells-abstract]. ISM1 is expressed by DX5+NKp46+ NK and NKT cells in mouse lung. Notably, ISM1 expression increases significantly when CD4+ T cells are polarized to the Th17 lineage in vitro, with expression levels correlating with RORgammat transcription factor levels, a marker of Th17 commitment. Importantly, IFN-gamma inhibits ISM1 expression during T cell polarization, suggesting cytokine-mediated regulation [valle-rios-2014-immune-cells-abstract]. Given ISM1's anti-angiogenic and immunomodulatory properties, these findings suggest ISM1 may mediate effector functions of Th17, NKT, and NK cells in innate and acquired immune responses.

Regarding developmental expression, during embryogenesis ISM1 shows dynamic spatiotemporal expression patterns. In Xenopus, it is strongly expressed maternally and shows zygotic expression in the ventral blastopore lip, notochord, midbrain-hindbrain boundary, neural crest, ear vesicle, and developing blood islands [pera-2002-isthmin-discovery-abstract]. In developing kidney, ISM1 is initially broadly expressed in both condensed and surrounding metanephric mesenchyme and ureteric epithelium at E10.5-E11.5, becoming specifically expressed in mesenchyme from E12.5 onward [gao-2023-kidney-development-abstract].

The protein acts in an autocrine and paracrine manner. As a secreted protein, ISM1 acts on nearby cells expressing appropriate receptors (GRP78, integrins). Its effects on endothelial cells, cancer cells, alveolar macrophages, and mesenchymal cells demonstrate its paracrine signaling capacity.

## Aging and Longevity

Emerging research has identified ISM1 as a potential biomarker of aging and a factor with rejuvenation properties. Li et al. demonstrated that ISM1 expression decreases with age in fish (Nothobranchius guentheri), mice, and humans, with reduced levels observed in liver, muscle, and serum [li-2022-aging-biomarker-abstract]. Strikingly, oral treatment with recombinant ISM1 increased maximum lifespan by 7.2% (from 51.5 to 55.2 weeks) and mean lifespan by 7.5% (from 45.4 to 48.8 weeks) in killifish. Treatment also reduced accumulation of aging markers including liver lipofuscin, reactive oxygen species, and protein oxidation in muscle, suggesting ISM1 may be both an aging biomarker and a potential rejuvenation factor.

Further supporting a role in age-related pathology, cardiac-specific overexpression of ISM1 significantly mitigated insulin resistance and improved cardiac function in aging mice [hu-2024-cardiac-aging-abstract]. ISM1 overexpression alleviated cellular senescence, cardiac inflammation, and dysfunction in both natural and accelerated cardiac aging models. Mechanistically, ISM1 promotes glycolysis and activates SIRT1 (a key longevity-associated deacetylase) through enhancing glucose uptake via GLUT4 translocation [hu-2024-cardiac-aging-abstract]. Since SIRT1 activation extends lifespan in various organisms, these findings position ISM1 as a potential therapeutic target for age-related cardiac disease, though caution is warranted given the evolutionary distance between model organisms and humans.

## Role in Disease

Beyond the developmental disorders discussed above (renal agenesis/hypoplasia, cleft lip/palate), ISM1 has been implicated in several disease contexts.

For cancer, elevated ISM1 expression correlates with progression in gastric cancer, hepatocellular carcinoma, and colorectal cancer, where it serves as an independent prognostic indicator [wu-2021-colorectal-cancer-abstract]. ISM1's role in promoting EMT and correlating with immunosuppressive markers suggests involvement in tumor progression and immunotherapy resistance.

Regarding pulmonary diseases, ISM1 deficiency phenocopies aspects of COPD, and ISM1 dysfunction may contribute to acute lung injury and pulmonary fibrosis [nguyen-2022-lung-injury-abstract].

For metabolic disease, if ISM1's metabolic functions are confirmed following resolution of the recent controversy, reduced ISM1 levels or signaling could contribute to type 2 diabetes and NAFLD [jiang-2021-adipokine-glucose-abstract]. Human studies have shown correlations between circulating ISM1 levels and metabolic parameters, though interpretations remain tentative pending clarification of ISM1's direct metabolic activities.

## Open Questions

Several significant questions remain unresolved in ISM1 biology:

1. **Metabolic function controversy**: The discrepancy between the reported metabolic functions of ISM1 and the recent structural study attributing these effects to contaminants requires resolution. Independent replication with rigorously purified ISM1 preparations is essential.

2. **Receptor identification in adipocytes**: If ISM1 does have metabolic functions, the specific receptor mediating glucose uptake in adipocytes remains unidentified, as neither GRP78 nor known integrins appear responsible.

3. **Paradoxical roles in cancer**: How does ISM1 function as an anti-angiogenic, pro-apoptotic protein yet become elevated in multiple cancers? Understanding this context-dependency may reveal new therapeutic opportunities.

4. **Integrin binding mechanism**: The recent structural data suggesting the RKD motif cannot bind integrins contradicts functional studies demonstrating integrin-mediated effects. The molecular basis of ISM1-integrin interaction requires clarification.

5. **Relationship between ISM1 and ISM2**: While both isthmin family members share the TSR-AMOP architecture, their distinct expression patterns (temporal and tissue-specific) and differential disease associations suggest non-redundant functions that require elucidation.

6. **Therapeutic development**: Given ISM1's anti-angiogenic and pro-apoptotic properties toward cancer cells and its protective effects in lung, development of ISM1-based therapeutics or ISM1 pathway modulators represents an important translational direction.

7. **Post-translational regulation**: How do N-glycosylation and C-mannosylation regulate ISM1 function in different tissues? Are there pathophysiological conditions where altered modification status affects ISM1 activity or receptor binding?

8. **Contradictory clinical findings**: Why do some studies show lower ISM1 in diabetes (suggesting protective effects) while others show elevated ISM1 correlating with macrovascular complications? Understanding the temporal dynamics and tissue-specific regulation of ISM1 during disease progression is critical for therapeutic development.

9. **Hematopoietic mechanisms**: What is the molecular mechanism by which ISM1 supports HSPC generation? Does ISM1 act directly on HSPCs or through the stromal microenvironment? What receptors mediate ISM1's hematopoietic functions?

## References

- [pera-2002-isthmin-discovery-abstract]: Pera EM, Kim JI, Martinez SL, Brechner M, Li SY, Wessely O, De Robertis EM. Isthmin is a novel secreted protein expressed as part of the Fgf-8 synexpression group in the Xenopus midbrain-hindbrain organizer. Mech Dev. 2002;116(1-2):169-72. PMID: 12128218. DOI: 10.1016/s0925-4773(02)00123-5

- [chen-2014-grp78-apoptosis-abstract]: Chen M, Zhang Y, Yu VC, Chong YS, Yoshioka T, Ge R. Isthmin targets cell-surface GRP78 and triggers apoptosis via induction of mitochondrial dysfunction. Cell Death Differ. 2014;21(5):797-810. PMID: 24464222. PMCID: PMC3978310. DOI: 10.1038/cdd.2014.3

- [zhang-2011-integrin-dual-effect-abstract]: Zhang Y, Chen M, Venugopal S, Zhou Y, Xiang W, Li YH, Lin Q, Kini RM, Chong YS, Ge R. Isthmin exerts pro-survival and death-promoting effect on endothelial cells through alphavbeta5 integrin depending on its physical state. Cell Death Dis. 2011;2(5):e153. PMID: 21544092. DOI: 10.1038/cddis.2011.37

- [jiang-2021-adipokine-glucose-abstract]: Jiang Z, Zhao M, Voilquin L, et al. Isthmin-1 is an adipokine that promotes glucose uptake and improves glucose tolerance and hepatic steatosis. Cell Metab. 2021;33(9):1836-1852.e11. PMID: 34348115. PMCID: PMC8429235. DOI: 10.1016/j.cmet.2021.07.010

- [osorio-2019-nodal-signaling-abstract]: Osório L, Wu X, Wang L, Jiang Z, Neideck C, Sheng G, Zhou Z. ISM1 regulates NODAL signaling and asymmetric organ morphogenesis during development. J Cell Biol. 2019;218(7):2388-2402. PMID: 31171630. PMCID: PMC6605798. DOI: 10.1083/jcb.201801081

- [gao-2023-kidney-development-abstract]: Gao G, Li X, Jiang Z, et al. Isthmin-1 (Ism1) modulates renal branching morphogenesis and mesenchyme condensation during early kidney development. Nat Commun. 2023;14:2459. PMID: 37185772. PMCID: PMC10130008. DOI: 10.1038/s41467-023-37992-x

- [venugopal-2015-vascular-permeability-abstract]: Venugopal S, Chen M, Liao W, Er SY, Wong WSF, Ge R. Isthmin is a novel vascular permeability inducer that functions through cell-surface GRP78-mediated Src activation. Cardiovasc Res. 2015;107(1):131-42. PMID: 25952901. DOI: 10.1093/cvr/cvv142

- [nguyen-2022-lung-injury-abstract]: Nguyen N, Xu S, Lam TYW, Liao W, Wong WSF, Ge R. ISM1 suppresses LPS-induced acute lung injury and post-injury lung fibrosis in mice. Mol Med. 2022;28:72. PMID: 35745564. PMCID: PMC9233842. DOI: 10.1186/s10020-022-00500-w

- [li-2023-isthmin-review-abstract]: Li J, Zhao X, Xin X, et al. Advances in research of biological functions of Isthmin-1. J Cell Commun Signal. 2023;17:507-521. PMID: 36635535. PMCID: PMC10409700. DOI: 10.1007/s12079-023-00732-3

- [wu-2021-colorectal-cancer-abstract]: Wu Y, Liang X, Ni J, Zhao R, Shao S, Lu S, Han W, Yu L. Effect of ISM1 on the Immune Microenvironment and Epithelial-Mesenchymal Transition in Colorectal Cancer. Front Cell Dev Biol. 2021;9:681240. DOI: 10.3389/fcell.2021.681240

- [valle-dorado-2022-isthmin-family-abstract]: Valle-Dorado MG, et al. Isthmin—A Multifaceted Protein Family. Int J Mol Sci. 2022;24(1):133. PMCID: PMC9818725. DOI: 10.3390/ijms24010133

- [cao-2025-crystal-structure-abstract]: Cao J, et al. Crystal structure of Isthmin-1 and reassessment of its functional role in pre-adipocyte signaling. Nat Commun. 2025;16:3675. PMID: 40234450. PMCID: PMC12000326. DOI: 10.1038/s41467-025-58828-w

- [yoshimoto-2021-cmannosylation-abstract]: Yoshimoto S, Katayama K, Suzuki T, Dohmae N, Simizu S. Regulation of N-glycosylation and secretion of Isthmin-1 by its C-mannosylation. Biochim Biophys Acta Gen Subj. 2021;1865(3):129840. PMID: 33412225. DOI: 10.1016/j.bbagen.2020.129840

- [berrun-2018-hematopoiesis-abstract]: Berrun A, Harris E, Stachura DL. Isthmin 1 (ism1) is required for normal hematopoiesis in developing zebrafish. PLoS One. 2018;13(5):e0196872. PMID: 29758043. PMCID: PMC5951578. DOI: 10.1371/journal.pone.0196872

- [wang-2025-macrovascular-abstract]: Wang Y, Feng Y, Wang X, et al. Serum Isthmin-1 levels are positively correlated with macrovascular complications in type 2 diabetic patients. Front Endocrinol. 2025;16:1594158. DOI: 10.3389/fendo.2025.1594158

- [li-2022-aging-biomarker-abstract]: Li C, Song L, Zhou Y, Yuan J, Zhang S. Identification of Isthmin1 in the small annual fish, Nothobranchius guentheri, as a novel biomarker of aging and its potential rejuvenation activity. Biogerontology. 2022;23(1):99-114. PMID: 34988750. DOI: 10.1007/s10522-021-09948-5

- [hu-2024-cardiac-aging-abstract]: Hu M, Zhang X, Gao YP, et al. Isthmin-1 Improves Aging-Related Cardiac Dysfunction in Mice through Enhancing Glycolysis and SIRT1 Deacetylase Activity. Aging Dis. 2024;15(6):2682-2696. PMID: 38300636. PMCID: PMC11567257. DOI: 10.14336/AD.2024.0113

- [kao-2018-bc71-peptide-abstract]: Kao C, Chandna R, Ghode A, et al. Proapoptotic Cyclic Peptide BC71 Targets Cell-Surface GRP78 and Functions as an Anticancer Therapeutic in Mice. EBioMedicine. 2018;33:22-32. PMID: 29907328. PMCID: PMC6085501. DOI: 10.1016/j.ebiom.2018.06.004

- [valle-rios-2014-immune-cells-abstract]: Valle-Rios R, Maravillas-Montero JL, Burkhardt AM, et al. Isthmin 1 is a secreted protein expressed in skin, mucosal tissues, and NK, NKT, and Th17 cells. J Interferon Cytokine Res. 2014;34(10):795-801. PMID: 24956034. PMCID: PMC4186767. DOI: 10.1089/jir.2013.0137


## Citations

1. berrun-2018-hematopoiesis-abstract.md
2. cao-2025-crystal-structure-abstract.md
3. chen-2014-grp78-apoptosis-abstract.md
4. chen-2014-grp78-apoptosis-summary.md
5. gao-2023-kidney-development-abstract.md
6. hu-2024-cardiac-aging-abstract.md
7. jiang-2021-adipokine-glucose-abstract.md
8. jiang-2021-adipokine-glucose-summary.md
9. kao-2018-bc71-peptide-abstract.md
10. li-2022-aging-biomarker-abstract.md
11. li-2023-isthmin-review-abstract.md
12. nguyen-2022-lung-injury-abstract.md
13. osorio-2019-nodal-signaling-abstract.md
14. pera-2002-isthmin-discovery-abstract.md
15. valle-dorado-2022-isthmin-family-abstract.md
16. valle-rios-2014-immune-cells-abstract.md
17. venugopal-2015-vascular-permeability-abstract.md
18. wang-2025-macrovascular-abstract.md
19. wu-2021-colorectal-cancer-abstract.md
20. yoshimoto-2021-cmannosylation-abstract.md
21. zhang-2011-integrin-dual-effect-abstract.md