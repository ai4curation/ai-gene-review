---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-15T17:06:50.839646'
end_time: '2026-01-15T17:25:50.516744'
duration_seconds: 1139.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ATF4
  gene_symbol: ATF4
  uniprot_accession: P18848
  protein_description: 'RecName: Full=Cyclic AMP-dependent transcription factor ATF-4
    {ECO:0000305}; Short=cAMP-dependent transcription factor ATF-4 {ECO:0000305};
    AltName: Full=Activating transcription factor 4 {ECO:0000303|PubMed:2516827};
    AltName: Full=Cyclic AMP-responsive element-binding protein 2 {ECO:0000303|PubMed:1534408};
    Short=CREB-2 {ECO:0000303|PubMed:1534408}; Short=cAMP-responsive element-binding
    protein 2 {ECO:0000303|PubMed:1534408}; AltName: Full=Tax-responsive enhancer
    element-binding protein 67 {ECO:0000303|PubMed:1847461}; Short=TaxREB67 {ECO:0000303|PubMed:1847461};'
  gene_info: Name=ATF4 {ECO:0000303|PubMed:2516827, ECO:0000312|HGNC:HGNC:786}; Synonyms=CREB2
    {ECO:0000303|PubMed:1534408}, TXREB {ECO:0000303|PubMed:1847461};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the bZIP family. .
  protein_domains: bZIP. (IPR004827); bZIP_sf. (IPR046347); bZIP_1 (PF00170)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 10
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P18848
- **Protein Description:** RecName: Full=Cyclic AMP-dependent transcription factor ATF-4 {ECO:0000305}; Short=cAMP-dependent transcription factor ATF-4 {ECO:0000305}; AltName: Full=Activating transcription factor 4 {ECO:0000303|PubMed:2516827}; AltName: Full=Cyclic AMP-responsive element-binding protein 2 {ECO:0000303|PubMed:1534408}; Short=CREB-2 {ECO:0000303|PubMed:1534408}; Short=cAMP-responsive element-binding protein 2 {ECO:0000303|PubMed:1534408}; AltName: Full=Tax-responsive enhancer element-binding protein 67 {ECO:0000303|PubMed:1847461}; Short=TaxREB67 {ECO:0000303|PubMed:1847461};
- **Gene Information:** Name=ATF4 {ECO:0000303|PubMed:2516827, ECO:0000312|HGNC:HGNC:786}; Synonyms=CREB2 {ECO:0000303|PubMed:1534408}, TXREB {ECO:0000303|PubMed:1847461};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the bZIP family. .
- **Key Domains:** bZIP. (IPR004827); bZIP_sf. (IPR046347); bZIP_1 (PF00170)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ATF4" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ATF4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ATF4** (gene ID: ATF4, UniProt: P18848) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ATF4 (Activating Transcription Factor 4): A Comprehensive Review

## Introduction

Activating Transcription Factor 4 (ATF4), also known as CREB-2 (cAMP response element-binding protein 2) or TaxREB67, is a basic leucine zipper (bZIP) transcription factor that serves as a master regulator of cellular stress responses in eukaryotes. ATF4 (UniProt: P18848) is encoded by the *ATF4* gene on human chromosome 22q13.1 and produces a 351 amino acid protein that functions as a central effector of the Integrated Stress Response (ISR) [pakos-zebrucka-2016-isr-review-summary]. Unlike typical transcription factors that are primarily regulated at the transcriptional level, ATF4 is predominantly controlled through a sophisticated translational mechanism involving upstream open reading frames (uORFs) that enable preferential translation under stress conditions when global protein synthesis is suppressed [young-wek-2016-uorf-summary].

ATF4 belongs to the ATF/CREB family of transcription factors, which are characterized by their ability to bind cAMP response elements (CREs) in target gene promoters. The protein was first molecularly cloned in 1992 by Karpinski and colleagues from a Jurkat T-cell cDNA library, where it was initially characterized as a transcriptional repressor of CRE-dependent transcription [karpinski-1992-creb2-cloning-summary]. Subsequent research has revealed that ATF4 can function as both an activator and repressor of transcription depending on its dimerization partners and post-translational modifications. ATF4 plays pivotal roles in amino acid metabolism, oxidative stress response, autophagy, apoptosis, and development, making it a critical nexus point in cellular adaptation to environmental challenges [neill-2023-atf4-review-summary].

## Protein Structure and DNA Binding Mechanism

The 351 amino acid ATF4 protein is organized into two major functional domains: an N-terminal transactivation domain (TAD, residues 1-275) and a C-terminal basic leucine zipper (bZIP) domain (residues 276-351). The N-terminal domain, which includes a p300 interaction site, functions as a transcriptional activation domain and is also implicated in regulating protein stability. Structurally, the N-terminal transactivation domain is intrinsically disordered, a feature that allows for flexible interactions with multiple binding partners and regulatory proteins.

