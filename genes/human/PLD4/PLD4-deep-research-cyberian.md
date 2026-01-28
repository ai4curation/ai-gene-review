---
provider: cyberian
model: deep-research
cached: true
start_time: '2026-01-23T16:52:50.287520'
end_time: '2026-01-23T16:52:50.289725'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PLD4
  gene_symbol: PLD4
  uniprot_accession: Q96BZ4
  protein_description: 'RecName: Full=5''-3'' exonuclease PLD4 {ECO:0000305}; EC=3.1.16.1
    {ECO:0000250|UniProtKB:Q8BG07}; AltName: Full=(S,S)-bis(monoacylglycero)phosphate
    synthase PLD4 {ECO:0000305|PubMed:39423811}; EC=3.1.4.- {ECO:0000269|PubMed:39423811};
    AltName: Full=Phospholipase D family member 4; AltName: Full=Phospholipase D4;'
  gene_info: Name=PLD4 {ECO:0000303|PubMed:30111894, ECO:0000312|HGNC:HGNC:23792};
    Synonyms=C14orf175; ORFNames=UNQ2488/PRO5775;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the phospholipase D family. .
  protein_domains: Diverse_PLD-related. (IPR050874); PLDc_3. (IPR032803); PLipase_D/transphosphatidylase.
    (IPR001736); PLDc_3 (PF13918)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 18
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q96BZ4
- **Protein Description:** RecName: Full=5'-3' exonuclease PLD4 {ECO:0000305}; EC=3.1.16.1 {ECO:0000250|UniProtKB:Q8BG07}; AltName: Full=(S,S)-bis(monoacylglycero)phosphate synthase PLD4 {ECO:0000305|PubMed:39423811}; EC=3.1.4.- {ECO:0000269|PubMed:39423811}; AltName: Full=Phospholipase D family member 4; AltName: Full=Phospholipase D4;
- **Gene Information:** Name=PLD4 {ECO:0000303|PubMed:30111894, ECO:0000312|HGNC:HGNC:23792}; Synonyms=C14orf175; ORFNames=UNQ2488/PRO5775;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the phospholipase D family. .
- **Key Domains:** Diverse_PLD-related. (IPR050874); PLDc_3. (IPR032803); PLipase_D/transphosphatidylase. (IPR001736); PLDc_3 (PF13918)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PLD4" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PLD4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PLD4** (gene ID: PLD4, UniProt: Q96BZ4) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PLD4 (Phospholipase D Family Member 4): A Comprehensive Research Report

## Introduction and Summary

Phospholipase D family member 4 (PLD4) is a fascinating example of how protein nomenclature can mislead regarding function. Despite its name suggesting phospholipase activity, PLD4 has been definitively established as a 5'-to-3' single-stranded nucleic acid exonuclease that plays critical roles in immune regulation and, more recently discovered, in lysosomal lipid metabolism [gavin-2018-exonuclease-abstract]. This type II transmembrane glycoprotein localizes to endolysosomes where it performs two biochemically distinct functions: degradation of single-stranded DNA and RNA that would otherwise activate innate immune sensors, and synthesis of bis(monoacylglycero)phosphate (BMP), a phospholipid essential for lysosomal lipid catabolism [singh-2024-bmp-synthase-abstract].

PLD4 is encoded by a gene on human chromosome 14q32.33 and is predominantly expressed in dendritic cells, particularly plasmacytoid dendritic cells (pDCs), as well as microglia in the brain. The protein is structurally related to PLD3, with which it shares considerable functional overlap, though their tissue-specific expression patterns differ substantially. The discovery that PLD4 deficiency causes autoimmune and autoinflammatory diseases, including monogenic systemic lupus erythematosus, has cemented its importance in understanding immune homeostasis [wang-2025-sle-mutations-abstract].

## Enzymatic Function: 5'-3' Exonuclease Activity

### Catalytic Mechanism

PLD4 functions as a 5'-to-3' exonuclease that degrades single-stranded nucleic acids in the acidic environment of endolysosomes. The enzyme contains two conserved HxKxxxxD/E (HKD) motifs characteristic of the phospholipase D superfamily, which form the catalytic core responsible for phosphodiester bond cleavage [yuan-2024-structure-abstract]. Structural studies have revealed that PLD4 employs a "link-and-release" two-step catalytic mechanism. In the first step, His428 (using human PLD4 numbering) from the second HKD motif performs nucleophilic attack on the phosphodiester bond, forming a covalent phospho-histidine intermediate, while His214 from the first HKD motif protonates the leaving 5'-OH ssDNA. In the second step, the deprotonated His214 accepts a proton from an attacking water molecule, which then hydrolyzes the phospho-histidine intermediate to release the product [yuan-2024-structure-abstract].

