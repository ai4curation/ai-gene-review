---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T21:24:29.639086'
end_time: '2026-01-22T21:46:12.926290'
duration_seconds: 1303.29
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: KIAA1614
  gene_symbol: KIAA1614
  uniprot_accession: Q5VZ46
  protein_description: 'RecName: Full=Uncharacterized protein KIAA1614;'
  gene_info: Name=KIAA1614;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: DUF4685. (IPR032756); PAR6_homolog. (IPR051741); DUF4685 (PF15737)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 12
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q5VZ46
- **Protein Description:** RecName: Full=Uncharacterized protein KIAA1614;
- **Gene Information:** Name=KIAA1614;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DUF4685. (IPR032756); PAR6_homolog. (IPR051741); DUF4685 (PF15737)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KIAA1614" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KIAA1614' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KIAA1614** (gene ID: KIAA1614, UniProt: Q5VZ46) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KIAA1614: An Uncharacterized Human Protein with Predicted Roles in Cell Polarity and Centrosome Function

## Introduction and Overview

KIAA1614 (UniProt: Q5VZ46, NCBI Gene ID: 57710) is a human protein-coding gene located on chromosome 1q25.3 that encodes an uncharacterized protein of 1,190 amino acids. Despite being identified more than two decades ago as part of the Kazusa cDNA project, the precise molecular function of KIAA1614 remains experimentally undefined [nagase-2000-kiaa-cloning-abstract]. The protein is annotated as "uncharacterized" in major databases including UniProt and NCBI, reflecting the current state of limited experimental characterization. However, computational analyses and high-throughput studies have provided insights that suggest KIAA1614 may function in cell polarity establishment, centrosome biology, and potentially protein kinase C signaling pathways [ncbi-gene-summary][human-protein-atlas-summary].

The KIAA naming convention derives from the Kazusa DNA Research Institute's systematic effort to clone and sequence unidentified human cDNAs, particularly those encoding large proteins from brain tissue. KIAA1614 was among 100 cDNAs (KIAA1544-KIAA1643) sequenced by Nagase and colleagues in 2000 from human adult and fetal brain cDNA libraries [nagase-2000-kiaa-cloning-abstract]. This origin from brain tissue provides early evidence of neuronal expression, a pattern that has been confirmed by subsequent expression profiling studies.

## Gene and Protein Structure

The KIAA1614 gene spans approximately 39 kilobases on chromosome 1q25.3 and contains 9 exons [ncbi-gene-summary]. The gene produces a validated transcript that encodes a 1,190 amino acid protein. The RefSeq database lists two validated protein isoforms: NP_066001.1 (isoform 2) and NP_001414570.1 (isoform 1), suggesting the existence of alternative splicing [ncbi-gene-summary].

Domain analysis reveals that KIAA1614 contains two annotated protein domains. The first is DUF4685 (Domain of Unknown Function 4685; InterPro: IPR032756; Pfam: PF15737), a conserved domain whose biochemical function has not been experimentally determined. Domains of Unknown Function represent a substantial fraction of the Pfam database, comprising over 22% of known protein families as of 2019. While their sequences are evolutionarily conserved across species—indicating biological importance—their specific roles often remain undefined until targeted experimental studies are conducted [uniprot-q5vz46-summary].

The second annotated domain is designated PAR6_homolog (InterPro: IPR051741), which bears sequence similarity to the partitioning defective 6 (PAR6) family of cell polarity proteins. The canonical PAR6 proteins are well-characterized adaptor molecules that contain a PDZ domain and a CRIB-like (Cdc42/Rac interactive binding) motif, enabling them to simultaneously interact with GTP-bound Rac and Cdc42 small GTPases and with atypical protein kinase C (aPKC) isoforms [noda-2001-par6-abstract]. The presence of a PAR6 homolog domain in KIAA1614 suggests potential involvement in cell polarity pathways, though the extent of functional similarity between KIAA1614 and canonical PAR6 proteins requires experimental validation.

## Predicted Molecular Function