The C-terminal bZIP domain is essential for ATF4's DNA binding and dimerization functions. This domain comprises three distinct regions: a DNA binding region (DB, residues 280-301), a leucine zipper region (LZ, residues 306-340), and a secondary basic motif (B2, residues 341-351) that is shared exclusively with its closest paralogue, ATF5. The leucine zipper region contains the characteristic heptad repeat with leucine residues at every seventh position, enabling homo- and heterodimerization through coiled-coil interactions. Structural studies using proteolysis, electrophoretic mobility shift assays, circular dichroism, and NMR have demonstrated that the bZIP domain of ATF4 exists as a disordered monomer in solution but forms a homodimer upon binding to target DNA sequences.

ATF4 binds to the cAMP response element (CRE) with the consensus sequence 5'-GTGACGT[AC][AG]-3'. Notably, ATF4 binds to asymmetric CREs as a heterodimer and to palindromic CREs as a homodimer. A crystal structure of the C/EBPβ-ATF4 bZIP heterodimer revealed that the heterodimer forms an asymmetric coiled-coil structure. Intriguingly, even in the absence of DNA, the basic region of ATF4 forms a continuous alpha-helix, while the basic region of C/EBPβ remains disordered, suggesting a structural asymmetry that may contribute to target gene specificity.

The selection of target genes regulated by ATF4 is critically dependent on its dimerization partners. Neill and Masson catalogued 14 direct dimerization partners for ATF4, predominantly bZIP transcription factors including CEBPB, CEBPG, JUN, and DDIT3/CHOP [neill-2023-atf4-review-summary]. Work in mice has identified CEBPG as the main ATF4 heterodimerization partner for inducing stress-responsive genes. ATF4 can also heterodimerize with JUN, FOS, and FRA1 to bind CRE sequences, or with CHOP to regulate a distinct subset of pro-apoptotic genes. These partnerships function as "combinatorial switches" that select target gene subsets depending on the cellular context and nature of the stress stimulus.

## Translational Regulation via Upstream Open Reading Frames

One of the most distinctive features of ATF4 regulation is the sophisticated mechanism by which its translation is controlled. Although ATF4 mRNA is constitutively expressed in cells, ATF4 protein levels are kept low under normal conditions through a translational repression mechanism involving upstream open reading frames (uORFs) in the 5' untranslated region [young-wek-2016-uorf-summary]. This mechanism enables a paradoxical increase in ATF4 translation precisely when global protein synthesis is suppressed during cellular stress.

The 5' UTR of ATF4 mRNA contains two uORFs in strong Kozak sequences: uORF1 is only 3 codons long, while uORF2 is 59 amino acids long and overlaps out-of-frame with the main ATF4 coding sequence. Under normal non-stress conditions, when the eukaryotic initiation factor 2 (eIF2) ternary complex (eIF2-GTP-Met-tRNAi) is abundant, ribosomes translate the short uORF1, remain attached to the mRNA, resume scanning downstream, and rapidly reacquire the ternary complex before encountering uORF2. Translation of uORF2 then prevents initiation at the ATF4 main open reading frame because of the out-of-frame overlap.

During cellular stress, the picture changes dramatically. Stress signals activate one of four eIF2α kinases (PERK, GCN2, PKR, or HRI), leading to phosphorylation of eIF2α at serine 51. Phosphorylated eIF2α binds more strongly to eIF2B, inhibiting its guanine nucleotide exchange factor (GEF) function and reducing the available pool of eIF2 ternary complex. Under these conditions, ribosomes that translate uORF1 and resume scanning take longer to reacquire the ternary complex. By the time they do so, many have bypassed uORF2, allowing them to instead reinitiate translation at the ATF4 main coding sequence. This "delayed reinitiation" mechanism elegantly couples stress-induced eIF2α phosphorylation to preferential ATF4 translation [young-wek-2016-uorf-summary].

Recent studies have identified additional regulators of this translational mechanism. The noncanonical initiation factors eIF2D and DENR are critical for ATF4 induction, with loss of these factors in *Drosophila* resulting in increased vulnerability to amino acid deprivation, susceptibility to retinal degeneration caused by ER stress, and developmental defects similar to ATF4 mutants.

## Evolutionary Conservation with Yeast GCN4

The translational control mechanism governing ATF4 expression is remarkably conserved across eukaryotes, reflecting its fundamental importance in cellular stress responses. In the budding yeast *Saccharomyces cerevisiae*, the transcription factor GCN4 serves as the functional homolog of mammalian ATF4, orchestrating the general amino acid control (GAAC) response to amino acid starvation [hinnebusch-2005-gcn4-review-summary]. Like ATF4, GCN4 is a bZIP transcription factor whose translation is regulated by upstream open reading frames in response to eIF2α phosphorylation. GCN4 contains four short uORFs in its 5' leader (compared to two in ATF4), but the fundamental mechanism of delayed reinitiation is conserved: under amino acid sufficiency, the uORFs repress GCN4 translation, while during starvation, reduced eIF2 ternary complex availability allows ribosomes to bypass the inhibitory uORFs and translate GCN4.