The crystal structures of PLD4 reveal an intra-chain dimer topology forming a basic active site at the interface, with a narrow and deep catalytic cavity into which the oligonucleotide substrate enters almost vertically [yuan-2024-structure-abstract]. Notably, PLD4 contains an extra hydrophobic clamp not present in PLD3 that stabilizes the substrate and affects oligonucleotide substrate preference and product release, potentially contributing to differences in processivity between the two enzymes.

### Substrate Specificity

PLD4 exhibits exquisite substrate specificity that reflects its endolysosomal function. The enzyme degrades single-stranded DNA and RNA but cannot cleave double-stranded nucleic acids [gavin-2018-exonuclease-abstract]. Key features of substrate recognition include: (1) absolute requirement for unphosphorylated 5' termini, as 5'-phosphorylation completely blocks enzymatic activity; (2) insensitivity to 3'-phosphorylation status; (3) processivity from 5' to 3' direction only, with no 3'-to-5' or endonuclease activity observed [gavin-2018-exonuclease-abstract]. The enzyme generates 3' mononucleotide products and operates optimally at acidic pH (5.0-5.5), consistent with its endolysosomal localization.

Importantly, PLD4 can degrade phosphorothioate-modified oligonucleotides, though approximately 20-50 times less efficiently than unmodified substrates [gavin-2018-exonuclease-abstract]. The enzyme cannot degrade A-type CpG oligodeoxynucleotides due to their secondary structure, which forms higher-order complexes that resist exonuclease attack. PLD3 demonstrates approximately 17-fold higher specific activity than PLD4 under comparable conditions and is more processive in RNA degradation [berouti-2024-tlr7-ligands-abstract].

### Historical Connection to Spleen Phosphodiesterase

The enzymatic properties of PLD4 are remarkably similar to "spleen phosphodiesterase" or "spleen acid exonuclease," an activity described in the biochemical literature for decades but whose molecular identity remained unknown. This classic enzyme was characterized as having a pH optimum of 5.5, being 5' single strand-specific, functioning as a non-processive nuclease, being inhibited by 5' phosphate, and generating 3' nucleotide monophosphate products [gavin-2018-exonuclease-abstract]. The striking correspondence between these properties and those of PLD3/PLD4 strongly suggests that one or both of these proteins represents the molecular identity of the long-studied spleen phosphodiesterase activity.

## Second Enzymatic Function: BMP Synthase Activity

### Discovery of BMP Synthase Activity

A breakthrough study in 2024 revealed an unexpected second enzymatic function for PLD4: the synthesis of bis(monoacylglycero)phosphate (BMP), also known as lysobisphosphatidic acid (LBPA), a peculiar phospholipid found almost exclusively in lysosomes [singh-2024-bmp-synthase-abstract]. BMP is required for proper degradation of glycosphingolipids, particularly gangliosides, and its unusual S,S-stereochemistry had long puzzled researchers regarding its biosynthetic origin.

### Mechanism of BMP Synthesis

PLD4 (and PLD3) catalyze the critical stereo-inversion reaction that converts R-configured precursors into S,S-BMP. The enzymes operate through a transphosphatidylation mechanism, using lysophosphatidylglycerol (lyso-PG) and monoacylglycerol (MAG) as substrates to perform glycerol exchange [singh-2024-bmp-synthase-abstract]. The reaction involves stereo-inversion of the glycerol backbone, converting the standard R configuration found in most glycerophospholipids to the unusual S configuration that characterizes lysosomal BMP. This S,S-configuration is crucial because it renders BMP resistant to degradation by lysosomal phospholipases, allowing the lipid to accumulate in the lysosomal membrane where it facilitates lipid catabolism.

Both purified PLD3 and PLD4 showed preference for S,R-lyso-PG compared with R,racemic-lyso-PG as substrates, though both stereoisomers could be utilized [singh-2024-bmp-synthase-abstract]. Importantly, the standard form of phosphatidylglycerol cannot serve directly as a substrate, indicating that upstream lipolytic enzymes such as PLA2G15 must first generate lyso-PG precursors.