In the absence of direct experimental characterization, the predicted molecular function of KIAA1614 derives from computational analyses including sequence homology, domain architecture, and coexpression networks. Gene Ontology annotations based on electronic annotation (IEA evidence code) suggest involvement in several biological processes [ncbi-gene-summary][human-protein-atlas-summary]:

The protein is predicted to participate in the centrosome cycle, which encompasses the duplication, maturation, and separation of centrosomes during cell division. This prediction aligns with the presence of the PAR6 homolog domain, as PAR6 proteins localize to centrosomes in mammalian cells. Studies have shown that Par6γ localizes specifically to the mother centriole and controls centrosomal protein composition through a Par6α-dependent pathway, with depletion resulting in defects in ciliogenesis, microtubule organization, and centrosome reorientation during cell migration.

KIAA1614 is also predicted to function in the establishment or maintenance of cell polarity, a fundamental process in epithelial tissues, neurons, and dividing cells. The Par3-Par6-aPKC complex represents a master regulator of cell polarity across metazoans, from C. elegans embryonic asymmetric division to mammalian epithelial apico-basal polarity. The PAR6 homolog domain in KIAA1614 raises the possibility that this protein may participate in polarity-related signaling, potentially through interactions with aPKC or small GTPases.

Additionally, Gene Ontology annotations predict protein kinase C (PKC) binding activity for KIAA1614 [human-protein-atlas-summary]. This is particularly intriguing given that canonical PAR6 proteins bind to atypical PKC isoforms (PKCι/λ and PKCζ) through their N-terminal PB1 domain. If KIAA1614 possesses PKC binding capability, it could function as a scaffold or regulatory protein in PKC-mediated signaling pathways.

## Subcellular Localization

Computational predictions and limited experimental data indicate that KIAA1614 localizes to multiple cellular compartments [ncbi-gene-summary][human-protein-atlas-summary]. Gene Ontology annotations predict localization to the apical plasma membrane, cell cortex, and nucleus. These predictions are consistent with the proposed roles in cell polarity, as polarity proteins characteristically localize to specific cortical domains.

The Human Protein Atlas provides experimental immunocytochemistry data suggesting that KIAA1614 localizes to the nuclear membrane and vesicles [human-protein-atlas-summary]. This experimental observation of nuclear membrane localization is noteworthy, as the nuclear envelope represents a specialized membrane system with distinct protein composition. Vesicular localization could indicate involvement in membrane trafficking pathways, which are intimately connected to cell polarity through the targeted delivery of polarity determinants.

The dual nuclear and cytoplasmic distribution observed in most tissues by the Human Protein Atlas suggests that KIAA1614 may shuttle between these compartments or perform distinct functions in different cellular contexts. Nuclear-cytoplasmic shuttling is a common regulatory mechanism for signaling molecules.

## Expression Profile and Tissue Distribution

KIAA1614 exhibits ubiquitous expression across human tissues but shows enhanced expression in specific cell types [human-protein-atlas-summary][ncbi-gene-summary]. At the tissue level, the highest RNA expression is observed in the retina (27.3 nTPM), followed by cerebellum (17.7 nTPM), with notable expression also in heart muscle, urinary bladder, and endometrium. The enhanced retinal expression is particularly striking when examined at single-cell resolution.

Single-cell RNA sequencing data from the Human Protein Atlas reveals that rod photoreceptor cells show the highest expression of KIAA1614 among all human cell types, with 139.4 normalized counts per million (nCPM) [human-protein-atlas-summary]. Cone photoreceptor cells (95.2 nCPM) and retinal bipolar cells (77.2 nCPM) also show elevated expression. This pattern of high expression across multiple retinal cell types suggests that KIAA1614 may play a specialized role in the retina, potentially related to the highly polarized structure of photoreceptor cells or the unique functional demands of visual processing.

Within the brain, KIAA1614 shows low regional specificity but has highest expression in the cerebellum (33.2 nTPM). The cerebellum is notable for containing the most abundant neuronal type in the human body—the granule cells—which exhibit highly polarized morphology with distinct axonal and dendritic compartments. Expression clustering analysis suggested involvement in nucleosome-related functions, though this computational prediction requires experimental validation [human-protein-atlas-summary].