The eIF2α/GCN2 signaling pathway upstream of this translational control is extremely well conserved, with GCN2 protein kinases phosphorylating eIF2α in response to uncharged tRNA accumulation across fungi, mammals, plants, and parasitic organisms including *Plasmodium* and *Toxoplasma*. GCN4 regulates the expression of more than 500 genes in yeast, including nearly all genes encoding amino acid biosynthetic enzymes. Interestingly, despite the conservation of the signaling pathway, the downstream transcription factors themselves have diverged considerably. GCN4 is not conserved beyond the Saccharomycotina, and ATF4 is not conserved beyond metazoans. In fission yeast *Schizosaccharomyces pombe*, a GATA-type transcription factor called Fil1, which lacks any sequence homology to GCN4 or ATF4, mediates the amino acid starvation response through similar regulatory mechanisms. This remarkable example of transcriptional network plasticity demonstrates that evolution can maintain conserved regulatory principles while substituting nonorthologous transcription factors.

Beyond its role in starvation responses, GCN4 has been found to reduce protein synthesis capacity and extend yeast lifespan, suggesting that the growth-limiting functions of the GCN4/ATF4 pathway may have beneficial effects on organismal longevity. This is consistent with observations that ATF4 activity is a common feature shared by multiple slow-aging mouse models.

## The Integrated Stress Response and ATF4 as Central Effector

ATF4 is described as "the main effector of the integrated stress response (ISR)" [pakos-zebrucka-2016-isr-review-summary], a fundamental cellular adaptation mechanism that helps cells respond to diverse stressors while maintaining homeostasis. The ISR is activated when any of four stress-sensing kinases phosphorylate eIF2α at serine 51, converging on the common outcome of reduced global translation and increased ATF4 synthesis.

The four eIF2α kinases respond to distinct stress stimuli: PERK (PKR-like endoplasmic reticulum kinase) is activated by accumulation of misfolded proteins in the endoplasmic reticulum; GCN2 (general control nonderepressible 2) responds to amino acid deprivation and uncharged tRNA accumulation; PKR (double-stranded RNA-dependent protein kinase) is activated by viral double-stranded RNA; and HRI (heme-regulated eIF2α kinase) responds to heme deficiency and mitochondrial stress primarily in erythroid cells. Despite these different upstream triggers, all four kinases converge on eIF2α phosphorylation and subsequent ATF4 induction, providing a unified cellular response to diverse stresses.

Once translated, ATF4 accumulates in the nucleus where it binds to specific DNA regulatory elements to activate transcription of stress-responsive genes. ATF4 regulates target genes through C/EBP-ATF response elements (CAREs), which can mediate transcriptional activation in response to various stimuli. The gene expression program activated by the ISR is context-dependent, influenced by the cellular identity, the nature and intensity of the stress, and the duration of stress exposure. While the ISR is primarily a pro-survival, homeostatic program, prolonged or severe stress can redirect ATF4 signaling toward pro-apoptotic outcomes [pakos-zebrucka-2016-isr-review-summary].

## ATF4 in the Unfolded Protein Response and ER Stress

ATF4 plays a central role in the PERK arm of the unfolded protein response (UPR), the cellular program activated when misfolded proteins accumulate in the endoplasmic reticulum. Under ER stress conditions, the ER chaperone BiP (immunoglobulin binding protein) dissociates from the luminal domain of PERK, allowing PERK oligomerization and trans-autophosphorylation. Active PERK then phosphorylates eIF2α, leading to both global translation attenuation and preferential ATF4 synthesis.

ATF4 translocates to the nucleus where it induces expression of ER chaperones, autophagy/apoptosis genes, oxidative response genes, and amino acid metabolism pathways. A key target of ATF4 during ER stress is CHOP (C/EBP homologous protein, also known as DDIT3), a transcription factor that can form heterodimers with ATF4 to regulate additional downstream genes. However, studies in liver-specific ATF4 knockout mice revealed that ATF4's role in the UPR is more limited than previously appreciated from cell culture studies [fusakio-2016-atf4-liver-summary]. RNA-Seq analysis indicated that ATF4 affects only approximately 7.5% of stress-regulated genes in liver, compared to nearly 50% for PERK, suggesting that PERK activates multiple transcriptional networks beyond ATF4. Furthermore, in liver exposed to ER stress, CHOP expression occurs independently of ATF4, with ATF6 serving as a major contributor to CHOP induction.

Nevertheless, ATF4 has tissue-specific and context-dependent roles in the UPR. It is essential for expression of genes involved in oxidative stress response both basally and under stress conditions, and for cholesterol metabolism genes. ATF4 deletion in liver results in increased free cholesterol accumulation under stress and altered cholesterol homeostasis [fusakio-2016-atf4-liver-summary].