### Physiological Consequences of BMP Deficiency

Deletion of PLD4 markedly reduced BMP levels in tissues where the enzyme is highly expressed, particularly the spleen (whereas PLD3 deletion affects brain BMP levels) [singh-2024-bmp-synthase-abstract]. The reduction in BMP leads to gangliosidosis and lysosomal abnormalities, as BMP is essential for the function of lipid-degrading enzymes that require the anionic phospholipid as a cofactor. Intralumenal vesicle (ILV) formation within lysosomes is compromised, cholesterol egress is impaired, and galectin-3 recruitment increases, indicating lysosomal membrane damage. Exogenous S,S-BMP supplementation can rescue ganglioside accumulation, demonstrating that BMP deficiency rather than indirect effects drives the pathology.

## Cellular Localization and Expression Pattern

### Subcellular Localization

PLD4 is synthesized as a type II transmembrane glycoprotein and localizes predominantly to endolysosomes [gavin-2018-exonuclease-abstract]. The protein contains an N-terminal cytosolic tail, followed by a transmembrane domain and a luminal catalytic domain. This topology places the exonuclease active site within the acidic lumen of late endosomes and lysosomes, where it can access internalized nucleic acids and participate in BMP synthesis. Studies using EGFP-tagged PLD4 have also detected the protein in the endoplasmic reticulum and Golgi complex, representing biosynthetic intermediates en route to the endolysosomal system.

### Tissue and Cell-Type Distribution

PLD4 expression is notably restricted compared to its paralog PLD3. According to the Human Protein Atlas, PLD4 shows highest tissue expression in brain white matter (42.2 nTPM), spinal cord (36.3 nTPM), and medulla oblongata (39.4 nTPM), followed by bone marrow (12.6 nTPM) and lymphoid tissues including lymph node, spleen, and tonsil (8.8-10.6 nTPM). At the cellular level, plasmacytoid dendritic cells (pDCs) show by far the highest expression (615.6 nCPM), followed by microglia (136.2 nCPM), conventional dendritic cells (41.9 nCPM), macrophages (38.6 nCPM), and B cells (16.0 nCPM).

The strong expression in dendritic cells, particularly pDCs, is functionally significant because these cells are primary sensors of nucleic acids via endosomal TLRs. The expression in microglia is consistent with PLD4's role in brain lipid homeostasis. The protein is detectable in blood plasma at approximately 2.6 micrograms per liter.

### Extracellular Distribution via Extracellular Vesicles

A recent discovery has revealed that PLD4, despite being primarily an intracellular endolysosomal enzyme, can be secreted extracellularly via extracellular vesicles (EVs) [betsuyaku-2025-extracellular-vesicles-abstract]. In human plasma, PLD4 circulates predominantly associated with EVs rather than as a soluble protein. Upon B cell activation through B cell receptor engagement and TLR9 agonist stimulation, PLD4 relocates from the Golgi apparatus to CD63-positive endosomes, which are the precursors of EVs. Activated B cells show increased multivesicular body formation and intraluminal vesicle accumulation, leading to release of PLD4-containing EVs. This finding establishes activated B cells as a key source of circulating PLD4 and suggests potential roles in intercellular communication and paracrine immune regulation that extend beyond the cell-autonomous functions previously characterized.

## Role in Immune Regulation

### Regulation of TLR9 Signaling

The primary immune function of PLD4 is to limit activation of Toll-like receptor 9 (TLR9), an endosomal receptor that recognizes unmethylated CpG-containing single-stranded DNA [gavin-2018-exonuclease-abstract]. By degrading ssDNA in endolysosomes, PLD4 prevents excessive or inappropriate TLR9 activation that would otherwise trigger inflammatory responses. PLD4-deficient mice develop an inflammatory disease characterized by elevated interferon-gamma (IFN-gamma), splenomegaly, and altered dendritic cell responses to TLR9 ligands [gavin-2018-exonuclease-abstract]. Critically, all pathological features in PLD4-deficient mice depend on TLR9, as genetic deletion of TLR9 rescues the phenotype.

### Regulation of TLR7 Signaling