At the immune cell level, overexpression has been noted in CD4 T cells, NK cells, and T lymphocytes [ncbi-gene-summary], potentially indicating a role in immune cell biology, though this has not been functionally characterized.

## Protein-Protein Interactions

The only experimentally validated protein-protein interaction for KIAA1614 documented in major interaction databases is with neuroglobin (NGB), identified through affinity capture-mass spectrometry [vanacker-2019-neuroglobin-abstract][biogrid-kiaa1614-summary]. This interaction was discovered in a proteomics study by Van Acker and colleagues investigating the neuroglobin interactome in SH-SY5Y neuroblastoma cells under normal and ferroptotic stress conditions.

Neuroglobin is a heme protein expressed predominantly in neurons that provides neuroprotection against various cellular stressors, including conditions that promote ferroptosis—an iron-dependent form of cell death characterized by lipid peroxide accumulation [vanacker-2019-neuroglobin-abstract]. The Van Acker study found that NGB-expressing neuroblastoma cells showed significantly increased resistance to ferroptosis induction. KIAA1614 was identified among the proteins that co-immunoprecipitated with NGB, though the functional significance of this interaction was not specifically characterized in the study.

The biological relevance of the NGB-KIAA1614 interaction remains unclear. Both proteins are expressed in neural tissues, raising the possibility of physiological relevance. However, this interaction was detected in a high-throughput screen and appeared in only one of two experimental replicates, warranting cautious interpretation until confirmed by targeted studies. The observation that NGB interacts with proteins involved in iron metabolism, cell death pathways, and DNA repair suggests that its interactome may be complex and condition-dependent [vanacker-2019-neuroglobin-abstract].

## Evolutionary Conservation and Paralogs

KIAA1614 orthologs are found across mammals, with conservation documented in chimpanzee, Rhesus monkey, dog, cow, mouse, and rat [ncbi-gene-summary]. A broader analysis identified orthologs in 177 organisms, indicating substantial evolutionary conservation of this gene across the animal kingdom. Such conservation typically implies functional importance, though it does not necessarily reveal what that function is.

The most significant paralog of KIAA1614 is SYNJ2BP (Synaptojanin 2 Binding Protein), an outer mitochondrial membrane protein with a cytosolic PDZ domain [ncbi-gene-summary]. SYNJ2BP functions as a cellular signaling hub through its PDZ domain, which mediates interactions with multiple partners including synaptojanin 2 (SYNJ2), the cell adhesion molecule TMIGD1, and activin type 2 receptor kinases. SYNJ2BP plays important roles in localizing specific mRNAs to mitochondria and in regulating mitochondrial-ER contact sites.

The paralogous relationship between KIAA1614 and SYNJ2BP suggests possible shared ancestry and potentially related functions. Both proteins may function as adaptor or scaffolding molecules that organize signaling complexes at specific subcellular locations. However, SYNJ2BP is considerably smaller (206 amino acids versus 1,190 amino acids for KIAA1614) and has distinct domain architecture, indicating substantial divergence in their precise molecular functions.

## Disease Associations and Clinical Studies

Disease associations for KIAA1614 are currently limited to computational predictions, text-mining approaches, and emerging transcriptomic studies rather than robust genetic evidence. The DISEASES database indicates an association with Fanconi anemia complementation group E based on text mining of biomedical literature, though the confidence level and mechanistic basis for this association are unclear [ncbi-gene-summary].

### Cancer Associations

The Human Protein Atlas has identified KIAA1614 as a prognostic marker in several cancers, including glioblastoma multiforme, kidney renal clear cell carcinoma, and rectal adenocarcinoma [human-protein-atlas-summary]. The COSMIC (Catalogue of Somatic Mutations in Cancer) database documents somatic mutations in KIAA1614 across multiple tumor types, though mouse insertional mutagenesis experiments do not support the designation of KIAA1614 as a cancer-causing gene. These prognostic associations likely reflect correlations between KIAA1614 expression levels and patient outcomes rather than causal relationships. Nevertheless, the associations in multiple cancer types suggest that KIAA1614 expression may influence tumor biology, potentially through its predicted roles in cell polarity and centrosome function—both processes frequently dysregulated in cancer.