## Target Genes and Downstream Functions

ATF4 regulates a diverse set of target genes that control cellular adaptation to stress. Neill and Masson catalogued 41 well-validated ATF4 target genes across multiple studies [neill-2023-atf4-review-summary], which can be grouped into several functional categories.

**Amino Acid Biosynthesis and Transport:** ATF4 is a master regulator of amino acid metabolism, controlling genes essential for biosynthesis of non-essential amino acids and amino acid uptake. Key targets include ASNS (asparagine synthetase), which catalyzes the conversion of aspartate and glutamine to asparagine and glutamate in an ATP-dependent reaction. During amino acid limitation, ATF4 binding to the amino acid response element (AARE) in the ASNS promoter occurs within 30-60 minutes of amino acid deprivation and continues for 3-4 hours. Other amino acid metabolism targets include PSAT1 (phosphoserine aminotransferase 1) and PHGDH (phosphoglycerate dehydrogenase) involved in serine biosynthesis, as well as amino acid transporters such as SLC7A11 (the cystine/glutamate antiporter xCT) and SLC1A5.

**Aminoacyl-tRNA Synthetases:** ATF4 induces the expression of 15 aminoacyl-tRNA synthetases, including CARS (cysteinyl-tRNA synthetase), GARS (glycyl-tRNA synthetase), AARS (alanyl-tRNA synthetase), and SARS (seryl-tRNA synthetase). This coordinated upregulation ensures that cells have adequate capacity for protein synthesis when amino acid availability is restored.

**Autophagy:** ATF4 directly regulates autophagy genes through binding to CRE sites in their promoters. Key autophagy targets include MAP1LC3B (LC3B, a core autophagosome membrane component), BECN1 (Beclin 1), ATG5, ATG7, ATG12, ATG16L1, GABARAP, and the cargo receptors p62/SQSTM1 and NBR1 [rouschop-2010-autophagy-summary]. During severe hypoxia, ATF4 facilitates autophagy through direct binding to the LC3B promoter, providing a mechanistic link between the UPR and the autophagic machinery.

**Oxidative Stress Response:** ATF4 regulates genes that protect cells from oxidative damage, including CTH (cystathionine gamma-lyase), SOD2 (superoxide dismutase 2), and xCT/SLC7A11. The induction of xCT is particularly important because it imports cystine for glutathione biosynthesis, the major cellular antioxidant system [lewerenz-2012-atf4-oxidative-summary]. Recent studies have revealed that ATF4 is an obligatory metabolic activator of NRF2, increasing NRF2 transcription and inducing the glutathione-degrading enzyme CHAC1, which is critically important for maintaining NRF2 activation.

**Pro-apoptotic Factors:** Under conditions of prolonged or severe stress, ATF4 can induce pro-apoptotic genes including CHOP/DDIT3, PUMA, NOXA, and TRB3. The ATF4-CHOP axis is particularly important for the cell death decision. CHOP, an ATF4 target gene and heterodimerization partner, can trigger the intrinsic apoptotic pathway through inhibition of BCL-2 and upregulation of BIM, as well as the extrinsic pathway through upregulation of death receptors DR4 and DR5.

## Subcellular Localization and Trafficking

ATF4 contains a nuclear localization sequence within its C-terminal region that mediates its transport to the nucleus following synthesis. Under basal conditions, ATF4 shows diffuse cellular distribution in both cytoplasm and nucleus at low levels. Upon activation of the ISR, ATF4 protein accumulates and translocates to the nucleus to activate target gene transcription. Studies on TLR4 signaling have documented the kinetics of this translocation: ATF4 initially moves to the cytoplasmic membrane within 5 minutes of stimulation, then gradually enters the nucleus by 15 minutes, achieving complete nuclear localization by 60 minutes.

In neurons, ATF4/CREB2 localizes to distal dendrites and shows importin-mediated retrograde transport to the soma and nucleus. Biochemical studies have demonstrated that ATF4 binds specifically to importins α1 and α6, and this binding is required for transport from distal dendrites to the nucleus. This dendritic localization may be relevant to ATF4's reported role in modulating synaptic plasticity and long-term memory formation.

Importantly, trafficking of ATF4 to the nucleus does not require additional signals from stress pathways beyond its synthesis; ectopically expressed ATF4 localizes predominantly to the nuclear compartment. The Human Protein Atlas documents ATF4 primarily as a nuclear protein with predominant localization in cardiomyocytes.

## Post-Translational Modifications and Protein Stability

ATF4 protein is highly unstable, with a short half-life that allows for rapid changes in protein levels in response to changing conditions. Neill and Masson documented 33 post-translational modifications affecting ATF4, concentrated in the N-terminal and C-terminal bZIP domain regions [neill-2023-atf4-review-summary]. These modifications critically influence ATF4 activity, stability, and target gene selection.