PLD4 also regulates TLR7, the endosomal sensor of single-stranded RNA [gavin-2021-dna-rna-cleavage-abstract]. Recent work has shown that PLD4 and PLD3 cooperate with the endonuclease RNase T2 to generate the specific RNA ligands that activate TLR7 [berouti-2024-tlr7-ligands-abstract]. TLR7 contains two ligand-binding pockets: pocket 1 recognizes guanosine nucleosides (specifically 2',3'-cyclic GMP), while pocket 2 binds pyrimidine-rich RNA fragments. The PLD exonucleases are essential for generating ligands for both pockets. Together with RNase T2, PLD enzymes release 2',3'-cGMP for pocket 1. Conversely, PLD exonucleases tend to stall at cytidines, leaving pyrimidine-rich fragments suitable for pocket 2 [berouti-2024-tlr7-ligands-abstract].

### Functional Redundancy with PLD3

PLD4 and PLD3 show substantial functional redundancy in immune regulation. Single knockouts of either gene produce relatively mild phenotypes, but mice deficient in both PLD3 and PLD4 develop lethal hemophagocytic lymphohistiocytosis (HLH) characterized by inflammatory liver damage and massive overproduction of IFN-gamma early in life [gavin-2021-dna-rna-cleavage-abstract]. These double-knockout mice accumulate small single-stranded RNAs, and the pathology can be rescued by eliminating all endosomal TLR signaling, with partial rescue achieved by blocking either TLR7 or TLR9 individually.

## Disease Associations

### Monogenic Systemic Lupus Erythematosus

The most direct evidence linking PLD4 to human disease comes from the identification of loss-of-function mutations causing monogenic systemic lupus erythematosus (SLE) [wang-2025-sle-mutations-abstract]. Five patients carrying biallelic PLD4 mutations have been identified, all presenting with classic SLE features. The mutations impair single-stranded nucleic acid exonuclease activity and lead to excessive activation of TLR7 and TLR9. Downstream inflammatory signaling pathways, especially type I interferon signaling, are hyperactivated in patient dendritic cells. Mouse models lacking Pld4 recapitulate key features, including autoimmunity with cell-intrinsic expansion of plasmacytoid dendritic cells and plasma cells [wang-2025-sle-mutations-abstract].

Importantly, Pld4-deficient mice respond to the JAK inhibitor baricitinib, which blocks type I interferon signaling downstream of the JAK-STAT pathway [wang-2025-sle-mutations-abstract]. This finding suggests that targeting the interferon pathway may be a viable therapeutic strategy for patients with PLD4 deficiency, representing an example of genotype-directed personalized medicine in autoimmunity.

### Polygenic Autoimmune Disease Associations

Genome-wide association studies (GWAS) have linked common variants in PLD4 to susceptibility to multiple autoimmune diseases. The SNP rs2841277 in PLD4 was first identified as a susceptibility locus for systemic sclerosis in a Japanese population, with significant association (P = 0.00017) [terao-2013-systemic-sclerosis-abstract]. This same variant has been associated with rheumatoid arthritis in both Japanese and Taiwanese populations, where the minor allele C confers reduced risk (OR = 0.6, p = 3.0 x 10^-6) [chen-2017-rheumatoid-arthritis-abstract].

A meta-analysis of SLE genetics identified PLD4 as a genetic determinant of disease, with the risk allele associated with anti-dsDNA antibody production [akizuki-2019-sle-genetic-abstract]. Mouse studies in this work demonstrated that Pld4 mutant mice develop autoimmune phenotypes compatible with lupus, including splenomegaly, lymphadenopathy, and autoantibody production.

Interestingly, the association of PLD4 rs2841277 with systemic sclerosis was not replicated in a European American population, suggesting genetic heterogeneity between ancestral groups that may reflect different linkage disequilibrium patterns or gene-environment interactions.

### Neurodegenerative Disease Connections