Supporting this cancer association, a multi-omics integration study of glioma using TCGA data identified KIAA1614 as one of several novel biomarkers "likely helpful in both diagnosis and prognosis" of glioma [bhatnagar-2023-glioma-biomarkers-abstract]. This preprint study used sparse canonical correlation analysis to integrate mRNA, DNA methylation, and miRNA data to discriminate between glioblastoma and lower-grade gliomas. While KIAA1614 was listed among the biomarker candidates alongside genes like PPP1R8, GPBP1L1, and CD300A, no specific mechanistic insight into its role in glioma biology was provided. The identification of KIAA1614 as a glioma biomarker is consistent with its high expression in brain tissue, particularly the cerebellum, and its predicted functions in cell polarity—a process frequently disrupted in cancer.

A case-control study examining KIAA gene variants in breast cancer in a Chinese population analyzed the synonymous SNP rs3795504 in KIAA1614 [pang-2021-kiaa-breast-cancer-abstract]. This variant showed no statistically significant association with breast cancer risk (OR: 1.14, 95% CI: 0.98–1.31, P=0.084), suggesting that common variation in KIAA1614 does not substantially contribute to breast cancer susceptibility in this population.

### CRISPR Screen Data

The BioGRID ORCS database documents that KIAA1614 has been identified in 35 hits across 1,396 genome-wide CRISPR screens [biogrid-orcs-summary]. While this indicates the gene has been captured in various functional genomic screens, the specific phenotypes and cell fitness effects across different cell lines require further investigation. The DepMap (Cancer Dependency Map) project, which systematically identifies genes required for cancer cell fitness, has data on KIAA1614 dependency scores, though the gene does not appear to be classified as a core essential gene or a strong cancer dependency based on available summaries.

### COVID-19 Gene Expression Signature

A notable finding emerged from COVID-19 transcriptomic research. Zhang and colleagues identified KIAA1614 as one of five critical genes (along with ABCB6, MND1, SMG1, and RIPK3) that form a predictive signature for COVID-19 status in blood samples [zhang-2022-covid-genomic-abstract]. Using max-linear logistic regression analysis of 126 blood samples, this five-gene classifier achieved 100% sensitivity and specificity in distinguishing COVID-19 patients from healthy controls.

KIAA1614 appears in multiple COVID-19 patient subtypes defined by gene expression patterns. Notably, patients in subtype I—characterized by KIAA1614 involvement along with negative SMG1 expression—showed higher ICU admission rates compared to subtype II patients. In the statistical model, KIAA1614 had substantial coefficients (+3.4153 in one competing factor model, -0.4620 in another), and its expression correlated with SMG1 (r = 0.5948). ABCB6 expression positively correlates with KIAA1614 expression, suggesting coordinated regulation of these genes during infection.

The authors suggested that KIAA1614, despite being uncharacterized, "could be fundamental" to understanding COVID-19 pathophysiology and warrants focused investigation for vaccine and therapeutic development [zhang-2022-covid-genomic-abstract]. However, subsequent research analyzing gene expression from nasopharyngeal/oropharyngeal swab samples found that these five critical genes no longer played a decisive role, suggesting that genes functionally associated with SARS-CoV-2 infection may differ from genes associated with COVID-19 disease pathology. The biological mechanism by which KIAA1614 contributes to COVID-19 outcomes remains unknown and represents an intriguing avenue for future investigation.

### Genetic Variation Studies

KIAA family genes broadly have been implicated in various complex diseases through genetic association studies. Polymorphisms in KIAA genes have drawn attention in the context of cancers, diabetes, autoimmune diseases, and cardiac disease. However, specific robust GWAS findings implicating KIAA1614 SNPs in disease risk appear limited in the current literature [pang-2021-kiaa-breast-cancer-abstract].