Phosphorylation is the most extensively characterized modification class. Phosphorylation at serine 219 is required for βTRCP-mediated proteasomal degradation, providing a mechanism for rapid ATF4 turnover when stress is resolved. Casein kinase 2 (CK2)-mediated phosphorylation at serine 215, in contrast, increases ATF4 transcriptional activity. RET kinase phosphorylation at multiple sites (T107, T114, T115, T119) reduces expression of pro-apoptotic target genes, potentially biasing ATF4 activity toward pro-survival outcomes. The intricate coupling between the transactivation and bZIP domains governs the efficiency of CK2-mediated phosphorylation, indicating that ATF4's structural organization influences its post-translational regulation.

The balance between ATF4 synthesis and degradation determines net protein levels and, consequently, the transcriptional output. During stress, increased synthesis coupled with stabilization leads to ATF4 accumulation. The ISR includes a negative feedback loop through ATF4-dependent induction of GADD34, which combines with PP1 to dephosphorylate eIF2α and restore normal translation, thereby reducing further ATF4 synthesis.

## Physiological and Developmental Roles

Studies in ATF4 knockout mice have revealed essential physiological functions for this transcription factor in multiple tissues and developmental processes. ATF4-deficient mice exhibit abnormal lens formation, growth retardation, anemia, and delayed bone development.

**Lens Development:** Adult homozygous *Atf4* null mice invariably exhibit severe microphthalmia (small eyes) arising late in embryonic development due to complete aphakia (absence of the eye lens). This phenotype results from p53-mediated apoptosis of anterior lens epithelial cells. RNA-seq analysis revealed that E16.5 *Atf4* null mouse lenses show downregulation of lens epithelial markers and markers of late lens fiber cell differentiation. ATF4 appears to function by metabolically adapting the avascular lens to its unique environment.

**Bone Development and Homeostasis:** ATF4 is critical for bone formation and homeostasis. A landmark 2004 study by Yang, Karsenty, and colleagues identified ATF4 as an essential regulator of osteoblast biology and demonstrated that ATF4 is a critical substrate of the kinase RSK2 [yang-2004-atf4-rsk2-bone-summary]. ATF4-deficient mice display dramatically reduced bone mass and bone formation rate, with severe osteopenia, impaired osteoblast terminal differentiation, reduced osteocalcin expression, and decreased Type I collagen synthesis. The mice show delayed skeletal development and thereafter develop a severe low-bone-mass phenotype caused by decreased bone formation. At the molecular level, ATF4 activates osteocalcin transcription through the osteocalcin-specific element 1 (OSE1) in the promoter and promotes osteoblast differentiation. RSK2 phosphorylates ATF4 at serine 251 (mouse) or serine 245 (human), and this phosphorylation is required for ATF4 to regulate collagen synthesis and osteocalcin expression in osteoblasts. Importantly, the shared skeletal phenotypes between *Atf4*-deficient and *Rsk2*-deficient mice suggest that lack of ATF4 phosphorylation by RSK2 contributes to the skeletal abnormalities observed in Coffin-Lowry Syndrome, a human genetic disorder caused by RSK2 mutations. ATF4 also promotes bone angiogenesis by increasing VEGF expression and release in the bone environment, and ablation of *Atf4* severely impairs skeletal vasculature with reduced microvascular density and decreased expression of HIF-1α and VEGF in osteoblasts. Notably, the connection between ATF4's role in amino acid import and bone formation has nutritional implications: a high-protein diet can partially rescue the skeletal defects in *Atf4*-deficient mice, highlighting how ATF4 links bone formation to nutritional status.

**Metabolism and Energy Homeostasis:** ATF4-null mice are lean, mildly hypoglycemic, and resistant to obesity induced by aging or high-energy diets. This metabolic phenotype suggests roles for ATF4 in lipid metabolism and energy expenditure. Interestingly, ATF4 activity has been identified as a common feature shared by many kinds of slow-aging mice.

**Hematopoiesis:** ATF4-deficient mice show defects in production of erythrocytes by the fetal liver, consistent with the sensitivity of erythroid cells to stress via the HRI kinase pathway.

## ATF4 in Synaptic Plasticity and Memory

ATF4, originally identified as CREB-2, has emerged as an important regulator of synaptic plasticity and memory formation, although its precise role remains complex and context-dependent [chen-2003-atf4-memory-summary]. The initial characterization of ATF4's role in memory came from studies in the marine mollusk *Aplysia*, where the ATF4 homolog ApCREB-2 was identified as an inhibitor of CREB-dependent long-term facilitation (LTF). This finding established the model that ATF4 functions as a "memory suppressor" gene, constraining the formation of long-term memories by opposing CREB-mediated transcription.