While PLD3 has stronger associations with neurodegenerative diseases (particularly Alzheimer's disease), PLD4's role in BMP synthesis suggests potential relevance to brain health [singh-2024-bmp-synthase-abstract]. Disease-associated PLD3 mutations (including the V232M variant associated with Alzheimer's risk) reduce BMP synthesis by more than 50%, leading to ganglioside accumulation and lysosomal dysfunction. Given the functional overlap between PLD3 and PLD4, and PLD4's expression in microglia, it is plausible that PLD4 variants could also contribute to neurodegeneration, though this remains to be definitively established.

## Role in Microglial Function and Brain Development

### Early Characterization Studies

Before the discovery of PLD4's exonuclease activity in 2018, initial characterization studies in 2010 established PLD4 as a transmembrane glycoprotein with restricted expression in microglia and spleen [yoshikawa-2010-pld4-characterization-abstract]. Notably, these early studies could detect no phospholipase D activity despite the presence of HKD motifs, foreshadowing the later revelation that PLD4 catalyzes a completely different reaction. The protein was found to be heavily N-glycosylated, existing as approximately 70 kDa in glycosylated form versus 46 kDa after enzymatic deglycosylation. Expression was detected in Iba1-positive microglia in brain white matter during the first postnatal week, with peak expression at postnatal day 7, suggesting a role in early brain development.

### Involvement in Microglial Phagocytosis

Subsequent studies revealed that PLD4 participates in microglial phagocytic activity [otani-2011-microglial-phagocytosis-abstract]. In resting microglia, PLD4 localizes primarily to the nucleus, but upon stimulation with lipopolysaccharide (LPS), expression increases and the protein accumulates in early phagosomes during active phagocytosis. siRNA knockdown experiments in MG6 microglial cells demonstrated that reducing PLD4 expression significantly decreased the number of phagocytic cells and reduced overall phagocytic activity. These findings implicated PLD4 in microglial innate immune functions, though at the time, before its exonuclease activity was known, the mechanism remained unclear.

### Transient Role in Myelination

Studies using PLD4-deficient mice revealed an unexpected role in myelination during brain development [chiba-2016-myelination-abstract]. Wild-type microglia in early postnatal brain showed strong CD68 immunoreactivity (a marker of activated microglia), whereas PLD4-deficient microglia had weak CD68 signals, indicating that loss of PLD4 affects microglial activation state. More striking was the observation that PLD4-deficient mice exhibited a mild but significant delay in myelination in the cerebellum and corpus callosum at postnatal days 5 and 7. However, this difference disappeared by postnatal day 10, suggesting that microglia play a transient, PLD4-dependent role in supporting early myelination. The precise mechanism connecting PLD4 to myelination remains unclear but may involve microglial phagocytosis of myelin debris or secretion of factors that support oligodendrocyte maturation.

## Structural Biology

### Overall Architecture

The crystal structures of PLD4 reveal important insights into its function [yuan-2024-structure-abstract]. The protein forms an intra-chain pseudo-dimer structure, with two halves each containing an HKD motif coming together to form a single active site at their interface. This architecture is characteristic of the PLD superfamily and positions the two histidine residues for their sequential roles in the two-step catalytic mechanism.

The catalytic cavity is narrow and deep, with the oligonucleotide substrate entering almost vertically. The substrate bends into an L-shape at the phosphodiester bond between the 5' end and the second nucleotide, a conformation that appears important for product release. This substrate-capturing mechanism is distinctive among known nucleases.

### Structural Basis for Disease Mutations

Structural analysis of disease-associated mutations provides mechanistic insights into pathogenesis [yuan-2024-structure-abstract]. Mutations in the catalytic domain reduce enzymatic activity either by directly affecting the active site or by destabilizing the protein fold. These findings support a loss-of-function mechanism whereby reduced nucleic acid degradation leads to TLR hyperactivation and downstream inflammatory consequences.

### Recent Cryo-EM Structural Advances

More recent cryo-EM studies have captured additional catalytic states of PLD3 and PLD4, providing deeper mechanistic understanding [hirano-2025-cryoem-structure-abstract]. These structures reveal that the substrate-binding pocket is dynamic, with conformational changes in key loops (particularly the Phe335-containing loop in PLD3) depending on the substrate. The studies also captured metastable states that appear during substrate rearrangement following product release, illuminating the complete catalytic cycle of these endolysosomal exonucleases.

## Therapeutic Development and Biomarker Potential

### Small Molecule Modulators

The identification of PLD4 as an immunoregulatory enzyme has spurred interest in developing small molecule modulators for therapeutic applications [shirey-2021-pld4-modulators-abstract]. A high-throughput fluorescence enzymatic assay was developed to screen compound libraries for PLD3 and PLD4 modulators. Screening of 17,952 compounds identified both inhibitors and activators with selectivity for PLD4 over PLD3. These findings establish the feasibility of pharmacologically targeting PLD4 and provide chemical scaffolds for further development. Potential therapeutic applications span multiple areas: PLD4 inhibitors could enhance nucleic acid sensing for cancer immunotherapy or vaccine adjuvant effects, while PLD4 activators or gene therapy approaches could suppress excessive TLR activation in autoimmune diseases. A phase I clinical trial testing PLD4 inhibitors for systemic lupus erythematosus is reportedly ongoing in Japan, representing the first attempt to translate PLD4 biology into clinical application.

### PLD4 as a Cancer Biomarker

Beyond autoimmune diseases, PLD4 has emerged as a promising biomarker for blastic plasmacytoid dendritic cell neoplasm (BPDCN), a rare and aggressive hematological malignancy derived from plasmacytoid dendritic cell precursors. Given that pDCs express high levels of PLD4, this marker shows excellent diagnostic performance with 100% sensitivity and 83.3% specificity, outperforming the established CD123 marker. PLD4 expression remains consistently elevated across bone marrow, peripheral blood, and skin tissues in BPDCN patients, providing clear differentiation from other hematological malignancies. These findings suggest that PLD4 could serve both as a diagnostic marker and potentially as a therapeutic target for BPDCN.

## Open Questions

Several important questions remain regarding PLD4 biology:

1. **Relative contribution of exonuclease versus BMP synthase functions to disease**: The dual enzymatic activities of PLD4 raise the question of which function is more critical in different pathological contexts. For autoimmune diseases, the exonuclease activity appears paramount, but the relative contributions to lysosomal storage phenotypes require further investigation.

2. **Mechanism of dual activity**: How a single protein catalyzes two biochemically distinct reactions (phosphodiester bond hydrolysis in nucleic acids versus transphosphatidylation in lipids) using the same active site residues remains incompletely understood. Structural studies of PLD4 with lipid substrates would be informative.

3. **Tissue-specific compensation between PLD3 and PLD4**: Why does PLD3 dominate BMP synthesis in brain while PLD4 dominates in spleen? The mechanisms underlying tissue-specific functional dominance despite structural similarity are unclear.

4. **Therapeutic targeting**: Could modulation of PLD4 activity provide therapeutic benefit in autoimmune disease (by enhancing activity) or cancer immunotherapy (by reducing activity to potentiate nucleic acid sensing)? Small molecule modulators of PLD4 have been identified in high-throughput screens but their therapeutic potential remains to be explored.

5. **Role in other cell types**: While pDCs and microglia express high levels of PLD4, the function of PLD4 in other cell types expressing lower levels remains poorly characterized.

6. **Evolutionary conservation**: Understanding when and how PLD4 diverged from PLD3 and whether organisms lacking PLD4 have alternative mechanisms for the same functions could provide additional insights into its essential roles.

## References

- [gavin-2018-exonuclease-abstract] Gavin AL, Huang D, Huber C, et al. PLD3 and PLD4 are single-stranded acid exonucleases that regulate endosomal nucleic-acid sensing. Nat Immunol. 2018;19(9):942-953. PMID: 30111894. DOI: 10.1038/s41590-018-0179-y

- [singh-2024-bmp-synthase-abstract] Singh S, Dransfeld UE, Ambaw YA, et al. PLD3 and PLD4 synthesize S,S-BMP, a key phospholipid enabling lipid degradation in lysosomes. Cell. 2024;187(24):6820-6834.e24. PMID: 39423811. DOI: 10.1016/j.cell.2024.09.036

- [yuan-2024-structure-abstract] Yuan M, Peng L, Huang D, et al. Structural and mechanistic insights into disease-associated endolysosomal exonucleases PLD3 and PLD4. Structure. 2024;32(6):766-779.e7. PMID: 38537643. DOI: 10.1016/j.str.2024.02.019

- [gavin-2021-dna-rna-cleavage-abstract] Gavin AL, Huang D, Blane TR, et al. Cleavage of DNA and RNA by PLD3 and PLD4 limits autoinflammatory triggering by multiple sensors. Nat Commun. 2021;12(1):5874. PMID: 34620855. DOI: 10.1038/s41467-021-26150-w

- [wang-2025-sle-mutations-abstract] Wang Q, Zhu H, Sun X, et al. Loss-of-function mutations in PLD4 lead to systemic lupus erythematosus. Nature. 2025;647(8089):498-505. PMID: 40931063. DOI: 10.1038/s41586-025-09513-x

- [terao-2013-systemic-sclerosis-abstract] Terao C, Ohmura K, Kawaguchi Y, et al. PLD4 as a novel susceptibility gene for systemic sclerosis in a Japanese population. Arthritis Rheum. 2013;65(2):472-480. PMID: 23124809. DOI: 10.1002/art.37777

- [berouti-2024-tlr7-ligands-abstract] Bérouti M, Lammens K, Heiss M, et al. Lysosomal endonuclease RNase T2 and PLD exonucleases cooperatively generate RNA ligands for TLR7 activation. Immunity. 2024;57(7):1482-1496.e8. PMID: 38697119. DOI: 10.1016/j.immuni.2024.04.010

- [akizuki-2019-sle-genetic-abstract] Akizuki S, Ishigaki K, Kochi Y, et al. PLD4 is a genetic determinant to systemic lupus erythematosus and involved in murine autoimmune phenotypes. Ann Rheum Dis. 2019;78(4):509-518. PMID: 30679154. DOI: 10.1136/annrheumdis-2018-214116

- [chen-2017-rheumatoid-arthritis-abstract] Chen WC, Wang WC, Okada Y, et al. rs2841277 (PLD4) is associated with susceptibility and rs4672495 is associated with disease activity in rheumatoid arthritis. Oncotarget. 2017;8(38):64180-64190. PMID: 28969061. DOI: 10.18632/oncotarget.19419

- [yoshikawa-2010-pld4-characterization-abstract] Yoshikawa F, Banno Y, Otani Y, et al. Phospholipase D Family Member 4, a Transmembrane Glycoprotein with No Phospholipase D Activity, Expression in Spleen and Early Postnatal Microglia. PLoS ONE. 2010;5(11):e13932. PMID: 21085684. DOI: 10.1371/journal.pone.0013932

- [otani-2011-microglial-phagocytosis-abstract] Otani Y, Yamaguchi Y, Sato Y, et al. PLD4 is involved in phagocytosis of microglia: expression and localization changes of PLD4 are correlated with activation state of microglia. PLoS ONE. 2011;6(11):e27544. PMID: 22102906. DOI: 10.1371/journal.pone.0027544

- [chiba-2016-myelination-abstract] Chiba T, Otani Y, Yamaguchi Y, et al. Microglial phospholipase D4 deficiency influences myelination during brain development. Proc Jpn Acad Ser B Phys Biol Sci. 2016;92(7):237-254. PMID: 27477458. DOI: 10.2183/pjab.92.237

- [shirey-2021-pld4-modulators-abstract] Shirey RJ, Turner LD, Lairson LL, Janda KD. Modulators of immunoregulatory exonucleases PLD3 and PLD4 identified by high-throughput screen. Bioorg Med Chem Lett. 2021;49:128293. PMID: 34332037. DOI: 10.1016/j.bmcl.2021.128293

- [hirano-2025-cryoem-structure-abstract] Hirano Y, Ezaki W, Sato R, et al. Mechanistic insights into single-stranded DNA degradation by lysosomal exonucleases PLD3 and PLD4 from structural snapshots. Nat Commun. 2025;16:11431. DOI: 10.1038/s41467-025-66261-2

- [betsuyaku-2025-extracellular-vesicles-abstract] Betsuyaku T, Akizuki S, Liu Y, Morinobu A. Activated human B cells produce phospholipase D4-containing extracellular vesicles. PLoS ONE. 2025. DOI: 10.1371/journal.pone.0329832


## Citations

1. akizuki-2019-sle-genetic-abstract.md
2. berouti-2024-tlr7-ligands-abstract.md
3. betsuyaku-2025-extracellular-vesicles-abstract.md
4. chen-2017-rheumatoid-arthritis-abstract.md
5. chiba-2016-myelination-abstract.md
6. gavin-2018-exonuclease-abstract.md
7. gavin-2018-exonuclease-summary.md
8. gavin-2021-dna-rna-cleavage-abstract.md
9. hirano-2025-cryoem-structure-abstract.md
10. otani-2011-microglial-phagocytosis-abstract.md
11. shirey-2021-pld4-modulators-abstract.md
12. singh-2024-bmp-synthase-abstract.md
13. singh-2024-bmp-synthase-summary.md
14. terao-2013-systemic-sclerosis-abstract.md
15. wang-2025-sle-mutations-abstract.md
16. wang-2025-sle-mutations-summary.md
17. yoshikawa-2010-pld4-characterization-abstract.md
18. yuan-2024-structure-abstract.md