## Open Questions

Despite the availability of extensive computational predictions, several fundamental questions about KIAA1614 remain unanswered and represent priorities for future investigation:

**What is the primary molecular function of KIAA1614?** The protein is annotated as "uncharacterized" because no biochemical activity has been experimentally demonstrated. Is it an enzyme, a scaffolding protein, a regulatory adaptor, or something else entirely? The predicted PKC binding activity requires experimental validation.

**What is the functional significance of the PAR6 homolog domain?** Does KIAA1614 participate in the same cell polarity pathways as canonical PAR6 proteins? Does it interact with atypical PKC, Cdc42/Rac GTPases, or other known polarity components? The extent of functional overlap with PAR6 family members needs to be determined.

**Why is KIAA1614 highly expressed in photoreceptor cells?** The striking enrichment in rod and cone photoreceptors suggests a specialized function in these highly polarized cells. Does KIAA1614 contribute to photoreceptor development, maintenance, or function? Are there retinal phenotypes in knockout animal models?

**What is the biological significance of the neuroglobin interaction?** The Van Acker study identified KIAA1614 as a potential NGB interactor, but the functional relevance of this interaction remains unexplored. Does KIAA1614 modulate NGB's neuroprotective function or participate in ferroptosis regulation?

**What is the function of the DUF4685 domain?** This domain is present in KIAA1614 and presumably in other proteins, yet its biochemical function is unknown. Structural biology and comparative genomics approaches may help elucidate its role.

**Does KIAA1614 localize to centrosomes?** The predicted involvement in centrosome biology should be testable through localization studies in cycling cells. If confirmed, what role does it play—structural, regulatory, or both?

**What is the mechanistic basis for KIAA1614's association with COVID-19 severity?** The identification of KIAA1614 as one of five critical genes in a COVID-19 transcriptomic signature raises intriguing questions about its potential role in immune responses or viral pathogenesis. Does KIAA1614 expression change during viral infection, and if so, through what mechanism? Is this association with COVID-19 severity direct or does it reflect broader dysregulation of cell polarity or other pathways during severe disease?

**What are the phenotypes of KIAA1614 knockout in model organisms?** While the gene is conserved across vertebrates, no phenotype data from targeted knockouts appears to be publicly available. Generation and phenotyping of KIAA1614 knockout mice through resources like IMPC would provide critical insights into the gene's physiological functions.

Addressing these questions will require targeted experimental approaches including protein interaction studies (co-immunoprecipitation, proximity labeling), localization studies (live cell imaging, immunofluorescence), functional studies (knockout/knockdown phenotypes in cell culture and animal models), and structural characterization. The high expression in retina makes this tissue and photoreceptor cell culture models particularly attractive systems for investigating KIAA1614 function. The unexpected connection to COVID-19 severity also suggests that immune cell models may be informative for understanding KIAA1614 biology.

## References

1. **[nagase-2000-kiaa-cloning-abstract]** Nagase T, Kikuno R, Nakayama M, Hirosawa M, Ohara O. Prediction of the coding sequences of unidentified human genes. XVIII. The complete sequences of 100 new cDNA clones from brain which code for large proteins in vitro. DNA Res. 2000 Aug 31;7(4):273-81. PMID: 10997877. DOI: 10.1093/dnares/7.4.271. https://pubmed.ncbi.nlm.nih.gov/10997877/

2. **[vanacker-2019-neuroglobin-abstract]** Van Acker ZP, Van Raemdonck GA, Logie E, Van Acker SI, Baggerman G, Vanden Berghe W, Ponsaerts P, Dewilde S. Connecting the Dots in the Neuroglobin-Protein Interaction Network of an Unstressed and Ferroptotic Cell Death Neuroblastoma Model. Cells. 2019 Aug 11;8(8):873. PMID: 31405213. PMCID: PMC6721670. DOI: 10.3390/cells8080873. https://pubmed.ncbi.nlm.nih.gov/31405213/