In the mammalian hippocampus, the molecular basis of long-term memory involves gene expression mediated by the transcription factor CREB. ATF4 can heterodimerize with CREB and other bZIP factors to repress transcription from CRE-containing promoters, thereby restraining the gene expression programs required for memory consolidation. In 2003, Chen and colleagues demonstrated that transgenic mice expressing a dominant-negative inhibitor of ATF4 and C/EBP proteins (EGFP-AZIP) exhibited enhanced hippocampal-based spatial memory and enhanced long-term potentiation (LTP), a cellular correlate of memory. More recent studies using conditional knockout approaches confirmed that deletion of ATF4 specifically in forebrain excitatory neurons lowers the threshold for LTP induction and enhances long-term memory formation.

The subcellular localization of ATF4 in neurons is particularly relevant to its function in plasticity. ATF4/CREB2 localizes to distal dendrites of hippocampal neurons, where it binds to specific importin α isoforms (importin α1 and α6) for retrograde transport to the nucleus. This dendritic localization positions ATF4 to respond to local synaptic signals and translate them into nuclear transcriptional responses. During long-term synaptic plasticity, ATF4 is removed through ubiquitin-proteasome-mediated proteolysis, relieving its inhibition of CREB-dependent gene expression.

However, the role of ATF4 in memory is not simply inhibitory. Emerging evidence suggests that ATF4 may also have positive functions in specific memory processes, including consolidation of object recognition memory, formation of fear extinction memory, and memory flexibility. A recent study demonstrated that elevating ApCREB2 (the *Aplysia* ATF4 homolog) post-synaptically increased synaptic strength, while doing so pre-synaptically decreased synaptic strength, indicating that ATF4's effects on plasticity are cell-type and compartment-specific. These findings suggest that ATF4 functions as a regulator of excitability and plasticity thresholds rather than a simple memory suppressor, with its net effect depending on cellular context, timing, and the specific memory process involved.

## Cell Fate Decisions: Survival versus Apoptosis

A central question in ATF4 biology is how cells decide between adaptive survival and apoptotic death outcomes during stress. The ISR can output two contradicting outcomes, and ATF4 "pulls multiple potential levers" that can lead to either outcome [neill-2023-atf4-review-summary]. Evidence suggests that the choice depends on multiple factors including heterodimerization partner availability, post-translational modification patterns, stress duration and intensity, and cell type-specific properties.

The relative abundance of different heterodimerization partners appears crucial. CEBPG is the main ATF4 partner for inducing pro-survival stress-responsive genes. In contrast, ATF4-CHOP heterodimers preferentially activate genes that promote apoptosis. The temporal dynamics of ATF4 signaling also matter: early and transient ATF4 activation typically promotes adaptation, while sustained ATF4/CHOP activation shifts the balance toward cell death.

CHOP-mediated apoptosis occurs through multiple mechanisms. CHOP triggers the intrinsic apoptotic pathway through inhibition of BCL-2 and upregulation of BIM and PUMA, which promote BAX-BAK-mediated mitochondrial outer membrane permeabilization, cytochrome c release, and caspase cascade activation. CHOP also directly induces death receptor 5 (DR5) expression, activating the extrinsic apoptotic pathway through FADD and caspase-8. Additionally, CHOP activates calcium-mediated apoptosis through ERO1α, which promotes ER calcium release and downstream CaMKII signaling.

Terminally differentiated cells such as neurons may suppress apoptotic pathways to favor survival, reflecting cell type-specific regulation of the ATF4 response network.

## Therapeutic Implications

Given ATF4's central role in stress responses and cell fate decisions, it has emerged as a potential therapeutic target for multiple disease contexts.

**Cancer:** Many cancer cells exploit the ISR-ATF4 pathway to survive nutrient-poor, hypoxic tumor microenvironments. ATF4-dependent induction of amino acid biosynthesis and transport genes supports tumor cell proliferation under metabolic stress. Elevated ASNS expression, an ATF4 target, is associated with resistance to asparaginase therapy in acute lymphoblastic leukemia and may predict drug sensitivity in solid tumors. Targeting the PERK-ATF4-CHOP pathway has been explored as a strategy to induce cancer cell death, with compounds that activate this pathway showing efficacy against HTLV-1-infected cells.

**Neurodegeneration:** The ISR has been implicated in neurodegenerative diseases where protein misfolding and ER stress occur. ISR enhancers such as Guanabenz and Sephin1, which inhibit GADD34 and prolong eIF2α phosphorylation, show potential benefits in some neurodegenerative contexts. Conversely, ISRIB (integrated stress response inhibitor), which renders cells insensitive to eIF2α phosphorylation, has shown cognitive-enhancing effects in aged mice.

**Metabolic Disease:** ATF4's roles in lipid metabolism, glucose homeostasis, and energy expenditure suggest potential relevance to obesity and diabetes therapies.

## Open Questions

Despite extensive research on ATF4, several important questions remain unresolved:

1. **Heterodimerization Specificity:** What determines which dimerization partner ATF4 associates with in a given cellular context, and how does this selection mechanism operate at the molecular level?