3. **[khambata-ford-2003-promoters-abstract]** Khambata-Ford S, Liu Y, Gleason C, Dickson M, Altman RB, Batzoglou S, Myers RM. Identification of promoter regions in the human genome by using a retroviral plasmid library-based functional reporter gene assay. Genome Res. 2003 Jul;13(7):1765-74. PMID: 12805274. PMCID: PMC403750. DOI: 10.1101/gr.529803. https://pubmed.ncbi.nlm.nih.gov/12805274/

4. **[noda-2001-par6-abstract]** Noda Y, Takeya R, Ohno S, Naito S, Ito T, Sumimoto H. Human homologues of the Caenorhabditis elegans cell polarity protein PAR6 as an adaptor that links the small GTPases Rac and Cdc42 to atypical protein kinase C. Genes Cells. 2001 Feb;6(2):107-19. PMID: 11260256. DOI: 10.1046/j.1365-2443.2001.00404.x. https://pubmed.ncbi.nlm.nih.gov/11260256/

5. **[ncbi-gene-summary]** NCBI Gene Database. KIAA1614 KIAA1614 [Homo sapiens (human)]. Gene ID: 57710. https://www.ncbi.nlm.nih.gov/gene/57710

6. **[human-protein-atlas-summary]** Human Protein Atlas. KIAA1614 protein expression summary. Ensembl: ENSG00000135835. https://www.proteinatlas.org/ENSG00000135835-KIAA1614

7. **[biogrid-kiaa1614-summary]** BioGRID Database. NGB - KIAA1614 Interaction Summary. Interaction ID: 2756644. https://thebiogrid.org/interaction/2756644

8. **[uniprot-q5vz46-summary]** UniProt Consortium. UniProtKB entry Q5VZ46 - Uncharacterized protein KIAA1614 - Homo sapiens (Human). https://www.uniprot.org/uniprotkb/Q5VZ46

9. **[zhang-2022-covid-genomic-abstract]** Zhang Z, Guo L, Huang L, Deng Q, et al. The Existence of At Least Three Genomic Signature Patterns and At Least Seven Subtypes of COVID-19 and the End of the Disease. J Data Sci. 2022 Apr;20(2):145-167. PMID: 35529157. PMCID: PMC9146581. DOI: 10.6339/22-JDS1040. https://pmc.ncbi.nlm.nih.gov/articles/PMC9146581/

10. **[pang-2021-kiaa-breast-cancer-abstract]** Pang H, Zhao Y, Qin Z, Xu X, Ren Q, Song T, Li J, Zhu F, Liu D, Zhong Y. Potential functional variants of KIAA genes are associated with breast cancer risk in a case control study. Ann Transl Med. 2021 May;9(9):764. PMID: 34012873. PMCID: PMC8105804. DOI: 10.21037/atm-20-8028. https://pmc.ncbi.nlm.nih.gov/articles/PMC8105804/

11. **[bhatnagar-2023-glioma-biomarkers-abstract]** Bhatnagar R, et al. Integration of Multi-omics Data for the Classification of Glioma Types and Identification of Novel Biomarkers. bioRxiv. 2023 Dec 22. DOI: 10.1101/2023.12.22.572983. https://www.biorxiv.org/content/10.1101/2023.12.22.572983v1 (Preprint)

12. **[biogrid-orcs-summary]** BioGRID ORCS Database. KIAA1614 CRISPR Screens (Homo sapiens). Gene ID: 57710. https://orcs.thebiogrid.org/Gene/57710


## Citations

1. bhatnagar-2023-glioma-biomarkers-abstract.md
2. biogrid-kiaa1614-summary.md
3. biogrid-orcs-summary.md
4. human-protein-atlas-summary.md
5. khambata-ford-2003-promoters-abstract.md
6. nagase-2000-kiaa-cloning-abstract.md
7. ncbi-gene-summary.md
8. noda-2001-par6-abstract.md
9. pang-2021-kiaa-breast-cancer-abstract.md
10. uniprot-q5vz46-summary.md
11. vanacker-2019-neuroglobin-abstract.md
12. zhang-2022-covid-genomic-abstract.md