2. **Cell Fate Decision Mechanism:** What is the precise mechanism that determines whether ATF4 activation leads to adaptive survival or apoptosis? How do cells "integrate" stress intensity and duration into this decision?

3. **Tissue-Specific Functions:** How do ATF4's functions differ across tissues, and what accounts for the tissue-specific phenotypes in ATF4 knockout mice? Are there tissue-specific dimerization partners or post-translational modifications?

4. **ATF4 in Immunity:** Emerging evidence suggests roles for ATF4 in immune cell function and inflammation. What are the specific functions of ATF4 in different immune cell populations?

5. **Non-transcriptional Functions:** Does ATF4 have functions beyond transcriptional regulation, such as cytoplasmic roles or direct protein-protein interactions that influence signaling?

6. **Therapeutic Window:** For therapeutic modulation of the ATF4 pathway, what is the optimal approach to achieve beneficial effects while avoiding adverse outcomes in normal tissues?

7. **Evolution of ATF4 Regulation:** The uORF-mediated translational control mechanism is highly conserved from yeast (GCN4) to mammals. What evolutionary pressures maintained this complex regulatory mechanism, and are there species-specific variations in ATF4 function?

## References

1. **[neill-2023-atf4-review-summary]** Neill G, Masson GR. A stay of execution: ATF4 regulation and potential outcomes for the integrated stress response. Front Mol Neurosci. 2023;16:1112253. PMID: 36825279; PMCID: PMC9941348. doi:10.3389/fnmol.2023.1112253. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9941348/

2. **[pakos-zebrucka-2016-isr-review-summary]** Pakos-Zebrucka K, Koryga I, Mnich K, Ljujic M, Samali A, Gorman AM. The integrated stress response. EMBO Rep. 2016;17(10):1374-1395. PMID: 27629041; PMCID: PMC5048378. doi:10.15252/embr.201642195. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5048378/

3. **[karpinski-1992-creb2-cloning-summary]** Karpinski BA, Morle GD, Huggenvik J, Uhler MD, Leiden JM. Molecular cloning of human CREB-2: an ATF/CREB transcription factor that can negatively regulate transcription from the cAMP response element. Proc Natl Acad Sci U S A. 1992;89(11):4820-4824. PMID: 1534408; PMCID: PMC49179. doi:10.1073/pnas.89.11.4820. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC49179/

4. **[young-wek-2016-uorf-summary]** Young SK, Wek RC. Upstream Open Reading Frames Differentially Regulate Gene-specific Translation in the Integrated Stress Response. J Biol Chem. 2016;291(33):16927-16935. PMID: 27358398; PMCID: PMC5016099. doi:10.1074/jbc.R116.733899. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5016099/

5. **[fusakio-2016-atf4-liver-summary]** Fusakio ME, Willy JA, Wang Y, Mirek ET, Al Baghdadi RJ, Adams CM, Anthony TG, Wek RC. Transcription factor ATF4 directs basal and stress-induced gene expression in the unfolded protein response and cholesterol metabolism in the liver. Mol Biol Cell. 2016;27(9):1536-1551. PMID: 26960794; PMCID: PMC4850040. doi:10.1091/mbc.E16-01-0039. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4850040/

6. **[rouschop-2010-autophagy-summary]** Rouschop KM, van den Beucken T, Dubois L, et al. Regulation of autophagy by ATF4 in response to severe hypoxia. Oncogene. 2010;29(31):4424-4435. PMID: 20514020. doi:10.1038/onc.2010.191. URL: https://pubmed.ncbi.nlm.nih.gov/20514020/

7. **[lewerenz-2012-atf4-oxidative-summary]** Lewerenz J, Maher P. Mutation of ATF4 mediates resistance of neuronal cell lines against oxidative stress by inducing xCT expression. Cell Death Differ. 2011;18(5):847-858. PMID: 21200489. doi:10.1038/cdd.2011.165. URL: https://pubmed.ncbi.nlm.nih.gov/21200489/

8. **C/EBPβ-ATF4 structure:** Podust LM, Krezel AM, Kim Y. Crystal structure of the CCAAT box/enhancer binding protein beta activating transcription factor-4 basic leucine zipper heterodimer in the absence of DNA. J Biol Chem. 2001;276(1):505-513. PMID: 11018027. doi:10.1074/jbc.M005594200. URL: https://pubmed.ncbi.nlm.nih.gov/11018027/

9. **ATF4-NRF2 interaction:** Sarcinelli C, Sharma H, Mossoba ME, et al. The integrated stress response effector ATF4 is an obligatory metabolic activator of NRF2. Cell Rep. 2023;42(7):112724. PMID: 37410595. doi:10.1016/j.celrep.2023.112724. URL: https://pubmed.ncbi.nlm.nih.gov/37410595/

10. **ASNS regulation:** Kilberg MS, Balasubramanian M, Fu L, Shan J. The transcription factor network associated with the amino acid response in mammalian cells. Adv Nutr. 2012;3(3):295-306. PMID: 22585903; PMCID: PMC3649461. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3625782/

11. **PERK-ATF4-CHOP pathway:** Wang M, Kaufman RJ. The Role of the PERK/eIF2α/ATF4/CHOP Signaling Pathway in Tumor Progression During Endoplasmic Reticulum Stress. Curr Mol Med. 2016;16(6):533-544. PMID: 27211800; PMCID: PMC5008685. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5008685/

12. **CHOP review:** Yang Y, Liu L, Naik I, Braunstein Z, Zhong J, Ren B. Transcription Factor C/EBP Homologous Protein in Health and Diseases. Front Immunol. 2017;8:1612. PMID: 29230208; PMCID: PMC5711810. doi:10.3389/fimmu.2017.01612. URL: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2017.01612/full

13. **ATF4 B2 motif:** Shirafuji T, et al. Fine-Tuning of ATF4 DNA Binding Activity by a Secondary Basic Motif Unique to the ATF-X Subfamily of bZip Transcription Factors. Biochemistry. 2024. doi:10.1021/acs.biochem.4c00640. URL: https://pubs.acs.org/doi/10.1021/acs.biochem.4c00640

14. **Importin-mediated transport:** Lai KO, Zhao Y, Ch'ng TH, Martin KC. Importin-mediated retrograde transport of CREB2 from distal processes to the nucleus in neurons. Proc Natl Acad Sci U S A. 2008;105(44):17175-17180. PMID: 18957548; PMCID: PMC2579388. doi:10.1073/pnas.0803906105. URL: https://www.pnas.org/doi/10.1073/pnas.0803906105

15. **Human Protein Atlas - ATF4:** Subcellular localization. URL: https://www.proteinatlas.org/ENSG00000128272-ATF4/subcellular

16. **[yang-2004-atf4-rsk2-bone-summary]** Yang X, Matsuda K, Bialek P, et al. ATF4 is a substrate of RSK2 and an essential regulator of osteoblast biology: implication for Coffin-Lowry Syndrome. Cell. 2004;117(3):387-398. PMID: 15109498. doi:10.1016/S0092-8674(04)00344-7. URL: https://pubmed.ncbi.nlm.nih.gov/15109498/

17. **[hinnebusch-2005-gcn4-review-summary]** Hinnebusch AG. Translational regulation of GCN4 and the general amino acid control of yeast. Annu Rev Microbiol. 2005;59:407-450. PMID: 16153175. doi:10.1146/annurev.micro.59.031805.133833. URL: https://pubmed.ncbi.nlm.nih.gov/16153175/

18. **[chen-2003-atf4-memory-summary]** Chen A, Muzzio IA, Bhardwaj SK, et al. Inducible enhancement of memory storage and synaptic plasticity in transgenic mice expressing an inhibitor of ATF4 (CREB-2) and C/EBP proteins. Neuron. 2003;39(4):655-669. PMID: 12925279. doi:10.1016/S0896-6273(03)00501-4. URL: https://pubmed.ncbi.nlm.nih.gov/12925279/

19. **ATF4 in fission yeast:** Duncan CDS, Rodriguez-Lopez M, Rechnitzer C, et al. General amino acid control in fission yeast is regulated by a nonconserved transcription factor, with functions analogous to Gcn4/Atf4. Proc Natl Acad Sci U S A. 2018;115(8):E1829-E1838. PMID: 29432178; PMCID: PMC5828588. doi:10.1073/pnas.1713991115. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5828588/

20. **GCN4 and lifespan:** Postnikoff SDL, Johnson JE, Tyler JK. The Gcn4 transcription factor reduces protein synthesis capacity and extends yeast lifespan. Nat Commun. 2017;8:457. doi:10.1038/s41467-017-00539-y. URL: https://www.nature.com/articles/s41467-017-00539-y

21. **ATF4 deletion enhances LTP:** Oren DA, Bhardwaj SK, et al. The ISR downstream target ATF4 represses long-term memory in a cell type–specific manner. Proc Natl Acad Sci U S A. 2024. PMID: pending. doi:10.1073/pnas.2407472121. URL: https://www.pnas.org/doi/10.1073/pnas.2407472121



## Citations

1. chen-2003-atf4-memory-summary.md
2. fusakio-2016-atf4-liver-summary.md
3. hinnebusch-2005-gcn4-review-summary.md
4. karpinski-1992-creb2-cloning-summary.md
5. lewerenz-2012-atf4-oxidative-summary.md
6. neill-2023-atf4-review-summary.md
7. pakos-zebrucka-2016-isr-review-summary.md
8. rouschop-2010-autophagy-summary.md
9. yang-2004-atf4-rsk2-bone-summary.md
10. young-wek-2016-uorf-summary.md